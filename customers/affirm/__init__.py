"""Affirm Holdings, Inc.

The page (``Affirm_Platform.html``) reads the pay-over-time lender as five
discs, Foundation to Access, with its revenue lines (merchant network, card
network, interest, loan sales and servicing), a Mastercard lens (a Visa house,
with Mastercard at the edges) and ten journeys, two of them for Mastercard.
Public sources as at 17 October 2026; the research behind it is in
``Affirm_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``affirm_inventory.py`` and ``affirm_story.py``::

    python customers/build_page.py affirm
"""

CUSTOMER = {
    "id": "affirm",
    "order": 1320,
    "name": "Affirm Holdings",
    "short": "Affirm",
    "brands": ["Affirm", "Affirm Card", "Affirm Money", "Affirm Edge", "AdaptAI"],
    "country": "United States",
    "region": "Americas",
    "type": "wallet",
    "accent": "#4a4af4",   # Affirm blue, the site's primary colour
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Affirm", "bg": "#13131f", "source": "https://www.affirm.com/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The pay-over-time lender as five discs: $50.2 billion of GMV for 27.8 million shoppers, an Affirm Card "
               "on Visa, plans on banks' debit cards through Fiserv, and a bank charter pending.",
    "stats": [
        {"label": "GMV FY2026", "value": "$50.2bn"},
        {"label": "Active consumers", "value": "27.8m"},
        {"label": "Revenue FY2026", "value": "$4.26bn"},
        {"label": "Card users", "value": "5.2m"},
    ],
    "page": "Affirm_Platform.html",
    "notes": (
        ("Research notes", "Affirm_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "affirmcard": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "pfm"], "bundles": ["issuer_toolkit"]},
        "vcn": {"apis": ["bin_lookup"], "use_cases": ["bin_lookup"]},
        "fiservdebit": {"apis": ["open_finance", "transaction_notifications"], "use_cases": ["identity", "txnotify"], "bundles": ["issuer_toolkit"]},
        "monthly": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "repay": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L3 Services
        "fraud": {"apis": ["consumer_clarity", "match"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "adaptai": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "ap2": {"apis": ["merchant_identifier", "bin_lookup"], "use_cases": ["enrichment"]},
        # L4 Business lines
        "money": {"apis": ["easy_savings", "consumer_clarity"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        "merchants": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "uk": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L5 Access
        "mcgw": {"apis": ["merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "merchant_resolution", "loyalty_stack"),
        "mcnow": ("merchant_resolution",),
        "card": ("issuer_toolkit", "pfm_stack"),
        "merch": ("acquirer_risk", "merchant_resolution"),
        "bank": ("issuer_toolkit",),
    },
}
