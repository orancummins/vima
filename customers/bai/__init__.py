"""Banco Angolano de Investimentos (BAI).

The page (``Banco_Angolano_de_Investimentos_Platform.html``) reads Angola's largest bank as
five discs, Foundation to Access, with the segments it reports (retail, commercial, private,
investment and correspondent banking, insurance), a Mastercard lens (a Multicaixa bank where
Visa travels and Mastercard has just arrived) and nine journeys, two of them for Mastercard.
Public sources as at 17 October 2026, mostly in Portuguese; the research behind it is in
``Banco_Angolano_de_Investimentos_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the template and swaps in
the data from ``page_data.py``, ``bai_inventory.py`` and ``bai_story.py``::

    python customers/build_page.py bai
"""

CUSTOMER = {
    "id": "bai",
    "order": 1140,
    "name": "Banco Angolano de Investimentos (BAI)",
    "short": "BAI",
    "brands": ["BAI", "BAI Directo", "BAI Europa", "BAI Cabo Verde", "NOSSA Seguros", "ÁUREA", "é-Kwanza"],
    "country": "Angola",
    "region": "EEMEA",
    "type": "bank",
    "accent": "#002d74",   # BAI navy, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "BAI - Banco Angolano de Investimentos", "bg": "#ffffff",
         "source": "https://www.bancobai.ao/media/2584/logo-bai.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Angola's largest bank as five discs: 3.1 million customers on Multicaixa debit cards, Visa for prepaid "
               "travel and credit, and a new debit card that runs on Mastercard abroad.",
    "stats": [
        {"label": "Active customers", "value": "3.1m"},
        {"label": "Assets Jun 2026", "value": "Kz 5.3trn"},
        {"label": "Net profit 2025", "value": "Kz 296bn"},
        {"label": "Mastercard cards", "value": "796"},
    ],
    "page": "Banco_Angolano_de_Investimentos_Platform.html",
    "notes": (
        ("Research notes", "Banco_Angolano_de_Investimentos_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mcxdebit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "multibrand": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications", "consumer_clarity"],
                       "use_cases": ["txnotify", "consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "kamba": {"apis": ["enhanced_currency_conversion_calculator", "bin_lookup"], "use_cases": ["bin_lookup"]},
        "mccorp": {"apis": ["business_payment_controls", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "flex": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "tpa": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "ebai": {"apis": ["match", "merchant_identifier"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "luena": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "tourism": {"apis": ["offers_for_publishers", "priceless_cities", "places"], "use_cases": ["specials", "places"], "bundles": ["loyalty_stack"]},
        # L4 Business lines / L5 Access
        "corporate": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "app": {"apis": ["consumer_clarity"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "loyalty_stack", "sustainability"),
        "mcnow": ("issuer_toolkit",),
        "abroad": ("issuer_toolkit", "pfm_stack"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "everyday": ("pfm_stack",),
    },
}
