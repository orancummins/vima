"""Central API registry.

Each API module must expose:
  - MANIFEST: dict describing the API, its categories and operations
  - execute(op_id, params) -> dict response envelope
  - get_state() -> dict (optional, UI-safe state snapshot)
  - is_configured() -> bool (optional)
"""
from __future__ import annotations

import os
from typing import Any, Dict, List

from .ofin import api as ofin_api
from .binlookup import api as binlookup_api
from .clarity import api as clarity_api
from .priceless import api as priceless_api
from .easysavings import api as easysavings_api
from .places import api as places_api
from .txnotify import api as txnotify_api
from .consent import api as consent_api
from .ofpub import api as ofpub_api
from .ofmc import api as ofmc_api
from .eligibility import api as eligibility_api
from .bces import api as bces_api


REGISTRY = {
    "ofin": ofin_api,
    "binlookup": binlookup_api,
    "clarity": clarity_api,
    "priceless": priceless_api,
    "easysavings": easysavings_api,
    "places": places_api,
    "txnotify": txnotify_api,
    "consent": consent_api,
    "ofpub": ofpub_api,
    "ofmc": ofmc_api,
    "eligibility": eligibility_api,
    "bces": bces_api,
}

# Display order for the API sub-tabs.
ORDER: List[str] = ["ofin", "binlookup", "clarity", "priceless", "easysavings", "places", "ofpub", "ofmc", "consent", "txnotify", "eligibility", "bces"]


def manifests() -> List[Dict[str, Any]]:
    out = []
    for key in ORDER:
        mod = REGISTRY[key]
        m = dict(mod.MANIFEST)
        m["configured"] = bool(getattr(mod, "is_configured", lambda: True)())
        m["directory"] = os.path.dirname(os.path.abspath(mod.__file__))
        out.append(m)
    return out


def get_module(api_id: str):
    return REGISTRY.get(api_id)
