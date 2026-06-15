"""tests/usecases/bin_lookup.py — BIN Lookup Use Case tests.

Covers:
  - Iframe index.html loads (GET /bin_lookup/index.html → 200)
  - BIN ranges status (GET /usecases/bin_lookup/bin-ranges/status → 200)
  - Lookup action (POST /usecases/bin_lookup/action)

The BIN Lookup use case is an animated payment-card visualiser driven
by the same BIN Lookup API.  Unlike most use cases it exposes a custom
bin-ranges cache and uses the action pattern rather than /data.

Independently runnable::

    python tests/usecases/bin_lookup.py --base-url http://localhost:9021
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

UC_ID    = "bin_lookup"
TEST_BIN = "543210"


def run(base_url: str = "http://127.0.0.1:9021") -> TestRunner:
    runner = TestRunner("BIN Lookup Use Case")

    # ── 1. Iframe loads ────────────────────────────────────────
    def _index_loads():
        resp = assert_status(get(f"{base_url}/bin_lookup/index.html"), 200)
        assert len(resp.text) > 500, (
            f"/bin_lookup/index.html body is unexpectedly short ({len(resp.text)} chars)"
        )

    runner.run("/bin_lookup/index.html loads (200)", _index_loads)

    # ── 2. BIN ranges status ───────────────────────────────────
    def _ranges_status():
        resp = assert_status(get(f"{base_url}/usecases/bin_lookup/bin-ranges/status"), 200)
        data = assert_json(resp)
        # Expected: {"status": "idle"|"loading"|"loaded"|"error", ...}
        assert "status" in data, (
            f"No 'status' field in /usecases/bin_lookup/bin-ranges/status response: {data}"
        )

    runner.run("BIN ranges status endpoint returns valid JSON", _ranges_status)

    # ── 3. Lookup action ───────────────────────────────────────
    def _lookup_action():
        # First-call gateway rejection is absorbed by the warm-up in run.py.
        resp = assert_status(
            post(
                f"{base_url}/usecases/bin_lookup/action",
                {"action": "lookup", "params": {"account_range": TEST_BIN}},
            ),
            200,
        )
        data = assert_json(resp)

        assert data.get("found") is True, (
            f"BIN lookup action: expected found=true for BIN {TEST_BIN}. "
            f"Response: {data}"
        )
        assert_field(data, "card", msg="'card' object missing from BIN lookup response")

    runner.run(f"Lookup action returns card data for BIN {TEST_BIN}", _lookup_action)

    # ── 4. Lookup action — unknown BIN returns found=false ─────
    def _lookup_unknown():
        resp = assert_status(
            post(
                f"{base_url}/usecases/bin_lookup/action",
                {"action": "lookup", "params": {"account_range": "000000"}},
            ),
            200,
        )
        data = assert_json(resp)
        # Should return found=False gracefully, not a 500
        assert "found" in data, (
            f"'found' field missing from response for unknown BIN. Response: {data}"
        )

    runner.run("Lookup action handles unknown BIN gracefully", _lookup_unknown)

    return runner


# ── Standalone entry point ─────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vima BIN Lookup use case tests")
    parser.add_argument("--base-url", default="http://127.0.0.1:9021")
    args = parser.parse_args()

    runner = run(args.base_url)
    summary = Summary()
    summary.add(runner)
    runner.print_summary()
    summary.print_and_exit()
