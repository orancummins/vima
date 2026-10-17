"""Banco Itaú Paraguay S.A.

The page (``Itau_Paraguay_Platform.html``) reads Itaú Unibanco's Paraguayan bank as five
discs, Foundation to Access, with the segments it reports (Personal Banking, Business Banking,
Institutional Treasury), a Mastercard lens (debit on Mastercard, the digital edge on Visa) and
ten journeys, two of them for Mastercard. Public sources as at 17 October 2026; the research
behind it is in ``Itau_Paraguay_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the template and swaps in
the data from ``page_data.py``, ``itauparaguay_inventory.py`` and ``itauparaguay_story.py``::

    python customers/build_page.py itauparaguay
"""

CUSTOMER = {
    "id": "itauparaguay",
    "order": 430,
    "name": "Itaú Paraguay",
    "short": "Itaú Paraguay",
    "brands": ["Itaú", "Personal Bank", "Itaú Campo", "Itaú BBA", "Pik", "Tienda Naranja"],
    "country": "Paraguay",
    "region": "Latin America",
    "type": "bank",
    "accent": "#ff6200",   # Itaú orange, from itau.com.py's stylesheet
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Itaú Paraguay", "bg": "#ff6200", "source": "https://www.itau.com.py/images/redis/logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Itaú Unibanco's Paraguayan bank as five discs: the largest card book by balances, every debit card "
               "on Mastercard, while Visa holds most credit programmes and the only Click to Pay.",
    "stats": [
        {"label": "Customers", "value": "726k+"},
        {"label": "Assets Sep 2026", "value": "Gs 40.7tn"},
        {"label": "Card balances share", "value": "35.6%"},
        {"label": "ROAE 2025", "value": "20.3%"},
    ],
    "page": "Itau_Paraguay_Platform.html",
    "notes": (
        ("Research notes", "Itau_Paraguay_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit", "subscriptions"]},
        "premium": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "c2p": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "pik": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "fx": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "places"], "bundles": ["loyalty_stack"]},
        "openapi": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L4 Business lines
        "accounts": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
        "corpcard": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "auto": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "pfm_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "cards": ("loyalty_stack", "subscriptions"),
    },
}
