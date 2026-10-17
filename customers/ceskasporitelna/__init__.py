"""Česká spořitelna, a.s.

The page (``Ceska_sporitelna_Platform.html``) reads the largest Czech bank by
clients as five discs, Foundation to Access, with the segments it reports
(Retail, Corporates, Group Markets, ALM & Local Corporate Center), a
Mastercard lens (a Visa-only bank since 2023, reached by Mastercard only
through acceptance) and ten journeys, two of them for Mastercard. Erste Group,
the parent, is a separate customer. Public sources as at 17 October 2026; the
research behind it is in ``Ceska_sporitelna_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``ceskasporitelna_inventory.py`` and
``ceskasporitelna_story.py``::

    python customers/build_page.py ceskasporitelna
"""

CUSTOMER = {
    "id": "ceskasporitelna",
    "order": 560,
    "name": "Česká spořitelna",
    "short": "Česká spořitelna",
    "brands": ["Česká spořitelna", "George", "Erste Premier", "Stavební spořitelna ČS", "ČS penzijní společnost", "Moneyback"],
    "country": "Czech Republic",
    "region": "Europe",
    "accent": "#2870ed",   # Erste / ČS bright blue, from the logo background on csas.cz
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Česká spořitelna", "bg": "#2870ed",
         "source": "https://cdn.erstegroup.com/content/dam/cz/csas/financnezdravejsi_csas_cz/obrazky/ikony-a-loga/2023_logo_cs.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The largest Czech bank as five discs: 4.6 million clients, every card on Visa since 2023, and Mastercard "
               "left with acceptance and an award.",
    "stats": [
        {"label": "Clients", "value": "4.6m"},
        {"label": "Loans", "value": "CZK 1,259bn"},
        {"label": "ROE H1 2026", "value": "19.4%"},
        {"label": "Active cards", "value": "4.5m"},
    ],
    "page": "Ceska_sporitelna_Platform.html",
    "notes": (
        ("Research notes", "Ceska_sporitelna_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "enhanced_currency_conversion_calculator"], "use_cases": ["txnotify"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "transfers": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L3 Services
        "bankid": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "heygeorge": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "moneyback": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "fithealth": {"apis": ["easy_savings"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "sme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "accounts": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        # L5 Access
        "georgebiz": {"apis": ["open_finance_eu", "business_payment_controls"], "use_cases": ["identity"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "loyalty_stack", "acquirer_risk"),
        "mcnow": ("acquirer_risk", "merchant_resolution"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "save": ("pfm_stack",),
    },
}
