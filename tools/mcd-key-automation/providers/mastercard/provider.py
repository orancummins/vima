"""Mastercard Developers provider."""
from __future__ import annotations

from pathlib import Path

from loguru import logger
from playwright.async_api import Page

from app.models import AppConfig, DownloadedArtifact, ProjectSpec
from providers.base import DeveloperPortalProvider
from providers.mastercard.pages.login_page import LoginPage


class MastercardProvider(DeveloperPortalProvider):
    name = "mastercard"

    def __init__(self, page: Page, config: AppConfig, workspace: Path) -> None:
        super().__init__(page, config, workspace)
        self.login_page = LoginPage(page, login_url=config.login_url)

    async def login(self) -> None:
        await self.login_page.goto()
        await self.login_page.wait_for_manual_auth()
        logger.info("Authenticated session detected.")

    async def ensure_project(self, project: ProjectSpec) -> None:
        logger.warning("ensure_project not yet implemented — pending DOM discovery")

    async def attach_api(self, project: ProjectSpec, api: str) -> None:
        logger.warning("attach_api not yet implemented — pending DOM discovery")

    async def download_keys(self, project: ProjectSpec, api: str) -> list[DownloadedArtifact]:
        logger.warning("download_keys not yet implemented — pending DOM discovery")
        return []
