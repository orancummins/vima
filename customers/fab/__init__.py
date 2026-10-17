"""First Abu Dhabi Bank P.J.S.C.

The page (``First_Abu_Dhabi_Bank_Platform.html``) reads the UAE's largest bank
as five discs, Foundation to Access, with the business units it reports
(Personal, Business, Wealth & Privileged Client Banking; Wholesale Banking;
Investment Banking & Markets; International), a Mastercard lens (Mastercard's
exclusive partner, with Visa left in the co-brands) and ten journeys, two of
them for Mastercard. Public sources as at 17 October 2026; the research behind
it is in ``First_Abu_Dhabi_Bank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``fab_inventory.py`` and
``fab_story.py``::

    python customers/build_page.py fab
"""

CUSTOMER = {
    "id": "fab",
    "order": 1620,
    "name": "First Abu Dhabi Bank",
    "short": "FAB",
    "brands": ["FAB", "FAB Islamic", "Payit", "Dubai First", "FABMISR", "FAB Capital"],
    "country": "United Arab Emirates",
    "region": "EEMEA",
    "type": "bank",
    "accent": "#003da6",   # FAB blue, from bankfab.com
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "First Abu Dhabi Bank", "bg": "#003da6",
         "source": "https://www.bankfab.com/-/media/project/fab2/fab2/data/media/img/fab-logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The UAE's largest bank as five discs: AED 1.41 trillion, an exclusive Mastercard partner since 2024, "
               "with Visa left in its biggest co-brands and Jaywan and Aani as the new domestic rails.",
    "stats": [
        {"label": "Total assets", "value": "AED 1.41tn"},
        {"label": "H1 2026 net profit", "value": "AED 10.7bn"},
        {"label": "Customers", "value": "4m+"},
        {"label": "Markets", "value": "20+"},
    ],
    "page": "First_Abu_Dhabi_Bank_Platform.html",
    "notes": (
        ("Research notes", "First_Abu_Dhabi_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "royale": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"],
                   "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "adnoc": {"apis": ["places", "carbon_calculator"], "use_cases": ["places"], "bundles": ["sustainability"]},
        "commcards": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        "payit": {"apis": ["enhanced_currency_conversion_calculator", "consumer_clarity"], "use_cases": ["settle_in", "pfm"], "bundles": ["pfm_stack"]},
        "acquiring": {"apis": ["match", "merchant_identifier"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "apis": {"apis": ["open_finance", "bin_lookup"], "use_cases": ["identity", "bin_lookup"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "accounts": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity", "enrichment"], "bundles": ["merchant_resolution", "subscriptions"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "issuer_toolkit", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "premium": ("loyalty_stack",),
        "sme": ("acquirer_risk", "merchant_resolution", "issuer_toolkit"),
        "remit": ("pfm_stack",),
    },
}
