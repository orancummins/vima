"""Use cases registry."""
from __future__ import annotations

import importlib
from typing import Any, Dict, List, Optional


# Each use case is a module under `usecases/` exposing at least a MANIFEST dict.
USE_CASE_MODULES = ["pfm", "enrichment", "recurring", "psi", "binlookup", "clarity", "easysavings", "places", "identity", "specials", "findacard", "sonic"]


_modules: Dict[str, Any] = {}


def _load():
    if _modules:
        return
    for mod_name in USE_CASE_MODULES:
        try:
            m = importlib.import_module(f"usecases.{mod_name}")
            uc_id = m.MANIFEST["id"]
            _modules[uc_id] = m
        except Exception as e:  # pragma: no cover
            print(f"[usecases] failed to load {mod_name}: {e}")


def manifests() -> List[Dict[str, Any]]:
    _load()
    return [m.MANIFEST for m in _modules.values()]


def get_module(uc_id: str) -> Optional[Any]:
    _load()
    return _modules.get(uc_id)
