"""Nexi Group (Nexi S.p.A.).

The page (``Nexi_Platform.html``) reads the Milan payments group as five
discs, Foundation to Access, with the segments it reports (Merchant Solutions,
Issuing Solutions, Digital Banking Solutions), a Mastercard lens (Mastercard
owns Nets' old rails; Visa won Nexi Ready) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``Nexi_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``nexi_inventory.py`` and ``nexi_story.py``::

    python customers/build_page.py nexi
"""

CUSTOMER = {
    "id": "nexi",
    "order": 180,
    "name": "Nexi Group",
    "short": "Nexi",
    "brands": ["Nexi", "Nets", "SIA", "Computop", "Przelewy24"],
    "country": "Italy",
    "region": "Europe",
    "type": "payments",
    "accent": "#2d32aa",   # Nexi blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Nexi", "bg": "#ffffff", "source": "https://www.nexigroup.com/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Europe's self-styled PayTech as five discs: €837 billion acquired and 140 million cards processed, "
               "open banking and Move on Mastercard, while Visa took the Nexi Ready launch.",
    "stats": [
        {"label": "Revenue 2025", "value": "€3.6bn"},
        {"label": "EBITDA margin", "value": "53%"},
        {"label": "Cards processed", "value": "140m"},
        {"label": "POS terminals", "value": "3m"},
    ],
    "page": "Nexi_Platform.html",
    "notes": (
        ("Research notes", "Nexi_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "acquiring": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "issuing": {"apis": ["bin_lookup", "consumer_clarity", "transaction_notifications"], "use_cases": ["txnotify", "consumer_clarity"],
                    "bundles": ["issuer_toolkit"]},
        "move": {"apis": ["enhanced_currency_conversion_calculator", "business_payment_controls"]},
        "apms": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "mcob": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "ethoca": {"apis": ["consumer_clarity", "match"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "agentic": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "nexiready": {"apis": ["bin_lookup", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "vas": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "checkout": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "cards": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["pfm", "txnotify"], "bundles": ["pfm_stack"]},
        "eurowag": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "merchant_resolution", "subscriptions"),
        "mcnow": ("merchant_resolution", "acquirer_risk"),
        "shop": ("acquirer_risk",),
        "online": ("subscriptions", "acquirer_risk"),
        "issue": ("issuer_toolkit", "loyalty_stack"),
    },
}
