"""Bank of America Corporation.

The page (``Bank_of_America_Platform.html``) reads the Charlotte bank as five
discs, Foundation to Access, with the segments it reports (Consumer Banking,
Global Wealth & Investment Management, Global Banking, Global Markets), a
Mastercard lens (Visa's birthplace, with Mastercard on its small-business
cards) and nine journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in
``Bank_of_America_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``bofa_inventory.py`` and ``bofa_story.py``::

    python customers/build_page.py bofa
"""

CUSTOMER = {
    "id": "bofa",
    "order": 200,
    "name": "Bank of America",
    "short": "BofA",
    "brands": ["Bank of America", "Merrill", "Bank of America Private Bank", "BofA Securities", "CashPro", "Erica",
               "BofA Merchant Services"],
    "country": "United States",
    "region": "Americas",
    "accent": "#012169",   # Bank of America navy, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Bank of America", "bg": "#ffffff",
         "source": "static/logos/financial-logos-500/01-financial-institutions/bank-of-america.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "America's largest consumer-deposit bank as five discs: the home of BankAmericard, Visa-led in consumer "
               "cards, with Mastercard on its small-business line and Zelle and Paze for payments.",
    "stats": [
        {"label": "Deposits", "value": "$2.04tn"},
        {"label": "Checking accounts", "value": "38.9m"},
        {"label": "Erica users", "value": "24.2m"},
        {"label": "Zelle 2025", "value": "$556bn"},
    ],
    "page": "Bank_of_America_Platform.html",
    "notes": (
        ("Research notes", "Bank_of_America_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "cashrewards": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                        "bundles": ["issuer_toolkit"]},
        "ncl": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "bizadvantage": {"apis": ["business_payment_controls", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "commercial": {"apis": ["business_payment_controls"]},
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "bams": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "security": {"apis": ["open_finance", "transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        "mycredit": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "erica": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "bofarewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "bankamerideals": {"apis": ["offers_merchant_content", "easy_savings"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "consumer_clarity"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "issuer_toolkit", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "card": ("loyalty_stack", "issuer_toolkit"),
    },
}
