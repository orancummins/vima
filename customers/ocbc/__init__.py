"""OCBC (Oversea-Chinese Banking Corporation Limited).

The page (``OCBC_Platform.html``) reads Singapore's oldest bank as five discs,
Foundation to Access, with the segments it reports (Global Consumer/Private
Banking, Global Wholesale Banking, Global Markets, Insurance), a Mastercard
lens (Visa's flagship and transfers, Mastercard's newer cards and Malaysia) and
ten journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``OCBC_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``ocbc_inventory.py`` and ``ocbc_story.py``::

    python customers/build_page.py ocbc
"""

CUSTOMER = {
    "id": "ocbc",
    "order": 1570,
    "name": "OCBC",
    "short": "OCBC",
    "brands": ["OCBC", "FRANK by OCBC", "Bank of Singapore", "Great Eastern", "Lion Global Investors", "OCBC Malaysia",
               "OCBC Indonesia", "OCBC Hong Kong"],
    "country": "Singapore",
    "region": "Asia-Pacific",
    "type": "bank",
    "accent": "#ed1c24",   # OCBC red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "OCBC", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:Logo-ocbc.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Singapore's oldest bank as five discs: the flagship 365 card and Visa Direct transfers on Visa, newer "
               "cards and most of Malaysia on Mastercard, and PayNow and QR in 57 destinations.",
    "stats": [
        {"label": "1H26 net profit", "value": "S$4.19bn"},
        {"label": "Wealth AUM", "value": "S$350bn"},
        {"label": "Card fees 2025", "value": "S$414m"},
        {"label": "Markets", "value": "19"},
    ],
    "page": "OCBC_Platform.html",
    "notes": (
        ("Research notes", "OCBC_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "c365": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"], "bundles": ["pfm_stack"]},
        "infinity": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "n90": {"apis": ["enhanced_currency_conversion_calculator", "priceless_cities"], "use_cases": ["places"], "bundles": ["loyalty_stack"]},
        "nxt": {"apis": ["consumer_clarity"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "onecollect": {"apis": ["merchant_identifier"], "use_cases": ["psi"], "bundles": ["merchant_resolution"]},
        # L3 Services
        "inappcalls": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "singpass": {"use_cases": ["identity"]},
        "wow": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "sme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "gtb": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "issuer_toolkit", "sustainability"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "cashback": ("pfm_stack", "loyalty_stack"),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "corp": ("sustainability",),
    },
}
