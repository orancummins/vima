"""tests/apis/_template.py — copy-paste starting point for API test authors.

To add tests for a new API:
  1. Copy this file to tests/apis/<api_id>.py
  2. Replace every occurrence of "template" / "TEMPLATE" with your api_id
  3. Fill in the API-specific assertions (marked with TODO)
  4. Register the module in tests/run.py

Independently runnable::

    python tests/apis/<api_id>.py --base-url http://localhost:9021
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

# ── Replace with your API id ───────────────────────────────────────────────────
API_ID       = "template"       # e.g. "merchant_identifier"
OPERATION_ID = "template_op"    # e.g. "identify_merchant"
TEST_PARAMS  = {}               # e.g. {"merchant_name": "McDonalds"}


def run(base_url: str = "http://127.0.0.1:9021") -> TestRunner:
    runner = TestRunner(f"{API_ID.replace('_', ' ').title()} API")

    # ── 1. Configured check ────────────────────────────────────
    def _configured():
        resp   = assert_status(get(f"{base_url}/explorer/apis"), 200)
        data   = assert_json(resp)
        items  = data if isinstance(data, list) else data.get("apis", data)
        entry  = next((a for a in items if a.get("id") == API_ID), None)
        assert entry is not None, f"API '{API_ID}' not found in /explorer/apis"
        assert entry.get("configured"), (
            f"API '{API_ID}' is not configured. "
            f"Provision or set credentials in config/.env first."
        )

    runner.run(f"{API_ID} is configured", _configured)

    # ── 2. Execute operation ───────────────────────────────────
    def _execute():
        resp = assert_status(
            post(f"{base_url}/explorer/{API_ID}/execute",
                 {"operation": OPERATION_ID, "params": TEST_PARAMS}),
            200,
        )
        data = assert_json(resp)
        assert data.get("success"), (
            f"execute {OPERATION_ID} did not return success=true. "
            f"Response: {data}"
        )
        # TODO: add field assertions specific to this API, e.g.:
        # assert_field(data, "response", "body")

    runner.run(f"Execute {OPERATION_ID}", _execute)

    # ── 3. Snippet ("Get Code") ────────────────────────────────
    def _snippet():
        resp = assert_status(
            get(f"{base_url}/explorer/{API_ID}/snippet?op={OPERATION_ID}"),
            200,
        )
        data = assert_json(resp)
        snippet_text = assert_field(data, "snippet")
        # Python snippets always contain an import statement
        assert "import" in snippet_text, (
            f"Snippet for {OPERATION_ID} does not look like Python code. "
            f"Got: {snippet_text[:200]}"
        )

    runner.run(f"Get Code snippet for {OPERATION_ID}", _snippet)

    return runner


# ── Standalone entry point ─────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"Vima {API_ID} API tests")
    parser.add_argument("--base-url", default="http://127.0.0.1:9021")
    args = parser.parse_args()

    runner = run(args.base_url)
    summary = Summary()
    summary.add(runner)
    runner.print_summary()
    summary.print_and_exit()
