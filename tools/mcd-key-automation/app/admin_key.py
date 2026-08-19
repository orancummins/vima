"""Provision the Mastercard **Developers API** (admin) key.

Scoped, self-contained flow: log in to the portal, open the Account page's
'Developers API Keys' section, generate + download the PKCS#12 keystore, and
capture the consumer key. This is the one-time bootstrap credential for the
documented Mastercard Developers API — it is intentionally independent of the
per-API project provisioning in ``orchestrator.run``.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from loguru import logger

from browser.screenshots import capture
from browser.session import browser_session
from providers.mastercard.pages.account_page import AccountApiKeyPage
from providers.mastercard.pages.login_page import LoginPage


@dataclass
class AdminKeyResult:
    status: str  # "download" (p12 saved) or "submitted" (Pending review)
    key_path: Path | None
    consumer_key: str | None
    key_name: str
    key_password: str


async def run_admin_key(
    *,
    login_url: str,
    key_name: str,
    key_password: str,
    dest_dir: Path,
    headless: bool = False,
) -> AdminKeyResult:
    """Create/request the Developers API key and, if offered, download it."""
    dest_dir.mkdir(parents=True, exist_ok=True)

    async with browser_session(headless=headless, downloads_dir=dest_dir) as (_browser, _ctx, page):
        login = LoginPage(page, login_url=login_url)
        account = AccountApiKeyPage(page)
        try:
            await login.goto()
            await login.wait_for_manual_auth(headless=headless)
            logger.info("Authenticated — starting Developers API key provisioning")

            await account.goto()
            await account.open_add_key()
            await account.choose_generate_key()
            await account.fill_key_details(key_name, key_password)
            await account.accept_terms_if_present()
            status = await account.create_key()

            key_path: Path | None = None
            consumer_key: str | None = None
            if status == "download":
                key_path = await account.download_key(
                    dest_dir=str(dest_dir), filename_hint=key_name
                )
                consumer_key = await account.extract_consumer_key(key_name=key_name)
            else:
                logger.info(
                    "Developers API key request submitted — status Pending. "
                    "Mastercard reviews within ~3 business days; a download/consumer "
                    "key becomes available after approval."
                )
        except Exception as exc:
            logger.exception("Developers API key provisioning failed: {}", exc)
            await capture(page, "admin_key_failure")
            raise

    # Persist a small credentials sidecar next to the keystore for later use.
    creds = {
        "status": status,
        "consumer_key": consumer_key,
        "key_name": key_name,
        "key_alias": key_name,
        "key_file": key_path.name if key_path else None,
    }
    (dest_dir / "developers-api-credentials.json").write_text(json.dumps(creds, indent=2))

    return AdminKeyResult(
        status=status,
        key_path=key_path,
        consumer_key=consumer_key,
        key_name=key_name,
        key_password=key_password,
    )


async def sync_admin_key(
    *,
    login_url: str,
    key_name: str,
    headless: bool = False,
) -> dict | None:
    """Read the Developers API key row (name, consumer_key, status) — no creation.

    Used to auto-wire the consumer key into config/.env once the key exists,
    including while it is still PENDING (the portal shows the consumer key
    immediately; it only becomes usable against the API after approval).
    """
    async with browser_session(headless=headless) as (_browser, _ctx, page):
        login = LoginPage(page, login_url=login_url)
        account = AccountApiKeyPage(page)
        await login.goto()
        await login.wait_for_manual_auth(headless=headless)
        logger.info("Authenticated — reading Developers API key row")
        return await account.read_key_row(key_name=key_name)
