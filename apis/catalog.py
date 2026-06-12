"""Canonical catalog of every Mastercard Developers API integrated by vima.

This module is the **single source of truth** for an API's identity:

    * ``id``           — short, unique, snake_case identifier. **Also the folder
                          name** under ``apis/`` and ``simulator/handlers/`` and
                          the fixture filename stem.
    * ``env_prefix``   — uppercase prefix used for every credential variable in
                          ``config/.env`` (e.g. ``BIN_LOOKUP_CONSUMER_KEY``).
    * ``portal_slug``  — slug used on developer.mastercard.com (drives the URL
                          for "Add API", "Generate keys", etc.).
    * ``display_name`` — formal product name shown in the UI ("BIN Lookup",
                          "Open Finance", "Consumer Clarity").
    * ``auth``         — credential schema: ``oauth1``, ``oauth1_enc``, ``oauth2``.
    * ``categories``   — high-level grouping tags shown in the UI.
    * ``docs_url``     — link to the official docs landing page.
    * ``legacy_id``    — previous short id (pre-formal-naming). Used by the
                          ``.env`` migration helper so users don't lose creds.

The order of ``CATALOG`` determines display order in the Explorer tab and the
home page.  Adding a new Mastercard API is now a one-line catalog entry plus
the matching ``apis/<id>/api.py`` module.
"""
from __future__ import annotations

import importlib
import os
from dataclasses import dataclass, field
from typing import Iterable, Optional


# ---------------------------------------------------------------------------
# Auth schemas
# ---------------------------------------------------------------------------

AUTH_OAUTH1 = "oauth1"            # PKCS#12 signing key only
AUTH_OAUTH1_ENC = "oauth1_enc"    # PKCS#12 + client encryption PEM
AUTH_OAUTH2 = "oauth2"            # Partner ID / Secret / App Key (Finicity)
AUTH_JWT_RS256 = "jwt_rs256"      # OAuth 2.0 client_credentials with RS256-
                                  # signed JWT client assertion (Aiia / EU)


# ---------------------------------------------------------------------------
# Product groupings
# ---------------------------------------------------------------------------
#
# Mirrors the top-level categorization used on developer.mastercard.com so the
# VIMA sidebar groups APIs the same way a developer would find them on the
# Mastercard Developers portal.
#
# The order of GROUP_ORDER drives the rendering order of group headings.

GROUP_OPEN_FINANCE = "Open Banking & Open Finance"
GROUP_SECURITY = "Security & Risk"
GROUP_DATA = "Data & Insights"
GROUP_LOYALTY = "Loyalty, Offers & Benefits"

GROUP_ORDER: tuple[str, ...] = (
    GROUP_OPEN_FINANCE,
    GROUP_SECURITY,
    GROUP_DATA,
    GROUP_LOYALTY,
)


# ---------------------------------------------------------------------------
# Disabled APIs
# ---------------------------------------------------------------------------
#
# APIs listed here are kept in the catalog (their code/spec/checklist remain
# intact) but are hidden from the sidebar API list AND the provisioning modal.
# Use this for APIs that cannot be auto-provisioned today and are not yet
# ready for end-user exposure — they can be re-enabled later by removing the
# id from this set.
#
# Currently disabled:
#   * flight_delay_pass — manual tenant onboarding (~26 days) + JWE; not
#                         usable end-to-end until Mastercard tenant onboarding
#                         is complete and the encryption client is wired in.
#
# Open Finance Europe is intentionally NOT in this set: it is exposed in the
# UI with a disabled "Manual onboarding" pill so partners can discover it.

DISABLED_API_IDS: frozenset[str] = frozenset({
    "flight_delay_pass",
    "carbon_calculator",
})


def is_disabled(api_id: str) -> bool:
    return api_id in DISABLED_API_IDS


