"""Project lifecycle workflow.

Each API has a distinct ``provision_type`` in api_config.API_CONFIG.
The top-level ``ensure_project_with_api`` dispatches to the matching
``_provision_*`` function so that every API's portal flow is explicit
and self-contained — no shared flags or generic branching.
"""
from __future__ import annotations

import json
from pathlib import Path

from loguru import logger

from app.models import AppConfig, ProjectSpec
from providers.mastercard.api_config import API_CONFIG
from providers.mastercard.pages.create_project_page import CreateProjectPage
from providers.mastercard.pages.dashboard_page import DashboardPage
from providers.mastercard.pages.project_page import AddProjectKeyPage, OAuth2SandboxPage, SandboxPage
from providers.mastercard.selectors import API_SLUGS, CreateProjectSelectors, OAuth2SandboxSelectors


def _key_alias(api_name: str) -> str:
    """Portal requires key alias to be 8-75 chars. Pad short names with '-signing'."""
    alias = api_name if len(api_name) >= 8 else f"{api_name}-signing"
    return alias[:75]


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

async def _capture_consumer_key(
    page,
    uuid: str,
    dest_dir: Path,
    project: ProjectSpec,
    api_name: str,
    alias: str | None,
    *,
    retries: int = 4,
    retry_delay_s: float = 4.0,
) -> Path | None:
    """Return to sandbox and write a credentials.json with the consumer key for OAuth 1.0a.

    Retries up to ``retries`` times with a page reload between attempts — newly-created
    projects occasionally take a few seconds for the portal to populate key rows.
    """
    import asyncio as _asyncio
    sandbox = SandboxPage(page)
    await sandbox.goto(uuid)
    consumer_key: str | None = None
    for attempt in range(1, retries + 1):
        consumer_key = await sandbox.extract_consumer_key(alias=alias)
        if consumer_key:
            break
        if attempt < retries:
            logger.info(
                "Key rows not yet visible for {}/{} (attempt {}/{}) — waiting {:.0f}s then reloading…",
                project.name, api_name, attempt, retries, retry_delay_s,
            )
            await _asyncio.sleep(retry_delay_s)
            await page.reload(wait_until="domcontentloaded")
            try:
                await page.wait_for_load_state("networkidle", timeout=5000)
            except Exception:
                pass
            await _asyncio.sleep(2)

    if not consumer_key:
        logger.warning("No consumer key captured for {}/{} after {} attempts", project.name, api_name, retries)
        return None
    creds = {"consumer_key": consumer_key, "key_alias": alias}
    dest = dest_dir / f"{project.name}-{api_name}-credentials.json"
    dest.write_text(json.dumps(creds, indent=2))
    logger.info("Saved OAuth 1.0a credentials JSON: {}", dest)
    return dest


async def _add_oauth_signing_key_via_sandbox(
    page,
    uuid: str,
    dest_dir: Path,
    project: ProjectSpec,
    api_name: str,
    alias: str,
    config: AppConfig,
) -> list[Path]:
    """
    Add an OAuth 1.0a signing key via the sandbox 'Add project key' flow.
    Used when the wizard only downloads an encryption .pem, not a signing key.
    Returns [credentials_json, key_zip].
    """
    sandbox = SandboxPage(page)
    await sandbox.goto(uuid)

    if not await sandbox.has_oauth1_key_section():
        logger.warning("Project {!r} has no OAuth 1.0a section — cannot add signing key", project.name)
        return []

    logger.info("Adding OAuth 1.0a signing key to project {!r} ({})", project.name, api_name)
    await sandbox.click_add_project_key()

    add_key_page = AddProjectKeyPage(page)
    await add_key_page.wait_for_form()
    await add_key_page.select_generate_new()
    await add_key_page.proceed()
    await add_key_page.fill_credentials(alias=alias, password=config.key_password)
    await add_key_page.create_key()
    key_zip = await add_key_page.download_key_file(
        dest_dir=dest_dir, filename_hint=f"{project.name}-{api_name}-signing"
    )
    logger.info("OAuth signing key downloaded: {}", key_zip)
    creds_file = await _capture_consumer_key(page, uuid, dest_dir, project, api_name, alias=alias)
    return [creds_file, key_zip] if creds_file else [key_zip]


