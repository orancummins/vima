"""Project page object (placeholder)."""
from __future__ import annotations

from playwright.async_api import Page


class ProjectPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    async def attach_api(self, api_slug: str) -> None:
        raise NotImplementedError

    async def open_api(self, api_slug: str) -> None:
        raise NotImplementedError
