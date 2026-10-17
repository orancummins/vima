"""Revolut.

The page (``Revolut_Platform.html``) reads Europe's most valuable fintech as
five discs, Foundation to Access, with its business lines (Retail, Business,
Wealth and crypto, Credit), a Mastercard lens (launch partner, sharing the
card book with Visa) and ten journeys, two of them for Mastercard. Revolut is
private: figures are its 2025 annual report, regulators and press, as at
17 October 2026; the research behind it is in ``Revolut_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``revolut_inventory.py`` and ``revolut_story.py``::

    python customers/build_page.py revolut
"""

CUSTOMER = {
    "id": "revolut",
    "order": 300,
    "name": "Revolut",
    "short": "Revolut",
    "brands": ["Revolut", "Revolut Business", "Revolut Pay", "Revolut X", "AIR"],
    "country": "United Kingdom",
    "region": "Global",
    "accent": "#191c1f",   # Revolut black, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Revolut", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:Revolut_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Europe's most valuable fintech as five discs: 80 million customers, $2.3 billion of profit and new "
               "bank licences, with Mastercard and Visa sharing its cards and Revolut Pay taking checkout off both.",
    "stats": [
        {"label": "Customers", "value": "80m+"},
        {"label": "Revenue 2025", "value": "$6.0bn"},
        {"label": "Profit before tax", "value": "$2.3bn"},
        {"label": "Valuation (reported)", "value": "$115bn"},
    ],
    "page": "Revolut_Platform.html",
    "notes": (
        ("Research notes", "Revolut_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "cards": {"apis": ["bin_lookup", "transaction_notifications", "consumer_clarity"],
                  "use_cases": ["txnotify", "consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "payouts": {"apis": ["enhanced_currency_conversion_calculator"]},
        "fx": {"apis": ["enhanced_currency_conversion_calculator"]},
        "acquiring": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"],
                      "bundles": ["acquirer_risk"]},
        "revpay": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L3 Services
        "protection": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "air": {"apis": ["bin_lookup", "consumer_clarity"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "revpoints": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"],
                      "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "accounts": {"apis": ["consumer_clarity", "merchant_identifier", "automatic_billing_updater"],
                     "use_cases": ["pfm", "enrichment", "recurring"], "bundles": ["pfm_stack", "subscriptions"]},
        "business": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("subscriptions", "issuer_toolkit", "merchant_resolution"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "everyday": ("pfm_stack", "loyalty_stack"),
        "merchant": ("acquirer_risk",),
        "agent": ("subscriptions",),
    },
}
