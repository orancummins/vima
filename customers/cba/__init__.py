"""Commonwealth Bank of Australia.

The page (``Commonwealth_Bank_Platform.html``) reads Australia's largest bank
as five discs, Foundation to Access, with the segments it reports (Retail
Banking Services, Business Banking, Institutional Banking and Markets, New
Zealand), a Mastercard lens (Australia's biggest card book on Mastercard, with
eftpos in the same wallet) and ten journeys, two of them for Mastercard.
Public sources as at 17 October 2026; the research behind it is in
``Commonwealth_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``cba_inventory.py`` and ``cba_story.py``::

    python customers/build_page.py cba
"""

CUSTOMER = {
    "id": "cba",
    "order": 760,
    "name": "Commonwealth Bank",
    "short": "CommBank",
    "brands": ["CommBank", "Bankwest", "Unloan", "CommSec", "ASB", "CommBank Yello"],
    "country": "Australia",
    "region": "Asia-Pacific",
    "type": "bank",
    "accent": "#ffcc00",   # CommBank yellow, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Commonwealth Bank", "bg": "#ffffff",
         "source": "https://commons.wikimedia.org/wiki/File:Commonwealth_Bank_Logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Australia's largest bank as five discs: consumer debit and every consumer credit card on Mastercard, "
               "eftpos on the same debit cards, and the country's first Agent Pay purchase.",
    "stats": [
        {"label": "FY26 cash profit", "value": "A$11.0bn"},
        {"label": "Card balance share", "value": "29.3%"},
        {"label": "App users", "value": "9.6m"},
        {"label": "ROE", "value": "14.0%"},
    ],
    "page": "Commonwealth_Bank_Platform.html",
    "notes": (
        ("Research notes", "Commonwealth_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "enrichment"]},
        "worlddebit": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility"], "use_cases": ["findacard"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "bizcredit": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "payto": {"apis": ["open_finance"], "use_cases": ["identity", "recurring"], "bundles": ["subscriptions"]},
        "ctp": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "companion": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "insights": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
        "yello": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials", "findacard"],
                  "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "business": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit", "merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "loyalty_stack", "acquirer_risk"),
        "mcnow": ("issuer_toolkit", "subscriptions"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "card": ("loyalty_stack", "issuer_toolkit"),
        "sme": ("acquirer_risk", "subscriptions"),
    },
}
