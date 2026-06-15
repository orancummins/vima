"""The Wire — x-ray of a single transaction's journey.

Most consumer-finance demos visualise *aggregates* (charts, fingerprints,
category fields).  The Wire does the opposite: it picks one transaction
and shows the entire data journey it took to land on your phone — from
raw POS descriptor at the merchant terminal, through Mastercard's Open
Finance aggregation, merchant cleanup, category enrichment, and finally
the line of text the consumer sees in their banking app.

The visualisation is a vertical glowing wire with five nodes.  A packet
animates along it; each node reveals the exact JSON shape of the
transaction at that stage.  This makes the *plumbing* of Open Banking
tangible — something nobody normally shows consumers.

Data shape (returned by :func:`get_data`)::

    {
      "transactions": [
        {
          "id": "tw_1",
          "summary": "Blue Bottle Coffee  ·  $4.50",
          "stages": [
            {"id": "bank",     "label": "...", "blob": {...}},
            {"id": "agg",      "label": "...", "blob": {...}},
            {"id": "merchant", "label": "...", "blob": {...}},
            {"id": "category", "label": "...", "blob": {...}},
            {"id": "app",      "label": "...", "blob": {...}},
          ],
        },
        ...
      ]
    }

The data is curated and baked in so the demo is reliable and offline-
capable.  Each transaction is hand-picked to show a different facet of
enrichment (cryptic descriptor cleanup, brand recognition, MCC mapping,
recurring detection, etc.).
"""
from __future__ import annotations

from typing import Any

MANIFEST: dict[str, Any] = {
    "id": "the_wire",
    "name": "The Wire",
    "description": (
        "An x-ray of the journey a single transaction takes — from a "
        "cryptic POS descriptor at the merchant terminal, through Open "
        "Finance aggregation, merchant cleanup and category enrichment, "
        "to the clean line your consumer finally sees in their banking "
        "app.  Pick a transaction, watch the packet travel the wire, "
        "click any node to inspect the exact JSON shape at that stage."
    ),
    "apis": ["open_finance", "merchant_identifier", "consumer_clarity"],
    "render": "the_wire",
}

# This use case is fully offline-capable — no live Open Finance customer
# required.  Lets the route at ``/usecases/the_wire/data`` serve the
# curated journeys even when nobody has connected a bank yet.
REQUIRES_CUSTOMER = False

