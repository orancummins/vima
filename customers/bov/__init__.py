"""Bank of Valletta p.l.c.

The page (``Bank_of_Valletta_Platform.html``) reads Malta's largest bank as
five discs, Foundation to Access, with the segments it reports (Retail
Banking, Wealth Management, Business Banking, Treasury, Others), a Mastercard
lens (every card on Visa since the Mastercard credit programme closed in 2021)
and ten journeys, two of them for Mastercard. Public sources as at 17 October
2026; the research behind it is in ``Bank_of_Valletta_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``bov_inventory.py``
and ``bov_story.py``::

    python customers/build_page.py bov
"""

CUSTOMER = {
    "id": "bov",
    "order": 660,
    "name": "Bank of Valletta",
    "short": "BOV",
    "brands": ["BOV", "BOV SmartPay", "BOV Pay", "BOV Mobile", "Valletta Fund Management", "BOV Foundation"],
    "country": "Malta",
    "region": "Europe",
    "accent": "#8e0250",   # BOV magenta, from the logo on the H1 2026 interim report
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "BOV Bank of Valletta", "bg": "#ffffff",
         "source": "https://cdn.borzamalta.com.mt/download/announcements/BOV599.pdf"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Malta's largest bank as five discs: €17.6 billion of assets, a quarter owned by the state, every card "
               "on Visa since Mastercard credit closed in 2021, and SmartPay terminals that take both networks.",
    "stats": [
        {"label": "Total assets", "value": "€17.6bn"},
        {"label": "Deposits", "value": "€14.5bn"},
        {"label": "PBT H1 2026", "value": "€119.8m"},
        {"label": "Mastercard cards", "value": "0 since 2021"},
    ],
    "page": "Bank_of_Valletta_Platform.html",
    "notes": (
        ("Research notes", "Bank_of_Valletta_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "corpcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "smartpay": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "mobilepos": {"apis": ["merchant_identifier", "places"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
        "sepainst": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L3 Services
        "vop": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "crm": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "loyalty": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L1 and L4
        "esg": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        "accounts": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "pfm_stack", "loyalty_stack"),
        "mcnow": ("acquirer_risk", "merchant_resolution"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "sme": ("issuer_toolkit", "sustainability"),
    },
}
