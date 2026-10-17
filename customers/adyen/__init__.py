"""Adyen N.V.

The page (``Adyen_Platform.html``) reads the Amsterdam payments platform as
five discs, Foundation to Access, with its reported pillars (Digital, Unified
Commerce, Platforms), a Mastercard lens (Mastercard in every flow, Visa at
parity, and a router that picks the cheaper rail) and ten journeys, two of
them for Mastercard. Public sources as at 17 October 2026; the research behind
it is in ``Adyen_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``adyen_inventory.py`` and ``adyen_story.py``::

    python customers/build_page.py adyen
"""

CUSTOMER = {
    "id": "adyen",
    "order": 230,
    "name": "Adyen",
    "short": "Adyen",
    "brands": ["Adyen", "Adyen Uplift", "Adyen Issuing", "Adyen Capital", "Talon.One", "Orb"],
    "country": "Netherlands",
    "region": "Global",
    "type": "payments",
    "accent": "#0abf53",   # Adyen green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Adyen", "bg": "#ffffff", "source": "https://www.adyen.com/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A global payments platform as five discs: €1.39 trillion of volume on one in-house stack, "
               "Mastercard in every flow and Visa at parity, with routing that favours the cheaper rail.",
    "stats": [
        {"label": "Volume 2025", "value": "€1.39tn"},
        {"label": "Net revenue H1 2026", "value": "€1.30bn"},
        {"label": "EBITDA margin 2025", "value": "53%"},
        {"label": "Terminals", "value": "838k"},
    ],
    "page": "Adyen_Platform.html",
    "notes": (
        ("Research notes", "Adyen_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "acquiring": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "issuing": {"apis": ["business_payment_controls", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "virtualcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "cardpayouts": {"apis": ["enhanced_currency_conversion_calculator"]},
        "paybybank": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L3 Services
        "tokens": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "clicktopay": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring", "bin_lookup"], "bundles": ["subscriptions"]},
        "risk": {"apis": ["consumer_clarity", "match"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "talonone": {"apis": ["offers_merchant_content", "offers_for_publishers"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "ap4m": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L4 Business lines
        "unified": {"apis": ["merchant_identifier", "carbon_calculator"], "bundles": ["sustainability"]},
        "platforms": {"apis": ["merchant_identifier", "match"], "bundles": ["acquirer_risk"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "subscriptions"),
        "mcnow": ("acquirer_risk", "subscriptions", "issuer_toolkit"),
        "accept": ("acquirer_risk", "subscriptions"),
        "platform": ("acquirer_risk", "issuer_toolkit"),
        "store": ("loyalty_stack", "sustainability"),
    },
}
