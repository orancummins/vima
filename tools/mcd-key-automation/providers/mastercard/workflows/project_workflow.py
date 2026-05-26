"""Project lifecycle workflow."""
from __future__ import annotations

from pathlib import Path

from loguru import logger

from app.models import AppConfig, ProjectSpec
from providers.mastercard.pages.create_project_page import CreateProjectPage
from providers.mastercard.pages.dashboard_page import DashboardPage
from providers.mastercard.pages.project_page import AddProjectKeyPage, SandboxPage
from providers.mastercard.selectors import API_SLUGS, CreateProjectSelectors


async def ensure_project_with_api(
    dashboard: DashboardPage,
    project: ProjectSpec,
    api_name: str,
    workspace: Path,
    config: AppConfig,
    region: str | None = None,
) -> Path:
    """
    Ensure the project exists and return the downloaded raw key file path.

    Strategy for NEW projects:
      1. Use the fast-path URL (/create-project?services=<slug>) which pre-selects
         the API and lands on a confirmation page with 'Download key file'.

    Strategy for EXISTING projects:
      1. Get the project UUID from the dashboard link href.
      2. Navigate to /project-details/<uuid>/sandbox.
      3. Click 'Add project key' → fill the wizard → download the p12.
    """
    page = dashboard.page
    dest_dir = workspace / "downloads"
    dest_dir.mkdir(parents=True, exist_ok=True)

    if await dashboard.has_project(project.name):
        logger.info("Project {!r} already exists — using sandbox key flow", project.name)
        uuid = await dashboard.get_project_uuid(project.name)
        if not uuid:
            raise RuntimeError(f"Could not determine UUID for project {project.name!r}")

        sandbox = SandboxPage(page)
        await sandbox.goto(uuid)
        direct_download = await sandbox.click_add_project_key()

        add_key_page = AddProjectKeyPage(page)

        if direct_download:
            # Portal generated the key and presented the download page directly (no wizard)
            raw_file = await add_key_page.download_key_file(
                dest_dir=dest_dir,
                filename_hint=f"{project.name}-{api_name}",
            )
            logger.info("Raw key file (direct download): {}", raw_file)
            return raw_file

        await add_key_page.wait_for_form()
        await add_key_page.select_generate_new()
        await add_key_page.proceed()
        await add_key_page.fill_credentials(
            alias=api_name,
            password=config.key_password,
        )
        await add_key_page.create_key()
        raw_file = await add_key_page.download_key_file(
            dest_dir=dest_dir,
            filename_hint=f"{project.name}-{api_name}",
        )
        logger.info("Raw key file (existing project): {}", raw_file)
        return raw_file

    api_slug = API_SLUGS.get(api_name, api_name)
    fast_path = CreateProjectSelectors.fast_path_url_tpl.format(api_slug=api_slug)
    logger.info("Navigating to create-project fast-path: {}", fast_path)
    await page.goto(fast_path, wait_until="domcontentloaded")

    create_page = CreateProjectPage(page)
    await create_page.wait_for_form()
    await create_page.fill(project_name=project.name, on_behalf_of_company=False, region=region)
    await create_page.proceed()

    # The portal sometimes skips the confirmation page and goes straight to the project detail.
    # Detect which page we landed on and fall through to sandbox key flow if needed.
    landed_on_project = await create_page.wait_for_confirmation_or_project_page()

    if landed_on_project:
        # Project was created but confirmation page was skipped — use sandbox key flow.
        logger.info("Confirmation page skipped — falling back to sandbox key flow for new project")
        uuid = page.url.rstrip("/").split("/project-details/")[-1].split("/")[0]
        sandbox = SandboxPage(page)
        await sandbox.goto(uuid)
        await sandbox.click_add_project_key()

        add_key_page = AddProjectKeyPage(page)
        await add_key_page.wait_for_form()
        await add_key_page.select_generate_new()
        await add_key_page.proceed()
        await add_key_page.fill_credentials(alias=api_name, password=config.key_password)
        await add_key_page.create_key()
        raw_file = await add_key_page.download_key_file(
            dest_dir=dest_dir,
            filename_hint=f"{project.name}-{api_name}",
        )
        logger.info("Raw key file (new project, sandbox fallback): {}", raw_file)
        return raw_file

    raw_file = await create_page.download_key_file(
        dest_dir=dest_dir,
        filename_hint=f"{project.name}-{api_name}",
    )
    logger.info("Raw key file (new project): {}", raw_file)
    return raw_file

