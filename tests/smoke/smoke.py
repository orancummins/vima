"""tests/smoke/smoke.py — basic connectivity and home-screen render checks.

Validates that:
  - The home page (GET /app) returns 200 without a server error page
  - The HTML contains all three top-level navigation panels
  - The API manifest endpoint (GET /explorer/apis) returns valid JSON
  - The API list is non-empty and contains a known API id

Independently runnable::

    python tests/smoke/smoke.py --base-url http://localhost:9021
"""
from __future__ import annotations

import argparse
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tests.lib.utils import (
    TestRunner, Summary,
    get, assert_status, assert_json, assert_field, assert_no_server_error,
)


def run(base_url: str = "http://127.0.0.1:9021") -> TestRunner:
    runner = TestRunner("Smoke — Home / APIs / Use Cases")

    # ── GET /app ───────────────────────────────────────────────
    runner.run("GET /app returns 200", lambda: assert_status(get(f"{base_url}/app"), 200))

    def _home_no_error():
        resp = assert_status(get(f"{base_url}/app"), 200)
        assert_no_server_error(resp.text, f"{base_url}/app")

    runner.run("GET /app has no server error", _home_no_error)

    def _home_nav_panels():
        resp = assert_status(get(f"{base_url}/app"), 200)
        html = resp.text
        for marker in ("panel-home", "panel-apis", "panel-usecases"):
            assert marker in html, (
                f"Navigation panel marker {marker!r} not found in /app HTML. "
                f"The page may not have loaded correctly."
            )

    runner.run("GET /app contains all navigation panels", _home_nav_panels)

    # ── GET /explorer/apis ──────────────────────────────────────
    def _apis_200():
        assert_status(get(f"{base_url}/explorer/apis"), 200)

    runner.run("GET /explorer/apis returns 200", _apis_200)

    def _apis_json_list():
        resp = assert_status(get(f"{base_url}/explorer/apis"), 200)
        data = assert_json(resp)
        # Response may be a list or {"apis": [...]}
        items = data if isinstance(data, list) else data.get("apis", data)
        assert isinstance(items, list) and len(items) > 0, (
            f"/explorer/apis returned an empty or non-list response: {data}"
        )

    runner.run("GET /explorer/apis returns a non-empty list", _apis_json_list)

    def _apis_has_bin_lookup():
        resp = assert_status(get(f"{base_url}/explorer/apis"), 200)
        data = assert_json(resp)
        items = data if isinstance(data, list) else data.get("apis", data)
        ids = [a.get("id") for a in items]
        assert "bin_lookup" in ids, (
            f"'bin_lookup' not found in API list. Available ids: {ids}"
        )

    runner.run("GET /explorer/apis includes bin_lookup", _apis_has_bin_lookup)

    # ── Use Cases page marker (served from same /app SPA) ──────
    def _uc_panel():
        resp = assert_status(get(f"{base_url}/app"), 200)
        assert "panel-usecases" in resp.text, (
            "Use Cases panel marker not found in /app HTML."
        )

    runner.run("Use Cases panel marker present in /app", _uc_panel)

    return runner


# ── Standalone entry point ─────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vima smoke tests")
    parser.add_argument("--base-url", default="http://127.0.0.1:9021")
    args = parser.parse_args()

    runner = run(args.base_url)
    summary = Summary()
    summary.add(runner)
    runner.print_summary()
    summary.print_and_exit()
