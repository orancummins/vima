"""Wells Fargo & Company.

The page (``Wells_Fargo_Platform.html``) reads the San Francisco bank as five
discs, Foundation to Access, with the segments it reports (Consumer Banking &
Lending, Commercial Banking, Corporate & Investment Banking, Wealth &
Investment Management), a Mastercard lens (Visa at the core, Mastercard on the
partner cards) and nine journeys, two of them for Mastercard. Public sources
as at 17 October 2026; the research behind it is in
``Wells_Fargo_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``wellsfargo_inventory.py`` and ``wellsfargo_story.py``::

    python customers/build_page.py wellsfargo
"""

CUSTOMER = {
    "id": "wellsfargo",
    "order": 290,
    "name": "Wells Fargo",
    "short": "Wells Fargo",
    "brands": ["Wells Fargo", "Wells Fargo Advisors", "Wells Fargo Premier", "Wells Fargo Private Bank",
               "Wells Fargo Merchant Services", "Vantage"],
    "country": "United States",
    "region": "Americas",
    "accent": "#dd1e25",   # Wells Fargo red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Wells Fargo", "bg": "#ffffff", "source": "https://commons.wikimedia.org/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A $2.25 trillion American bank as five discs: freed from its asset cap, with its own credit cards and "
               "debit on Visa and Mastercard on the Choice, Expedia and small-business cards.",
    "stats": [
        {"label": "Assets", "value": "$2.25tn"},
        {"label": "ROTCE Q3 2026", "value": "16.3%"},
        {"label": "Mobile-active", "value": "34m"},
        {"label": "Branches", "value": "4,068"},
    ],
    "page": "Wells_Fargo_Platform.html",
    "notes": (
        ("Research notes", "Wells_Fargo_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "autograph": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                      "bundles": ["issuer_toolkit"]},
        "choice": {"apis": ["benefits_eligibility", "offers_for_publishers"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "onekey": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator", "priceless_cities"], "use_cases": ["specials"],
                   "bundles": ["loyalty_stack"]},
        "signify": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "commcard": {"apis": ["business_payment_controls"]},
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "merchant": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "finicity": {"apis": ["open_finance"], "use_cases": ["identity", "enrichment"]},
        "fraud": {"apis": ["open_finance", "transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        "fargo": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "premier": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "consumer_clarity"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "loyalty_stack", "issuer_toolkit"),
        "mcnow": ("loyalty_stack", "issuer_toolkit"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "travel": ("loyalty_stack",),
    },
}
