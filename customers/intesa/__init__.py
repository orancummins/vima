"""Intesa Sanpaolo S.p.A.

The page (``Intesa_Sanpaolo_Platform.html``) reads Italy's largest bank as five
discs, Foundation to Access, with the divisions it reports (Banca dei Territori,
IMI Corporate & Investment Banking, International Banks, the wealth divisions
and the Corporate Centre), a Mastercard lens (Mastercard at the top of the book,
Visa with the contract, Bancomat at home) and ten journeys, two of them for
Mastercard. Banca Intesa Beograd has its own page. Public sources as at
17 October 2026; the research behind it is in
``Intesa_Sanpaolo_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``intesa_inventory.py`` and
``intesa_story.py``::

    python customers/build_page.py intesa
"""

CUSTOMER = {
    "id": "intesa",
    "order": 1460,
    "name": "Intesa Sanpaolo",
    "short": "Intesa Sanpaolo",
    "brands": ["Intesa Sanpaolo", "Isybank", "Fideuram", "Eurizon", "IMI CIB", "XME"],
    "country": "Italy",
    "region": "Europe",
    "type": "bank",
    "accent": "#258900",   # Intesa Sanpaolo green, from intesasanpaolo.com
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Intesa Sanpaolo", "bg": "#258900",
         "source": "https://group.intesasanpaolo.com/content/dam/portalgroup/nuove-immagini/immagini-cross/loghi/logo_isp.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Italy's largest bank as five discs: 13.9 million Italian customers choosing Visa or Mastercard on top of "
               "Bancomat, Mastercard alone on the Exclusive and Isybank cards, and Visa holding the renewed partnership.",
    "stats": [
        {"label": "Customers", "value": "21m"},
        {"label": "Net income 2025", "value": "€9.3bn"},
        {"label": "Loans H1 2026", "value": "€437bn"},
        {"label": "Isybank customers", "value": "1.2m"},
    ],
    "page": "Intesa_Sanpaolo_Platform.html",
    "notes": (
        ("Research notes", "Intesa_Sanpaolo_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"]},
        "credit": {"apis": ["consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "exclusive": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"],
                      "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "isycards": {"apis": ["consumer_clarity", "merchant_identifier", "transaction_notifications"],
                     "use_cases": ["enrichment", "pfm", "txnotify"], "bundles": ["pfm_stack"]},
        "accept": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "spensierata": {"apis": ["consumer_clarity", "automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "ai": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "isybank": {"apis": ["open_finance_eu", "consumer_clarity"], "use_cases": ["identity", "settle_in"], "bundles": ["merchant_resolution"]},
        "business": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "loyalty_stack", "subscriptions"),
        "mcnow": ("loyalty_stack", "issuer_toolkit"),
        "digital": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "loyalty_stack"),
        "exclusive": ("loyalty_stack",),
    },
}
