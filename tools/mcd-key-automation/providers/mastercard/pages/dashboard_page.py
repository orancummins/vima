"""Dashboard page object."""
from __future__ import annotations

from loguru import logger
from playwright.async_api import Page

from providers.mastercard.selectors import DashboardSelectors

DASHBOARD_URL = "https://developer.mastercard.com/dashboard"


class DashboardPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    async def goto(self) -> None:
        logger.info("Navigating to dashboard")
        await self.page.goto(DASHBOARD_URL, wait_until="domcontentloaded")
        await self.page.wait_for_selector(DashboardSelectors.create_project_button, timeout=20000)

    async def has_project(self, name: str) -> bool:
        try:
            loc = self.page.locator(DashboardSelectors.project_link_by_name(name))
            return await loc.count() > 0
        except Exception:
            return False

    async def project_names(self) -> list[str]:
        els = await self.page.locator(DashboardSelectors.project_link_any).all()
        return [(await e.inner_text()).strip() for e in els]

    async def get_project_url(self, name: str) -> str | None:
        """Return the full URL of the project link with the given name, or None."""
        loc = self.page.locator(DashboardSelectors.project_link_by_name(name))
        if await loc.count() == 0:
            return None
        return await loc.first.get_attribute("href")

    async def get_project_uuid(self, name: str) -> str | None:
        """Extract the UUID from a project's href, e.g. /project-details/<uuid>."""
        url = await self.get_project_url(name)
        if not url:
            return None
        # href: /project-details/<uuid>  or  https://.../<uuid>
        parts = url.rstrip("/").split("/")
        return parts[-1] if parts else None

    async def click_create_project(self) -> None:
        logger.info("Clicking 'Create new project'")
        await self.page.locator(DashboardSelectors.create_project_button).click()
