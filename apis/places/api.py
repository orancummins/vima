"""Mastercard Places API — OAuth 1.0a.

Endpoints (base: /location-intelligence/places-locator):
  POST /places/searches                          — search for places (radius or filter)
  GET  /places/{location_id}                     — get location details by ID
  GET  /merchant-category-codes                  — list all active MCC codes
  GET  /merchant-category-codes/mcc-codes/{mcc}  — get MCC by code
  GET  /merchant-industry-codes                  — list all active industry codes
  GET  /merchant-industry-codes/industries/{ind}  — get industry code details

Auth: OAuth 1.0a (Mastercard signing library).

Docs:
  https://developer.mastercard.com/places/documentation/
  https://developer.mastercard.com/places/documentation/api-reference/
"""
from __future__ import annotations

import json
import os
from typing import Any, Dict

_SANDBOX_BASE_URL = "https://sandbox.api.mastercard.com/location-intelligence/places-locator"
_PROD_BASE_URL = "https://api.mastercard.com/location-intelligence/places-locator"

MANIFEST: Dict[str, Any] = {
    "id": "places",
    "name": "Places",
    "description": (
        "Mastercard Places — a comprehensive global point-of-interest dataset "
        "delivering accurate, current merchant location data sourced from "
        "anonymized transaction data on the Mastercard payments network."
    ),
    "docs_url": "https://developer.mastercard.com/places/documentation/",
    "how_to": (
        "<p><strong>Places</strong> provides the most accurate and current snapshot of "
        "merchant locations accepting Mastercard — both brick-and-mortar and eCommerce.</p>"
        "<h3>How to use</h3>"
        "<ol>"
        "<li>Use <strong>Places → Search places</strong> to find merchants near a "
        "latitude/longitude or within a country/city. Set <code>radiusSearch</code> to "
        "<code>true</code> and provide distance + unit for proximity searches.</li>"
        "<li>Use <strong>Places → Get place details</strong> with a <code>locationId</code> "
        "from search results to retrieve full merchant metadata.</li>"
        "<li>Use <strong>Reference → List MCC codes</strong> or "
        "<strong>List industry codes</strong> to look up category taxonomies.</li>"
        "</ol>"
        "<h3>Sandbox tips</h3>"
        "<ul>"
        "<li>Lat <code>38.7468</code>, Lng <code>-90.7461</code> (O'Fallon, MO) with "
        "industry <code>EAP</code> returns restaurants.</li>"
        "<li>Country <code>US</code> with radius search works well in sandbox.</li>"
        "<li>Download the <a href='https://static.developer.mastercard.com/content/"
        "places/uploads/places_sandbox_data.xlsx' target='_blank'>sandbox data sheet</a> "
        "for all valid test locations.</li>"
        "</ul>"
    ),
    "categories": ["Places", "Reference"],
    "state_schema": [],
    "configured": bool(
        os.environ.get("PLACES_CONSUMER_KEY")
        and os.environ.get("PLACES_CONSUMER_KEY") != "your-consumer-key-here"
        and os.environ.get("PLACES_SIGNING_KEY_PATH")
    ),
    "operations": [
        {
            "id": "search_places",
            "name": "Search places",
            "category": "Places",
            "method": "POST",
            "description": (
                "Search for merchant locations by country, city, lat/lng radius, "
                "industry, MCC code, and other filters."
            ),
            "params": [
                {
                    "name": "latitude",
                    "label": "Latitude",
                    "type": "text",
                    "default": "38.7468239",
                    "required": False,
                },
                {
                    "name": "longitude",
                    "label": "Longitude",
                    "type": "text",
                    "default": "-90.7460708",
                    "required": False,
                },
                {
                    "name": "radiusSearch",
                    "label": "Radius search",
                    "type": "select",
                    "default": "true",
                    "required": True,
                    "options": [
                        {"value": "true", "label": "Yes"},
                        {"value": "false", "label": "No"},
                    ],
                },
                {
                    "name": "distance",
                    "label": "Distance",
                    "type": "text",
                    "default": "15",
                    "required": False,
                },
                {
                    "name": "unit",
                    "label": "Unit",
                    "type": "select",
                    "default": "MILE",
                    "required": False,
                    "options": [
                        {"value": "MILE", "label": "Mile"},
                        {"value": "KM", "label": "Kilometer"},
                    ],
                },
                {
                    "name": "countryCode",
                    "label": "Country code (ISO-2)",
                    "type": "text",
                    "default": "US",
                    "required": True,
                },
                {
                    "name": "industry",
                    "label": "Industry code",
                    "type": "text",
                    "default": "EAP",
                    "required": False,
                },
                {
                    "name": "cityName",
                    "label": "City name",
                    "type": "text",
                    "default": "",
                    "required": False,
                },
                {
                    "name": "limit",
                    "label": "Limit",
                    "type": "text",
                    "default": "25",
                    "required": False,
                },
                {
                    "name": "offset",
                    "label": "Offset",
                    "type": "text",
                    "default": "0",
                    "required": False,
                },
            ],
        },
        {
            "id": "get_place",
            "name": "Get place details",
            "category": "Places",
            "method": "GET",
            "description": "Retrieve full details of a specific location by its ID.",
            "params": [
                {
                    "name": "location_id",
                    "label": "Location ID",
                    "type": "text",
                    "default": "300945305",
                    "required": True,
                },
            ],
        },
        {
            "id": "list_mcc_codes",
            "name": "List MCC codes",
            "category": "Reference",
            "method": "GET",
            "description": "Retrieve all active Merchant Category Codes.",
            "params": [],
        },
        {
            "id": "get_mcc_code",
            "name": "Get MCC by code",
            "category": "Reference",
            "method": "GET",
            "description": "Get details of a specific Merchant Category Code.",
            "params": [
                {
                    "name": "mcc_code",
                    "label": "MCC code",
                    "type": "text",
                    "default": "5812",
                    "required": True,
                },
            ],
        },
        {
            "id": "list_industry_codes",
            "name": "List industry codes",
            "category": "Reference",
            "method": "GET",
            "description": "Retrieve all active merchant industry codes.",
            "params": [],
        },
        {
            "id": "get_industry_code",
            "name": "Get industry code details",
            "category": "Reference",
            "method": "GET",
            "description": "Get details of a specific industry code.",
            "params": [
                {
                    "name": "industry",
                    "label": "Industry code",
                    "type": "text",
                    "default": "EAP",
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
    env = os.environ.get("PLACES_ENV", "sandbox").lower()
    real = _PROD_BASE_URL if env == "production" else _SANDBOX_BASE_URL
    return sim_base_url("places", real)


def _configured() -> bool:
    key = os.environ.get("PLACES_CONSUMER_KEY", "")
    path = os.environ.get("PLACES_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated("places")


def get_state() -> Dict[str, Any]:
    return {"configured": _configured()}


def _not_configured_err() -> Dict[str, Any]:
    return {
        "success": False,
        "error": (
            "Places is not configured. Set PLACES_CONSUMER_KEY and "
            "PLACES_SIGNING_KEY_PATH in .env, then restart the server."
        ),
    }


def _resolve_key_path(path: str) -> str:
    if os.path.isabs(path):
        return path
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(project_root, path)


def _signed_request(method: str, url: str, body_str: str | None) -> Dict[str, Any]:
    """Build OAuth-signed headers + execute the HTTP call."""
    from simulator.switcher import is_simulated
    import requests

    headers = {"Accept": "application/json"}
    if body_str is not None:
        headers["Content-Type"] = "application/json"

    if is_simulated("places"):
        headers["Authorization"] = "Simulated"
    else:
        import oauth1.authenticationutils as authutils
        from oauth1.oauth import OAuth

        consumer_key = os.environ["PLACES_CONSUMER_KEY"]
        key_path = _resolve_key_path(os.environ["PLACES_SIGNING_KEY_PATH"])
        key_password = os.environ.get("PLACES_SIGNING_KEY_PASSWORD", "keystorepassword")

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
        "error": None if success else (
            resp_body.get("Errors") if isinstance(resp_body, dict) else resp_body
        ),
        "request": {"method": method, "url": url, "body": body_str},
        "response": {"status_code": status_code, "body": resp_body},
        "state_updates": {},
    }


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------
def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if op_id == "search_places":
        return _search_places(params)
    if op_id == "get_place":
        return _get_place(params)
    if op_id == "list_mcc_codes":
        return _list_mcc_codes()
    if op_id == "get_mcc_code":
        return _get_mcc_code(params)
    if op_id == "list_industry_codes":
        return _list_industry_codes()
    if op_id == "get_industry_code":
        return _get_industry_code(params)
    return {"success": False, "error": f"Unknown operation: {op_id}"}


# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------
def _search_places(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("places"):
        return _not_configured_err()
    from urllib.parse import urlencode

    country = (params.get("countryCode") or "").strip()
    if not country:
        return {"success": False, "error": "countryCode is required."}

    place: Dict[str, Any] = {"countryCode": country}

    industry = (params.get("industry") or "").strip()
    if industry:
        place["industry"] = industry

    city = (params.get("cityName") or "").strip()
    if city:
        place["cityName"] = city

    radius_search = str(params.get("radiusSearch", "false")).lower() == "true"

    lat = (params.get("latitude") or "").strip()
    lng = (params.get("longitude") or "").strip()
    if lat:
        place["latitude"] = float(lat)
    if lng:
        place["longitude"] = float(lng)

    body: Dict[str, Any] = {
        "place": place,
        "radiusSearch": radius_search,
    }

    if radius_search:
        distance = (params.get("distance") or "15").strip()
        unit = (params.get("unit") or "MILE").strip()
        body["distance"] = int(distance)
        body["unit"] = unit

    limit = (params.get("limit") or "25").strip()
    offset = (params.get("offset") or "0").strip()
    qs = urlencode({"limit": limit, "offset": offset})

    body_str = json.dumps(body)
    url = f"{_base_url()}/places/searches?{qs}"
    return _signed_request("POST", url, body_str)


def _get_place(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("places"):
        return _not_configured_err()
    location_id = (params.get("location_id") or "").strip()
    if not location_id:
        return {"success": False, "error": "location_id is required."}
    url = f"{_base_url()}/places/{location_id}"
    return _signed_request("GET", url, None)


def _list_mcc_codes() -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("places"):
        return _not_configured_err()
    return _signed_request("GET", f"{_base_url()}/merchant-category-codes", None)


def _get_mcc_code(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("places"):
        return _not_configured_err()
    mcc = (params.get("mcc_code") or "").strip()
    if not mcc:
        return {"success": False, "error": "mcc_code is required."}
    return _signed_request("GET", f"{_base_url()}/merchant-category-codes/mcc-codes/{mcc}", None)


def _list_industry_codes() -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("places"):
        return _not_configured_err()
    return _signed_request("GET", f"{_base_url()}/merchant-industry-codes", None)


def _get_industry_code(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("places"):
        return _not_configured_err()
    industry = (params.get("industry") or "").strip()
    if not industry:
        return {"success": False, "error": "industry code is required."}
    return _signed_request(
        "GET", f"{_base_url()}/merchant-industry-codes/industries/{industry}", None
    )
