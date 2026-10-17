"""Equity Bank (Equity Bank Kenya, part of Equity Group Holdings Plc).

The page (``Equity_Bank_Platform.html``) reads Kenya's second-largest bank and
its six-country group as five discs, Foundation to Access, with the businesses
it reports (Equity Bank Kenya, the regional banks, insurance and the
non-banking units), a Mastercard lens (a ten-year deal in a market that pays
by phone) and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in ``Equity_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``equitybank_inventory.py`` and ``equitybank_story.py``::

    python customers/build_page.py equitybank
"""

CUSTOMER = {
    "id": "equitybank",
    "order": 1100,
    "name": "Equity Bank",
    "short": "Equity",
    "brands": ["Equity Bank", "Equity BCDC", "Equitel", "Finserve", "Equity Insurance", "Equity Afya", "Equity Investment Bank"],
    "country": "Kenya",
    "region": "EEMEA",
    "accent": "#a32a29",   # Equity maroon, from the roof in the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Equity Bank", "bg": "#ffffff",
         "source": "https://equitygroupholdings.com/ke/ke/Content/assets/img/equity-bank-logo.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Kenya's second-largest bank as five discs: 23 million accounts in six countries, debit on Visa and "
               "Mastercard side by side under a ten-year Mastercard deal, while most money moves on Equitel, tills and M-Pesa.",
    "stats": [
        {"label": "Customer accounts", "value": "23.3m"},
        {"label": "Assets", "value": "KES 2.16tn"},
        {"label": "Merchants", "value": "1.4m"},
        {"label": "Digital share", "value": "89.7%"},
    ],
    "page": "Equity_Bank_Platform.html",
    "notes": (
        ("Research notes", "Equity_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"]},
        "premiumdebit": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator"], "use_cases": ["findacard"],
                         "bundles": ["issuer_toolkit"]},
        "corpcard": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "posacq": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "pwe": {"apis": ["merchant_identifier", "places"], "use_cases": ["places", "enrichment"], "bundles": ["merchant_resolution"]},
        "mccbs": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["consumer_clarity"]},
        # L3 Services
        "communitypass": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "cyber": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "aidata": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "apis": {"apis": ["open_finance", "bin_lookup"], "use_cases": ["bin_lookup"]},
        "carddeals": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("merchant_resolution", "acquirer_risk", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "cards": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack",),
    },
}
