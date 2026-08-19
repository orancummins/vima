"""Stable selectors for the Mastercard Developers portal.

Captured 2026-05-26 via tools/mcd-key-automation/discover.py. See
logs/discovery.json and logs/dom/*.html for raw evidence.
"""
from __future__ import annotations


class LoginSelectors:
    # Detection of authenticated state is via URL change (page no longer contains /account/log-in).
    sign_in_link = "a[href*='log-in']"

    # Login form — verify / update with discover.py if auto-fill fails.
    # Run: cd tools/mcd-key-automation && .venv/bin/python discover.py
    # then inspect logs/dom/*.html for the actual input selectors.
    email_input = "input[type='email'], input[name='email'], #email, input[name='identifier']"
    password_input = "input[type='password'], input[name='password'], #password"
    submit_button = "button[type='submit'], input[type='submit'], button:has-text('Sign in'), button:has-text('Log in')"


class AccountApiKeySelectors:
    """Account page → 'Developers API Keys' section.

    Used to provision the Mastercard **Developers API** (admin) key — the
    bootstrap credential that lets us later manage projects/keys via the
    documented Developers API instead of driving the portal UI.

    Portal ref (Quick Start Guide): Account → Developers API Keys → Add key →
    Browser Keystore → Generate key → Key name + Key password → accept T&C →
    Create key → Download key → read Consumer key from the section.

    Every entry is a comma-separated list of fallbacks so a single portal
    redesign (data-testid churn, relabelled buttons) degrades gracefully.
    Prefer role/label/text locators over data-testid — they survive UI
    refactors far better.
    """

    # Candidate account URLs, tried in order until the section renders.
    account_urls = (
        "https://developer.mastercard.com/account/profile",
        "https://developer.mastercard.com/account",
        "https://developer.mastercard.com/account/api-keys",
    )

    # The 'Developers API Keys' section anchor — used to confirm we're on the
    # right page before interacting.
    section_heading = (
        "text=/Developers API Keys/i, "
        "h1:has-text('Developers API'), h2:has-text('Developers API'), "
        "h3:has-text('Developers API'), [data-testid*='developers-api']"
    )

    # 'Add key' link/button inside the Developers API Keys section.
    add_key_button = (
        "[data-testid*='add'][data-testid*='key'], "
        "a:has-text('Add key'), button:has-text('Add key'), "
        "[role='button']:has-text('Add key')"
    )

    # The 'Create Developers API key' modal container — used to confirm the
    # dialog actually opened after clicking 'Add key'.
    dialog = (
        "[role='dialog']:has-text('Create Developers API key'), "
        "[class*='modal']:has-text('Create Developers API key'), "
        "[role='dialog']:has-text('How would you like to create')"
    )

    # Step 1 — 'Generate key' toggle (vs 'Upload a CSR'). Selected by default,
    # so clicking it is optional/idempotent.
    browser_keystore_option = (
        "button:has-text('Generate key'), [role='tab']:has-text('Generate key'), "
        "[role='radio']:has-text('Generate key'), text='Generate key'"
    )

    # Step 2 — key name + key password inputs (ground-truth data-testids).
    key_name_input = (
        "[data-testid='key-name-input'], "
        "input[name='developersKeyForm.keyName'], "
        "input[placeholder='Enter key name']"
    )
    key_password_input = (
        "[data-testid='key-password-input'], "
        "input[name='developersKeyForm.keyPassword'], "
        "input[placeholder='Enter key password']"
    )

    # Terms & Conditions — a per-agreement checkbox that must be ticked to
    # enable 'Create key'. The id/name embeds a per-tenant agreement UUID.
    terms_checkbox = (
        "[data-testid$='-consent'], "
        "input[name^='legalAgreements.'], "
        "input[type='checkbox'][id^='legalAgreements']"
    )
    terms_accept_button = (
        "button:has-text('Accept'), button:has-text('Agree'), "
        "button:has-text('I agree'), [role='button']:has-text('Accept')"
    )

    # 'Create key' submit button (disabled until the form is valid + T&C ticked).
    create_key_button = (
        "[data-testid='create-key-btn'], [data-testid='create-btn'], "
        "button:has-text('Create key'), button:has-text('Create Key'), "
        "[role='button']:has-text('Create key')"
    )

    # 'Download key' button — only appears for the Browser Keystore path, where
    # the keypair is generated client-side and must be downloaded immediately.
    download_key_button = (
        "[data-testid='download-key-btn'], [data-testid='Download'], "
        "button:has-text('Download key'), button:has-text('Download Key'), "
        "a:has-text('Download key'), button:has-text('Download key file')"
    )

    # A confirmation that the request was submitted (key enters 'Pending' state,
    # reviewed within 3 business days) when no immediate download is offered.
    submitted_confirmation = (
        "text=/reviewed within 3 business days/i, "
        "text=/you.?ll receive an email/i, "
        "[data-testid*='pending'], text=/Pending/"
    )

    # Consumer key value shown in the Developers API Keys table after creation.
    # The table renders even while the key is PENDING approval.
    consumer_key_value = (
        "[data-testid$='-fingerprint-0'], "
        "[data-testid*='consumer-key'], [data-testid*='consumerKey'], "
        "[data-testid='bar-value']"
    )

    # Keys-table anchors (ground truth from discover_admin_key_table.py).
    keys_card = "[data-testid='developer-keys-card']"
    key_name_row_any = "[data-testid^='key-name-']"
    status_pill = "[data-testid='pill-testid']"


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

    # Existing Mastercard Signature Verification Key row.
    # Region-agnostic: the data-testid is prefixed by the service slug, which is
    # "open-finance" for the US tenant but "open-finance-au" for Australia, so we
    # match on the stable suffix rather than a hardcoded prefix.
    sig_key_name_any = "[data-testid*='mastercard-signature-verification-key-name-']"
    # The download link is inside a Bootstrap dropdown — must open toggle first
    sig_key_manage_toggle = "[data-testid*='-manage-0'] button, [data-testid='mastercard-signature-verification-manage-key'] button"
    sig_key_download = "[data-testid='Download']"

    # Add key wizard (creates new sig verification key). Region-agnostic prefix so
    # it matches both 'add-encryption-key-open-finance' and '...-open-finance-au'.
    add_sig_key_button = "[data-testid^='add-encryption-key-']"
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
    # Plaintext consumer-key value sits next to each key-name in the same row.
    oauth_consumer_key_value_any = "[data-testid='bar-value']"
    # "Rotate key" links — one per key row. Use .nth(n) to target a specific key.
    rotate_key_link = "a:has-text('Rotate key')"


