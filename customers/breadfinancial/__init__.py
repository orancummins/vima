"""Bread Financial Holdings, Inc.

The page (``Bread_Financial_Platform.html``) reads a US private-label and
co-brand card issuer as five discs, Foundation to Access, with its product
lines (co-brand, private label, direct to consumer, Bread Pay), a Mastercard
lens (Mastercard on the biggest brands, Visa winning the new ones) and nine
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``Bread_Financial_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``breadfinancial_inventory.py`` and ``breadfinancial_story.py``::

    python customers/build_page.py breadfinancial
"""

CUSTOMER = {
    "id": "breadfinancial",
    "order": 1240,
    "name": "Bread Financial",
    "short": "Bread Financial",
    "brands": ["Bread Financial", "Comenity", "Bread Pay", "Bread Savings", "Bread Cashback"],
    "country": "United States",
    "region": "Americas",
    "type": "issuer",
    "accent": "#13294b",   # Bread navy, from the website
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Bread Financial", "bg": "#13294b",
         "source": "https://www.breadfinancial.com/content/dam/breadfinancial/us/en/images/Header-and-Footer/Bread%20Logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A US private-label and co-brand card issuer as five discs: $18.5 billion of loans for about 100 brands, "
               "with Victoria's Secret and Ulta on Mastercard and the newest co-brands on Visa.",
    "stats": [
        {"label": "Loans", "value": "$18.5bn"},
        {"label": "Credit sales 2025", "value": "$27.8bn"},
        {"label": "Open accounts", "value": "34m"},
        {"label": "Net loss rate 2Q26", "value": "6.98%"},
    ],
    "page": "Bread_Financial_Platform.html",
    "notes": (
        ("Research notes", "Bread_Financial_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "privatelabel": {"apis": ["bin_lookup"], "use_cases": ["bin_lookup"]},
        "mccobrand": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater", "benefits_eligibility"],
                      "use_cases": ["consumer_clarity", "recurring"], "bundles": ["issuer_toolkit"]},
        "vsmc": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"],
                 "bundles": ["loyalty_stack"]},
        "splitpay": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "wallets": {"apis": ["bin_lookup", "transaction_notifications"], "use_cases": ["txnotify"]},
        # L3 Services
        "underwriting": {"apis": ["open_finance"], "use_cases": ["identity", "enrichment"]},
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"], "bundles": ["issuer_toolkit"]},
        "loyalty": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"],
                    "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "agentic": {"apis": ["bin_lookup"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L4 Business lines
        "savings": {"apis": ["open_finance"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["consumer_clarity", "txnotify"],
                "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("subscriptions", "loyalty_stack", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "beauty": ("loyalty_stack",),
        "save": ("pfm_stack",),
        "smb": ("subscriptions",),
    },
}
