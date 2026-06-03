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

from apis.catalog import CATALOG, DISABLED_API_IDS, GROUP_ORDER, iter_ordered, get as catalog_get
from apis.bundles import iter_bundles, bundles_for_api
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
    """Return the manifest for every registered API, in display order.

    APIs listed in ``catalog.DISABLED_API_IDS`` are silently omitted so the
    UI sidebar and the /explorer/apis endpoint don't surface them. The
    underlying modules are still loaded and importable for tests/tools.
    """
    _load_all()
    out: List[Dict[str, Any]] = []
    for api_id in ORDER:
        if api_id in DISABLED_API_IDS:
            continue
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
        m["legacy_id"] = entry.legacy_id  # may be None for newer APIs
        m["group"] = entry.group
        m["complements"] = list(entry.complements)
        m["requires"] = list(entry.requires)
        m["bundles"] = [b.id for b in bundles_for_api(entry.id)]
        configured_fn = getattr(mod, "is_configured", None)
        if callable(configured_fn):
            m["configured"] = bool(configured_fn())
        else:
            m["configured"] = bool(default_is_configured(entry))
        m["directory"] = os.path.dirname(os.path.abspath(mod.__file__))
        out.append(m)
    return out


def manifests_grouped() -> List[Dict[str, Any]]:
    """Return manifests bucketed by ``ApiCatalogEntry.group``.

    Output: ``[{"group": "...", "apis": [manifest, ...]}, ...]`` ordered by
    ``GROUP_ORDER`` (Mastercard Developers product categories). Within each
    group the order matches the catalog declaration order.
    """
    by_group: Dict[str, List[Dict[str, Any]]] = {g: [] for g in GROUP_ORDER}
    for m in manifests():
        g = m.get("group") or GROUP_ORDER[-1]
        by_group.setdefault(g, []).append(m)
    sections: List[Dict[str, Any]] = []
    for g in GROUP_ORDER:
        items = by_group.get(g) or []
        if items:
            sections.append({"group": g, "apis": items})
    # Any groups not in GROUP_ORDER (shouldn't normally happen)
    for g, items in by_group.items():
        if g not in GROUP_ORDER and items:
            sections.append({"group": g, "apis": items})
    return sections


def get_module(api_id: str):
    """Look up a module by canonical id or legacy id."""
    _load_all()
    if api_id in REGISTRY:
        return REGISTRY[api_id]
    entry = catalog_get(api_id)
    if entry is None:
        return None
def solutions() -> List[Dict[str, Any]]:
    """Return solution-shaped bundles enriched with per-bundle status.

    Each bundle yields:

        {
          "id":         "pfm_stack",
          "name":       "Account intelligence & PFM",
          "tagline":    "...",
          "anchor":     "open_finance",
          "apis":       [ {id, name, configured, group, disabled}, ... ],
          "configured": 3,   # how many APIs in the bundle are configured
          "total":      8,   # total APIs in the bundle (excl. disabled)
        }

    Disabled APIs (catalog ``DISABLED_API_IDS``) are filtered out of the
    ``apis`` array so the UI doesn't surface things the user cannot
    onboard.  The chat agent uses this same shape so it can recommend
    coherent solution stacks rather than individual APIs.
    """
    manifest_by_id = {m["id"]: m for m in manifests()}
    out: List[Dict[str, Any]] = []
    for b in iter_bundles():
        apis_out: List[Dict[str, Any]] = []
        configured = 0
        for api_id in b.apis:
            m = manifest_by_id.get(api_id)
            if m is None:
                # Either unknown or disabled — skip so the bundle stays clean.
                continue
            apis_out.append({
                "id": m["id"],
                "name": m["name"],
                "group": m.get("group"),
                "configured": bool(m.get("configured")),
            })
            if m.get("configured"):
                configured += 1
        out.append({
            "id": b.id,
            "name": b.name,
            "tagline": b.tagline,
            "description": b.description,
            "accent": b.accent,
            "icon_path": b.icon_path,
            "value_props": list(b.value_props),
            "journey": [
                {"api_id": step[0], "title": step[1], "detail": step[2]}
                for step in b.journey
            ],
            "walkthroughs": [
                {"title": w[0], "body": w[1]} for w in b.walkthroughs
            ],
            "examples": list(b.examples),
            "anchor": b.anchor,
            "apis": apis_out,
            "configured": configured,
            "total": len(apis_out),
        })
    return out


__all__ = ["REGISTRY", "ORDER", "manifests", "manifests_grouped", "get_module", "solutions"]
