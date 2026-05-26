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

    async def click_create_project(self) -> None:
        logger.info("Clicking 'Create new project'")
        await self.page.locator(DashboardSelectors.create_project_button).click()
