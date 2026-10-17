"""BMO Financial Group (Bank of Montreal).

The page (``BMO_Platform.html``) reads Canada's first bank as five discs,
Foundation to Access, with the segments it reports (Canadian P&C, U.S. Banking,
Wealth Management, BMO Capital Markets, Corporate Services), a Mastercard lens
(a Mastercard bank with a Visa premium line and Interac debit) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``BMO_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``bmo_inventory.py``
and ``bmo_story.py``::

    python customers/build_page.py bmo
"""

CUSTOMER = {
    "id": "bmo",
    "order": 160,
    "name": "BMO Financial Group",
    "short": "BMO",
    "brands": ["BMO", "BMO Bank N.A.", "Blue Rewards", "BMO Nesbitt Burns", "BMO InvestorLine", "BMO Capital Markets",
               "Burgundy Asset Management", "Moneris"],
    "country": "Canada",
    "region": "Americas",
    "accent": "#0079c1",   # BMO blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "BMO", "bg": "#ffffff",
         "source": "static/logos/financial-logos-500/01-financial-institutions/bmo.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Canada's first bank as five discs: most of its credit cards, all its commercial cards and its US cards on "
               "Mastercard, a premium line on Visa, debit on Interac, and a new loyalty coalition in Blue Rewards.",
    "stats": [
        {"label": "Assets", "value": "C$1.54tn"},
        {"label": "Clients", "value": "13m"},
        {"label": "Adj. ROE Q3 2026", "value": "14.0%"},
        {"label": "Blue Rewards brands", "value": "400+"},
    ],
    "page": "BMO_Platform.html",
    "notes": (
        ("Research notes", "BMO_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "bluecard": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "viporter": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "commercial": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        "commexpress": {"apis": ["business_payment_controls", "merchant_identifier"], "use_cases": ["enrichment"]},
        "debitmc": {"apis": ["transaction_notifications", "enhanced_currency_conversion_calculator"], "use_cases": ["txnotify"]},
        "usdebit": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "globalpay": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "moneris": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "bluerewards": {"apis": ["offers_for_publishers", "offers_merchant_content", "places"], "use_cases": ["specials", "places"],
                        "bundles": ["loyalty_stack"]},
        "pushprov": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["bin_lookup", "recurring"], "bundles": ["subscriptions"]},
        "controls": {"apis": ["consumer_clarity", "merchant_identifier", "transaction_notifications"], "use_cases": ["consumer_clarity", "enrichment"],
                     "bundles": ["merchant_resolution"]},
        "lumi": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "merchant_resolution", "subscriptions"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "rewards": ("loyalty_stack",),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "everyday": ("pfm_stack", "merchant_resolution"),
    },
}
