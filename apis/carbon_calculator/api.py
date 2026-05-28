"""Mastercard Carbon Calculator API (carbon).

OAuth 1.0a one-legged signing. Payment-card registration operations
require JWE payload encryption (RSA-OAEP-256 + A256GCM) on the PAN.

Sandbox base: ``https://sandbox.api.mastercard.com/carbon``
Docs:         https://developer.mastercard.com/carbon-calculator/documentation/
Reference:    https://developer.mastercard.com/carbon-calculator/documentation/api-reference/

Operations exposed by this module (subset of the full surface):

  Service Provider
    GET  /service-providers
    PUT  /service-providers

  Payment Card (PII / encrypted)
    POST   /service-providers/payment-cards            (JWE — bulk register)
    DELETE /service-providers/payment-cards/{id}
    GET    /payment-cards/{id}/transaction-footprints
    POST   /payment-cards/transaction-footprints/aggregates

  Environmental Impact (no PAN — plain JSON)
    POST /transaction-footprints

  Supported parameters (reference data)
    GET /supported-currencies
    GET /supported-merchant-categories

Live sandbox access requires the issuer to be provisioned with a Mastercard
Customer ID (CID), Legal Name, and BIN range — none of which can be self-
provisioned via the portal wizard. Until that is done all live calls will
return 401/403.
"""
from __future__ import annotations

import json
import os
import uuid
from typing import Any, Dict, List, Optional


_PROD_BASE    = "https://api.mastercard.com/carbon"
_SANDBOX_BASE = "https://sandbox.api.mastercard.com/carbon"


def _base() -> str:
    from simulator.switcher import sim_base_url
    real = _PROD_BASE if os.environ.get("CARBON_CALCULATOR_ENV", "sandbox").lower() == "production" else _SANDBOX_BASE
    return sim_base_url("carbon_calculator", real)


