"""Mastercard Developers provider."""
from __future__ import annotations

from pathlib import Path

from loguru import logger
from playwright.async_api import Page

from app.alias_engine import make_alias, make_filename
from app.models import AppConfig, DownloadedArtifact, ProjectSpec
from app.validators import sha256_file, classify_extension
from providers.base import DeveloperPortalProvider
from providers.mastercard.pages.dashboard_page import DashboardPage
from providers.mastercard.pages.login_page import LoginPage
from providers.mastercard.workflows.project_workflow import ensure_project_with_api


class MastercardProvider(DeveloperPortalProvider):
    name = "mastercard"

    def __init__(self, page: Page, config: AppConfig, workspace: Path) -> None:
        super().__init__(page, config, workspace)
        self.login_page = LoginPage(page, login_url=config.login_url)
        self.dashboard = DashboardPage(page)

    async def login(self) -> None:
        await self.login_page.goto()
        await self.login_page.wait_for_manual_auth()
        logger.info("Authenticated session detected.")

    async def ensure_project(self, project: ProjectSpec) -> None:
        # Project creation is now done per-API via ensure_project_with_api.
        pass

    async def attach_api(self, project: ProjectSpec, api: str) -> None:
        # API is attached during project creation (fast-path URL includes ?services=).
        pass

    async def download_keys(self, project: ProjectSpec, api: str) -> list[DownloadedArtifact]:
        await self.dashboard.goto()
        raw_file = await ensure_project_with_api(self.dashboard, project, api, self.workspace)

        alias = make_alias(
            organization=self.config.organization,
            environment=self.config.environment,
            project=project.name,
            api=api,
        )
        ext = raw_file.suffix.lstrip(".")
        filename = make_filename(alias, ext)
        dest = self.workspace / "normalized" / filename
        dest.parent.mkdir(parents=True, exist_ok=True)
        raw_file.rename(dest)

        artifact = DownloadedArtifact(
            alias=alias,
            filename=filename,
            path=str(dest),
            sha256=sha256_file(dest),
            kind=classify_extension(filename),
            project=project.name,
            api=api,
        )
        logger.info("Artifact: {} ({})", artifact.filename, artifact.sha256[:12])
        return [artifact]

