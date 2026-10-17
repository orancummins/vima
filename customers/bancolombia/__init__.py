"""Bancolombia S.A. (Grupo Cibest).

The page (``Bancolombia_Platform.html``) reads Colombia's biggest bank as
five discs, Foundation to Access, with the parts of Grupo Cibest it reports
(Bancolombia in Colombia, Central America, Nequi and the digital businesses,
leasing and consumer finance), a Mastercard lens (Mastercard owns the debit,
shares the credit, and faces Bre-B) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``Bancolombia_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``bancolombia_inventory.py`` and ``bancolombia_story.py``::

    python customers/build_page.py bancolombia
"""

CUSTOMER = {
    "id": "bancolombia",
    "order": 390,
    "name": "Bancolombia",
    "short": "Bancolombia",
    "brands": ["Bancolombia", "Grupo Cibest", "Nequi", "Wompi", "Wenia", "Banco Agrícola", "BAM", "Sufi"],
    "country": "Colombia",
    "region": "Latin America",
    "type": "bank",
    "accent": "#fdda24",   # Bancolombia yellow, from the website
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Bancolombia", "bg": "#ffffff",
         "source": "https://www.bancolombia.com/wcm/connect/a67af2d6-c768-4f4f-a33b-fd58074f7ce9/logo-bancolombia-black.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Colombia's biggest bank as five discs: every debit card on Mastercard, a credit book split three ways "
               "with Visa and Amex, Nequi on Visa, and the QR moving onto Bre-B.",
    "stats": [
        {"label": "Assets", "value": "COP 363trn"},
        {"label": "ROE Q2 2026", "value": "28.7%"},
        {"label": "Active credit cards", "value": "2.76m"},
        {"label": "Nequi clients", "value": "29m"},
    ],
    "page": "Bancolombia_Platform.html",
    "notes": (
        ("Research notes", "Bancolombia_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"],
                  "bundles": ["issuer_toolkit"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit", "subscriptions"]},
        "legend": {"apis": ["benefits_eligibility", "priceless_cities", "offers_for_publishers"], "use_cases": ["specials", "findacard"],
                   "bundles": ["loyalty_stack"]},
        "wallets": {"apis": ["merchant_identifier", "consumer_clarity"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "nequisv": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["txnotify", "settle_in"]},
        "breb": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "wompi": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "agents": {"apis": ["merchant_identifier", "consumer_clarity"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
        "points": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "nequicredit": {"apis": ["open_finance", "bin_lookup"], "use_cases": ["identity", "bin_lookup"]},
        "renting": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "merchant_resolution", "sustainability"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "issuer_toolkit"),
        "premium": ("loyalty_stack",),
        "merchant": ("acquirer_risk", "merchant_resolution"),
    },
}
