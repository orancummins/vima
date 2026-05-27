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
from providers.mastercard.selectors import API_SLUGS, CreateProjectSelectors


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
) -> list[Path]:
    """
    Standard OAuth 1.0a flow:
      Step 1 (name form) → Proceed → Step 2 (alias + password) → Create project → download zip
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

    if result == "project_page":
        uuid = page.url.rstrip("/").split("/project-details/")[-1].split("/")[0]
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


async def _provision_oauth1_enc_key(
    page, dashboard: DashboardPage, portal_name: str,
    dest_dir: Path, project: ProjectSpec, api_name: str,
    alias: str, config: AppConfig,
) -> list[Path]:
    """
    OAuth 1.0a with client encryption key:
      Step 1 → Proceed → Step 2 (alias + password) → Create project
      → [Step 3: auto-generated encryption key — Create project again] → download .pem
      → sandbox: Add project key (OAuth signing key) → download zip

    APIs: clarity, consent, eligibility, bces
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
        enc_pem = await create_page.download_key_file(dest_dir=dest_dir, filename_hint=f"{project.name}-{api_name}-enc")
        logger.info("Downloaded client encryption key: {}", enc_pem)
        uuid = await _get_uuid_after_creation(page, dashboard, portal_name)
        signing_artifacts = []
        if uuid:
            signing_artifacts = await _add_oauth_signing_key_via_sandbox(
                page, uuid, dest_dir, project, api_name, alias, config
            )
        return [enc_pem] + signing_artifacts

    if result == "project_page":
        # Wizard landed directly on project page — add signing key via sandbox.
        uuid = page.url.rstrip("/").split("/project-details/")[-1].split("/")[0]
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

    api_slug = API_SLUGS.get(api_name, api_cfg.slug)
    fast_path = CreateProjectSelectors.fast_path_url_tpl.format(api_slug=api_slug)
    logger.info("Provisioning {!r} (type={}) — project {!r}", api_name, api_cfg.provision_type, portal_name)
    await page.goto(fast_path, wait_until="domcontentloaded")

    ptype = api_cfg.provision_type

    if ptype == "oauth1_standard":
        return await _provision_oauth1_standard(
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


