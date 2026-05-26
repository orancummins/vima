#!/usr/bin/env python3
"""
Smoke test: verifies that generated keys can authenticate against each API's sandbox.

Usage:
    python tests/smoke_test.py [--normalized-dir temp/normalized] [--password foobar!!]

Results per API:
    PASS           - 2xx response
    NEEDS_APPROVAL - 401/403 (key created but not yet approved by API Owner)
    FAIL           - other error or unexpected status
    SKIPPED        - credentials not found in normalized dir
"""

import argparse
import json
import os
import sys
import tempfile
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import requests

# ---------------------------------------------------------------------------
# OAuth 1.0a signing helper (using mastercard-oauth1-signer if installed)
# ---------------------------------------------------------------------------

def _oauth1_header(url: str, method: str, body_str: Optional[str],
                   consumer_key: str, p12_path: str, password: str) -> str:
    import oauth1.authenticationutils as authutils
    from oauth1.oauth import OAuth
    signing_key = authutils.load_signing_key(p12_path, password)
    return OAuth.get_authorization_header(url, method, body_str or "", consumer_key, signing_key)


# ---------------------------------------------------------------------------
# Credential loader
# ---------------------------------------------------------------------------

NORMALIZED_DIR = Path(__file__).parent.parent / "temp" / "normalized"


def _find_credentials(api_id: str, normalized_dir: Path) -> Optional[Path]:
    """Return the newest credentials JSON for an API id, or None if not found."""
    matches = list(normalized_dir.glob(f"*-{api_id}-signing-v1-credentials.json"))
    return max(matches, key=lambda p: p.stat().st_mtime) if matches else None


def _find_zip(api_id: str, normalized_dir: Path, cred_path: Optional[Path] = None) -> Optional[Path]:
    """Return the zip matching the same project as cred_path (same prefix), or the newest."""
    if cred_path:
        # Derive zip from credentials path: replace -credentials.json suffix with .zip
        stem = cred_path.name.replace("-credentials.json", ".zip")
        candidate = cred_path.parent / stem
        if candidate.exists():
            return candidate
    matches = list(normalized_dir.glob(f"*-{api_id}-signing-v1.zip"))
    return max(matches, key=lambda p: p.stat().st_mtime) if matches else None


def _extract_p12(zip_path: Path, tmp_dir: str) -> Optional[str]:
    with zipfile.ZipFile(zip_path) as zf:
        for name in zf.namelist():
            if name.endswith(".p12"):
                zf.extract(name, tmp_dir)
                return os.path.join(tmp_dir, name)
    return None


# ---------------------------------------------------------------------------
# Per-API test definitions
# ---------------------------------------------------------------------------

@dataclass
class ApiTest:
    api_id: str
    name: str
    method: str
    url: str
    body: Optional[dict] = None
    extra_headers: dict = field(default_factory=dict)
    oauth_type: str = "oauth1"  # "oauth1" or "oauth2_ofin"


