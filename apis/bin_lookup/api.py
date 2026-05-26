"""BIN Lookup API (Mastercard BIN Resource Lookup) — OAuth 1.0a implementation."""
from __future__ import annotations

import os
from typing import Any, Dict

MANIFEST: Dict[str, Any] = {
    "id": "binlookup",
    "name": "BIN Lookup",
    "description": (
        "Mastercard BIN Resource Lookup API — identify the issuer, brand, "
        "country and product type for a Bank Identification Number (BIN)."
    ),
    "docs_url": "https://developer.mastercard.com/bin-lookup/documentation/",
    "how_to": (
        "<p><strong>BIN Lookup</strong> identifies a card's issuer, network, product type, and country "
        "from the first 6–8 digits of a payment card number (the Bank Identification Number, or BIN).</p>"
        "<h3>How to use</h3>"
        "<ol>"
        "<li>Select <strong>Lookup → Lookup BIN</strong> from the operations panel.</li>"
        "<li>Enter the first 6–8 digits of a card in the <strong>BIN / Account Range</strong> field — "
        "e.g. <code>511111</code> (Mastercard credit) or <code>411111</code> (Visa).</li>"
        "<li>Click <strong>Send</strong>. The response identifies the issuer, brand, product type, "
        "issuing country, and prepaid / debit flags.</li>"
        "</ol>"
        "<h3>What you get back</h3>"
        "<ul>"
        "<li><strong>Issuer name</strong> — the bank or institution that issued the card.</li>"
        "<li><strong>Brand</strong> — Mastercard, Visa, Amex, Discover, etc.</li>"
        "<li><strong>Product type</strong> — credit, debit, prepaid, corporate, etc.</li>"
        "<li><strong>Country</strong> — issuing country (ISO 3166-1 alpha-2).</li>"
        "<li><strong>Prepaid / debit flags</strong> — useful for payment routing and risk decisions.</li>"
        "</ul>"
    ),
    "categories": ["Lookup"],
    "state_schema": [],
    "configured": bool(
        os.environ.get("BINLOOKUP_CONSUMER_KEY")
        and os.environ.get("BINLOOKUP_CONSUMER_KEY") != "your-consumer-key-here"
        and os.environ.get("BINLOOKUP_SIGNING_KEY_PATH")
    ),
    "operations": [
        {
            "id": "lookup_bin",
            "name": "Lookup BIN",
            "category": "Lookup",
            "method": "POST",
            "description": "Look up a BIN (first 6–8 digits of a card number).",
            "params": [
                {
                    "name": "account_range",
                    "label": "BIN / Issuer",
                    "type": "select",
                    "default": "543210",
                    "required": True,
                    "options": [
                        {"value": "543210", "label": "543210 — Buckeye State Credit Union (US)"},
                        {"value": "111102", "label": "111102 — Arab Bank PLC (JO)"},
                        {"value": "356600", "label": "356600 — Credencial Argentina SA (AR)"},
                        {"value": "520000", "label": "520000 — Orange Bank (FR)"},
                        {"value": "541111", "label": "541111 — Entropay Limited (CH)"},
                    ],
                },
            ],
        },
    ],
}

_PROD_BASE_URL    = "https://api.mastercard.com/bin-resources"
_SANDBOX_BASE_URL = "https://sandbox.api.mastercard.com/bin-resources"
_ENDPOINT         = "/bin-ranges"          # supports filtering; works on free plan
_ENDPOINT_SEARCH  = "/bin-ranges/account-searches"  # requires paid plan


def _base_url() -> str:
    from simulator.switcher import sim_base_url
    env = os.environ.get("BINLOOKUP_ENV", "sandbox").lower()
    real = _PROD_BASE_URL if env == "production" else _SANDBOX_BASE_URL
    return sim_base_url("binlookup", real)


def _configured() -> bool:
    key = os.environ.get("BINLOOKUP_CONSUMER_KEY", "")
    path = os.environ.get("BINLOOKUP_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated("binlookup")


def get_state() -> Dict[str, Any]:
    return {"configured": _configured()}


def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if op_id == "lookup_bin":
        return _lookup_bin(params)
    return {"success": False, "error": f"Unknown operation: {op_id}"}


def _lookup_bin(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("binlookup"):
        return {
            "success": False,
            "error": (
                "BIN Lookup is not configured. Set BINLOOKUP_CONSUMER_KEY and "
                "BINLOOKUP_SIGNING_KEY_PATH in .env, then restart the server."
            ),
        }

    account_range = (params.get("account_range") or "").strip()
    if not account_range:
        return {"success": False, "error": "account_range is required"}

    import json
    import requests

    # Filter /bin-ranges by binNum — works on free plan (account-searches needs paid plan)
    base = _base_url()
    url_with_params = f"{base}{_ENDPOINT}?page=1&size=10"
    body = [{"key": "binNum", "value": account_range}]
    body_str = json.dumps(body)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    if is_simulated("binlookup"):
        headers["Authorization"] = "Simulated"
    else:
        consumer_key  = os.environ["BINLOOKUP_CONSUMER_KEY"]
        key_path      = os.environ["BINLOOKUP_SIGNING_KEY_PATH"]
        key_password  = os.environ.get("BINLOOKUP_SIGNING_KEY_PASSWORD", "keystorepassword")

        if not os.path.isabs(key_path):
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            key_path = os.path.join(project_root, key_path)

        import oauth1.authenticationutils as authutils
        from oauth1.oauth import OAuth

        try:
            signing_key = authutils.load_signing_key(key_path, key_password)
            auth_header = OAuth.get_authorization_header(url_with_params, "POST", body_str, consumer_key, signing_key)
            headers["Authorization"] = auth_header
        except Exception as e:
            return {"success": False, "error": f"OAuth signing failed: {e}"}

    try:
        resp = requests.post(url_with_params, data=body_str, headers=headers, timeout=15)
        status_code = resp.status_code
        try:
            resp_body = resp.json()
        except Exception:
            resp_body = {"raw": resp.text}
    except Exception as e:
        return {"success": False, "error": f"Request failed: {e}"}

    success = 200 <= status_code < 300
    if success:
        items = resp_body.get("items", [])
        data = {
            "items": items,
            "totalItems": resp_body.get("totalItems", 0),
            "currentPage": resp_body.get("currentPageNumber", 1),
        }
        if not items:
            data["note"] = "No matching BIN found in the sandbox dataset. Try a different BIN."
    else:
        data = {}
    return {
        "success": success,
        "data": data,
        "error": None if success else (resp_body.get("Errors", {}) or resp_body),
        "request": {
            "method": "POST",
            "url": url_with_params,
            "body": body,
        },
        "response": {
            "status_code": status_code,
            "body": resp_body,
        },
        "state_updates": {},
    }
