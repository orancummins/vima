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


async def run(config_path: Path, *, dry_run: bool = False) -> Path | None:
    config: AppConfig = load_config(config_path)
    logger.info("Loaded config for env={} ({} projects)", config.environment, len(config.projects))

    WORKSPACE.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    artifacts: list[DownloadedArtifact] = []
    async with browser_session(downloads_dir=WORKSPACE) as (_browser, _ctx, page):
        provider: DeveloperPortalProvider = _provider_for(config.organization)(page, config, WORKSPACE)
        try:
            await provider.login()
            if dry_run:
                logger.info("Dry-run: stopping after login.")
                return None
            for project in config.projects:
                await provider.ensure_project(project)
                for api_spec in project.normalised_apis():
                    await provider.attach_api(project, api_spec.name)
                    arts = await provider.download_keys(project, api_spec.name)
                    artifacts.extend(arts)
        except Exception as e:
            logger.exception("Workflow failed: {}", e)
            await capture(page, "workflow_failure")
            raise

    if not artifacts:
        logger.warning("No artifacts collected — skipping bundle build.")
        return None

    return build_bundle(config=config, artifacts=artifacts, output_dir=OUTPUT_DIR)
