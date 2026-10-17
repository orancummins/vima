"""Access Bank Plc.

The page (``Access_Bank_Platform.html``) reads Nigeria's largest bank as five
discs, Foundation to Access, with the segments it reports (Corporate and
Investment, Commercial, Retail, and Rest of Africa and International), a
Mastercard lens (a Visa-led bank whose cross-border payments run on Mastercard
Move) and ten journeys, two of them for Mastercard. Access Holdings Plc, the
listed parent, and the group's African and UK banks are context. Public
sources as at 17 October 2026; the research behind it is in
``Access_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``accessbank_inventory.py`` and ``accessbank_story.py``::

    python customers/build_page.py accessbank
"""

CUSTOMER = {
    "id": "accessbank",
    "order": 1090,
    "name": "Access Bank",
    "short": "Access Bank",
    "brands": ["Access Bank", "Access Holdings", "AccessMore", "Access Closa", "The Access Bank UK", "Hydrogen"],
    "country": "Nigeria",
    "region": "EEMEA",
    "accent": "#ee7e01",   # Access orange, the site's base brand colour
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Access Bank", "bg": "#ffffff", "source": "https://www.accessbankplc.com/Content/images/access-lg-logo.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Nigeria's largest bank as five discs: N51 trillion of assets and 60 million customers, credit on Visa, "
               "debit split between Visa, Mastercard and Verve, and cross-border payments on Mastercard Move.",
    "stats": [
        {"label": "Assets 2025", "value": "N51.3trn"},
        {"label": "PBT 2025", "value": "N954bn"},
        {"label": "AccessMore users", "value": "8.4m"},
        {"label": "Agents", "value": "750k+"},
    ],
    "page": "Access_Bank_Platform.html",
    "notes": (
        ("Research notes", "Access_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mcdebit": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["txnotify"],
                    "bundles": ["issuer_toolkit"]},
        "prepaid": {"apis": ["bin_lookup", "transaction_notifications"], "use_cases": ["bin_lookup", "txnotify"], "bundles": ["issuer_toolkit"]},
        "virtual": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring", "bin_lookup"], "bundles": ["subscriptions"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "hydrogen": {"apis": ["match", "bin_lookup"], "use_cases": ["bin_lookup"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "accessafrica": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "accessping": {"apis": ["merchant_identifier", "transaction_notifications"], "use_cases": ["txnotify", "enrichment"], "bundles": ["merchant_resolution"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "sme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "accessu": {"apis": ["consumer_clarity", "benefits_eligibility"], "use_cases": ["pfm", "findacard"], "bundles": ["pfm_stack"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "places"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "subscriptions", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "pfm_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "private": ("loyalty_stack",),
    },
}
