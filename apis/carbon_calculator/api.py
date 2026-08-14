"""Mastercard Carbon Calculator API (carbon).

OAuth 1.0a one-legged signing. Payment-card registration operations
require Field Level Encryption (FLE / RSA-OAEP-256 + AES-128-CBC) on the PAN.

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
from typing import Any

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


def get_state() -> dict[str, Any]:
    return {"configured": _configured()}


_HOW_TO = (
    "<p><strong>Carbon Calculator</strong> surfaces the estimated carbon footprint of "
    "payment card transactions so issuers can show cardholders their environmental "
    "impact in real time.</p>"
    "<h3>How to use</h3>"
    "<ol>"
    "<li>Start with <strong>Reference &rarr; Supported merchant categories</strong> "
    "(no parameters). Returns every MCC the API scores — e.g. "
    "<code>5411</code> = Grocery, <code>5812</code> = Restaurant, "
    "<code>4111</code> = Transit, <code>5541</code> = Fuel.</li>"
    "<li>Select <strong>Environmental Impact &rarr; Calculate transaction footprint</strong>. "
    "Enter:<br>"
    "&nbsp;&nbsp;<strong>Amount</strong>: <code>42.50</code><br>"
    "&nbsp;&nbsp;<strong>Currency</strong>: <code>USD</code><br>"
    "&nbsp;&nbsp;<strong>MCC</strong>: <code>5411</code> (grocery)<br>"
    "Click <strong>Send</strong>. The response returns <code>carbonEmissionInGrams</code> "
    "— e.g. ~12 750 g CO&#8322; for a $42.50 grocery spend.</li>"
    "<li>Once your service provider is provisioned with a Mastercard Customer ID (CID), "
    "try <strong>Service Provider &rarr; View service provider</strong> to confirm your "
    "CID and registered BIN ranges.</li>"
    "<li>To register cards for near real-time scoring, use "
    "<strong>Payment Cards &rarr; Bulk register payment cards</strong> and enter one or more "
    "sandbox PANs (BIN prefixes <code>534403</code>, <code>518145</code>, <code>518152</code>, "
    "<code>5403</code>, <code>5424</code>). "
    "Requires <code>CARBON_CALCULATOR_ENCRYPTION_KEY_PATH</code> set to your "
    "downloaded client encryption certificate.</li>"
    "</ol>"
    "<h3>What you get back</h3>"
    "<ul>"
    "<li><strong>carbonEmissionInGrams</strong> — estimated CO&#8322; equivalent in grams.</li>"
    "<li><strong>transactionId</strong> — echoed back for correlation.</li>"
    "<li><strong>paymentCardId</strong> — assigned ID after successful card registration.</li>"
    "<li><strong>legalName / binRanges</strong> — your service-provider onboarding details.</li>"
    "</ul>"
    "<h3>Test data &amp; references</h3>"
    "<ul>"
    "<li>Sandbox base URL: <code>https://sandbox.api.mastercard.com/carbon</code></li>"
    "<li>Reference MCCs: <code>5411</code> (grocery), <code>5812</code> (restaurant), "
    "<code>4111</code> (transit), <code>5541</code> (fuel)</li>"
    "<li>Tutorial test BIN prefixes: <code>534403</code>, <code>518145</code>, "
    "<code>518152</code>, <code>5403</code>, <code>5424</code></li>"
    "<li><a href='https://developer.mastercard.com/carbon-calculator/documentation/' "
    "target='_blank' rel='noopener'>API documentation</a></li>"
    "<li><a href='https://developer.mastercard.com/carbon-calculator/documentation/api-reference/' "
    "target='_blank' rel='noopener'>Try It console</a></li>"
    "<li><a href='https://developer.mastercard.com/carbon-calculator/tutorial/api-testing/' "
    "target='_blank' rel='noopener'>Test cases tutorial</a></li>"
    "</ul>"
    "<p><em>Live sandbox access requires a Mastercard-issued Customer ID (CID), "
    "Legal Name, and BIN range — contact "
    "<a href='mailto:carboncalculator@mastercard.com'>carboncalculator@mastercard.com</a>. "
    "The <strong>Reference</strong> and <strong>Environmental Impact</strong> operations "
    "work without CID provisioning once your signing key is configured.</em></p>"
    "<p>"
    "<a href='https://developer.mastercard.com/create-project/carbon-calculator?services=carbon-calculator' "
    "target='_blank' rel='noopener'><strong>Create a sandbox project &#8599;</strong></a> "
    "&nbsp;&middot;&nbsp; "
    "<a href='https://developer.mastercard.com/carbon-calculator/documentation/quick-start-guide/' "
    "target='_blank' rel='noopener'>Quick start guide &#8599;</a> "
    "&nbsp;&middot;&nbsp; "
    "<a href='mailto:carboncalculator@mastercard.com'>Email carboncalculator@mastercard.com</a>"
    "</p>"
)


_ENC_KEY_MISSING = (
    "CARBON_CALCULATOR_ENCRYPTION_KEY_PATH is not set. "
    "Download the client encryption certificate (.pem) from your sandbox project on "
    "developer.mastercard.com and set this environment variable to its path."
)


# --- params -----------------------------------------------------------------

_SP_UPDATE_PARAMS: list[dict[str, Any]] = [
    {"name": "legalName", "label": "Legal name",           "type": "text", "default": "Test Issuer", "required": False},
    {"name": "country",   "label": "Country (ISO-3166-1)", "type": "text", "default": "USA",         "required": False},
]

_BULK_CARDS_PARAMS: list[dict[str, Any]] = [
    {"name": "primaryAccountNumbers", "label": "PANs (comma-separated)", "type": "text",
     "default": "5204735874100012", "required": True,
     "help": "Sandbox PANs only. Encrypted as a JWE on the wire."},
]

_DELETE_CARD_PARAMS: list[dict[str, Any]] = [
    {"name": "paymentCardId", "label": "Payment card ID", "type": "text", "default": "", "required": True},
]

_HISTORICAL_PARAMS: list[dict[str, Any]] = [
    {"name": "paymentCardId", "label": "Payment card ID", "type": "text", "default": "", "required": True},
    {"name": "fromDate",      "label": "From date (YYYY-MM-DD)", "type": "text", "default": "", "required": False},
    {"name": "toDate",        "label": "To date (YYYY-MM-DD)",   "type": "text", "default": "", "required": False},
]

_AGGREGATE_PARAMS: list[dict[str, Any]] = [
    {"name": "paymentCardIds", "label": "Payment card IDs (comma-separated)",
     "type": "text", "default": "", "required": True},
    {"name": "aggregation",    "label": "Aggregation",
     "type": "select", "default": "MONTHLY", "required": True,
     "options": [{"value": "WEEKLY", "label": "Weekly"}, {"value": "MONTHLY", "label": "Monthly"}]},
]

_TXN_FOOTPRINT_PARAMS: list[dict[str, Any]] = [
    {"name": "amount",        "label": "Amount",              "type": "number", "default": 42.50, "required": True},
    {"name": "currency",      "label": "Currency (ISO-4217)", "type": "text",   "default": "USD", "required": True},
    {"name": "mcc",           "label": "MCC",                 "type": "text",   "default": "5411", "required": True,
     "help": "4-digit Merchant Category Code (e.g. 5411 = grocery)."},
    {"name": "transactionId", "label": "Transaction ID",      "type": "text",   "default": "txn-001", "required": False},
]


MANIFEST: dict[str, Any] = {
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
            "description": "Register one or more PANs for near real-time transaction footprint notifications. PANs are field-level encrypted (FLE). Requires CARBON_CALCULATOR_ENCRYPTION_KEY_PATH.",
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


def execute(op_id: str, params: dict[str, Any]) -> dict[str, Any]:
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
        q: dict[str, Any] = {}
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
        pans_raw = params.get("primaryAccountNumbers", "")
        if isinstance(pans_raw, str):
            pans = [p.strip() for p in pans_raw.split(",") if p.strip()]
        else:
            pans = [str(p).strip() for p in pans_raw if str(p).strip()]
        if not pans:
            return {"success": False, "error": "Provide at least one PAN."}
        return _bulk_register_live(pans)
    return {"success": False, "error": f"Unknown operation: {op_id}"}


# ---------------------------------------------------------------------------
# FLE (field-level encryption) helper for PAN-bearing operations
# ---------------------------------------------------------------------------

_FLE_CONFIG_DICT = {
    "paths": {
        "$": {
            "toEncrypt": {"$": "$"},
            "toDecrypt": {"encryptedData": "$"},
        }
    },
    # encryptionCertificate is injected at call time from env
    "encryptedValueFieldName":             "encryptedData",
    "encryptedKeyFieldName":               "encryptedKey",
    "oaepPaddingDigestAlgorithm":          "SHA256",
    "oaepPaddingDigestAlgorithmFieldName": "oaepHashingAlgorithm",
    "encryptionKeyFingerprintFieldName":   "publicKeyFingerprint",
    "ivFieldName":                         "iv",
    "dataEncoding":                        "HEX",
}


def _bulk_register_live(pans: list[str]) -> dict[str, Any]:
    """POST /service-providers/payment-cards with FLE-encrypted PAN list.

    In simulator mode the body is sent unencrypted (the simulator does not
    enforce encryption). In live mode the PANs are encrypted using Mastercard
    Field Level Encryption before OAuth signing.
    """
    from simulator.switcher import is_simulated
    if is_simulated("carbon_calculator"):
        return _signed_request("POST", "/service-providers/payment-cards",
                               body={"primaryAccountNumbers": pans})

    enc_path = os.environ.get("CARBON_CALCULATOR_ENCRYPTION_KEY_PATH", "")
    if not enc_path:
        return {"success": False, "error": _ENC_KEY_MISSING}

    if not os.path.isabs(enc_path):
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        enc_path = os.path.join(project_root, enc_path)

    try:
        from client_encryption.field_level_encryption import encrypt_payload
        from client_encryption.field_level_encryption_config import FieldLevelEncryptionConfig
    except ImportError:
        return {"success": False, "error": "client_encryption library not installed."}

    try:
        cfg = dict(_FLE_CONFIG_DICT, encryptionCertificate=enc_path)
        fle_config = FieldLevelEncryptionConfig(cfg)
        body = encrypt_payload({"primaryAccountNumbers": pans}, fle_config)
    except Exception as e:
        return {"success": False, "error": f"Field-level encryption failed: {e}"}

    return _signed_request("POST", "/service-providers/payment-cards", body=body)


# ---------------------------------------------------------------------------
# Signed request helper
# ---------------------------------------------------------------------------

def _signed_request(
    method: str,
    path: str,
    *,
    body: dict[str, Any] | None = None,
    query: dict[str, Any] | None = None,
) -> dict[str, Any]:
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
        headers: dict[str, str] = {
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
    state_updates: dict[str, Any] = {}
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
