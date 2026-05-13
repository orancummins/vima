"""Central API registry.

Each API module must expose:
  - MANIFEST: dict describing the API, its categories and operations
  - execute(op_id, params) -> dict response envelope
  - get_state() -> dict (optional, UI-safe state snapshot)
  - is_configured() -> bool (optional)
"""
from __future__ import annotations

from typing import Any, Dict, List

from .ofin import api as ofin_api
from .binlookup import api as binlookup_api
from .clarity import api as clarity_api
from .priceless import api as priceless_api


REGISTRY = {
    "ofin": ofin_api,
    "binlookup": binlookup_api,
    "clarity": clarity_api,
    "priceless": priceless_api,
}

# Display order for the API sub-tabs.
ORDER: List[str] = ["ofin", "binlookup", "clarity", "priceless"]


def manifests() -> List[Dict[str, Any]]:
    out = []
    for key in ORDER:
        mod = REGISTRY[key]
        m = dict(mod.MANIFEST)
        m["configured"] = bool(getattr(mod, "is_configured", lambda: True)())
        out.append(m)
    return out


def get_module(api_id: str):
    return REGISTRY.get(api_id)
