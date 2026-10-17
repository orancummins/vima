"""Kapital Bank OJSC (Birbank), Azerbaijan.

The page (``Kapital_Bank_Azerbaijan_Platform.html``) reads Azerbaijan's
second-largest bank, which since 2025 sells everything as Birbank, as five
discs, Foundation to Access, with the segments it reports (Retail, Corporate,
Treasury and Ecosystem), a Mastercard lens (a Visa-first bank where Mastercard
holds the niches) and ten journeys, two of them for Mastercard. Public sources
as at 17 October 2026; the research behind it is in
``Kapital_Bank_Azerbaijan_research_notes.md``. Not to be confused with
Kapitalbank of Uzbekistan.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``kapitalbankaz_inventory.py`` and ``kapitalbankaz_story.py``::

    python customers/build_page.py kapitalbankaz
"""

CUSTOMER = {
    "id": "kapitalbankaz",
    "order": 920,
    "name": "Kapital Bank",
    "short": "Kapital Bank",
    "brands": ["Kapital Bank", "Birbank", "Birbank Biznes", "Birbank Private", "Birbank Invest", "m10", "MilliÖn", "Birmarket"],
    "country": "Azerbaijan",
    "region": "EEMEA",
    "accent": "#b61d29",   # Kapital Bank red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Kapital Bank", "bg": "#ffffff",
         "source": "https://www.kapitalbank.az/assets/static/img/content/elements/svg/Group%20427318881.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Azerbaijan's second-largest bank as five discs: more than 5 million customers on the Birbank app and "
               "Taksit cards, Visa on the core cards, and Mastercard on Miles, World Elite and a new teachers' card.",
    "stats": [
        {"label": "Individual customers", "value": "5m+"},
        {"label": "Assets Sep 2026", "value": "AZN 13.9bn"},
        {"label": "Net profit 9M 2026", "value": "AZN 297m"},
        {"label": "Birbank app users", "value": "3.5m"},
    ],
    "page": "Kapital_Bank_Azerbaijan_Platform.html",
    "notes": (
        ("Research notes", "Kapital_Bank_Azerbaijan_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "taksit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "debit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "miles": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility"], "use_cases": ["findacard"]},
        "tehsil": {"apis": ["offers_for_publishers", "priceless_cities", "benefits_eligibility"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "bizcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "transfers": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["txnotify"]},
        # L3 Services
        "birbonus": {"apis": ["offers_for_publishers", "offers_merchant_content", "places"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "fraud": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["identity", "txnotify"], "bundles": ["issuer_toolkit"]},
        "notify": {"apis": ["consumer_clarity", "merchant_identifier", "automatic_billing_updater"], "use_cases": ["enrichment", "recurring"],
                   "bundles": ["subscriptions", "merchant_resolution"]},
        # L4 Business lines
        "birmarket": {"apis": ["match", "merchant_identifier"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "subscriptions"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "loyalty_stack"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "credit": ("issuer_toolkit", "subscriptions"),
    },
}