async def _get_uuid_after_creation(page, dashboard: DashboardPage, portal_name: str) -> str | None:
    """Extract project UUID from URL, or look it up on the dashboard."""
    if "/project-details/" in page.url:
        return page.url.split("/project-details/")[-1].split("/")[0]
    await dashboard.goto()
    return await dashboard.get_project_uuid(portal_name)


# ---------------------------------------------------------------------------
# Per-provision-type functions
# ---------------------------------------------------------------------------

async def _provision_oauth1_standard(
    page, dashboard: DashboardPage, portal_name: str,
    dest_dir: Path, project: ProjectSpec, api_name: str,
    alias: str, config: AppConfig,
    api_selection: str | tuple[str, ...] | None = None,
) -> list[Path]:
    """
    Standard OAuth 1.0a flow:
      Step 1 (name form) → Proceed → Step 2 (alias + password) → Create project → download zip
    """
    create_page = CreateProjectPage(page)
    await create_page.wait_for_form()
    await create_page.fill(
        project_name=portal_name,
        on_behalf_of_company=False,
        api_selection=api_selection,
    )
    await create_page.proceed()

    result = await create_page.wait_for_confirmation_or_project_page()

    if result == "step2_credentials":
        await create_page.fill_step2_credentials(alias=alias, password=config.key_password)
        await create_page.create_key_step2()
        result = await create_page.wait_for_download_after_step2(alias=alias, password=config.key_password)

    if result == "project_page":
        uuid = await _get_uuid_after_creation(page, dashboard, portal_name)
        if not uuid:
            logger.error("oauth1_standard: could not resolve project UUID after redirect")
            return []
        logger.info("Landed on project page — adding key via sandbox ({})", uuid)
        artifacts = await _add_oauth_signing_key_via_sandbox(page, uuid, dest_dir, project, api_name, alias, config)
        return artifacts

    if result == "download":
        key_zip = await create_page.download_key_file(dest_dir=dest_dir, filename_hint=f"{project.name}-{api_name}")
        logger.info("Downloaded signing key zip: {}", key_zip)
        uuid = await _get_uuid_after_creation(page, dashboard, portal_name)
        if uuid:
            creds = await _capture_consumer_key(page, uuid, dest_dir, project, api_name, alias=alias)
            return [creds, key_zip] if creds else [key_zip]
        return [key_zip]

    logger.error("Unexpected result {!r} for oauth1_standard ({})", result, api_name)
    return []


