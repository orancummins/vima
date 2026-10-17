"""Standard Chartered PLC.

The page (``Standard_Chartered_Platform.html``) reads the international bank
for Asia, Africa and the Middle East as five discs, Foundation to Access, with
the segments it reports (Corporate & Investment Banking, Wealth & Retail
Banking, Central & other items), a Mastercard lens (Mastercard in Hong Kong,
Pakistan and Mox, Visa almost everywhere else) and nine journeys, two of them
for Mastercard. Public sources as at 17 October 2026; the research behind it
is in ``Standard_Chartered_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``stanchart_inventory.py`` and ``stanchart_story.py``::

    python customers/build_page.py stanchart
"""

CUSTOMER = {
    "id": "stanchart",
    "order": 1510,
    "name": "Standard Chartered",
    "short": "StanChart",
    "brands": ["Standard Chartered", "Mox", "Trust Bank", "Saadiq", "SC Ventures", "Zodia"],
    "country": "United Kingdom",
    "region": "Global",
    "type": "bank",
    "accent": "#0473ea",   # Standard Chartered blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Standard Chartered", "bg": "#ffffff", "source": "https://www.sc.com/en/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "An international bank for Asia, Africa and the Middle East as five discs: 55 markets, Mastercard in Hong "
               "Kong, Pakistan and Mox, Visa in most other markets, and stablecoins on its own rails.",
    "stats": [
        {"label": "Markets", "value": "55"},
        {"label": "Total assets", "value": "$993bn"},
        {"label": "RoTE H1 2026", "value": "17.6%"},
        {"label": "Affluent NNM H1", "value": "$33bn"},
    ],
    "page": "Standard_Chartered_Platform.html",
    "notes": (
        ("Research notes", "Standard_Chartered_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "hkcathay": {"apis": ["bin_lookup", "priceless_cities", "benefits_eligibility"], "use_cases": ["findacard", "specials"],
                     "bundles": ["loyalty_stack", "issuer_toolkit"]},
        "sgmc": {"apis": ["consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"], "bundles": ["issuer_toolkit"]},
        "pkcards": {"apis": ["benefits_eligibility", "priceless_cities", "business_payment_controls"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "moxcard": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications", "consumer_clarity"],
                    "use_cases": ["txnotify", "pfm"], "bundles": ["pfm_stack"]},
        "mcsend": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "payments": {"apis": ["merchant_identifier", "open_finance"], "use_cases": ["identity"], "bundles": ["merchant_resolution"]},
        # L3 Services
        "fincrime": {"apis": ["transaction_notifications", "match"], "use_cases": ["txnotify", "identity"], "bundles": ["acquirer_risk"]},
        "wealthai": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "retail": {"apis": ["business_payment_controls", "bin_lookup"], "use_cases": ["bin_lookup"], "bundles": ["issuer_toolkit"]},
        "cib": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "issuer_toolkit", "merchant_resolution"),
        "mcnow": ("issuer_toolkit", "loyalty_stack", "pfm_stack"),
        "wealth": ("loyalty_stack",),
        "digital": ("pfm_stack",),
        "corp": ("sustainability", "merchant_resolution"),
    },
}
