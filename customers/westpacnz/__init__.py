"""Westpac New Zealand Limited.

The page (``Westpac_New_Zealand_Platform.html``) reads New Zealand's
fourth-largest bank, a wholly owned subsidiary of Westpac Banking Corporation,
as five discs, Foundation to Access, with its two banking divisions (Consumer
Banking & Wealth; Institutional & Business Banking), a Mastercard lens (every
card is a Mastercard; the services are not) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``Westpac_New_Zealand_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``westpacnz_inventory.py`` and ``westpacnz_story.py``::

    python customers/build_page.py westpacnz
"""

CUSTOMER = {
    "id": "westpacnz",
    "order": 820,
    "name": "Westpac New Zealand",
    "short": "Westpac NZ",
    "brands": ["Westpac", "Westpac One", "Westpac KiwiSaver Scheme", "BT Funds Management (NZ)", "hotpoints"],
    "country": "New Zealand",
    "region": "Asia-Pacific",
    "type": "bank",
    "accent": "#da1710",   # Westpac red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Westpac", "bg": "#ffffff", "source": "https://www.westpac.com.au/about-westpac/investor-centre/financial-information/results/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "New Zealand's fourth-largest bank as five discs: NZ$108 billion of lending, a parent that chose Visa "
               "in Australia in 2013, and every card it issues on Mastercard.",
    "stats": [
        {"label": "Net profit HY26", "value": "NZ$545m"},
        {"label": "Lending", "value": "NZ$108bn"},
        {"label": "Deposit share", "value": "17%"},
        {"label": "Cards on Mastercard", "value": "All"},
    ],
    "page": "Westpac_New_Zealand_Platform.html",
    "notes": (
        ("Research notes", "Westpac_New_Zealand_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"]},
        "airpoints": {"apis": ["benefits_eligibility", "offers_for_publishers", "priceless_cities"], "use_cases": ["findacard", "specials"],
                      "bundles": ["loyalty_stack"]},
        "hotpoints": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                      "bundles": ["issuer_toolkit"]},
        "bizcards": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        "digicard": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring", "bin_lookup"], "bundles": ["subscriptions"]},
        "merchant": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "openbanking": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "intl": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "substrap": {"apis": ["automatic_billing_updater", "merchant_identifier"], "use_cases": ["recurring", "enrichment"],
                     "bundles": ["subscriptions", "merchant_resolution"]},
        "enrich": {"apis": ["merchant_identifier", "consumer_clarity"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "airnz": {"apis": ["offers_merchant_content", "offers_for_publishers"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "sme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "agri": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "subscriptions", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "safe": ("subscriptions", "merchant_resolution"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "fly": ("loyalty_stack",),
    },
}