# ---------------------------------------------------------------------------
# Catalog entry
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ApiCatalogEntry:
    id: str
    env_prefix: str
    portal_slug: str
    display_name: str
    auth: str
    categories: tuple[str, ...] = ()
    docs_url: str = ""
    legacy_id: Optional[str] = None
    # Top-level Mastercard Developers product grouping (see GROUP_* above).
    # Drives sidebar section headings in the API explorer.
    group: str = GROUP_DATA
    # Optional provisioning UX note shown in auto-provision selection UI.
    provision_note: str = ""
    # When False, the API cannot be auto-provisioned via the portal-wizard
    # flow — the provisioning modal will disable the checkbox and show the
    # ``manual_onboarding_url`` instead so the user can request access.
    auto_provisionable: bool = True
    manual_onboarding_url: str = ""
    # Sibling APIs that pair naturally with this one. Surfaced as
    # "Often paired with" chips on the API detail panel. Free-form
    # ordering — closest pair first. See ``apis/bundles.py`` for the
    # solution-shaped bundle definitions that aggregate these pairings.
    complements: tuple[str, ...] = ()
    # Hard prerequisites — APIs whose credentials must be in place for
    # *this* API to be useful (e.g. Easy Savings needs a BIN to query
    # against; any Open Finance use case needs a Consent mandate first).
    requires: tuple[str, ...] = ()
    # Optional override; defaults to ``apis.<id>.api``.
    module_path: Optional[str] = None

    @property
    def folder(self) -> str:
        """Folder name on disk — identical to ``id`` by design."""
        return self.id

    @property
    def module_name(self) -> str:
        return self.module_path or f"apis.{self.id}.api"

    def load_module(self):
        return importlib.import_module(self.module_name)


# ---------------------------------------------------------------------------
# The catalog
# ---------------------------------------------------------------------------
# Order here drives display order in the UI.

