"""Republic Bank (Republic Financial Holdings Limited).

The page (``Republic_Bank_Platform.html``) reads Trinidad and Tobago's largest
bank as five discs, Foundation to Access, with the parent group's banks across
the Caribbean and Ghana as context, a Mastercard lens (Visa on every debit
card, Mastercard on part of the credit book) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; amounts in Trinidad and
Tobago dollars. The research behind it is in ``Republic_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``republicbank_inventory.py`` and ``republicbank_story.py``::

    python customers/build_page.py republicbank
"""

CUSTOMER = {
    "id": "republicbank",
    "order": 480,
    "name": "Republic Bank",
    "short": "Republic Bank",
    "brands": ["Republic Bank", "Republic Financial Holdings", "Endcash", "Cayman National", "Republic Life"],
    "country": "Trinidad and Tobago",
    "region": "Latin America",
    "accent": "#008fc3",   # Republic blue, from republictt.com
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Republic Bank", "bg": "#008fc3", "source": "https://www.republictt.com/sites/default/files/logo.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Trinidad and Tobago's largest bank as five discs: the country's biggest credit card book on Visa and "
               "Mastercard, Visa/LINX debit, the Endcash wallet, and sister banks in 16 countries.",
    "stats": [
        {"label": "Group assets", "value": "TT$135bn"},
        {"label": "FY2025 profit", "value": "TT$2.2bn"},
        {"label": "T&T branches", "value": "38"},
        {"label": "Countries", "value": "16"},
    ],
    "page": "Republic_Bank_Platform.html",
    "notes": (
        ("Research notes", "Republic_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mccc": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                 "bundles": ["issuer_toolkit"]},
        "aadvantage": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility"], "use_cases": ["findacard"],
                       "bundles": ["loyalty_stack"]},
        "endcash": {"apis": ["merchant_identifier", "places"], "use_cases": ["places", "enrichment"], "bundles": ["pfm_stack"]},
        "cardinwallet": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "instant": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "onboard": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "cashback": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "priceless": {"apis": ["priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "bizcards": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        # L5 Access
        "online": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "pfm_stack", "sustainability"),
        "mcnow": ("issuer_toolkit", "loyalty_stack", "acquirer_risk"),
        "card": ("issuer_toolkit", "loyalty_stack"),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "wallet": ("pfm_stack",),
    },
}
