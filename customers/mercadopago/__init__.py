"""Mercado Pago.

The page (``Mercado_Pago_Platform.html``) reads Mercado Libre's fintech arm
as five discs, Foundation to Access, with its lines (acquiring, fintech
services, credit), a Mastercard lens (in the Spanish-speaking wallets,
with Visa holding Brazil and the growing credit cards) and ten
journeys, two of them for Mastercard. Figures are MercadoLibre's own releases
and Mercado Pago's country sites, as at 17 October 2026; the research behind
it is in ``Mercado_Pago_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``mercadopago_inventory.py`` and ``mercadopago_story.py``::

    python customers/build_page.py mercadopago
"""

CUSTOMER = {
    "id": "mercadopago",
    "order": 1370,
    "name": "Mercado Pago",
    "short": "Mercado Pago",
    "brands": ["Mercado Pago", "Mercado Crédito", "Point", "Meli+", "Meli Dólar", "Mercado Fondo"],
    "country": "Argentina",
    "region": "Latin America",
    "type": "wallet",
    "accent": "#00bcff",   # Mercado Pago blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Mercado Pago", "bg": "#ffffff", "source": "https://http2.mlstatic.com/frontend-assets/mp-web-navigation/ui-navigation/7.7.2/mercadopago/header/logo-v3-full.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Latin America's largest fintech as five discs: $12.6 billion of revenue and $101 billion of quarterly "
               "volume, Mastercard on the cards in Mexico debit, Argentina and Chile, and Visa on the Brazilian and "
               "Mexican credit cards that are growing fastest.",
    "stats": [
        {"label": "Revenue 2025", "value": "$12.6bn"},
        {"label": "TPV Q2 2026", "value": "$101bn"},
        {"label": "Monthly users", "value": "88m"},
        {"label": "Credit book", "value": "$16bn+"},
    ],
    "page": "Mercado_Pago_Platform.html",
    "notes": (
        ("Research notes", "Mercado_Pago_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "acquiring": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "point": {"apis": ["merchant_identifier", "bin_lookup"], "use_cases": ["psi", "bin_lookup"], "bundles": ["acquirer_risk"]},
        "checkout": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "arcc": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["txnotify", "consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "mxdebit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "brcc": {"apis": ["consumer_clarity", "enhanced_currency_conversion_calculator"], "use_cases": ["consumer_clarity"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "credit": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "security": {"apis": ["consumer_clarity"], "use_cases": ["identity"], "bundles": ["merchant_resolution"]},
        "meliplus": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "savings": {"apis": ["open_finance"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "marketplace": {"apis": ["merchant_identifier", "consumer_clarity"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
        "merchants": {"apis": ["business_payment_controls", "match"], "bundles": ["acquirer_risk"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "merchant_resolution", "subscriptions"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "card": ("issuer_toolkit", "loyalty_stack"),
        "accept": ("acquirer_risk",),
        "save": ("pfm_stack",),
    },
}