async def _provision_oauth1_skip_step3(
    page, dashboard: DashboardPage, portal_name: str,
    dest_dir: Path, project: ProjectSpec, api_name: str,
    alias: str, config: AppConfig,
) -> list[Path]:
    """
    OAuth 1.0a where the wizard Step 3 ("Additional credentials") offers an
    optional Mastercard Encryption Key we don't want. Clicking the encryption
    "Create project" suppresses the signing-key download and leaves the
    sandbox page with no extractable consumer key.

    Flow:
      Step 1 (name) → Proceed → Step 2 (signing alias+password) → Create project
      → Step 3: click 'Skip this step' → lands on /project-details/.../sandbox
      → sandbox: 'Add project key' wizard → download signing zip + extract consumer key

    APIs: transaction_notifications
    """
    create_page = CreateProjectPage(page)
    await create_page.wait_for_form()
    await create_page.fill(project_name=portal_name, on_behalf_of_company=False)
    await create_page.proceed()

    result = await create_page.wait_for_confirmation_or_project_page()

    if result == "step2_credentials":
        await create_page.fill_step2_credentials(alias=alias, password=config.key_password)
        await create_page.create_key_step2()
        result = await create_page.wait_for_download_after_step2(
            alias=alias, password=config.key_password, skip_step3=True,
        )

    extra_artifacts: list[Path] = []
    if result == "download":
        # Mastercard auto-generated an encryption .pem after we clicked Create
        # on Step 3 without filling the encryption fields. Capture it, then
        # navigate to the sandbox to add a signing key.
        enc_pem = await create_page.download_key_file(
            dest_dir=dest_dir, filename_hint=f"{project.name}-{api_name}-enc"
        )
        logger.info("Downloaded auto-generated encryption key: {}", enc_pem)
        extra_artifacts.append(enc_pem)
        uuid = await _get_uuid_after_creation(page, dashboard, portal_name)
        if not uuid:
            logger.error("oauth1_skip_step3: could not locate project UUID after download")
            return extra_artifacts
        signing = await _add_oauth_signing_key_via_sandbox(
            page, uuid, dest_dir, project, api_name, alias, config
        )
        return extra_artifacts + signing

    if result == "project_page":
        uuid = await _get_uuid_after_creation(page, dashboard, portal_name)
        if not uuid:
            logger.error("oauth1_skip_step3: could not resolve project UUID after redirect")
            return []
        logger.info("Skipped Step 3 — adding signing key via sandbox ({})", uuid)
        return await _add_oauth_signing_key_via_sandbox(
            page, uuid, dest_dir, project, api_name, alias, config
        )

    logger.error("Unexpected result {!r} for oauth1_skip_step3 ({})", result, api_name)
    return []


async def _provision_match_inline(
    page, dashboard: DashboardPage, portal_name: str,
    dest_dir: Path, project: ProjectSpec, api_name: str,
    alias: str, config: AppConfig,
) -> list[Path]:
    """MATCH Pro single-page create-project flow.

    Drives every interaction directly with the deterministic selectors
    captured from a manual recording (see logs/recordings/*/trace.jsonl):
    project name → service details (company/ICA/email/No) → key alias +
    password → Create project → Download key file → Open project.
    """
    create_page = CreateProjectPage(page)
    await create_page.wait_for_form()
    key_zip, uuid = await create_page.provision_match(
        project_name=portal_name,
        alias=alias,
        password=config.key_password,
        dest_dir=dest_dir,
        filename_hint=f"{project.name}-{api_name}-signing",
    )
    creds_file = await _capture_consumer_key(
        page, uuid, dest_dir, project, api_name, alias=alias
    )
    return [creds_file, key_zip] if creds_file else [key_zip]


# ---------------------------------------------------------------------------
# Generic playbook-driven provisioning
# ---------------------------------------------------------------------------

async def _provision_via_playbook(
    page, dashboard: DashboardPage, portal_name: str,
    dest_dir: Path, project: ProjectSpec, api_name: str,
    alias: str, config: AppConfig,
) -> list[Path]:
    """Drive a portal create-project flow from a recorded JSON playbook.

    Looks up ``playbooks/mastercard/<api-slug>.json`` (recorded by
    ``mcd-key-automation record-api <URL>`` against a manual walk-through).
    Records artifacts to ``dest_dir`` and captures the consumer key from
    the resulting project page.
    """
    from providers.mastercard.playbook_runner import (
        PlaybookRunner, find_playbook, load_playbook,
    )
    from providers.mastercard.pages.create_project_page import CreateProjectPage

    api_slug = API_SLUGS.get(api_name, api_name)
    playbook_file = find_playbook("mastercard", api_slug)
    if playbook_file is None:
        raise FileNotFoundError(
            f"No playbook for api_slug={api_slug!r} at "
            f"playbooks/mastercard/{api_slug}.json. "
            f"Record one with: mcd-key-automation record-api <docs-url>"
        )

    playbook = load_playbook(playbook_file)
    defaults = playbook.get("defaults", {})

    # Resolve contact email from session JWT / env (reuses CreateProjectPage logic).
    create_page = CreateProjectPage(page)
    contact_email = await create_page._resolve_contact_email()

    variables: dict[str, str] = {
        "project_name": portal_name,
        "alias": alias,
        "key_password": config.key_password,
        "contact_email": contact_email,
        **{k: str(v) for k, v in defaults.items()},
    }

    runner = PlaybookRunner(
        page, playbook, variables,
        dest_dir=dest_dir,
        download_name_hint=f"{project.name}-{api_name}-signing",
    )
    await runner.run()

    # Extract project UUID from the resulting URL (e.g. /project-details/<uuid>).
    final_url = runner.final_url or page.url
    if "/project-details/" not in final_url:
        logger.warning(
            "Playbook for {} did not land on /project-details/ (final_url={})",
            api_slug, final_url,
        )
        return list(runner.downloads)
    uuid = final_url.split("/project-details/")[-1].split("/")[0].split("?")[0]
    logger.info("Playbook[{}] provisioned project uuid={}", api_slug, uuid)

    creds_file = await _capture_consumer_key(
        page, uuid, dest_dir, project, api_name, alias=alias
    )
    artifacts: list[Path] = list(runner.downloads)
    if creds_file:
        artifacts.insert(0, creds_file)
    return artifacts


