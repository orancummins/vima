"""tests/sdks/_placeholder.py — SDK / ofin CLI test stub.

This module is a placeholder for SDK-owner tests.

To implement:
  - POST /sdk/run  → 200, launcher reported for current OS
  - ofin CLI direct invocation: subprocess ofin.bat/ofin.sh
  - Three-region OfinClient smoke test (requires credentials)
  - GET /explorer/<api_id>/snippet?op=<op_id> returns runnable Python

Independently runnable (currently always passes as a placeholder)::

    python tests/sdks/_placeholder.py --base-url http://localhost:9021
"""
from __future__ import annotations

import argparse
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tests.lib.utils import TestRunner, Summary, get, assert_status


def run(base_url: str = "http://127.0.0.1:9021") -> TestRunner:
    runner = TestRunner("SDKs / ofin CLI")

    # ── App serves without error ───────────────────────────────
    def _app_up():
        assert_status(get(f"{base_url}/app"), 200)

    runner.run("SDKs: /app reachable (placeholder)", _app_up)

    # TODO: add SDK-specific tests here, e.g.:
    #   - POST /sdk/run with {"region":"us","command":"auth-token"} → {"ok":true}
    #   - subprocess([ofin.bat/ofin.sh, "us", "auth-token"]) exits 0
    #   - ofin CLI snippet endpoint returns multi-region code

    return runner


# ── Standalone entry point ─────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vima SDK tests")
    parser.add_argument("--base-url", default="http://127.0.0.1:9021")
    args = parser.parse_args()

    runner = run(args.base_url)
    summary = Summary()
    summary.add(runner)
    runner.print_summary()
    summary.print_and_exit()
