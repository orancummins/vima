"""Sandbox credentials page object (/project-details/<uuid>/sandbox)."""
from __future__ import annotations

import asyncio
import json
from pathlib import Path

from loguru import logger
from playwright.async_api import Page

from browser.downloads import save_download
from providers.mastercard.selectors import AddProjectKeySelectors, OAuth2SandboxSelectors, SandboxSelectors


class OAuth2SandboxPage:
    """Handles the sandbox page for OAuth 2.0 projects (Partner ID / App Key / Secret + Sig Key)."""

    def __init__(self, page: Page) -> None:
        self.page = page

    async def extract_credentials(self) -> dict[str, str]:
        """Read OAuth 2.0 credentials, revealing masked values via the show icons."""
        partner_id = (await self.page.locator(OAuth2SandboxSelectors.partner_id_value).first.text_content() or "").strip()

        show_app = self.page.locator(OAuth2SandboxSelectors.app_key_show)
        if await show_app.count() > 0:
            await show_app.first.click()
            await asyncio.sleep(0.5)
        app_key = (await self.page.locator(OAuth2SandboxSelectors.app_key_value).first.text_content() or "").strip()

        show_secret = self.page.locator(OAuth2SandboxSelectors.secret_show)
        if await show_secret.count() > 0:
            await show_secret.first.click()
            await asyncio.sleep(0.5)
        secret = (await self.page.locator(OAuth2SandboxSelectors.secret_value).first.text_content() or "").strip()

        logger.info("Extracted OAuth 2.0 credentials (partner_id={})", partner_id)
        return {"partner_id": partner_id, "app_key": app_key, "secret": secret}

    async def has_signature_key(self) -> bool:
        """Return True if a Mastercard Signature Verification Key already exists."""
        return await self.page.locator(OAuth2SandboxSelectors.sig_key_name_any).count() > 0

    async def download_existing_signature_key(self, *, dest_dir: Path, filename_hint: str = "sig_key") -> Path:
        """Click Download on the existing Mastercard Signature Verification Key row."""
        logger.info("Downloading existing Mastercard Signature Verification Key")
        # The Download link is inside a Bootstrap dropdown — open the toggle first
        toggle = self.page.locator(OAuth2SandboxSelectors.sig_key_manage_toggle)
        if await toggle.count() > 0:
            await toggle.first.click()
            await asyncio.sleep(1.0)  # wait for dropdown animation to complete
        async with self.page.expect_download() as dl_info:
            await self.page.locator(OAuth2SandboxSelectors.sig_key_download).first.click(force=True)
        download = await dl_info.value
        original = download.suggested_filename or f"{filename_hint}.zip"
        dest = dest_dir / original
        await save_download(download, dest)
        logger.info("Downloaded signature verification key: {}", dest)
        return dest

    async def add_signature_key(self, *, dest_dir: Path, filename_hint: str = "sig_key") -> Path:
        """Run the add-api-key wizard to create + download a new Mastercard Signature Verification Key."""
        logger.info("Clicking 'Add key' for Mastercard Signature Verification Key")
        await self.page.locator(OAuth2SandboxSelectors.add_sig_key_button).click()
        await self.page.wait_for_selector(OAuth2SandboxSelectors.sig_key_proceed, timeout=15000)
        await self.page.locator(OAuth2SandboxSelectors.sig_key_proceed).click()
        await self.page.wait_for_selector(OAuth2SandboxSelectors.sig_key_create, timeout=15000)
        logger.info("Clicking 'Create key' for signature verification key")
        await self.page.locator(OAuth2SandboxSelectors.sig_key_create).click()
        await self.page.wait_for_selector(OAuth2SandboxSelectors.sig_key_download_after_create, timeout=30000)
        logger.info("Downloading new Mastercard Signature Verification Key")
        async with self.page.expect_download() as dl_info:
            await self.page.locator(OAuth2SandboxSelectors.sig_key_download_after_create).first.click()
        download = await dl_info.value
        original = download.suggested_filename or f"{filename_hint}.zip"
        dest = dest_dir / original
        await save_download(download, dest)
        logger.info("Downloaded new signature verification key: {}", dest)
        return dest

    async def save_credentials_json(self, creds: dict[str, str], dest_dir: Path, filename: str) -> Path:
        """Serialise credentials dict to a JSON file and return the path."""
        dest = dest_dir / filename
        dest.write_text(json.dumps(creds, indent=2))
        logger.info("Saved OAuth 2.0 credentials JSON: {}", dest)
        return dest


