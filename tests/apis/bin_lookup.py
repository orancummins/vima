"""tests/apis/bin_lookup.py — BIN Lookup API tests.

Covers:
  - Configured check (credentials present)
  - Execute: POST /explorer/bin_lookup/execute with op=lookup_bin
  - Snippet ("Get Code"): GET /explorer/bin_lookup/snippet?op=lookup_bin

Independently runnable::

    python tests/apis/bin_lookup.py --base-url http://localhost:9021
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

API_ID       = "bin_lookup"
OPERATION_ID = "lookup_bin"
# Use the default sandbox BIN from the manifest
TEST_BIN     = "543210"


def run(base_url: str = "http://127.0.0.1:9021") -> TestRunner:
    runner = TestRunner("BIN Lookup API")

    # ── 1. Configured check ────────────────────────────────────
    def _configured():
        resp  = assert_status(get(f"{base_url}/explorer/apis"), 200)
        data  = assert_json(resp)
        items = data if isinstance(data, list) else data.get("apis", data)
        entry = next((a for a in items if a.get("id") == API_ID), None)
        assert entry is not None, f"'{API_ID}' not found in /explorer/apis"
        assert entry.get("configured"), (
            f"'{API_ID}' is not configured — "
            f"provision or set BIN_LOOKUP_CONSUMER_KEY / BIN_LOOKUP_SIGNING_KEY_PATH in config/.env"
        )

    runner.run("BIN Lookup is configured", _configured)

    # ── 2. Execute lookup_bin ──────────────────────────────────
    def _execute():
        import time as _time
        payload = {"operation": OPERATION_ID, "params": {"account_range": TEST_BIN}}
        url = f"{base_url}/explorer/{API_ID}/execute"

        # Freshly provisioned keys can be rejected by the Mastercard gateway on
        # the first call (sandbox propagation delay is usually 5–30 s).  Retry
        # up to 3 times with increasing backoff, skipping failures that look
        # like gateway auth errors rather than misconfiguration.
        _GATEWAY_ERRORS = ("Unauthorized", "Access Not Granted", "DECLINED")
        data = {}
        for attempt in range(3):
            resp = assert_status(post(url, payload), 200)
            data = assert_json(resp)
            if data.get("success"):
                break
            err = str(data.get("error", ""))
            # Only retry gateway / propagation errors, not missing-key errors
            if not any(e in err for e in _GATEWAY_ERRORS):
                break
            if attempt < 2:
                _time.sleep(10 * (attempt + 1))  # 10 s, 20 s

        assert data.get("success"), (
            f"execute {OPERATION_ID} returned success=false after retries. Response: {data}"
        )
        # Response envelope has a nested response.body from the Mastercard API
        assert_field(data, "response", msg="'response' key missing from execute result")

    runner.run(f"Execute {OPERATION_ID} (BIN {TEST_BIN})", _execute)

    # ── 3. Snippet — "Get Code" ────────────────────────────────
    def _snippet():
        resp = assert_status(
            get(f"{base_url}/explorer/{API_ID}/snippet?op={OPERATION_ID}"),
            200,
        )
        data = assert_json(resp)
        snippet_text = assert_field(data, "snippet", msg="No 'snippet' field in response")
        # Python OAuth1 snippets must import requests and contain the BIN param
        assert "import" in snippet_text, (
            f"Snippet does not look like Python code. Got: {snippet_text[:200]}"
        )
        assert "requests" in snippet_text, (
            f"Snippet does not reference the 'requests' library. Got: {snippet_text[:200]}"
        )

    runner.run("Get Code snippet contains valid Python", _snippet)

    return runner


# ── Standalone entry point ─────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vima BIN Lookup API tests")
    parser.add_argument("--base-url", default="http://127.0.0.1:9021")
    args = parser.parse_args()

    runner = run(args.base_url)
    summary = Summary()
    summary.add(runner)
    runner.print_summary()
    summary.print_and_exit()
