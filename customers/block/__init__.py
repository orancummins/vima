"""Block, Inc.

The page (``Block_Platform.html``) reads the company behind Square, Cash App
and Afterpay as five discs, Foundation to Access, with the segments it reports
(Square, Cash App, and bitcoin, TIDAL and other), a Mastercard lens
(Mastercard on the seller's card, Visa in the Cash App wallet) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``Block_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``block_inventory.py`` and ``block_story.py``::

    python customers/build_page.py block
"""

CUSTOMER = {
    "id": "block",
    "order": 1270,
    "name": "Block",
    "short": "Block",
    "brands": ["Square", "Cash App", "Afterpay", "TIDAL", "Bitkey", "Proto"],
    "country": "United States",
    "region": "Global",
    "type": "wallet",
    "accent": "#191c1f",   # Block black, from the wordmark on block.xyz
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Block", "bg": "#ffffff", "source": "https://block.xyz/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Square, Cash App and Afterpay as five discs: $10.4 billion of gross profit and its own bank, "
               "Mastercard on the Square Debit Card, Visa on the Cash App Card, and a push to its own rails.",
    "stats": [
        {"label": "Gross profit 2025", "value": "$10.4bn"},
        {"label": "Square GPV 2025", "value": "$250bn"},
        {"label": "Cash App actives", "value": "59m"},
        {"label": "2026 guidance", "value": "$12.5bn"},
    ],
    "page": "Block_Platform.html",
    "notes": (
        ("Research notes", "Block_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "acquiring": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi", "bin_lookup"], "bundles": ["acquirer_risk"]},
        "sqdebit": {"apis": ["business_payment_controls", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "cashcard": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["consumer_clarity", "txnotify"], "bundles": ["issuer_toolkit"]},
        "flex": {"apis": ["bin_lookup", "consumer_clarity"], "use_cases": ["consumer_clarity"]},
        "instant": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["identity"]},
        "cashapppay": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L3 Services
        "fraud": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["consumer_clarity", "txnotify"], "bundles": ["merchant_resolution"]},
        "score": {"apis": ["open_finance"], "use_cases": ["identity", "pfm"]},
        "neighborhoods": {"apis": ["offers_for_publishers", "offers_merchant_content", "places"], "use_cases": ["specials", "places"], "bundles": ["loyalty_stack"]},
        "agentic": {"apis": ["merchant_identifier", "automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L4 Business lines
        "sqbanking": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "cashbanking": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "merchant_resolution", "subscriptions"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "sell": ("acquirer_risk", "issuer_toolkit"),
        "bank": ("pfm_stack", "issuer_toolkit"),
        "send": ("loyalty_stack",),
    },
}
