"""Banco Santander, S.A.

The page (``Santander_Platform.html``) reads the eurozone's most valuable
bank as five discs, Foundation to Access, with the five global businesses it
reports (Retail & Commercial, Openbank, CIB, Wealth & Insurance, Payment
Solutions) and its nine core markets, a Mastercard lens (UK and Mexico debit,
first in agentic) and ten journeys, two of them for Mastercard. Public sources
as at 17 October 2026; the research behind it is in
``Santander_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``santander_inventory.py`` and ``santander_story.py``::

    python customers/build_page.py santander
"""

CUSTOMER = {
    "id": "santander",
    "order": 110,
    "name": "Banco Santander",
    "short": "Santander",
    "brands": ["Santander", "Openbank", "Getnet", "TSB", "Ebury"],
    "country": "Spain",
    "region": "Europe & Latin America",
    "accent": "#ec0000",   # Santander red, on the Customers tab card
    "as_of": "17 October 2026",
    "tagline": "The eurozone's most valuable bank as five discs: 182.5 million customers in nine markets, Mastercard "
               "debit in the UK and Mexico, and Europe's first live AI-agent payment.",
    "stats": [
        {"label": "Assets", "value": "€1.95tn"},
        {"label": "Customers", "value": "182.5m"},
        {"label": "Getnet H1 2026", "value": "€129bn"},
        {"label": "Agent Pay", "value": "Europe first"},
    ],
    "page": "Santander_Platform.html",
    "notes": (
        ("Research notes", "Santander_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "ukcards": {"apis": ["transaction_notifications", "bin_lookup", "consumer_clarity"],
                    "use_cases": ["txnotify", "consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "mxcards": {"apis": ["bin_lookup", "transaction_notifications"], "use_cases": ["txnotify"],
                    "bundles": ["issuer_toolkit"]},
        "tokens": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring"],
                   "bundles": ["subscriptions"]},
        "getnet": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"],
                   "bundles": ["acquirer_risk"]},
        "getnetagent": {"apis": ["merchant_identifier"], "bundles": ["acquirer_risk"]},
        "ebury": {"apis": ["enhanced_currency_conversion_calculator"]},
        # L3 Services
        "agentpay": {"apis": ["bin_lookup"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "datalab": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"],
                    "bundles": ["pfm_stack"]},
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "select": {"apis": ["priceless_cities", "benefits_eligibility", "offers_for_publishers"],
                   "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "spain": {"apis": ["open_finance_eu", "consumer_clarity"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        "smegrowth": {"apis": ["business_payment_controls", "open_finance_eu"]},
        "ukretail": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"],
                     "bundles": ["merchant_resolution"]},
        "openbankeu": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L5 Access
        "oneapp": {"apis": ["consumer_clarity", "carbon_calculator"], "use_cases": ["consumer_clarity"],
                   "bundles": ["merchant_resolution", "sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("subscriptions", "acquirer_risk", "merchant_resolution"),
        "mcnow": ("issuer_toolkit", "subscriptions"),
        "everyday": ("pfm_stack", "issuer_toolkit"),
        "agent": ("subscriptions",),
        "merchant": ("acquirer_risk",),
        "select": ("loyalty_stack",),
    },
}
