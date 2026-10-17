"""Banamex (Grupo Financiero Banamex).

The page (``Banamex_Platform.html``) reads Mexico's second-largest card
issuer as five discs, Foundation to Access: Consumer Banking (cards,
payroll, mortgages, wealth), Commercial, Government & Institutional
Banking, Insurance & Pensions and the Afore, with a Mastercard lens (ten of
fourteen credit cards on Mastercard, Visa on Beyond and Costco) and eleven
journeys, two of them for Mastercard. Citi is selling down ahead of an IPO;
Citi's own institutional business in Mexico is a separate customer. Public
sources as at 17 October 2026; amounts in pesos. The research behind it is
in ``Banamex_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``banamex_inventory.py`` and ``banamex_story.py``::

    python customers/build_page.py banamex
"""

CUSTOMER = {
    "id": "banamex",
    "order": 360,
    "name": "Banamex",
    "short": "Banamex",
    "brands": ["Banamex", "Banamex Priority", "Beyond", "Switch", "Seguros Banamex", "Afore Banamex"],
    "country": "Mexico",
    "region": "Latin America",
    "accent": "#ff1b44",   # Banamex red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Banamex", "bg": "#ffffff", "source": "https://www.banamex.com/content/dam/banamex/Logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Mexico's second-largest card issuer as five discs: a 24% card share with ten of fourteen credit cards "
               "on Mastercard, Visa on Beyond and Costco, and Citi selling down ahead of an IPO.",
    "stats": [
        {"label": "Loans", "value": "Ps 542bn"},
        {"label": "Card share", "value": "24%"},
        {"label": "Citi stake", "value": "~51%"},
        {"label": "Digital customers", "value": "9.4m"},
    ],
    "page": "Banamex_Platform.html",
    "notes": (
        ("Research notes", "Banamex_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"],
                   "use_cases": ["consumer_clarity", "recurring"], "bundles": ["issuer_toolkit"]},
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "lacomer": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"],
                    "bundles": ["loyalty_stack"]},
        "wallets": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["recurring"],
                    "bundles": ["subscriptions"]},
        "acquiring": {"apis": ["merchant_identifier", "match", "places"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "commcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "securecall": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "clarity": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"],
                    "bundles": ["merchant_resolution", "pfm_stack"]},
        "belvo": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "mcbenefits": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard", "specials"]},
        "momentos": {"apis": ["offers_for_publishers", "easy_savings"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "sme": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("subscriptions", "merchant_resolution", "issuer_toolkit", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "travel": ("loyalty_stack",),
        "everyday": ("pfm_stack",),
    },
}
