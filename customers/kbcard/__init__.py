"""KB Kookmin Card Co., Ltd.

The page (``KB_Kookmin_Card_Platform.html``) reads KB Financial Group's card
company as five discs, Foundation to Access, with the business it reports
(card business, card loans and cash advances, instalment finance and leasing,
overseas), a Mastercard lens (premium cards, travel debit and a stablecoin
test on Mastercard, but its own K-World brand on JCB and UnionPay and Visa
on agent payments) and ten journeys, two of them for Mastercard. Public
sources as at 17 October 2026; the research behind it is in
``KB_Kookmin_Card_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``kbcard_inventory.py`` and ``kbcard_story.py``::

    python customers/build_page.py kbcard
"""

CUSTOMER = {
    "id": "kbcard",
    "order": 1540,
    "name": "KB Kookmin Card",
    "short": "KB Card",
    "brands": ["KB Kookmin Card", "KB Pay", "ALL·YOU·NEED", "HERITAGE", "K-World", "KB J Capital"],
    "country": "South Korea",
    "region": "Asia-Pacific",
    "type": "issuer",
    "accent": "#ffbc00",   # KB yellow, from the logo's star
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "KB Kookmin Card", "bg": "#ffffff",
         "source": "https://img1.kbcard.com/home_re/mo/logo/24/logo-kbcard-color.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Korea's number-three card company by H1 2026 profit as five discs: Mastercard on its premium cards, travel "
               "debit and a stablecoin test, but its own K-World brand on JCB and UnionPay, and Visa on agent payments.",
    "stats": [
        {"label": "Net income H1 2026", "value": "₩219bn"},
        {"label": "Card usage H1 2026", "value": "₩93.5tn"},
        {"label": "Members", "value": "13m"},
        {"label": "KB Pay monthly users", "value": "9.1m"},
    ],
    "page": "KB_Kookmin_Card_Platform.html",
    "notes": (
        ("Research notes", "KB_Kookmin_Card_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "youprime": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "hclassic": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "travelers": {"apis": ["enhanced_currency_conversion_calculator", "offers_for_publishers"], "use_cases": ["settle_in", "specials"],
                      "bundles": ["loyalty_stack"]},
        "applepay": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring", "bin_lookup"], "bundles": ["subscriptions"]},
        "agentpoc": {"apis": ["merchant_identifier", "transaction_notifications"], "use_cases": ["identity", "txnotify"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "overseassafe": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "mtr": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "datalake": {"apis": ["merchant_identifier", "places"], "use_cases": ["places", "psi"], "bundles": ["merchant_resolution"]},
        # L4 Business lines
        "corpcard": {"apis": ["business_payment_controls", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "merchant": {"apis": ["merchant_identifier", "places"], "use_cases": ["places", "psi"], "bundles": ["merchant_resolution", "acquirer_risk"]},
        # L5 Access
        "kbpay": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "subscriptions", "merchant_resolution"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "travel": ("loyalty_stack",),
        "everyday": ("pfm_stack", "issuer_toolkit"),
        "biz": ("merchant_resolution", "acquirer_risk"),
    },
}
