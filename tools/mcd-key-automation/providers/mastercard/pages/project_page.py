"""Sandbox credentials page object (/project-details/<uuid>/sandbox)."""
from __future__ import annotations

import asyncio
from pathlib import Path

from loguru import logger
from playwright.async_api import Page

from browser.downloads import save_download
from providers.mastercard.selectors import AddProjectKeySelectors, SandboxSelectors


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

    async def has_oauth1_key_section(self) -> bool:
        """Return True if this project uses OAuth 1.0a (has 'Add project key' button)."""
        try:
            await self.page.wait_for_selector(
                SandboxSelectors.add_project_key_button, timeout=5000
            )
            return True
        except Exception:
            return False

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
