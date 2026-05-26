"""Stable selectors for the Mastercard Developers portal.

Captured 2026-05-26 via tools/mcd-key-automation/discover.py. See
logs/discovery.json and logs/dom/*.html for raw evidence.
"""
from __future__ import annotations


class LoginSelectors:
    # Detection of authenticated state is via URL change (page no longer contains /account/log-in).
    sign_in_link = "a[href*='log-in']"


class DashboardSelectors:
    """Dashboard at https://developer.mastercard.com/dashboard"""

    page_heading = "h1:has-text('My projects'), h2:has-text('My projects')"
    create_project_button = "button:has-text('Create new project')"
    # Each existing project is rendered as <a href="/project-details/{uuid}">{name}</a>
    project_link_any = "a[href*='/project-details/']"

    @staticmethod
    def project_link_by_name(name: str) -> str:
        # Playwright will match exact text via :has-text(); name is user-controlled but only used for selection.
        return f"a[href*='/project-details/']:has-text({name!r})"


class CreateProjectSelectors:
    """Create-project form (opened from dashboard or via /create-project URL).

    Fast-path URL: https://developer.mastercard.com/create-project?services=<api-slug>
    e.g. ?services=bin-lookup → after submit lands on a 'Creating your project' confirmation
    page with a 'Download key file' button.
    """

    fast_path_url_tpl = "https://developer.mastercard.com/create-project?services={api_slug}"

    name_input = "#project-name"
    on_behalf_self_radio = "#ui\\.onBehalf-0"   # "On behalf of myself"
    on_behalf_company_radio = "#ui\\.onBehalf-1"  # "On behalf of a company"
    company_select_input = "#react-select-2-input"
    proceed_button = "button:has-text('Proceed')"
    exit_button = "button:has-text('Exit')"


class ProjectCreatedSelectors:
    """Post-creation confirmation page ('Creating your project')."""

    heading = "h1:has-text('Creating your project'), h2:has-text('Creating your project')"
    download_key_button = "button:has-text('Download key file')"
    open_project_button = "button:has-text('Open project')"


class ProjectSelectors:
    """Project detail page at /project-details/<uuid>."""

    # Placeholders — to be discovered via a follow-up pass that opens an existing project.
    add_api_button = "button:has-text('Add API')"
    api_search_input = "input[placeholder*='Search']"


# Known API slugs used in the fast-path URL.
API_SLUGS: dict[str, str] = {
    "binlookup": "bin-lookup",
    "ofin": "ofin",
}

