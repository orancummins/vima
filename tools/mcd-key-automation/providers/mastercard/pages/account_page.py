"""Account page object — provisions the Mastercard **Developers API** (admin) key.

This is deliberately scoped to the single "Developers API Keys" flow on the
Account page (Quick Start Guide → Generate API Credentials). It does not touch
project provisioning; its job is to create + download the one bootstrap
credential that later lets us manage projects/keys via the documented
Developers API instead of driving the portal UI.

The portal UI changes often, so every interaction goes through the resilient
``_first`` helper which tries each comma-separated candidate selector in turn
and skips ones that aren't present/visible. Prefer role/label/text locators —
they survive redesigns far better than data-testid values.
"""
from __future__ import annotations

import asyncio
import re

from loguru import logger
from playwright.async_api import Locator, Page

from browser.downloads import save_download
from browser.screenshots import capture
from providers.mastercard.selectors import AccountApiKeySelectors as S


# Mastercard OAuth 1.0a consumer keys look like "<keyid>!<hash>", where the
# key id is base62 (alphanumeric, NOT hex) and the tail is hex, e.g.
# "AiKMBQK0B79g...875669!ef8224edcb...0000". Match alphanumerics on both sides.
_CONSUMER_KEY_RE = re.compile(r"[A-Za-z0-9]{16,}![A-Za-z0-9]{16,}")


def _candidates(spec: str) -> list[str]:
    """Split a comma-separated selector spec into individual candidate selectors."""
    return [part.strip() for part in spec.split(",") if part.strip()]