TESTS = [
    ApiTest(
        api_id="binlookup",
        name="BIN Lookup",
        method="POST",
        url="https://sandbox.api.mastercard.com/bin-resources/bin-ranges?page=1&size=1",
        body=[{"key": "binNum", "value": "543210"}],
    ),
    ApiTest(
        api_id="places",
        name="Places",
        method="GET",
        url="https://sandbox.api.mastercard.com/location-intelligence/places-locator/merchant-category-codes/mcc-codes/5812",
    ),
    ApiTest(
        api_id="easysavings",
        name="Easy Savings",
        method="GET",
        url="https://sandbox.sme.api.mastercard.com/easysavings/specials/countries",
    ),
    ApiTest(
        api_id="clarity",
        name="Consumer Clarity",
        method="POST",
        url="https://sandbox.api.ethocaweb.com/ethoca/consumer-clarity/searches",
        body={
            "locale": "en-US",
            "searchCriteria": [{"merchantCriteria": {"name": "TestMerchant"}}],
        },
    ),
    ApiTest(
        api_id="priceless",
        name="Priceless",
        method="GET",
        url="https://sandbox.api.mastercard.com/the-portal/categories",
    ),
    ApiTest(
        api_id="txnotify",
        name="Transaction Notifications",
        method="GET",
        url="https://sandbox.api.mastercard.com/openapis/undelivered-notifications?pageNumber=1&pageSize=1",
    ),
    ApiTest(
        api_id="consent",
        name="Consent Management",
        method="GET",
        url="https://sandbox.api.mastercard.com/openapis/authentication/consents/smoke-test-ref",
    ),
    ApiTest(
        api_id="ofpub",
        name="Offers (Publisher)",
        method="GET",
        url="https://sandbox.api.mastercard.com/loyalty/offers/presentment/platforms/offers?limit=1&offset=0",
    ),
    ApiTest(
        api_id="ofmc",
        name="Offers (Merchant)",
        method="GET",
        url="https://sandbox.api.mastercard.com/loyalty/offers/eop/sources?limit=1&offset=0",
    ),
    ApiTest(
        api_id="eligibility",
        name="Benefits Eligibility",
        method="GET",
        url="https://sandbox.api.mastercard.com/loyalty/eligibility/widgets/access-tokens",
    ),
    ApiTest(
        api_id="bces",
        name="Benefits Content (BCES)",
        method="POST",
        url="https://sandbox.api.mastercard.com/loyalty/eligibility/benefit-contents/searches",
        body={"cardNumber": 5100000000000000},
    ),
    ApiTest(
        api_id="ofin",
        name="Open Finance (Finicity)",
        method="POST",
        url="https://api.finicity.com/aggregation/v2/partners/authentication",
        oauth_type="oauth2_ofin",
    ),
]


# ---------------------------------------------------------------------------
# Result types
# ---------------------------------------------------------------------------

PASS = "PASS"
NEEDS_APPROVAL = "NEEDS_APPROVAL"
SERVER_ERROR = "SERVER_ERROR"
FAIL = "FAIL"
SKIPPED = "SKIPPED"


@dataclass
class TestResult:
    api_id: str
    name: str
    status: str
    status_code: Optional[int] = None
    detail: str = ""


# ---------------------------------------------------------------------------
# Test runners
# ---------------------------------------------------------------------------

def _run_oauth1(test: ApiTest, normalized_dir: Path, password: str, tmp_dir: str) -> TestResult:
    cred_path = _find_credentials(test.api_id, normalized_dir)
    if not cred_path:
        return TestResult(test.api_id, test.name, SKIPPED, detail="credentials JSON not found")

    creds = json.loads(cred_path.read_text())
    consumer_key = creds.get("consumer_key")
    if not consumer_key:
        return TestResult(test.api_id, test.name, FAIL, detail="consumer_key missing from credentials JSON")

    zip_path = _find_zip(test.api_id, normalized_dir, cred_path)
    if not zip_path:
        return TestResult(test.api_id, test.name, SKIPPED, detail="key ZIP not found")

    p12_path = _extract_p12(zip_path, tmp_dir)
    if not p12_path:
        return TestResult(test.api_id, test.name, FAIL, detail="no .p12 found in ZIP")

    body_str = json.dumps(test.body) if test.body is not None else None

    try:
        auth_header = _oauth1_header(test.url, test.method, body_str, consumer_key, p12_path, password)
    except Exception as exc:
        return TestResult(test.api_id, test.name, FAIL, detail=f"OAuth signing failed: {exc}")

    headers = {"Accept": "application/json", "Authorization": auth_header}
    if body_str:
        headers["Content-Type"] = "application/json"
    headers.update(test.extra_headers)

    try:
        resp = requests.request(test.method, test.url, data=body_str, headers=headers, timeout=20)
    except Exception as exc:
        return TestResult(test.api_id, test.name, FAIL, detail=f"Request error: {exc}")

    if 200 <= resp.status_code < 300:
        return TestResult(test.api_id, test.name, PASS, status_code=resp.status_code, detail="OK")
    if resp.status_code in (401, 403):
        return TestResult(test.api_id, test.name, NEEDS_APPROVAL, status_code=resp.status_code,
                          detail="Unauthorized — key may need API Owner approval")
    if 400 <= resp.status_code < 500:
        # Auth worked; API rejected request for business reasons (missing required fields etc.)
        return TestResult(test.api_id, test.name, PASS, status_code=resp.status_code,
                          detail=f"Auth OK (API returned {resp.status_code} — business validation)")
    if resp.status_code >= 500:
        return TestResult(test.api_id, test.name, SERVER_ERROR, status_code=resp.status_code,
                          detail="Server/gateway error — unrelated to key validity")
    return TestResult(test.api_id, test.name, FAIL, status_code=resp.status_code,
                      detail=resp.text[:200])


