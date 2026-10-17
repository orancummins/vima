"""ING Groep N.V.

The page (``ING_Platform.html``) reads the Amsterdam-based bank as five
discs, Foundation to Access, with the segments it reports (Retail
Netherlands, Belgium, Germany and Other, and Wholesale Banking), a Mastercard
lens (a dual-sourced bank, with Wero rising beside both networks) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``ING_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``ing_inventory.py``
and ``ing_story.py``::

    python customers/build_page.py ing
"""

CUSTOMER = {
    "id": "ing",
    "order": 260,
    "name": "ING Groep",
    "short": "ING",
    "brands": ["ING", "ING-DiBa", "ING Bank Śląski", "ING Belgium"],
    "country": "Netherlands",
    "region": "Europe",
    "type": "bank",
    "accent": "#ff6200",   # ING orange, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "ING", "bg": "#ffffff", "source": "https://www.ing.com/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A mobile-first Dutch bank as five discs: 41 million customers, debit split between Visa and Mastercard "
               "by design, an agentic pilot with Mastercard, and Wero rising beside both.",
    "stats": [
        {"label": "Customers", "value": "41m"},
        {"label": "Net result 2025", "value": "€6.3bn"},
        {"label": "RoTE 2Q26", "value": "17.0%"},
        {"label": "Dutch debit cards", "value": "~10m"},
    ],
    "page": "ING_Platform.html",
    "notes": (
        ("Research notes", "ING_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "nldebit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "enrichment"], "bundles": ["pfm_stack"]},
        "bedebit": {"apis": ["transaction_notifications", "merchant_identifier"], "use_cases": ["txnotify", "enrichment"], "bundles": ["merchant_resolution"]},
        "decredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "plcredit": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "plpay": {"apis": ["automatic_billing_updater", "consumer_clarity"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "roacquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "wero": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L3 Services
        "agentpilot": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["identity", "enrichment"], "bundles": ["merchant_resolution"]},
        "monitoring": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "subs": {"apis": ["offers_for_publishers", "offers_merchant_content", "easy_savings"], "use_cases": ["specials", "pfm"], "bundles": ["loyalty_stack", "subscriptions"]},
        # L4 Business lines
        "business": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "upgrader": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "merchant_resolution"),
        "mcnow": ("pfm_stack", "subscriptions"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "agent": ("merchant_resolution",),
        "home": ("sustainability",),
    },
}
