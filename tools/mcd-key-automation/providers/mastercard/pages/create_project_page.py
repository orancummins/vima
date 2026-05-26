"""Create-project form page object."""
from __future__ import annotations

from pathlib import Path

from loguru import logger
from playwright.async_api import Page

from browser.downloads import save_download
from providers.mastercard.selectors import CreateProjectSelectors, ProjectCreatedSelectors


class CreateProjectPage:
    """Handles the multi-step create-project wizard."""

    def __init__(self, page: Page) -> None:
        self.page = page

    async def wait_for_form(self) -> None:
        await self.page.wait_for_selector(CreateProjectSelectors.name_input, timeout=20000)

    async def fill(self, *, project_name: str, on_behalf_of_company: bool = False, region: str | None = None) -> None:
        logger.info("Filling create-project form: name={!r} on_behalf={} region={!r}", project_name, on_behalf_of_company, region)

        # Project name
        await self.page.fill(CreateProjectSelectors.name_input, project_name)

        # On behalf of a company? Default No.
        label_text = "Yes" if on_behalf_of_company else "No"
        await self.page.locator(f"label:has-text('{label_text}')").first.click()

        # If company selected, the react-select becomes visible and needs a value.
        if on_behalf_of_company:
            raise NotImplementedError("Company selection not yet implemented")

        # Region dropdown (only present for some APIs e.g. Open Finance)
        if region:
            region_loc = self.page.locator(CreateProjectSelectors.region_select_input)
            if await region_loc.count() > 0:
                logger.info("Selecting region: {!r}", region)
                await region_loc.click()
                await self.page.locator(f"li:has-text('{region}'), [role='option']:has-text('{region}')").first.click()

    async def proceed(self) -> None:
        logger.info("Clicking Proceed")
        await self.page.locator(CreateProjectSelectors.proceed_button).click()

    async def wait_for_confirmation(self, timeout_ms: int = 30000) -> None:
        """Wait for the post-creation confirmation page."""
        await self.page.wait_for_selector(ProjectCreatedSelectors.heading, timeout=timeout_ms)
        logger.info("Project creation confirmed — at {}", self.page.url)

    async def wait_for_confirmation_or_project_page(self, timeout_ms: int = 30000) -> bool:
        """
        Wait for either the confirmation page or the project detail page.
        Returns True if we landed on the project detail page (confirmation was skipped),
        False if we're on the normal confirmation page.
        """
        import asyncio as _asyncio
        deadline = timeout_ms / 1000
        poll_interval = 0.5
        elapsed = 0.0
        while elapsed < deadline:
            url = self.page.url
            if "/project-details/" in url and "/create-project" not in url:
                logger.info("Landed on project detail page (confirmation skipped) — {}", url)
                return True
            if await self.page.locator(ProjectCreatedSelectors.heading).count() > 0:
                logger.info("Landed on confirmation page — {}", url)
                return False
            await _asyncio.sleep(poll_interval)
            elapsed += poll_interval
        raise TimeoutError(f"Neither confirmation nor project page appeared within {timeout_ms}ms")

    async def download_key_file(self, *, dest_dir: Path, filename_hint: str = "key") -> Path:
        """Click 'Download key file' and save the file."""
        logger.info("Clicking 'Download key file'")
        async with self.page.expect_download() as dl_info:
            await self.page.locator(ProjectCreatedSelectors.download_key_button).click()
        download = await dl_info.value
        original = download.suggested_filename or f"{filename_hint}.p12"
        dest = dest_dir / original
        await save_download(download, dest)
        logger.info("Downloaded key file: {}", dest)
        return dest

    async def open_project(self) -> str:
        """Click 'Open project' and return the resulting URL."""
        async with self.page.expect_navigation():
            await self.page.locator(ProjectCreatedSelectors.open_project_button).click()
        logger.info("Opened project — at {}", self.page.url)
        return self.page.url
