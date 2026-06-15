"""Mastercard Business Payment Controls (BPC) API.

OAuth 1.0a one-legged, body-signed. Optional payload encryption (JWE) is
*not* enabled by default — only required if the project has uploaded a
Client Encryption key in the Mastercard Developers credentials panel.

Sandbox base URL pattern follows the standard Mastercard convention:
    https://sandbox.api.mastercard.com/business-payment-controls

Docs:           https://developer.mastercard.com/business-payment-controls/documentation/
API reference:  https://developer.mastercard.com/business-payment-controls/documentation/api-reference/
Reference app:  https://developer.mastercard.com/business-payment-controls/documentation/reference-app/

GATING (see catalog.DISABLED_API_IDS):
    Sandbox project creation requires a *registration token* issued by a
    Mastercard Commercial Products implementation manager, plus an existing
    Mastercard Commercial Identity (ICCP or In Control API customer). The
    portal wizard cannot be replayed headlessly; vima exposes BPC in the
    catalog for discovery but defers actual provisioning to the partner.
"""
from __future__ import annotations

import os
from typing import Any

_PROD_BASE    = "https://api.mastercard.com/business-payment-controls"
_SANDBOX_BASE = "https://sandbox.api.mastercard.com/business-payment-controls"


def _base() -> str:
    from simulator.switcher import sim_base_url
    env = os.environ.get("BUSINESS_PAYMENT_CONTROLS_ENV", "sandbox").lower()
    real = _PROD_BASE if env == "production" else _SANDBOX_BASE
    return sim_base_url("business_payment_controls", real)


