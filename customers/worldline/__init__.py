"""Worldline SA.

The page (``Worldline_Platform.html``) reads the Paris payments processor as
five discs, Foundation to Access, with the segments it reports (Merchant
Services, Financial Services), a Mastercard lens (Agent Pay's European first,
on a home turf of domestic schemes) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``Worldline_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``worldline_inventory.py`` and ``worldline_story.py``::

    python customers/build_page.py worldline
"""

CUSTOMER = {
    "id": "worldline",
    "order": 190,
    "name": "Worldline",
    "short": "Worldline",
    "brands": ["Worldline", "PAYONE", "Global Collect", "Bambora", "Axepta", "equensWorldline"],
    "country": "France",
    "region": "Europe",
    "type": "payments",
    "accent": "#46beaa",   # Worldline teal, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Worldline", "bg": "#ffffff", "source": "https://worldline.com/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A European payments processor as five discs: €245 billion acquired in half a year and Europe's first "
               "live Agent Pay payment, on home markets run by domestic schemes and Wero.",
    "stats": [
        {"label": "Revenue 2025", "value": "€4.0bn"},
        {"label": "Acquiring H1 2026", "value": "€245bn"},
        {"label": "Merchants", "value": "1.2m"},
        {"label": "Cards processed", "value": "156m"},
    ],
    "page": "Worldline_Platform.html",
    "notes": (
        ("Research notes", "Worldline_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "acquiring": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "issuing": {"apis": ["bin_lookup", "consumer_clarity", "transaction_notifications"], "use_cases": ["txnotify", "consumer_clarity"],
                    "bundles": ["issuer_toolkit"]},
        "globalcollect": {"apis": ["enhanced_currency_conversion_calculator", "bin_lookup"], "use_cases": ["bin_lookup"]},
        "klarna": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "tokens": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "c2p": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "fraud": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["consumer_clarity", "txnotify"], "bundles": ["merchant_resolution"]},
        "agentpay": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "openbanking": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L4 Business lines
        "smb": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "enterprise": {"apis": ["merchant_identifier", "carbon_calculator"], "bundles": ["sustainability"]},
        # L1 Foundation
        "remediation": {"apis": ["match", "merchant_identifier"], "bundles": ["acquirer_risk", "merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "issuer_toolkit", "subscriptions"),
        "mcnow": ("subscriptions", "issuer_toolkit"),
        "shop": ("acquirer_risk",),
        "global": ("subscriptions", "merchant_resolution"),
        "bank": ("issuer_toolkit", "merchant_resolution"),
    },
}
