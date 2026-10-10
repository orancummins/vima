"""Settle In — a concept use case: a newcomer's first day in a new country.

Priya moves from Dublin to New York with no US credit history. The page
steps through her day, one moment at a time: Open Finance brings her Irish
bank history, a card is approved and tokenised into her phone's wallet,
money goes home with the rate shown up front, her statement is enriched,
fraud is stopped in milliseconds, and a Priceless Surprise ends the day.

It is a concept: the screens are illustrative and the APIs are not called
yet. The ones already wired in Solution Studio are listed below; those to
add (Cross-Border Services or Mastercard Send, MDES tokenisation, Identity
Insights, Decision Intelligence, Identity Check) are marked on the page.
"""
from __future__ import annotations

from typing import Any

MANIFEST: dict[str, Any] = {
    "id": "settle_in",
    "name": "Settle In",
    "description": (
        "Concept: a newcomer's first day in New York, on Mastercard. Open Finance brings "
        "Priya's Irish bank history so she's approved for a card with no US credit file; "
        "it's tokenised into her phone, accepted almost everywhere, and protected by AI "
        "fraud scoring. She sends money home with the rate up front, her statement "
        "makes sense, and her first night ends with a Priceless Surprise."
    ),
    "apis": [
        "open_finance_eu",
        "bin_lookup",
        "enhanced_currency_conversion_calculator",
        "consumer_clarity",
        "merchant_identifier",
        "places",
        "transaction_notifications",
        "benefits_eligibility",
        "priceless_cities",
    ],
    "render": "webview",
    "concept": True,
}
