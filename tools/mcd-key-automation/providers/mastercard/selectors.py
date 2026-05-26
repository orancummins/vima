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
    # Region dropdown (present for some APIs e.g. Open Finance)
    region_select_input = "[placeholder='Type to search']"
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

    # Navigation tabs on the project detail page.
    sandbox_tab = "[data-testid='option-sandbox']"


class OAuth2SandboxSelectors:
    """OAuth 2.0 sandbox page selectors (Partner ID / App Key / Secret + Sig Verification Key)."""

    # Credentials card
    partner_id_value = "[data-testid='credentialscard-partnerid']"
    app_key_show = "[data-testid^='icon-show-credentials-appKey-']"
    app_key_value = "[data-testid^='bar-value-credentials-appKey-']"
    secret_show = "[data-testid^='icon-show-credentialscard-secret-']"
    secret_value = "[data-testid^='bar-value-credentialscard-secret-']"

    # Existing Mastercard Signature Verification Key row
    sig_key_name_any = "[data-testid^='open-finance-mastercard-signature-verification-key-name-']"
    # The download link is inside a Bootstrap dropdown — must open toggle first
    sig_key_manage_toggle = "[data-testid='open-finance-manage-0'] button, [data-testid='mastercard-signature-verification-manage-key'] button"
    sig_key_download = "[data-testid='Download']"

    # Add key wizard (creates new sig verification key)
    add_sig_key_button = "[data-testid='add-encryption-key-open-finance']"
    sig_key_proceed = "[data-testid='proceed-btn']"
    sig_key_create = "[data-testid='create-btn']"
    sig_key_download_after_create = "button:has-text('Download'), a:has-text('Download'), [data-testid='Download']"


class SandboxSelectors:
    """Sandbox credentials page at /project-details/<uuid>/sandbox."""

    sandbox_url_tpl = "https://developer.mastercard.com/project-details/{uuid}/sandbox"

    # OAuth (project-level) keys section
    add_project_key_button = "[data-testid='add-key-button']"
    # Existing keys rendered as data-testid="key-name-0", "key-name-1" etc.
    oauth_key_name_any = "[data-testid^='key-name-']"
    rotate_key_link = "a:has-text('Rotate key')"


class AddProjectKeySelectors:
    """Add-project-key wizard at /sandbox/add-project-key."""

    # Step 1 — choose key type
    generate_new_radio_label = "label[for='1']"

    # Step 2 — fill alias and password
    key_alias_input = "[data-testid='key-alias-input']"
    key_store_password_input = "[data-testid='key-store-password-input']"

    proceed_button = "button:has-text('Proceed')"
    create_key_button = "button:has-text('Create key')"

    # Post-creation — same button text as the project-creation confirmation page.
    download_key_button = "button:has-text('Download key file')"
    download_key_heading = "h2:has-text('You are almost done'), h3:has-text('You are almost done')"


# Known API slugs used in the fast-path URL.
API_SLUGS: dict[str, str] = {
    "binlookup": "bin-lookup",
    "ofin": "ofin",
}

