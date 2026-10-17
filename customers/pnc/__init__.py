"""PNC (The PNC Financial Services Group).

The page (``PNC_Platform.html``) reads PNC as five discs, Foundation to
Access, with the segments it reports (Retail Banking, Corporate &
Institutional Banking, Asset Management Group), a Mastercard lens (Visa on
every PNC card, Mastercard only at the till) and ten journeys, two of them
for Mastercard. Public sources as at 17 October 2026, including the FirstBank
acquisition (closed 5 January 2026, converted 22 June 2026); the research
behind it is in ``PNC_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``pnc_inventory.py``
and ``pnc_story.py``::

    python customers/build_page.py pnc
"""

CUSTOMER = {
    "id": "pnc",
    "order": 1170,
    "name": "PNC",
    "short": "PNC",
    "brands": ["PNC Bank", "PNC Wealth Management", "PNC Private Bank", "PNC Treasury Management", "Harris Williams", "Linga", "FirstBank"],
    "country": "United States",
    "region": "Americas",
    "type": "bank",
    "accent": "#f58025",   # PNC orange, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "PNC", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:PNClogo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A $628 billion coast-to-coast bank as five discs: FirstBank folded in, every PNC card on Visa, "
               "and Mastercard reaching it through the merchants it acquires for.",
    "stats": [
        {"label": "Assets", "value": "$628bn"},
        {"label": "Branches", "value": "~2,400"},
        {"label": "ROTCE Q3 2026", "value": "18.3%"},
        {"label": "FirstBank customers", "value": "780k"},
    ],
    "page": "PNC_Platform.html",
    "notes": (
        ("Research notes", "PNC_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "comcard": {"apis": ["business_payment_controls", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "merchant": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "mobileaccept": {"apis": ["match", "merchant_identifier"], "bundles": ["acquirer_risk"]},
        "linga": {"apis": ["offers_merchant_content", "places"], "use_cases": ["places"], "bundles": ["loyalty_stack"]},
        # L3 Services
        "akoya": {"apis": ["open_finance"], "use_cases": ["identity", "pfm"], "bundles": ["pfm_stack"]},
        "healthcheck": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment"]},
        "totalrewards": {"apis": ["offers_for_publishers", "offers_merchant_content", "benefits_eligibility"], "use_cases": ["specials", "findacard"],
                         "bundles": ["loyalty_stack"]},
        "security": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "merchant_identifier", "transaction_notifications"], "use_cases": ["enrichment", "pfm", "txnotify"],
                "bundles": ["pfm_stack", "subscriptions"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "loyalty_stack", "issuer_toolkit"),
        "mcnow": ("acquirer_risk", "merchant_resolution"),
        "everyday": ("pfm_stack", "subscriptions"),
        "merchant": ("acquirer_risk", "loyalty_stack"),
        "credit": ("issuer_toolkit", "loyalty_stack"),
    },
}