async def _provision_oauth1_enc_key(
    page, dashboard: DashboardPage, portal_name: str,
    dest_dir: Path, project: ProjectSpec, api_name: str,
    alias: str, config: AppConfig,
) -> list[Path]:
    """
    OAuth 1.0a with a Mastercard-provided client encryption PEM:
      Step 1 → Proceed → Step 2 (signing alias + password) → Create project
      → Step 3: Mastercard public encryption key — Create project → download PEM
      → sandbox: Add project key → download signing ZIP + capture consumer key

    The Step 3 download is the Mastercard PUBLIC encryption key (PEM) for JWE
    body encryption — it is NOT the OAuth signing key. The wizard does NOT
    create an OAuth signing key on the sandbox tab when it creates the
    encryption pair, so attempting to read the consumer key immediately after
    Step 3 yields no rows.

    We therefore replicate the oauth1_skip_step3 approach: after downloading
    the encryption PEM we go to the sandbox "Add project key" flow to generate
    the OAuth signing key (ZIP + consumer key credentials).

    When the wizard lands on the project page directly (no Step 3 download),
    the signing key already exists on the sandbox tab and we fall through to
    _add_oauth_signing_key_via_sandbox in the same way.
    """
    create_page = CreateProjectPage(page)
    await create_page.wait_for_form()
    await create_page.fill(project_name=portal_name, on_behalf_of_company=False)
    await create_page.proceed()

    result = await create_page.wait_for_confirmation_or_project_page()

    if result == "step2_credentials":
        await create_page.fill_step2_credentials(alias=alias, password=config.key_password)
        await create_page.create_key_step2()
        result = await create_page.wait_for_download_after_step2(alias=alias, password=config.key_password)

    if result == "download":
        # The wizard Step 3 downloads the Mastercard PUBLIC encryption PEM (for
        # JWE body encryption).  Save with -signing- hint so provider.download_keys
        # names it consistently with the other artifacts for this API; the export
        # layer searches for *-<slug>-signing-v1.pem when building the .env entry.
        enc_pem = await create_page.download_key_file(
            dest_dir=dest_dir, filename_hint=f"{project.name}-{api_name}-enc"
        )
        logger.info("Downloaded Mastercard encryption PEM from wizard Step 3: {}", enc_pem)
        # The wizard does NOT create a sandbox OAuth signing key during Step 3,
        # so _capture_consumer_key would find no key rows.  Add the signing key
        # explicitly via the sandbox "Add project key" flow instead.
        uuid = await _get_uuid_after_creation(page, dashboard, portal_name)
        if uuid:
            sandbox_artifacts = await _add_oauth_signing_key_via_sandbox(
                page, uuid, dest_dir, project, api_name, alias, config
            )
            return [enc_pem] + sandbox_artifacts
        logger.error("oauth1_enc_key: could not resolve project UUID after PEM download ({})", api_name)
        return [enc_pem]

    if result == "project_page":
        # Wizard landed directly on project page (no Step 3 download).
        # The signing key is already on the sandbox tab — add one via Add project key.
        uuid = await _get_uuid_after_creation(page, dashboard, portal_name)
        if not uuid:
            logger.error("oauth1_enc_key: could not resolve project UUID after redirect")
            return []
        return await _add_oauth_signing_key_via_sandbox(page, uuid, dest_dir, project, api_name, alias, config)

    logger.error("Unexpected result {!r} for oauth1_enc_key ({})", result, api_name)
    return []


