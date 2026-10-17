"""Zagrebačka banka d.d. (Zaba), UniCredit's bank in Croatia.

The page (``Zagrebacka_banka_Platform.html``) reads Croatia's largest bank as
five discs, Foundation to Access, with its business lines (Retail & Prime,
Small business, Corporate & investment banking and the subsidiaries), a
Mastercard lens (every card Zaba issues moved to Mastercard in 2024–25;
acquiring and transfers stay network-neutral) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``Zagrebacka_banka_research_notes.md``. The parent is mapped as ``unicredit``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``zaba_inventory.py`` and
``zaba_story.py``::

    python customers/build_page.py zaba
"""

CUSTOMER = {
    "id": "zaba",
    "order": 620,
    "name": "Zagrebačka banka",
    "short": "Zaba",
    "brands": ["Zaba", "m-zaba", "IziPay", "go!card", "UniCredit Invest", "UniCredit Leasing Croatia", "UniCredit Bank Mostar"],
    "country": "Croatia",
    "region": "Europe",
    "accent": "#ee3124",   # Zaba red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Zagrebačka banka", "bg": "#ffffff",
         "source": "https://www.zaba.hr/home/static/img/zaba_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Croatia's largest bank as five discs: a quarter of the market, UniCredit's, and since 2024–25 every "
               "card it issues on Mastercard after two million debit cards left Visa.",
    "stats": [
        {"label": "Asset share", "value": "25.8%"},
        {"label": "Assets", "value": "€23.6bn"},
        {"label": "Profit H1 2026", "value": "€251m"},
        {"label": "Debit cards moved", "value": "~2m"},
    ],
    "page": "Zagrebacka_banka_Platform.html",
    "notes": (
        ("Research notes", "Zagrebacka_banka_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit", "subscriptions"]},
        "virtual": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "accept": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "softpos": {"apis": ["merchant_identifier", "places"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
        "izipay": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L3 Services
        "fraudcamp": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "identity"]},
        "perks": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "priceless": {"apis": ["priceless_cities", "benefits_eligibility"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "bizcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "homeloans": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        # L5 Access
        "mzaba": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "issuer_toolkit", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "card": ("issuer_toolkit", "subscriptions"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
    },
}
