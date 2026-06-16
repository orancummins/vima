"""Places use case — "Near Me" merchant discovery.

Wraps the Places API to provide a proximity-based merchant search and
detail view for the Use Cases tab.  Users enter a location (lat/lng or
city/country) and see nearby merchants plotted on a map with rich
metadata: NFC support, payment capabilities, business status, etc.
"""
from __future__ import annotations

from typing import Any

# Industry code labels used in the UI dropdown.
INDUSTRY_PRESETS: list[dict[str, str]] = [
    {"value": "EAP", "label": "Eating Places & Restaurants"},
    {"value": "SHS", "label": "Shoe Stores"},
    {"value": "GRS", "label": "Grocery Stores & Supermarkets"},
    {"value": "GSS", "label": "Gas & Service Stations"},
    {"value": "DRS", "label": "Drug Stores & Pharmacies"},
    {"value": "",    "label": "All industries"},
]

MANIFEST: dict[str, Any] = {
    "id": "places",
    "name": "Places",
    "description": (
        "Mastercard Places turns anonymized transaction data from the payments "
        "network into a live, global merchant directory. Search for nearby "
        "merchants that accept Mastercard — filtered by industry, capabilities, "
        "and distance — and see them on a map with rich metadata: NFC, EMV, "
        "Apple/Google/Samsung Pay support, POS terminal counts, and more."
    ),
    "apis": ["places"],
    "render": "places",
    "industryPresets": INDUSTRY_PRESETS,
    "defaults": {
        "latitude": "38.7468239",
        "longitude": "-90.7460708",
        "distance": "15",
        "unit": "MILE",
        "countryCode": "US",
        "industry": "EAP",
    },
}

def do_action(action: str, params: dict[str, Any]) -> dict[str, Any]:
    from apis.places import api as places_api

    if action == "search":
        result = places_api.execute("search_places", {
            "latitude": params.get("latitude", ""),
            "longitude": params.get("longitude", ""),
            "radiusSearch": "true" if params.get("radiusSearch", True) else "false",
            "distance": params.get("distance", "15"),
            "unit": params.get("unit", "MILE"),
            "countryCode": params.get("countryCode", "US"),
            "industry": params.get("industry", ""),
            "cityName": params.get("cityName", ""),
            "limit": params.get("limit", "25"),
            "offset": params.get("offset", "0"),
        })
        if not result.get("success"):
            return {"error": result.get("error", "Search failed")}
        data = result.get("data") or {}
        items = data.get("items") or []
        return {
            "places": [_shape(p) for p in items],
            "total": data.get("total", len(items)),
            "offset": data.get("offset", 0),
            "limit": data.get("limit", 25),
        }

    if action == "detail":
        loc_id = (params.get("location_id") or "").strip()
        if not loc_id:
            return {"error": "location_id is required."}
        result = places_api.execute("get_place", {"location_id": loc_id})
        if not result.get("success"):
            return {"error": result.get("error", "Lookup failed")}
        data = result.get("data") or {}
        return {"place": _shape(data)}

    return {"error": f"Unknown action: {action}"}

def _build_address_parts(item: dict[str, Any]) -> list[str]:
    """Build ordered address components from a raw Places item."""
    parts: list[str] = []
    street = item.get("cleansedStreetAddress") or item.get("streetAddress")
    if street:
        parts.append(street)
    city  = item.get("cleansedCityName") or item.get("cityName")
    state = item.get("cleansedStateProvinceCode") or item.get("stateProvinceCode")
    city_state = " ".join(x for x in [city, state] if x)
    if city_state:
        parts.append(city_state)
    postal  = item.get("cleansedPostalCode") or item.get("postalCode")
    country = item.get("cleansedCountryCode") or item.get("countryCode")
    if postal:
        parts.append(postal)
    if country:
        parts.append(country)
    return parts


def _build_caps(item: dict[str, Any]) -> list[str]:
    """Return a list of payment capability labels present on a Places item."""
    _flag_labels = [
        ("hasNfc",         "NFC / Contactless"),
        ("hasEmv",         "EMV Chip"),
        ("hasApplePay",    "Apple Pay"),
        ("hasAndroidPay",  "Google Pay"),
        ("hasSamsungPay",  "Samsung Pay"),
        ("hasCashBack",    "Cash Back"),
        ("hasPayAtThePump","Pay at Pump"),
        ("isEcommerce",    "E-commerce"),
        ("isBrickAndMortar","In-store"),
    ]
    return [label for flag, label in _flag_labels if item.get(flag)]


def _shape(item: dict[str, Any]) -> dict[str, Any]:
    """Normalize a raw Places item into a UI-friendly dict."""
    name = (
        item.get("cleansedMerchantName")
        or item.get("merchantName")
        or "Unknown Merchant"
    )
    address_parts = _build_address_parts(item)
    caps = _build_caps(item)

    return {
        "locationId": item.get("locationId"),
        "name": name,
        "legalName": item.get("cleansedLegalCorporateName") or item.get("legalCorporateName") or "",
        "address": ", ".join(address_parts),
        "addressParts": address_parts,
        "phone": item.get("cleansedTelephoneNumber") or item.get("telephoneNumber") or "",
        "website": item.get("cleansedMerchantUrl") or "",
        "lat": item.get("latitude"),
        "lng": item.get("longitude"),
        "industry": item.get("industry") or "",
        "superIndustry": item.get("superIndustry") or "",
        "mccCode": item.get("mccCode") or "",
        "aggregateMerchantName": item.get("aggregateMerchantName") or "",
        "parentMerchantName": item.get("parentAggregateMerchantName") or "",
        "geocodeQuality": item.get("geocodeQualityIndicator") or "",
        "isNewBusiness": bool(item.get("isNewBusiness")),
        "isInBusiness": bool(item.get("isInBusiness7Day")),
        "channel": item.get("primaryChannelOfDistribution") or "",
        "posTerminals": item.get("posTerminalCount") or 0,
        "capabilities": caps,
        "hasNfc": bool(item.get("hasNfc")),
        "hasEmv": bool(item.get("hasEmv")),
        "firstSeen": item.get("firstSeenWeek") or "",
        "lastSeen": item.get("lastSeenWeek") or "",
    }
