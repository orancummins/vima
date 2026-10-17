"""International Development Bank for Investment and Finance (IDB, Iraq).

The page (``International_Development_Bank_Platform.html``) reads an Iraqi
private bank as five discs, Foundation to Access, with its retail, corporate
and treasury and investment business, a Mastercard lens (licensed by
Mastercard, issuing mostly on Visa, cut off from the dollar) and nine
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
IDB's own site was behind bot protection, so sources are thin. The research
behind it is in ``International_Development_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``idb_inventory.py`` and ``idb_story.py``::

    python customers/build_page.py idb
"""

CUSTOMER = {
    "id": "idb",
    "order": 1030,
    "name": "International Development Bank",
    "short": "IDB",
    "brands": ["IDB", "e-IDB", "IDB UAE", "Arab Tourist Card"],
    "country": "Iraq",
    "region": "EEMEA",
    "accent": "#e80028",   # IDB red, from the logo on idb.iq
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "International Development Bank", "bg": "#ffffff",
         "source": "https://web.archive.org/web/20250129072801/https://www.idb.iq/content/images/logo2.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "An Iraqi private bank as five discs: about USD 2.4 billion of assets, licences from Mastercard and Visa, "
               "Visa debit and a Mastercard Gold credit card, and a US-dollar bar that limits both abroad.",
    "stats": [
        {"label": "Assets 2024", "value": "USD 2.4bn"},
        {"label": "Profit 2024", "value": "USD 46m"},
        {"label": "Branches", "value": "27"},
        {"label": "POS terminals", "value": "5,000"},
    ],
    "page": "International_Development_Bank_Platform.html",
    "notes": (
        ("Research notes", "International_Development_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "visaclassic": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "mcgold": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "arabtourist": {"apis": ["priceless_cities", "benefits_eligibility", "enhanced_currency_conversion_calculator"], "use_cases": ["specials"],
                        "bundles": ["loyalty_stack"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "atms": {"apis": ["places"], "use_cases": ["places"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "benefits": {"apis": ["benefits_eligibility", "offers_for_publishers"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "salaries": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "cashmgmt": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L5 Access
        "mobile": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "merchant": ("acquirer_risk",),
        "travel": ("loyalty_stack",),
    },
}
