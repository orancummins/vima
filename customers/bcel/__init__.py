"""BCEL (Banque pour le Commerce Extérieur Lao Public).

The page (``BCEL_Platform.html``) reads Laos's biggest commercial bank as five discs,
Foundation to Access, with its main activities (retail and digital, corporate and SME lending,
treasury and FX, group and investments), a Mastercard lens (a UnionPay and Visa bank with one
Mastercard in the wallet) and nine journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in ``BCEL_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the template and swaps in
the data from ``page_data.py``, ``bcel_inventory.py`` and ``bcel_story.py``::

    python customers/build_page.py bcel
"""

CUSTOMER = {
    "id": "bcel",
    "order": 880,
    "name": "BCEL",
    "short": "BCEL",
    "brands": ["BCEL", "BCEL One", "OnePay", "BCOME", "EZyKip", "BCEL-KT Securities"],
    "country": "Laos",
    "region": "Asia-Pacific",
    "accent": "#e81820",   # BCEL red, from the logo and the bank's brand page
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "BCEL", "bg": "#ffffff", "source": "https://www.bcel.com.la/bcel/resources/imgs/logobcel.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Laos's biggest commercial bank as five discs: mass debit on UnionPay, premium and corporate cards on "
               "Visa, QR everywhere through OnePay and LAO QR, and one World Mastercard and a prepaid card for Mastercard.",
    "stats": [
        {"label": "Assets H1 2026", "value": "LAK 166tn"},
        {"label": "Net profit 2025", "value": "LAK 933bn"},
        {"label": "BCEL One users", "value": "1.4m+"},
        {"label": "BCOME agents", "value": "734"},
    ],
    "page": "BCEL_Platform.html",
    "notes": (
        ("Research notes", "BCEL_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "updebit": {"apis": ["bin_lookup", "transaction_notifications"], "use_cases": ["bin_lookup", "txnotify"], "bundles": ["issuer_toolkit"]},
        "wmc": {"apis": ["benefits_eligibility", "priceless_cities", "consumer_clarity"], "use_cases": ["findacard", "consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "vpmc": {"apis": ["transaction_notifications", "enhanced_currency_conversion_calculator"], "use_cases": ["txnotify", "recurring"], "bundles": ["subscriptions"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "onepay": {"apis": ["merchant_identifier", "places"], "use_cases": ["places", "enrichment"], "bundles": ["merchant_resolution"]},
        "ezykip": {"apis": ["enhanced_currency_conversion_calculator", "places"], "use_cases": ["settle_in", "places"]},
        "moneygram": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "visacorp": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "pci": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["identity", "txnotify"]},
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L5 Access
        "bcelone": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "acquirer_risk"),
        "mcnow": ("issuer_toolkit", "subscriptions"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "visit": ("loyalty_stack",),
    },
}
