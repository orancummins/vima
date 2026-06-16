"""Consumer Clarity API (Ethoca / Mastercard) — OAuth 1.0a implementation.

Endpoint: POST https://sandbox.api.ethocaweb.com/ethoca/consumer-clarity/searches
Auth:     OAuth 1.0a  (same signing library as BIN Lookup)
Docs:     https://developer.mastercard.com/consumer-clarity/documentation/
"""
from __future__ import annotations

import os
from typing import Any

# ---------------------------------------------------------------------------
# Sandbox preset queries (from official test cases in the docs)
# ---------------------------------------------------------------------------
_PRESETS: dict[str, dict[str, Any]] = {
    "shoe_store": {
        "label": "SHOE STORE 1234 — Austin, TX, USA  →  The Shoe Store",
        "criteria": {
            "cardAcceptorName": "SHOE STORE 1234",
            "cardAcceptorLocation": "AUSTIN",
            "cardAcceptorRegionCode": "TX",
            "cardAcceptorCountryCode": None,
            "merchantCategoryCode": "5661",
        },
    },
    "academy_ny": {
        "label": "ZZZ*ACADEMY — New York, USA  →  Ziggy's School Center",
        "criteria": {
            "cardAcceptorName": "ZZZ*ACADEMY",
            "cardAcceptorLocation": "NEW YORK",
            "cardAcceptorRegionCode": None,
            "cardAcceptorCountryCode": "USA",
            "merchantCategoryCode": None,
        },
    },
    "bakery_leeds": {
        "label": "ANT*156LE — Leeds, GBR  →  Antler's Bakery",
        "criteria": {
            "cardAcceptorName": "ANT*156LE",
            "cardAcceptorLocation": "LEEDS",
            "cardAcceptorRegionCode": None,
            "cardAcceptorCountryCode": "GBR",
            "merchantCategoryCode": None,
        },
    },
    "applhmk_ny": {
        "label": "APPLHMK — New York, NY, USA  →  Apple Hammock's",
        "criteria": {
            "cardAcceptorName": "APPLHMK",
            "cardAcceptorLocation": "8002325512",
            "cardAcceptorRegionCode": "NY",
            "cardAcceptorCountryCode": "USA",
            "merchantCategoryCode": None,
        },
    },
    "my_chur_z_gr": {
        "label": "MY CHUR-Z — Pastida, GRC  →  My Churroz (Greece)",
        "criteria": {
            "cardAcceptorName": "MY CHUR-Z",
            "cardAcceptorLocation": "PASTIDA",
            "cardAcceptorRegionCode": None,
            "cardAcceptorCountryCode": "GRC",
            "merchantCategoryCode": None,
        },
    },
    "warehouse_nzl": {
        "label": "THE WAREHOUSE — Richmond, NZL  →  The Warehouse (New Zealand)",
        "criteria": {
            "cardAcceptorName": "THE WAREHOUSE",
            "cardAcceptorLocation": "RICHMOND",
            "cardAcceptorRegionCode": None,
            "cardAcceptorCountryCode": "NZL",
            "merchantCategoryCode": None,
        },
    },
}

_SANDBOX_BASE_URL = "https://sandbox.api.ethocaweb.com/ethoca"
_PROD_BASE_URL    = "https://api.ethocaweb.com/ethoca"
_ENDPOINT         = "/consumer-clarity/searches"

MANIFEST: dict[str, Any] = {
    "id": "consumer_clarity",
    "name": "Consumer Clarity",
    "description": (
        "Ethoca Consumer Clarity — enrich raw card-statement merchant names with "
        "clean merchant names, logos, location, category, and digital receipt links."
    ),
    "docs_url": "https://developer.mastercard.com/consumer-clarity/documentation/",
    "how_to": (
        "<p><strong>Consumer Clarity</strong> (Ethoca) turns raw card-statement merchant "
        "descriptors into rich merchant details — clean names, logos, addresses, "
        "MCC descriptions, and links to digital receipts where available.</p>"
        "<h3>How to use</h3>"
        "<ol>"
        "<li>Select <strong>Merchant Search → Search Merchant</strong>.</li>"
        "<li>Choose a preset transaction from the dropdown. Each preset matches a "
        "sandbox test case provided by Ethoca, so you will always get a real response.</li>"
        "<li>Click <strong>Send</strong>. The response includes the resolved merchant "
        "name, address, category, logo URLs, and receipt availability.</li>"
        "</ol>"
        "<h3>What you get back</h3>"
        "<ul>"
        "<li><strong>Merchant name</strong> — clean, consumer-facing name (e.g. "
        "<em>Antler's Bakery</em> instead of <em>ANT*156LE</em>).</li>"
        "<li><strong>Address &amp; location</strong> — full address with lat/lng.</li>"
        "<li><strong>Category</strong> — MCC code and human-readable description.</li>"
        "<li><strong>Logos</strong> — merchant and/or industry logo URLs.</li>"
        "<li><strong>Digital receipt</strong> — link if the merchant is on the Ethoca "
        "network.</li>"
        "</ul>"
        "<h3>Sandbox note</h3>"
        "<p>The presets above use Ethoca's published sandbox test-case data and will "
        "reliably return a match. Arbitrary merchant strings may return "
        "<em>MERCHANT_NOT_FOUND</em> in the sandbox environment.</p>"
    ),
    "categories": ["Merchant Search"],
    "state_schema": [],
    "configured": bool(
        os.environ.get("CONSUMER_CLARITY_CONSUMER_KEY")
        and os.environ.get("CONSUMER_CLARITY_CONSUMER_KEY") != "your-consumer-key-here"
        and os.environ.get("CONSUMER_CLARITY_SIGNING_KEY_PATH")
    ),
    "operations": [
        {
            "id": "search_merchant",
            "name": "Search Merchant",
            "category": "Merchant Search",
            "method": "POST",
            "description": (
                "Resolve a raw card-statement merchant descriptor to enriched "
                "merchant details (name, logo, address, MCC, receipt link)."
            ),
            "params": [
                {
                    "name": "preset",
                    "label": "Transaction preset",
                    "type": "select",
                    "default": "shoe_store",
                    "required": True,
                    "options": [
                        {"value": k, "label": v["label"]}
                        for k, v in _PRESETS.items()
                    ],
                },
            ],
        },
    ],
}


