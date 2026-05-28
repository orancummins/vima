"""Mastercard Flight Delay Pass API (loyalty/flight-delay-pass).

OAuth 1.0a one-legged signing. PII-bearing operations (POST /registrations,
PUT /registrations/{id}) require JWE payload encryption per
https://developer.mastercard.com/flight-delay-pass/documentation/api-basics/

Endpoints (sandbox base ``/loyalty/flight-delay-pass``):
    GET    /eligibility-checks         - Check if a flight is eligible
    POST   /registrations              - Create registration  (JWE required)
    GET    /registrations/{id}         - Fetch registration details
    PUT    /registrations/{id}         - Update registration   (JWE required)
    DELETE /registrations/{id}         - Cancel registration

Docs:  https://developer.mastercard.com/flight-delay-pass/documentation/
Spec:  /flight-delay-pass/documentation/api-reference/  (FlightDelayPassSpec.yaml)

Live access also requires the issuer to be on-boarded as a Flight Delay Pass
tenant by the Mastercard implementation team (~26 days). Until that is done
all calls will return 403 even with a valid OAuth signature.
"""
from __future__ import annotations

import json
import os
import uuid
from typing import Any, Dict, List, Optional


_PROD_BASE    = "https://api.mastercard.com/loyalty/flight-delay-pass"
_SANDBOX_BASE = "https://sandbox.api.mastercard.com/loyalty/flight-delay-pass"


def _base() -> str:
    from simulator.switcher import sim_base_url
    real = _PROD_BASE if os.environ.get("FLIGHT_DELAY_PASS_ENV", "sandbox").lower() == "production" else _SANDBOX_BASE
    return sim_base_url("flight_delay_pass", real)


