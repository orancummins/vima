"""NLB Group (Nova Ljubljanska banka d.d., Ljubljana).

The page (``NLB_Platform.html``) reads Slovenia's biggest bank and its six
sister banks in the Western Balkans as five discs, Foundation to Access, with
the segments it reports (retail, corporate and investment banking and
financial markets in Slovenia, strategic foreign markets, other activities), a
Mastercard lens (Mastercard owns the Slovenian consumer wallet, Visa took
business debit) and ten journeys, two of them for Mastercard. Public sources as
at 17 October 2026; the research behind it is in ``NLB_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``nlb_inventory.py`` and
``nlb_story.py``::

    python customers/build_page.py nlb
"""

CUSTOMER = {
    "id": "nlb",
    "order": 630,
    "name": "NLB",
    "short": "NLB",
    "brands": ["NLB", "NLB Komercijalna banka", "NLB Banka", "NLB Pay", "NLB Klik", "NLB Skladi", "NLB Lease&Go"],
    "country": "Slovenia",
    "region": "Europe",
    "type": "bank",
    "accent": "#230078",   # NLB violet, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "NLB Group", "bg": "#ffffff",
         "source": "https://www.nlbgroup.com/content/dam/nlb/brand-assets/logos/Desktop%20-%20NLB%20Group.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Slovenia's biggest bank and six Balkan sisters as five discs: a Debit Mastercard in every Slovenian "
               "package, Visa for business debit, DinaCard in Serbia, and Flik at the till.",
    "stats": [
        {"label": "Active clients", "value": "2.9m"},
        {"label": "Assets", "value": "€31.9bn"},
        {"label": "Profit H1 2026", "value": "€252m"},
        {"label": "Tokenised card payments", "value": "28.9%"},
    ],
    "page": "NLB_Platform.html",
    "notes": (
        ("Research notes", "NLB_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "digitalcard": {"apis": ["bin_lookup"], "use_cases": ["identity"]},
        "credit": {"apis": ["consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "premium": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "bizcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "nlbpay": {"apis": ["enhanced_currency_conversion_calculator", "merchant_identifier"], "use_cases": ["enrichment", "pfm"],
                   "bundles": ["pfm_stack"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "loyalty": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"],
                    "bundles": ["loyalty_stack"]},
        # L5 Access
        "klik": {"apis": ["consumer_clarity", "open_finance_eu"], "use_cases": ["pfm"], "bundles": ["pfm_stack", "merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "acquirer_risk", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "pfm_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "merchant": ("acquirer_risk", "loyalty_stack"),
        "private": ("loyalty_stack",),
    },
}
