"""Per-API setup instructions for the Mastercard Developers portal.

Each API entry defines EXACTLY how to create a project and provision keys for it.
All API-specific portal knowledge lives here — the workflow layer just dispatches
on ``provision_type``.

provision_type values:
    "oauth1_standard"    Standard OAuth 1.0a: Step1 → Step2 (alias+password) → download zip
    "oauth1_enc_key"     OAuth 1.0a but wizard downloads a client encryption .pem; signing key
                         must be added separately via sandbox "Add project key"
    "oauth2_region"      OAuth 2.0 with mandatory region dropdown on Step 1 (e.g. Open Finance)
    "priceless"          Must select a sub-API card before proceeding (requires API Owner approval)
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ApiSetup:
    slug: str
    provision_type: str = "oauth1_standard"
    # Optional: region dropdown value to select in Step 1 (oauth2_region only)
    region: str | None = None
    # Optional: sub-API card/checkbox label to click in Step 1
    api_selection: str | None = None


API_CONFIG: dict[str, ApiSetup] = {
    # --- Standard OAuth 1.0a (Step1 → Step2 → zip download) ---
    "binlookup": ApiSetup(slug="bin-lookup"),
    "places":    ApiSetup(slug="places"),
    "easysavings": ApiSetup(slug="easy-savings-specials"),
    "txnotify":  ApiSetup(slug="transaction-notifications"),
    "ofpub":     ApiSetup(slug="presentment"),
    "ofmc":      ApiSetup(slug="eop-admin"),

    # --- OAuth 1.0a with client encryption key (wizard downloads .pem; signing key added separately) ---
    "clarity":   ApiSetup(slug="consumer-clarity",   provision_type="oauth1_enc_key"),
    "consent":   ApiSetup(slug="consent-management", provision_type="oauth1_enc_key"),
    "eligibility": ApiSetup(slug="eligibility-api",  provision_type="oauth1_enc_key"),
    "bces":      ApiSetup(slug="bces-service",        provision_type="oauth1_enc_key"),

    # --- OAuth 2.0 with mandatory region selection ---
    "ofin": ApiSetup(
        slug="ofin",
        provision_type="oauth2_region",
        region="United States of America",
    ),

    # --- Priceless: must select sub-API card (requires API Owner approval) ---
    "priceless": ApiSetup(
        slug="priceless-cities",
        provision_type="priceless",
        api_selection="Priceless Specials",
    ),
}
