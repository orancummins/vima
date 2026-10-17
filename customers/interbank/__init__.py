"""Interbank (Banco Internacional del Perú).

The page (``Interbank_Platform.html``) reads Peru's consumer-lending bank,
part of Intercorp Financial Services, as five discs, Foundation to Access:
Retail Banking (cards, payroll, mortgages, Plin), Commercial Banking and
Izipay acquiring, a Mastercard lens (a Visa and Amex issuer that owns
Mastercard's old Peruvian acquirer) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; amounts in soles. The
research behind it is in ``Interbank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``interbank_inventory.py`` and ``interbank_story.py``::

    python customers/build_page.py interbank
"""

CUSTOMER = {
    "id": "interbank",
    "order": 400,
    "name": "Interbank",
    "short": "Interbank",
    "brands": ["Interbank", "Izipay", "Plin", "Millas Benefit", "Interseguro", "Inteligo"],
    "country": "Peru",
    "region": "Latin America",
    "type": "bank",
    "accent": "#00a24f",   # Interbank green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Interbank", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:Interbank_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Peru's consumer-lending bank as five discs: credit and debit on Visa, an Amex range and a small "
               "Mastercard one, and Izipay, once Mastercard's acquirer in Peru, now the group's own.",
    "stats": [
        {"label": "Loans", "value": "S/52.6bn"},
        {"label": "ROE 2Q26", "value": "15.6%"},
        {"label": "Plin monthly users", "value": "2.8m"},
        {"label": "Izipay share (own claim)", "value": "45%+"},
    ],
    "page": "Interbank_Platform.html",
    "notes": (
        ("Research notes", "Interbank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "visacredit": {"apis": ["bin_lookup", "consumer_clarity"], "use_cases": ["bin_lookup", "consumer_clarity"]},
        "mccredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "izipay": {"apis": ["merchant_identifier", "match", "places"], "use_cases": ["psi", "places"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "plincredit": {"apis": ["automatic_billing_updater", "transaction_notifications"], "use_cases": ["recurring", "txnotify"], "bundles": ["subscriptions"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "avi": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "millas": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["findacard", "specials"],
                   "bundles": ["loyalty_stack"]},
        "openbanking": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L4 Business lines
        "smallbiz": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "consumer": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "loyalty_stack", "issuer_toolkit", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "card": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack",),
    },
}
