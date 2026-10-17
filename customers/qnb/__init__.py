"""QNB Group (Qatar National Bank Q.P.S.C.).

The page (``QNB_Group_Platform.html``) reads the Middle East and Africa's
largest bank as five discs, Foundation to Access, with the segments it reports
(Consumer Banking, Corporate & Institutional Banking, Asset & Wealth
Management, International Banking), a Mastercard lens (Mastercard runs QNB's
business cards; Visa has its consumers) and nine journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``QNB_Group_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``qnb_inventory.py``
and ``qnb_story.py``::

    python customers/build_page.py qnb
"""

CUSTOMER = {
    "id": "qnb",
    "order": 970,
    "name": "QNB Group",
    "short": "QNB",
    "brands": ["QNB", "QNB First", "QNB Private", "QNB Türkiye", "Enpara", "QNB Egypt"],
    "country": "Qatar",
    "region": "EEMEA",
    "accent": "#003d74",   # QNB navy, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "QNB", "bg": "#ffffff",
         "source": "https://commons.wikimedia.org/wiki/File:QNB_Logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The Middle East and Africa's largest bank as five discs: QR1.46 trillion of assets, Mastercard for "
               "corporate, SME and Private cards, Visa for consumer credit and co-brands, and Fawran and NAPS at home.",
    "stats": [
        {"label": "Assets", "value": "QR1.46tn"},
        {"label": "9M 2026 profit", "value": "QR13.3bn"},
        {"label": "Countries", "value": "28+"},
        {"label": "Cost:income", "value": "24.3%"},
    ],
    "page": "QNB_Group_Platform.html",
    "notes": (
        ("Research notes", "QNB_Group_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "liferewards": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                        "bundles": ["issuer_toolkit"]},
        "worldelite": {"apis": ["benefits_eligibility", "priceless_cities", "offers_for_publishers"], "use_cases": ["specials", "findacard"],
                       "bundles": ["loyalty_stack"]},
        "mcdebit": {"apis": ["transaction_notifications", "enhanced_currency_conversion_calculator"], "use_cases": ["txnotify"]},
        "corpcards": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        "virtualcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "mypos": {"apis": ["places", "merchant_identifier"], "use_cases": ["places"], "bundles": ["acquirer_risk"]},
        "simplify": {"apis": ["merchant_identifier", "automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["identity", "txnotify"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "smartdata": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "acquirer_risk"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "corp": ("issuer_toolkit", "merchant_resolution"),
        "merchant": ("acquirer_risk", "subscriptions"),
        "first": ("loyalty_stack",),
    },
}
