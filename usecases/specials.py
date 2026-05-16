"""Priceless Concierge — Priceless Specials use case.

Wraps the Priceless Specials API and shapes its three core feeds —
offers, benefits and programs — together with merchants into a single
"trip planner" experience for a Mastercard cardholder.

The user picks:
    * Issuing country  (eligible_markets)
    * Destination      (destination_markets)
    * Mastercard product  (MWE / MWP / MPL / …)
    * Category interest    (Dining / Travel / Shopping / …)

… and the page shows curated offers, card benefits, marketing programs
and participating merchants for that combination.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List


MANIFEST: Dict[str, Any] = {
    "id": "specials",
    "name": "Priceless Concierge",
    "description": (
        "Travelling abroad? Priceless Specials surfaces Mastercard's curated "
        "catalogue of merchant offers, card-product benefits and marketing "
        "programs available in your destination. Pick your card and where "
        "you're going — the concierge does the rest."
    ),
    "apis": ["Priceless Specials"],
    "render": "specials",
    "defaults": {
        "eligible_markets": "US",
        "destination_markets": "JP",
        "mastercard_product": "MWE",
        "category": "",
        "language": "en-US",
    },
}


# --- Action dispatcher ----------------------------------------------------

def do_action(action: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if action == "search":
        return _search(params)
    return {"error": f"Unknown action: {action}"}


# --- Search ---------------------------------------------------------------

def _search(params: Dict[str, Any]) -> Dict[str, Any]:
    from apis.priceless import api as p_api

    base: Dict[str, Any] = {
        "language":            params.get("language") or "en-US",
        "eligible_markets":    params.get("eligible_markets") or "",
        "destination_markets": params.get("destination_markets") or "",
        "category":            params.get("category") or "",
        "mastercard_product":  params.get("mastercard_product") or "",
    }
    # Drop empties for the merchants & programs feeds that don't use category etc.
    merchants_params = {k: v for k, v in base.items() if v}
    programs_params  = {k: v for k, v in {
        "language":         base["language"],
        "eligible_markets": base["eligible_markets"],
    }.items() if v}

    feeds = {
        "offers":    ("specials_offers",    base),
        "benefits":  ("specials_benefits",  base),
        "programs":  ("specials_programs",  programs_params),
        "merchants": ("specials_merchants", merchants_params),
    }

    results: Dict[str, Dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=4) as ex:
        futures = {key: ex.submit(p_api.execute, op, p) for key, (op, p) in feeds.items()}
        for key, fut in futures.items():
            try:
                results[key] = fut.result(timeout=20) or {}
            except Exception as e:  # pragma: no cover
                results[key] = {"success": False, "error": str(e)}

    # If every call failed for the same reason (e.g. not configured) surface a
    # single error so the UI can show a clean message rather than four cards.
    if all(not r.get("success") for r in results.values()):
        first_err = next((r.get("error") for r in results.values() if r.get("error")), None)
        return {
            "error": _stringify_error(first_err) or "Priceless Specials request failed.",
        }

    return {
        "offers":    [_shape_offer(o)    for o in _items(results["offers"].get("data"))],
        "benefits":  [_shape_benefit(b)  for b in _items(results["benefits"].get("data"))],
        "programs":  [_shape_program(p)  for p in _items(results["programs"].get("data"))],
        "merchants": [_shape_merchant(m) for m in _items(results["merchants"].get("data"))],
        "partial_errors": {
            key: _stringify_error(r.get("error"))
            for key, r in results.items()
            if not r.get("success")
        },
    }


# --- Helpers --------------------------------------------------------------

def _items(data: Any) -> List[Dict[str, Any]]:
    """Normalize any Priceless Specials response shape to a flat list."""
    if data is None:
        return []
    if isinstance(data, list):
        return [x for x in data if isinstance(x, dict)]
    if isinstance(data, dict):
        for key in (
            "Offers", "offers",
            "Benefits", "benefits",
            "Programs", "programs",
            "Merchants", "merchants",
            "items", "Items",
            "data", "Data",
            "results",
        ):
            v = data.get(key)
            if isinstance(v, list):
                return [x for x in v if isinstance(x, dict)]
            if isinstance(v, dict):
                # Sometimes the inner shape is { Offers: { Offer: [...] } }
                for inner_key in ("Offer", "Benefit", "Program", "Merchant", "items"):
                    iv = v.get(inner_key)
                    if isinstance(iv, list):
                        return [x for x in iv if isinstance(x, dict)]
                    if isinstance(iv, dict):
                        return [iv]
    return []


def _first(d: Dict[str, Any], *keys: str, default: str = "") -> str:
    for k in keys:
        v = d.get(k)
        if v not in (None, "", []):
            return str(v) if not isinstance(v, (dict, list)) else default
    return default


def _shape_offer(o: Dict[str, Any]) -> Dict[str, Any]:
    merchant = o.get("merchant") or o.get("Merchant") or {}
    if not isinstance(merchant, dict):
        merchant = {}
    dates = o.get("offerDates") or o.get("OfferDates") or {}
    if not isinstance(dates, dict):
        dates = {}
    return {
        "id":           _first(o, "id", "offerId", "OfferId", "Id"),
        "title":        _first(o, "offerTitle", "title", "Title", "name", "Name", default="Untitled offer"),
        "description":  _first(o, "offerDescription", "description", "Description", "shortDescription"),
        "merchantName": _first(merchant, "name", "Name", "merchantName") or _first(o, "merchantName"),
        "merchantLogo": _first(merchant, "logoUrl", "logo", "imageUrl") or _first(o, "merchantLogoUrl", "logoUrl"),
        "category":     _first(merchant, "categoryName", "category") or _first(o, "category", "categoryName"),
        "discount":     _first(o, "offerHeadline", "discountText", "discount", "discountValue", "savings"),
        "startDate":    _first(dates, "startDate", "from") or _first(o, "startDate"),
        "endDate":      _first(dates, "endDate", "to") or _first(o, "endDate", "expiryDate"),
        "redemptionUrl":_first(o, "redemptionUrl", "RedemptionURL", "ctaUrl", "url"),
        "termsUrl":     _first(o, "termsAndConditionsUrl", "termsUrl", "tncUrl"),
        "tags":         _list_str(o.get("tags") or o.get("Tags")),
    }


def _shape_benefit(b: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id":          _first(b, "id", "benefitId", "BenefitId"),
        "title":       _first(b, "benefitTitle", "title", "Title", "name", default="Benefit"),
        "description": _first(b, "benefitDescription", "description", "shortDescription"),
        "category":    _first(b, "category", "categoryName", "type"),
        "icon":        _first(b, "iconUrl", "imageUrl", "logoUrl"),
        "url":         _first(b, "redemptionUrl", "url", "detailsUrl"),
        "endDate":     _first(b, "endDate", "expiryDate"),
    }


def _shape_program(p: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id":          _first(p, "id", "programId", "ProgramId"),
        "title":       _first(p, "programTitle", "title", "Name", "name", default="Program"),
        "description": _first(p, "programDescription", "description"),
        "image":       _first(p, "imageUrl", "heroImageUrl", "bannerUrl"),
        "url":         _first(p, "programUrl", "url"),
    }


def _shape_merchant(m: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id":       _first(m, "id", "merchantId", "MerchantId"),
        "name":     _first(m, "merchantName", "name", "Name", default="Merchant"),
        "category": _first(m, "categoryName", "category"),
        "logo":     _first(m, "logoUrl", "imageUrl", "logo"),
        "country":  _first(m, "country", "countryCode"),
    }


def _list_str(v: Any) -> List[str]:
    if isinstance(v, list):
        return [str(x) for x in v if x is not None]
    if isinstance(v, str):
        return [t.strip() for t in v.split(",") if t.strip()]
    return []


def _stringify_error(err: Any) -> str:
    if err is None:
        return ""
    if isinstance(err, str):
        return err
    try:
        import json as _json
        return _json.dumps(err)[:400]
    except Exception:
        return str(err)[:400]
