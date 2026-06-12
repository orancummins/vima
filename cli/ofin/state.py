"""Persistent, per-region "active id" store for the CLI.

Stores small bits of flow state (active customer_id, consent_id, account_id,
EU end_user_id, etc.) so multi-step flows feel stateful between separate CLI
invocations — mirroring what the web app keeps in memory.

Default location: ``~/.ofin/state.json`` (override with ``--state-file`` or the
``OFIN_STATE_FILE`` env var). Writes are atomic.
"""
from __future__ import annotations

import json
import os
import tempfile
from typing import Any, Dict, Optional

_DEFAULT_KEYS_BY_REGION = ("us", "au", "eu")


def default_state_path() -> str:
    override = os.environ.get("OFIN_STATE_FILE")
    if override:
        return override
    home = os.path.expanduser("~")
    return os.path.join(home, ".ofin", "state.json")


class State:
    """A JSON-backed dict of ``{region: {key: value}}``."""

    def __init__(self, path: Optional[str] = None) -> None:
        self.path = path or default_state_path()
        self._data: Dict[str, Dict[str, Any]] = {r: {} for r in _DEFAULT_KEYS_BY_REGION}
        self._load()

    def _load(self) -> None:
        try:
            with open(self.path, "r", encoding="utf-8") as fh:
                loaded = json.load(fh)
            if isinstance(loaded, dict):
                for region, vals in loaded.items():
                    if isinstance(vals, dict):
                        self._data.setdefault(region, {}).update(vals)
        except (OSError, ValueError):
            pass  # No state yet or unreadable — start fresh.

    def save(self) -> None:
        directory = os.path.dirname(os.path.abspath(self.path))
        try:
            os.makedirs(directory, exist_ok=True)
            fd, tmp = tempfile.mkstemp(dir=directory, prefix=".ofin-state-", suffix=".tmp")
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                json.dump(self._data, fh, indent=2, sort_keys=True)
            os.replace(tmp, self.path)
        except OSError:
            pass  # Best-effort; never break a command because state can't persist.

    # -- accessors ----------------------------------------------------------
    def region(self, region: str) -> Dict[str, Any]:
        return self._data.setdefault(region, {})

    def get(self, region: str, key: str, default: Any = None) -> Any:
        return self.region(region).get(key, default)

    def set(self, region: str, key: str, value: Any) -> None:
        self.region(region)[key] = value

    def update(self, region: str, updates: Dict[str, Any]) -> None:
        if updates:
            self.region(region).update({k: v for k, v in updates.items() if v is not None})

    def clear(self, region: Optional[str] = None) -> None:
        if region:
            self._data[region] = {}
        else:
            self._data = {r: {} for r in _DEFAULT_KEYS_BY_REGION}

    def as_dict(self) -> Dict[str, Dict[str, Any]]:
        return {r: dict(v) for r, v in self._data.items() if v}
