"""BRAC Bank PLC.

The page (``BRAC_Bank_Platform.html``) reads Bangladesh's leading SME bank as
five discs, Foundation to Access, with the segments it reports (SME, Retail,
Wholesale, plus subsidiaries such as bKash), a Mastercard lens (a Visa-led
bank whose Mastercard business is growing, mainly through bKash) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``BRAC_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``brac_inventory.py`` and ``brac_story.py``::

    python customers/build_page.py brac
"""

CUSTOMER = {
    "id": "brac",
    "order": 840,
    "name": "BRAC Bank",
    "short": "BRAC Bank",
    "brands": ["BRAC Bank", "TARA", "Astha", "bKash", "BRAC Saajan", "BRAC EPL"],
    "country": "Bangladesh",
    "region": "Asia-Pacific",
    "type": "bank",
    "accent": "#006cb5",   # BRAC Bank blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "BRAC Bank", "bg": "#ffffff", "source": "https://www.bracbank.com/logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Bangladesh's leading SME bank as five discs: 2.3 million customers, Visa first and Mastercard second "
               "on its cards, and bKash's 84 million wallets receiving remittances on Mastercard Move.",
    "stats": [
        {"label": "Customers", "value": "2.3m"},
        {"label": "H1 2026 profit", "value": "BDT 14.2bn"},
        {"label": "bKash customers", "value": "84m"},
        {"label": "Astha users", "value": "1.2m"},
    ],
    "page": "BRAC_Bank_Platform.html",
    "notes": (
        ("Research notes", "BRAC_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mccredit": {"apis": ["bin_lookup", "consumer_clarity", "benefits_eligibility"], "use_cases": ["consumer_clarity", "findacard"],
                     "bundles": ["issuer_toolkit"]},
        "mcdebit": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["txnotify"],
                    "bundles": ["issuer_toolkit"]},
        "gpay": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring", "bin_lookup"], "bundles": ["subscriptions"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "gateways": {"apis": ["match", "bin_lookup"], "use_cases": ["bin_lookup"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "remitin": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "bkmove": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "settle_in"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "tara": {"apis": ["priceless_cities", "benefits_eligibility"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "smecards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L5 Access
        "astha": {"apis": ["consumer_clarity", "places"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "subscriptions"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("issuer_toolkit", "acquirer_risk"),
        "tara": ("loyalty_stack",),
    },
}
