"""Provider abstraction. New developer portals implement this interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from playwright.async_api import Page

from app.models import AppConfig, DownloadedArtifact, ProjectSpec


class DeveloperPortalProvider(ABC):
    name: str = "abstract"

    def __init__(self, page: Page, config: AppConfig, workspace: Path, *, headless: bool = False) -> None:
        self.page = page
        self.config = config
        self.workspace = workspace
        self.headless = headless

    @abstractmethod
    async def login(self) -> None:
        """Navigate to login page and wait for authenticated state."""

    @abstractmethod
    async def ensure_project(self, project: ProjectSpec) -> None:
        """Create the project if it doesn't exist."""

    @abstractmethod
    async def attach_api(self, project: ProjectSpec, api: str) -> None:
        """Attach the named API to the project."""

    @abstractmethod
    async def download_keys(self, project: ProjectSpec, api: str) -> list[DownloadedArtifact]:
        """Generate/download keys and return artifact records."""
