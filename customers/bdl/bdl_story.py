"""Banque de Développement Local's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bdl_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("An Algerian public bank as five discs that stack into one platform, from DA 2.4 trillion of assets and a 2025 "
       "listing at the bottom to DigitBDL, 185 branches and public platforms at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in "
       "the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Households", "user-round"),
    ("trav", "Travellers", "plane"),
    ("dias", "Algerians abroad", "earth"),
    ("pro", "Professionals & merchants", "briefcase"),
    ("corp", "Companies & public sector", "factory"),
    ("inv", "Shareholders & savers", "trending-up"),
]
USERS_DESC = ("Six kinds of user: households, travellers drawing the €750 allowance, Algerians abroad, professionals "
              "and merchants, companies and public enterprises, and 11,583 shareholders. BDL does not publish a "
              "customer count.")

WHO = {"con": "A BDL customer", "trav": "A traveller", "dias": "An Algerian abroad", "pro": "A merchant",
       "corp": "A company treasurer", "inv": "A shareholder"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop runs on domestic rails: an account opened online, a CIB card, CIB online payments, WIMPAY and DigitBDL.",
     "steps": [("3.2", "onlineacct", "Open an account online"), ("2.1", "cib", "Pay with a CIB card"),
               ("2.3", "epay", "Pay bills online by CIB"), ("2.5", "wimpay", "Scan a QR with WIMPAY"),
               ("5.1", "digit", "Run it in DigitBDL")]},
    {"id": "travel", "who": "trav", "name": "Travel abroad with the allowance",
     "why": "Since July 2026 the €750 allowance arrives only on an international card: Visa or Mastercard.",
     "steps": [("3.2", "onlineacct", "Open a foreign-currency account"), ("2.2", "mastercard", "Take a Mastercard"),
               ("2.2", "visa", "Or a Visa"), ("2.2", "allowance", "Load the €750 allowance"),
               ("3.3", "travelins", "Insure the trip")]},
    {"id": "borrow", "who": "con", "name": "Borrow for home and family",
     "why": "Pawn loans against gold, home loans, Crédit Confort for Algerian-made goods, or Islamic finance.",
     "steps": [("4.1", "psg", "Pledge gold for a loan"), ("4.1", "homeloans", "Take a home loan"),
               ("4.1", "confort", "Buy local goods on credit"), ("4.2", "islamic", "Or choose Mourabaha or Ijara")]},
    {"id": "merchant", "who": "pro", "name": "Get paid as a merchant",
     "why": "CIB and EDAHABIA at the terminal and online, and QR through WIMPAY.",
     "steps": [("2.3", "tpe", "Take cards at a terminal"), ("2.3", "webmarchand", "Sell online as a web merchant"),
               ("2.5", "wimpay", "Take QR payments"), ("4.3", "pros", "Borrow to grow")]},
    {"id": "export", "who": "corp", "name": "Sell abroad online",
     "why": "BDL's cross-border acquiring takes Visa and Mastercard from foreign buyers.",
     "steps": [("2.4", "ecomint", "Accept Visa and Mastercard from abroad"), ("3.1", "secure", "Authenticate with 3-D Secure"),
               ("4.4", "trade", "Repatriate through trade finance")]},
    {"id": "diaspora", "who": "dias", "name": "Pay into Algeria from abroad",
     "why": "CNAS contributions by Visa, and Algerian merchants paid by foreign cards.",
     "steps": [("2.4", "cnas", "Pay CNAS contributions by card"), ("5.4", "partners", "Use Djezzy and public platforms"),
               ("2.4", "ecomint", "Buy from Algerian e-merchants")]},
    {"id": "corp", "who": "corp", "name": "Finance a company or project",
     "why": "Investment and working-capital credit, trade, leasing, corporate cards and bulk payments.",
     "steps": [("4.4", "corplending", "Finance an investment"), ("4.5", "leasing", "Lease equipment through SNL"),
               ("2.1", "corpcard", "Give staff corporate cards"), ("5.2", "ebank", "Pay salaries and suppliers in bulk")]},
    {"id": "invest", "who": "inv", "name": "Save and invest",
     "why": "Bons de caisse and savings, or shares in the bank itself since 2025.",
     "steps": [("4.5", "savings", "Buy bons de caisse"), ("1.2", "ipo", "Buy BDL shares"), ("1.2", "owners", "Collect a dividend")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mastercard cards on foreign-currency accounts since 2018, the travel allowance on them, cross-border acquiring since December 2025, and sponsorship of local processing at SATIM.",
     "steps": [("2.2", "mastercard", "Mastercard Titanium and Platinum"), ("2.2", "allowance", "The €750 allowance on a Mastercard"),
               ("2.4", "ecomint", "Mastercard acquiring for exporters"), ("2.6", "satim", "Local processing at SATIM")]},
    {"id": "mcnext", "who": "mc", "name": "Where terminals, exporters and the diaspora could land",
     "why": "Where BDL has needs and Mastercard is not yet in: foreign cards at 17,000 terminals, fraud tools for exporters, the CNAS platform, faster allowance cards, and an international corporate card.",
     "steps": [("2.3", "tpe", "Mastercard acceptance at BDL terminals"), ("3.1", "secure", "Fraud and authentication tools for e-commerce"),
               ("2.4", "cnas", "Mastercard on the CNAS platform"), ("2.2", "allowance", "Faster, tokenised allowance cards"),
               ("2.1", "corpcard", "An international corporate card")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across BDL's map",
    "title": "Mastercard's sponsor bank in a CIB country",
    "lead": "BDL calls itself a Mastercard principal member. It has issued Mastercard Titanium and Platinum cards since 2018, sponsored SATIM's 2023 project to process Mastercard in Algeria, and in December 2025 began acquiring Mastercard for Algerian e-merchants selling abroad. But everyday cards, its 17,000 terminals and WIMPAY run on Algeria's CIB scheme and DZ Mob Pay. Visa sits alongside on international cards and came first in cross-border acquiring. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are BDL's own (H1 2026 COSOB report, October 2026; 2025 annual report) or from GIE Monétique and Algerian press. BDL publishes no card counts by network and no customer count; the status of SATIM's Mastercard processing and the Visa launch date are unconfirmed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Everyday card", "CIB", "Domestic scheme; free, four years"],
        ["International cards", "Mastercard and Visa", "Mastercard since July 2018"],
        ["Travel allowance", "Visa or Mastercard", "€750 on a card from 19 July 2026"],
        ["Terminals", "CIB and EDAHABIA", "17,246 at June 2026"],
        ["Cross-border acquiring", "Visa, then Mastercard", "May 2025 and December 2025"],
        ["Processing", "SATIM", "Mastercard sponsor, 2023 ⚠"],
        ["Mobile", "DZ Mob Pay", "WIMPAY, 2025"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard cards on foreign-currency accounts, the allowance loaded on them, acquiring for exporters, and SATIM's local processing.",
                "deals": "What it does not do: CIB cards and terminals, WIMPAY, CNAS payments, corporate cards, or fraud and data tools."},
        "snb": {"dir": "CIB and EDAHABIA under GIE Monétique, DZ Mob Pay for QR, Visa for international cards, CNAS and the first cross-border acquiring.",
                "deals": "Where they meet: the €750 allowance, which customers can take on either network."},
    },
    "tl": [
        ["Jul 2018", "Mastercard Titanium and Platinum launched"],
        ["Dec 2023", "SATIM convention to process Mastercard in Algeria"],
        ["Jan 2025", "WIMPAY on DZ Mob Pay"],
        ["Mar 2025", "Listed on the Algiers Stock Exchange"],
        ["May 2025", "Cross-border acquiring on Visa; CNAS on Visa"],
        ["Dec 2025", "Cross-border acquiring extended to Mastercard"],
        ["Jul 2026", "€750 allowance moves onto international cards"],
        ["Sep 2026", "Single chairman and CEO, Mustapha Ferfera"],
    ],
    "l": {
        "U": {"d": 1, "s": "Travellers and exporters touch Mastercard; most customers do not.",
              "gap": "Households, merchants and companies use CIB and DZ Mob Pay day to day; travellers choose Visa or Mastercard.",
              "neo": "Mastercard cardholders, exporters taking Mastercard.", "snb": "CIB cardholders, merchants, CNAS payers, Visa cardholders."},
        "L5": {"d": 0, "s": "The front doors are BDL's.", "gap": "DigitBDL, e-banking, branches and public platforms have no network role.", "neo": "None.", "snb": "DigitBDL, e-banking, 185 branches, CNAS and Djezzy."},
        "L4": {"d": 0, "s": "The business lines run on CIB and the balance sheet.", "gap": "Lending, Islamic finance, savings and leasing carry no Mastercard role.",
               "neo": "None.", "snb": "Pawn and home loans, Islamic finance, corporate credit, savings, SNL."},
        "L3": {"d": 1, "s": "3-D Secure on the cards; the rest is BDL's.", "gap": "Authentication rides on the networks; risk, onboarding and travel services are BDL's own.",
               "neo": "3-D Secure on Mastercard.", "snb": "OTP on CIB, risk map, online onboarding, insurance."},
        "L2": {"d": 1, "s": "Mastercard cards, acquiring and processing; CIB for everything else.", "gap": "CIB has cards and terminals and DZ Mob Pay has QR; Mastercard and Visa share international cards and acquiring.",
               "neo": "Mastercard cards, cross-border acquiring, SATIM processing.", "snb": "CIB, EDAHABIA, DZ Mob Pay, Visa."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's; BDL owns 14.7% of SATIM.", "neo": "None.", "snb": "Treasury, shareholders, board, stakes, core system."},
    },
    "t": area_lens(LAYERS),
}
