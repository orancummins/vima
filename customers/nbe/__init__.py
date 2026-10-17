"""National Bank of Egypt (NBE).

The page (``National_Bank_of_Egypt_Platform.html``) reads Egypt's largest bank
as five discs, Foundation to Access, with the books it reports (corporate,
retail, SME, treasury, international), a Mastercard lens (level with Visa on
credit, while Meeza and InstaPay carry the domestic flows) and nine journeys,
two of them for Mastercard. Public sources as at 17 October 2026; the research
behind it is in ``National_Bank_of_Egypt_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``nbe_inventory.py`` and
``nbe_story.py``::

    python customers/build_page.py nbe
"""

CUSTOMER = {
    "id": "nbe",
    "order": 1040,
    "name": "National Bank of Egypt",
    "short": "NBE",
    "brands": ["National Bank of Egypt", "Al Ahly Net", "Al Ahly Phone Cash", "NBE (UK)", "Al Ahly Capital Holding", "Al Ahly Momkn"],
    "country": "Egypt",
    "region": "EEMEA",
    "type": "bank",
    "accent": "#107614",   # NBE green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "National Bank of Egypt", "bg": "#ffffff",
         "source": "https://commons.wikimedia.org/wiki/File:National_Bank_of_Egypt.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Egypt's largest bank as five discs: 21.7 million customers, a credit range split between Visa and "
               "Mastercard, Meeza debit, and 717 million InstaPay transfers in 2025.",
    "stats": [
        {"label": "Customers", "value": "21.7m"},
        {"label": "Total assets", "value": "EGP 9.2tn"},
        {"label": "Credit cards", "value": "1.9m"},
        {"label": "InstaPay transfers", "value": "717m"},
    ],
    "page": "National_Bank_of_Egypt_Platform.html",
    "notes": (
        ("Research notes", "National_Bank_of_Egypt_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "mcprem": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "uefa": {"apis": ["offers_for_publishers", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "usddebit": {"apis": ["business_payment_controls", "enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"], "bundles": ["issuer_toolkit"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "mpgs": {"apis": ["match", "merchant_identifier"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "applepay": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content", "easy_savings"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines and L5 Access
        "corpcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "ahlynet": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack", "merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack", "acquirer_risk"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "premium": ("loyalty_stack",),
    },
}
