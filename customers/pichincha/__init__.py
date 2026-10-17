"""Banco Pichincha C.A.

The page (``Banco_Pichincha_Platform.html``) reads Ecuador's largest bank as
five discs, Foundation to Access, with its lines of business (personal,
corporate and SME, microfinance, international, group), a Mastercard lens
(Visa first, Mastercard a strong second card) and nine journeys, two of them
for Mastercard. Public sources as at 17 October 2026; the research behind it
is in ``Banco_Pichincha_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``pichincha_inventory.py`` and ``pichincha_story.py``::

    python customers/build_page.py pichincha
"""

CUSTOMER = {
    "id": "pichincha",
    "order": 410,
    "name": "Banco Pichincha",
    "short": "Pichincha",
    "brands": ["Banco Pichincha", "Deuna", "Mi Vecino", "Pichincha Miles", "Banco Pichincha España", "Pibank"],
    "country": "Ecuador",
    "region": "Latin America",
    "type": "bank",
    "accent": "#ffdd00",   # Pichincha yellow, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Banco Pichincha", "bg": "#ffffff", "source": "https://www.pichincha.com/themes/custom/pichincha_theme/logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Ecuador's largest bank as five discs: 6.5 million customers and 28% of banking assets, Visa on every "
               "debit card and Mastercard a strong second on credit, beside its own Deuna QR wallet.",
    "stats": [
        {"label": "Customers", "value": "6.5m"},
        {"label": "Assets Mar 2026", "value": "$22.3bn"},
        {"label": "Profit 2025", "value": "$240m"},
        {"label": "Digital transactions", "value": "83%"},
    ],
    "page": "Banco_Pichincha_Platform.html",
    "notes": (
        ("Research notes", "Banco_Pichincha_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mccredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "debitdigital": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "quantum": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "mcbiz": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "deunamerchant": {"apis": ["merchant_identifier", "places"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
        "visadirect": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "miles": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "coops": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L4 Business lines and L5 Access
        "agro": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        "app": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "issuer_toolkit", "acquirer_risk"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack",),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "premium": ("loyalty_stack",),
    },
}
