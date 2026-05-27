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
    # Optional provisioning UX note shown in auto-provision selection UI.
    provision_note: str = ""
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
        display_name="Open Finance",
        auth=AUTH_OAUTH2,
        categories=("Auth", "Customers", "Data Connect", "Accounts", "Transactions",
                    "Reports", "Webhooks"),
        docs_url="https://developer.mastercard.com/open-finance-us/documentation/",
        legacy_id="ofin",
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
        provision_note="Requires API Owner approval",
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
    ),
    ApiCatalogEntry(
        id="offers_for_publishers",
        env_prefix="OFFERS_FOR_PUBLISHERS",
        portal_slug="presentment",
        display_name="Offers for Publishers",
        auth=AUTH_OAUTH1,
        categories=("Offers",),
        docs_url="https://developer.mastercard.com/presentment/documentation/",
        legacy_id="ofpub",
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
    "ApiCatalogEntry",
    "CATALOG",
    "LEGACY_TO_ID",
    "iter_ordered",
    "get",
    "by_portal_slug",
    "env_var",
]
