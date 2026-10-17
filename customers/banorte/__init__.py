"""Banorte (Grupo Financiero Banorte).

The page (``Banorte_Platform.html``) reads Mexico's second-largest financial
group as five discs, Foundation to Access: banking (cards, debit, RappiCard,
acquiring, mortgages, auto and payroll loans, SMEs, corporate and government),
insurance, annuities and the Afore, and brokerage, with a Mastercard lens
(core credit and RappiCard on Visa, Mastercard on the Marriott co-brand and
some debit) and ten journeys, two of them for Mastercard. Banamex is a
separate customer. Public sources as at 17 October 2026; amounts in pesos.
The research behind it is in ``Banorte_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``banorte_inventory.py`` and ``banorte_story.py``::

    python customers/build_page.py banorte
"""

CUSTOMER = {
    "id": "banorte",
    "order": 1260,
    "name": "Banorte",
    "short": "Banorte",
    "brands": ["Banorte", "Banorte Móvil", "RappiCard", "Seguros Banorte", "Afore XXI Banorte", "UniTeller"],
    "country": "Mexico",
    "region": "Latin America",
    "type": "bank",
    "accent": "#ec1c2d",   # Banorte red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Banorte", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:Logo_de_Banorte.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Mexico's second-largest financial group as five discs: third in cards with core credit and RappiCard "
               "on Visa, Mastercard on the Marriott co-brand and some debit, and 269,000 terminals taking both.",
    "stats": [
        {"label": "Loans", "value": "Ps 1.27tn"},
        {"label": "Banking clients", "value": "13.5m"},
        {"label": "Card share", "value": "11.5%"},
        {"label": "ROE 2Q26", "value": "25.7%"},
    ],
    "page": "Banorte_Platform.html",
    "notes": (
        ("Research notes", "Banorte_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "marriott": {"apis": ["benefits_eligibility", "offers_for_publishers"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "rappicard": {"apis": ["transaction_notifications", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["txnotify", "recurring"],
                      "bundles": ["subscriptions"]},
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "wallets": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring", "bin_lookup"], "bundles": ["subscriptions"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "spei": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "uniteller": {"apis": ["enhanced_currency_conversion_calculator"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "maya": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials"],
                    "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "corpcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "subscriptions", "pfm_stack"),
        "mcnow": ("loyalty_stack", "acquirer_risk"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "young": ("subscriptions", "issuer_toolkit"),
        "sme": ("acquirer_risk",),
    },
}
