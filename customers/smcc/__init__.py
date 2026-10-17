"""Sumitomo Mitsui Card Company, Limited.

The page (``Sumitomo_Mitsui_Card_Platform.html``) reads SMBC Group's card and
payments business as five discs, Foundation to Access, with card shopping,
finance, acquiring and guarantees as the reported lines, a Mastercard lens
(Japan's original Visa issuer, with Mastercard a real second brand) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``Sumitomo_Mitsui_Card_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``smcc_inventory.py``
and ``smcc_story.py``::

    python customers/build_page.py smcc
"""

CUSTOMER = {
    "id": "smcc",
    "order": 1530,
    "name": "Sumitomo Mitsui Card",
    "short": "SMBC Card",
    "brands": ["Sumitomo Mitsui Card", "Olive", "stera", "V Point", "Promise", "SMBC Mobit", "Amazon Mastercard"],
    "country": "Japan",
    "region": "Asia-Pacific",
    "type": "issuer",
    "accent": "#004b34",   # SMBC green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Sumitomo Mitsui Card", "bg": "#ffffff",
         "source": "https://commons.wikimedia.org/wiki/File:The_logo_of_Sumitomo_Mitsui_Card_Company,_Limited.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "SMBC Group's card business as five discs: 43 million card holders, Japan's first Visa issuer with "
               "Olive and the top tiers on Visa, and Mastercard on the numberless cards, Amazon and transit.",
    "stats": [
        {"label": "Card holders", "value": "43.35m"},
        {"label": "Shopping FY3/26", "value": "¥41.95tn"},
        {"label": "Olive accounts", "value": "8.0m"},
        {"label": "Transit operators", "value": "200+"},
    ],
    "page": "Sumitomo_Mitsui_Card_Platform.html",
    "notes": (
        ("Research notes", "Sumitomo_Mitsui_Card_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "nl": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["pfm", "txnotify"], "bundles": ["pfm_stack"]},
        "amazon": {"apis": ["automatic_billing_updater", "bin_lookup", "offers_merchant_content"], "use_cases": ["recurring", "bin_lookup"],
                   "bundles": ["issuer_toolkit", "subscriptions"]},
        "infinite": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator", "priceless_cities"],
                     "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "stera": {"apis": ["match", "merchant_identifier"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "clover": {"apis": ["merchant_identifier", "places"], "use_cases": ["places", "psi"], "bundles": ["acquirer_risk"]},
        "transit": {"apis": ["merchant_identifier", "enhanced_currency_conversion_calculator"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
        "wallets": {"apis": ["bin_lookup", "transaction_notifications"], "use_cases": ["txnotify", "identity"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "identity"], "bundles": ["issuer_toolkit"]},
        "agentic": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "identity"], "bundles": ["issuer_toolkit"]},
        "vpoint": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "trunk": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        # L5 Access
        "vpass": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["pfm", "txnotify"], "bundles": ["pfm_stack", "subscriptions"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "sustainability"),
        "mcnow": ("issuer_toolkit", "subscriptions", "merchant_resolution"),
        "everyday": ("pfm_stack", "loyalty_stack"),
        "merch": ("acquirer_risk", "merchant_resolution"),
        "amazon": ("subscriptions",),
    },
}
