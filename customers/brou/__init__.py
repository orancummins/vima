"""Banco República (BROU), Banco de la República Oriental del Uruguay.

The page (``Banco_Republica_BROU_Platform.html``) reads Uruguay's state bank
as five discs, Foundation to Access: retail banking (Personas), the corporate
division, finance and treasury, and the group (AFISA, AFAP, Microfinanzas,
Sistarbanc), with a Mastercard lens (debit moving wholly from Maestro to
Debit Mastercard, Recompensa on Mastercard, Visa holding the top card) and
ten journeys, two of them for Mastercard. Public sources as at 17 October
2026; amounts in US dollars. The research behind it is in
``Banco_Republica_BROU_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``brou_inventory.py``
and ``brou_story.py``::

    python customers/build_page.py brou
"""

CUSTOMER = {
    "id": "brou",
    "order": 420,
    "name": "Banco República (BROU)",
    "short": "BROU",
    "brands": ["BROU", "BROU Recompensa", "BROU a Mano", "eBROU", "República AFAP", "República AFISA"],
    "country": "Uruguay",
    "region": "Latin America",
    "type": "bank",
    "accent": "#0066b3",   # BROU blue, from brou.com.uy's logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Banco República", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:LogoBROU.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Uruguay's state bank as five discs: 41% of the system's assets, 1.8 million debit cards moving from "
               "Maestro to Debit Mastercard, Recompensa on Mastercard and Visa at the top of the card range.",
    "stats": [
        {"label": "System assets", "value": "41%"},
        {"label": "Profit 2025", "value": "$475m"},
        {"label": "Debit cards", "value": "1.78m"},
        {"label": "Maestro off", "value": "1 Nov 2026"},
    ],
    "page": "Banco_Republica_BROU_Platform.html",
    "notes": (
        ("Research notes", "Banco_Republica_BROU_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mcdebit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "reccredit": {"apis": ["consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                      "bundles": ["issuer_toolkit"]},
        "bam": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "bamcom": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "spi": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "alfabrou": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "recompensa": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "benefits": {"apis": ["priceless_cities", "benefits_eligibility"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "pymecard": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        "accounts": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity", "pfm"], "bundles": ["merchant_resolution"]},
        "corpcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "loyalty_stack", "acquirer_risk"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "credit": ("loyalty_stack",),
    },
}
