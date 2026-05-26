"""Download helpers."""
from __future__ import annotations

import shutil
from pathlib import Path

from loguru import logger
from playwright.async_api import Download


async def save_download(download: Download, dest_path: Path) -> Path:
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = await download.path()
    if tmp is None:
        await download.save_as(str(dest_path))
        logger.info("Saved download to {}", dest_path)
        return dest_path
    shutil.copy2(tmp, dest_path)
    logger.info("Copied download {} -> {}", tmp, dest_path)
    return dest_path
