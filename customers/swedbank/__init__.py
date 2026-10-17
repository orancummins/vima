"""Swedbank AB.

The page (``Swedbank_Platform.html``) reads Swedbank as five discs, Foundation
to Access, across its four home markets (Sweden, Estonia, Latvia and
Lithuania), with the business areas it reports (Swedish Banking, Baltic
Banking, Corporates and Institutions, Wealth Management), a Mastercard lens
(Mastercard on every consumer card; the rivals are account rails) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``Swedbank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``swedbank_inventory.py`` and ``swedbank_story.py``::

    python customers/build_page.py swedbank
"""

CUSTOMER = {
    "id": "swedbank",
    "order": 500,
    "name": "Swedbank",
    "short": "Swedbank",
    "brands": ["Swedbank", "Entercard", "Swedbank Pay", "Swedbank Robur", "Stabelo", "PayEx"],
    "country": "Sweden",
    "region": "Europe",
    "accent": "#ff5f00",   # Swedbank orange, from the logo's wordmark
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Swedbank", "bg": "#ffffff",
         "source": "https://www.swedbank.com/content/dam/global/brand/logotypes/8999-swedbank-logo-default.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Swedbank as five discs: 7.3 million private customers in Sweden, Estonia, Latvia and Lithuania, "
               "every consumer card a Mastercard, and Swish and account transfers as the real rivals.",
    "stats": [
        {"label": "Private customers", "value": "7.3m"},
        {"label": "Loans", "value": "SEK 1,934bn"},
        {"label": "RoE H1 2026", "value": "13.6%"},
        {"label": "Cards", "value": "8.6m + 1.4m"},
    ],
    "page": "Swedbank_Platform.html",
    "notes": (
        ("Research notes", "Swedbank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "sedebit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"],
                    "bundles": ["issuer_toolkit"]},
        "secredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "entercard": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring", "bin_lookup"], "bundles": ["subscriptions"]},
        "ltcards": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["txnotify"]},
        "c2p": {"apis": ["merchant_identifier"], "use_cases": ["enrichment"]},
        "swpay": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "swish": {"apis": ["open_finance_eu"], "use_cases": ["identity", "recurring"], "bundles": ["subscriptions"]},
        "bizcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "priceless": {"apis": ["priceless_cities", "offers_for_publishers"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "mikroinvest": {"apis": ["easy_savings", "consumer_clarity"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "corporate": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "subscriptions", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "save": ("pfm_stack",),
    },
}