def _configured() -> bool:
    key  = os.environ.get("FLIGHT_DELAY_PASS_CONSUMER_KEY", "")
    path = os.environ.get("FLIGHT_DELAY_PASS_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated("flight_delay_pass")


def get_state() -> Dict[str, Any]:
    return {"configured": _configured()}


_HOW_TO = (
    "<p><strong>Flight Delay Pass</strong> lets issuers register their "
    "cardholders for complimentary airport-lounge access if their qualifying "
    "flight is delayed. Mastercard validates the flight, issues a confirmation, "
    "and on the day of travel sends an email + SMS with a QR code if the flight "
    "is delayed.</p>"
    "<h3>Operations</h3>"
    "<ol>"
    "<li><strong>Eligibility check</strong> — <code>GET /eligibility-checks</code>: "
    "verify a flight is covered before offering registration to the cardholder. "
    "Returns provider details if eligible.</li>"
    "<li><strong>Create registration</strong> — <code>POST /registrations</code>: "
    "register the cardholder (and travel companions) for a specific flight. "
    "<em>PII fields are JWE-encrypted.</em></li>"
    "<li><strong>Get registration</strong> — <code>GET /registrations/{id}</code>: "
    "retrieve registration details by id.</li>"
    "<li><strong>Update registration</strong> — <code>PUT /registrations/{id}</code>: "
    "update personal info on an existing registration. <em>PII fields are JWE-encrypted.</em></li>"
    "<li><strong>Cancel registration</strong> — <code>DELETE /registrations/{id}</code>: "
    "cancel an existing registration prior to travel.</li>"
    "</ol>"
    "<h3>Manual onboarding required</h3>"
    "<p class='muted'>Live sandbox access requires the issuer to be on-boarded as "
    "a Flight Delay Pass tenant by the Mastercard implementation team, and the "
    "project's Client Key to be whitelisted. Until that is done all live calls "
    "will return 403 — use the simulator for local development.</p>"
    "<p><a href='https://developer.mastercard.com/flight-delay-pass/documentation/tutorials-and-guides/' "
    "target='_blank' rel='noopener'><strong>Read the onboarding guide ↗</strong></a> "
    "&nbsp;·&nbsp; "
    "<a href='https://developer.mastercard.com/support' target='_blank' rel='noopener'>"
    "Contact your Mastercard representative ↗</a></p>"
)


_ENC_NOTE = (
    "PII fields on this operation require JWE payload encryption "
    "(RSA-OAEP-256 + A256GCM). The Mastercard client-encryption library is "
    "not wired in for Flight Delay Pass yet — use the simulator for local "
    "development."
)


_ELIGIBILITY_PARAMS: List[Dict[str, Any]] = [
    {"name": "carrierCode",      "label": "Carrier code (IATA)",    "type": "text", "default": "AA",         "required": True,  "help": "2-letter IATA airline code (e.g. AA, BA, LH)."},
    {"name": "flightNumber",     "label": "Flight number",          "type": "text", "default": "100",        "required": True,  "help": "Numeric portion of the flight number."},
    {"name": "departureDate",    "label": "Departure date",         "type": "text", "default": "2026-06-15", "required": True,  "help": "YYYY-MM-DD in the local departure timezone."},
    {"name": "departureAirport", "label": "Departure airport (IATA)", "type": "text", "default": "JFK",      "required": True,  "help": "3-letter IATA airport code."},
    {"name": "arrivalAirport",   "label": "Arrival airport (IATA)", "type": "text", "default": "LHR",        "required": True,  "help": "3-letter IATA airport code."},
    {"name": "clientId",         "label": "Client ID (merchant)",   "type": "text", "default": "",           "required": False, "help": "Merchant client id supplied by your Mastercard implementation team."},
    {"name": "propositionCode",  "label": "Proposition code",       "type": "text", "default": "",           "required": False, "help": "Proposition code configured in the Mastercard system for this benefit."},
]

_GET_PARAMS: List[Dict[str, Any]] = [
    {"name": "registrationId", "label": "Registration ID", "type": "text", "default": "", "required": True, "help": "Returned by Create registration."},
]

_CREATE_PARAMS: List[Dict[str, Any]] = [
    {"name": "carrierCode",      "label": "Carrier code (IATA)",    "type": "text", "default": "AA",         "required": True},
    {"name": "flightNumber",     "label": "Flight number",          "type": "text", "default": "100",        "required": True},
    {"name": "departureDate",    "label": "Departure date",         "type": "text", "default": "2026-06-15", "required": True, "help": "YYYY-MM-DD."},
    {"name": "departureAirport", "label": "Departure airport (IATA)", "type": "text", "default": "JFK",      "required": True},
    {"name": "arrivalAirport",   "label": "Arrival airport (IATA)", "type": "text", "default": "LHR",        "required": True},
    {"name": "firstName",        "label": "Cardholder first name",  "type": "text", "default": "Test",       "required": True},
    {"name": "lastName",         "label": "Cardholder last name",   "type": "text", "default": "Cardholder", "required": True},
    {"name": "email",            "label": "Email",                  "type": "text", "default": "test@example.com", "required": True},
    {"name": "phoneNumber",      "label": "Phone (E.164)",          "type": "text", "default": "+15555550100", "required": True},
    {"name": "clientId",         "label": "Client ID (merchant)",   "type": "text", "default": "", "required": False},
    {"name": "propositionCode",  "label": "Proposition code",       "type": "text", "default": "", "required": False},
]

_UPDATE_PARAMS: List[Dict[str, Any]] = [
    {"name": "registrationId", "label": "Registration ID", "type": "text", "default": "", "required": True},
    {"name": "firstName",      "label": "First name",      "type": "text", "default": "", "required": False},
    {"name": "lastName",       "label": "Last name",       "type": "text", "default": "", "required": False},
    {"name": "email",          "label": "Email",           "type": "text", "default": "", "required": False},
    {"name": "phoneNumber",    "label": "Phone (E.164)",   "type": "text", "default": "", "required": False},
]

_CANCEL_PARAMS: List[Dict[str, Any]] = [
    {"name": "registrationId", "label": "Registration ID", "type": "text", "default": "", "required": True},
]


MANIFEST: Dict[str, Any] = {
    "id": "flight_delay_pass",
    "name": "Flight Delay Pass",
    "description": (
        "Mastercard Flight Delay Pass — register cardholders (and travel "
        "companions) for complimentary airport-lounge access if their "
        "qualifying flight is delayed on the day of travel. OAuth 1.0a with "
        "JWE payload encryption for PII operations."
    ),
    "docs_url": "https://developer.mastercard.com/flight-delay-pass/documentation/",
    "how_to": _HOW_TO,
    "categories": ["Eligibility", "Registrations"],
    "state_schema": [
        {"name": "lastRegistrationId", "label": "Last registration ID", "type": "text", "default": ""},
    ],
    "configured": _configured(),
    "operations": [
        {
            "id": "eligibility_check",
            "name": "Eligibility check",
            "category": "Eligibility",
            "method": "GET",
            "description": "Validate that an upcoming flight is eligible for the Flight Delay Pass benefit.",
            "params": _ELIGIBILITY_PARAMS,
        },
        {
            "id": "create_registration",
            "name": "Create registration",
            "category": "Registrations",
            "method": "POST",
            "description": "Register the cardholder for lounge access on a specific flight. PII fields are JWE-encrypted.",
            "params": _CREATE_PARAMS,
            "encryption_required": True,
        },
        {
            "id": "get_registration",
            "name": "Get registration",
            "category": "Registrations",
            "method": "GET",
            "description": "Retrieve the details of a previously created registration.",
            "params": _GET_PARAMS,
        },
        {
            "id": "update_registration",
            "name": "Update registration",
            "category": "Registrations",
            "method": "PUT",
            "description": "Update personal information on an existing registration. PII fields are JWE-encrypted.",
            "params": _UPDATE_PARAMS,
            "encryption_required": True,
        },
        {
            "id": "cancel_registration",
            "name": "Cancel registration",
            "category": "Registrations",
            "method": "DELETE",
            "description": "Cancel an existing registration prior to the day of travel.",
            "params": _CANCEL_PARAMS,
        },
    ],
}


def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if op_id == "eligibility_check":
        return _eligibility_check(params)
    if op_id == "get_registration":
        return _get_registration(params)
    if op_id == "cancel_registration":
        return _cancel_registration(params)
    if op_id in ("create_registration", "update_registration"):
        # JWE encryption not implemented yet for Flight Delay Pass.
        return {
            "success": False,
            "error": _ENC_NOTE,
            "request":  {"method": "POST" if op_id == "create_registration" else "PUT",
                          "url": f"{_base()}/registrations",
                          "body": params},
            "response": {"status_code": None, "body": None},
            "state_updates": {},
        }
    return {"success": False, "error": f"Unknown operation: {op_id}"}


# ---------------------------------------------------------------------------
# Operation handlers
# ---------------------------------------------------------------------------

def _eligibility_check(params: Dict[str, Any]) -> Dict[str, Any]:
    required = ("carrierCode", "flightNumber", "departureDate",
                "departureAirport", "arrivalAirport")
    missing = [k for k in required if not (params.get(k) or "").strip()]
    if missing:
        return {"success": False, "error": f"Missing required fields: {', '.join(missing)}"}

    query: Dict[str, Any] = {k: params[k].strip() for k in required}
    for opt in ("clientId", "propositionCode"):
        v = (params.get(opt) or "").strip()
        if v:
            query[opt] = v
    return _signed_request("GET", "/eligibility-checks", query=query)


def _get_registration(params: Dict[str, Any]) -> Dict[str, Any]:
    reg_id = (params.get("registrationId") or "").strip()
    if not reg_id:
        return {"success": False, "error": "registrationId is required."}
    return _signed_request("GET", f"/registrations/{reg_id}")


def _cancel_registration(params: Dict[str, Any]) -> Dict[str, Any]:
    reg_id = (params.get("registrationId") or "").strip()
    if not reg_id:
        return {"success": False, "error": "registrationId is required."}
    return _signed_request("DELETE", f"/registrations/{reg_id}")


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
    if not _configured() and not is_simulated("flight_delay_pass"):
        return {
            "success": False,
            "error": (
                "Flight Delay Pass is not configured. Set FLIGHT_DELAY_PASS_CONSUMER_KEY "
                "and FLIGHT_DELAY_PASS_SIGNING_KEY_PATH in .env, then restart the server. "
                "Note: live sandbox access also requires Mastercard tenant onboarding."
            ),
        }

    from urllib.parse import urlencode
    import requests

    url = f"{_base()}{path}"
    if query:
        url = f"{url}?{urlencode(query)}"

    body_str = json.dumps(body) if body is not None else None

    if is_simulated("flight_delay_pass"):
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

        consumer_key = os.environ["FLIGHT_DELAY_PASS_CONSUMER_KEY"]
        key_path     = os.environ["FLIGHT_DELAY_PASS_SIGNING_KEY_PATH"]
        key_password = os.environ.get("FLIGHT_DELAY_PASS_SIGNING_KEY_PASSWORD", "keystorepassword")

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
        reg_id = resp_body.get("registrationId") or resp_body.get("id")
        if reg_id:
            state_updates["lastRegistrationId"] = str(reg_id)

    return {
        "success": success,
        "data":    resp_body if success else {},
        "error":   None if success else (resp_body.get("Errors", {}) if isinstance(resp_body, dict) else resp_body),
        "request": {"method": method, "url": url, "body": body},
        "response": {"status_code": status_code, "body": resp_body},
        "state_updates": state_updates,
    }
