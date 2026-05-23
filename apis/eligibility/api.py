"""Mastercard Benefits Eligibility API (loyalty/eligibility).

OAuth 1.0a one-legged, body-signed.

Sandbox test data (from Mastercard Testing page):
    cardNumber:          5341676355168133
    serviceProviderCode: 6

Endpoints:
    POST /benefits/searches      - Search benefits  (cardNumber OR cardNumberId)
    POST /products/searches      - Search products  (cardNumber OR cardNumberId)
    GET  /widgets/access-tokens  - Generate widget access token (no params)
    POST /card-identifiers       - Tokenise PAN  (JWE encryption required)

Docs: https://developer.mastercard.com/eligibility-api/documentation/
Spec: /eligibility-api/swagger/eligibility-spec.yaml
"""
from __future__ import annotations

import json
import os
import uuid
from typing import Any, Dict, List, Optional


_PROD_BASE    = "https://api.mastercard.com/loyalty/eligibility"
_SANDBOX_BASE = "https://sandbox.api.mastercard.com/loyalty/eligibility"


def _base() -> str:
    from simulator.switcher import sim_base_url
    real = _PROD_BASE if os.environ.get("ELIGIBILITY_ENV", "sandbox").lower() == "production" else _SANDBOX_BASE
    return sim_base_url("eligibility", real)