async def _provision_oauth2_region(
    page, dashboard: DashboardPage, portal_name: str,
    dest_dir: Path, project: ProjectSpec, api_name: str,
    region: str, config: AppConfig,
) -> list[Path]:
    """
    OAuth 2.0 with mandatory region selection (Open Finance / ofin):
      Step 1: fill name + select region from dropdown → Proceed
      → "Open project" button (no key download in wizard)
      → sandbox: extract partner_id / app_key / secret + download Mastercard sig-verification key

    The region dropdown uses a react-select with placeholder 'Type to search'.
    We type the region name to filter, then click the matching option.
    """
    create_page = CreateProjectPage(page)
    await create_page.wait_for_form()
    await create_page.fill_ofin(project_name=portal_name, region=region)
    await create_page.proceed()

    result = await create_page.wait_for_confirmation_or_project_page()

    if result == "open_project":
        logger.info("OAuth 2.0 project created — opening project")
        await create_page.open_project()
        uuid = page.url.rstrip("/").split("/project-details/")[-1].split("/")[0]
        return await _oauth2_sandbox_keys(page, uuid, dest_dir, project, api_name)

    if result == "project_page":
        # Wizard navigated directly to project page (no intermediate "Open project" button).
        uuid = page.url.rstrip("/").split("/project-details/")[-1].split("/")[0]
        logger.info("OAuth 2.0 project landed on project page directly — uuid={}", uuid)
        return await _oauth2_sandbox_keys(page, uuid, dest_dir, project, api_name)

    logger.error("Unexpected result {!r} for oauth2_region ({})", result, api_name)
    return []


async def _provision_priceless(
    page, dashboard: DashboardPage, portal_name: str,
    dest_dir: Path, project: ProjectSpec, api_name: str,
    alias: str, api_selection: str, config: AppConfig,
) -> list[Path]:
    """
    Priceless Cities — must select 'Priceless Specials' sub-API card before proceeding.
    Requires API Owner approval so keys will be NEEDS_APPROVAL until approved.

    Step 1: fill name → click 'Priceless Specials' card → Proceed
    → Step 2: alias + password → Create project → download zip
    """
    create_page = CreateProjectPage(page)
    await create_page.wait_for_form()
    await create_page.fill_priceless(project_name=portal_name, api_selection=api_selection)
    await create_page.proceed()

    result = await create_page.wait_for_confirmation_or_project_page()

    if result == "step2_credentials":
        await create_page.fill_step2_credentials(alias=alias, password=config.key_password)
        await create_page.create_key_step2()
        result = await create_page.wait_for_download_after_step2(alias=alias, password=config.key_password)

    if result == "download":
        key_zip = await create_page.download_key_file(dest_dir=dest_dir, filename_hint=f"{project.name}-{api_name}")
        logger.info("Priceless signing key downloaded (pending approval): {}", key_zip)
        uuid = await _get_uuid_after_creation(page, dashboard, portal_name)
        if uuid:
            creds = await _capture_consumer_key(page, uuid, dest_dir, project, api_name, alias=alias)
            return [creds, key_zip] if creds else [key_zip]
        return [key_zip]

    logger.error("Unexpected result {!r} for priceless ({})", result, api_name)
    return []


