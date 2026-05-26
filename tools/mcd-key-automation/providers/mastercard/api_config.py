"""Per-API setup instructions for the Mastercard Developers portal.

Each entry defines EXACTLY how to create a project and provision keys for an
API. All API-specific portal knowledge lives here — the workflow layer just
dispatches on ``provision_type``.

The ``slug`` (URL slug used on developer.mastercard.com) and the set of APIs
are derived from ``apis.catalog`` so the canonical vima catalog stays the
single source of truth. We key by **legacy id** here because YAML configs and
artifact filenames downloaded from prior runs still embed the legacy ids.

provision_type values:
    "oauth1_standard"    Standard OAuth 1.0a: Step1 → Step2 (alias+password) → download zip
    "oauth1_enc_key"     OAuth 1.0a but wizard downloads a client encryption .pem; signing key
                         must be added separately via sandbox "Add project key"
    "oauth2_region"      OAuth 2.0 with mandatory region dropdown on Step 1 (e.g. Open Finance)
    "priceless"          Must select a sub-API card before proceeding (requires API Owner approval)
"""
from __future__ import annotations

from dataclasses import dataclass

from app._vima_catalog import (
    AUTH_OAUTH1_ENC,
    AUTH_OAUTH2,
    iter_ordered,
)


@dataclass(frozen=True)
class ApiSetup:
    slug: str
    provision_type: str = "oauth1_standard"
    # Optional: region dropdown value to select in Step 1 (oauth2_region only)
    region: str | None = None
    # Optional: sub-API card/checkbox label to click in Step 1
    api_selection: str | None = None


# Special-case overrides keyed by the catalog id.
_REGION_BY_ID: dict[str, str] = {
    "open_finance": "United States of America",
}
_SPECIAL_BY_ID: dict[str, dict] = {
    "priceless_cities": {
        "provision_type": "priceless",
        "api_selection": "Priceless Specials",
    },
}


def _provision_type(entry) -> str:
    if entry.id in _SPECIAL_BY_ID:
        return _SPECIAL_BY_ID[entry.id]["provision_type"]
    if entry.auth == AUTH_OAUTH2:
        return "oauth2_region"
    if entry.auth == AUTH_OAUTH1_ENC:
        return "oauth1_enc_key"
    return "oauth1_standard"


def _build_api_config() -> dict[str, ApiSetup]:
    """Register each API under both its canonical id and its legacy id.

    YAML configs and downloaded artifact filenames may use either form; the
    workflow layer just does ``API_CONFIG[name]`` so both must resolve.
    """
    cfg: dict[str, ApiSetup] = {}
    for entry in iter_ordered():
        kwargs: dict = {
            "slug": entry.portal_slug,
            "provision_type": _provision_type(entry),
        }
        if entry.id in _REGION_BY_ID:
            kwargs["region"] = _REGION_BY_ID[entry.id]
        special = _SPECIAL_BY_ID.get(entry.id, {})
        if "api_selection" in special:
            kwargs["api_selection"] = special["api_selection"]
        setup = ApiSetup(**kwargs)
        # Canonical id (e.g. 'bin_lookup', 'open_finance')
        cfg[entry.id] = setup
        # Legacy id (e.g. 'binlookup', 'ofin') — keeps old YAMLs + artifacts working
        if entry.legacy_id and entry.legacy_id != entry.id:
            cfg[entry.legacy_id] = setup
    return cfg


API_CONFIG: dict[str, ApiSetup] = _build_api_config()
