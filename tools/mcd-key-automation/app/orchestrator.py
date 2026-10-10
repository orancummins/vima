"""Top-level workflow orchestrator."""
from __future__ import annotations

from pathlib import Path

from loguru import logger

from app.alias_engine import make_alias, make_filename  # noqa: F401  (used by downstream phases)
from app.config_loader import load_config
from app.exceptions import McdAutomationError
from app.models import AppConfig, DownloadedArtifact, ProjectSpec
from app.package_builder import build_bundle
from browser.screenshots import capture
from browser.session import browser_session
from providers.base import DeveloperPortalProvider
from providers.mastercard.provider import MastercardProvider


HERE = Path(__file__).parent.parent
WORKSPACE = HERE / "temp"
OUTPUT_DIR = HERE / "output"


def _provider_for(name: str):
    if name == "mastercard":
        return MastercardProvider
    raise McdAutomationError(f"Unknown provider {name!r}")


async def run(config_path: Path, *, dry_run: bool = False, headless: bool = False) -> Path | None:
    config: AppConfig = load_config(config_path)
    logger.info("Loaded config for env={} ({} projects)", config.environment, len(config.projects))

    # Expose the headless flag to downstream helpers (e.g. the playbook runner's
    # os_click, which must NOT fire physical mouse clicks when there is no
    # visible browser window).
    import os as _os
    _os.environ["MCD_HEADLESS"] = "1" if headless else "0"

    WORKSPACE.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # NOTE: previously this routine wiped ``temp/normalized`` and
    # ``temp/downloads`` so each run started from scratch. That made
    # re-provisioning a single API blow away the staged artifacts for all the
    # other APIs that had been provisioned in earlier runs. We now keep the
    # workspace and let the per-API filename naming convention overwrite only
    # the artifacts for the APIs being re-provisioned this run — so the
    # ``.env`` is updated one API at a time rather than rebuilt from zero.

    artifacts: list[DownloadedArtifact] = []
    failed: list[str] = []

    # ------------------------------------------------------------------
    # Phase 1 — Mastercard Developers API (fast, browser-free) where supported.
    # Falls back to the browser (Phase 2) for anything the admin key can't do
    # unattended, or when no admin key is configured.
    # ------------------------------------------------------------------
    from datetime import datetime as _dtdt

    from app._vima_catalog import entry_for_legacy
    from providers.mastercard.api_config import API_CONFIG
    from providers.mastercard_api import (
        ADMIN_KEY_INSTRUCTIONS,
        ApiProvisioner,
        is_admin_key_configured,
    )

    run_ts = _dtdt.now().strftime("%Y%m%d%H%M%S")
    prefix = getattr(config, "project_prefix", "SS") or "SS"

    provisioner = None if dry_run else ApiProvisioner.try_from_env()
    if provisioner is not None:
        logger.info(
            "Provisioning technique: Mastercard Developers API (admin key). "
            "Browser automation (Playwright) is the fallback."
        )
        print("[technique] Mastercard Developers API (admin key) — browser automation as fallback.", flush=True)
    elif not dry_run:
        if not is_admin_key_configured():
            # First-launch transparency: tell the user how to enable the fast path.
            print(ADMIN_KEY_INSTRUCTIONS, flush=True)
        logger.info("Provisioning technique: browser automation (Playwright).")
        print("[technique] Browser automation (Playwright) — no Developers API admin key configured.", flush=True)

    # (project, api_name) pairs that still need the browser flow.
    remaining: list[tuple[ProjectSpec, str]] = []
    for project in config.projects:
        for api_spec in project.normalised_apis():
            api = api_spec.name
            handled = False
            if provisioner is not None:
                setup = API_CONFIG.get(api)
                entry = entry_for_legacy(api)
                try:
                    if provisioner.supports(api, setup, entry):
                        logger.info("Provisioning '{}' via Developers API…", api)
                        arts = provisioner.provision(
                            api_id=api,
                            entry=entry,
                            setup=setup,
                            project_name=project.name,
                            portal_project_name=f"{prefix}-{api}-{run_ts}",
                            organization=config.organization,
                            environment=config.environment,
                            key_password=config.key_password,
                            dest_dir=WORKSPACE,
                        )
                        artifacts.extend(arts)
                        logger.info("Provisioned '{}' ✓ (Developers API)", api)
                        _rebuild_vima_zip(config.key_password)
                        handled = True
                except Exception as exc:  # noqa: BLE001 - fall back to the browser
                    logger.warning(
                        "Developers API provisioning of '{}' failed ({}) — "
                        "falling back to browser automation.", api, exc,
                    )
            if not handled:
                remaining.append((project, api))

    # ------------------------------------------------------------------
    # Phase 2 — browser automation for the remaining APIs (and dry-run login).
    # ------------------------------------------------------------------
    if remaining or dry_run:
        async with browser_session(headless=headless, downloads_dir=WORKSPACE) as (_browser, _ctx, page):
            provider: DeveloperPortalProvider = _provider_for(config.organization)(page, config, WORKSPACE, headless=headless)
            try:
                await provider.login()
                if dry_run:
                    logger.info("Dry-run: stopping after login.")
                    return None
                for project, api in remaining:
                    logger.info("Provisioning '{}' via browser automation…", api)
                    try:
                        await provider.attach_api(project, api)
                        arts = await provider.download_keys(project, api)
                        artifacts.extend(arts)
                        has_creds = any(a.filename.endswith("-credentials.json") for a in arts)
                        if has_creds:
                            logger.info("Provisioned '{}' ✓ (browser automation)", api)
                            # Rebuild the vima-config zip incrementally so the
                            # supervisor (the VIMA Flask app) can import each
                            # API as soon as it's been provisioned, rather
                            # than waiting for the entire run to finish.
                            _rebuild_vima_zip(config.key_password)
                        else:
                            logger.warning(
                                "Failed to provision '{}': key zip downloaded but consumer key could not be extracted — check sandbox page",
                                api,
                            )
                            failed.append(f"{project.name}/{api}")
                    except Exception as api_err:
                        logger.error(
                            "Failed to provision '{}': {} — skipping, continuing with remaining APIs",
                            api, api_err,
                        )
                        await capture(page, f"failure_{project.name}_{api}")
                        failed.append(f"{project.name}/{api}")
            except Exception as e:
                logger.exception("Workflow failed: {}", e)
                await capture(page, "workflow_failure")
                raise


    if failed:
        logger.warning("Skipped {} API(s) due to errors: {}", len(failed), failed)
    if not artifacts:
        logger.warning("No artifacts collected — skipping bundle build.")
        return None

    bundle = build_bundle(config=config, artifacts=artifacts, output_dir=OUTPUT_DIR)

    # Also build a vima-config.zip ready for /config/import. This is the
    # final, end-of-run rebuild that captures every artifact, including any
    # OAuth 2.0 / OFin credentials that were provisioned later in the run.
    _rebuild_vima_zip(config.key_password)

    return bundle


