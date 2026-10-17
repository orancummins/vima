"""OTP Bank Plc. and OTP Group.

The page (``OTP_Bank_Platform.html``) reads Hungary's biggest bank and the
CEE group it heads as five discs, Foundation to Access, with the segments it
reports (OTP Core, other Hungarian subsidiaries, foreign subsidiaries), a
Mastercard lens (Mastercard's bank in Hungary, Visa's in Bulgaria) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``OTP_Bank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``otp_inventory.py``
and ``otp_story.py``::

    python customers/build_page.py otp
"""

CUSTOMER = {
    "id": "otp",
    "order": 590,
    "name": "OTP Bank",
    "short": "OTP",
    "brands": ["OTP Bank", "DSK Bank", "OTP banka", "Ipoteka Bank", "Simple", "SimplePay", "Merkantil"],
    "country": "Hungary",
    "region": "Europe",
    "accent": "#52ae30",   # OTP green, from the logo and otpbank.hu
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "OTP Group", "bg": "#ffffff", "source": "https://www.otpgroup.info/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Hungary's biggest bank and CEE's largest group as five discs: 17.5 million customers in 11 countries, "
               "a Hungarian card range mostly on Mastercard, and Visa taking DSK Bank in Bulgaria.",
    "stats": [
        {"label": "Customers", "value": "17.5m"},
        {"label": "Countries", "value": "11"},
        {"label": "ROE 2025", "value": "21.6%"},
        {"label": "Market value", "value": "€36bn"},
    ],
    "page": "OTP_Bank_Platform.html",
    "notes": (
        ("Research notes", "OTP_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"]},
        "bonus": {"apis": ["bin_lookup", "automatic_billing_updater", "consumer_clarity"], "use_cases": ["recurring", "consumer_clarity"],
                  "bundles": ["issuer_toolkit"]},
        "worldelite": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["specials"]},
        "wallets": {"apis": ["enhanced_currency_conversion_calculator", "merchant_identifier"], "use_cases": ["enrichment", "pfm"],
                    "bundles": ["pfm_stack"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "simplepay": {"apis": ["match", "automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["acquirer_risk", "subscriptions"]},
        "qvik": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "dskcards": {"apis": ["bin_lookup"], "use_cases": ["bin_lookup"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "ai": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "loyalty": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "msme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "acquirer_risk", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "pfm_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "subscriptions"),
        "credit": ("issuer_toolkit", "loyalty_stack"),
    },
}
