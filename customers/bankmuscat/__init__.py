"""Bank Muscat SAOG.

The page (``Bank_Muscat_Platform.html``) reads Oman's largest bank as five
discs, Foundation to Access, with the segments it reports (Corporate,
Personal, Wholesale, International and Islamic Banking), a Mastercard lens (a
Visa bank whose merchants Mastercard needs) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``Bank_Muscat_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``bankmuscat_inventory.py`` and ``bankmuscat_story.py``::

    python customers/build_page.py bankmuscat
"""

CUSTOMER = {
    "id": "bankmuscat",
    "order": 1000,
    "name": "Bank Muscat",
    "short": "Bank Muscat",
    "brands": ["Bank Muscat", "Meethaq", "Al Jawhar", "Asalah", "Hisaby", "Bank Muscat Rewards"],
    "country": "Oman",
    "region": "EEMEA",
    "type": "bank",
    "accent": "#e83840",   # Bank Muscat red, from the logo on bankmuscat.com
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Bank Muscat", "bg": "#ffffff",
         "source": "https://www.bankmuscat.com/_catalogs/masterpage/images/bm_logo_color.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Oman's largest bank as five discs: about a third of the country's banking assets, Visa on almost every "
               "card, one LuLu Mastercard, and the acquirer behind 46% of Omani card payments.",
    "stats": [
        {"label": "Customers", "value": "~4m"},
        {"label": "Assets 2025", "value": "RO 15.1bn"},
        {"label": "Asset share", "value": "32%"},
        {"label": "Acquiring share", "value": "46%+"},
    ],
    "page": "Bank_Muscat_Platform.html",
    "notes": (
        ("Research notes", "Bank_Muscat_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "lulu": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                 "bundles": ["issuer_toolkit"]},
        "visacredit": {"apis": ["bin_lookup", "benefits_eligibility"], "use_cases": ["findacard"], "bundles": ["issuer_toolkit"]},
        "instantcard": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "tapngo": {"apis": ["match"], "bundles": ["acquirer_risk"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "corpcard": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "openbanking": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "loyalty_stack", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "credit": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack",),
    },
}
