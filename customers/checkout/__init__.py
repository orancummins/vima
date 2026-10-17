"""Checkout.com.

The page (``Checkout_com_Platform.html``) reads the enterprise payments
company as five discs, Foundation to Access, with its product lines
(acceptance, money movement, protect and optimise), a Mastercard lens (an
agentic partner, with Visa ahead in money movement) and nine journeys, two of
them for Mastercard. Checkout.com is private: figures are its own releases and
press, as at 17 October 2026; the research behind it is in
``Checkout_com_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``checkout_inventory.py`` and ``checkout_story.py``::

    python customers/build_page.py checkout
"""

CUSTOMER = {
    "id": "checkout",
    "order": 330,
    "name": "Checkout.com",
    "short": "Checkout.com",
    "brands": ["Checkout.com", "Flow", "Intelligent Acceptance", "Remember Me"],
    "country": "United Kingdom",
    "region": "Global",
    "accent": "#186aff",   # Checkout.com blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Checkout.com", "bg": "#ffffff", "source": "static/logos/financial-logos-500/02-payments-and-processors/checkout-com.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "An enterprise payments platform as five discs: $300 billion of volume and a new US charter, a "
               "Mastercard Agent Pay launch partner, with Visa ahead in payouts and issuing.",
    "stats": [
        {"label": "Volume 2025", "value": "$300bn+"},
        {"label": "Annualised revenue", "value": "$750m"},
        {"label": "Acquiring licences", "value": "10"},
        {"label": "Valuation", "value": "$12bn"},
    ],
    "page": "Checkout_com_Platform.html",
    "notes": (
        ("Research notes", "Checkout_com_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "acquiring": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "issuing": {"apis": ["business_payment_controls", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "wholesale": {"apis": ["business_payment_controls", "enhanced_currency_conversion_calculator"], "bundles": ["issuer_toolkit"]},
        "move": {"apis": ["enhanced_currency_conversion_calculator"]},
        # L3 Services
        "ia": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["bin_lookup", "recurring"], "bundles": ["subscriptions"]},
        "tokens": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "fraud": {"apis": ["consumer_clarity", "match"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "agentpay": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L4 Business lines
        "enterprise": {"apis": ["merchant_identifier", "carbon_calculator"], "bundles": ["sustainability"]},
        "platforms": {"apis": ["merchant_identifier", "match"], "bundles": ["acquirer_risk"]},
    },
    "journey_bundles": {
        "mcnext": ("merchant_resolution", "subscriptions", "issuer_toolkit"),
        "mcnow": ("subscriptions", "issuer_toolkit"),
        "accept": ("acquirer_risk", "subscriptions"),
        "agent": ("subscriptions",),
        "platform": ("acquirer_risk", "issuer_toolkit"),
    },
}
