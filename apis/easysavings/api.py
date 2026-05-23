"""Mastercard Easy Savings Specials Merchant Offers API — OAuth 1.0a.

Endpoints:
  GET  /easysavings/specials/countries
  GET  /easysavings/specials/offers?bin=&country=&language=&offset=&limit=
  POST /easysavings/specials/redemptions          (body: {"bin","offers":[{"id"}]} )
  GET  /easysavings/specials/redemptions/{order_id}

Auth: OAuth 1.0a (same Mastercard signing library used by BIN Lookup,
Consumer Clarity, Priceless).

Docs:
  https://developer.mastercard.com/easy-savings-specials/documentation/
  https://developer.mastercard.com/easy-savings-specials/documentation/api-reference/
"""
from __future__ import annotations

import os
from typing import Any, Dict

# Sandbox provides predefined responses for specific values.  These match the
# documented test cases so the Explorer "just works" out of the box.
_SANDBOX_BASE_URL = "https://sandbox.sme.api.mastercard.com/easysavings/specials"
_PROD_BASE_URL    = "https://sme.api.mastercard.com/easysavings/specials"

# Sample sandbox offer that always succeeds (per the docs).
_SAMPLE_OFFER_ID = "QDWC0NRZmyabde"

MANIFEST: Dict[str, Any] = {
    "id": "easysavings",
    "name": "Easy Savings",
    "description": (
        "Mastercard Easy Savings Specials — a global, no-cost merchant offers "
        "platform that lets issuers embed localised SME card-linked savings "
        "directly into their apps and channels."
    ),
    "docs_url": "https://developer.mastercard.com/easy-savings-specials/documentation/",
    "how_to": (
        "<p><strong>Easy Savings Specials</strong> exposes Mastercard's global "
        "merchant-offers catalogue for SME business cardholders. Issuers can list "
        "available offers for an enrolled BIN, then unlock voucher / promotion "
        "codes that the cardholder redeems at the merchant.</p>"
        "<h3>How to use</h3>"
        "<ol>"
        "<li>Use <strong>Lookups → List supported countries</strong> to see which "
        "countries and languages are available.</li>"
        "<li>Use <strong>Offers → List offers for a BIN</strong> with a valid "
        "8-digit Mastercard SME BIN, an ISO-3 country code (e.g. <code>IND</code>) "
        "and an IETF language tag (e.g. <code>en-US</code>).</li>"
        "<li>Pick an <code>offerId</code> from the response, then use "
        "<strong>Redemptions → Redeem an offer</strong> to unlock a voucher code.</li>"
        "<li>Use <strong>Redemptions → Get redemption by order ID</strong> to "
        "look up an existing order.</li>"
        "</ol>"
        "<h3>Sandbox tips</h3>"
        "<ul>"
        "<li>BIN <code>52345678</code> with country <code>IND</code> and language "
        "<code>en-US</code> returns a populated catalogue.</li>"
        "<li>Offer ID <code>" + _SAMPLE_OFFER_ID + "</code> is the canonical sample offer "
        "that always redeems successfully.</li>"
        "</ul>"
    ),
    "categories": ["Lookups", "Offers", "Redemptions"],
    "state_schema": [],
    "configured": bool(
        os.environ.get("EASYSAVINGS_CONSUMER_KEY")
        and os.environ.get("EASYSAVINGS_CONSUMER_KEY") != "your-consumer-key-here"
        and os.environ.get("EASYSAVINGS_SIGNING_KEY_PATH")
    ),
    "operations": [
        {
            "id": "list_countries",
            "name": "List supported countries",
            "category": "Lookups",
            "method": "GET",
            "description": "Retrieve every country (and its supported languages) in the Easy Savings catalogue.",
            "params": [],
        },
        {
            "id": "list_offers",
            "name": "List offers for a BIN",
            "category": "Offers",
            "method": "GET",
            "description": "Return the relevant SME offers for an enrolled 8-digit BIN, country and language.",
            "params": [
                {
                    "name": "bin",
                    "label": "BIN (8 digits)",
                    "type": "text",
                    "default": "52345678",
                    "required": True,
                },
                {
                    "name": "country",
                    "label": "Country (ISO-3)",
                    "type": "text",
                    "default": "IND",
                    "required": True,
                },
                {
                    "name": "language",
                    "label": "Language (IETF BCP-47)",
                    "type": "text",
                    "default": "en-US",
                    "required": True,
                },
                {
                    "name": "offset",
                    "label": "Offset",
                    "type": "text",
                    "default": "0",
                    "required": False,
                },
                {
                    "name": "limit",
                    "label": "Limit",
                    "type": "text",
                    "default": "30",
                    "required": False,
                },
            ],
        },
        {
            "id": "redeem_offer",
            "name": "Redeem an offer",
            "category": "Redemptions",
            "method": "POST",
            "description": "Unlock a voucher / promotion code for the supplied BIN + offer ID.",
            "params": [
                {
                    "name": "bin",
                    "label": "BIN (8 digits)",
                    "type": "text",
                    "default": "52345678",
                    "required": True,
                },
                {
                    "name": "offer_id",
                    "label": "Offer ID",
                    "type": "text",
                    "default": _SAMPLE_OFFER_ID,
                    "required": True,
                },
            ],
        },
        {
            "id": "get_redemption",
            "name": "Get redemption by order ID",
            "category": "Redemptions",
            "method": "GET",
            "description": "Retrieve the voucher details associated with a previously generated order ID.",
            "params": [
                {
                    "name": "order_id",
                    "label": "Order ID",
                    "type": "text",
                    "default": _SAMPLE_OFFER_ID,
                    "required": True,
                },
            ],
        },
    ],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _base_url() -> str:
    from simulator.switcher import sim_base_url
    env = os.environ.get("EASYSAVINGS_ENV", "sandbox").lower()
    real = _PROD_BASE_URL if env == "production" else _SANDBOX_BASE_URL
    return sim_base_url("easysavings", real)


def _configured() -> bool:
    key = os.environ.get("EASYSAVINGS_CONSUMER_KEY", "")
    path = os.environ.get("EASYSAVINGS_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated("easysavings")


def get_state() -> Dict[str, Any]:
    return {"configured": _configured()}


def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if op_id == "list_countries":
        return _list_countries()
    if op_id == "list_offers":
        return _list_offers(params)
    if op_id == "redeem_offer":
        return _redeem_offer(params)
    if op_id == "get_redemption":
        return _get_redemption(params)
    return {"success": False, "error": f"Unknown operation: {op_id}"}


def _not_configured_err() -> Dict[str, Any]:
    return {
        "success": False,
        "error": (
            "Easy Savings is not configured. Set EASYSAVINGS_CONSUMER_KEY and "
            "EASYSAVINGS_SIGNING_KEY_PATH in .env, then restart the server."
        ),
    }


def _resolve_key_path(path: str) -> str:
    if os.path.isabs(path):
        return path
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(project_root, path)


def _signed_request(method: str, url: str, body_str: str | None) -> Dict[str, Any]:
    """Build OAuth-signed headers + execute the HTTP call.

    Returns a uniform response envelope: success / data / error / request /
    response — matching the convention used by the other Mastercard APIs.
    """
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("easysavings"):
        return _not_configured_err()

    import requests

    headers = {
        "Accept": "application/json",
    }
    if body_str is not None:
        headers["Content-Type"] = "application/json"

    if is_simulated("easysavings"):
        headers["Authorization"] = "Simulated"
    else:
        import oauth1.authenticationutils as authutils
        from oauth1.oauth import OAuth

        consumer_key = os.environ["EASYSAVINGS_CONSUMER_KEY"]
        key_path     = _resolve_key_path(os.environ["EASYSAVINGS_SIGNING_KEY_PATH"])
        key_password = os.environ.get("EASYSAVINGS_SIGNING_KEY_PASSWORD", "keystorepassword")

        try:
            signing_key = authutils.load_signing_key(key_path, key_password)
            auth_header = OAuth.get_authorization_header(
                url, method, body_str or "", consumer_key, signing_key
            )
            headers["Authorization"] = auth_header
        except Exception as exc:
            return {"success": False, "error": f"OAuth signing failed: {exc}"}

    try:
        resp = requests.request(
            method=method,
            url=url,
            data=body_str,
            headers=headers,
            timeout=15,
        )
        status_code = resp.status_code
        try:
            resp_body = resp.json()
        except Exception:
            resp_body = {"raw": resp.text}
    except Exception as exc:
        return {"success": False, "error": f"Request failed: {exc}"}

    success = 200 <= status_code < 300
    return {
        "success": success,
        "data": resp_body if success else {},
        "error": None if success else (resp_body.get("Errors") if isinstance(resp_body, dict) else resp_body),
        "request": {
            "method": method,
            "url": url,
            "body": body_str,
        },
        "response": {
            "status_code": status_code,
            "body": resp_body,
        },
        "state_updates": {},
    }


# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------
def _list_countries() -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("easysavings"):
        return _not_configured_err()
    return _signed_request("GET", f"{_base_url()}/countries", None)


def _list_offers(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("easysavings"):
        return _not_configured_err()
    from urllib.parse import urlencode

    bin_val   = (params.get("bin") or "").strip()
    country   = (params.get("country") or "").strip()
    language  = (params.get("language") or "").strip()
    offset    = (params.get("offset") or "0").strip()
    limit     = (params.get("limit") or "30").strip()

    missing = [k for k, v in (("bin", bin_val), ("country", country), ("language", language)) if not v]
    if missing:
        return {"success": False, "error": f"Missing required parameter(s): {', '.join(missing)}"}

    qs = urlencode({
        "bin":      bin_val,
        "country":  country,
        "language": language,
        "offset":   offset,
        "limit":    limit,
    })
    url = f"{_base_url()}/offers?{qs}"
    return _signed_request("GET", url, None)


def _redeem_offer(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("easysavings"):
        return _not_configured_err()
    import json

    bin_val  = (params.get("bin") or "").strip()
    offer_id = (params.get("offer_id") or "").strip()
    if not bin_val or not offer_id:
        return {"success": False, "error": "Both 'bin' and 'offer_id' are required."}

    body = {"bin": bin_val, "offers": [{"id": offer_id}]}
    body_str = json.dumps(body)
    return _signed_request("POST", f"{_base_url()}/redemptions", body_str)


def _get_redemption(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("easysavings"):
        return _not_configured_err()

    order_id = (params.get("order_id") or "").strip()
    if not order_id:
        return {"success": False, "error": "'order_id' is required."}

    return _signed_request("GET", f"{_base_url()}/redemptions/{order_id}", None)
