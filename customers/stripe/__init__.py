"""Stripe.

The page (``Stripe_Platform.html``) reads Stripe, the payments company, as
five discs, Foundation to Access: licences and the payments foundation model,
the rails (acquiring, payouts, Issuing, stablecoins), the engine room (Radar,
Link, agentic commerce), what it sells (Payments, Connect, Billing, Capital,
Atlas, OpenRouter) and its front doors, with a Mastercard lens and eleven
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
Stripe is private, so volumes are its own claims and revenue is press
estimates. The research behind it is in ``Stripe_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``stripe_foundation.py``, ``stripe_inventory.py`` and ``stripe_story.py``::

    python customers/build_page.py stripe
"""

CUSTOMER = {
    "id": "stripe",
    "order": 40,
    "name": "Stripe",
    "short": "Stripe",
    "brands": ["Stripe", "Link", "Bridge", "Privy", "Tempo"],
    "country": "United States & Ireland",
    "region": "Global",
    "accent": "#635bff",   # Stripe blurple, on the Customers tab card
    "as_of": "17 October 2026",
    "tagline": "Payments infrastructure that moved $1.9 trillion in 2025 as five discs, building its own rails "
               "in stablecoins and agentic commerce while carrying every network, Mastercard among them.",
    "stats": [
        {"label": "Volume 2025", "value": "$1.9tn"},
        {"label": "Businesses", "value": "5m+"},
        {"label": "Link users", "value": "300m+"},
        {"label": "Valuation", "value": "$159bn"},
    ],
    "page": "Stripe_Platform.html",
    "notes": (
        ("Research notes", "Stripe_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "acquiring": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"],
                      "bundles": ["acquirer_risk"]},
        "globalpayouts": {"apis": ["enhanced_currency_conversion_calculator"]},
        "issuing": {"apis": ["business_payment_controls", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "treasury": {"apis": ["business_payment_controls"]},
        "fx": {"apis": ["enhanced_currency_conversion_calculator"]},
        # L3 Services
        "disputes": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "finconnect": {"apis": ["open_finance", "open_finance_eu"], "use_cases": ["identity", "enrichment"],
                       "bundles": ["pfm_stack"]},
        "authboost": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["psi", "recurring"],
                      "bundles": ["subscriptions"]},
        "data": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment"]},
        # L4 Business lines
        "checkout": {"apis": ["bin_lookup", "enhanced_currency_conversion_calculator"], "use_cases": ["bin_lookup"]},
        "connect": {"apis": ["merchant_identifier"], "bundles": ["acquirer_risk"]},
        "billing": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "capital": {"apis": ["open_finance"], "use_cases": ["enrichment"]},
        # L5 Access
        "climate": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("merchant_resolution", "subscriptions", "sustainability"),
        "mcnow": ("issuer_toolkit", "subscriptions"),
        "scale": ("acquirer_risk", "merchant_resolution"),
        "subs": ("subscriptions",),
        "cards": ("issuer_toolkit", "pfm_stack"),
        "market": ("acquirer_risk",),
    },
}
