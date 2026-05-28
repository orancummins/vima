"""Login page object."""
from __future__ import annotations

import os
from urllib.parse import urlparse

from loguru import logger
from playwright.async_api import Page

from browser.waits import wait_until
from providers.mastercard.selectors import LoginSelectors


_LOGIN_PATH_FRAGMENT = "/account/log-in"


class LoginPage:
    def __init__(self, page: Page, login_url: str) -> None:
        self.page = page
        self.login_url = login_url

    async def goto(self) -> None:
        logger.info("Navigating to {}", self.login_url)
        await self.page.goto(self.login_url, wait_until="domcontentloaded")

    async def fill_credentials(self, email: str, password: str) -> None:
        """Pre-fill the Mastercard Developers login form and submit.

        Uses press_sequentially to fire React/framework key events.
        Wrapped in try/except — if selectors don't match the current portal
        layout, logs a warning and falls back to manual login.

        Update LoginSelectors in selectors.py if auto-fill fails; run
        discover.py and inspect logs/dom/*.html for the correct selectors.
        """
        logger.info("Pre-filling login form for {}", email)
        try:
            await self.page.wait_for_load_state("domcontentloaded", timeout=10000)

            email_loc = self.page.locator(LoginSelectors.email_input).first
            await email_loc.wait_for(state="visible", timeout=8000)
            await email_loc.click(click_count=3)
            await email_loc.press_sequentially(email, delay=40)

            password_loc = self.page.locator(LoginSelectors.password_input).first
            await password_loc.wait_for(state="visible", timeout=8000)
            await password_loc.click(click_count=3)
            await password_loc.press_sequentially(password, delay=40)

            submit_loc = self.page.locator(LoginSelectors.submit_button).first
            await submit_loc.wait_for(state="visible", timeout=5000)
            await submit_loc.click()
            logger.info("Login form submitted — waiting for MFA/CAPTCHA if required...")
        except Exception as exc:
            logger.warning(
                "Credential pre-fill failed ({}): {} — complete login manually in the browser",
                type(exc).__name__,
                str(exc)[:120],
            )

    async def wait_for_manual_auth(self, *, timeout_s: float = 600.0) -> None:
        """Block until the user completes login (incl. MFA/CAPTCHA).

        If MCD_PORTAL_EMAIL and MCD_PORTAL_PASSWORD are set in the environment
        the login form is pre-filled automatically before waiting.  MFA/CAPTCHA
        still requires human action when prompted.

        On re-runs where session_state.json holds a valid cookie the browser
        redirects away from the login page immediately and this returns at once.
        """
        # Session already authenticated — redirect happened on goto().
        if _LOGIN_PATH_FRAGMENT not in self.page.url:
            logger.info("Session already authenticated — skipping login form.")
            return

        email = os.environ.get("MCD_PORTAL_EMAIL", "").strip()
        password = os.environ.get("MCD_PORTAL_PASSWORD", "").strip()
        if email and password:
            await self.fill_credentials(email, password)
        else:
            logger.info(
                "MCD_PORTAL_EMAIL / MCD_PORTAL_PASSWORD not set — "
                "complete sign-in manually in the browser window..."
            )

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
