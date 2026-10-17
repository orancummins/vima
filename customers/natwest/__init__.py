"""NatWest Group plc.

The page (``NatWest_Group_Platform.html``) reads the UK's largest bank for
business as five discs, Foundation to Access, with the segments it reports
(Retail Banking, Private Banking & Wealth Management, Commercial &
Institutional), a Mastercard lens (16 million debit cards and most credit
cards on Mastercard, with Visa at the edges) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``NatWest_Group_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``natwest_inventory.py``
and ``natwest_story.py``::

    python customers/build_page.py natwest
"""

CUSTOMER = {
    "id": "natwest",
    "order": 130,
    "name": "NatWest Group",
    "short": "NatWest",
    "brands": ["NatWest", "Royal Bank of Scotland", "Ulster Bank", "Coutts", "Mettle", "Tyl"],
    "country": "United Kingdom",
    "region": "Europe",
    "type": "bank",
    "accent": "#3c1053",   # NatWest purple, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "NatWest", "bg": "#3c1053", "source": "https://www.natwest.com/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The UK's largest bank for business as five discs: £745 billion of assets, private again since 2025, "
               "with 16 million debit cards on Mastercard and Visa first to its agentic payments.",
    "stats": [
        {"label": "Assets", "value": "£745bn"},
        {"label": "Customers", "value": "20m+"},
        {"label": "RoTE H1 2026", "value": "19.7%"},
        {"label": "Mastercard debit", "value": "16m cards"},
    ],
    "page": "NatWest_Group_Platform.html",
    "notes": (
        ("Research notes", "NatWest_Group_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mcdebit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"],
                    "bundles": ["issuer_toolkit"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater", "benefits_eligibility"],
                   "use_cases": ["consumer_clarity", "recurring"], "bundles": ["issuer_toolkit"]},
        "travelreward": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility"]},
        "tyl": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "payit": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "bankline": {"apis": ["enhanced_currency_conversion_calculator"]},
        "approval2buy": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "cfr": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "spendingchat": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"],
                         "bundles": ["pfm_stack"]},
        "agentic": {"apis": ["bin_lookup"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "loyalty": {"apis": ["easy_savings", "offers_for_publishers", "priceless_cities"], "use_cases": ["specials"],
                    "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "accounts": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"],
                     "bundles": ["pfm_stack"]},
        "youth": {"use_cases": ["pfm"]},
        "mortgages": {"apis": ["open_finance_eu"]},
        "smebank": {"apis": ["easy_savings", "business_payment_controls"], "bundles": ["loyalty_stack"]},
        "climatefin": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        # L5 Access
        "mettle": {"apis": ["easy_savings"]},
        "apps": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("subscriptions", "pfm_stack", "acquirer_risk", "sustainability"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "loyalty_stack"),
        "corp": ("issuer_toolkit",),
        "green": ("sustainability",),
    },
}