async def _oauth2_sandbox_keys(
    page,
    uuid: str,
    dest_dir: Path,
    project: ProjectSpec,
    api_name: str,
) -> list[Path]:
    """Extract OAuth 2.0 credentials and download the Mastercard Signature Verification Key."""
    sandbox = SandboxPage(page)
    await sandbox.goto(uuid)

    oauth2 = OAuth2SandboxPage(page)
    creds = await oauth2.extract_credentials()
    creds_file = await oauth2.save_credentials_json(
        creds,
        dest_dir,
        f"{project.name}-{api_name}-credentials.json",
    )

    if await oauth2.has_signature_key():
        sig_file = await oauth2.download_existing_signature_key(
            dest_dir=dest_dir,
            filename_hint=f"{project.name}-{api_name}-sig",
        )
    else:
        # Some OAuth 2.0 tenants (e.g. Open Finance Australia) do not expose
        # a Mastercard Signature Verification Key section at all — only the
        # Partner ID / App Key / Secret are needed. If the "Add key" button
        # isn't present on the sandbox page, skip the sig-key step instead
        # of timing out trying to click a non-existent element.
        add_btn = page.locator(OAuth2SandboxSelectors.add_sig_key_button)
        try:
            has_add_btn = await add_btn.count() > 0 and await add_btn.first.is_visible()
        except Exception:
            has_add_btn = False
        if not has_add_btn:
            logger.info(
                "No Mastercard Signature Verification Key section on sandbox page "
                "for {!r} — skipping (credentials-only tenant).",
                api_name,
            )
            return [creds_file]
        sig_file = await oauth2.add_signature_key(
            dest_dir=dest_dir,
            filename_hint=f"{project.name}-{api_name}-sig",
        )

    return [creds_file, sig_file]


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

async def ensure_project_with_api(
    dashboard: DashboardPage,
    project: ProjectSpec,
    api_name: str,
    workspace: Path,
    config: AppConfig,
    api_spec=None,
    run_timestamp: str | None = None,
) -> list[Path]:
    """
    Always creates a new ``SS-{project.name}-{run_timestamp}`` portal project
    and provisions key material for the given API.

    Dispatches to a per-provision-type function based on API_CONFIG[api_name].provision_type
    so every API's exact portal flow is explicit and isolated.
    """
    api_cfg = API_CONFIG.get(api_name)
    if not api_cfg:
        raise ValueError(f"Unknown API: {api_name!r} — add it to providers/mastercard/api_config.py")

    page = dashboard.page
    dest_dir = workspace / "downloads"
    dest_dir.mkdir(parents=True, exist_ok=True)

    alias = _key_alias(api_name)
    ts = run_timestamp or "000000"
    portal_name = f"SS-{project.name}-{ts}"
    # Mastercard Developers portal enforces a 50-char limit on project name.
    # When the API slug is long (e.g. enhanced-currency-conversion-calculator
    # is already 40 chars), the default "SS-<slug>-<ts>" overflows and the
    # Proceed button stays disabled. Truncate the middle while keeping the
    # SS- prefix and the full timestamp suffix so each run is still unique.
    _PORTAL_NAME_MAX = 50
    if len(portal_name) > _PORTAL_NAME_MAX:
        overflow = len(portal_name) - _PORTAL_NAME_MAX
        trimmed = project.name[: max(1, len(project.name) - overflow)]
        portal_name = f"SS-{trimmed}-{ts}"
        logger.info(
            "Project name exceeded {} chars — truncated slug portion to {!r}",
            _PORTAL_NAME_MAX, trimmed,
        )

    api_slug = API_SLUGS.get(api_name, api_cfg.slug)
    fast_path = CreateProjectSelectors.fast_path_url_tpl.format(api_slug=api_slug)
    logger.info("Provisioning {!r} (type={}) — project {!r}", api_name, api_cfg.provision_type, portal_name)

    from app.strategy_learner import (
        fallback_strategies, write_learned, write_failure_report,
    )
    from browser.screenshots import capture as _screenshot

    primary = api_cfg.provision_type
    strategies: list[str] = [primary, *fallback_strategies(primary)]
    attempts: list[dict] = []

    for idx, ptype in enumerate(strategies):
        # Each strategy attempt creates a fresh portal project so a partial
        # leftover from a failed attempt can't contaminate the next one.
        # ``portal_name`` already embeds ``run_timestamp``; for attempts 2+
        # we suffix the strategy name to keep portal names unique.
        attempt_portal_name = portal_name if idx == 0 else f"{portal_name}-{ptype}"
        if len(attempt_portal_name) > _PORTAL_NAME_MAX:
            attempt_portal_name = attempt_portal_name[:_PORTAL_NAME_MAX]
        if idx > 0:
            logger.warning(
                "Primary strategy {!r} failed for {!r}; trying fallback {!r} ({} of {})",
                primary, api_name, ptype, idx + 1, len(strategies),
            )
        await page.goto(fast_path, wait_until="domcontentloaded")

        try:
            artifacts = await _dispatch_provision(
                ptype, page, dashboard, attempt_portal_name, dest_dir,
                project, api_name, alias, api_cfg, config,
            )
        except Exception as exc:
            err_url = page.url
            try:
                shot_path = await _screenshot(page, f"failure_{api_name}_{ptype}")
            except Exception:
                shot_path = None
            attempts.append({
                "strategy": ptype,
                "error": f"{type(exc).__name__}: {exc}",
                "url": err_url,
                "screenshot": str(shot_path) if shot_path else None,
            })
            # Continue to next strategy unless this was the last.
            if idx == len(strategies) - 1:
                report = write_failure_report(
                    api_name, primary, attempts,
                    page_url=err_url,
                    screenshot_path=str(shot_path) if shot_path else None,
                )
                # Re-raise with the report path attached so the orchestrator
                # can surface it (and the user-facing message stays clean).
                raise type(exc)(
                    f"{exc} — see failure report: {report}"
                ) from exc
            continue

        # Success.
        attempts.append({
            "strategy": ptype, "error": None, "url": page.url, "screenshot": None,
        })
        if idx > 0:
            write_learned(api_name, primary, ptype, attempts)
        return artifacts

    # Unreachable — loop above either returns or raises.
    raise RuntimeError(f"No strategies tried for {api_name!r}")


