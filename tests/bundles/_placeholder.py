"""tests/bundles/_placeholder.py — API Bundles test stub.

This module is a placeholder for bundle-owner tests.  The structure
mirrors tests/apis/_template.py so bundle owners can add specific
assertions alongside the boilerplate below.

To implement:
  - Test that GET /explorer/apis returns bundles metadata (if exposed)
  - Test bundle navigation in the UI (requires browser automation)
  - Test the SDK panel "Run this code" button (POST /sdk/run)
  - Add one file per bundle e.g. open_finance_bundle.py

Independently runnable (currently always passes as a placeholder)::

    python tests/bundles/_placeholder.py --base-url http://localhost:9021
"""
from __future__ import annotations

import argparse
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tests.lib.utils import TestRunner, Summary, get, assert_status, assert_json


def run(base_url: str = "http://127.0.0.1:9021") -> TestRunner:
    runner = TestRunner("Bundles")

    # ── Bundles catalog endpoint ───────────────────────────────
    # The bundles catalog is served alongside the API catalog.
    def _bundles_endpoint():
        resp = assert_status(get(f"{base_url}/explorer/apis"), 200)
        data = assert_json(resp)
        items = data if isinstance(data, list) else data.get("apis", data)
        assert isinstance(items, list), f"/explorer/apis did not return a list: {type(data)}"
        # Presence of any entry is sufficient at this stage

    runner.run("Bundles: /explorer/apis reachable (placeholder)", _bundles_endpoint)

    # TODO: add bundle-specific tests here, e.g.:
    #   - GET /explorer/apis → entry has 'bundle' field
    #   - POST /sdk/run → 200, launcher reported
    #   - Specific bundle manifest entries present

    return runner


# ── Standalone entry point ─────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vima Bundles tests")
    parser.add_argument("--base-url", default="http://127.0.0.1:9021")
    args = parser.parse_args()

    runner = run(args.base_url)
    summary = Summary()
    summary.add(runner)
    runner.print_summary()
    summary.print_and_exit()
