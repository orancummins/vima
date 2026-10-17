"""Navy Federal Credit Union.

The page (``Navy_Federal_Credit_Union_Platform.html``) reads the world's
largest credit union as five discs, Foundation to Access, with its loan
classes standing in for segments (Navy Federal reports none), a Mastercard
lens (Visa's credit union, with Mastercard as the second card) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``Navy_Federal_Credit_Union_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``navyfederal_inventory.py`` and ``navyfederal_story.py``::

    python customers/build_page.py navyfederal
"""

CUSTOMER = {
    "id": "navyfederal",
    "order": 1220,
    "name": "Navy Federal Credit Union",
    "short": "Navy Federal",
    "brands": ["Navy Federal Credit Union", "Navy Federal Investment Services", "Business Solutions",
               "Overseas Military Banking Program"],
    "country": "United States",
    "region": "Americas",
    "type": "bank",
    "accent": "#0f3d70",   # Navy Federal navy, the logo fill on navyfederal.org
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Navy Federal Credit Union", "bg": "#ffffff", "source": "https://www.navyfederal.org/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The world's largest credit union as five discs: 15.5 million military members, debit on Visa, "
               "and everyday credit cards issued on Visa or Mastercard.",
    "stats": [
        {"label": "Members", "value": "15.5m"},
        {"label": "Assets", "value": "$204bn"},
        {"label": "Card balances 2025", "value": "$33.2bn"},
        {"label": "Debit payments 2025", "value": "3.7bn"},
    ],
    "page": "Navy_Federal_Credit_Union_Platform.html",
    "notes": (
        ("Research notes", "Navy_Federal_Credit_Union_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "cashrewards": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                        "bundles": ["issuer_toolkit"]},
        "goplat": {"apis": ["benefits_eligibility", "places"], "use_cases": ["findacard", "places"]},
        "secured": {"apis": ["bin_lookup", "consumer_clarity"], "use_cases": ["bin_lookup", "consumer_clarity"]},
        "merchant": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "rtp": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "makingcents": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "openbanking": {"apis": ["open_finance"], "use_cases": ["identity", "pfm"], "bundles": ["pfm_stack"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "gobiz": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L5 Access
        "ombp": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "issuer_toolkit", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "pfm_stack"),
        "credit": ("issuer_toolkit", "loyalty_stack"),
        "biz": ("acquirer_risk", "issuer_toolkit"),
        "save": ("pfm_stack",),
    },
}
