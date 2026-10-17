"""JSCB Kapitalbank, Uzbekistan's largest private bank (not Kapital Bank of Azerbaijan).

The page (``Kapitalbank_Platform.html``) reads the bank as five discs,
Foundation to Access, with its main businesses (retail, small business,
corporate and trade finance, treasury), a Mastercard lens (Visa's top Uzbek
issuer, with Mastercard as a strong second) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``Kapitalbank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``kapitalbankuz_inventory.py`` and
``kapitalbankuz_story.py``::

    python customers/build_page.py kapitalbankuz
"""

CUSTOMER = {
    "id": "kapitalbankuz",
    "order": 910,
    "name": "Kapitalbank",
    "short": "Kapitalbank",
    "brands": ["Kapitalbank", "KAPITALBANK.Online", "Uzum Business Kapitalbank", "Kapital Premium", "Kapital Privilege"],
    "country": "Uzbekistan",
    "region": "EEMEA",
    "type": "bank",
    "accent": "#fbc200",   # Kapitalbank yellow, the site's theme colour and the bars in the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Kapitalbank", "bg": "#ffffff",
         "source": "https://kapitalbank.uz/upload/media/images/Kapitalbank_new.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Uzbekistan's largest private bank as five discs: the country's biggest retail deposit book, Uzcard and "
               "HUMO at home, Visa's best Uzbek issuer abroad, and a full Mastercard line from World Elite to MoneySend.",
    "stats": [
        {"label": "Assets Jul 2026", "value": "UZS 62.7trn"},
        {"label": "Profit 2025", "value": "$156m"},
        {"label": "ROE 2025", "value": "28.9%"},
        {"label": "Retail clients", "value": "2m+"},
    ],
    "page": "Kapitalbank_Platform.html",
    "notes": (
        ("Research notes", "Kapitalbank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mccards": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "bin_lookup"],
                    "bundles": ["issuer_toolkit"]},
        "mcpremium": {"apis": ["benefits_eligibility", "priceless_cities", "places"], "use_cases": ["findacard", "places"], "bundles": ["loyalty_stack"]},
        "mcmulti": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["txnotify", "settle_in"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "ecom": {"apis": ["match", "merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
        "moneysend": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "mcbiz": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        # L3 Services
        "subs": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "fraud": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "identity"]},
        "mcoffers": {"apis": ["offers_for_publishers", "offers_merchant_content", "easy_savings"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "uzbizapp": {"apis": ["business_payment_controls", "merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "pfm_stack", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "premium": ("loyalty_stack",),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "everyday": ("pfm_stack", "subscriptions"),
    },
}
