"""Banca Transilvania S.A.

The page (``Banca_Transilvania_Platform.html``) reads Romania's largest bank
as five discs, Foundation to Access, with the segments it reports (Retail,
Micro & SME, Mid & Large Corporate, Treasury, Leasing & consumer finance), a
Mastercard lens (a two-scheme issuer where Mastercard has McLaren and Salt
Bank, and Visa the EU identity wallet) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``Banca_Transilvania_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``bancatransilvania_inventory.py`` and ``bancatransilvania_story.py``::

    python customers/build_page.py bancatransilvania
"""

CUSTOMER = {
    "id": "bancatransilvania",
    "order": 600,
    "name": "Banca Transilvania",
    "short": "BT",
    "brands": ["Banca Transilvania", "BT Pay", "BT Go", "Salt Bank", "Victoriabank", "BT Leasing", "BT Direct",
               "BT Asset Management", "BT Capital Partners", "BT Pensii"],
    "country": "Romania",
    "region": "Europe",
    "type": "bank",
    "accent": "#fec214",   # BT yellow, from the logo's shield and the brand
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Banca Transilvania", "bg": "#ffffff",
         "source": "https://commons.wikimedia.org/wiki/File:Banca_Transilvania_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Romania's largest bank as five discs: 22% of the market and 8 million cards on both schemes, "
               "with Mastercard on McLaren and Salt Bank, Visa on UNTOLD and the EU identity wallet, and RoPay in BT Pay.",
    "stats": [
        {"label": "Active customers", "value": "~5m"},
        {"label": "Group assets", "value": "RON 233bn"},
        {"label": "Cards", "value": "8m+"},
        {"label": "BT Pay users", "value": "4.6m"},
    ],
    "page": "Banca_Transilvania_Platform.html",
    "notes": (
        ("Research notes", "Banca_Transilvania_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debitmc": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"]},
        "star": {"apis": ["consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                 "bundles": ["issuer_toolkit"]},
        "mclaren": {"apis": ["priceless_cities", "benefits_eligibility", "offers_for_publishers"], "use_cases": ["specials", "findacard"],
                    "bundles": ["loyalty_stack"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "wallet": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "enrichment"], "bundles": ["pfm_stack"]},
        "btpayitalia": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "starloyalty": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "eudi": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "chatbt": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "openbanking": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L4 Business lines
        "saltbank": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["txnotify", "pfm"],
                     "bundles": ["issuer_toolkit"]},
        "smebank": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "loyalty_stack", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "fan": ("loyalty_stack",),
        "everyday": ("pfm_stack", "subscriptions"),
    },
}