class AccountApiKeyPage:
    """Drives the Account → Developers API Keys section."""

    def __init__(self, page: Page) -> None:
        self.page = page

    # ------------------------------------------------------------------ utils
    async def _first(self, spec: str, *, timeout_ms: int = 8000) -> Locator | None:
        """Return the first visible locator among the candidates in ``spec``.

        Polls up to ``timeout_ms`` so late-rendering React content is caught.
        Returns ``None`` if nothing matched — callers decide whether that's
        fatal or an optional step (e.g. a T&C dialog that may not appear).
        """
        deadline = timeout_ms / 1000.0
        waited = 0.0
        step = 0.4
        while waited <= deadline:
            for sel in _candidates(spec):
                try:
                    loc = self.page.locator(sel).first
                    if await loc.count() > 0 and await loc.is_visible():
                        return loc
                except Exception:
                    continue
            await asyncio.sleep(step)
            waited += step
        return None

    async def _click(self, spec: str, desc: str, *, timeout_ms: int = 8000, required: bool = True) -> bool:
        loc = await self._first(spec, timeout_ms=timeout_ms)
        if loc is None:
            if required:
                await capture(self.page, f"admin_key_missing_{desc}")
                raise RuntimeError(
                    f"Could not find '{desc}' on the Developers API Keys flow. "
                    f"The portal UI may have changed — re-run discover.py and update "
                    f"AccountApiKeySelectors.{desc} in selectors.py. "
                    f"Screenshot saved to logs/screenshots/."
                )
            logger.info("Optional element '{}' not present — skipping", desc)
            return False
        logger.info("Clicking '{}'", desc)
        await loc.scroll_into_view_if_needed(timeout=3000)
        await loc.click(force=True)
        return True

    async def _fill(self, spec: str, value: str, desc: str, *, timeout_ms: int = 8000) -> None:
        loc = await self._first(spec, timeout_ms=timeout_ms)
        if loc is None:
            await capture(self.page, f"admin_key_missing_{desc}")
            raise RuntimeError(
                f"Could not find the '{desc}' field on the Developers API Keys flow. "
                f"Update AccountApiKeySelectors.{desc} in selectors.py."
            )
        logger.info("Filling '{}'", desc)
        await loc.scroll_into_view_if_needed(timeout=3000)
        await loc.click(force=True)
        try:
            await loc.fill(value)
        except Exception:
            await loc.press_sequentially(value, delay=40)

    async def _settle(self, timeout_ms: int = 8000) -> None:
        try:
            await self.page.wait_for_load_state("domcontentloaded", timeout=timeout_ms)
        except Exception:
            pass
        try:
            await self.page.wait_for_load_state("networkidle", timeout=timeout_ms)
        except Exception:
            pass
        await asyncio.sleep(1.0)

    # ------------------------------------------------------------------ steps
    async def goto(self) -> None:
        """Navigate to the Account page and confirm the API-keys section renders."""
        last_url = None
        for url in S.account_urls:
            logger.info("Navigating to account page: {}", url)
            await self.page.goto(url, wait_until="domcontentloaded")
            await self._settle()
            last_url = url
            heading = await self._first(S.section_heading, timeout_ms=6000)
            if heading is not None:
                logger.info("Found 'Developers API Keys' section on {}", url)
                return
            logger.info("Section not found on {} — trying next candidate URL", url)
        # Not fatal: the Add key button may still be present without the exact heading.
        logger.warning(
            "Could not confirm 'Developers API Keys' heading (last tried {}). "
            "Continuing — will look for the Add key button directly.", last_url,
        )

    async def open_add_key(self) -> None:
        """Click 'Add key' and confirm the create-key dialog actually opened.

        The account page is heavy and the modal is created on click, so retry
        the click until the dialog's key-name input becomes visible.
        """
        for attempt in range(1, 4):
            last = attempt == 3
            await self._click(S.add_key_button, "add_key_button", timeout_ms=12000, required=last)
            # Confirm the dialog opened by waiting for its key-name input.
            loc = await self._first(S.key_name_input, timeout_ms=6000)
            if loc is not None:
                logger.info("Create-key dialog is open")
                return
            logger.info("Dialog not visible after 'Add key' (attempt {}/3) — retrying", attempt)
            await asyncio.sleep(1.0)
        await capture(self.page, "admin_key_dialog_not_open")
        raise RuntimeError(
            "Clicked 'Add key' but the 'Create Developers API key' dialog did not open. "
            "Check logs/screenshots/ and AccountApiKeySelectors.add_key_button in selectors.py."
        )

    async def choose_generate_key(self) -> None:
        """Ensure the 'Generate key' (Browser Keystore) tab is selected.

        It is selected by default, so this click is optional/idempotent.
        """
        await self._click(
            S.browser_keystore_option, "browser_keystore_option",
            timeout_ms=4000, required=False,
        )
        await asyncio.sleep(0.3)

    async def fill_key_details(self, name: str, password: str) -> None:
        await self._fill(S.key_name_input, name, "key_name_input", timeout_ms=12000)
        await self._fill(S.key_password_input, password, "key_password_input")
        await asyncio.sleep(0.5)

    async def accept_terms_if_present(self) -> None:
        """Tick the Developers API T&C checkbox (required to enable 'Create key')."""
        loc = await self._first(S.terms_checkbox, timeout_ms=5000)
        if loc is not None:
            try:
                if not await loc.is_checked():
                    logger.info("Accepting Developers API Terms & Conditions (checkbox)")
                    await loc.check(force=True)
            except Exception:
                # Not a native checkbox — fall back to clicking it.
                await loc.click(force=True)
        else:
            logger.warning("Terms & Conditions checkbox not found — 'Create key' may stay disabled")
        # Some variants also present an explicit Accept button.
        await self._click(
            S.terms_accept_button, "terms_accept_button",
            timeout_ms=2000, required=False,
        )

    async def create_key(self) -> str:
        """Click 'Create key' and classify the outcome.

        Returns one of:
          - "download"  : a 'Download key' button appeared (Browser Keystore path);
                          caller should call download_key().
          - "submitted" : the request was accepted and the key is Pending review
                          (no immediate download available).
        """
        loc = await self._first(S.create_key_button, timeout_ms=8000)
        if loc is None:
            await capture(self.page, "admin_key_missing_create_key_button")
            raise RuntimeError(
                "Could not find the 'Create key' button. Update "
                "AccountApiKeySelectors.create_key_button in selectors.py."
            )
        # Wait until the button is enabled (React validates name/password/T&C first).
        for _ in range(30):
            disabled = await loc.get_attribute("disabled")
            aria_disabled = await loc.get_attribute("aria-disabled")
            if disabled is None and aria_disabled not in ("true", ""):
                break
            await asyncio.sleep(0.5)
        else:
            await capture(self.page, "admin_key_create_button_disabled")
            raise RuntimeError(
                "'Create key' stayed disabled — the key name, password, or T&C "
                "checkbox was not accepted. Check logs/screenshots/."
            )
        logger.info("Clicking 'Create key'")
        await loc.click(force=True)

        # Race: either a download button appears (client-side keygen) or a
        # 'Pending/reviewed' confirmation appears.
        deadline = 45.0
        waited = 0.0
        while waited < deadline:
            dl = await self._first(S.download_key_button, timeout_ms=1500)
            if dl is not None:
                logger.info("Download key button appeared — Browser Keystore path")
                return "download"
            conf = await self._first(S.submitted_confirmation, timeout_ms=1000)
            if conf is not None:
                logger.info("Key request submitted — Pending review (no immediate download)")
                return "submitted"
            await asyncio.sleep(1.0)
            waited += 3.5

        await capture(self.page, "admin_key_no_outcome_after_create")
        raise RuntimeError(
            "'Create key' clicked but neither a 'Download key' button nor a "
            "'Pending/reviewed' confirmation appeared within 45s. "
            "Check logs/screenshots/ — a validation error may be blocking."
        )

    async def download_key(self, *, dest_dir: str, filename_hint: str = "mcd-developers-api"):
        """Click 'Download key' and save the PKCS#12 keystore. Returns the saved Path."""
        from pathlib import Path

        loc = await self._first(S.download_key_button, timeout_ms=15000)
        if loc is None:
            await capture(self.page, "admin_key_missing_download_button")
            raise RuntimeError("'Download key' button not found.")
        logger.info("Downloading Developers API key file")
        async with self.page.expect_download() as dl_info:
            await loc.click(force=True)
        download = await dl_info.value
        original = download.suggested_filename or f"{filename_hint}.p12"
        dest = Path(dest_dir) / original
        await save_download(download, dest)
        logger.info("Downloaded Developers API key: {}", dest)
        return dest

    async def read_key_row(self, *, key_name: str | None = None) -> dict | None:
        """Read a Developers API key row: name, consumer_key, status.

        Navigates to the account page, waits for the keys card to render
        (the SPA can take 10-20s), then returns the row matching ``key_name``
        (or the first/only row if not given). Returns ``None`` if no key row
        is present yet.
        """
        await self.goto()
        # Wait for the keys card (or any key-name row) to render.
        anchor = await self._first(f"{S.keys_card}, {S.key_name_row_any}", timeout_ms=30000)
        if anchor is None:
            logger.info("No Developers API key row present yet on the Account page")
            return None

        # Scope all lookups to the keys card so we don't pick up the COMPANY
        # 'VERIFIED' pill or other unrelated elements on the account page.
        card = self.page.locator(S.keys_card).first
        if await card.count() == 0:
            card = self.page  # fall back to whole page

        rows = await card.locator(S.key_name_row_any).all()
        if not rows:
            return None

        target_idx = 0
        if key_name:
            for i, el in enumerate(rows):
                txt = (await el.text_content() or "").strip()
                if txt == key_name:
                    target_idx = i
                    break

        name = (await rows[target_idx].text_content() or "").strip()

        # The consumer-key span can render a beat after the key-name row — wait
        # for it (matching the Mastercard <hex>!<hex> pattern) up to ~15s.
        consumer_key: str | None = None
        for _ in range(15):
            fp = card.locator(f"[data-testid='{name}-fingerprint-{target_idx}']")
            if await fp.count() > 0:
                val = (await fp.first.text_content() or "").strip()
                if _CONSUMER_KEY_RE.search(val):
                    consumer_key = val
                    break
            bars = await card.locator(S.consumer_key_value).all()
            if target_idx < len(bars):
                val = (await bars[target_idx].text_content() or "").strip()
                if _CONSUMER_KEY_RE.search(val):
                    consumer_key = val
                    break
            await asyncio.sleep(1.0)

        # Status pill (PENDING / APPROVED / etc.) — scoped to the keys card.
        status: str | None = None
        pills = await card.locator(S.status_pill).all()
        if pills:
            try:
                status = (await pills[min(target_idx, len(pills) - 1)].text_content() or "").strip()
            except Exception:
                status = (await pills[0].text_content() or "").strip()

        logger.info("Key row: name={!r} status={!r} consumer_key={}",
                    name, status, "present" if consumer_key else "absent")
        return {"name": name, "consumer_key": consumer_key, "status": status}

    async def extract_consumer_key(self, *, key_name: str | None = None) -> str | None:
        """Return the consumer key for ``key_name`` from the keys table, or None.

        The table renders even while the key is PENDING, so this succeeds right
        after creation as long as we wait for the SPA to finish loading.
        """
        row = await self.read_key_row(key_name=key_name)
        if row and row.get("consumer_key"):
            return row["consumer_key"]

        # Fallback: scan the whole page's text for the consumer-key pattern.
        try:
            body = await self.page.locator("body").inner_text()
            match = _CONSUMER_KEY_RE.search(body)
            if match:
                logger.info("Extracted consumer key via page-text pattern match")
                return match.group(0)
        except Exception:
            pass

        logger.warning(
            "Could not auto-extract the consumer key. Copy it manually from the "
            "'Developers API Keys' section of your Account page."
        )
        return None