def _configured() -> bool:
    key  = os.environ.get("CARBON_CALCULATOR_CONSUMER_KEY", "")
    path = os.environ.get("CARBON_CALCULATOR_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated("carbon_calculator")


def get_state() -> Dict[str, Any]:
    return {"configured": _configured()}


_HOW_TO = (
    "<p><strong>Carbon Calculator</strong> lets issuers surface the carbon "
    "footprint of cardholder transactions. Three integration options exist:</p>"
    "<ul>"
    "<li><strong>Option 1</strong> — Mastercard processes the transactions: "
    "register the consumer's PAN with the API and receive near real-time "
    "transaction footprint notifications.</li>"
    "<li><strong>Option 2.a</strong> — Issuer-processed transactions sent to "
    "<code>POST /transaction-footprints</code> for instant carbon scoring.</li>"
    "<li><strong>Option 2.b</strong> — Bulk file-based scoring through "
    "Mastercard File Exchange.</li>"
    "</ul>"
    "<h3>Operations</h3>"
    "<ol>"
    "<li><strong>Service Provider</strong> — <code>GET / PUT /service-providers</code>: "
    "view and update issuer onboarding details. The GET op is the recommended "
    "sandbox smoke test once your CID is provisioned.</li>"
    "<li><strong>Transaction Footprints</strong> — <code>POST /transaction-footprints</code>: "
    "compute carbon scores for a batch of payment transactions (no PAN required).</li>"
    "<li><strong>Aggregates</strong> — <code>POST /payment-cards/transaction-footprints/aggregates</code>: "
    "weekly / monthly aggregates for registered cards.</li>"
    "<li><strong>Historical footprints</strong> — <code>GET /payment-cards/{id}/transaction-footprints</code>.</li>"
    "<li><strong>Bulk register cards</strong> — <code>POST /service-providers/payment-cards</code> "
    "<em>(JWE-encrypted; not implemented in this client yet)</em>.</li>"
    "<li><strong>Delete card</strong> — <code>DELETE /service-providers/payment-cards/{id}</code>.</li>"
    "<li><strong>Supported reference data</strong> — <code>GET /supported-currencies</code> "
    "and <code>GET /supported-merchant-categories</code>.</li>"
    "</ol>"
    "<h3>Manual onboarding required</h3>"
    "<p class='muted'>Live sandbox access requires a Mastercard-issued Customer "
    "ID (CID), Legal Name, and BIN range. Until those are supplied at project "
    "creation, live calls will return 401/403 — use the simulator for local "
    "development.</p>"
    "<p>"
    "<a href='https://developer.mastercard.com/create-project/carbon-calculator?services=carbon-calculator' "
    "target='_blank' rel='noopener'><strong>Create a sandbox project ↗</strong></a> "
    "&nbsp;·&nbsp; "
    "<a href='https://developer.mastercard.com/carbon-calculator/documentation/quick-start-guide/' "
    "target='_blank' rel='noopener'>Quick start guide ↗</a> "
    "&nbsp;·&nbsp; "
    "<a href='mailto:carboncalculator@mastercard.com'>"
    "Email carboncalculator@mastercard.com</a>"
    "</p>"
)


_ENC_NOTE = (
    "PAN registration requires JWE payload encryption "
    "(RSA-OAEP-256 + A256GCM). The Mastercard client-encryption library is "
    "not wired in for Carbon Calculator yet — use the simulator for local "
    "development."
)


# --- params -----------------------------------------------------------------

_SP_UPDATE_PARAMS: List[Dict[str, Any]] = [
    {"name": "legalName", "label": "Legal name",           "type": "text", "default": "Test Issuer", "required": False},
    {"name": "country",   "label": "Country (ISO-3166-1)", "type": "text", "default": "USA",         "required": False},
]

_BULK_CARDS_PARAMS: List[Dict[str, Any]] = [
    {"name": "primaryAccountNumbers", "label": "PANs (comma-separated)", "type": "text",
     "default": "5204735874100012", "required": True,
     "help": "Sandbox PANs only. Encrypted as a JWE on the wire."},
]

_DELETE_CARD_PARAMS: List[Dict[str, Any]] = [
    {"name": "paymentCardId", "label": "Payment card ID", "type": "text", "default": "", "required": True},
]

_HISTORICAL_PARAMS: List[Dict[str, Any]] = [
    {"name": "paymentCardId", "label": "Payment card ID", "type": "text", "default": "", "required": True},
    {"name": "fromDate",      "label": "From date (YYYY-MM-DD)", "type": "text", "default": "", "required": False},
    {"name": "toDate",        "label": "To date (YYYY-MM-DD)",   "type": "text", "default": "", "required": False},
]

_AGGREGATE_PARAMS: List[Dict[str, Any]] = [
    {"name": "paymentCardIds", "label": "Payment card IDs (comma-separated)",
     "type": "text", "default": "", "required": True},
    {"name": "aggregation",    "label": "Aggregation",
     "type": "select", "default": "MONTHLY", "required": True,
     "options": [{"value": "WEEKLY", "label": "Weekly"}, {"value": "MONTHLY", "label": "Monthly"}]},
]

_TXN_FOOTPRINT_PARAMS: List[Dict[str, Any]] = [
    {"name": "amount",        "label": "Amount",              "type": "number", "default": 42.50, "required": True},
    {"name": "currency",      "label": "Currency (ISO-4217)", "type": "text",   "default": "USD", "required": True},
    {"name": "mcc",           "label": "MCC",                 "type": "text",   "default": "5411", "required": True,
     "help": "4-digit Merchant Category Code (e.g. 5411 = grocery)."},
    {"name": "transactionId", "label": "Transaction ID",      "type": "text",   "default": "txn-001", "required": False},
]


MANIFEST: Dict[str, Any] = {
    "id": "carbon_calculator",
    "name": "Carbon Calculator",
    "description": (
        "Mastercard Carbon Calculator — calculate the carbon footprint of "
        "payment transactions, register PANs for near real-time scoring, and "
        "surface aggregates / historical footprints. OAuth 1.0a with JWE "
        "payload encryption on PAN-bearing operations."
    ),
    "docs_url": "https://developer.mastercard.com/carbon-calculator/documentation/",
    "how_to": _HOW_TO,
    "categories": ["Service Provider", "Payment Cards", "Environmental Impact", "Reference"],
    "state_schema": [
        {"name": "lastPaymentCardId", "label": "Last payment card ID", "type": "text", "default": ""},
    ],
    "configured": _configured(),
    "operations": [
        {
            "id": "get_service_provider",
            "name": "View service provider",
            "category": "Service Provider",
            "method": "GET",
            "description": "Fetch the calling service-provider's onboarding details. Recommended sandbox smoke test.",
            "params": [],
        },
        {
            "id": "update_service_provider",
            "name": "Update service provider",
            "category": "Service Provider",
            "method": "PUT",
            "description": "Update the service-provider record (e.g. legal name, country).",
            "params": _SP_UPDATE_PARAMS,
        },
        {
            "id": "bulk_register_cards",
            "name": "Bulk register payment cards",
            "category": "Payment Cards",
            "method": "POST",
            "description": "Register one or more PANs for near real-time transaction footprint notifications. PANs are JWE-encrypted.",
            "params": _BULK_CARDS_PARAMS,
            "encryption_required": True,
        },
        {
            "id": "delete_card",
            "name": "Delete payment card",
            "category": "Payment Cards",
            "method": "DELETE",
            "description": "Remove a previously registered payment card by id.",
            "params": _DELETE_CARD_PARAMS,
        },
        {
            "id": "historical_footprints",
            "name": "Historical transaction footprints",
            "category": "Payment Cards",
            "method": "GET",
            "description": "Fetch historical transactions and their carbon footprints for a registered card.",
            "params": _HISTORICAL_PARAMS,
        },
        {
            "id": "aggregate_footprints",
            "name": "Aggregate footprints",
            "category": "Payment Cards",
            "method": "POST",
            "description": "Aggregate carbon scores weekly / monthly across one or more registered cards.",
            "params": _AGGREGATE_PARAMS,
        },
        {
            "id": "calculate_footprint",
            "name": "Calculate transaction footprint",
            "category": "Environmental Impact",
            "method": "POST",
            "description": "Compute the carbon score for a payment transaction without registering a PAN.",
            "params": _TXN_FOOTPRINT_PARAMS,
        },
        {
            "id": "supported_currencies",
            "name": "Supported currencies",
            "category": "Reference",
            "method": "GET",
            "description": "List the ISO-4217 currencies supported by the API.",
            "params": [],
        },
        {
            "id": "supported_mccs",
            "name": "Supported merchant categories",
            "category": "Reference",
            "method": "GET",
            "description": "List the MCCs (Merchant Category Codes) supported by the API.",
            "params": [],
        },
    ],
}


def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if op_id == "get_service_provider":
        return _signed_request("GET", "/service-providers")
    if op_id == "update_service_provider":
        body = {k: (params.get(k) or "").strip() for k in ("legalName", "country") if (params.get(k) or "").strip()}
        return _signed_request("PUT", "/service-providers", body=body)
    if op_id == "delete_card":
        cid = (params.get("paymentCardId") or "").strip()
        if not cid:
            return {"success": False, "error": "paymentCardId is required."}
        return _signed_request("DELETE", f"/service-providers/payment-cards/{cid}")
    if op_id == "historical_footprints":
        cid = (params.get("paymentCardId") or "").strip()
        if not cid:
            return {"success": False, "error": "paymentCardId is required."}
        q: Dict[str, Any] = {}
        for k in ("fromDate", "toDate"):
            v = (params.get(k) or "").strip()
            if v:
                q[k] = v
        return _signed_request("GET", f"/payment-cards/{cid}/transaction-footprints", query=q or None)
    if op_id == "aggregate_footprints":
        ids = [x.strip() for x in (params.get("paymentCardIds") or "").split(",") if x.strip()]
        if not ids:
            return {"success": False, "error": "Provide at least one paymentCardId."}
        body = {
            "paymentCardIds": ids,
            "aggregation":    (params.get("aggregation") or "MONTHLY").strip(),
        }
        return _signed_request("POST", "/payment-cards/transaction-footprints/aggregates", body=body)
    if op_id == "calculate_footprint":
        try:
            amount = float(params.get("amount") or 0)
        except (TypeError, ValueError):
            return {"success": False, "error": "amount must be a number."}
        body = {
            "transactions": [{
                "transactionId": (params.get("transactionId") or f"txn-{uuid.uuid4().hex[:8]}").strip(),
                "amount":   amount,
                "currency": (params.get("currency") or "USD").strip().upper(),
                "mcc":      (params.get("mcc") or "5411").strip(),
            }],
        }
        return _signed_request("POST", "/transaction-footprints", body=body)
    if op_id == "supported_currencies":
        return _signed_request("GET", "/supported-currencies")
    if op_id == "supported_mccs":
        return _signed_request("GET", "/supported-merchant-categories")
    if op_id == "bulk_register_cards":
        return {
            "success": False,
            "error": _ENC_NOTE,
            "request":  {"method": "POST", "url": f"{_base()}/service-providers/payment-cards", "body": params},
            "response": {"status_code": None, "body": None},
            "state_updates": {},
        }
    return {"success": False, "error": f"Unknown operation: {op_id}"}


# ---------------------------------------------------------------------------
# Signed request helper
# ---------------------------------------------------------------------------

def _signed_request(
    method: str,
    path: str,
    *,
    body: Optional[Dict[str, Any]] = None,
    query: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("carbon_calculator"):
        return {
            "success": False,
            "error": (
                "Carbon Calculator is not configured. Set CARBON_CALCULATOR_CONSUMER_KEY "
                "and CARBON_CALCULATOR_SIGNING_KEY_PATH in .env, then restart the server. "
                "Note: live sandbox access also requires a Mastercard Customer ID (CID)."
            ),
        }

    from urllib.parse import urlencode
    import requests

    url = f"{_base()}{path}"
    if query:
        url = f"{url}?{urlencode(query)}"

    body_str = json.dumps(body) if body is not None else None

    if is_simulated("carbon_calculator"):
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

        consumer_key = os.environ["CARBON_CALCULATOR_CONSUMER_KEY"]
        key_path     = os.environ["CARBON_CALCULATOR_SIGNING_KEY_PATH"]
        key_password = os.environ.get("CARBON_CALCULATOR_SIGNING_KEY_PASSWORD", "keystorepassword")

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
            resp_body = {"raw": resp.text} if resp.text else {}
    except Exception as e:
        return {"success": False, "error": f"Request failed: {e}"}

    success = 200 <= status_code < 300
    state_updates: Dict[str, Any] = {}
    if success and isinstance(resp_body, dict):
        card_id = resp_body.get("paymentCardId") or resp_body.get("id")
        if card_id:
            state_updates["lastPaymentCardId"] = str(card_id)

    return {
        "success": success,
        "data":    resp_body if success else {},
        "error":   None if success else (resp_body.get("Errors", {}) if isinstance(resp_body, dict) else resp_body),
        "request": {"method": method, "url": url, "body": body},
        "response": {"status_code": status_code, "body": resp_body},
        "state_updates": state_updates,
    }
