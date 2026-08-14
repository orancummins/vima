"""API enrollment workflow (placeholder)."""
from __future__ import annotations

from loguru import logger

from app.models import ProjectSpec
from providers.mastercard.pages.project_page import ProjectPage


async def attach_api(project_page: ProjectPage, project: ProjectSpec, api: str) -> None:
    logger.info("Attaching API {!r} to project {!r}", api, project.name)
    raise NotImplementedError
