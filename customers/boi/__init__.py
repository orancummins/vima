"""Bank of Ireland (Bank of Ireland Group plc).

The page (``Bank_of_Ireland_Platform.html``) reads Ireland's oldest bank as
five discs, Foundation to Access, with the segments it reports (Retail
Ireland, Wealth and Insurance, Retail UK, Corporate and Commercial), a
Mastercard lens (credit cards on Mastercard since 2015, debit on Visa) and
ten journeys, two of them for Mastercard. Public sources as at 17 October
2026; the research behind it is in ``Bank_of_Ireland_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``boi_foundation.py``,
``boi_inventory.py`` and ``boi_story.py``::

    python customers/build_page.py boi
"""

CUSTOMER = {
    "id": "boi",
    "order": 50,
    "name": "Bank of Ireland",
    "short": "BOI",
    "brands": ["Bank of Ireland", "Davy", "New Ireland", "Bank of Ireland UK"],
    "country": "Ireland",
    "region": "Europe",
    "accent": "#0047bb",   # Bank of Ireland blue, on the Customers tab card
    "as_of": "17 October 2026",
    "tagline": "Ireland's oldest bank as five discs: 42% of new mortgages, half of SME lending and Ireland's "
               "largest wealth manager, with every credit card on Mastercard and every debit card on Visa.",
    "stats": [
        {"label": "Assets", "value": "€169bn"},
        {"label": "Customers", "value": "4m+"},
        {"label": "New mortgages", "value": "42%"},
        {"label": "Mastercard credit", "value": "since 2015"},
    ],
    "page": "Bank_of_Ireland_Platform.html",
    "notes": (
        ("Research notes", "Bank_of_Ireland_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "visadebit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "creditcards": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"],
                        "use_cases": ["bin_lookup", "consumer_clarity", "recurring"], "bundles": ["issuer_toolkit"]},
        "aercard": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator"]},
        "bizcredit": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "boipa": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "markets": {"apis": ["enhanced_currency_conversion_calculator"]},
        "firstrate": {"apis": ["enhanced_currency_conversion_calculator"]},
        # L3 Services
        "onboarding": {"apis": ["open_finance_eu"], "use_cases": ["settle_in", "identity"]},
        "fraudai": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "openbanking": {"apis": ["open_finance_eu"], "use_cases": ["enrichment"], "bundles": ["pfm_stack"]},
        "priceless": {"apis": ["priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "cashback": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard"],
                     "bundles": ["loyalty_stack"]},
        "green": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        # L4 Business lines
        "pca": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"],
                "bundles": ["pfm_stack"]},
        "smartstart": {"use_cases": ["pfm"]},
        "mortgages": {"apis": ["open_finance_eu"]},
        # L5 Access
        "contact": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("merchant_resolution", "loyalty_stack", "sustainability", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack",),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "wealth": ("loyalty_stack",),
    },
}