class SandboxPage:
    """Handles the sandbox credentials page for an existing project."""

    def __init__(self, page: Page) -> None:
        self.page = page

    async def goto(self, project_uuid: str) -> None:
        url = SandboxSelectors.sandbox_url_tpl.format(uuid=project_uuid)
        logger.info("Navigating to sandbox page: {}", url)
        await self.page.goto(url, wait_until="domcontentloaded")
        try:
            await self.page.wait_for_load_state("networkidle", timeout=5000)
        except Exception:
            pass
        await asyncio.sleep(2)

    async def has_project_key(self) -> bool:
        """Return True if at least one OAuth project key already exists."""
        return await self.page.locator(SandboxSelectors.oauth_key_name_any).count() > 0

    async def key_count(self) -> int:
        """Return the number of existing OAuth project keys."""
        return await self.page.locator(SandboxSelectors.oauth_key_name_any).count()

    async def click_rotate_key(self, idx: int = 0) -> bool:
        """
        Click 'Rotate key' for the key at index ``idx`` (0 = first/oldest).

        The 'Rotate key' option is hidden inside a 3-dot (⋮) dropdown menu per key row.
        This method opens the dropdown for the target row, then clicks 'Rotate key'.

        Returns True if we landed directly on a download page (portal auto-generated the key),
        False if we landed on the wizard.
        Raises RuntimeError if no key rows or rotate links are found.
        """
        # Find the key-name element at the target index, then navigate to its row
        # to locate the per-row dropdown toggle (⋮ button).
        names = await self.page.locator(SandboxSelectors.oauth_key_name_any).all()
        if not names:
            raise RuntimeError("No key rows found on sandbox page — cannot rotate")
        target = min(idx, len(names) - 1)
        logger.info("Opening action menu for key at index {} (of {})", target, len(names))

        name_el = names[target]
        # Each row's ⋮ button is a dropdown toggle button inside the same <tr> container.
        row = await name_el.evaluate_handle(
            "el => el.closest('tr, [class*=\"key-row\"], [class*=\"credential\"]') || el.parentElement"
        )
        row_el = row.as_element()

        # Try to find the dropdown toggle (Bootstrap ⋮ button) inside the row.
        toggle = None
        for selector in [
            "button[data-testid*='manage']",
            "button.dropdown-toggle",
            "button[aria-haspopup='true']",
            "button[aria-expanded]",
            "button:has-text('⋮')",
            "button",  # last resort: any button in the row
        ]:
            el = await row_el.query_selector(selector)
            if el:
                toggle = el
                break

        if toggle:
            logger.info("Clicking dropdown toggle to reveal 'Rotate key' option")
            await toggle.click()
            await asyncio.sleep(0.5)

        # Now click the visible "Rotate key" item.
        rotate = self.page.locator(SandboxSelectors.rotate_key_link)
        count = await rotate.count()
        if count == 0:
            raise RuntimeError("'Rotate key' link not found after opening dropdown")
        logger.info("Clicking 'Rotate key'")
        await rotate.first.click()

        for _ in range(30):
            url = self.page.url
            if "add-project-key" in url or "rotate" in url:
                await asyncio.sleep(1)
                return False
            if await self.page.locator(AddProjectKeySelectors.download_key_button).count() > 0:
                logger.info("Rotate key presented download page directly")
                return True
            await asyncio.sleep(0.5)
        return False

    async def extract_consumer_key(self, alias: str | None = None) -> str | None:
        """
        Extract the OAuth 1.0a consumer key from the sandbox page.

        Strategy: the page lists keys as data-testid="key-name-N", with a sibling
        [data-testid='bar-value'] containing the plaintext consumer key.

        If ``alias`` is given, prefer the row whose key name text matches; otherwise
        return the consumer key from the *last* key row (the most recently created).
        """
        names = await self.page.locator(SandboxSelectors.oauth_key_name_any).all()
        if not names:
            logger.warning("No key rows found on sandbox page — cannot extract consumer key")
            return None

        target_idx: int | None = None
        if alias:
            for i, el in enumerate(names):
                txt = (await el.text_content() or "").strip()
                if txt == alias:
                    target_idx = i
                    # No break — keep iterating to find the LAST match.
                    # When the same alias is reused across runs, the portal adds a new key
                    # each time; the newest key is last in DOM order, and its consumer key
                    # must be paired with the most recently downloaded p12.
        if target_idx is None:
            # Default: newest = last row in DOM order
            target_idx = len(names) - 1

        # Each row contains exactly one bar-value sibling. Walk up to the row container
        # then locate the bar-value descendant.
        name_el = names[target_idx]
        row = await name_el.evaluate_handle("el => el.closest('tr, .row, [class*=\"row\"], li') || el.parentElement")
        try:
            bar_val_el = await row.as_element().query_selector("[data-testid='bar-value']")
            if bar_val_el:
                value = (await bar_val_el.text_content() or "").strip()
                if value:
                    logger.info("Extracted consumer key (alias={!r}, idx={}): {}...{}", alias, target_idx, value[:8], value[-4:] if len(value) > 12 else "")
                    return value
        except Exception:
            pass

        # Fallback: pick the bar-value at the same global index as the key-name.
        bar_values = await self.page.locator(SandboxSelectors.oauth_consumer_key_value_any).all()
        if target_idx < len(bar_values):
            value = (await bar_values[target_idx].text_content() or "").strip()
            if value:
                logger.info("Extracted consumer key by index (idx={}): {}...{}", target_idx, value[:8], value[-4:] if len(value) > 12 else "")
                return value

        logger.warning("Could not pair key-name-{} with a bar-value", target_idx)
        return None

    async def has_oauth1_key_section(self) -> bool:
        """Return True if this project uses OAuth 1.0a.

        Detected by either the 'Add project key' button being present OR by
        existing key-name rows (older projects may hide the add-button once a
        key exists but still use OAuth 1.0a).
        """
        try:
            await self.page.wait_for_selector(
                SandboxSelectors.add_project_key_button, timeout=5000
            )
            return True
        except Exception:
            pass
        # Fallback: existing key rows → also OAuth 1.0a
        return await self.page.locator(SandboxSelectors.oauth_key_name_any).count() > 0

    async def click_add_project_key(self) -> bool:
        """
        Click 'Add project key'. Returns True if we landed directly on a download page
        (portal auto-generated the key), False if we landed on the wizard.
        Raises RuntimeError if the button is not present (e.g. OAuth 2.0 project).
        """
        if not await self.has_oauth1_key_section():
            raise RuntimeError(
                "No 'Add project key' button found — project may use OAuth 2.0 credentials "
                "(Partner ID / App Key / Secret). Manual key download not supported yet."
            )
        logger.info("Clicking 'Add project key'")
        await self.page.locator(SandboxSelectors.add_project_key_button).click()
        # Wait for either the wizard URL or a direct download button (some APIs skip the wizard)
        for _ in range(30):
            url = self.page.url
            if "add-project-key" in url:
                await asyncio.sleep(1)
                return False
            if await self.page.locator(AddProjectKeySelectors.download_key_button).count() > 0:
                logger.info("Portal presented download page directly (no wizard)")
                return True
            await asyncio.sleep(0.5)
        # Default: assume wizard
        return False


