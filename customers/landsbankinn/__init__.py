"""Landsbankinn hf.

The page (``Landsbankinn_Platform.html``) reads Iceland's largest bank as five
discs, Foundation to Access, with the segments it reports (Personal Banking,
Corporate Banking, Asset Management & Capital Markets, TM tryggingar, Treasury
and other divisions), a Mastercard lens (a Visa issuer where Mastercard only
shows up at the till) and nine journeys, two of them for Mastercard. Public
sources as at 17 October 2026; the research behind it is in
``Landsbankinn_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``landsbankinn_inventory.py`` and ``landsbankinn_story.py``::

    python customers/build_page.py landsbankinn
"""

CUSTOMER = {
    "id": "landsbankinn",
    "order": 680,
    "name": "Landsbankinn",
    "short": "Landsbankinn",
    "brands": ["Landsbankinn", "TM", "Landsbréf", "Aukakrónur", "Yayland"],
    "country": "Iceland",
    "region": "Europe",
    "type": "bank",
    "accent": "#20446a",   # Landsbankinn navy, from the website's logo block
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Landsbankinn", "bg": "#20446a", "source": "https://www.landsbankinn.is/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Iceland's largest bank as five discs: 40% of the retail market, every card it issues on Visa, "
               "and an acquiring business with 27% of the market that takes Mastercard.",
    "stats": [
        {"label": "Retail share", "value": "40.2%"},
        {"label": "Total assets", "value": "ISK 2.4trn"},
        {"label": "ROE H1 2026", "value": "13.4%"},
        {"label": "Acquiring share", "value": "27%"},
    ],
    "page": "Landsbankinn_Platform.html",
    "notes": (
        ("Research notes", "Landsbankinn_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "bizcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "ecom": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["bin_lookup"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "elli": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "aukakronur": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "apis": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L4 Business lines
        "savings": {"apis": ["consumer_clarity"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        "carloans": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "loyalty_stack", "issuer_toolkit"),
        "mcnow": ("acquirer_risk", "merchant_resolution"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "everyday": ("pfm_stack",),
        "travel": ("issuer_toolkit", "loyalty_stack"),
    },
}
