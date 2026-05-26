"""Stable selectors for the Mastercard Developers portal.

PLACEHOLDERS — to be filled in during the discovery phase by inspecting the
authenticated portal DOM. Selectors MUST live only in this module.
"""
from __future__ import annotations


class LoginSelectors:
    sign_in_link = "a[href*='log-in']"
    email_input = "input[name='email']"
    password_input = "input[name='password']"
    submit_button = "button[type='submit']"
    # Marker indicating the user is authenticated (visible only after login).
    authenticated_marker = "[data-testid='user-menu'], a[href*='sign-out']"


class DashboardSelectors:
    new_project_button = "button:has-text('Create project')"
    project_list = "[data-testid='project-list']"
    project_link_tpl = "a[data-testid='project-link'][data-name='{name}']"


class ProjectSelectors:
    add_api_button = "button:has-text('Add API')"
    api_search_input = "input[placeholder*='Search']"
    api_card_tpl = "[data-testid='api-card'][data-slug='{slug}']"
    confirm_add_button = "button:has-text('Add')"


class ApiSelectors:
    generate_key_button = "button:has-text('Generate')"
    download_p12_button = "a:has-text('.p12'), button:has-text('Download .p12')"
    download_pem_button = "a:has-text('.pem'), button:has-text('Download .pem')"
