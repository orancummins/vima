"""UniCredit S.p.A.

The page (``UniCredit_Platform.html``) reads the pan-European bank as five
discs, Foundation to Access, with the segments it reports (Italy, Germany,
Austria, Central & Eastern Europe, and group functions), a Mastercard lens
(Mastercard's bank in 12 markets, with Commerzbank still to choose) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``UniCredit_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``unicredit_inventory.py`` and
``unicredit_story.py``::

    python customers/build_page.py unicredit
"""

CUSTOMER = {
    "id": "unicredit",
    "order": 220,
    "name": "UniCredit",
    "short": "UniCredit",
    "brands": ["UniCredit", "HypoVereinsbank", "Bank Austria", "buddy", "onemarkets"],
    "country": "Italy",
    "region": "Europe",
    "type": "bank",
    "accent": "#e31818",   # UniCredit red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "UniCredit", "bg": "#ffffff", "source": "https://www.unicreditgroup.eu/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A pan-European bank as five discs: 13 banks with Mastercard as card partner since 2023, HVB moving "
               "from Visa debit to Mastercard, and 49.65% of Commerzbank still to decide.",
    "stats": [
        {"label": "Loans", "value": "€443bn"},
        {"label": "RoTE 2Q26", "value": "21.7%"},
        {"label": "Cards in MC deal", "value": "~20m"},
        {"label": "Commerzbank", "value": "49.65%"},
    ],
    "page": "UniCredit_Platform.html",
    "notes": (
        ("Research notes", "UniCredit_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mcdeal": {"apis": ["bin_lookup", "consumer_clarity"], "use_cases": ["bin_lookup", "consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "myone": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"]},
        "ucard": {"apis": ["transaction_notifications", "automatic_billing_updater"], "use_cases": ["txnotify", "recurring"], "bundles": ["subscriptions"]},
        "flexiagold": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "baacq": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "itacq": {"apis": ["merchant_identifier", "match"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "priceless": {"apis": ["priceless_cities", "offers_for_publishers"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "aiagents": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "trade": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "italy": {"apis": ["consumer_clarity", "carbon_calculator"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution", "sustainability"]},
        # L5 Access
        "openbank": {"apis": ["open_finance_eu"], "use_cases": ["identity", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "issuer_toolkit", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "merch": ("acquirer_risk",),
        "credit": ("loyalty_stack",),
    },
}
