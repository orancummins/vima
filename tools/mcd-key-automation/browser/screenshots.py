"""Screenshot helpers for failure diagnostics."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from loguru import logger
from playwright.async_api import Page

SCREENSHOT_DIR = Path(__file__).parent.parent / "logs" / "screenshots"


async def capture(page: Page, label: str) -> Path:
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in label)
    out = SCREENSHOT_DIR / f"{stamp}_{safe}.png"
    try:
        await page.screenshot(path=str(out), full_page=True)
        logger.info("Captured screenshot {}", out)
    except Exception as e:
        logger.warning("Screenshot failed: {}", e)
    return out
