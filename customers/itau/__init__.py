"""Itaú (Itaú Unibanco Holding).

The page (``Itau_Platform.html``) reads Latin America's largest private bank
as five discs, Foundation to Access: Retail (cards, payroll, mortgages,
SMEs, Rede) and Wholesale (Itaú BBA, Private, asset management, Latin
America), a Mastercard lens (both networks, leaning Mastercard since the
Hipercard migration) and ten journeys, two of them for Mastercard. Public
sources as at 17 October 2026; amounts in reais. The research behind it is
in ``Itau_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``itau_inventory.py``
and ``itau_story.py``::

    python customers/build_page.py itau
"""

CUSTOMER = {
    "id": "itau",
    "order": 60,
    "name": "Itaú Unibanco",
    "short": "Itaú",
    "brands": ["Itaú", "Itaú Personnalité", "Itaú BBA", "Rede", "Itaucard"],
    "country": "Brazil",
    "region": "Latin America",
    "type": "bank",
    "accent": "#ff6200",   # Itaú orange, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Itaú", "bg": "#ffffff", "source": "static/logos/financial-logos-500/01-financial-institutions/ita-unibanco.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Latin America's largest private bank as five discs: Brazil's number-one card issuer and acquirer, "
               "on Mastercard and Visa, with Hipercard's 15 million cards moved to Mastercard in 2025.",
    "stats": [
        {"label": "Assets", "value": "R$3.2tn"},
        {"label": "Card share", "value": "24%"},
        {"label": "ROE", "value": "24%"},
        {"label": "Hipercard to Mastercard", "value": "2025"},
    ],
    "page": "Itau_Platform.html",
    "notes": (
        ("Research notes", "Itau_research_notes.md"),
    ),
    "studio": {
        # L1 Foundation
        "esg": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        # L2 Rails
        "hipercard": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["bin_lookup", "recurring"]},
        "rede": {"apis": ["merchant_identifier", "match", "places"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "contaglobal": {"apis": ["enhanced_currency_conversion_calculator"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "openfinance": {"apis": ["open_finance"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "loyalty": {"apis": ["offers_for_publishers", "easy_savings", "priceless_cities"], "use_cases": ["findacard"],
                    "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "cards": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"],
                  "use_cases": ["bin_lookup", "consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "legend": {"apis": ["priceless_cities", "benefits_eligibility"], "use_cases": ["specials"]},
        "airline": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator"]},
        "sme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L5 Access
        "superapp": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"],
                     "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("merchant_resolution", "loyalty_stack", "issuer_toolkit", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "travel": ("loyalty_stack",),
        "corp": ("sustainability",),
    },
}
