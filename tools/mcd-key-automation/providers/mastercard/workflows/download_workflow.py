"""Download workflow (placeholder)."""
from __future__ import annotations

from pathlib import Path

from loguru import logger

from app.models import ProjectSpec
from providers.mastercard.pages.api_page import ApiPage


async def download_keys(api_page: ApiPage, project: ProjectSpec, api: str, dest_dir: Path) -> list[Path]:
    logger.info("Downloading keys for {}/{}", project.name, api)
    raise NotImplementedError