_ENTRIES: tuple[ApiCatalogEntry, ...] = (
    ApiCatalogEntry(
        id="open_finance",
        env_prefix="OPEN_FINANCE",
        portal_slug="ofin",
        display_name="Open Finance US",
        auth=AUTH_OAUTH2,
        categories=("Auth", "Customers", "Data Connect", "Accounts", "Transactions",
                    "Reports", "Webhooks"),
        docs_url="https://developer.mastercard.com/open-finance-us/documentation/",
        legacy_id="ofin",
        group=GROUP_OPEN_FINANCE,
        complements=("consumer_clarity", "merchant_identifier", "places", "carbon_calculator", "consent_management"),
    ),
    ApiCatalogEntry(
        id="open_finance_au",
        env_prefix="OPEN_FINANCE_AU",
        # Same portal product as US Open Finance — the wizard selects the
        # variant via the Commercial Countries dropdown (Australia vs USA).
        portal_slug="ofin",
        display_name="Open Finance Australia",
        auth=AUTH_OAUTH2,
        categories=("Auth", "Customers", "Connect", "Accounts", "Transactions",
                    "Consent (CDR)", "Reports", "Webhooks"),
        docs_url="https://developer.mastercard.com/open-finance-au/documentation/",
        legacy_id=None,
        group=GROUP_OPEN_FINANCE,
        provision_note="",
        complements=("consumer_clarity", "merchant_identifier", "places", "carbon_calculator", "consent_management"),
    ),
    ApiCatalogEntry(
        id="open_finance_eu",
        env_prefix="OPEN_FINANCE_EU",
        # The Aiia-backed EU stack is a distinct product family from
        # Finicity-backed US/AU. Onboarding is manual: an onboarding officer
        # provisions a clientId and adds the partner's public RSA cert to the
        # trust list. No portal-wizard provisioning slug at this time.
        portal_slug="ofin-eu",
        display_name="Open Finance Europe",
        auth=AUTH_JWT_RS256,
        categories=("Auth", "Providers", "Consent", "Accounts",
                    "Transactions", "Balances", "Insights"),
        docs_url="https://developer.mastercard.com/open-finance-data/documentation/",
        legacy_id=None,
        group=GROUP_OPEN_FINANCE,
        provision_note=(
            "Manual onboarding only — email openbankingeu_support@mastercard.com "
            "with your RSA-4096 public PEM to receive a sandbox clientId."
        ),
        auto_provisionable=False,
        manual_onboarding_url="https://openbankingeu.mastercard.com/contact-us",
        complements=("consumer_clarity", "merchant_identifier", "places", "carbon_calculator", "consent_management"),
    ),
    ApiCatalogEntry(
        id="bin_lookup",
        env_prefix="BIN_LOOKUP",
        portal_slug="bin-lookup",
        display_name="BIN Lookup",
        auth=AUTH_OAUTH1,
        categories=("Lookup",),
        docs_url="https://developer.mastercard.com/bin-lookup/documentation/",
        legacy_id="binlookup",
        group=GROUP_DATA,
        complements=("easy_savings", "benefits_eligibility", "business_payment_controls", "match", "merchant_identifier"),
    ),
    ApiCatalogEntry(
        id="merchant_identifier",
        env_prefix="MERCHANT_IDENTIFIER",
        portal_slug="merchant-identifier",
        display_name="Merchant Identifier",
        auth=AUTH_OAUTH1,
        categories=("Merchant", "Lookup"),
        docs_url="https://developer.mastercard.com/merchant-identifier/documentation/",
        legacy_id=None,
        group=GROUP_DATA,
        complements=("consumer_clarity", "places", "open_finance", "match"),
    ),
    ApiCatalogEntry(
        id="automatic_billing_updater",
        env_prefix="AUTOMATIC_BILLING_UPDATER",
        portal_slug="automatic-billing-updater",
        display_name="Automatic Billing Updater",
        auth=AUTH_OAUTH1,
        categories=("Card Lifecycle", "Subscriptions"),
        docs_url="https://developer.mastercard.com/automatic-billing-updater/documentation/",
        legacy_id=None,
        group=GROUP_DATA,
        provision_note="Push operations require ABU Push service registration",
        complements=("open_finance", "transaction_notifications", "consent_management"),
    ),
    ApiCatalogEntry(
        id="match",
        env_prefix="MATCH",
        portal_slug="match",
        display_name="MATCH Pro",
        auth=AUTH_OAUTH1,
        categories=("Risk", "Merchants"),
        docs_url="https://developer.mastercard.com/match/documentation/",
        legacy_id=None,
        group=GROUP_SECURITY,
        complements=("merchant_identifier", "bin_lookup", "consumer_clarity"),
    ),
    ApiCatalogEntry(
        id="consumer_clarity",
        env_prefix="CONSUMER_CLARITY",
        portal_slug="consumer-clarity",
        display_name="Consumer Clarity",
        auth=AUTH_OAUTH1_ENC,
        categories=("Merchant Search",),
        docs_url="https://developer.mastercard.com/consumer-clarity-us/documentation/",
        legacy_id="clarity",
        group=GROUP_DATA,
        complements=("merchant_identifier", "places", "open_finance"),
    ),
    ApiCatalogEntry(
        id="priceless_cities",
        env_prefix="PRICELESS_CITIES",
        portal_slug="priceless-cities",
        display_name="Priceless Cities",
        auth=AUTH_OAUTH1,
        categories=("Offers",),
        docs_url="https://developer.mastercard.com/priceless-cities/documentation/",
        legacy_id="priceless",
        group=GROUP_LOYALTY,
        provision_note="Requires API Owner approval",
        complements=("places", "offers_for_publishers", "easy_savings"),
    ),
    ApiCatalogEntry(
        id="easy_savings",
        env_prefix="EASY_SAVINGS",
        portal_slug="easy-savings-specials",
        display_name="Easy Savings",
        auth=AUTH_OAUTH1,
        categories=("Offers",),
        docs_url="https://developer.mastercard.com/easy-savings/documentation/",
        legacy_id="easysavings",
        group=GROUP_LOYALTY,
        complements=("offers_for_publishers", "offers_merchant_content", "places"),
        requires=("bin_lookup",),
    ),
    ApiCatalogEntry(
        id="places",
        env_prefix="PLACES",
        portal_slug="places",
        display_name="Places",
        auth=AUTH_OAUTH1,
        categories=("Location",),
        docs_url="https://developer.mastercard.com/places/documentation/",
        legacy_id="places",
        group=GROUP_DATA,
        complements=("consumer_clarity", "merchant_identifier", "priceless_cities", "easy_savings"),
    ),
    ApiCatalogEntry(
        id="offers_for_publishers",
        env_prefix="OFFERS_FOR_PUBLISHERS",
        portal_slug="presentment",
        display_name="Offers for Publishers",
        auth=AUTH_OAUTH1_ENC,
        categories=("Offers",),
        docs_url="https://developer.mastercard.com/presentment/documentation/",
        legacy_id="ofpub",
        group=GROUP_LOYALTY,
        complements=("offers_merchant_content", "easy_savings", "places"),
    ),
    ApiCatalogEntry(
        id="offers_merchant_content",
        env_prefix="OFFERS_MERCHANT_CONTENT",
        portal_slug="eop-admin",
        display_name="Offers Merchant Content",
        auth=AUTH_OAUTH1,
        categories=("Offers",),
        docs_url="https://developer.mastercard.com/eop-admin/documentation/",
        legacy_id="ofmc",
        group=GROUP_LOYALTY,
        complements=("offers_for_publishers", "easy_savings", "merchant_identifier"),
    ),
    ApiCatalogEntry(
        id="consent_management",
        env_prefix="CONSENT_MANAGEMENT",
        portal_slug="consent-management",
        display_name="Consent Management",
        auth=AUTH_OAUTH1_ENC,
        categories=("Consent", "3DS"),
        docs_url="https://developer.mastercard.com/consent-management/documentation/",
        legacy_id="consent",
        group=GROUP_SECURITY,
        complements=("open_finance", "automatic_billing_updater", "transaction_notifications"),
    ),
    ApiCatalogEntry(
        id="transaction_notifications",
        env_prefix="TRANSACTION_NOTIFICATIONS",
        portal_slug="transaction-notifications",
        display_name="Transaction Notifications",
        auth=AUTH_OAUTH1,
        categories=("Notifications",),
        docs_url="https://developer.mastercard.com/transaction-notifications/documentation/",
        legacy_id="txnotify",
        group=GROUP_DATA,
        complements=("open_finance", "automatic_billing_updater", "consent_management"),
    ),
    ApiCatalogEntry(
        id="benefits_eligibility",
        env_prefix="BENEFITS_ELIGIBILITY",
        portal_slug="eligibility-api",
        display_name="Benefits Eligibility",
        auth=AUTH_OAUTH1_ENC,
        categories=("Benefits",),
        docs_url="https://developer.mastercard.com/eligibility-api/documentation/",
        legacy_id="eligibility",
        group=GROUP_LOYALTY,
        provision_note="Requires API Owner approval",
        complements=("benefits_content_eligibility", "flight_delay_pass"),
        requires=("bin_lookup",),
    ),
    ApiCatalogEntry(
        id="benefits_content_eligibility",
        env_prefix="BENEFITS_CONTENT_ELIGIBILITY",
        portal_slug="bces-service",
        display_name="Benefits Content Eligibility Service",
        auth=AUTH_OAUTH1_ENC,
        categories=("Benefits",),
        docs_url="https://developer.mastercard.com/bces-service/documentation/",
        legacy_id="bces",
        group=GROUP_LOYALTY,
        complements=("benefits_eligibility", "flight_delay_pass"),
    ),
    ApiCatalogEntry(
        id="enhanced_currency_conversion_calculator",
        env_prefix="ENHANCED_CURRENCY_CONVERSION_CALCULATOR",
        portal_slug="enhanced-currency-conversion-calculator",
        display_name="Enhanced Currency Conversion Calculator",
        auth=AUTH_OAUTH1,
        categories=("FX", "Settlement"),
        docs_url="https://developer.mastercard.com/enhanced-currency-conversion-calculator/documentation/",
        legacy_id=None,
        group=GROUP_DATA,
        provision_note="Requires API Owner approval",
        complements=("business_payment_controls",),
    ),
    ApiCatalogEntry(
        id="flight_delay_pass",
        env_prefix="FLIGHT_DELAY_PASS",
        portal_slug="flight-delay-pass",
        display_name="Flight Delay Pass",
        # OAuth 1.0a + JWE payload encryption for PII operations
        # (POST /registrations, PUT /registrations/{id}).
        auth=AUTH_OAUTH1_ENC,
        categories=("Benefits", "Loyalty", "Eligibility", "Registrations"),
        docs_url="https://developer.mastercard.com/flight-delay-pass/documentation/",
        legacy_id=None,
        group=GROUP_LOYALTY,
        # Issuer must be on-boarded by a Mastercard implementation team as a
        # Flight Delay Pass tenant (≤26 days) and the project's Client Key
        # must be whitelisted before the sandbox will return 2xx. The
        # self-serve portal wizard can mint OAuth1 keys but the API will
        # 403 until the tenant onboarding is complete.
        provision_note=(
            "Manual onboarding only — issuer must be provisioned as a Flight "
            "Delay Pass tenant (~26 days) and the Client Key whitelisted."
        ),
        auto_provisionable=False,
        manual_onboarding_url="https://developer.mastercard.com/flight-delay-pass/documentation/",
        complements=("benefits_eligibility", "benefits_content_eligibility"),
    ),
    ApiCatalogEntry(
        id="carbon_calculator",
        env_prefix="CARBON_CALCULATOR",
        portal_slug="carbon-calculator",
        display_name="Carbon Calculator",
        # OAuth 1.0a + JWE payload encryption on payment-card registration ops.
        auth=AUTH_OAUTH1_ENC,
        categories=("Sustainability", "Service Provider", "Payment Cards",
                    "Environmental Impact", "Engagement"),
        docs_url="https://developer.mastercard.com/carbon-calculator/documentation/",
        legacy_id=None,
        group=GROUP_DATA,
        # Sandbox project creation requires a Mastercard-issued Customer ID
        # (CID), Legal Name, and BIN range — none of which the portal wizard
        # can supply autonomously. Contact carboncalculator@mastercard.com.
        provision_note=(
            "Manual onboarding only — requires Mastercard-issued Customer ID, "
            "Legal Name and BIN range. Contact carboncalculator@mastercard.com."
        ),
        auto_provisionable=False,
        manual_onboarding_url="https://developer.mastercard.com/create-project/carbon-calculator?services=carbon-calculator",
        complements=("open_finance", "consumer_clarity", "merchant_identifier"),
    ),
    ApiCatalogEntry(
        id="business_payment_controls",
        env_prefix="BUSINESS_PAYMENT_CONTROLS",
        portal_slug="business-payment-controls",
        display_name="Business Payment Controls",
        # Standard OAuth 1.0a (signing key + consumer key). Payload encryption
        # is *optional* per Mastercard FAQ — only enable JWE if your project
        # has uploaded a Client Encryption key; default is unencrypted.
        auth=AUTH_OAUTH1,
        categories=("Real Cards", "Virtual Cards", "Funding Sources",
                    "Controls", "Custom Data", "Authorization Reports",
                    "Clearing Reports"),
        docs_url="https://developer.mastercard.com/business-payment-controls/documentation/",
        legacy_id=None,
        # Commercial-card spend controls — closest fit to Security & Risk
        # (controls limit spending, prevent unauthorised use).
        group=GROUP_SECURITY,
        # Provisioning wizard requires a Mastercard-issued *registration
        # token* (free-text field on Step 2). Auto-provisioning is wired
        # via a recorded playbook; the token defaults to ``123456789`` in
        # the playbook's ``defaults`` block for now — swap for a real
        # token issued by your Mastercard Commercial Products manager.
        provision_note=(
            "Requires a registration token from your Mastercard Commercial "
            "Products implementation manager (default in playbook: 123456789)."
        ),
        complements=("bin_lookup", "transaction_notifications", "enhanced_currency_conversion_calculator"),
    ),
)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

