"""JSC CB PrivatBank.

The page (``PrivatBank_Platform.html``) reads Ukraine's largest bank as five
discs, Foundation to Access, with the segments it reports (Retail banking,
Corporate banking business, Capital markets, the separate former-owner
portfolio, and capital management), a Mastercard lens (Europe's biggest card
issuer, split between two networks) and nine journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``PrivatBank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``privatbank_inventory.py`` and ``privatbank_story.py``::

    python customers/build_page.py privatbank
"""

CUSTOMER = {
    "id": "privatbank",
    "order": 700,
    "name": "PrivatBank",
    "short": "PrivatBank",
    "brands": ["PrivatBank", "Privat24", "LiqPay", "PrivatMoney", "Pryvit"],
    "country": "Ukraine",
    "region": "Europe",
    "accent": "#4ea524",   # PrivatBank green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "PrivatBank", "bg": "#ffffff", "source": "https://privatbank.ua/en"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Ukraine's largest bank as five discs: 18 million customers and about 32 million active cards split "
               "between Visa and Mastercard, with cross-border transfers and Ukraine's first Agent Pay payment on Mastercard.",
    "stats": [
        {"label": "Customers", "value": "18m"},
        {"label": "Active cards", "value": "32m"},
        {"label": "Net profit H1 2026", "value": "UAH 24.6bn"},
        {"label": "Privat24 users", "value": "13.7m"},
    ],
    "page": "PrivatBank_Platform.html",
    "notes": (
        ("Research notes", "PrivatBank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "universal": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                      "bundles": ["issuer_toolkit"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "liqpay": {"apis": ["match", "merchant_identifier"], "use_cases": ["psi", "recurring"], "bundles": ["acquirer_risk", "subscriptions"]},
        "p2pintl": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["txnotify"]},
        # L3 Services
        "agentpay": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["identity", "txnotify"], "bundles": ["issuer_toolkit"]},
        "docfraud": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "pryvit": {"apis": ["offers_for_publishers", "offers_merchant_content", "places"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "subs": {"apis": ["automatic_billing_updater", "consumer_clarity"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L4 Business lines
        "sme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "corp": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L5 Access
        "p24app": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "subscriptions", "acquirer_risk"),
        "mcnow": ("issuer_toolkit",),
        "everyday": ("pfm_stack", "loyalty_stack"),
        "sme": ("acquirer_risk",),
        "credit": ("subscriptions", "issuer_toolkit"),
    },
}
