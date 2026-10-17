"""Nordea Bank Abp.

The page (``Nordea_Platform.html``) reads the Nordics' largest bank group as
five discs, Foundation to Access, with the business areas it reports
(Personal Banking, Business Banking, Large Corporates & Institutions, Asset &
Wealth Management), a Mastercard lens (Visa for every day, Mastercard for
credit and the first agent) and nine journeys, two of them for Mastercard.
Public sources as at 17 October 2026; the research behind it is in
``Nordea_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``nordea_inventory.py`` and ``nordea_story.py``::

    python customers/build_page.py nordea
"""

CUSTOMER = {
    "id": "nordea",
    "order": 530,
    "name": "Nordea",
    "short": "Nordea",
    "brands": ["Nordea", "Nordea Life & Pension", "Nordea Asset Management", "Nordea Finance", "First Card", "Gimi"],
    "country": "Finland",
    "region": "Europe",
    "accent": "#0000a0",   # Nordea blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Nordea", "bg": "#ffffff", "source": "https://www.nordea.com/themes/custom/nordea_theme/logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The Nordics' largest bank group as five discs: four countries on one platform, Visa on every debit "
               "card and Mastercard on every credit card, and Finland's first agent payment run with Mastercard.",
    "stats": [
        {"label": "Loans", "value": "€400bn"},
        {"label": "AuM", "value": "€509bn"},
        {"label": "ROE Q3 2026", "value": "15.1%"},
        {"label": "Digital users", "value": "5m"},
    ],
    "page": "Nordea_Platform.html",
    "notes": (
        ("Research notes", "Nordea_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debitse": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "gold": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                 "bundles": ["issuer_toolkit"]},
        "premium": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"], "use_cases": ["specials"],
                    "bundles": ["loyalty_stack"]},
        "bizmc": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "agentpay": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["identity", "enrichment"]},
        "insights": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "mcob": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "cashback": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "sme": {"apis": ["business_payment_controls", "open_finance_eu"], "bundles": ["issuer_toolkit"]},
        "mortgages": {"apis": ["open_finance_eu", "carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "credit": ("loyalty_stack",),
    },
}