async def _dispatch_provision(
    ptype: str, page, dashboard: DashboardPage, portal_name: str,
    dest_dir: Path, project: ProjectSpec, api_name: str, alias: str,
    api_cfg, config: AppConfig,
) -> list[Path]:
    """Dispatch a single provisioning attempt for ``ptype``."""
    if ptype == "oauth1_standard":
        return await _provision_oauth1_standard(
            page, dashboard, portal_name, dest_dir, project, api_name,
            alias, config, api_selection=api_cfg.api_selection,
        )

    if ptype == "oauth1_skip_step3":
        return await _provision_oauth1_skip_step3(
            page, dashboard, portal_name, dest_dir, project, api_name, alias, config
        )

    if ptype == "match_inline":
        return await _provision_match_inline(
            page, dashboard, portal_name, dest_dir, project, api_name, alias, config
        )

    if ptype == "playbook":
        return await _provision_via_playbook(
            page, dashboard, portal_name, dest_dir, project, api_name, alias, config
        )

    if ptype == "oauth1_enc_key":
        return await _provision_oauth1_enc_key(
            page, dashboard, portal_name, dest_dir, project, api_name, alias, config
        )

    if ptype == "oauth2_region":
        return await _provision_oauth2_region(
            page, dashboard, portal_name, dest_dir, project, api_name,
            region=api_cfg.region or "United States of America", config=config
        )

    if ptype == "priceless":
        return await _provision_priceless(
            page, dashboard, portal_name, dest_dir, project, api_name,
            alias=alias, api_selection=api_cfg.api_selection or "Priceless Specials", config=config
        )

    raise ValueError(f"Unknown provision_type {ptype!r} for API {api_name!r}")


