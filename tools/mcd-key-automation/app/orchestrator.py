"""Top-level workflow orchestrator."""
from __future__ import annotations

from pathlib import Path

from loguru import logger

from app.alias_engine import make_alias, make_filename  # noqa: F401  (used by downstream phases)
from app.config_loader import load_config
from app.exceptions import McdAutomationError
from app.models import AppConfig, DownloadedArtifact
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
    async with browser_session(headless=headless, downloads_dir=WORKSPACE) as (_browser, _ctx, page):
        provider: DeveloperPortalProvider = _provider_for(config.organization)(page, config, WORKSPACE, headless=headless)
        try:
            await provider.login()
            if dry_run:
                logger.info("Dry-run: stopping after login.")
                return None
            failed: list[str] = []
            for project in config.projects:
                await provider.ensure_project(project)
                for api_spec in project.normalised_apis():
                    try:
                        await provider.attach_api(project, api_spec.name)
                        arts = await provider.download_keys(project, api_spec.name)
                        artifacts.extend(arts)
                        has_creds = any(a.filename.endswith("-credentials.json") for a in arts)
                        if has_creds:
                            logger.info("Provisioned '{}' ✓", api_spec.name)
                            # Rebuild the vima-config zip incrementally so the
                            # supervisor (the VIMA Flask app) can import each
                            # API as soon as it's been provisioned, rather
                            # than waiting for the entire run to finish.
                            _rebuild_vima_zip(config.key_password)
                        else:
                            logger.warning(
                                "Failed to provision '{}': key zip downloaded but consumer key could not be extracted — check sandbox page",
                                api_spec.name,
                            )
                            failed.append(f"{project.name}/{api_spec.name}")
                    except Exception as api_err:
                        logger.error(
                            "Failed to provision '{}': {} — skipping, continuing with remaining APIs",
                            api_spec.name, api_err,
                        )
                        await capture(page, f"failure_{project.name}_{api_spec.name}")
                        failed.append(f"{project.name}/{api_spec.name}")
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
