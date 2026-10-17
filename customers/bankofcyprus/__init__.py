"""Bank of Cyprus Holdings plc.

The page (``Bank_of_Cyprus_Platform.html``) reads Cyprus' largest financial
group as five discs, Foundation to Access, with the business lines it reports
(Consumer, SME & Corporate, International, Insurance, JCC & other), a
Mastercard lens (every card on both networks, but the extras are Visa's) and
ten journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``Bank_of_Cyprus_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``bankofcyprus_inventory.py`` and ``bankofcyprus_story.py``::

    python customers/build_page.py bankofcyprus
"""

CUSTOMER = {
    "id": "bankofcyprus",
    "order": 670,
    "name": "Bank of Cyprus",
    "short": "Bank of Cyprus",
    "brands": ["Bank of Cyprus", "JCC", "EuroLife", "Genikes Insurance", "Jinius", "Fleksy"],
    "country": "Cyprus",
    "region": "Europe",
    "accent": "#006880",   # Bank of Cyprus teal, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Bank of Cyprus", "bg": "#ffffff",
         "source": "https://www.bankofcyprus.com/globalassets/bank-of-cyprus-logo-en.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Cyprus' largest financial group as five discs: three quarters of Cypriots, cards issued on both Visa and "
               "Mastercard, JCC acquiring every network, and Click to Pay and P2P on Visa.",
    "stats": [
        {"label": "Profit H1 2026", "value": "€252m"},
        {"label": "Deposits", "value": "€22.8bn"},
        {"label": "CET1", "value": "20.9%"},
        {"label": "Digital users", "value": "517k"},
    ],
    "page": "Bank_of_Cyprus_Platform.html",
    "notes": (
        ("Research notes", "Bank_of_Cyprus_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debitmc": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"]},
        "creditmc": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "aegean": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "topup": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "c2p": {"apis": ["bin_lookup"], "use_cases": ["bin_lookup", "identity"]},
        "quickpay": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "jcc": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        # L3 Services
        "antamivi": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "fleksy": {"apis": ["consumer_clarity", "open_finance_eu"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        "assistant": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "business": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "accounts": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "pfm_stack", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "travel": ("loyalty_stack",),
    },
}