def _base_url() -> str:
    from simulator.switcher import sim_base_url
    env = os.environ.get("CONSUMER_CLARITY_ENV", "sandbox").lower()
    real = _PROD_BASE_URL if env == "production" else _SANDBOX_BASE_URL
    return sim_base_url("consumer_clarity", real)


def _configured() -> bool:
    key = os.environ.get("CONSUMER_CLARITY_CONSUMER_KEY", "")
    path = os.environ.get("CONSUMER_CLARITY_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated("consumer_clarity")


def get_state() -> dict[str, Any]:
    return {"configured": _configured()}


def execute(op_id: str, params: dict[str, Any]) -> dict[str, Any]:
    if op_id == "search_merchant":
        return _search_merchant(params)
    return {"success": False, "error": f"Unknown operation: {op_id}"}


def _search_merchant(params: dict[str, Any]) -> dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("consumer_clarity"):
        return {
            "success": False,
            "error": (
                "Consumer Clarity is not configured. Set CONSUMER_CLARITY_CONSUMER_KEY and "
                "CONSUMER_CLARITY_SIGNING_KEY_PATH in .env, then restart the server."
            ),
        }

    preset_key = (params.get("preset") or "shoe_store").strip()
    preset = _PRESETS.get(preset_key)
    if not preset:
        return {"success": False, "error": f"Unknown preset: {preset_key!r}"}

    criteria = {k: v for k, v in preset["criteria"].items()}

    import json

    import requests

    url = f"{_base_url()}{_ENDPOINT}"
    body_obj = {
        "locale": "en-US",
        "searchCriteria": [{"merchantCriteria": criteria}],
    }
    body_str = json.dumps(body_obj)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    if is_simulated("consumer_clarity"):
        headers["Authorization"] = "Simulated"
    else:
        import oauth1.authenticationutils as authutils
        from oauth1.oauth import OAuth

        consumer_key  = os.environ["CONSUMER_CLARITY_CONSUMER_KEY"]
        key_path      = os.environ["CONSUMER_CLARITY_SIGNING_KEY_PATH"]
        key_password  = os.environ.get("CONSUMER_CLARITY_SIGNING_KEY_PASSWORD", "keystorepassword")

        if not os.path.isabs(key_path):
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            key_path = os.path.join(project_root, key_path)

        try:
            signing_key = authutils.load_signing_key(key_path, key_password)
            auth_header = OAuth.get_authorization_header(
                url, "POST", body_str, consumer_key, signing_key
            )
            headers["Authorization"] = auth_header
        except Exception as exc:
            return {"success": False, "error": f"OAuth signing failed: {exc}"}

    try:
        resp = requests.post(url, data=body_str, headers=headers, timeout=15)
        status_code = resp.status_code
        try:
            resp_body = resp.json()
        except Exception:
            resp_body = {"raw": resp.text}
    except Exception as exc:
        return {"success": False, "error": f"Request failed: {exc}"}

    success = 200 <= status_code < 300
    if success:
        results = resp_body.get("searchResults", [])
        enriched = []
        for r in results:
            merchant = r.get("merchantResult", {})
            receipt  = r.get("purchaseReceipt", {})
            enriched.append({
                "recordId":       r.get("recordId"),
                "status":         r.get("resultStatus", {}).get("code"),
                "merchantName":   merchant.get("merchantName"),
                "address":        merchant.get("address"),
                "category":       merchant.get("merchantCategory"),
                "websiteUrl":     merchant.get("websiteUrl"),
                "logos":          merchant.get("logos", []),
                "location":       merchant.get("merchantLocation"),
                "merchantStatus": merchant.get("resultStatus", {}).get("code"),
                "receiptStatus":  receipt.get("resultStatus", {}).get("code"),
                "receiptUrl":     receipt.get("receiptUrl"),
            })
        data = {
            "results": enriched,
            "total":   len(enriched),
            "preset":  preset["label"],
        }
    else:
        data = {}

    return {
        "success": success,
        "data": data,
        "error": None if success else resp_body,
        "request": {
            "method": "POST",
            "url": url,
            "body": body_obj,
        },
        "response": {
            "status_code": status_code,
            "body": resp_body,
        },
        "state_updates": {},
    }
