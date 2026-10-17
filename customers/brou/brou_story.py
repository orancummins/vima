"""Banco República (BROU)'s kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from brou_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Uruguay's state bank as five discs that stack into one platform, from 41% of the system's assets at the bottom "
       "to the eBROU app, 129 branches and WhatsApp at the top. Click the stack to open it. Choose who you are and what "
       "you want to do, and the areas that deliver it light up across the layers, joined in the order they act. Switch "
       "to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("saver", "Savers & pension members", "coins"),
    ("sme", "Small businesses & professionals", "briefcase"),
    ("agro", "Farmers", "earth"),
    ("corp", "Corporates & the state", "factory"),
    ("social", "Social-programme beneficiaries", "users-round"),
]
USERS_DESC = ("Six kinds of customer, 2.1 million depositors in a country of 3.6 million: everyday customers, savers and "
              "pension members, small businesses and professionals, farmers, corporates and public bodies, and the "
              "families paid through social programmes.")

WHO = {"con": "A BROU customer", "saver": "A saver", "sme": "A small business", "agro": "A farmer",
       "corp": "A corporate treasurer", "social": "A beneficiary"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Debit Mastercard, the app, instant transfers and fraud alerts.",
     "steps": [("4.1", "accounts", "Open an account"), ("2.1", "mcdebit", "Pay with Debit Mastercard"), ("5.1", "app", "Run it in eBROU"),
               ("2.6", "spi", "Send an instant transfer"), ("3.1", "notif", "Get purchase alerts")]},
    {"id": "switch", "who": "con", "name": "Swap Maestro for a new debit card",
     "why": "Maestro stops on 1 November 2026; the replacement is Debit Mastercard, or Visa debit.",
     "steps": [("2.1", "maestro", "Retire the Maestro card"), ("5.1", "app", "Request the new card in eBROU"),
               ("5.2", "tit", "Print it at a branch terminal"), ("2.1", "mcdebit", "Use Debit Mastercard")]},
    {"id": "credit", "who": "con", "name": "Borrow and earn on a card",
     "why": "BROU Recompensa on Mastercard, with Visa at the top of the range.",
     "steps": [("2.2", "reccredit", "Take a Recompensa Mastercard"), ("3.2", "recompensa", "Earn points worth pesos"),
               ("3.2", "benefits", "Use seasonal discounts"), ("3.1", "idcheck", "Shop online with Identity Check")]},
    {"id": "wallet", "who": "con", "name": "Pay with the phone",
     "why": "BROU a Mano, Google Pay and QR payments from the account.",
     "steps": [("2.4", "bam", "Tap to pay with BROU a Mano"), ("2.4", "gpay", "Or use Google Pay"), ("2.6", "toke", "Pay by QR")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "The June 2026 Paquete Pyme: an account, a Pyme Mastercard, and the phone as a POS.",
     "steps": [("4.2", "pyme", "Take the Paquete Pyme"), ("4.2", "pymecard", "Spend on a Pyme Mastercard"),
               ("2.5", "bamcom", "Take cards and QR on a phone"), ("4.4", "micro", "Borrow from Microfinanzas")]},
    {"id": "agro", "who": "agro", "name": "Finance a harvest",
     "why": "Farm credit, an agro card and branches in every department.",
     "steps": [("5.2", "branches", "Visit a branch"), ("4.3", "agro", "Finance the harvest"), ("4.3", "corpcards", "Pay with BROU Agro Visa")]},
    {"id": "social", "who": "social", "name": "Receive a social payment",
     "why": "Family allowances and subsidies paid through BROU cards and tuapp.",
     "steps": [("5.4", "partners", "Enrol through MIDES"), ("2.7", "social", "Receive the social card"), ("2.7", "tuapp", "Pay with tuapp")]},
    {"id": "save", "who": "saver", "name": "Save for retirement",
     "why": "Term deposits at BROU and pensions at República AFAP.",
     "steps": [("4.1", "accounts", "Save in a term deposit"), ("4.4", "afap", "Join República AFAP")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Debit Mastercard for the mass base, Recompensa credit, the Pyme Mastercard and Identity Check.",
     "steps": [("2.1", "mcdebit", "Debit Mastercard replacing Maestro"), ("2.2", "reccredit", "Recompensa Mastercard credit"),
               ("4.2", "pymecard", "Pyme Mastercard"), ("3.1", "idcheck", "Mastercard Identity Check")]},
    {"id": "mcnext", "who": "mc", "name": "Where tokens, fraud tools and A2A could land",
     "why": "Where BROU has needs and Mastercard is not yet in: debit tokens and Apple Pay in BROU a Mano, scam scoring for instant transfers, open finance, offers for Recompensa, Tap on Phone and cross-border payments.",
     "steps": [("2.4", "bam", "Tokenise debit in BROU a Mano"), ("3.1", "fraud", "Scam scoring for SPI"),
               ("2.6", "spi", "Open-finance and A2A tools"), ("3.2", "recompensa", "Card-linked offers"),
               ("2.5", "bamcom", "Tap on Phone acceptance"), ("4.5", "ny", "Cross-border payments")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Banco República's map",
    "title": "Uruguay's state bank goes all in on Debit Mastercard, with Visa holding the top card",
    "lead": "BROU's mass debit base has long run on Maestro and moves to Debit Mastercard when Maestro switches off on 1 November 2026. A December 2019 agreement renewed the alliance and produced BROU Recompensa, the credit card behind the bank's comeback in cards. Visa remains a real second network, with Visa debit, the top-tier Visa Infinite and agro cards. Meanwhile instant transfers and wallets are growing faster than cards. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are BROU's own (Financial Synthesis, June 2026; 2024 Annual Report) or from BROU's card pages and press. Mastercard's and Visa's newsrooms could not be reached, and BROU publishes no card counts by network.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Maestro to Debit Mastercard", "1.78m cards; Maestro off 1 Nov 2026"],
        ["Credit", "Mastercard and Visa", "Recompensa on Mastercard; Visa Infinite on top"],
        ["Agreement", "Mastercard", "Renewed December 2019"],
        ["SMEs", "Pyme Mastercard", "June 2026"],
        ["Security", "Identity Check", "2024"],
        ["Wallets", "BROU a Mano, Google Pay", "Both networks; no debit tokens"],
        ["Instant", "SPI, Toke QR", "34m instant transfers in H2 2025"],
        ["Processing", "Sistarbanc", "BROU's own, both networks"],
    ],
    "sides": {
        "neo": {"dir": "Debit Mastercard for the mass base, Recompensa and Mastercard credit tiers, the Pyme Mastercard, corporate debit and Identity Check.",
                "deals": "What it does not run: instant transfers and QR, tuapp, Visa debit and the Visa credit range, processing, and lending."},
        "snb": {"dir": "Visa debit, MI BROU and the Visa credit range up to Infinite, the agro card, SPI and Toke, tuapp, Sistarbanc processing and BROU's own fraud tools.",
                "deals": "Where they meet: wallets, prepaid, corporate credit and the Recompensa programme."},
    },
    "tl": [
        ["Dec 2019", "BROU and Mastercard renew their alliance"],
        ["2020", "BROU Recompensa Mastercard launched"],
        ["2024", "Debit Mastercard launched; Identity Check"],
        ["Sep 2024", "Toke QR payments in the app"],
        ["Feb 2025", "BROU a Mano wallet"],
        ["Aug 2025", "Visa Platinum adds Priority Pass"],
        ["Mar 2026", "Central bank roadmap: open finance"],
        ["Jun 2026", "Paquete Pyme and Pyme Mastercard"],
        ["1 Nov 2026", "Maestro switched off"],
    ],
    "l": {
        "U": {"d": 2, "s": "Most debit holders and Recompensa members carry Mastercard.",
              "gap": "The mass debit base is moving to Debit Mastercard; Visa debit, Visa credit and agro cardholders carry Visa.",
              "neo": "Debit holders, Recompensa members, SMEs.", "snb": "Visa debit and credit holders, farmers, social-programme families."},
        "L5": {"d": 0, "s": "The front doors are BROU's.", "gap": "App, branches, kiosks and WhatsApp are the bank's; the kiosks print both networks' cards.",
               "neo": "None.", "snb": "eBROU, branches, WhatsApp."},
        "L4": {"d": 1, "s": "SME and debit products lean on Mastercard.", "gap": "Paquete Pyme carries Mastercard; lending, trusts and pensions have no network role; agro is Visa.",
               "neo": "Pyme Mastercard, debit in accounts.", "snb": "Lending, AFISA, AFAP, treasury, Agro Visa."},
        "L3": {"d": 1, "s": "Identity Check is Mastercard's; the rest is shared or BROU's.", "gap": "Recompensa leans on Mastercard; fraud tools and data are BROU's own.",
               "neo": "Identity Check, Recompensa.", "snb": "Anti-fraud module, alerts, ANCAPuntos, data."},
        "L2": {"d": 1, "s": "Debit and Recompensa on Mastercard; A2A growing beside them.", "gap": "Mastercard has debit and the flagship credit card; Visa has the rest of credit; SPI, QR and tuapp are domestic.",
               "neo": "Debit Mastercard, Recompensa, Pyme cards.", "snb": "Visa cards, SPI, Toke, tuapp."},
        "L1": {"d": 0, "s": "The state's own foundation.", "gap": "Capital, governance and Sistarbanc processing are BROU's.", "neo": "None.", "snb": "Capital, board, Sistarbanc, strategy."},
    },
    "t": area_lens(LAYERS),
}
