"""Kapitalbank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from kapitalbankuz_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Uzbekistan's largest private bank as five discs that stack into one platform, from UZS 62.7 trillion of assets "
       "and the country's biggest retail deposit book at the bottom to the KAPITALBANK.Online app, the Uzum Business app "
       "and 1,500 ATMs at the top. Click the stack to open it. Choose who you are and what you want to do, and the areas "
       "that deliver it light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how "
       "deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("prem", "Premium clients", "gem"),
    ("borrow", "Car buyers & borrowers", "hand-coins"),
    ("sme", "Entrepreneurs", "briefcase"),
    ("merch", "Merchants", "store"),
    ("corp", "Corporates & exporters", "factory"),
]
USERS_DESC = ("Six kinds of customer, more than 2 million people and about 100,000 businesses: everyday customers, premium "
              "clients, car buyers and borrowers, entrepreneurs, merchants and the corporates and exporters it finances.")

WHO = {"con": "A Kapitalbank customer", "prem": "A premium client", "borrow": "A borrower", "sme": "An entrepreneur",
       "merch": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: sign up in the app, pay at home on Uzcard or HUMO, pay abroad with Visa Sum, keep subscriptions in check.",
     "steps": [("5.1", "app", "Sign up in the app with MyID"), ("2.1", "uzcardhumo", "Pay at home with Uzcard or HUMO"),
               ("2.2", "visasum", "Pay abroad with Visa Sum"), ("3.2", "subs", "Pause a subscription"), ("3.1", "fraud", "Protected by card risk checks")]},
    {"id": "save", "who": "con", "name": "Save in soums or dollars",
     "why": "The country's largest retail deposit book, opened and topped up in the app.",
     "steps": [("5.1", "app", "Open a deposit in the app"), ("4.1", "deposits", "Earn interest on soums, dollars or euros")]},
    {"id": "travel", "who": "con", "name": "Travel and send money abroad",
     "why": "Multicurrency cards and three ways to move money across borders.",
     "steps": [("2.4", "mcmulti", "Carry a multicurrency Mastercard"), ("2.6", "moneysend", "Send with MoneySend"),
               ("2.6", "visadirect", "Or with Visa Direct"), ("2.6", "swiftwu", "Or by Western Union and SWIFT")]},
    {"id": "premium", "who": "prem", "name": "Bank as a premium client",
     "why": "Kapital Premium and Privilege pair a Visa Infinite with a Mastercard World Elite or Black Edition.",
     "steps": [("4.3", "kpremium", "Join Kapital Premium or Privilege"), ("2.4", "mcpremium", "Hold a Mastercard World Elite"),
               ("2.4", "visainf", "And a Visa Infinite"), ("3.3", "mctravel", "Win Mastercard travel rewards"), ("3.3", "mcoffers", "Use Mastercard partner offers")]},
    {"id": "borrow", "who": "borrow", "name": "Buy a car or a home",
     "why": "Car loans with UzAuto Motors, mortgages and microloans.",
     "steps": [("5.4", "partners", "Choose a car at an UzAuto dealer"), ("4.2", "carloans", "Take a 0% UzAuto Nasiya loan"),
               ("4.2", "mortgage", "Or a Comfortable House mortgage")]},
    {"id": "sme", "who": "sme", "name": "Start and run a small business",
     "why": "An account opened online, a company card, and cash paid in at any ATM.",
     "steps": [("5.2", "uzbizapp", "Download Uzum Business Kapitalbank"), ("4.4", "smeaccount", "Open an account online"),
               ("2.7", "mcbiz", "Get a Mastercard Business card"), ("4.4", "selfcollect", "Pay in takings at an ATM")]},
    {"id": "merchant", "who": "merch", "name": "Take payments",
     "why": "Terminals for five card brands, online checkout and the new national QR.",
     "steps": [("2.5", "acquiring", "Rent a POS terminal"), ("2.5", "qr", "Show a UzQR code"), ("2.5", "ecom", "Take cards online")]},
    {"id": "corp", "who": "corp", "name": "Trade abroad",
     "why": "Trade finance, factoring, FX and a direct dollar line at BNY.",
     "steps": [("4.5", "tradefin", "Finance imports with a letter of credit"), ("4.5", "factoring", "Factor receivables"),
               ("4.5", "fx", "Settle dollars through BNY"), ("2.7", "bizcards", "Give staff Visa Business cards")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "A full card range, the second premium slot, multicurrency cards, Mastercard Business, MoneySend and partner offers.",
     "steps": [("2.3", "mccards", "Mastercard Standard to World"), ("2.4", "mcpremium", "Black Edition and World Elite"),
               ("2.4", "mcmulti", "Multicurrency Mastercard"), ("2.7", "mcbiz", "Mastercard Business"),
               ("2.6", "moneysend", "MoneySend transfers"), ("3.3", "mcoffers", "Mastercard partner offers")]},
    {"id": "mcnext", "who": "mc", "name": "Where wallets, fraud tools and Uzum could land",
     "why": "Where Kapitalbank has needs and Mastercard is not yet in: tokens for Apple Pay and Google Pay on its own processing, scam and fraud tools, AI scoring, acceptance as UzQR arrives, and a share of Visa's corporate and remittance lead.",
     "steps": [("1.3", "core", "Tokens on its own card processing"), ("3.1", "fraud", "Scam and fraud scoring"),
               ("3.4", "identity", "AI credit scoring, as with Xalq Bank"), ("2.5", "acquiring", "Acceptance and merchant risk tools"),
               ("2.7", "bizcards", "Commercial cards against Visa Business"), ("5.4", "uzumeco", "Uzum's mass market")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Kapitalbank's map",
    "title": "Visa's top Uzbek issuer, with Mastercard as a strong second",
    "lead": "Kapitalbank's domestic cards run on Uzcard and HUMO, and its international book leans on Visa: best Visa issuer in Uzbekistan in 2022, 2023 and 2024, top Visa Direct sender and first on CyberSource. Its sister Uzum Bank has issued more than 5 million Visa cards. Mastercard is a full second line: Standard to World Elite, the second premium slot in both premium packages, multicurrency cards from December 2025, Mastercard Business, MoneySend and partner offers to the end of 2026. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (FY2025 results, 2 March 2026), Central Bank league tables (1 July 2026) and Uzbek press. The bank's sites block scripted reads and were read from archived snapshots; no Kapitalbank–Mastercard agreement or card split by network has been published.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Domestic cards", "Uzcard and HUMO", "Most cards by count ⚠"],
        ["International debit", "Visa first, Mastercard second", "Best Visa issuer 2022–24"],
        ["Premium", "Both", "Visa Infinite with World Elite or Black Edition"],
        ["Multicurrency", "Both", "Mastercard from December 2025 ⚠"],
        ["Corporate cards", "Visa first", "Mastercard Business since July 2024"],
        ["Transfers", "Visa Direct leads; MoneySend too", "Visa awards 2023–24"],
        ["Acceptance", "All five brands, plus UzQR", "QR mandatory from July 2026"],
        ["Sister bank", "Uzum Bank: Visa only", "5 million cards, March 2026"],
    ],
    "sides": {
        "neo": {"dir": "A full Mastercard range, premium and multicurrency cards, Mastercard Business, MoneySend, partner offers and acceptance at Kapitalbank's terminals and ATMs.",
                "deals": "What it does not do: domestic cards, the lead in debit, corporate and premium Visa volume, fraud tools, wallets or scoring."},
        "snb": {"dir": "Uzcard and HUMO at home, Visa's award-winning card, transfer and CyberSource business, UzQR, the bank's own processing and Uzum Bank's Visa cards.",
                "deals": "Where they meet: the premium packages, where Visa Infinite and Mastercard World Elite sit side by side."},
    },
    "tl": [
        ["Jun 2021", "HUMO–Mastercard co-badge enters the market (other banks)"],
        ["Sep 2022", "Tender for 300,000 Mastercard cards"],
        ["Dec 2022", "Uzum takes 61.54%; Apelsin is now Uzum Bank"],
        ["May 2023", "ATMs take all five brands; Mastercard opens a Tashkent office"],
        ["Dec 2023", "Best Visa issuer; first on CyberSource"],
        ["Jul 2024", "Mastercard Business card"],
        ["Nov 2024", "Mastercard Cashback Abroad"],
        ["Dec 2024", "Best Visa issuer again; Visa Direct leader"],
        ["Dec 2025", "Multicurrency Mastercard Black Edition and World Elite ⚠"],
        ["Mar 2026", "Uzum Bank passes 5 million Visa cards"],
        ["Jul 2026", "Moody's Ba3; UzQR mandatory"],
        ["Aug 2026", "Mastercard partner offers to end-2026"],
        ["2027", "National Payment Switch due"],
    ],
    "l": {
        "U": {"d": 1, "s": "Mastercard holders are a minority beside Uzcard, HUMO and Visa.",
              "gap": "Everyday customers mostly carry domestic and Visa cards; premium clients get a Mastercard alongside Visa.",
              "neo": "Mastercard cardholders, premium clients, MoneySend users.", "snb": "Uzcard, HUMO and Visa holders, borrowers, depositors."},
        "L5": {"d": 1, "s": "The app and ATMs carry Mastercard among others.", "gap": "The app offers MoneySend and Mastercard cards; ATMs take five brands; Uzum's cards are Visa.",
               "neo": "MoneySend in the app, ATM acceptance.", "snb": "The apps, branches, Uzum's Visa cards."},
        "L4": {"d": 1, "s": "Premium packages pair Visa and Mastercard.", "gap": "Kapital Premium and Privilege include Mastercard World Elite or Black Edition; deposits and loans have no network role.",
               "neo": "Premium packages.", "snb": "Deposits, loans, SME accounts, trade finance."},
        "L3": {"d": 1, "s": "Mastercard offers; Visa's controls and risk tools.", "gap": "Mastercard runs partner offers and travel rewards; Visa runs subscription control and earned the risk award.",
               "neo": "Partner offers, travel rewards.", "snb": "Fraud tools, subscription control, scoring, APIs."},
        "L2": {"d": 1, "s": "A full Mastercard line beside a leading Visa line.", "gap": "Visa leads debit, premium, corporate and transfers; Mastercard has a full range, MoneySend and acceptance.",
               "neo": "Mastercard range, premium and multicurrency cards, Mastercard Business, MoneySend.", "snb": "Uzcard and HUMO, Visa range, Visa Direct, UzQR."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Capital, ownership, the CS core and the bank's own card processing are its own.", "neo": "None.", "snb": "Capital, Uzum, core and processing, strategy."},
    },
    "t": area_lens(LAYERS),
}
