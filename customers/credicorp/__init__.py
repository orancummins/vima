"""Credicorp Ltd. (Banco de Crédito del Perú, Yape, Mibanco).

The page (``Credicorp_BCP_Platform.html``) reads Peru's largest financial
group as five discs, Foundation to Access, with BCP, Yape and Mibanco at the
core and the segments it reports (Universal Banking, Microfinance, Insurance
& Pensions, Investment Management & Advisory), a Mastercard lens (Visa issues
the cards, Yape moves the money, Mastercard stands at the edges) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
amounts in soles. The research behind it is in
``Credicorp_BCP_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``credicorp_inventory.py`` and ``credicorp_story.py``::

    python customers/build_page.py credicorp
"""

CUSTOMER = {
    "id": "credicorp",
    "order": 1250,
    "name": "Credicorp (BCP)",
    "short": "Credicorp",
    "brands": ["BCP", "Yape", "iO", "Mibanco", "Tenpo", "Culqi", "Pacífico", "Prima AFP"],
    "country": "Peru",
    "region": "Latin America",
    "type": "bank",
    "accent": "#00458c",   # BCP blue, from the BCP logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Credicorp", "bg": "#ffffff", "source": "https://grupocredicorp.com/wp-content/uploads/2024/10/CREDICORP_Logo-header.svg"},
        {"file": "logo-bcp.svg", "alt": "BCP", "bg": "#ffffff", "source": "https://grupocredicorp.com/wp-content/uploads/2024/09/BCP-logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Peru's largest financial group as five discs: BCP's cards on Visa and Amex, Yape moving money "
               "account to account for 16.7 million people, and Mastercard only at the edges, through Tenpo in Chile.",
    "stats": [
        {"label": "ROE 2Q26", "value": "20.3%"},
        {"label": "Yape monthly users", "value": "16.7m"},
        {"label": "BCP loan share", "value": "33%"},
        {"label": "Net income 2025", "value": "S/6.9bn"},
    ],
    "page": "Credicorp_BCP_Platform.html",
    "notes": (
        ("Research notes", "Credicorp_BCP_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "visacredit": {"apis": ["bin_lookup", "consumer_clarity"], "use_cases": ["bin_lookup", "consumer_clarity"]},
        "tenpo": {"apis": ["automatic_billing_updater", "transaction_notifications"], "use_cases": ["recurring", "txnotify"],
                  "bundles": ["issuer_toolkit", "subscriptions"]},
        "yapepay": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "interop": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["identity"]},
        "culqi": {"apis": ["merchant_identifier", "match", "places"], "use_cases": ["psi", "places"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        # L3 Services
        "scams": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "promos": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "retail": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "smallbiz": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L5 Access
        "yapeapp": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "pfm_stack", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "yape": ("pfm_stack", "loyalty_stack"),
        "card": ("issuer_toolkit",),
    },
}
