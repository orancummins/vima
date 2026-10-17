"""JSC Bank of Georgia, the Georgian bank of Lion Finance Group PLC.

The page (``Bank_of_Georgia_Platform.html``) reads Georgia's largest bank as
five discs, Foundation to Access, with the segments the group reports (Retail,
SME, Corporate & Investment Banking, with Ameriabank in Armenia and the other
businesses as context), a Mastercard lens (Visa and Mastercard side by side,
Amex on an exclusive deal, a Mastercard Corporate Card, and scheme fees under
pressure) and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in
``Bank_of_Georgia_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``bog_inventory.py`` and
``bog_story.py``::

    python customers/build_page.py bog
"""

CUSTOMER = {
    "id": "bog",
    "order": 930,
    "name": "Bank of Georgia",
    "short": "Bank of Georgia",
    "brands": ["Bank of Georgia", "SOLO", "Galt & Taggart", "Digital Area", "Ameriabank", "Lion Finance Group"],
    "country": "Georgia",
    "region": "EEMEA",
    "accent": "#ff5c0a",   # Bank of Georgia orange, from the website and the lion in the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Bank of Georgia", "bg": "#ffffff",
         "source": "https://upload.wikimedia.org/wikipedia/en/4/4c/Bank_of_Georgia_logo.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Georgia's largest bank as five discs: a million daily app users, more than half the country's card "
               "acquiring, and Visa and Mastercard side by side while the central bank builds its own rails.",
    "stats": [
        {"label": "Digital users", "value": "1.9m"},
        {"label": "Acquiring share", "value": "56.7%"},
        {"label": "ROAE H1 2026", "value": "27.2%"},
        {"label": "Group loans", "value": "GEL 44bn"},
    ],
    "page": "Bank_of_Georgia_Platform.html",
    "notes": (
        ("Research notes", "Bank_of_Georgia_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"]},
        "credit": {"apis": ["consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "solocards": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "corpcard": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "ecom": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "openbanking": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L3 Services
        "assistant": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "fincrime": {"apis": ["transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials"],
                   "bundles": ["loyalty_stack"]},
        "bizoffers": {"apis": ["offers_merchant_content"], "use_cases": ["specials"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "pfm_stack", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "premium": ("loyalty_stack",),
        "everyday": ("pfm_stack",),
    },
}