def _configured() -> bool:
    key  = os.environ.get("BUSINESS_PAYMENT_CONTROLS_CONSUMER_KEY", "")
    path = os.environ.get("BUSINESS_PAYMENT_CONTROLS_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated("business_payment_controls")


def get_state() -> dict[str, Any]:
    return {"configured": _configured()}


_HOW_TO = (
    "<p><strong>Business Payment Controls (BPC)</strong> lets issuers and "
    "corporate customers register real cards (RCNs), generate virtual cards "
    "(VCNs), apply spend controls to both, attach custom data fields for "
    "reconciliation, and pull authorization / clearing reports — all backed "
    "by Mastercard's Commercial Products platform.</p>"
    "<h3>Manual onboarding required</h3>"
    "<p><em>BPC is gated behind Mastercard Commercial Products.</em> Before "
    "a sandbox project can be created, you must:</p>"
    "<ol>"
    "<li>Engage your Mastercard Commercial Products representative "
    "(or call <strong>+1-800-288-3381 (US)</strong> / "
    "<strong>+1-636-722-6636 (intl)</strong>, Option 4 — or email "
    "<a href=\"mailto:commercial.support@mastercard.com\">"
    "commercial.support@mastercard.com</a>).</li>"
    "<li>If you are already an <em>In Control for Commercial Payments</em> "
    "(ICCP) or <em>In Control API</em> customer, no additional contracts "
    "are needed.</li>"
    "<li>Otherwise the implementation manager sets you up in the Commercial "
    "Products registration service and gives you a <strong>registration "
    "token</strong>.</li>"
    "<li>Create a project on Mastercard Developers and paste the "
    "registration token when adding the Business Payment Controls API.</li>"
    "</ol>"
    "<h3>How it works (four microservices)</h3>"
    "<ul>"
    "<li><strong>Registration</strong> — links your MC Developers identity "
    "with your Commercial Identity for uniform access management.</li>"
    "<li><strong>Card Account</strong> — register RCNs, generate VCNs, apply "
    "spend controls on both.</li>"
    "<li><strong>Custom Data</strong> — attach key/value fields to a card for "
    "downstream reconciliation (sent to GDR on clearing).</li>"
    "<li><strong>Reporting</strong> — authorization, clearing, and clearing "
    "summary reports per RCN/VCN.</li>"
    "</ul>"
    "<h3>Operation groups (from the API reference)</h3>"
    "<ul>"
    "<li>Entities — <code>GET /entities/user-entity</code>, "
    "<code>GET /entities/{guid}/descendants</code></li>"
    "<li>Real Card — register / search / get / update / delete "
    "<code>/real-card-accounts</code></li>"
    "<li>Contact — manage contacts under a real card</li>"
    "<li>Funding Source — register / update / delete / search "
    "<code>/funding-sources</code> and their controls</li>"
    "<li>Virtual Card — register / update / delete VCNs and end-user "
    "contact details</li>"
    "<li>Custom Data Fields — CRUD <code>/custom-data</code></li>"
    "<li>Authorization / Clearing / Clearing Summary Reports</li>"
    "<li>Retail Api Migration — migrate RCNs/VCNs from Retail API</li>"
    "</ul>"
    "<h3>Authentication</h3>"
    "<p>OAuth 1.0a one-legged, body-signed (standard Mastercard pattern). "
    "Payload encryption (JWE) is <strong>optional</strong> — only required "
    "if your project has uploaded a Client Encryption key. See "
    "<a href=\"https://developer.mastercard.com/business-payment-controls/documentation/support/#payload-encryption\">Payload "
    "Encryption FAQ</a>.</p>"
    "<h3>Idempotency</h3>"
    "<p>All endpoints support idempotency. Pass a v4 UUID in the "
    "<code>Idempotency-Key</code> request header; duplicate requests within "
    "30 seconds return the same response.</p>"
    "<h3>Test data &amp; references</h3>"
    "<ul>"
    "<li><a href=\"https://developer.mastercard.com/business-payment-controls/documentation/\">"
    "Product overview &amp; onboarding</a></li>"
    "<li><a href=\"https://developer.mastercard.com/business-payment-controls/documentation/api-reference/\">"
    "API reference (OpenAPI 3.0.3)</a></li>"
    "<li><a href=\"https://developer.mastercard.com/business-payment-controls/documentation/tutorial/tutorial-1/\">"
    "Tutorial — create &amp; configure a sandbox project</a></li>"
    "<li><a href=\"https://developer.mastercard.com/business-payment-controls/documentation/reference-app/\">"
    "Reference application (Java sample code)</a></li>"
    "<li><a href=\"https://developer.mastercard.com/business-payment-controls/documentation/use-cases/\">"
    "Use cases</a> &middot; "
    "<a href=\"https://developer.mastercard.com/business-payment-controls/documentation/tutorial-guides/\">"
    "Tutorials &amp; guides</a></li>"
    "<li><a href=\"https://developer.mastercard.com/api-status?environment=production&service=Business%20Payment%20Controls\">"
    "API status (production)</a></li>"
    "</ul>"
    "<p><em>Once a registration token is issued and the project is created, "
    "expected sandbox values (ownerGUID / entityGUID, funding source GUID, "
    "RCN/VCN GUIDs) are minted per-tenant; there are no shared sandbox PANs "
    "the way some other Mastercard APIs publish.</em></p>"
)


MANIFEST: dict[str, Any] = {
    "id": "business_payment_controls",
    "name": "Business Payment Controls",
    "description": (
        "Mastercard Business Payment Controls — register real cards (RCNs), "
        "generate virtual cards (VCNs), apply spend controls, attach custom "
        "data fields, and pull authorization / clearing reports for "
        "commercial-card spend reconciliation."
    ),
    "docs_url": "https://developer.mastercard.com/business-payment-controls/documentation/",
    "how_to": _HOW_TO,
    "categories": [
        "Real Cards", "Virtual Cards", "Funding Sources", "Controls",
        "Custom Data", "Authorization Reports", "Clearing Reports",
    ],
    "state_schema": [],
    "configured": bool(
        os.environ.get("BUSINESS_PAYMENT_CONTROLS_CONSUMER_KEY")
        and os.environ.get("BUSINESS_PAYMENT_CONTROLS_CONSUMER_KEY") != "your-consumer-key-here"
        and os.environ.get("BUSINESS_PAYMENT_CONTROLS_SIGNING_KEY_PATH")
    ),
    "operations": [
        {
            "id": "get_user_entity",
            "name": "Get user entity (ownerGUID)",
            "category": "Entities",
            "method": "GET",
            "description": (
                "Return the API user's entity identifier (entityGUID / ownerGUID) — "
                "the root identifier used as the parent for real-card registrations."
            ),
            "params": [],
        },
        {
            "id": "register_real_card",
            "name": "Register a real card (RCN)",
            "category": "Real Card",
            "method": "POST",
            "description": (
                "Register a real card (RCN) under an entity. Only an Issuer or "
                "the Issuer's corporate customer can register an RCN."
            ),
            "params": [
                {"name": "owner_guid",        "label": "Owner GUID (entity)", "type": "text", "required": True},
                {"name": "card_number",       "label": "Real card PAN",       "type": "text", "required": True},
                {"name": "expiration_month",  "label": "Expiry month (MM)",   "type": "text", "required": True, "default": "12"},
                {"name": "expiration_year",   "label": "Expiry year (YYYY)",  "type": "text", "required": True, "default": "2030"},
            ],
        },
        {
            "id": "register_virtual_card",
            "name": "Generate a virtual card (VCN)",
            "category": "Virtual Card",
            "method": "POST",
            "description": (
                "Generate a VCN linked to a funding source, with spend controls "
                "applied at creation time."
            ),
            "params": [
                {"name": "funding_source_guid", "label": "Funding source GUID", "type": "text", "required": True},
                {"name": "validity_months",     "label": "Validity (months)",   "type": "text", "required": True, "default": "12"},
                {"name": "spend_limit",         "label": "Spend limit (cents)", "type": "text", "required": True, "default": "100000"},
            ],
        },
        {
            "id": "search_authorization_reports",
            "name": "Create authorization report",
            "category": "Authorization Report",
            "method": "POST",
            "description": (
                "Create an authorization report listing authorizations recorded "
                "against an RCN/VCN over a date range."
            ),
            "params": [
                {"name": "from_date", "label": "From (YYYY-MM-DD)", "type": "text", "required": True},
                {"name": "to_date",   "label": "To (YYYY-MM-DD)",   "type": "text", "required": True},
            ],
        },
    ],
}


def execute(op_id: str, params: dict[str, Any]) -> dict[str, Any]:
    """Dispatch to a per-operation handler. All handlers return the standard
    envelope ({success, data, error, request, response, state_updates}) so the
    UI can render request/response panels without backfill."""
    from simulator.switcher import is_simulated
    if is_simulated("business_payment_controls"):
        return {
            "success": True,
            "simulated": True,
            "note": (
                "Simulator path — live BPC calls require a registration token "
                "from your Mastercard Commercial Products implementation manager."
            ),
            "op_id": op_id,
            "data": {"op_id": op_id, "params": params},
            "request": {
                "method": "(simulated)",
                "url": f"sim://business_payment_controls/{op_id}",
                "body": params,
            },
            "response": {
                "status_code": 200,
                "body": {"simulated": True, "op_id": op_id, "params": params},
            },
            "state_updates": {},
        }
    if not _configured():
        return {
            "success": False,
            "error": "not_configured",
            "message": (
                "Business Payment Controls is not configured. Set "
                "BUSINESS_PAYMENT_CONTROLS_CONSUMER_KEY and "
                "BUSINESS_PAYMENT_CONTROLS_SIGNING_KEY_PATH in .env, then "
                "restart the server. Provisioning requires a registration "
                "token from your Mastercard Commercial Products implementation "
                "manager — see the 'How To Use' panel for details."
            ),
            "manual_onboarding_url": "https://developer.mastercard.com/business-payment-controls/documentation/",
        }
    if op_id == "get_user_entity":
        return _call("GET", "/entities/user-entity", None)
    if op_id == "register_real_card":
        body = {
            "ownerGuid": params.get("owner_guid"),
            "cardNumber": params.get("card_number"),
            "expirationMonth": params.get("expiration_month"),
            "expirationYear": params.get("expiration_year"),
        }
        return _call("POST", "/real-card-accounts", body)
    if op_id == "register_virtual_card":
        body = {
            "fundingSourceGuid": params.get("funding_source_guid"),
            "validityMonths": params.get("validity_months"),
            "spendLimit": params.get("spend_limit"),
        }
        return _call("POST", "/virtual-card-accounts", body)
    if op_id == "search_authorization_reports":
        body = {
            "fromDate": params.get("from_date"),
            "toDate": params.get("to_date"),
        }
        return _call("POST", "/authorization-reports", body)
    return {"success": False, "error": f"Unknown operation: {op_id}"}


def _call(method: str, path: str, body: Any) -> dict[str, Any]:
    """Issue an OAuth1.0a body-signed request against the BPC base URL."""
    import json

    import requests

    url = f"{_base()}{path}"
    body_str = json.dumps(body) if body is not None else ""
    headers = {"Accept": "application/json"}
    if body is not None:
        headers["Content-Type"] = "application/json"

    consumer_key = os.environ["BUSINESS_PAYMENT_CONTROLS_CONSUMER_KEY"]
    key_path = os.environ["BUSINESS_PAYMENT_CONTROLS_SIGNING_KEY_PATH"]
    key_password = os.environ.get("BUSINESS_PAYMENT_CONTROLS_SIGNING_KEY_PASSWORD", "keystorepassword")
    if not os.path.isabs(key_path):
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        key_path = os.path.join(project_root, key_path)

    try:
        import oauth1.authenticationutils as authutils
        from oauth1.oauth import OAuth
        signing_key = authutils.load_signing_key(key_path, key_password)
        headers["Authorization"] = OAuth.get_authorization_header(
            url, method, body_str, consumer_key, signing_key
        )
    except Exception as e:
        return {
            "success": False,
            "error": f"OAuth signing failed: {e}",
            "request": {"method": method, "url": url, "body": body},
            "response": {"status_code": None, "body": None},
        }

    try:
        if method == "GET":
            resp = requests.get(url, headers=headers, timeout=15)
        else:
            resp = requests.request(method, url, data=body_str, headers=headers, timeout=15)
        status_code = resp.status_code
        try:
            resp_body = resp.json()
        except Exception:
            resp_body = {"raw": resp.text}
    except Exception as e:
        return {
            "success": False,
            "error": f"Request failed: {e}",
            "request": {"method": method, "url": url, "body": body},
            "response": {"status_code": None, "body": None},
        }

    success = 200 <= status_code < 300
    return {
        "success": success,
        "data": resp_body if success else {},
        "error": None if success else (resp_body.get("Errors") if isinstance(resp_body, dict) else resp_body),
        "request": {"method": method, "url": url, "body": body},
        "response": {"status_code": status_code, "body": resp_body},
        "state_updates": {},
    }

