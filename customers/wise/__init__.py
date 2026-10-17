"""Wise Group plc.

The page (``Wise_Platform.html``) reads the cross-border money network as
five discs, Foundation to Access, with its revenue lines (cross-border, card,
other transactions, interest), a Mastercard lens (Mastercard launched the
card, Visa now carries it) and ten journeys, two of them for Mastercard.
Public sources as at 17 October 2026; the research behind it is in
``Wise_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``wise_inventory.py`` and ``wise_story.py``::

    python customers/build_page.py wise
"""

CUSTOMER = {
    "id": "wise",
    "order": 1350,
    "name": "Wise",
    "short": "Wise",
    "brands": ["Wise", "Wise Business", "Wise Platform", "Wise Assets"],
    "country": "United Kingdom",
    "region": "Global",
    "type": "wallet",
    "accent": "#9fe870",   # Wise bright green, from wise.com (the wordmark itself is forest green #163300)
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Wise", "bg": "#ffffff", "source": "https://wise.com/gb/about/our-story"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A cross-border money network as five discs: $243 billion of transfers on its own rails, now listed "
               "on Nasdaq, with a debit card Mastercard launched and Visa now carries.",
    "stats": [
        {"label": "Active customers FY26", "value": "18.9m"},
        {"label": "Cross-border volume FY26", "value": "$243bn"},
        {"label": "Net revenue FY26", "value": "$2.5bn"},
        {"label": "Card spend FY26", "value": "$43.6bn"},
    ],
    "page": "Wise_Platform.html",
    "notes": (
        ("Research notes", "Wise_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "card": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications", "bin_lookup"],
                 "use_cases": ["txnotify", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "digital": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "bizcard": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        "xborder": {"apis": ["enhanced_currency_conversion_calculator"]},
        "receive": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "mcsend": {"apis": ["enhanced_currency_conversion_calculator", "bin_lookup"], "use_cases": ["bin_lookup"]},
        # L3 Services
        "fincrime": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["identity", "consumer_clarity"],
                     "bundles": ["merchant_resolution"]},
        "accounting": {"apis": ["merchant_identifier"], "use_cases": ["enrichment"]},
        "cashback": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "account": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
        "platcards": {"apis": ["bin_lookup", "business_payment_controls"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "merchant_resolution", "loyalty_stack"),
        "mcnow": ("issuer_toolkit",),
        "spend": ("pfm_stack", "issuer_toolkit"),
        "biz": ("issuer_toolkit", "loyalty_stack", "sustainability"),
        "issue": ("issuer_toolkit",),
    },
}
