"""Commerzbank AG.

The page (``Commerzbank_Platform.html``) reads Germany's bank for the
Mittelstand as five discs, Foundation to Access, with the segments it reports
(Private and Small-Business Customers, Corporate Clients, mBank), a Mastercard
lens (a Visa bank with a Mastercard owner at the door) and nine journeys, two
of them for Mastercard. Public sources as at 17 October 2026; the research
behind it is in ``Commerzbank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``commerzbank_inventory.py`` and ``commerzbank_story.py``::

    python customers/build_page.py commerzbank
"""

CUSTOMER = {
    "id": "commerzbank",
    "order": 1490,
    "name": "Commerzbank",
    "short": "Commerzbank",
    "brands": ["Commerzbank", "comdirect", "mBank", "Commerz Real", "Commerz Globalpay"],
    "country": "Germany",
    "region": "Europe",
    "type": "bank",
    "accent": "#002e3c",   # Commerzbank petrol, from the website
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Commerzbank", "bg": "#002e3c", "source": "https://www.commerzbank.de/ms/media/favicons/CB-2021-Logo_horizontal_RGB_Solid_white.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Germany's bank for the Mittelstand as five discs: girocards and credit cards moved to Visa in 2025–26, "
               "Mastercard left with a debit card, mBank credit and acceptance, and UniCredit at about 49.65%.",
    "stats": [
        {"label": "Net result H1 2026", "value": "€1.8bn"},
        {"label": "Corporate client groups", "value": "24k"},
        {"label": "mBank customers", "value": "6m"},
        {"label": "UniCredit position", "value": "~49.65%"},
    ],
    "page": "Commerzbank_Platform.html",
    "notes": (
        ("Research notes", "Commerzbank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "girocard": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "mcdebit": {"apis": ["consumer_clarity", "transaction_notifications", "merchant_identifier"], "use_cases": ["consumer_clarity", "txnotify"],
                    "bundles": ["issuer_toolkit"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit", "subscriptions"]},
        "bizcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "globalpay": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "wero": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "mbcards": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"], "use_cases": ["specials"],
                    "bundles": ["loyalty_stack"]},
        # L3 Services
        "fraudai": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "ava": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "retail": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "corporates": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "credit": ("subscriptions",),
    },
}
