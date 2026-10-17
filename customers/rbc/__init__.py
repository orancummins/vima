"""Royal Bank of Canada (RBC).

The page (``RBC_Platform.html``) reads Canada's biggest bank as five discs,
Foundation to Access, with the segments it reports (Personal Banking,
Commercial Banking, Wealth Management, Insurance, Capital Markets), a
Mastercard lens (a Visa bank where Mastercard keeps the WestJet and cash back
cards) and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in ``RBC_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``rbc_inventory.py``
and ``rbc_story.py``::

    python customers/build_page.py rbc
"""

CUSTOMER = {
    "id": "rbc",
    "order": 1190,
    "name": "RBC",
    "short": "RBC",
    "brands": ["RBC Royal Bank", "Avion Rewards", "RBC Dominion Securities", "RBC Wealth Management", "City National Bank",
               "RBC Bank", "RBC Capital Markets", "RBC Insurance", "Moneris"],
    "country": "Canada",
    "region": "Americas",
    "type": "bank",
    "accent": "#0059b3",   # RBC blue, from the shield logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "RBC", "bg": "#ffffff",
         "source": "https://www.rbcroyalbank.com/dvl/v1.0/assets/images/logos/rbc-logo-shield.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Canada's biggest bank as five discs: Avion, commercial and US cards on Visa, debit on Interac, the WestJet and "
               "cash back cards on Mastercard, and its own Avion Rewards running across them all.",
    "stats": [
        {"label": "Assets", "value": "C$2.5tn"},
        {"label": "Clients", "value": "19m+"},
        {"label": "ROE Q3 2026", "value": "17.9%"},
        {"label": "Card spend FY25", "value": "C$197bn"},
    ],
    "page": "RBC_Platform.html",
    "notes": (
        ("Research notes", "RBC_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "westjet": {"apis": ["benefits_eligibility", "priceless_cities", "automatic_billing_updater"], "use_cases": ["findacard", "recurring"],
                    "bundles": ["loyalty_stack", "issuer_toolkit"]},
        "cashback": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit", "subscriptions"]},
        "westjetbiz": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        "imt": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "moneris": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "avionrewards": {"apis": ["offers_for_publishers", "offers_merchant_content", "places"], "use_cases": ["specials", "places"],
                         "bundles": ["loyalty_stack"]},
        "linked": {"apis": ["offers_merchant_content", "merchant_identifier"], "use_cases": ["enrichment", "specials"], "bundles": ["loyalty_stack"]},
        "wallets": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["bin_lookup", "recurring"], "bundles": ["subscriptions"]},
        "controls": {"apis": ["transaction_notifications", "consumer_clarity", "merchant_identifier"], "use_cases": ["txnotify", "consumer_clarity"],
                     "bundles": ["merchant_resolution"]},
        # L5 Access
        "app": {"apis": ["open_finance", "consumer_clarity", "easy_savings"], "use_cases": ["pfm", "identity"], "bundles": ["pfm_stack"]},
        "newcomer": {"apis": ["open_finance"], "use_cases": ["identity", "settle_in"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "subscriptions", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack", "acquirer_risk"),
        "rewards": ("loyalty_stack",),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "everyday": ("pfm_stack", "merchant_resolution"),
    },
}
