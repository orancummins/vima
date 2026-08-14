"""API page object (placeholder)."""
from __future__ import annotations

from pathlib import Path

from playwright.async_api import Page


class ApiPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    async def generate_and_download(self, *, dest_dir: Path) -> list[Path]:
        """Trigger key generation flow and return downloaded paths."""
        raise NotImplementedError
