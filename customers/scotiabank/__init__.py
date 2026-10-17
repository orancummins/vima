"""Scotiabank (The Bank of Nova Scotia).

The page (``Scotiabank_Platform.html``) reads Canada's most international bank
as five discs, Foundation to Access, with the segments it reports (Canadian
Banking, International Banking, Global Wealth Management, Global Banking and
Markets, Other), a Mastercard lens (Visa and Amex at home, Mastercard at
Tangerine and abroad) and ten journeys, two of them for Mastercard. Public
sources as at 17 October 2026; the research behind it is in
``Scotiabank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``scotiabank_inventory.py`` and ``scotiabank_story.py``::

    python customers/build_page.py scotiabank
"""

CUSTOMER = {
    "id": "scotiabank",
    "order": 1200,
    "name": "Scotiabank",
    "short": "Scotiabank",
    "brands": ["Scotiabank", "Tangerine", "Scene+", "Scotia Wealth Management", "Scotia iTRADE", "ScotiaConnect", "Roynat"],
    "country": "Canada",
    "region": "Americas",
    "type": "bank",
    "accent": "#ec111a",   # Scotiabank red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Scotiabank", "bg": "#ffffff",
         "source": "https://www.scotiabank.com/content/dam/scotiabank/images/logos/2019/scotiabank-logo-red-desktop-200px.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Canada's most international bank as five discs: its own cards on Visa and Amex, debit on Interac and Visa "
               "Debit, Mastercard at Tangerine, in Caribbean debit and in Peru, and stakes in KeyCorp and Davivienda.",
    "stats": [
        {"label": "Assets", "value": "C$1.55tn"},
        {"label": "ROE Q3 2026", "value": "14.1%"},
        {"label": "Scene+ members", "value": "15m+"},
        {"label": "KeyCorp stake", "value": "14.9%"},
    ],
    "page": "Scotiabank_Platform.html",
    "notes": (
        ("Research notes", "Scotiabank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "tangworldelite": {"apis": ["benefits_eligibility", "priceless_cities", "offers_for_publishers"], "use_cases": ["findacard"],
                           "bundles": ["loyalty_stack"]},
        "tangmoneyback": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                          "bundles": ["issuer_toolkit"]},
        "bizvisa": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "mexicocards": {"apis": ["enhanced_currency_conversion_calculator", "priceless_cities"], "use_cases": ["settle_in"]},
        "perucards": {"apis": ["bin_lookup", "benefits_eligibility"], "use_cases": ["findacard"], "bundles": ["issuer_toolkit"]},
        "caribdebit": {"apis": ["transaction_notifications", "enhanced_currency_conversion_calculator"], "use_cases": ["txnotify"]},
        "interac": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "wallets": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "scotiaconnect": {"apis": ["business_payment_controls", "enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "consumer_clarity", "merchant_identifier"], "use_cases": ["txnotify", "identity"],
                  "bundles": ["merchant_resolution"]},
        "predictive": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
        "sceneplus": {"apis": ["offers_for_publishers", "offers_merchant_content", "places"], "use_cases": ["specials", "places"],
                      "bundles": ["loyalty_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "merchant_resolution", "subscriptions"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "rewards": ("loyalty_stack",),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("sustainability",),
    },
}
