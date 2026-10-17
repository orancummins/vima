"""Barclays PLC.

The page (``Barclays_Platform.html``) reads Britain's first card issuer as
five discs, Foundation to Access, with the divisions it reports (Barclays UK,
UK Corporate Bank, Private Bank & Wealth Management, Investment Bank, US
Consumer Bank), a Mastercard lens (Visa at home, Mastercard on most US
partner cards, Avios and Tesco) and ten journeys, two of them for Mastercard.
Public sources as at 17 October 2026; the research behind it is in
``Barclays_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``barclays_inventory.py`` and ``barclays_story.py``::

    python customers/build_page.py barclays
"""

CUSTOMER = {
    "id": "barclays",
    "order": 120,
    "name": "Barclays",
    "short": "Barclays",
    "brands": ["Barclays", "Barclaycard", "Tesco Bank", "Kensington", "Best Egg"],
    "country": "United Kingdom",
    "region": "Europe & Americas",
    "accent": "#00aeef",   # Barclays blue, on the Customers tab card
    "as_of": "17 October 2026",
    "tagline": "Britain's first card issuer as five discs: £1.7 trillion of assets and a Visa bank at home, with "
               "Mastercard on most US partner cards, the Avios cards and Tesco Bank.",
    "stats": [
        {"label": "Assets", "value": "£1.7tn"},
        {"label": "RoTE H1 2026", "value": "14.8%"},
        {"label": "UK customers", "value": "20m+"},
        {"label": "US partners", "value": "20"},
    ],
    "page": "Barclays_Platform.html",
    "notes": (
        ("Research notes", "Barclays_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "barclaycard": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"],
                        "use_cases": ["consumer_clarity", "recurring"], "bundles": ["issuer_toolkit"]},
        "avios": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator", "priceless_cities"],
                  "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "tesco": {"apis": ["offers_for_publishers", "offers_merchant_content", "bin_lookup"],
                  "use_cases": ["findacard"], "bundles": ["loyalty_stack", "issuer_toolkit"]},
        "usmc": {"apis": ["benefits_eligibility", "consumer_clarity", "bin_lookup"],
                 "use_cases": ["consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "bcpayments": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"],
                       "bundles": ["acquirer_risk", "merchant_resolution"]},
        "commcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "txbanking": {"apis": ["enhanced_currency_conversion_calculator"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "loyalty": {"apis": ["offers_for_publishers", "priceless_cities"], "use_cases": ["specials"],
                    "bundles": ["loyalty_stack"]},
        "agentic": {"apis": ["bin_lookup"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L4 Business lines
        "accounts": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"],
                     "bundles": ["pfm_stack"]},
        "mortgages": {"apis": ["open_finance_eu"]},
        "bizbank": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("subscriptions", "acquirer_risk", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack",),
        "credit": ("issuer_toolkit", "loyalty_stack"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "us": ("issuer_toolkit",),
    },
}