class AddProjectKeySelectors:
    """Add-project-key wizard at /sandbox/add-project-key."""

    # Step 1 — choose key type (Add Key wizard)
    generate_new_radio_label = "label[for='1']"

    # Step 1 of the Rotate wizard — the step container test id for targeting the correct Proceed button.
    rotate_step1_proceed = "[data-testid='stepview-selectMethod'] [data-testid='proceed-btn']"

    # Step 2 of the Rotate wizard — "Set private key" (Generate new / existing / CSR)
    rotate_step2_proceed = "[data-testid='stepview-SetYourPrivateKey'] [data-testid='proceed-btn']"
    # Fallback radio label visible in Step 2 (confirms we've advanced from Step 1)
    rotate_step2_generate_new_radio = "label:has-text('Generate a new private key')"

    # Step 3 — fill alias and password (same for Add Key and Rotate wizards)
    key_alias_input = "[data-testid='key-alias-input']"
    key_store_password_input = "[data-testid='key-store-password-input']"

    proceed_button = "button:has-text('Proceed')"
    create_key_button = "button:has-text('Create key')"

    # Post-creation — same button text as the project-creation confirmation page.
    download_key_button = "button:has-text('Download key file')"
    download_key_heading = "h2:has-text('You are almost done'), h3:has-text('You are almost done')"


# API slug lookup is now in providers.mastercard.api_config.API_CONFIG.
# This shim keeps imports that still use API_SLUGS working.
from providers.mastercard.api_config import API_CONFIG as _API_CONFIG  # noqa: E402
API_SLUGS: dict[str, str] = {k: v.slug for k, v in _API_CONFIG.items()}

