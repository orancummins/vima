"""CaixaBank, S.A.

The page (``CaixaBank_Platform.html``) reads Spain's largest bank as five
discs, Foundation to Access, with the segments it reports (Banking and
insurance, BPI, Corporate centre), a Mastercard lens (a Visa-led card giant
where Mastercard holds the corners) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``CaixaBank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``caixabank_inventory.py`` and ``caixabank_story.py``::

    python customers/build_page.py caixabank
"""

CUSTOMER = {
    "id": "caixabank",
    "order": 1470,
    "name": "CaixaBank",
    "short": "CaixaBank",
    "brands": ["CaixaBank", "BPI", "imagin", "CaixaBank Payments & Consumer", "Comercia Global Payments", "VidaCaixa", "MicroBank"],
    "country": "Spain",
    "region": "Europe",
    "type": "bank",
    "accent": "#009ad8",   # CaixaBank blue, from the star in the logo and the website
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "CaixaBank", "bg": "#ffffff",
         "source": "https://www.caixabank.es/deployedfiles/particulares/R2025/Estaticos/Imagenes/logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Spain's largest bank as five discs: 20.9 million customers and 34 million cards, a credit range on Visa, "
               "Mastercard in travel and B2B virtual cards, and Bizum moving into shops.",
    "stats": [
        {"label": "Customers", "value": "20.9m"},
        {"label": "Cards", "value": "34m+"},
        {"label": "Card turnover share", "value": "31%"},
        {"label": "Profit H1 2026", "value": "€3.2bn"},
    ],
    "page": "CaixaBank_Platform.html",
    "notes": (
        ("Research notes", "CaixaBank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mycard": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "imagintravel": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility"], "use_cases": ["settle_in", "pfm"],
                         "bundles": ["pfm_stack"]},
        "virtualb2b": {"apis": ["business_payment_controls", "merchant_identifier"], "use_cases": ["enrichment"]},
        "corporate": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "comercia": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "bizum": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "agentic": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment"]},
        "loyalty": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "consumer": {"apis": ["consumer_clarity", "automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "imaginbank": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "issuer_toolkit", "loyalty_stack"),
        "mcnow": ("pfm_stack", "issuer_toolkit"),
        "travel": ("pfm_stack",),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "suppliers": ("sustainability",),
    },
}
