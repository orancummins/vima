"""TD Bank Group (The Toronto-Dominion Bank).

The page (``TD_Bank_Group_Platform.html``) reads TD Canada Trust and TD Bank in
the US as five discs, Foundation to Access, with the segments it reports
(Canadian Personal & Commercial Banking, U.S. Banking, Wealth Management &
Insurance, Wholesale Banking, Corporate), a Mastercard lens (a Visa bank whose
Mastercard business came with MBNA and Target) and ten journeys, two of them
for Mastercard. Public sources as at 17 October 2026; the research behind it
is in ``TD_Bank_Group_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``tdbank_inventory.py``
and ``tdbank_story.py``::

    python customers/build_page.py tdbank
"""

CUSTOMER = {
    "id": "tdbank",
    "order": 1180,
    "name": "TD Bank Group",
    "short": "TD",
    "brands": ["TD Canada Trust", "TD Bank", "MBNA", "TD Wealth", "TD Direct Investing", "TD Insurance", "TD Securities",
               "TD Cowen", "TD Auto Finance"],
    "country": "Canada",
    "region": "Americas",
    "type": "bank",
    "accent": "#54b948",   # TD green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "TD Bank Group", "bg": "#ffffff",
         "source": "https://commons.wikimedia.org/wiki/File:Toronto-Dominion_Bank_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "TD Canada Trust and TD Bank in the US as five discs: its own cards on Visa in both countries, Mastercard "
               "through MBNA, Amazon.ca and Target, and a US bank under a US$434 billion asset cap.",
    "stats": [
        {"label": "Assets", "value": "C$2.1tn"},
        {"label": "Clients", "value": "28.2m"},
        {"label": "Adj. ROE Q3 2026", "value": "16.0%"},
        {"label": "US asset cap", "value": "US$434bn"},
    ],
    "page": "TD_Bank_Group_Platform.html",
    "notes": (
        ("Research notes", "TD_Bank_Group_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mbna": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                 "bundles": ["issuer_toolkit"]},
        "amazonca": {"apis": ["offers_for_publishers", "automatic_billing_updater", "merchant_identifier"], "use_cases": ["recurring", "specials"],
                     "bundles": ["subscriptions", "loyalty_stack"]},
        "target": {"apis": ["offers_merchant_content", "consumer_clarity", "merchant_identifier"], "use_cases": ["specials", "enrichment"],
                   "bundles": ["loyalty_stack"]},
        "usdebit": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "tdms": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "globaltransfer": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "monitoring": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "clari": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["merchant_resolution"]},
        "myspend": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
        "partnerloyalty": {"apis": ["offers_for_publishers", "offers_merchant_content", "places"], "use_cases": ["specials", "places"],
                           "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "commercial": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        "uscredit": {"apis": ["benefits_eligibility", "bin_lookup"], "use_cases": ["findacard", "bin_lookup"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "merchant_resolution", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "mbna": ("issuer_toolkit", "subscriptions"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "everyday": ("pfm_stack", "merchant_resolution"),
    },
}
