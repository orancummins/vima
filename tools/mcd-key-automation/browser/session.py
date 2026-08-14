"""Playwright session manager.

Headful chromium with persistent storage state. Provides a context manager that yields
a (browser, context, page) tuple ready for orchestration to drive.
"""
from __future__ import annotations

import contextlib
import os
from pathlib import Path
from typing import AsyncIterator

from loguru import logger
from playwright.async_api import (
    Browser,
    BrowserContext,
    Page,
    async_playwright,
)


STATE_FILE = Path(__file__).parent.parent / "session_state.json"

# Allow forcing a system-installed browser channel (e.g. "msedge", "chrome")
# when the bundled Playwright chromium download is blocked by corp networks.
# Set PLAYWRIGHT_BROWSER_CHANNEL=msedge in the environment to drive system Edge.
_BROWSER_CHANNEL = os.environ.get("PLAYWRIGHT_BROWSER_CHANNEL", "").strip() or None


@contextlib.asynccontextmanager
async def browser_session(
    *,
    headless: bool = False,
    storage_state: Path | None = STATE_FILE,
    downloads_dir: Path | None = None,
) -> AsyncIterator[tuple[Browser, BrowserContext, Page]]:
    async with async_playwright() as pw:
        launch_kwargs: dict = {
            "headless": headless,
            "args": ["--foreground"] if not headless else [],
        }
        if _BROWSER_CHANNEL:
            launch_kwargs["channel"] = _BROWSER_CHANNEL
            logger.info("Using system browser channel: {}", _BROWSER_CHANNEL)
        browser = await pw.chromium.launch(**launch_kwargs)
        ctx_kwargs: dict = {"accept_downloads": True}
        if storage_state and storage_state.exists():
            logger.info("Reusing saved session from {}", storage_state)
            ctx_kwargs["storage_state"] = str(storage_state)
        if downloads_dir:
            downloads_dir.mkdir(parents=True, exist_ok=True)
        context = await browser.new_context(**ctx_kwargs)
        page = await context.new_page()
        await page.bring_to_front()
        try:
            yield browser, context, page
        finally:
            try:
                if storage_state:
                    await context.storage_state(path=str(storage_state))
                    logger.info("Saved session state to {}", storage_state)
            except Exception as e:
                logger.warning("Failed to save session state: {}", e)
            await context.close()
            await browser.close()
