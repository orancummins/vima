"""National Commercial Bank Jamaica (NCB Financial Group).

The page (``National_Commercial_Bank_Jamaica_Platform.html``) reads Jamaica's
largest bank as five discs, Foundation to Access, with the segments its parent
reports (Consumer & SME, Payment Services, Corporate & Commercial, Treasury and
Wealth, Insurance), a Mastercard lens (Mastercard in credit and prepaid, Visa on
every debit card) and ten journeys, two of them for Mastercard. Public sources
as at 17 October 2026; the research behind it is in
``National_Commercial_Bank_Jamaica_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``ncb_inventory.py``
and ``ncb_story.py``::

    python customers/build_page.py ncb
"""

CUSTOMER = {
    "id": "ncb",
    "order": 470,
    "name": "National Commercial Bank Jamaica",
    "short": "NCB",
    "brands": ["NCB", "NCB Financial Group", "Lynk", "NCB Capital Markets", "Guardian Group", "Clarien"],
    "country": "Jamaica",
    "region": "Latin America",
    "accent": "#01529a",   # NCB blue, from jncb.com and the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "NCB", "bg": "#01529a",
         "source": "https://www.jncb.com/wp-content/uploads/sites/2/2026/06/NCB-Logo-White.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Jamaica's largest bank as five discs: about 70% of the island's card terminals, Visa on every debit "
               "card, credit split with Mastercard, and the Lynk wallet for people who pay in cash.",
    "stats": [
        {"label": "Group assets", "value": "J$2.43tn"},
        {"label": "Deposits", "value": "J$844bn"},
        {"label": "Share of POS", "value": "~70%"},
        {"label": "Lynk users", "value": "~300k"},
    ],
    "page": "National_Commercial_Bank_Jamaica_Platform.html",
    "notes": (
        ("Research notes", "National_Commercial_Bank_Jamaica_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "mccredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "bizcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "prepaid": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify"], "bundles": ["subscriptions"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "epos": {"apis": ["merchant_identifier"], "use_cases": ["psi"], "bundles": ["merchant_resolution"]},
        "mcmsme": {"apis": ["places", "merchant_identifier"], "use_cases": ["places"], "bundles": ["acquirer_risk"]},
        "ncbpay": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["enrichment", "txnotify"], "bundles": ["pfm_stack"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["enrichment"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["identity", "txnotify"]},
        "miles": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials", "findacard"],
                  "bundles": ["loyalty_stack"]},
        # L2 wallets
        "lynk": {"apis": ["consumer_clarity"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "pfm_stack"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "travel": ("loyalty_stack",),
        "cashless": ("pfm_stack", "subscriptions"),
    },
}
