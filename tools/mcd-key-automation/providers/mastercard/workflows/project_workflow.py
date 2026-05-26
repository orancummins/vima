"""Project lifecycle workflow."""
from __future__ import annotations

from pathlib import Path

from loguru import logger

from app.models import ProjectSpec
from providers.mastercard.pages.create_project_page import CreateProjectPage
from providers.mastercard.pages.dashboard_page import DashboardPage
from providers.mastercard.selectors import API_SLUGS, CreateProjectSelectors


async def ensure_project_with_api(
    dashboard: DashboardPage,
    project: ProjectSpec,
    api_name: str,
    workspace: Path,
) -> Path:
    """
    Ensure the project exists and return the downloaded raw key file path.

    Strategy:
      1. Check dashboard for existing project with same name.
      2. If absent, use the fast-path URL (/create-project?services=<slug>)
         which pre-selects the API in the creation wizard.
      3. Fill form (name + No on-behalf-of), click Proceed.
      4. On confirmation page, click 'Download key file'.
    """
    page = dashboard.page

    # Re-check dashboard for existing project
    if await dashboard.has_project(project.name):
        logger.info("Project {!r} already exists — skipping creation", project.name)
        # Key download from existing projects is a future phase (project detail page).
        raise NotImplementedError(
            f"Project {project.name!r} exists; existing-project key download not yet implemented."
        )

    api_slug = API_SLUGS.get(api_name, api_name)
    fast_path = CreateProjectSelectors.fast_path_url_tpl.format(api_slug=api_slug)
    logger.info("Navigating to create-project fast-path: {}", fast_path)
    await page.goto(fast_path, wait_until="domcontentloaded")

    create_page = CreateProjectPage(page)
    await create_page.wait_for_form()
    await create_page.fill(project_name=project.name, on_behalf_of_company=False)
    await create_page.proceed()
    await create_page.wait_for_confirmation()

    dest_dir = workspace / "downloads"
    dest_dir.mkdir(parents=True, exist_ok=True)
    raw_file = await create_page.download_key_file(dest_dir=dest_dir, filename_hint=f"{project.name}-{api_name}")
    logger.info("Raw key file: {}", raw_file)
    return raw_file

