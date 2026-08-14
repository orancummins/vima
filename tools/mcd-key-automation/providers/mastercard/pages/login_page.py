"""Login page object."""
from __future__ import annotations

import os
from urllib.parse import urlparse

from loguru import logger
from playwright.async_api import Page

from app.exceptions import LoginTimeoutError
from browser.waits import wait_until
from app.exceptions import LoginTimeoutError
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
            await self.page.bring_to_front()
            await self.page.wait_for_load_state("domcontentloaded", timeout=10000)

            email_loc = self.page.locator(LoginSelectors.email_input).first
            await email_loc.wait_for(state="visible", timeout=8000)
            await email_loc.scroll_into_view_if_needed(timeout=3000)
            # Use force=True so React portals that intercept pointer events still receive the click.
            await email_loc.click(click_count=3, force=True)
            # Prefer fill() so the full value is committed atomically; fall back to
            # press_sequentially for frameworks that only respond to key events.
            try:
                await email_loc.fill(email)
            except Exception:
                await email_loc.press_sequentially(email, delay=40)

            password_loc = self.page.locator(LoginSelectors.password_input).first
            await password_loc.wait_for(state="visible", timeout=8000)
            await password_loc.scroll_into_view_if_needed(timeout=3000)
            await password_loc.click(click_count=3, force=True)
            try:
                await password_loc.fill(password)
            except Exception:
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

    async def fill_email_sso(self, email: str) -> None:
        """Pre-fill the email field only and submit — for SSO/federated login.

        After entering the email and clicking submit the portal redirects to
        the corporate SSO provider (e.g. Okta, AAD).  We do not attempt to
        fill the password field because it lives on a different domain.
        The caller is responsible for waiting until authentication completes.

        Set MCD_PORTAL_EMAIL (without MCD_PORTAL_PASSWORD) to trigger this
        path automatically, or pass SSO=Y via the test launcher.
        """
        logger.info("Pre-filling email for SSO login: {}", email)
        try:
            await self.page.bring_to_front()
            await self.page.wait_for_load_state("domcontentloaded", timeout=10000)

            email_loc = self.page.locator(LoginSelectors.email_input).first
            await email_loc.wait_for(state="visible", timeout=8000)
            await email_loc.scroll_into_view_if_needed(timeout=3000)
            # Use force=True so React portals that intercept pointer events still receive the click.
            await email_loc.click(click_count=3, force=True)
            try:
                await email_loc.fill(email)
            except Exception:
                await email_loc.press_sequentially(email, delay=40)

            submit_loc = self.page.locator(LoginSelectors.submit_button).first
            await submit_loc.wait_for(state="visible", timeout=5000)
            await submit_loc.click()
            logger.info("SSO email submitted — waiting for corporate SSO redirect...")
        except Exception as exc:
            logger.warning(
                "SSO email fill failed ({}): {} — complete login manually",
                type(exc).__name__,
                str(exc)[:120],
            )

    async def wait_for_manual_auth(self, *, timeout_s: float = 600.0, headless: bool = False) -> None:
        """Block until the user completes login (incl. MFA/CAPTCHA).

        If MCD_PORTAL_EMAIL and MCD_PORTAL_PASSWORD are set in the environment
        the login form is pre-filled automatically before waiting.  MFA/CAPTCHA
        still requires human action when prompted.

        On re-runs where session_state.json holds a valid cookie the browser
        redirects away from the login page immediately and this returns at once.

        headless=True shortens the wait to 45 s and raises SessionExpiredError
        if the portal requires interactive login, keeping unattended runs from
        hanging for 10 minutes on an expired session.
        """
        # Session already authenticated — redirect happened on goto().
        if _LOGIN_PATH_FRAGMENT not in self.page.url:
            logger.info("Session already authenticated — skipping login form.")
            return

        # The SSO redirect from /account/log-in -> /dashboard often fires
        # AFTER domcontentloaded, especially in headless. Give the saved
        # session a brief window to redirect before deciding we need a login.
        async def _redirected_away() -> bool:
            try:
                return _LOGIN_PATH_FRAGMENT not in self.page.url
            except Exception:
                return False

        try:
            await wait_until(_redirected_away, timeout_s=8.0, description="saved-session redirect")
            logger.info("Saved session redirected to {} — skipping login form.", self.page.url)
            return
        except (TimeoutError, LoginTimeoutError):
            # Saved session is expired — fall through to credential pre-fill.
            pass

        if headless:
            logger.info("Headless mode: attempting credential-based login...")

        _PLACEHOLDER_EMAILS = {"your@email.com", "your-email@example.com"}
        _PLACEHOLDER_PASSWORDS = {"your-portal-password"}

        email = os.environ.get("MCD_PORTAL_EMAIL", "").strip()
        password = os.environ.get("MCD_PORTAL_PASSWORD", "").strip()
        have_real_creds = (
            bool(email) and email not in _PLACEHOLDER_EMAILS
            and bool(password) and password not in _PLACEHOLDER_PASSWORDS
        )
        # SSO / email-only mode: MCD_PORTAL_EMAIL set but MCD_PORTAL_PASSWORD absent.
        # We auto-fill just the email and submit; the portal redirects to the
        # corporate SSO provider which handles authentication from there.
        have_sso_email = (
            bool(email) and email not in _PLACEHOLDER_EMAILS and not password
        )
        if have_real_creds:
            await self.fill_credentials(email, password)
        elif have_sso_email:
            await self.fill_email_sso(email)
        else:
            if headless:
                raise RuntimeError(
                    "Headless mode requires MCD_PORTAL_EMAIL and MCD_PORTAL_PASSWORD in config/.env. "
                    "Set them and retry, or run 'mcd-key-automation init-session' headfully first."
                )
            logger.info(
                "MCD_PORTAL_EMAIL / MCD_PORTAL_PASSWORD not set — "
                "complete sign-in manually in the browser window..."
            )

        # In headless mode allow up to 2 minutes for SSO/MFA to complete after
        # credential pre-fill — 45 s was too short when the portal is slow or
        # when an MFA prompt appears.
        effective_timeout = 120.0 if headless else timeout_s

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

        try:
            await wait_until(authenticated, timeout_s=effective_timeout, description="authenticated session")
        except (TimeoutError, LoginTimeoutError):
            if headless:
                raise RuntimeError(
                    "Session expired or MFA required — cannot complete login in headless mode.\n"
                    "Run 'mcd-key-automation init-session' to refresh your session, then retry."
                ) from None
            raise

        logger.info("Authenticated — landed on {}", self.page.url)