# ---------------------------------------------------------------------------
# Curated journeys — each one is real-shaped data hand-assembled so the demo
# works without any live API calls.  Picked to show different facets:
#   tw_1 — cryptic descriptor → recognised brand (coffee shop)
#   tw_2 — ambiguous airline code → branded carrier + travel category
#   tw_3 — recurring subscription detection (streaming)
#   tw_4 — grocery store with location
#   tw_5 — ride-share with MCC mapping
#   tw_6 — bill-pay / utilities recurring
# ---------------------------------------------------------------------------
_JOURNEYS: list[dict[str, Any]] = [
    {
        "id": "tw_1",
        "summary": "Blue Bottle Coffee  ·  $4.50",
        "stages": [
            {
                "id": "bank",
                "label": "Bank terminal",
                "sub": "Raw POS descriptor from the issuer",
                "blob": {
                    "postingDate": "2026-05-09T10:31:14Z",
                    "amount": -4.50,
                    "currency": "USD",
                    "description": "POS DEBIT BLBOT*SF42 OAKLAND CA",
                    "merchantId": None,
                },
            },
            {
                "id": "agg",
                "label": "Open Finance aggregation",
                "sub": "GET /aggregation/v3/customers/{id}/transactions",
                "blob": {
                    "id": "9921774461",
                    "amount": -4.50,
                    "accountId": "5011112233",
                    "customerId": "9021080528",
                    "status": "active",
                    "description": "POS DEBIT BLBOT*SF42 OAKLAND CA",
                    "postedDate": 1762684274,
                    "transactionDate": 1762684274,
                    "type": "directDebit",
                },
            },
            {
                "id": "merchant",
                "label": "Merchant Identifier",
                "sub": "POST /merchant-identifier/v1/lookup",
                "blob": {
                    "merchant": {
                        "name": "Blue Bottle Coffee",
                        "merchantId": "BBC-OAK-42",
                        "logoUrl": "https://logos.mastercard.com/blue-bottle.png",
                        "location": {
                            "city": "Oakland",
                            "region": "CA",
                            "country": "US",
                            "lat": 37.8044,
                            "lon": -122.2712,
                        },
                        "confidence": 0.97,
                    },
                },
            },
            {
                "id": "category",
                "label": "Category enrichment",
                "sub": "Enrichment service (MCC 5814 → group mapping)",
                "blob": {
                    "category": "Coffee Shops",
                    "categoryGroup": "Groceries & Dining",
                    "mcc": "5814",
                    "isRecurring": False,
                    "isEcommerce": False,
                    "categoryScore": 0.92,
                },
            },
            {
                "id": "app",
                "label": "Your banking app",
                "sub": "What the consumer finally sees",
                "blob": {
                    "title": "Blue Bottle Coffee",
                    "subtitle": "Oakland, CA · Today",
                    "amount": "-$4.50",
                    "icon": "☕",
                    "category": "Coffee Shops",
                },
            },
        ],
    },
    {
        "id": "tw_2",
        "summary": "United Airlines  ·  $487.20",
        "stages": [
            {
                "id": "bank",
                "label": "Bank terminal",
                "sub": "Raw POS descriptor from the issuer",
                "blob": {
                    "postingDate": "2026-05-07T08:11:02Z",
                    "amount": -487.20,
                    "currency": "USD",
                    "description": "UAL*0162287733991 800-932-2732 TX",
                    "merchantId": None,
                },
            },
            {
                "id": "agg",
                "label": "Open Finance aggregation",
                "sub": "GET /aggregation/v3/customers/{id}/transactions",
                "blob": {
                    "id": "9921774314",
                    "amount": -487.20,
                    "accountId": "5011112233",
                    "customerId": "9021080528",
                    "status": "active",
                    "description": "UAL*0162287733991 800-932-2732 TX",
                    "postedDate": 1762502262,
                    "transactionDate": 1762502262,
                    "type": "directDebit",
                },
            },
            {
                "id": "merchant",
                "label": "Merchant Identifier",
                "sub": "POST /merchant-identifier/v1/lookup",
                "blob": {
                    "merchant": {
                        "name": "United Airlines",
                        "merchantId": "UAL-CORP",
                        "logoUrl": "https://logos.mastercard.com/united.png",
                        "location": None,
                        "confidence": 0.99,
                        "website": "https://www.united.com",
                    },
                },
            },
            {
                "id": "category",
                "label": "Category enrichment",
                "sub": "Enrichment service (MCC 3000 → group mapping)",
                "blob": {
                    "category": "Airlines",
                    "categoryGroup": "Travel & Vacation",
                    "mcc": "3000",
                    "isRecurring": False,
                    "isEcommerce": True,
                    "categoryScore": 0.95,
                },
            },
            {
                "id": "app",
                "label": "Your banking app",
                "sub": "What the consumer finally sees",
                "blob": {
                    "title": "United Airlines",
                    "subtitle": "Flight · 2 days ago",
                    "amount": "-$487.20",
                    "icon": "✈",
                    "category": "Travel",
                },
            },
        ],
    },
    {
        "id": "tw_3",
        "summary": "Netflix  ·  $15.99  (recurring)",
        "stages": [
            {
                "id": "bank",
                "label": "Bank terminal",
                "sub": "Raw POS descriptor from the issuer",
                "blob": {
                    "postingDate": "2026-05-05T00:00:00Z",
                    "amount": -15.99,
                    "currency": "USD",
                    "description": "NETFLIX.COM 866-579-7172 CA",
                    "merchantId": None,
                },
            },
            {
                "id": "agg",
                "label": "Open Finance aggregation",
                "sub": "GET /aggregation/v3/customers/{id}/transactions",
                "blob": {
                    "id": "9921773901",
                    "amount": -15.99,
                    "accountId": "5011112233",
                    "customerId": "9021080528",
                    "status": "active",
                    "description": "NETFLIX.COM 866-579-7172 CA",
                    "postedDate": 1762304000,
                    "transactionDate": 1762304000,
                    "type": "directDebit",
                },
            },
            {
                "id": "merchant",
                "label": "Merchant Identifier",
                "sub": "POST /merchant-identifier/v1/lookup",
                "blob": {
                    "merchant": {
                        "name": "Netflix",
                        "merchantId": "NFLX-SUB",
                        "logoUrl": "https://logos.mastercard.com/netflix.png",
                        "location": None,
                        "confidence": 1.00,
                        "website": "https://www.netflix.com",
                    },
                },
            },
            {
                "id": "category",
                "label": "Category enrichment",
                "sub": "Recurrence detector + MCC 4899 → streaming",
                "blob": {
                    "category": "Streaming Services",
                    "categoryGroup": "Utilities & Service Charges",
                    "mcc": "4899",
                    "isRecurring": True,
                    "recurrence": {
                        "cadence": "monthly",
                        "nextExpected": "2026-06-05",
                        "averageAmount": -15.99,
                    },
                    "categoryScore": 1.00,
                },
            },
            {
                "id": "app",
                "label": "Your banking app",
                "sub": "What the consumer finally sees",
                "blob": {
                    "title": "Netflix",
                    "subtitle": "Subscription · monthly",
                    "amount": "-$15.99",
                    "icon": "▶",
                    "category": "Streaming",
                    "badge": "RECURRING",
                },
            },
        ],
    },
    {
        "id": "tw_4",
        "summary": "Whole Foods Market  ·  $91.37",
        "stages": [
            {
                "id": "bank",
                "label": "Bank terminal",
                "sub": "Raw POS descriptor from the issuer",
                "blob": {
                    "postingDate": "2026-05-06T11:15:00Z",
                    "amount": -91.37,
                    "currency": "USD",
                    "description": "WHOLEFDS MKT #10452 SFCA",
                    "merchantId": None,
                },
            },
            {
                "id": "agg",
                "label": "Open Finance aggregation",
                "sub": "GET /aggregation/v3/customers/{id}/transactions",
                "blob": {
                    "id": "9921773727",
                    "amount": -91.37,
                    "accountId": "5011112233",
                    "customerId": "9021080528",
                    "status": "active",
                    "description": "WHOLEFDS MKT #10452 SFCA",
                    "postedDate": 1762427700,
                    "transactionDate": 1762427700,
                    "type": "directDebit",
                },
            },
            {
                "id": "merchant",
                "label": "Merchant Identifier",
                "sub": "POST /merchant-identifier/v1/lookup",
                "blob": {
                    "merchant": {
                        "name": "Whole Foods Market",
                        "merchantId": "WFM-SF-10452",
                        "logoUrl": "https://logos.mastercard.com/whole-foods.png",
                        "location": {
                            "city": "San Francisco",
                            "region": "CA",
                            "country": "US",
                            "lat": 37.7749,
                            "lon": -122.4194,
                        },
                        "confidence": 0.98,
                    },
                },
            },
            {
                "id": "category",
                "label": "Category enrichment",
                "sub": "Enrichment service (MCC 5411 → group mapping)",
                "blob": {
                    "category": "Groceries",
                    "categoryGroup": "Groceries & Dining",
                    "mcc": "5411",
                    "isRecurring": False,
                    "isEcommerce": False,
                    "categoryScore": 0.94,
                },
            },
            {
                "id": "app",
                "label": "Your banking app",
                "sub": "What the consumer finally sees",
                "blob": {
                    "title": "Whole Foods Market",
                    "subtitle": "San Francisco, CA · Yesterday",
                    "amount": "-$91.37",
                    "icon": "🛒",
                    "category": "Groceries",
                },
            },
        ],
    },
    {
        "id": "tw_5",
        "summary": "Lyft  ·  $12.50",
        "stages": [
            {
                "id": "bank",
                "label": "Bank terminal",
                "sub": "Raw POS descriptor from the issuer",
                "blob": {
                    "postingDate": "2026-05-04T08:00:00Z",
                    "amount": -12.50,
                    "currency": "USD",
                    "description": "LYFT *RIDE 855-865-9553",
                    "merchantId": None,
                },
            },
            {
                "id": "agg",
                "label": "Open Finance aggregation",
                "sub": "GET /aggregation/v3/customers/{id}/transactions",
                "blob": {
                    "id": "9921773588",
                    "amount": -12.50,
                    "accountId": "5011112233",
                    "customerId": "9021080528",
                    "status": "active",
                    "description": "LYFT *RIDE 855-865-9553",
                    "postedDate": 1762243200,
                    "transactionDate": 1762243200,
                    "type": "directDebit",
                },
            },
            {
                "id": "merchant",
                "label": "Merchant Identifier",
                "sub": "POST /merchant-identifier/v1/lookup",
                "blob": {
                    "merchant": {
                        "name": "Lyft",
                        "merchantId": "LYFT-CORP",
                        "logoUrl": "https://logos.mastercard.com/lyft.png",
                        "location": None,
                        "confidence": 0.99,
                        "website": "https://lyft.com",
                    },
                },
            },
            {
                "id": "category",
                "label": "Category enrichment",
                "sub": "Enrichment service (MCC 4121 → group mapping)",
                "blob": {
                    "category": "Rental Car & Taxi",
                    "categoryGroup": "Travel & Vacation",
                    "mcc": "4121",
                    "isRecurring": False,
                    "isEcommerce": True,
                    "categoryScore": 0.97,
                },
            },
            {
                "id": "app",
                "label": "Your banking app",
                "sub": "What the consumer finally sees",
                "blob": {
                    "title": "Lyft",
                    "subtitle": "Ride · 3 days ago",
                    "amount": "-$12.50",
                    "icon": "🚗",
                    "category": "Transport",
                },
            },
        ],
    },
    {
        "id": "tw_6",
        "summary": "PG&E  ·  $142.18  (recurring)",
        "stages": [
            {
                "id": "bank",
                "label": "Bank terminal",
                "sub": "Raw ACH descriptor from the issuer",
                "blob": {
                    "postingDate": "2026-05-02T03:00:00Z",
                    "amount": -142.18,
                    "currency": "USD",
                    "description": "ACH DEBIT PGANDE WEBPAY 5550012",
                    "merchantId": None,
                },
            },
            {
                "id": "agg",
                "label": "Open Finance aggregation",
                "sub": "GET /aggregation/v3/customers/{id}/transactions",
                "blob": {
                    "id": "9921773201",
                    "amount": -142.18,
                    "accountId": "5011112233",
                    "customerId": "9021080528",
                    "status": "active",
                    "description": "ACH DEBIT PGANDE WEBPAY 5550012",
                    "postedDate": 1762056000,
                    "transactionDate": 1762056000,
                    "type": "ach",
                },
            },
            {
                "id": "merchant",
                "label": "Merchant Identifier",
                "sub": "POST /merchant-identifier/v1/lookup",
                "blob": {
                    "merchant": {
                        "name": "Pacific Gas & Electric",
                        "merchantId": "PGE-UTIL",
                        "logoUrl": "https://logos.mastercard.com/pge.png",
                        "location": None,
                        "confidence": 0.94,
                        "website": "https://www.pge.com",
                    },
                },
            },
            {
                "id": "category",
                "label": "Category enrichment",
                "sub": "Recurrence detector + MCC 4900 → utilities",
                "blob": {
                    "category": "Utilities",
                    "categoryGroup": "Bills & Utilities",
                    "mcc": "4900",
                    "isRecurring": True,
                    "recurrence": {
                        "cadence": "monthly",
                        "nextExpected": "2026-06-02",
                        "averageAmount": -138.74,
                    },
                    "categoryScore": 0.91,
                },
            },
            {
                "id": "app",
                "label": "Your banking app",
                "sub": "What the consumer finally sees",
                "blob": {
                    "title": "Pacific Gas & Electric",
                    "subtitle": "Utility bill · monthly",
                    "amount": "-$142.18",
                    "icon": "⚡",
                    "category": "Utilities",
                    "badge": "RECURRING",
                },
            },
        ],
    },
]

def get_data(customer_id: str) -> dict[str, Any]:
    """Return the curated journeys.

    ``customer_id`` is accepted for API symmetry with other use cases but
    is not used — the data is hand-curated so the demo is fully offline-
    capable.  A future iteration could substitute live transactions
    pulled via Open Finance + Merchant Identifier here.
    """
    return {"transactions": _JOURNEYS, "customer_id": customer_id}
