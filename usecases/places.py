"""Places use case — "Near Me" merchant discovery.

Wraps the Places API to provide a proximity-based merchant search and
detail view for the Use Cases tab.  Users enter a location (lat/lng or
city/country) and see nearby merchants plotted on a map with rich
metadata: NFC support, payment capabilities, business status, etc.
"""
from __future__ import annotations

from typing import Any, Dict, List


# Industry code labels used in the UI dropdown.
INDUSTRY_PRESETS: List[Dict[str, str]] = [
    {"value": "EAP", "label": "Eating Places & Restaurants"},
    {"value": "SHS", "label": "Shoe Stores"},
    {"value": "GRS", "label": "Grocery Stores & Supermarkets"},
    {"value": "GSS", "label": "Gas & Service Stations"},
    {"value": "DRS", "label": "Drug Stores & Pharmacies"},
    {"value": "",    "label": "All industries"},
]


MANIFEST: Dict[str, Any] = {
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


def do_action(action: str, params: Dict[str, Any]) -> Dict[str, Any]:
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


def _shape(item: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize a raw Places item into a UI-friendly dict."""
    name = (
        item.get("cleansedMerchantName")
        or item.get("merchantName")
        or "Unknown Merchant"
    )
    address_parts = []
    street = item.get("cleansedStreetAddress") or item.get("streetAddress")
    if street:
        address_parts.append(street)
    city = item.get("cleansedCityName") or item.get("cityName")
    state = item.get("cleansedStateProvinceCode") or item.get("stateProvinceCode")
    postal = item.get("cleansedPostalCode") or item.get("postalCode")
    country = item.get("cleansedCountryCode") or item.get("countryCode")
    city_state = " ".join(x for x in [city, state] if x)
    if city_state:
        address_parts.append(city_state)
    if postal:
        address_parts.append(postal)
    if country:
        address_parts.append(country)

    phone = item.get("cleansedTelephoneNumber") or item.get("telephoneNumber")
    url = item.get("cleansedMerchantUrl") or ""

    caps = []
    if item.get("hasNfc"):
        caps.append("NFC / Contactless")
    if item.get("hasEmv"):
        caps.append("EMV Chip")
    if item.get("hasApplePay"):
        caps.append("Apple Pay")
    if item.get("hasAndroidPay"):
        caps.append("Google Pay")
    if item.get("hasSamsungPay"):
        caps.append("Samsung Pay")
    if item.get("hasCashBack"):
        caps.append("Cash Back")
    if item.get("hasPayAtThePump"):
        caps.append("Pay at Pump")
    if item.get("isEcommerce"):
        caps.append("E-commerce")
    if item.get("isBrickAndMortar"):
        caps.append("In-store")

    return {
        "locationId": item.get("locationId"),
        "name": name,
        "legalName": item.get("cleansedLegalCorporateName") or item.get("legalCorporateName") or "",
        "address": ", ".join(address_parts),
        "addressParts": address_parts,
        "phone": phone or "",
        "website": url,
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