class AddProjectKeyPage:
    """Handles the add-project-key wizard (/sandbox/add-project-key)."""

    def __init__(self, page: Page) -> None:
        self.page = page

    async def wait_for_form(self) -> None:
        await self.page.wait_for_selector(
            AddProjectKeySelectors.generate_new_radio_label, timeout=20000
        )

    async def select_generate_new(self) -> None:
        """Select 'Generate a new private key' option."""
        logger.info("Selecting 'Generate a new private key'")
        await self.page.locator(AddProjectKeySelectors.generate_new_radio_label).click()

    async def proceed(self) -> None:
        """Click Proceed and wait for the alias/password step (browser key gen may take a moment)."""
        logger.info("Clicking Proceed on add-project-key wizard")
        await self.page.locator(AddProjectKeySelectors.proceed_button).click()
        await self.page.wait_for_selector(
            AddProjectKeySelectors.key_alias_input, timeout=30000
        )
        # Allow browser-side key generation to complete before filling the form
        await asyncio.sleep(2)

    async def proceed_rotate_step1(self) -> None:
        """
        Click the Step 1 Proceed button in the 'Rotate project key' wizard.

        Step 1 = "Select a method" (Rotate key / Renew key).  After clicking, waits
        for Step 2 "Set private key" to become visible (not the alias input — that's Step 3).
        """
        logger.info("Clicking Proceed on rotate-project-key wizard (Step 1)")
        btn = self.page.locator(AddProjectKeySelectors.rotate_step1_proceed)
        if await btn.count() == 0:
            btn = self.page.locator(AddProjectKeySelectors.proceed_button).first
        await btn.click()
        # Wait for Step 2 "Generate a new private key" radio to confirm transition
        await self.page.wait_for_selector(
            AddProjectKeySelectors.rotate_step2_generate_new_radio, timeout=30000
        )
        await asyncio.sleep(1)

    async def proceed_rotate_step2(self) -> None:
        """
        Click the Step 2 Proceed button in the 'Rotate project key' wizard.

        Step 2 = "Set private key" (Generate new / existing / CSR) — 'Generate a new
        private key' is pre-selected.  After clicking, waits for the Step 3 alias input.
        """
        logger.info("Clicking Proceed on rotate-project-key wizard (Step 2 — Set private key)")
        btn = self.page.locator(AddProjectKeySelectors.rotate_step2_proceed)
        if await btn.count() == 0:
            btn = self.page.locator(AddProjectKeySelectors.proceed_button).first
        await btn.click()
        await self.page.wait_for_selector(
            AddProjectKeySelectors.key_alias_input, timeout=30000
        )
        await asyncio.sleep(2)

    async def fill_credentials(self, alias: str, password: str) -> None:
        """Fill key alias and keystore password using keyboard events React can detect."""
        logger.info("Filling key alias={!r}", alias)
        alias_loc = self.page.locator(AddProjectKeySelectors.key_alias_input)
        await alias_loc.click()
        await alias_loc.clear()
        await alias_loc.type(alias, delay=50)

        pwd_loc = self.page.locator(AddProjectKeySelectors.key_store_password_input)
        await pwd_loc.click()
        await pwd_loc.clear()
        await pwd_loc.type(password, delay=50)
        # Give React time to validate and enable the submit button
        await asyncio.sleep(1)

    async def create_key(self) -> None:
        """Wait for 'Create key' to be enabled then click it."""
        logger.info("Waiting for 'Create key' button to be enabled")
        btn = self.page.locator(AddProjectKeySelectors.create_key_button)
        await btn.wait_for(state="visible", timeout=15000)
        # Poll until not disabled (React validation may take a moment)
        for _ in range(30):
            disabled = await btn.get_attribute("disabled")
            if disabled is None:
                break
            await asyncio.sleep(0.5)
        logger.info("Clicking 'Create key'")
        await btn.click()
        await self.page.wait_for_selector(
            AddProjectKeySelectors.download_key_button, timeout=30000
        )

    async def download_key_file(self, *, dest_dir: Path, filename_hint: str = "key") -> Path:
        """Click 'Download key file' and save the .p12 to dest_dir."""
        logger.info("Downloading key file from add-project-key wizard")
        async with self.page.expect_download() as dl_info:
            await self.page.locator(AddProjectKeySelectors.download_key_button).click()
        download = await dl_info.value
        original = download.suggested_filename or f"{filename_hint}.p12"
        dest = dest_dir / original
        await save_download(download, dest)
        logger.info("Downloaded key file: {}", dest)
        return dest
