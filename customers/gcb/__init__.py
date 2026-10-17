"""GCB Bank PLC.

The page (``GCB_Bank_Platform.html``) reads Ghana's largest bank as five
discs, Foundation to Access, with its business lines (personal banking, SME
and commercial, corporate, SOE and government, and treasury and trade), a
Mastercard lens (Ghana's first Mastercard bank, where Visa took the top tier
and mobile money moves the cash) and ten journeys, two of them for Mastercard.
Public sources as at 17 October 2026; the research behind it is in
``GCB_Bank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``gcb_inventory.py``
and ``gcb_story.py``::

    python customers/build_page.py gcb
"""

CUSTOMER = {
    "id": "gcb",
    "order": 1110,
    "name": "GCB Bank",
    "short": "GCB",
    "brands": ["GCB Bank", "G-Money", "GCB Capital", "ReadyCash", "Lite Pay", "Amber Club"],
    "country": "Ghana",
    "region": "EEMEA",
    "type": "bank",
    "accent": "#ffc72a",   # GCB eagle yellow, from the logo in the bank's 2025 tariff guide
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "GCB Bank", "bg": "#2f3d44",
         "source": "https://web.archive.org/web/20250421111644/https://www.gcbbank.com.gh/downloads/informational/432-2025-tariff-guide/file"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Ghana's largest bank as five discs: ReadyCash on gh-link, debit on both Visa and Mastercard, the premium "
               "tier on Visa, a Corporate Mastercard since 2008, and its own G-Money wallet where mobile money moves the cash.",
    "stats": [
        {"label": "Assets Jun 2026", "value": "GH¢67bn"},
        {"label": "Share of loans", "value": "17.8%"},
        {"label": "Profit H1 2026", "value": "GH¢1.23bn"},
        {"label": "Branches", "value": "184"},
    ],
    "page": "GCB_Bank_Platform.html",
    "notes": (
        ("Research notes", "GCB_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "hnw": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "corpmc": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "visabiz": {"apis": ["business_payment_controls"]},
        "litepay": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "gmoney": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["pfm", "txnotify"], "bundles": ["pfm_stack"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        "amber": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "gcbpay": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L4 Business lines, L5 Access
        "sme": {"apis": ["business_payment_controls", "places"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
        "app": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "issuer_toolkit", "acquirer_risk"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "everyday": ("pfm_stack", "issuer_toolkit"),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "wallet": ("pfm_stack",),
    },
}
