"""Project lifecycle workflow (placeholder)."""
from __future__ import annotations

from loguru import logger

from app.models import ProjectSpec
from providers.mastercard.pages.dashboard_page import DashboardPage


async def ensure_project(dashboard: DashboardPage, project: ProjectSpec) -> None:
    logger.info("Ensuring project {!r}", project.name)
    # Implementation pending DOM discovery.
    raise NotImplementedError
