"""Login page object."""
from __future__ import annotations

from loguru import logger
from playwright.async_api import Page

from browser.waits import wait_until
from providers.mastercard.selectors import LoginSelectors


class LoginPage:
    def __init__(self, page: Page, login_url: str) -> None:
        self.page = page
        self.login_url = login_url

    async def goto(self) -> None:
        logger.info("Navigating to {}", self.login_url)
        await self.page.goto(self.login_url, wait_until="domcontentloaded")

    async def wait_for_manual_auth(self, *, timeout_s: float = 600.0) -> None:
        """Block until the user completes login (incl. MFA/CAPTCHA)."""
        logger.info("Waiting for manual login. Complete sign-in + MFA in the browser window...")

        async def authenticated() -> bool:
            try:
                loc = self.page.locator(LoginSelectors.authenticated_marker).first
                return await loc.is_visible(timeout=500)
            except Exception:
                return False

        await wait_until(authenticated, timeout_s=timeout_s, description="authenticated session")
