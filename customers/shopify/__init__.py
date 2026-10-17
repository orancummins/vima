"""Shopify Inc.

The page (``Shopify_Platform.html``) reads the commerce platform through
payments, as five discs, Foundation to Access, with the revenue it reports
(subscription and merchant solutions), a Mastercard lens (accepted at every
checkout, but Shopify's own cards and agent work lean to Visa) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``Shopify_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``shopify_inventory.py`` and ``shopify_story.py``::

    python customers/build_page.py shopify
"""

CUSTOMER = {
    "id": "shopify",
    "order": 1340,
    "name": "Shopify",
    "short": "Shopify",
    "brands": ["Shopify", "Shopify Payments", "Shop Pay", "Shop Pay Installments", "Shopify Balance", "Shopify Credit", "Shopify Capital", "Shopify POS"],
    "country": "Canada",
    "region": "Global",
    "type": "merchant",
    "accent": "#95bf47",   # Shopify green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Shopify", "bg": "#ffffff", "source": "https://cdn.shopify.com/shopifycloud/brochure/assets/brand-assets/shopify-logo-primary-logo-456baa801ee66a0a435671082365958316831c9960c480451dd0330bcdae304f.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The commerce platform as five discs: $378.4 billion of GMV, Mastercard accepted at every checkout, "
               "but Shopify's own Balance and Credit cards are Visa and its agentic checkout names no network yet.",
    "stats": [
        {"label": "GMV 2025", "value": "$378bn"},
        {"label": "Q2 2026 GMV", "value": "$115.6bn"},
        {"label": "Payments share", "value": "65.6%"},
        {"label": "Shop Pay users", "value": "250m+"},
    ],
    "page": "Shopify_Platform.html",
    "notes": (
        ("Research notes", "Shopify_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "shoppayments": {"apis": ["merchant_identifier", "bin_lookup", "match"], "use_cases": ["psi", "bin_lookup"], "bundles": ["acquirer_risk"]},
        "shoppay": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "pos": {"apis": ["places", "merchant_identifier"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
        "markets": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "fraud": {"apis": ["match", "merchant_identifier"], "use_cases": ["identity"], "bundles": ["acquirer_risk"]},
        "copilot": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
        # L4 Business lines
        "balancecard": {"apis": ["business_payment_controls", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "credit": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "b2b": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "capital": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "campaigns": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L5 Access
        "aichannels": {"apis": ["merchant_identifier", "consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("merchant_resolution", "acquirer_risk", "issuer_toolkit"),
        "mcnow": ("acquirer_risk", "subscriptions"),
        "checkout": ("subscriptions", "merchant_resolution"),
        "money": ("issuer_toolkit",),
        "agent": ("merchant_resolution",),
    },
}
