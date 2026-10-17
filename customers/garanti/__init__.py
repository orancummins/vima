"""Türkiye Garanti Bankası A.Ş. (Garanti BBVA).

The page (``Garanti_BBVA_Platform.html``) reads Turkey's second-largest
private bank, 86% owned by BBVA, as five discs, Foundation to Access, with
its business areas (retail, SME and commercial, corporate and investment
banking, payment systems, and finance and subsidiaries), a Mastercard lens
(Mastercard's credit-card partner of 30 years in a bank that also issues
Visa, American Express and Troy) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``Garanti_BBVA_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``garanti_inventory.py`` and ``garanti_story.py``::

    python customers/build_page.py garanti
"""

CUSTOMER = {
    "id": "garanti",
    "order": 950,
    "name": "Garanti BBVA",
    "short": "Garanti BBVA",
    "brands": ["Garanti BBVA", "Bonus", "BonusFlaş", "Paracard", "Miles&Smiles", "Shop&Fly", "TAMİ", "Garanti BBVA Kripto"],
    "country": "Turkey",
    "region": "EEMEA",
    "type": "bank",
    "accent": "#217536",   # Garanti green, from the logo and garantibbva.com.tr
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Garanti BBVA", "bg": "#ffffff",
         "source": "https://www.garantibbva.com.tr/content/dam/public-website/logo/logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Turkey's second-largest private bank as five discs: 31 million customers, the largest private card "
               "business with Bonus credit cards mostly on Mastercard, and Visa, Amex and Troy alongside.",
    "stats": [
        {"label": "Customers", "value": "31.2m"},
        {"label": "Credit cards", "value": "20.6m"},
        {"label": "ROAE 1H26", "value": "28.1%"},
        {"label": "POS terminals", "value": "932k"},
    ],
    "page": "Garanti_BBVA_Platform.html",
    "notes": (
        ("Research notes", "Garanti_BBVA_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "bonus": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                  "bundles": ["issuer_toolkit"]},
        "miles": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator"], "use_cases": ["findacard"]},
        "paracard": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "tami": {"apis": ["merchant_identifier", "places"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
        "odemeiste": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L3 Services
        "token": {"apis": ["automatic_billing_updater", "transaction_notifications"], "use_cases": ["recurring", "txnotify"], "bundles": ["subscriptions"]},
        "agentpay": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "bonusprog": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials", "findacard"],
                      "bundles": ["loyalty_stack"]},
        "openbank": {"apis": ["open_finance_eu"], "use_cases": ["identity", "pfm"]},
        # L4 Business lines
        "commcard": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        "cardlend": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "acquirer_risk", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "subscriptions"),
        "bonus": ("loyalty_stack", "issuer_toolkit"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "sme": ("sustainability",),
    },
}