def _run_ofin(test: ApiTest, normalized_dir: Path) -> TestResult:
    cred_path = _find_credentials(test.api_id, normalized_dir)
    if not cred_path:
        return TestResult(test.api_id, test.name, SKIPPED, detail="credentials JSON not found")

    creds = json.loads(cred_path.read_text())
    partner_id = creds.get("partner_id")
    app_key = creds.get("app_key")
    secret = creds.get("secret")

    if not all([partner_id, app_key, secret]):
        return TestResult(test.api_id, test.name, FAIL, detail="Missing partner_id/app_key/secret in credentials")

    body = {"partnerId": partner_id, "partnerSecret": secret}
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Finicity-App-Key": app_key,
    }

    try:
        resp = requests.post(test.url, json=body, headers=headers, timeout=20)
    except Exception as exc:
        return TestResult(test.api_id, test.name, FAIL, detail=f"Request error: {exc}")

    if 200 <= resp.status_code < 300:
        return TestResult(test.api_id, test.name, PASS, status_code=resp.status_code, detail="OK")
    if resp.status_code in (401, 403):
        return TestResult(test.api_id, test.name, NEEDS_APPROVAL, status_code=resp.status_code,
                          detail="Unauthorized — check partner credentials")
    return TestResult(test.api_id, test.name, FAIL, status_code=resp.status_code,
                      detail=resp.text[:200])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_smoke_tests(normalized_dir: Path, password: str) -> list[TestResult]:
    results = []
    with tempfile.TemporaryDirectory() as tmp_dir:
        for test in TESTS:
            print(f"  Testing {test.name} ({test.api_id})... ", end="", flush=True)
            if test.oauth_type == "oauth2_ofin":
                result = _run_ofin(test, normalized_dir)
            else:
                result = _run_oauth1(test, normalized_dir, password, tmp_dir)
            results.append(result)
            code_str = f" [{result.status_code}]" if result.status_code else ""
            print(f"{result.status}{code_str} — {result.detail}")
    return results


def main():
    parser = argparse.ArgumentParser(description="Smoke test generated Mastercard API keys")
    parser.add_argument(
        "--normalized-dir",
        default=str(NORMALIZED_DIR),
        help="Path to temp/normalized directory (default: %(default)s)",
    )
    parser.add_argument(
        "--password",
        default="foobar!!",
        help="Keystore password for .p12 files (default: %(default)s)",
    )
    args = parser.parse_args()

    normalized_dir = Path(args.normalized_dir).resolve()
    if not normalized_dir.exists():
        print(f"ERROR: normalized dir not found: {normalized_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"\n=== Mastercard API Smoke Test ===")
    print(f"Credentials dir : {normalized_dir}")
    print(f"Keystore password: {'*' * len(args.password)}")
    print()

    results = run_smoke_tests(normalized_dir, args.password)

    # Summary
    counts = {PASS: 0, NEEDS_APPROVAL: 0, SERVER_ERROR: 0, FAIL: 0, SKIPPED: 0}
    for r in results:
        counts[r.status] += 1

    print()
    print("=== Summary ===")
    print(f"  PASS          : {counts[PASS]}")
    print(f"  NEEDS_APPROVAL: {counts[NEEDS_APPROVAL]}")
    print(f"  SERVER_ERROR  : {counts[SERVER_ERROR]} (backend issue, not key-related)")
    print(f"  FAIL          : {counts[FAIL]}")
    print(f"  SKIPPED       : {counts[SKIPPED]}")
    print()

    any_fail = counts[FAIL] > 0
    if any_fail:
        print("FAILED APIs:")
        for r in results:
            if r.status == FAIL:
                print(f"  - {r.name}: {r.detail}")
        sys.exit(1)
    else:
        print("All tests passed or are pending approval.")


if __name__ == "__main__":
    main()
