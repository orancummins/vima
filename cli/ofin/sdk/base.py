"""Shared SDK primitives: the :class:`Result` envelope and helpers."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Result:
    """Normalised result of an Open Finance API call.

    The underlying clients return ``(body, status_code)`` tuples and expose
    ``last_request`` / ``last_response`` properties. :class:`Result` packages
    all of that into one object the CLI can render in ``--json`` or
    human-readable form.
    """

    status: int
    body: Any
    request: dict[str, Any] | None = None
    response: dict[str, Any] | None = None
    #: Local state mutations produced by this call (e.g. captured customer_id).
    state_updates: dict[str, Any] = field(default_factory=dict)
    #: Side-channel hints, e.g. a Connect/flow URL to open in a browser.
    hints: dict[str, Any] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return 200 <= int(self.status) < 300

    @property
    def token(self) -> str | None:
        """The access token from an auth call, regardless of region.

        US/AU return it as ``token``; EU as ``access_token``.
        """
        if isinstance(self.body, dict):
            return self.body.get("token") or self.body.get("access_token")
        return None

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "status": self.status,
            "body": self.body,
            "state_updates": self.state_updates,
            "hints": self.hints,
            "request": self.request,
            "response": self.response,
        }


def first(d: Any, *keys: str) -> Any | None:
    """Return the first present, truthy value among ``keys`` in mapping ``d``."""
    if not isinstance(d, dict):
        return None
    for k in keys:
        v = d.get(k)
        if v:
            return v
    return None
