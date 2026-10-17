"""PT Bank Central Asia Tbk (BCA).

The page (``Bank_Central_Asia_BCA_Platform.html``) reads Indonesia's most
valuable bank as five discs, Foundation to Access, with the segments it
reports (corporate, commercial and SME, consumer, transaction banking), a
Mastercard lens (domestic rails at home, Mastercard for abroad and online)
and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in
``Bank_Central_Asia_BCA_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``bca_inventory.py``
and ``bca_story.py``::

    python customers/build_page.py bca
"""

CUSTOMER = {
    "id": "bca",
    "order": 750,
    "name": "Bank Central Asia (BCA)",
    "short": "BCA",
    "brands": ["BCA", "myBCA", "blu by BCA Digital", "BCA Syariah", "BCA Finance", "Flazz"],
    "country": "Indonesia",
    "region": "Asia-Pacific",
    "accent": "#005cab",   # BCA blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "BCA", "bg": "#ffffff",
         "source": "https://www.bca.co.id/-/media/Feature/Header/Header-Logo/Blue-en-svg.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Indonesia's most valuable bank as five discs: 33 million customers on GPN debit, QRIS and its own BCA Card "
               "at home, with Mastercard carrying Paspor debit abroad, four credit cards and every blu card.",
    "stats": [
        {"label": "Customers", "value": "33m"},
        {"label": "Net profit 1H26", "value": "Rp29.5tn"},
        {"label": "CASA share", "value": "85%"},
        {"label": "Credit cards", "value": "4.9m"},
    ],
    "page": "Bank_Central_Asia_BCA_Platform.html",
    "notes": (
        ("Research notes", "Bank_Central_Asia_BCA_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "paspormc": {"apis": ["transaction_notifications", "enhanced_currency_conversion_calculator"], "use_cases": ["txnotify"],
                      "bundles": ["issuer_toolkit"]},
        "mccc": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                 "bundles": ["issuer_toolkit"]},
        "bbt": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "xbqr": {"apis": ["enhanced_currency_conversion_calculator", "priceless_cities", "places"], "use_cases": ["places"]},
        "edc": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        "api": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "rewards": {"apis": ["offers_for_publishers", "benefits_eligibility"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "corplend": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L5 Access
        "mybca": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
        "bludebit": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "issuer_toolkit", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "cards": ("loyalty_stack", "issuer_toolkit"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "young": ("pfm_stack",),
    },
}
