"""Chime Financial, Inc.

The page (``Chime_Platform.html``) reads the US digital bank as five discs,
Foundation to Access, with its two revenue lines (Payments and
Platform-related), a Mastercard lens (an all-Visa neobank about to own its
own issuer) and nine journeys, two of them for Mastercard. Public sources as
at 17 October 2026; the research behind it is in ``Chime_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``chime_inventory.py`` and ``chime_story.py``::

    python customers/build_page.py chime
"""

CUSTOMER = {
    "id": "chime",
    "order": 1360,
    "name": "Chime",
    "short": "Chime",
    "brands": ["Chime", "Chime Card", "SpotMe", "MyPay", "Chime Prime", "Chime Workplace"],
    "country": "United States",
    "region": "Americas",
    "type": "digital",
    "accent": "#1ec677",   # Chime green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Chime", "bg": "#ffffff",
         "source": "https://images.ctfassets.net/ao7gxs2zk32d/yotdxJL87qeGLqgbdb678/29b00551376d6a7ba307dc4a042c1dd1/chime_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A US digital bank as five discs: 10.4 million active members on Visa debit and credit, GAAP profit in "
               "2026, and a deal to buy Stride Bank that hands Chime its own issuer in 2027.",
    "stats": [
        {"label": "Active members", "value": "10.4m"},
        {"label": "Revenue Q2 2026", "value": "$670m"},
        {"label": "Purchase volume 2025", "value": "$134bn"},
        {"label": "Stride Bank deal", "value": "$590m"},
    ],
    "page": "Chime_Platform.html",
    "notes": (
        ("Research notes", "Chime_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "consumer_clarity", "bin_lookup"],
                  "use_cases": ["txnotify", "consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "chimecard": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"],
                      "use_cases": ["recurring", "consumer_clarity"], "bundles": ["issuer_toolkit", "subscriptions"]},
        "oit": {"apis": ["bin_lookup"], "use_cases": ["bin_lookup"]},
        "linkcards": {"apis": ["bin_lookup", "open_finance"], "use_cases": ["identity", "bin_lookup"]},
        # L3 Services
        "riskmodels": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "chimeprime": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities", "benefits_eligibility"],
                       "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "alerts": {"apis": ["transaction_notifications", "merchant_identifier"], "use_cases": ["txnotify", "enrichment"],
                   "bundles": ["merchant_resolution"]},
        # L4 Business lines
        "mypay": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "instantloans": {"apis": ["open_finance"], "use_cases": ["identity", "pfm"]},
        "checking": {"apis": ["consumer_clarity", "merchant_identifier", "easy_savings"], "use_cases": ["pfm", "enrichment"],
                     "bundles": ["pfm_stack"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "merchant_resolution"),
        "mcnow": ("issuer_toolkit",),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "prime": ("loyalty_stack",),
        "credit": ("issuer_toolkit", "subscriptions"),
    },
}
