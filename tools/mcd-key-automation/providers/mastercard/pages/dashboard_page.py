"""Dashboard page object (placeholder)."""
from __future__ import annotations

from playwright.async_api import Page


class DashboardPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    async def goto(self) -> None:
        # Discovery phase will fill in the canonical dashboard URL.
        raise NotImplementedError("Dashboard navigation not yet discovered")

    async def has_project(self, name: str) -> bool:
        raise NotImplementedError

    async def open_project(self, name: str) -> None:
        raise NotImplementedError

    async def create_project(self, name: str, description: str = "") -> None:
        raise NotImplementedError
