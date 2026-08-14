"""Output helpers: JSON / raw / human rendering, color, and browser launch."""
from __future__ import annotations

import json
import os
import sys
import webbrowser
from typing import Any

from .sdk.base import Result


def _color_enabled(no_color: bool) -> bool:
    if no_color or os.environ.get("NO_COLOR"):
        return False
    return sys.stdout.isatty()


class Printer:
    """Renders SDK results and messages according to global output flags."""

    def __init__(self, as_json: bool = False, raw: bool = False, no_color: bool = False) -> None:
        self.as_json = as_json
        self.raw = raw
        self.color = _color_enabled(no_color)

    # -- ansi helpers -------------------------------------------------------
    def _c(self, text: str, code: str) -> str:
        if not self.color:
            return text
        return f"\033[{code}m{text}\033[0m"

    def green(self, t: str) -> str:
        return self._c(t, "32")

    def red(self, t: str) -> str:
        return self._c(t, "31")

    def yellow(self, t: str) -> str:
        return self._c(t, "33")

    def dim(self, t: str) -> str:
        return self._c(t, "2")

    def bold(self, t: str) -> str:
        return self._c(t, "1")

    # -- messages -----------------------------------------------------------
    def info(self, msg: str) -> None:
        print(msg)

    def error(self, msg: str) -> None:
        print(self.red("error: ") + msg, file=sys.stderr)

    def warn(self, msg: str) -> None:
        print(self.yellow("warning: ") + msg, file=sys.stderr)

    # -- structured payloads ------------------------------------------------
    def data(self, obj: Any) -> None:
        """Print an arbitrary structured object (config/state listings)."""
        print(json.dumps(obj, indent=2, sort_keys=True, default=str))

    def result(self, res: Result) -> None:
        """Render an SDK :class:`Result`."""
        if self.raw:
            self._print_body(res.body)
            return
        if self.as_json:
            print(json.dumps(res.to_dict(), indent=2, default=str))
            return

        # Human-readable.
        status_txt = f"{res.status}"
        head = (self.green("● " + status_txt) if res.ok else self.red("✕ " + status_txt))
        print(f"{head}  {self.dim('HTTP status')}")
        if res.hints.get("open_link"):
            label = res.hints.get("open_link_label", "Open link")
            print(self.yellow(f"↗ {label}: ") + res.hints["open_link"])
        if res.state_updates:
            kv = ", ".join(f"{k}={v}" for k, v in res.state_updates.items())
            print(self.dim(f"saved: {kv}"))
        self._print_body(res.body)

    def _print_body(self, body: Any) -> None:
        if body is None:
            return
        if isinstance(body, (dict, list)):
            print(json.dumps(body, indent=2, default=str))
        else:
            print(str(body))


def open_in_browser(url: str) -> bool:
    """Open ``url`` in the default browser. Returns True on success."""
    try:
        return webbrowser.open(url)
    except Exception:  # noqa: BLE001
        return False