def _configured() -> bool:
    key  = os.environ.get("ELIGIBILITY_CONSUMER_KEY", "")
    path = os.environ.get("ELIGIBILITY_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated("eligibility")


def get_state() -> Dict[str, Any]:
    return {"configured": _configured()}


_CARD_OPTIONS = [
    {"value": "5416116000000233", "label": "5416116000000233 — Sandbox PAN (tutorial, returns HMB benefits)"},
    {"value": "5341676355168133", "label": "5341676355168133 — Sandbox PAN (testing page, may 400 if BIN not provisioned)"},
    {"value": "5291070000000000", "label": "5291070000000000 — Sandbox PAN (BCES testing page)"},
]

_SERVICE_PROVIDER_OPTIONS = [
    {"value": "",  "label": "(any vendor)"},
    {"value": "6", "label": "6 — Sandbox test service provider"},
]

_PRODUCT_CODE_OPTIONS = [
    {"value": "",    "label": "(auto / not required)"},
    {"value": "DCG", "label": "DCG — Sandbox test product"},
    {"value": "MST", "label": "MST — Standard"},
    {"value": "MGD", "label": "MGD — Gold"},
    {"value": "MPL", "label": "MPL — Platinum"},
    {"value": "MWE", "label": "MWE — World Elite"},
    {"value": "MWP", "label": "MWP — World"},
    {"value": "MBC", "label": "MBC — Business"},
]


_HOW_TO = (
    "<p><strong>Benefits Eligibility</strong> checks whether a cardholder is entitled "
    "to specific Mastercard benefits, and lets a vendor mint an access token for an "
    "embedded benefits widget.</p>"
    "<h3>Sandbox test data</h3>"
    "<ul>"
    "<li><code>cardNumber</code>: <code>5416116000000233</code> (tutorial, returns HMB benefits)</li>"
    "<li><code>benefitCode</code>: <code>HMB</code> (works with the above PAN)</li>"
    "<li><code>serviceProviderCode</code>: <code>6</code></li>"
    "</ul>"
    "<h3>How to use</h3>"
    "<ol>"
    "<li>Open <strong>Benefits → Search benefits</strong>. Provide either a "
    "<code>cardNumber</code> (6-digit BIN or 12–19-digit PAN) <em>or</em> a "
    "<code>cardNumberId</code> (UUID-style identifier). Optionally narrow with "
    "<code>serviceProviderCode</code>, <code>productCode</code>, "
    "<code>benefitCode</code> or <code>effectiveDate</code>.</li>"
    "<li>The response contains a <code>data[]</code> array — each entry has "
    "<code>benefitBundleId</code>, <code>benefitID</code>, <code>benefitCode</code>, "
    "and rich policy data.</li>"
    "<li>Feed any <code>benefitCode</code> + <code>productCode</code> into "
    "the BCES API → <em>Search benefit contents</em> to retrieve renderable "
    "marketing content for those benefits.</li>"
    "<li>Use <strong>Products → Search products</strong> for the catalogue of "
    "Mastercard products tied to a card / BIN.</li>"
    "<li>Use <strong>Widget → Generate access token</strong> to mint a "
    "short-lived widget access token (takes no parameters).</li>"
    "</ol>"
    "<p class='muted'>Sandbox PANs only — never submit real card data.</p>"
)


_BENEFIT_PARAMS: List[Dict[str, Any]] = [
    {"name": "cardNumber",          "label": "Card number / BIN",     "type": "select", "default": "5416116000000233", "required": False, "options": _CARD_OPTIONS, "help": "6-digit BIN or 12–19-digit PAN. Provide this OR cardNumberId."},
    {"name": "cardNumberId",        "label": "Card number ID (UUID)", "type": "text",   "default": "", "required": False, "help": "36–40 char UUID returned by /card-identifiers."},
    {"name": "effectiveDate",       "label": "Effective date",        "type": "text",   "default": "", "required": False, "help": "YYYY-MM-DD. Defaults to today."},
    {"name": "serviceProviderCode", "label": "Service provider",      "type": "select", "default": "", "required": False, "options": _SERVICE_PROVIDER_OPTIONS, "help": "Optional — restrict to a specific benefit vendor."},
    {"name": "productCode",         "label": "Product code",          "type": "select", "default": "", "required": False, "options": _PRODUCT_CODE_OPTIONS, "help": "3-char alpha. Required only if the BIN has multiple products."},
    {"name": "benefitCode",         "label": "Benefit code",          "type": "text",   "default": "", "required": False, "help": "Optional — 3-char alpha benefit code (e.g. CDW)."},
]

_PRODUCT_PARAMS: List[Dict[str, Any]] = [
    {"name": "cardNumber",    "label": "Card number / BIN",     "type": "select", "default": "5416116000000233", "required": False, "options": _CARD_OPTIONS},
    {"name": "cardNumberId",  "label": "Card number ID (UUID)", "type": "text",   "default": "", "required": False},
    {"name": "effectiveDate", "label": "Effective date",        "type": "text",   "default": "", "required": False, "help": "YYYY-MM-DD. Defaults to today."},
]


MANIFEST: Dict[str, Any] = {
    "id": "eligibility",
    "name": "Benefits Eligibility",
    "description": (
        "Mastercard Benefits Eligibility — verify benefits a cardholder is "
        "entitled to, browse the loyalty product catalogue, and mint short-lived "
        "access tokens for embeddable widgets. OAuth 1.0a, body-signed."
    ),
    "docs_url": "https://developer.mastercard.com/eligibility-api/documentation/",
    "how_to": _HOW_TO,
    "categories": ["Benefits", "Products", "Widget", "Card Identifiers"],
    "state_schema": [
        {"name": "lastCardNumberId", "label": "Last cardNumberId",    "type": "text", "default": ""},
        {"name": "lastBundleId",     "label": "Last benefitBundleId", "type": "text", "default": ""},
        {"name": "lastBenefitCode",  "label": "Last benefitCode",     "type": "text", "default": ""},
        {"name": "lastProductCode",  "label": "Last productCode",     "type": "text", "default": ""},
    ],
    "configured": _configured(),
    "operations": [
        {
            "id": "search_benefits",
            "name": "Search benefits",
            "category": "Benefits",
            "method": "POST",
            "description": "Returns the benefits a cardNumber (BIN or PAN) or cardNumberId is eligible for on a given date.",
            "params": _BENEFIT_PARAMS,
        },
        {
            "id": "search_products",
            "name": "Search products",
            "category": "Products",
            "method": "POST",
            "description": "Returns Mastercard product information (ICA + product list) for a cardNumber or cardNumberId.",
            "params": _PRODUCT_PARAMS,
        },
        {
            "id": "access_token",
            "name": "Generate widget access token",
            "category": "Widget",
            "method": "GET",
            "description": "Mint a short-lived widget access token (no parameters).",
            "params": [],
        },
        {
            "id": "card_identifier",
            "name": "Generate card identifier",
            "category": "Card Identifiers",
            "method": "POST",
            "description": "Tokenise a PAN into a cardNumberId. Requires JWE field-level encryption — not implemented in this client.",
            "params": [
                {"name": "cardNumber", "label": "Card number (sandbox PAN)", "type": "text", "default": "5416116000000233", "required": True},
            ],
            "encryption_required": True,
        },
    ],
}


def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if op_id == "search_benefits":
        return _search_benefits(params)
    if op_id == "search_products":
        return _search_products(params)
    if op_id == "access_token":
        return _access_token(params)
    if op_id == "card_identifier":
        return {
            "success": False,
            "error": (
                "Generate card identifier requires JWE field-level encryption, "
                "which isn't implemented in this client. Use cardNumber directly "
                "with Search Benefits in the sandbox."
            ),
            "request":  {"method": "POST", "url": f"{_base()}/card-identifiers", "body": params},
            "response": {"status_code": None, "body": None},
            "state_updates": {},
        }
    return {"success": False, "error": f"Unknown operation: {op_id}"}


def _search_benefits(params: Dict[str, Any]) -> Dict[str, Any]:
    card_number    = (params.get("cardNumber") or "").strip()
    card_number_id = (params.get("cardNumberId") or "").strip()
    if not card_number and not card_number_id:
        return {"success": False, "error": "Provide cardNumber or cardNumberId."}

    body: Dict[str, Any] = {}
    if card_number_id:
        body["cardNumberId"] = card_number_id
    else:
        body["cardNumber"] = card_number

    for opt_key in ("effectiveDate", "serviceProviderCode", "productCode", "benefitCode"):
        v = (params.get(opt_key) or "").strip()
        if v:
            body[opt_key] = v

    result = _signed_request("POST", "/benefits/searches", body=body)
    if result.get("success"):
        result["state_updates"] = _capture_ids(result.get("response", {}).get("body"))
    return result


def _search_products(params: Dict[str, Any]) -> Dict[str, Any]:
    card_number    = (params.get("cardNumber") or "").strip()
    card_number_id = (params.get("cardNumberId") or "").strip()
    if not card_number and not card_number_id:
        return {"success": False, "error": "Provide cardNumber or cardNumberId."}

    body: Dict[str, Any] = {}
    if card_number_id:
        body["cardNumberId"] = card_number_id
    else:
        body["cardNumber"] = card_number

    eff = (params.get("effectiveDate") or "").strip()
    if eff:
        body["effectiveDate"] = eff

    return _signed_request("POST", "/products/searches", body=body)


def _access_token(_params: Dict[str, Any]) -> Dict[str, Any]:
    return _signed_request("GET", "/widgets/access-tokens")


def _capture_ids(body: Any) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    keymap = {
        "benefitBundleId": "lastBundleId",
        "benefitCode":     "lastBenefitCode",
        "productCode":     "lastProductCode",
        "cardNumberId":    "lastCardNumberId",
    }

    def walk(node: Any):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in keymap and isinstance(v, (str, int)) and out.get(keymap[k]) in (None, ""):
                    out[keymap[k]] = str(v)
                walk(v)
        elif isinstance(node, list):
            for x in node:
                walk(x)

    walk(body)
    return out


def _signed_request(
    method: str,
    path: str,
    *,
    body: Optional[Dict[str, Any]] = None,
    query: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("eligibility"):
        return {
            "success": False,
            "error": (
                "Benefits Eligibility is not configured. Set ELIGIBILITY_CONSUMER_KEY "
                "and ELIGIBILITY_SIGNING_KEY_PATH in .env, then restart the server."
            ),
        }

    from urllib.parse import urlencode
    import requests

    url = f"{_base()}{path}"
    if query:
        url = f"{url}?{urlencode(query)}"

    body_str = json.dumps(body) if body is not None else None

    if is_simulated("eligibility"):
        headers: Dict[str, str] = {
            "Accept": "application/json",
            "x-openapi-transid": str(uuid.uuid4()),
        }
        if body_str is not None:
            headers["Content-Type"] = "application/json"
        headers["Authorization"] = "Simulated"
    else:
        import oauth1.authenticationutils as authutils
        from oauth1.oauth import OAuth

        consumer_key = os.environ["ELIGIBILITY_CONSUMER_KEY"]
        key_path     = os.environ["ELIGIBILITY_SIGNING_KEY_PATH"]
        key_password = os.environ.get("ELIGIBILITY_SIGNING_KEY_PASSWORD", "keystorepassword")

        if not os.path.isabs(key_path):
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            key_path = os.path.join(project_root, key_path)

        headers = {
            "Accept": "application/json",
            "X-OpenApi-ClientId": consumer_key.split("!", 1)[0],
            "x-openapi-transid":  str(uuid.uuid4()),
        }
        if body_str is not None:
            headers["Content-Type"] = "application/json"

        try:
            signing_key = authutils.load_signing_key(key_path, key_password)
            headers["Authorization"] = OAuth.get_authorization_header(
                url, method, body_str, consumer_key, signing_key,
            )
        except Exception as e:
            return {"success": False, "error": f"OAuth signing failed: {e}"}

    try:
        resp = requests.request(method, url, data=body_str, headers=headers, timeout=20)
        status_code = resp.status_code
        try:
            resp_body: Any = resp.json()
        except Exception:
            resp_body = {"raw": resp.text}
    except Exception as e:
        return {"success": False, "error": f"Request failed: {e}"}

    success = 200 <= status_code < 300
    return {
        "success": success,
        "data":    resp_body if success else {},
        "error":   None if success else (resp_body.get("Errors", {}) if isinstance(resp_body, dict) else resp_body),
        "request": {"method": method, "url": url, "body": body},
        "response": {"status_code": status_code, "body": resp_body},
        "state_updates": {},
    }
