"""BAC (BAC International Bank, formerly BAC Credomatic).

The page (``BAC_Platform.html``) reads Central America's largest bank as five
discs, Foundation to Access, across its six markets (Costa Rica, Panama,
Guatemala, Honduras, El Salvador and Nicaragua), with its loan book split into
consumer, corporate and SME, and mortgages, a Mastercard lens (one of three
networks at the region's card leader) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``BAC_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``bac_inventory.py`` and
``bac_story.py``::

    python customers/build_page.py bac
"""

CUSTOMER = {
    "id": "bac",
    "order": 450,
    "name": "BAC",
    "short": "BAC",
    "brands": ["BAC", "BAC Credomatic", "Credomatic", "Multibank", "Compra Click", "Tasa Cero"],
    "country": "Costa Rica",
    "region": "Latin America",
    "accent": "#e4002b",   # BAC red, from the logo and baccredomatic.com
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "BAC", "bg": "#ffffff",
         "source": "https://commons.wikimedia.org/wiki/File:Logotipo_BAC_sin_Credomatic_-_Horizontal_-_rojo.jpg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Central America's largest bank as five discs: six markets, about 41% of the region's credit-card "
               "issuing and 54% of acquiring, on Visa, Mastercard and American Express alike.",
    "stats": [
        {"label": "Assets", "value": "US$46.9bn"},
        {"label": "Clients", "value": "6.3m"},
        {"label": "Acquiring share", "value": "54%"},
        {"label": "Markets", "value": "6"},
    ],
    "page": "BAC_Platform.html",
    "notes": (
        ("Research notes", "BAC_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "premium": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "compraclick": {"apis": ["match", "merchant_identifier"], "use_cases": ["psi", "recurring"], "bundles": ["acquirer_risk", "subscriptions"]},
        "wallets": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "remesa": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "icbac": {"apis": ["places", "consumer_clarity"], "use_cases": ["enrichment", "places"], "bundles": ["merchant_resolution"]},
        "loyalty": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines and L5 Access
        "corporate": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "app": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "merchant_resolution", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "sme": ("acquirer_risk", "subscriptions"),
        "card": ("issuer_toolkit", "loyalty_stack"),
        "corp": ("issuer_toolkit",),
    },
}
