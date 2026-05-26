"""Login page object."""
from __future__ import annotations

from urllib.parse import urlparse

from loguru import logger
from playwright.async_api import Page

from browser.waits import wait_until


_LOGIN_PATH_FRAGMENT = "/account/log-in"


class LoginPage:
    def __init__(self, page: Page, login_url: str) -> None:
        self.page = page
        self.login_url = login_url

    async def goto(self) -> None:
        logger.info("Navigating to {}", self.login_url)
        await self.page.goto(self.login_url, wait_until="domcontentloaded")

    async def wait_for_manual_auth(self, *, timeout_s: float = 600.0) -> None:
        """Block until the user completes login (incl. MFA/CAPTCHA).

        Detection strategy: the login page redirects away from /account/log-in
        once the session is established, so we poll the current URL.
        """
        logger.info("Waiting for manual login. Complete sign-in + MFA in the browser window...")

        async def authenticated() -> bool:
            try:
                url = self.page.url
                host = urlparse(url).hostname or ""
                return (
                    _LOGIN_PATH_FRAGMENT not in url
                    and host.endswith("developer.mastercard.com")
                )
            except Exception:
                return False

        await wait_until(authenticated, timeout_s=timeout_s, description="authenticated session")
        logger.info("Authenticated — landed on {}", self.page.url)
