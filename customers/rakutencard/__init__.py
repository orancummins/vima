"""Rakuten Card Co., Ltd.

The page (``Rakuten_Card_Platform.html``) reads Japan's biggest card issuer as
five discs, Foundation to Access, with Rakuten's FinTech businesses as the
reported segments, a Mastercard lens (one of four brands, with Visa taking the
new launches) and ten journeys, two of them for Mastercard. Public sources as
at 17 October 2026; the research behind it is in
``Rakuten_Card_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``rakutencard_inventory.py`` and ``rakutencard_story.py``::

    python customers/build_page.py rakutencard
"""

CUSTOMER = {
    "id": "rakutencard",
    "order": 720,
    "name": "Rakuten Card",
    "short": "Rakuten Card",
    "brands": ["Rakuten Card", "Rakuten Premium Card", "Rakuten Black Card", "Rakuten Business Card", "Mizuho Rakuten Card"],
    "country": "Japan",
    "region": "Asia-Pacific",
    "accent": "#bf0000",   # Rakuten crimson, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Rakuten Card", "bg": "#ffffff",
         "source": "https://commons.wikimedia.org/wiki/File:Rakuten_Card_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Japan's biggest card issuer as five discs: 34 million cards on Visa, Mastercard, JCB and Amex, "
               "owned by Rakuten Bank since October 2026, with Visa taking the new launches.",
    "stats": [
        {"label": "Cards issued", "value": "34.3m"},
        {"label": "Spend 2025", "value": "¥26.5tn"},
        {"label": "Card brands", "value": "4"},
        {"label": "Q2 2026 GTV growth", "value": "+9.4%"},
    ],
    "page": "Rakuten_Card_Platform.html",
    "notes": (
        ("Research notes", "Rakuten_Card_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "classic": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["pfm", "txnotify"], "bundles": ["pfm_stack"]},
        "black": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator", "priceless_cities"],
                  "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "netmc": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["bin_lookup", "recurring"], "bundles": ["issuer_toolkit"]},
        "acquiring": {"apis": ["match", "merchant_identifier"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "revolving": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "identity"], "bundles": ["issuer_toolkit"]},
        "aiagent": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "points": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "corporate": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        "bizplat": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["pfm", "txnotify"], "bundles": ["pfm_stack", "subscriptions"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "pfm_stack", "sustainability"),
        "mcnow": ("issuer_toolkit", "acquirer_risk", "loyalty_stack"),
        "everyday": ("pfm_stack", "loyalty_stack"),
        "merch": ("acquirer_risk", "merchant_resolution"),
        "travel": ("loyalty_stack",),
    },
}
