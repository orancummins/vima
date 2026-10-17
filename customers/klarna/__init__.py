"""Klarna Group plc.

The page (``Klarna_Platform.html``) reads the pay-later network and Swedish
bank as five discs, Foundation to Access, with its product lines (Pay Now,
Pay Later, Fair Financing, banking and memberships), a Mastercard lens (a
Visa card company that Mastercard only touches at the till) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``Klarna_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``klarna_inventory.py`` and ``klarna_story.py``::

    python customers/build_page.py klarna
"""

CUSTOMER = {
    "id": "klarna",
    "order": 1310,
    "name": "Klarna",
    "short": "Klarna",
    "brands": ["Klarna", "Klarna Card", "Klarna Balance", "Fair Financing", "PriceRunner", "Klarna Mobile", "KlarnaUSD"],
    "country": "Sweden",
    "region": "Global",
    "type": "wallet",
    "accent": "#ffb3c7",   # Klarna pink, the brand's primary colour
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Klarna", "bg": "#ffffff", "source": "https://www.klarna.com/international/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The world's biggest pay-later network as five discs: 120 million consumers and $128 billion of volume, "
               "a Swedish bank whose card runs on Visa in 16 countries, with Mastercard only at the till.",
    "stats": [
        {"label": "Active consumers", "value": "120m"},
        {"label": "GMV 2025", "value": "$128bn"},
        {"label": "Klarna Card users", "value": "6.5m"},
        {"label": "Merchants", "value": "1.2m"},
    ],
    "page": "Klarna_Platform.html",
    "notes": (
        ("Research notes", "Klarna_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "paynow": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["bin_lookup", "recurring"], "bundles": ["subscriptions"]},
        "paylater": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "cardeu": {"apis": ["transaction_notifications", "consumer_clarity", "bin_lookup"], "use_cases": ["txnotify", "pfm"],
                   "bundles": ["issuer_toolkit", "pfm_stack"]},
        "balance": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "p2p": {"apis": ["enhanced_currency_conversion_calculator"]},
        # L3 Services
        "signin": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "callstatus": {"apis": ["consumer_clarity"], "use_cases": ["identity"]},
        "agentic": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "cashback": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "openbanking": {"apis": ["open_finance_eu"], "use_cases": ["identity", "pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines and L5 Access
        "merchants": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["merchant_resolution"]},
        "mpgs": {"apis": ["merchant_identifier", "match"], "bundles": ["acquirer_risk"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "issuer_toolkit", "subscriptions"),
        "mcnow": ("acquirer_risk", "subscriptions"),
        "card": ("issuer_toolkit", "pfm_stack"),
        "merchant": ("merchant_resolution", "acquirer_risk"),
        "member": ("loyalty_stack",),
    },
}
