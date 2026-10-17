"""Shinhan Card Co., Ltd.

The page (``Shinhan_Card_Platform.html``) reads Shinhan Financial Group's card
company as five discs, Foundation to Access, with the business it reports
(card business, card loans and consumer finance, lease and instalment
finance, overseas), a Mastercard lens (the default overseas brand on new
cards, Agent Pay, but domestic spend on Korean rails) and ten journeys, two of
them for Mastercard. Public sources as at 17 October 2026; the research
behind it is in ``Shinhan_Card_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``shinhancard_inventory.py`` and ``shinhancard_story.py``::

    python customers/build_page.py shinhancard
"""

CUSTOMER = {
    "id": "shinhancard",
    "order": 740,
    "name": "Shinhan Card",
    "short": "Shinhan Card",
    "brands": ["Shinhan Card", "SOL Pay", "Plan series", "SOL Travel", "Shinhan MyCar", "Shinhan Vietnam Finance"],
    "country": "South Korea",
    "region": "Asia-Pacific",
    "type": "issuer",
    "accent": "#0040f8",   # Shinhan blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Shinhan Card", "bg": "#ffffff",
         "source": "https://www.shinhancard.com/pconts/company/images/common/shcard_logo01.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Korea's number-two card company by H1 2026 profit as five discs: Mastercard on the overseas version of its "
               "new cards and on SOL Travel, partner for Korea's first Agent Pay, but domestic spend on Korean rails.",
    "stats": [
        {"label": "Net income H1 2026", "value": "₩253bn"},
        {"label": "Volume 2025", "value": "₩236tn"},
        {"label": "Cardholders", "value": "28m"},
        {"label": "SOL Travel cards", "value": "3m"},
    ],
    "page": "Shinhan_Card_Platform.html",
    "notes": (
        ("Research notes", "Shinhan_Card_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "plan": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                 "bundles": ["issuer_toolkit"]},
        "bestx": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "soltravel": {"apis": ["enhanced_currency_conversion_calculator", "offers_for_publishers"], "use_cases": ["settle_in", "specials"],
                      "bundles": ["loyalty_stack"]},
        "applepay": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring", "bin_lookup"], "bundles": ["subscriptions"]},
        "agentpay": {"apis": ["merchant_identifier", "transaction_notifications"], "use_cases": ["identity", "txnotify"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "solfds": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "mydata": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "plcc": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "biz": {"apis": ["business_payment_controls", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "myshop": {"apis": ["merchant_identifier", "places"], "use_cases": ["places", "psi"], "bundles": ["merchant_resolution"]},
        "trippass": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "subscriptions", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "travel": ("loyalty_stack",),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "merch": ("merchant_resolution",),
    },
}
