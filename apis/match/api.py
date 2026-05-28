"""MATCH Pro API — OAuth 1.0a.

Docs:
  https://developer.mastercard.com/match/documentation/
  https://developer.mastercard.com/match/documentation/api-reference/

Canonical bases (MATCH Pro swagger + docs):
  Sandbox:    https://sandbox.apiedge.mastercard.com/mcp/match/api
  Production: https://apiedge.mastercard.com/mcp/match/api
"""
from __future__ import annotations

import json
import os
from typing import Any, Dict
from urllib.parse import urlencode

_SANDBOX_BASE_URL = "https://sandbox.apiedge.mastercard.com/mcp/match/api"
_PROD_BASE_URL = "https://apiedge.mastercard.com/mcp/match/api"


MANIFEST: Dict[str, Any] = {
    "id": "match",
    "name": "MATCH Pro",
    "description": (
        "Mastercard MATCH Pro (Member Alert To Control High-risk Merchants) helps acquirers "
        "inquire about terminated merchants and retrieve jurisdiction reference data."
    ),
    "docs_url": "https://developer.mastercard.com/match/documentation/",
    "how_to": (
        "<p><strong>MATCH Pro</strong> supports acquirer risk controls by exposing terminated "
        "merchant inquiry workflows and country/state/city reference data.</p>"
        "<h3>Before you send</h3>"
        "<ol>"
        "<li>Provision OAuth 1.0a credentials for MATCH Pro in Mastercard Developers.</li>"
        "<li>Ensure <code>MATCH_CONSUMER_KEY</code> and <code>MATCH_SIGNING_KEY_PATH</code> are set.</li>"
        "<li>Use the documented MATCH Pro base path <code>/mcp/match/api</code> (not legacy host paths).</li>"
        "</ol>"
        "<h3>Sandbox guidance</h3>"
        "<ul>"
        "<li>Use your assigned sandbox acquirer ICA as <code>acquirer_id</code> (default 1996 is a common sample).</li>"
        "<li>Start with <strong>Countries</strong> to verify auth/base URL, then run inquiry operations.</li>"
        "</ul>"
    ),
    "categories": ["Inquiry", "Reference"],
    "state_schema": [],
    "configured": bool(
        os.environ.get("MATCH_CONSUMER_KEY")
        and os.environ.get("MATCH_CONSUMER_KEY") != "your-consumer-key-here"
        and os.environ.get("MATCH_SIGNING_KEY_PATH")
    ),
    "operations": [
        {
            "id": "create_termination_inquiry",
            "name": "Create termination inquiry",
            "category": "Inquiry",
            "method": "POST",
            "description": "Submit a merchant/principal inquiry and receive possible MATCH results.",
            "params": [
                {
                    "name": "acquirer_id",
                    "label": "Acquirer ICA",
                    "type": "text",
                    "default": "1996",
                    "required": True,
                    "help": "Member ICA number (numeric string).",
                },
                {"name": "merchant_name", "label": "Merchant legal name", "type": "text", "default": "TEST MERCHANT LLC", "required": True},
                {"name": "merchant_id", "label": "Merchant ID", "type": "text", "default": "M123456789", "required": False},
                {"name": "address_line_one", "label": "Merchant address line 1", "type": "text", "default": "123 MAIN ST", "required": True},
                {"name": "city", "label": "Merchant city", "type": "text", "default": "SAINT LOUIS", "required": True},
                {"name": "state", "label": "Merchant state/subdivision", "type": "text", "default": "MO", "required": False},
                {"name": "country", "label": "Merchant country (alpha-3)", "type": "text", "default": "USA", "required": True},
                {"name": "postal_code", "label": "Postal code", "type": "text", "default": "63101", "required": True},
                {"name": "phone_number", "label": "Merchant phone", "type": "text", "default": "3145551234", "required": True},
                {"name": "merchant_category", "label": "Merchant category code", "type": "text", "default": "5999", "required": True},
                {"name": "principal_first_name", "label": "Principal first name", "type": "text", "default": "JANE", "required": True},
                {"name": "principal_last_name", "label": "Principal last name", "type": "text", "default": "DOE", "required": True},
                {"name": "principal_address_line_one", "label": "Principal address line 1", "type": "text", "default": "123 MAIN ST", "required": True},
                {"name": "principal_city", "label": "Principal city", "type": "text", "default": "SAINT LOUIS", "required": True},
                {"name": "principal_state", "label": "Principal state/subdivision", "type": "text", "default": "MO", "required": False},
                {"name": "principal_postal_code", "label": "Principal postal code", "type": "text", "default": "63101", "required": False},
                {"name": "principal_country", "label": "Principal country (alpha-3)", "type": "text", "default": "USA", "required": True},
                {"name": "principal_phone_number", "label": "Principal phone", "type": "text", "default": "3145551234", "required": True},
                {"name": "principal_email", "label": "Principal email", "type": "text", "default": "jane.doe@example.com", "required": True},
                {
                    "name": "page_length",
                    "label": "Page length",
                    "type": "select",
                    "default": "10",
                    "required": False,
                    "options": [
                        {"value": "10", "label": "10"},
                        {"value": "25", "label": "25"},
                        {"value": "50", "label": "50"},
                    ],
                },
                {
                    "name": "page_offset",
                    "label": "Page offset",
                    "type": "text",
                    "default": "0",
                    "required": False,
                },
            ],
        },
        {
            "id": "get_inquiry_history",
            "name": "Get inquiry by reference",
            "category": "Inquiry",
            "method": "GET",
            "description": "Retrieve a historical termination inquiry by inquiry reference number.",
            "params": [
                {"name": "inquiry_ref_num", "label": "Inquiry reference number", "type": "text", "default": "IRN000001", "required": True},
                {
                    "name": "page_length",
                    "label": "Page length",
                    "type": "select",
                    "default": "10",
                    "required": False,
                    "options": [
                        {"value": "10", "label": "10"},
                        {"value": "25", "label": "25"},
                        {"value": "50", "label": "50"},
                    ],
                },
                {"name": "page_offset", "label": "Page offset", "type": "text", "default": "0", "required": False},
            ],
        },
        {
            "id": "get_contact_details",
            "name": "Get acquirer contact details",
            "category": "Inquiry",
            "method": "POST",
            "description": "Retrieve contact information for an acquirer ICA.",
            "params": [
                {"name": "acquirer_id", "label": "Acquirer ICA", "type": "text", "default": "1996", "required": True}
            ],
        },
        {
            "id": "get_countries",
            "name": "List countries",
            "category": "Reference",
            "method": "GET",
            "description": "Retrieve countries supported by MATCH Pro.",
            "params": [],
        },
        {
            "id": "get_states",
            "name": "List states",
            "category": "Reference",
            "method": "GET",
            "description": "Retrieve states for a country code.",
            "params": [
                {"name": "country_code", "label": "Country code (alpha-3)", "type": "text", "default": "USA", "required": True}
            ],
        },
        {
            "id": "get_cities",
            "name": "List cities",
            "category": "Reference",
            "method": "GET",
            "description": "Retrieve cities for a country code and optional state code.",
            "params": [
                {"name": "country_code", "label": "Country code (alpha-3)", "type": "text", "default": "USA", "required": True},
                {"name": "state_code", "label": "State code", "type": "text", "default": "MO", "required": False},
            ],
        },
    ],
}


