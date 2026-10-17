"""Nabil Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from nabil_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Nepal's most profitable bank as five discs that stack into one platform, from NPR 735 billion of assets at the "
       "bottom to the nBank app, 268 branches and partner apps at the top. Click the stack to open it. Choose who you "
       "are and what you want to do, and the areas that deliver it light up across the layers, joined in the order they "
       "act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("nrn", "Nepalis abroad & their families", "earth"),
    ("tour", "Visitors to Nepal", "globe"),
    ("sme", "Small businesses & merchants", "briefcase"),
    ("corp", "Corporates & projects", "factory"),
    ("inv", "Savers & investors", "trending-up"),
]
USERS_DESC = ("Six kinds of user, about 2.5 million customers in all: everyday customers, Nepalis abroad and the families "
              "they send money to, foreign visitors, small businesses and QR merchants, corporates and hydropower projects, "
              "and savers and shareholders.")

WHO = {"con": "A Nabil customer", "nrn": "A Nepali abroad", "tour": "A visitor to Nepal", "sme": "A merchant",
       "corp": "A corporate treasurer", "inv": "A saver or investor"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account opened by video, a debit card on Visa or Mastercard, nBank, QR payments and 3-D Secure.",
     "steps": [("3.2", "videokyc", "Open an account by video KYC"), ("4.1", "deposits", "Keep savings"),
               ("2.1", "debitvisa", "Pay with a Smart Debit card"), ("5.1", "app", "Run it in nBank"),
               ("2.5", "a2a", "Scan QR and transfer by connectIPS"), ("3.1", "esecure", "Protected online by e-Secure")]},
    {"id": "credit", "who": "con", "name": "Buy now, pay over time",
     "why": "A domestic credit card on Visa or Mastercard, instalments and 0% iPhone EMI, or a FoneLoan.",
     "steps": [("2.2", "creditmc", "Take a credit card"), ("3.4", "installment", "Split a purchase into EMIs"),
               ("3.4", "offers", "Use cardholder offers"), ("4.2", "foneloan", "Or borrow instantly in the app")]},
    {"id": "remit", "who": "nrn", "name": "Send money home",
     "why": "nRemit with a Mastercard or Visa card, Visa Direct, or Nabil Remit's partners, into an account opened from abroad.",
     "steps": [("3.2", "videokyc", "Open an account from abroad"), ("2.6", "nremit", "Send with a card through nRemit"),
               ("2.6", "remit", "Or send through Nabil Remit partners"), ("2.6", "visadirect", "Or push to a Visa card"),
               ("5.1", "app", "Family sees it in nBank")]},
    {"id": "travel", "who": "con", "name": "Travel and shop abroad",
     "why": "Visa prepaid travel cards, the USD iCard and the international debit card.",
     "steps": [("2.3", "prepaid", "Load a travel card"), ("2.3", "icard", "Shop online with the iCard"),
               ("2.1", "debitvisa", "Spend from a foreign-currency account")]},
    {"id": "tourist", "who": "tour", "name": "Pay as a visitor to Nepal",
     "why": "Nepal Now loaded from a foreign card, Fonepay QR, card terminals and ATMs.",
     "steps": [("2.6", "nepalnow", "Load Nepal Now with a foreign card"), ("2.4", "qr", "Pay at QR merchants"),
               ("2.4", "pos", "Tap at card terminals"), ("5.2", "branches", "Withdraw at a Nabil ATM")]},
    {"id": "merchant", "who": "sme", "name": "Get paid as a merchant",
     "why": "Fonepay QR with Koili alerts, card terminals, the gateway for Visa, Mastercard and UnionPay, and SME credit.",
     "steps": [("2.4", "qr", "Take QR payments"), ("2.4", "pos", "Take cards at a terminal"),
               ("2.4", "epg", "Sell online through the gateway"), ("4.3", "sme", "Borrow to grow")]},
    {"id": "corp", "who": "corp", "name": "Finance a project and pay suppliers",
     "why": "Infrastructure loans, trade finance and corporatePAY on NCHL's rails.",
     "steps": [("4.4", "corporate", "Finance a hydropower project"), ("4.4", "trade", "Open letters of credit"),
               ("5.3", "corpdigital", "Pay suppliers through corporatePAY"), ("3.3", "openapi", "Connect the ERP by API")]},
    {"id": "invest", "who": "inv", "name": "Save and invest",
     "why": "Fixed deposits, an FD-backed card, and Nabil's investment-banking and broking arms.",
     "steps": [("4.1", "deposits", "Open a fixed deposit"), ("2.2", "fdcard", "Spend against it with the FD Card"),
               ("4.5", "invest", "Invest through Nabil Investment Banking"), ("1.2", "owners", "Hold Nabil shares")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mastercard debit and credit, gateway acceptance, SecureCode and card-funded nRemit.",
     "steps": [("2.1", "debitmc", "Mastercard debit, Danphe card"), ("2.2", "creditmc", "Mastercard domestic credit"),
               ("2.4", "epg", "Mastercard on the gateway"), ("3.1", "esecure", "Mastercard SecureCode"),
               ("2.6", "nremit", "nRemit funded by Mastercard cards")]},
    {"id": "mcnext", "who": "mc", "name": "Where remittances, tokens and tourists could land",
     "why": "Where Nabil has needs and Mastercard is not yet in: account-based remittance, Tap N' Pay in nBank, tourist acceptance, dispute and fraud tools, card credit against QR credit, and commercial cards.",
     "steps": [("2.6", "nremit", "Mastercard Move for account-based remittance"), ("5.1", "app", "Tokenised Tap N' Pay in nBank"),
               ("2.6", "nepalnow", "Tourist spending on Mastercard"), ("3.1", "fraudops", "Fraud and dispute tools"),
               ("3.4", "installment", "Instalments and offers on Mastercard credit"), ("5.3", "corpdigital", "Commercial cards for suppliers")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Nabil Bank's map",
    "title": "A Visa-first bank where QR moves the money and Mastercard is building in debit",
    "lead": "Nabil has issued Visa and Mastercard for more than two decades, but Visa leads: its prepaid, USD, FD and international debit cards are Visa, Visa Direct has run since 2022, and Visa named it a principal client in November 2025. Mastercard has a domestic credit card, a debit choice and, since November 2025, a Danphe Mastercard debit card, plus acceptance on Nabil's gateway and card-funded nRemit. Most of Nepal's digital money now moves on Fonepay QR and NCHL's rails, not cards. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (Q4 FY2025/26 report and audited extract, year to 16 July 2026; 2024/25 annual report) or from NRB, NCHL and Nepali business press. Nabil publishes no card counts by network, so the split between Visa and Mastercard is read from product pages.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa, Mastercard as a choice", "Danphe Mastercard debit, Nov 2025"],
        ["Credit", "Visa and Mastercard", "Domestic cards; book NPR 1.5bn"],
        ["Prepaid & USD", "Visa", "Travel cards, iCard, FD Card"],
        ["E-commerce acquiring", "Visa, Mastercard, UnionPay", "Visa award, Nov 2025"],
        ["QR acquiring", "Fonepay", "43,600+ QR terminals"],
        ["Remittance", "nRemit, Visa Direct", "Mastercard or Visa cards fund nRemit"],
        ["Scheme fees", "Visa and Mastercard", "NPR 929m in FY2025/26"],
        ["National rails", "NCHL", "238m transactions, FY2025/26"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard debit and domestic credit, gateway acceptance, SecureCode, card-funded nRemit and instalments on Mastercard credit.",
                "deals": "What it does not do: prepaid, USD and FD cards, Visa Direct, QR acquiring, national rails, AI or tokenised mobile payments."},
        "snb": {"dir": "Visa across debit, prepaid and Visa Direct; Fonepay for QR; NCHL for connectIPS, corporatePAY and NEPALPAY; Nabil's own AI and operations.",
                "deals": "Where they meet: the Smart Debit choice, the gateway and nRemit, which take both networks."},
    },
    "tl": [
        ["1999–2004", "Visa and Mastercard cards introduced"],
        ["Mar 2019", "Contactless cards and POS, claimed first in Nepal"],
        ["Sep 2022", "Visa Direct launched"],
        ["Dec 2022", "nBank launched"],
        ["Oct 2024", "nRemit in Hamro Patro, funded by Mastercard or Visa cards"],
        ["Mar 2025", "NEPALPAY domestic card scheme goes live (NCHL)"],
        ["Nov 2025", "Danphe Mastercard debit; three Visa awards"],
        ["Jan 2026", "Nirvana Kumar Chaudhary becomes chairman"],
        ["May 2026", "UnionPay joins Fonepay QR"],
        ["Jul 2026", "FY2025/26: NPR 7.9bn profit, top in Nepal"],
        ["Oct 2026", "42nd AGM: 15.8% dividend"],
    ],
    "l": {
        "U": {"d": 1, "s": "Some cardholders carry Mastercard; most digital payers use QR and connectIPS.",
              "gap": "Mastercard reaches customers who choose its debit or credit card and senders using nRemit; Visa holds prepaid and international cards.",
              "neo": "Mastercard debit and credit holders, nRemit senders.", "snb": "Visa cardholders, QR payers, connectIPS users, borrowers and savers."},
        "L5": {"d": 0, "s": "The front doors are Nabil's.", "gap": "nBank, branches and corporate portals are the bank's; ATMs accept Mastercard ⚠.",
               "neo": "ATM acceptance ⚠.", "snb": "nBank, branches, corporatePAY, agents and partner apps."},
        "L4": {"d": 0, "s": "The business lines have no network role.", "gap": "Deposits, loans, trade and treasury do not run on card networks.",
               "neo": "None.", "snb": "Deposits, retail and SME loans, corporate and trade, treasury."},
        "L3": {"d": 1, "s": "SecureCode and Mastercard instalments; the rest is Nabil's.", "gap": "3-D Secure and instalments cover Mastercard; AI, KYC, APIs and dispute operations are Nabil's own.",
               "neo": "SecureCode, instalments on Mastercard credit.", "snb": "Visa Secure, AI, video KYC, open APIs, operations."},
        "L2": {"d": 1, "s": "Mastercard in debit, credit, gateway and nRemit; Visa and QR lead.", "gap": "Visa carries prepaid, USD and international cards; Fonepay carries QR; NCHL carries account-to-account payments.",
               "neo": "Mastercard debit and credit, EPG, nRemit.", "snb": "Visa cards and Visa Direct, Fonepay QR, connectIPS, Nabil Remit."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's, though Nabil holds Mastercard Class B shares.",
               "neo": "None.", "snb": "Capital, owners, heritage, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
