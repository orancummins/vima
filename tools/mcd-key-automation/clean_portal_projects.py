#!/usr/bin/env python3
"""Delete all Solution Studio ('SS-*') projects from Mastercard Developers portal.

Run standalone:
    python clean_portal_projects.py [--prefix SS]

Or called programmatically from clean_keys.py.
"""
from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path

# Make the tool's own packages importable.
_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

# Load MCD_PORTAL_EMAIL / MCD_PORTAL_PASSWORD from the vima root config/.env so
# LoginPage can pre-fill credentials automatically (no manual typing required).
_VIMA_ROOT = _HERE.parent.parent  # tools/mcd-key-automation → tools → vima root
_ENV_FILE = _VIMA_ROOT / "config" / ".env"


def _load_dotenv(path: Path) -> None:
    """Load a .env file into os.environ without overriding already-set variables."""
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


_load_dotenv(_ENV_FILE)

from loguru import logger
from playwright.async_api import Page

from browser.session import browser_session
from providers.mastercard.pages.dashboard_page import DashboardPage
from providers.mastercard.pages.login_page import LoginPage
from providers.mastercard.selectors import DashboardSelectors


LOGIN_URL = "https://developer.mastercard.com/account/log-in"
PROJECT_LINK_SEL = "a[href*='/project-details/']"


async def _ensure_authenticated(page: Page) -> None:
    """Navigate to login URL and wait for the user to complete SSO/MFA.

    Mirrors exactly how orchestrator.run() handles login — uses LoginPage
    which polls until the URL is back on developer.mastercard.com and no
    longer on /account/log-in (handles SSO/Ping/Okta redirects transparently).
    """
    login_page = LoginPage(page, LOGIN_URL)
    await login_page.goto()
    await login_page.wait_for_manual_auth()


async def _load_dashboard(page: Page) -> None:
    """Go to dashboard and wait until the page is fully loaded (project list rendered)."""
    dashboard = DashboardPage(page)
    await dashboard.goto()  # waits for 'Create new project' button — matches normal provisioning flow


async def _list_ss_projects(page: Page, prefix: str) -> list[tuple[str, str]]:
    """Return [(name, href), ...] for all projects whose name starts with `prefix`."""
    await _load_dashboard(page)
    links = await page.locator(PROJECT_LINK_SEL).all()
    results: list[tuple[str, str]] = []
    for link in links:
        name = (await link.inner_text()).strip()
        href = (await link.get_attribute("href")) or ""
        if name.startswith(prefix):
            results.append((name, href))
    return results


async def _delete_project(page: Page, name: str, href: str, base_url: str = "https://developer.mastercard.com") -> bool:
    """Navigate to a project detail page and click 'Delete this project' → confirm."""
    if href.startswith("http"):
        project_url = href
    else:
        project_url = base_url + href

    logger.info("Deleting project '{}' — navigating to {}", name, project_url)
    await page.goto(project_url, wait_until="domcontentloaded")
    try:
        await page.wait_for_load_state("networkidle", timeout=8000)
    except Exception:
        pass
    await asyncio.sleep(1)

    # Click "Delete this project" link/button.
    delete_selectors = [
        "a:has-text('Delete this project')",
        "button:has-text('Delete this project')",
        "text=Delete this project",
    ]
    clicked = False
    for sel in delete_selectors:
        loc = page.locator(sel)
        if await loc.count() > 0:
            await loc.first.click()
            clicked = True
            logger.info("Clicked 'Delete this project' for '{}'", name)
            break

    if not clicked:
        logger.warning("Could not find 'Delete this project' link for '{}' ({})", name, project_url)
        return False

    # Wait for confirmation dialog then click 'Yes' / 'Confirm' / 'Delete'.
    await asyncio.sleep(1.5)
    confirm_selectors = [
        "[role='dialog'] button:has-text('Yes')",
        "[role='dialog'] button:has-text('Delete')",
        "[role='dialog'] button:has-text('Confirm')",
        "button:has-text('Yes, delete')",
        "button:has-text('Yes')",
        "button:has-text('Confirm')",
    ]
    confirmed = False
    for sel in confirm_selectors:
        loc = page.locator(sel)
        if await loc.count() > 0:
            await loc.first.click()
            confirmed = True
            logger.info("Confirmed deletion of '{}'", name)
            break

    if not confirmed:
        logger.warning("Confirmation dialog not found for '{}' — project may not be deleted", name)
        return False

    # Wait for redirect back to dashboard / page update.
    await asyncio.sleep(3)
    return True


async def run_cleanup(prefix: str = "SS-") -> dict:
    """Open browser (reusing saved session), list SS projects, delete them all.

    Always navigates through the login flow (LoginPage.wait_for_manual_auth) so
    SSO/Ping/Okta redirects are handled transparently — same as provisioning runs.

    Returns a dict with 'deleted' and 'failed' lists.
    """
    result: dict = {"deleted": [], "failed": []}

    async with browser_session() as (_browser, _ctx, page):
        await _ensure_authenticated(page)

        projects = await _list_ss_projects(page, prefix)
        if not projects:
            logger.info("No projects found with prefix '{}'", prefix)
            return result

        logger.info("Found {} project(s) to delete: {}", len(projects), [n for n, _ in projects])

        for name, href in projects:
            ok = await _delete_project(page, name, href)
            if ok:
                result["deleted"].append(name)
            else:
                result["failed"].append(name)

        # Final check — refresh dashboard and report any that remain.
        remaining = await _list_ss_projects(page, prefix)
        if remaining:
            logger.warning("Still found {} project(s) after cleanup: {}", len(remaining), [n for n, _ in remaining])
            for name, _ in remaining:
                if name not in result["failed"]:
                    result["failed"].append(name)

    return result


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Delete SS-* projects from Mastercard Developers portal.")
    parser.add_argument("--prefix", default="SS-", help="Project name prefix to match (default: SS-)")
    args = parser.parse_args()

    logger.remove()
    logger.add(sys.stderr, level="INFO")

    r = asyncio.run(run_cleanup(prefix=args.prefix))
    if r["deleted"]:
        print(f"\n✓ Deleted {len(r['deleted'])} project(s):")
        for n in r["deleted"]:
            print(f"  • {n}")
    if r["failed"]:
        print(f"\n⚠ Failed to delete {len(r['failed'])} project(s):")
        for n in r["failed"]:
            print(f"  • {n}")
    if not r["deleted"] and not r["failed"]:
        print("No SS-* projects found.")

