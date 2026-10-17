"""Erste Group Bank AG and Erste Bank der oesterreichischen Sparkassen AG.

The page (``Erste_Bank_Platform.html``) reads Austria's savings-bank group as
five discs, Foundation to Access, with the segments it reports (Erste Bank
Oesterreich, the Savings Banks, Other Austria, Central & Eastern Europe and
Poland), a Mastercard lens (Mastercard debit in every Austrian wallet, credit
split with Visa, Wero at the door) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``Erste_Bank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``erste_inventory.py`` and
``erste_story.py``::

    python customers/build_page.py erste
"""

CUSTOMER = {
    "id": "erste",
    "order": 540,
    "name": "Erste Bank",
    "short": "Erste",
    "brands": ["Erste Group", "Erste Bank Oesterreich", "Sparkassen", "George", "Erste Bank Polska", "Erste Asset Management"],
    "country": "Austria",
    "region": "Europe",
    "type": "bank",
    "accent": "#2870ed",   # Erste blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Erste Bank", "bg": "#2870ed",
         "source": "https://cdn.erstegroup.com/content/dam/at/eh/common/pictures/logos/eboe/EBOe_Special_screen_RGB.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Austria's savings-bank group as five discs: 23 million customers in eight markets, Debit Mastercard on "
               "every Austrian account, credit split with Visa, and a new stake in Wero.",
    "stats": [
        {"label": "Customers", "value": "23.2m"},
        {"label": "Loans", "value": "€283bn"},
        {"label": "ROTE H1 2026", "value": "19.6%"},
        {"label": "George users", "value": "11.8m+"},
    ],
    "page": "Erste_Bank_Platform.html",
    "notes": (
        ("Research notes", "Erste_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit", "subscriptions"]},
        "miles": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility", "priceless_cities"], "use_cases": ["findacard", "specials"],
                  "bundles": ["loyalty_stack"]},
        "accept": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "wero": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L3 Services
        "psd2": {"apis": ["open_finance_eu"], "use_cases": ["identity", "pfm"], "bundles": ["pfm_stack"]},
        "heygeorge": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "moneyback": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "georgefit": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "virtual": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "housing": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "issuer_toolkit", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "card": ("issuer_toolkit", "subscriptions"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
    },
}