def _base_url() -> str:
    from simulator.switcher import sim_base_url

    env = os.environ.get("MATCH_ENV", "sandbox").lower()
    real = _PROD_BASE_URL if env == "production" else _SANDBOX_BASE_URL
    return sim_base_url("match", real)


def _configured() -> bool:
    key = os.environ.get("MATCH_CONSUMER_KEY", "")
    path = os.environ.get("MATCH_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated

    return _configured() or is_simulated("match")


def get_state() -> Dict[str, Any]:
    return {"configured": _configured()}


def _oauth_header(url: str, method: str, body_str: str = "") -> str:
    import oauth1.authenticationutils as authutils
    from oauth1.oauth import OAuth

    consumer_key = os.environ["MATCH_CONSUMER_KEY"]
    key_path = os.environ["MATCH_SIGNING_KEY_PATH"]
    key_password = os.environ.get("MATCH_SIGNING_KEY_PASSWORD", "keystorepassword")

    if not os.path.isabs(key_path):
        key_path = os.path.abspath(key_path)

    signing_key = authutils.load_signing_key(key_path, key_password)
    return OAuth.get_authorization_header(
        url,
        method,
        body_str,
        consumer_key,
        signing_key,
    )


def _request(method: str, path: str, query: Dict[str, Any] | None = None, body: Dict[str, Any] | None = None) -> Dict[str, Any]:
    import requests
    from simulator.switcher import is_simulated

    url = f"{_base_url()}{path}"
    if query:
        clean = {k: v for k, v in query.items() if v not in (None, "")}
        if clean:
            url = f"{url}?{urlencode(clean)}"

    body_str = json.dumps(body) if body is not None else ""

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    if not is_simulated("match"):
        try:
            auth_header = _oauth_header(url, method, body_str)
        except Exception as e:
            return {"success": False, "error": f"Signing error: {e}"}
        headers["Authorization"] = auth_header

    try:
        resp = requests.request(
            method,
            url,
            headers=headers,
            data=body_str if body is not None else None,
            timeout=45,
        )
    except Exception as e:
        return {"success": False, "error": f"Request failed: {e}"}

    try:
        payload = resp.json()
    except ValueError:
        payload = {"raw": resp.text}

    return {
        "success": resp.ok,
        "status": resp.status_code,
        "data": payload,
    }


def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if not is_configured():
        return {
            "success": False,
            "error": (
                "MATCH not configured. Set MATCH_CONSUMER_KEY and MATCH_SIGNING_KEY_PATH "
                "(and MATCH_SIGNING_KEY_PASSWORD if needed)."
            ),
        }

    if op_id == "get_countries":
        return _request("GET", "/countries")

    if op_id == "get_states":
        country_code = str(params.get("country_code") or "").strip().upper()
        if not country_code:
            return {"success": False, "error": "country_code is required"}
        return _request("GET", f"/countries/{country_code}/states")

    if op_id == "get_cities":
        country_code = str(params.get("country_code") or "").strip().upper()
        if not country_code:
            return {"success": False, "error": "country_code is required"}
        state_code = str(params.get("state_code") or "").strip().upper()
        query = {"state_code": state_code} if state_code else None
        return _request("GET", f"/countries/{country_code}/cities", query=query)

    if op_id == "get_contact_details":
        acquirer_id = str(params.get("acquirer_id") or "").strip()
        if not acquirer_id:
            return {"success": False, "error": "acquirer_id is required"}
        body = {"contactRequest": {"acquirerId": acquirer_id}}
        return _request("POST", "/contact-details", body=body)

    if op_id == "get_inquiry_history":
        inquiry_ref_num = str(params.get("inquiry_ref_num") or "").strip()
        if not inquiry_ref_num:
            return {"success": False, "error": "inquiry_ref_num is required"}
        query = {
            "page_length": params.get("page_length"),
            "page_offset": params.get("page_offset"),
        }
        return _request("GET", f"/termination-inquiries/{inquiry_ref_num}", query=query)

    if op_id == "create_termination_inquiry":
        required = [
            "acquirer_id",
            "merchant_name",
            "address_line_one",
            "city",
            "country",
            "postal_code",
            "phone_number",
            "merchant_category",
            "principal_first_name",
            "principal_last_name",
            "principal_address_line_one",
            "principal_city",
            "principal_country",
            "principal_phone_number",
            "principal_email",
        ]
        missing = [k for k in required if not str(params.get(k, "")).strip()]
        if missing:
            return {"success": False, "error": f"Missing required params: {', '.join(missing)}"}

        body = {
            "terminationInquiryRequest": {
                "acquirerId": str(params["acquirer_id"]).strip(),
                "merchant": {
                    "name": str(params["merchant_name"]).strip(),
                    "merchantId": str(params.get("merchant_id") or "").strip() or None,
                    "address": {
                        "addressLineOne": str(params["address_line_one"]).strip(),
                        "city": str(params["city"]).strip(),
                        **({("countrySubdivision"): str(params["state"]).strip()} if params.get("state") else {}),
                        "country": str(params["country"]).strip().upper(),
                        "postalCode": str(params["postal_code"]).strip(),
                    },
                    "phoneNumber": str(params["phone_number"]).strip(),
                    "merchantCategory": str(params["merchant_category"]).strip(),
                    "principals": [
                        {
                            "firstName": str(params["principal_first_name"]).strip(),
                            "lastName": str(params["principal_last_name"]).strip(),
                            "address": {
                                "addressLineOne": str(params["principal_address_line_one"]).strip(),
                                "city": str(params["principal_city"]).strip(),
                                **({"countrySubdivision": str(params["principal_state"]).strip()} if params.get("principal_state") else {}),
                                **({"postalCode": str(params["principal_postal_code"]).strip()} if params.get("principal_postal_code") else {}),
                                "country": str(params["principal_country"]).strip().upper(),
                            },
                            "phoneNumber": str(params["principal_phone_number"]).strip(),
                            "email": str(params["principal_email"]).strip(),
                        }
                    ],
                },
            }
        }

        # Remove optional None values to keep the request body clean.
        if body["terminationInquiryRequest"]["merchant"].get("merchantId") is None:
            body["terminationInquiryRequest"]["merchant"].pop("merchantId")

        query = {
            "page_length": params.get("page_length"),
            "page_offset": params.get("page_offset"),
        }
        return _request("POST", "/termination-inquiries", query=query, body=body)

    return {"success": False, "error": f"Unknown operation: {op_id}"}
