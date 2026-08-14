"""tests/usecases/_template.py — copy-paste starting point for Use Case test authors.

To add tests for a new use case:
  1. Copy this file to tests/usecases/<uc_id>.py
  2. Replace every occurrence of "template" / "TEMPLATE" with your uc_id
  3. Fill in the use-case-specific assertions (marked with TODO)
  4. Register the module in tests/run.py

Independently runnable::

    python tests/usecases/<uc_id>.py --base-url http://localhost:9021
"""
from __future__ import annotations

import argparse
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tests.lib.utils import (
    TestRunner, Summary,
    get, post, assert_status, assert_json, assert_field,
)

# ── Replace with your use case id ─────────────────────────────────────────────
UC_ID       = "template"        # e.g. "easy_savings"
# HTML page served by the use-case static route (/<uc_id>/index.html)
INDEX_HTML  = f"/{UC_ID}/index.html"


def run(base_url: str = "http://127.0.0.1:9021") -> TestRunner:
    runner = TestRunner(f"{UC_ID.replace('_', ' ').title()} Use Case")

    # ── 1. Iframe / index.html loads ───────────────────────────
    def _index_loads():
        resp = assert_status(get(f"{base_url}{INDEX_HTML}"), 200)
        assert len(resp.text) > 100, (
            f"{INDEX_HTML} returned an unexpectedly short body ({len(resp.text)} chars)"
        )

    runner.run(f"{INDEX_HTML} loads (200)", _index_loads)

    # ── 2. Action endpoint ─────────────────────────────────────
    # TODO: replace action name and params with those specific to this use case
    def _action():
        resp = assert_status(
            post(
                f"{base_url}/usecases/{UC_ID}/action",
                {"action": "TODO_action_name", "params": {}},
            ),
            200,
        )
        data = assert_json(resp)
        assert "error" not in data or not data["error"], (
            f"Use case action returned an error: {data.get('error')}"
        )
        # TODO: assert specific fields in the response

    runner.run("Action endpoint returns 200 without error", _action)

    return runner


# ── Standalone entry point ─────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"Vima {UC_ID} use case tests")
    parser.add_argument("--base-url", default="http://127.0.0.1:9021")
    args = parser.parse_args()

    runner = run(args.base_url)
    summary = Summary()
    summary.add(runner)
    runner.print_summary()
    summary.print_and_exit()
