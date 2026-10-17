"""BDO Unibank, Inc.

The page (``BDO_Unibank_Platform.html``) reads the Philippines' largest bank
as five discs, Foundation to Access, with corporate, commercial and MSME,
consumer, and trust, wealth and insurance lines, a Mastercard lens (twenty
years of debit and remittances, one brand among six in credit) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
amounts in pesos. The research behind it is in
``BDO_Unibank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``bdo_inventory.py``
and ``bdo_story.py``::

    python customers/build_page.py bdo
"""

CUSTOMER = {
    "id": "bdo",
    "order": 810,
    "name": "BDO Unibank",
    "short": "BDO",
    "brands": ["BDO", "BDO Pay", "BDO Private Bank", "BDO Network Bank", "BDO Life", "BDO Capital"],
    "country": "Philippines",
    "region": "Asia-Pacific",
    "type": "bank",
    "accent": "#0b2972",   # BDO navy, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "BDO Unibank", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:BDO_Unibank_(logo).svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The Philippines' largest bank as five discs: ₱3.9 trillion of loans, ATM debit and remittances on "
               "Mastercard for twenty years, credit on six networks, and free InstaPay and QR Ph in BDO Pay.",
    "stats": [
        {"label": "Net income H1 2026", "value": "₱40.7bn"},
        {"label": "Loans", "value": "₱3.9tn"},
        {"label": "Branches", "value": "2,000+"},
        {"label": "Filipinos abroad served", "value": "4m+"},
    ],
    "page": "BDO_Unibank_Platform.html",
    "notes": (
        ("Research notes", "BDO_Unibank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater", "benefits_eligibility"],
                   "use_cases": ["consumer_clarity", "recurring"], "bundles": ["issuer_toolkit", "subscriptions"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["txnotify"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "qrph": {"apis": ["merchant_identifier", "places"], "use_cases": ["places", "enrichment"], "bundles": ["merchant_resolution"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "payrewards": {"apis": ["offers_for_publishers", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "data": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "msme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "corp": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        # L5 Access
        "bdopay": {"apis": ["consumer_clarity", "merchant_identifier", "transaction_notifications"],
                   "use_cases": ["enrichment", "pfm", "txnotify"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "loyalty_stack", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "wallet": ("pfm_stack", "loyalty_stack"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "corp": ("sustainability",),
    },
}
