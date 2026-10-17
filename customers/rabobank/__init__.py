"""Coöperatieve Rabobank U.A.

The page (``Rabobank_Platform.html``) reads the Utrecht cooperative bank as
five discs, Foundation to Access, with the segments it reports (Domestic
Retail Banking, Wholesale & Rural, Leasing and Property Development), a
Mastercard lens (debit shared with Visa, iDEAL turning into Wero, and
Mastercard's first Dutch agent payment) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``Rabobank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``rabobank_inventory.py`` and ``rabobank_story.py``::

    python customers/build_page.py rabobank
"""

CUSTOMER = {
    "id": "rabobank",
    "order": 1500,
    "name": "Rabobank",
    "short": "Rabobank",
    "brands": ["Rabobank", "Obvion", "Freo", "DLL", "BPD", "Rabo Investments"],
    "country": "Netherlands",
    "region": "Europe",
    "type": "bank",
    "accent": "#0008a8",   # Rabobank blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Rabobank", "bg": "#ffffff", "source": "https://www.rabobank.com/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A Dutch cooperative and global food & agri bank as five discs: debit split between Mastercard and Visa, "
               "iDEAL turning into Wero, and the first Dutch AI-agent payment on Mastercard.",
    "stats": [
        {"label": "NL customers", "value": "9m+"},
        {"label": "Net profit 2025", "value": "€5.0bn"},
        {"label": "CET1 H1 2026", "value": "20.2%"},
        {"label": "Total assets", "value": "€639bn"},
    ],
    "page": "Rabobank_Platform.html",
    "notes": (
        ("Research notes", "Rabobank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "enrichment"], "bundles": ["pfm_stack"]},
        "credit": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator", "automatic_billing_updater"], "use_cases": ["findacard", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "bizcard": {"apis": ["business_payment_controls", "bin_lookup"], "use_cases": ["bin_lookup"], "bundles": ["issuer_toolkit"]},
        "ideal": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "smartpay": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "taptopay": {"apis": ["merchant_identifier"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "agentpay": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["identity", "enrichment"], "bundles": ["merchant_resolution"]},
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "personal": {"apis": ["consumer_clarity", "offers_for_publishers", "easy_savings"], "use_cases": ["pfm", "specials"], "bundles": ["pfm_stack", "loyalty_stack"]},
        # L4 Business lines
        "sme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "wholesale": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "dll": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "sustainability", "pfm_stack"),
        "mcnow": ("pfm_stack", "acquirer_risk"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "farm": ("sustainability",),
    },
}
