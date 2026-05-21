"""Use cases registry."""
from __future__ import annotations

import importlib
import os
from typing import Any, Dict, List, Optional


# Each use case is a module under `usecases/` exposing at least a MANIFEST dict.
USE_CASE_MODULES = ["pfm", "enrichment", "recurring", "psi", "binlookup", "clarity", "easysavings", "places", "identity", "specials", "findacard", "sonic", "testchat"]


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
    result = []
    for m in _modules.values():
        entry = dict(m.MANIFEST)
        entry["directory"] = os.path.dirname(os.path.abspath(m.__file__))
        result.append(entry)
    return result


def get_module(uc_id: str) -> Optional[Any]:
    _load()
    return _modules.get(uc_id)
