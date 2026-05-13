"""Consumer Clarity use case — merchant descriptor enrichment.

Wraps the Consumer Clarity (Ethoca) API and shapes its response into a
clean "before → after" merchant card for the Use Cases tab.
"""
from __future__ import annotations

from typing import Any, Dict, List

# Pull the sandbox preset list from the underlying API module so the UI
# always offers the same choices the backend can actually serve.
from apis.clarity.api import _PRESETS as _CLARITY_PRESETS  # type: ignore


_PRESET_OPTIONS: List[Dict[str, str]] = [
    {"value": key, "label": preset["label"]}
    for key, preset in _CLARITY_PRESETS.items()
]


MANIFEST: Dict[str, Any] = {
    "id": "clarity",
    "name": "Consumer Clarity",
    "description": (
        "Cryptic card statements drive cardholder confusion, unnecessary support calls, "
        "and costly chargebacks. Consumer Clarity transforms raw merchant descriptors — "
        "the kind that read like \"ANT*156LE\" or \"ZZZ*ACADEMY\" — into rich, recognisable "
        "merchant identities: clean names, logos, full addresses, MCC categories, and "
        "links to digital receipts. The result: fewer disputes, happier customers, and "
        "a transaction history that actually makes sense."
    ),
    "apis": ["clarity"],
    "render": "clarity",
    "presets": _PRESET_OPTIONS,
}


def do_action(action: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if action == "lookup":
        from apis.clarity import api as clarity_api

        result = clarity_api.execute("search_merchant", params)
        if not result.get("success"):
            return {"found": False, "error": result.get("error", "Lookup failed")}

        data = result.get("data") or {}
        results = data.get("results") or []

        # Recover the raw descriptor from the request body so the UI can render
        # the "before" state alongside the enriched "after" state.
        request_body = (result.get("request") or {}).get("body") or {}
        raw_criteria: Dict[str, Any] = {}
        try:
            raw_criteria = (
                request_body["searchCriteria"][0]["merchantCriteria"] or {}
            )
        except (KeyError, IndexError, TypeError):
            raw_criteria = {}

        if not results:
            return {
                "found": False,
                "raw": raw_criteria,
                "preset": data.get("preset"),
                "note": "No matching merchant found in the sandbox dataset.",
            }

        first = results[0]
        return {
            "found": True,
            "preset": data.get("preset"),
            "raw": raw_criteria,
            "merchant": _shape(first),
        }

    return {"error": f"Unknown action: {action}"}


# ---------------------------------------------------------------------------
# Shape a single Consumer Clarity result into a UI-friendly dict.
# ---------------------------------------------------------------------------
def _shape(item: Dict[str, Any]) -> Dict[str, Any]:
    address = item.get("address") or {}
    category = item.get("category") or {}
    location = item.get("location") or {}
    logos = item.get("logos") or []

    merchant_logo = _pick_logo(logos, ("MERCHANT", "MERCHANT_LOGO"))
    industry_logo = _pick_logo(logos, ("INDUSTRY", "INDUSTRY_LOGO"))

    addr_lines: List[str] = []
    line1 = address.get("addressLine1") or address.get("line1")
    if line1:
        addr_lines.append(line1)
    line2 = address.get("addressLine2") or address.get("line2")
    if line2:
        addr_lines.append(line2)
    city_region = " ".join(
        x for x in [address.get("city"), address.get("region") or address.get("regionCode")]
        if x
    ).strip()
    if city_region:
        addr_lines.append(city_region)
    postal = address.get("postalCode")
    country = address.get("country") or address.get("countryCode")
    last_line = " ".join(x for x in [postal, country] if x).strip()
    if last_line:
        addr_lines.append(last_line)

    return {
        "name":          item.get("merchantName") or "Unknown Merchant",
        "websiteUrl":    item.get("websiteUrl"),
        "merchantLogo":  merchant_logo,
        "industryLogo":  industry_logo,
        "addressLines":  addr_lines,
        "lat":           location.get("latitude"),
        "lng":           location.get("longitude"),
        "categoryCode":  category.get("code") or category.get("mcc"),
        "categoryName":  category.get("description") or category.get("name"),
        "receiptStatus": item.get("receiptStatus"),
        "receiptUrl":    item.get("receiptUrl"),
        "merchantStatus": item.get("merchantStatus"),
    }


def _pick_logo(logos: List[Dict[str, Any]], kinds: tuple) -> str | None:
    """Return the first logo URL whose ``logoType`` matches one of *kinds*."""
    if not logos:
        return None
    for logo in logos:
        kind = (logo.get("logoType") or logo.get("type") or "").upper()
        if kind in kinds:
            url = logo.get("url") or logo.get("logoUrl")
            if url:
                return url
    # Fallback: first logo with any URL
    for logo in logos:
        url = logo.get("url") or logo.get("logoUrl")
        if url:
            return url
    return None
