"""Easy Savings use case — browse and redeem SME merchant offers.

Wraps the Easy Savings Specials API and shapes the response into a
clean offer-browsing experience for the Use Cases tab.
"""
from __future__ import annotations

from typing import Any

MANIFEST: dict[str, Any] = {
    "id": "easysavings",
    "name": "Easy Savings",
    "description": (
        "Mastercard Easy Savings Specials lets issuers embed localised SME "
        "merchant offers — discounts, vouchers, and promotions — directly into "
        "their apps so business cardholders can discover and unlock savings in "
        "seconds. Browse the global catalogue by BIN and country, then redeem "
        "an offer to reveal its voucher code."
    ),
    "apis": ["easysavings"],
    "render": "easysavings",
    "defaults": {
        "bin": "52345678",
        "country": "IND",
        "language": "en-US",
    },
}


def do_action(action: str, params: dict[str, Any]) -> dict[str, Any]:
    from apis.easysavings import api as es_api

    if action == "browse":
        result = es_api.execute("list_offers", params)
        if not result.get("success"):
            return {"error": result.get("error", "Failed to list offers")}
        data = result.get("data") or {}
        offers = data.get("offers") or data.get("items") or []
        if isinstance(data, list):
            offers = data
        return {
            "offers": [_shape_offer(o) for o in offers],
            "total": data.get("total") or len(offers),
        }

    if action == "redeem":
        bin_val = (params.get("bin") or "").strip()
        offer_id = (params.get("offer_id") or "").strip()
        if not bin_val or not offer_id:
            return {"error": "Both 'bin' and 'offer_id' are required."}
        result = es_api.execute("redeem_offer", {
            "bin": bin_val,
            "offer_id": offer_id,
        })
        if not result.get("success"):
            return {"error": result.get("error", "Redemption failed")}
        data = result.get("data") or {}
        return {"redemption": _shape_redemption(data)}

    return {"error": f"Unknown action: {action}"}


def _shape_offer(o: dict[str, Any]) -> dict[str, Any]:
    merchant = o.get("merchant") or {}
    return {
        "id": o.get("id") or o.get("offerId") or "",
        "title": o.get("title") or o.get("offerTitle") or "Untitled offer",
        "description": o.get("description") or o.get("offerDescription") or "",
        "merchantName": merchant.get("name") or o.get("merchantName") or "Unknown merchant",
        "merchantLogo": merchant.get("logoUrl") or o.get("merchantLogoUrl") or "",
        "category": merchant.get("category") or o.get("category") or "",
        "discountValue": o.get("discountValue") or o.get("discount") or "",
        "discountType": o.get("discountType") or "",
        "startDate": o.get("startDate") or "",
        "endDate": o.get("endDate") or o.get("expiryDate") or "",
        "termsUrl": o.get("termsUrl") or "",
        "redemptionUrl": o.get("redemptionUrl") or "",
        "redemptionChannel": o.get("redemptionChannel") or "",
    }


def _shape_redemption(data: dict[str, Any]) -> dict[str, Any]:
    return {
        "orderId": data.get("orderId") or data.get("order_id") or "",
        "status": data.get("status") or "unknown",
        "voucherCode": data.get("voucherCode") or data.get("voucher_code") or "",
        "redemptionUrl": data.get("redemptionUrl") or "",
        "validUntil": data.get("validUntil") or data.get("expiryDate") or "",
    }