def _rebuild_vima_zip(key_password: str) -> None:
    """Rebuild output/vima-config.zip from the current temp/normalized contents.

    Called both after each successful per-API provisioning (for incremental
    .env updates on the supervisor side) and at the end of the run.
    Failures are logged and swallowed — the worst case is the next iteration
    or the end-of-run rebuild catches whatever this one missed.
    """
    try:
        import sys as _sys
        from pathlib import Path as _Path
        _tool_root = _Path(__file__).resolve().parents[1]
        if str(_tool_root) not in _sys.path:
            _sys.path.insert(0, str(_tool_root))
        from export_vima_config import build_vima_config_zip
        vima_zip = OUTPUT_DIR / "vima-config.zip"
        result = build_vima_config_zip(WORKSPACE / "normalized", key_password, vima_zip)
        logger.info(
            "Built vima-config.zip: {} API(s) included",
            len(result.get("apis", [])),
        )
        if result.get("skipped"):
            logger.debug("vima-config.zip skipped: {}", result["skipped"])
        # Emit a stable, machine-readable marker so the supervisor (the
        # VIMA Flask app) can trigger an incremental import without having
        # to parse loguru's free-form log lines.
        print("__VIMA_ZIP_READY__", flush=True)
    except Exception as e:
        logger.warning("vima-config.zip rebuild failed (non-fatal): {}", e)