CATALOG: dict[str, ApiCatalogEntry] = {e.id: e for e in _ENTRIES}

# Reverse lookup by legacy id (used by the .env migration helper).
LEGACY_TO_ID: dict[str, str] = {
    e.legacy_id: e.id for e in _ENTRIES if e.legacy_id
}


def iter_ordered() -> Iterable[ApiCatalogEntry]:
    """Iterate entries in display order."""
    return iter(_ENTRIES)


def get(api_id: str) -> Optional[ApiCatalogEntry]:
    """Look up by canonical id; falls back to legacy id."""
    if api_id in CATALOG:
        return CATALOG[api_id]
    return CATALOG.get(LEGACY_TO_ID.get(api_id, ""))


def by_portal_slug(slug: str) -> Optional[ApiCatalogEntry]:
    for e in _ENTRIES:
        if e.portal_slug == slug:
            return e
    return None


def env_var(api_id: str, suffix: str) -> str:
    """Build an env var name: ``<env_prefix>_<SUFFIX>``."""
    entry = get(api_id)
    if entry is None:
        raise KeyError(f"Unknown API id: {api_id!r}")
    return f"{entry.env_prefix}_{suffix}"


__all__ = [
    "AUTH_OAUTH1",
    "AUTH_OAUTH1_ENC",
    "AUTH_OAUTH2",
    "AUTH_JWT_RS256",
    "ApiCatalogEntry",
    "CATALOG",
    "LEGACY_TO_ID",
    "iter_ordered",
    "get",
    "by_portal_slug",
    "env_var",
]
