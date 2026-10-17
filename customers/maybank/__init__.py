"""Malayan Banking Berhad (Maybank).

The page (``Maybank_Platform.html``) reads Malaysia's largest bank as five
discs, Foundation to Access, with the segments it reports (Community
Financial Services, Global Banking, Insurance & Takaful), a Mastercard lens
(one of three networks at Malaysia's largest card issuer, as DuitNow QR takes
the growth) and nine journeys, two of them for Mastercard. Public sources as
at 17 October 2026; the research behind it is in
``Maybank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``maybank_inventory.py`` and ``maybank_story.py``::

    python customers/build_page.py maybank
"""

CUSTOMER = {
    "id": "maybank",
    "order": 780,
    "name": "Maybank",
    "short": "Maybank",
    "brands": ["Maybank", "Maybank Islamic", "MAE", "Maybank2u", "Maybank Singapore", "Maybank Indonesia", "Etiqa",
               "Maybank Investment Bank"],
    "country": "Malaysia",
    "region": "Asia-Pacific",
    "accent": "#ffc70a",   # Maybank yellow, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Maybank", "bg": "#ffc70a",
         "source": "https://www.maybank.com/iwov-resources/images/icons/maybank_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Malaysia's largest bank as five discs: cards on Visa, Mastercard and Amex, World Elite and the Islamic "
               "range on Mastercard, the Grab card gone, and DuitNow QR in MAE doubling.",
    "stats": [
        {"label": "Loans", "value": "RM696bn"},
        {"label": "2Q26 net profit", "value": "RM2.69bn"},
        {"label": "Digital users", "value": "10.7m"},
        {"label": "Cross-border 1H26", "value": "RM465bn"},
    ],
    "page": "Maybank_Platform.html",
    "notes": (
        ("Research notes", "Maybank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "ccmc": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                 "bundles": ["issuer_toolkit"]},
        "grabnext": {"apis": ["offers_for_publishers", "offers_merchant_content", "automatic_billing_updater"],
                     "use_cases": ["specials", "recurring"], "bundles": ["loyalty_stack", "subscriptions"]},
        "nadi": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "xborder": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["bin_lookup"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "ai": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "treats": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "wemc": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "sgcards": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility"], "use_cases": ["findacard"]},
        "travelpass": {"apis": ["benefits_eligibility", "places"], "use_cases": ["places"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "loyalty_stack", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack",),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "wealth": ("loyalty_stack",),
    },
}
