"""Bootstrap helper to import the vima ``apis.catalog`` module.

The mcd-key-automation tool lives under ``tools/mcd-key-automation/`` while
the canonical API catalog lives in ``apis/catalog.py`` at the vima repo root.
This shim adds the repo root to ``sys.path`` and re-exports the catalog API
plus a few helpers that map between the legacy ids still used inside this
tool (YAML configs, downloaded artifact filenames) and the canonical catalog.
"""
from __future__ import annotations

import sys
from pathlib import Path

_VIMA_ROOT = Path(__file__).resolve().parents[3]  # tools/mcd-key-automation/app -> vima
if str(_VIMA_ROOT) not in sys.path:
    sys.path.insert(0, str(_VIMA_ROOT))

from apis.catalog import (  # noqa: E402
    AUTH_OAUTH1,
    AUTH_OAUTH1_ENC,
    AUTH_OAUTH2,
    AUTH_JWT_RS256,
    CATALOG,
    LEGACY_TO_ID,
    ApiCatalogEntry,
    get,
    iter_ordered,
)


def entry_for_legacy(legacy_id: str) -> ApiCatalogEntry | None:
    """Look up a catalog entry by legacy id (e.g. 'binlookup', 'ofin')."""
    new_id = LEGACY_TO_ID.get(legacy_id, legacy_id)
    return CATALOG.get(new_id)


def env_prefix_for(legacy_id: str) -> str:
    """Return the new vima env-var prefix for a legacy api id."""
    e = entry_for_legacy(legacy_id)
    return e.env_prefix if e else legacy_id.upper()


def encryption_env_var(legacy_id: str) -> str | None:
    """Return the encryption-key env var for APIs that need one, else None."""
    e = entry_for_legacy(legacy_id)
    if e and e.auth == AUTH_OAUTH1_ENC:
        return f"{e.env_prefix}_ENCRYPTION_KEY_PATH"
    return None


__all__ = [
    "AUTH_OAUTH1",
    "AUTH_OAUTH1_ENC",
    "AUTH_OAUTH2",
    "AUTH_JWT_RS256",
    "CATALOG",
    "LEGACY_TO_ID",
    "ApiCatalogEntry",
    "get",
    "iter_ordered",
    "entry_for_legacy",
    "env_prefix_for",
    "encryption_env_var",
]
