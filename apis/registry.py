"""Central API registry — dynamic discovery via ``apis.catalog``.

Each API module under ``apis/<id>/api.py`` must expose:

  * ``MANIFEST``           — dict describing the API and its operations
  * ``execute(op_id, params)`` -> response envelope
  * ``get_state()``        — optional, UI-safe state snapshot
  * ``is_configured()``    — optional, defaults to ``credentials.is_configured``

The list of APIs (and their ids, env prefixes, display names) lives in
``apis/catalog.py``.  Adding a new Mastercard API is now:

    1. Add an entry to ``apis/catalog.py``.
    2. Create ``apis/<new_id>/api.py`` with ``MANIFEST`` + ``execute``.

No edits required here.
"""
from __future__ import annotations

import os
from typing import Any, Dict, List

from apis.catalog import CATALOG, iter_ordered, get as catalog_get
from apis.credentials import is_configured as default_is_configured


# Map: api_id -> module. Built lazily on first access.
REGISTRY: Dict[str, Any] = {}

# Display order, matching the catalog declaration order.
ORDER: List[str] = [e.id for e in iter_ordered()]


def _load_all() -> None:
    if REGISTRY:
        return
    for entry in iter_ordered():
        try:
            REGISTRY[entry.id] = entry.load_module()
        except Exception as exc:  # pragma: no cover — surface but don't crash startup
            print(f"[apis] failed to load {entry.id}: {exc}")


def manifests() -> List[Dict[str, Any]]:
    """Return the manifest for every registered API, in display order."""
    _load_all()
    out: List[Dict[str, Any]] = []
    for api_id in ORDER:
        mod = REGISTRY.get(api_id)
        if mod is None:
            continue
        entry = CATALOG[api_id]
        m = dict(getattr(mod, "MANIFEST", {}))
        # Catalog wins for identity fields.
        m["id"] = entry.id
        m["name"] = entry.display_name
        m.setdefault("docs_url", entry.docs_url)
        m["env_prefix"] = entry.env_prefix
        m["portal_slug"] = entry.portal_slug
        configured_fn = getattr(mod, "is_configured", None)
        if callable(configured_fn):
            m["configured"] = bool(configured_fn())
        else:
            m["configured"] = bool(default_is_configured(entry))
        m["directory"] = os.path.dirname(os.path.abspath(mod.__file__))
        out.append(m)
    return out


def get_module(api_id: str):
    """Look up a module by canonical id or legacy id."""
    _load_all()
    if api_id in REGISTRY:
        return REGISTRY[api_id]
    entry = catalog_get(api_id)
    if entry is None:
        return None
    return REGISTRY.get(entry.id)


__all__ = ["REGISTRY", "ORDER", "manifests", "get_module"]
