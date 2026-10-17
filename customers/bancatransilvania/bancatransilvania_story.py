"""Banca Transilvania's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bancatransilvania_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Romania's largest bank as five discs that stack into one platform, from RON 233 billion of group assets at the "
       "bottom to BT Pay, branches and partners at the top. Click the stack to open it. Choose who you are and what you "
       "want to do, and the areas that deliver it light up across the layers, joined in the order they act. Switch to "
       "the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young & mobile-first", "smartphone"),
    ("dias", "Romanians abroad", "earth"),
    ("saver", "Savers & investors", "coins"),
    ("sme", "Micro & small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
    ("merch", "Merchants", "store"),
]
USERS_DESC = ("Seven kinds of customer, nearly 5 million active in all: everyday customers, the young and mobile-first, "
              "Romanians abroad, savers and investors, about 600,000 companies from micro firms to corporates, and the "
              "merchants who take cards on BT's terminals.")

WHO = {"con": "A BT customer", "young": "A young customer", "dias": "A Romanian abroad", "saver": "A saver",
       "sme": "A small business", "corp": "A corporate treasurer", "merch": "A merchant"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a debit card on either scheme, phone payments in BT Pay and instant transfers.",
     "steps": [("4.1", "accounts", "Open an account"), ("2.1", "debitmc", "Pay with a debit card"), ("2.5", "wallet", "Pay by phone in BT Pay"),
               ("2.6", "ropay", "Send money with RoPay"), ("3.4", "chatbt", "Ask Chat BT")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Star Forte on Mastercard with instalments at STAR merchants, or Flying Blue on Visa.",
     "steps": [("2.2", "star", "Take a Star Forte card"), ("3.1", "starloyalty", "Split purchases at STAR merchants"),
               ("2.2", "flyingblue", "Or earn miles with Flying Blue")]},
    {"id": "fan", "who": "young", "name": "Carry a fan's card",
     "why": "Co-brands made in BT Pay: McLaren on Mastercard and UNTOLD on Visa.",
     "steps": [("5.1", "btpay", "Open BT Pay"), ("2.3", "mclaren", "Issue a McLaren Mastercard"), ("3.1", "benefits", "Collect Priceless and race cashback"),
               ("2.3", "untold", "Or carry BT Visa UNTOLD")]},
    {"id": "digital", "who": "young", "name": "Bank only on the phone",
     "why": "Salt Bank's Mastercard, or BT Pay Kiddo for children.",
     "steps": [("4.2", "saltbank", "Join Salt Bank"), ("4.1", "kiddo", "Start a child on BT Pay Kiddo")]},
    {"id": "abroad", "who": "dias", "name": "Bank from abroad",
     "why": "Onboarding in BT Pay, an Italian IBAN and money home.",
     "steps": [("5.4", "diaspora", "Open an account from abroad"), ("2.6", "btpayitalia", "Use BT Pay Italia"),
               ("2.1", "fxcards", "Hold a euro card"), ("2.6", "remit", "Collect remittances at ATMs")]},
    {"id": "save", "who": "saver", "name": "Save, invest and retire",
     "why": "Funds, shares and pensions inside BT Pay.",
     "steps": [("5.1", "btpay", "Open BT Pay"), ("4.6", "invest", "Buy funds and shares"), ("4.6", "pensii", "Save with BT Pensii")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account in BT Go, business cards, leasing and card acceptance.",
     "steps": [("4.3", "smebank", "Open a business account"), ("5.1", "btgo", "Run it in BT Go"), ("2.2", "bizcards", "Pay with a business card"),
               ("4.5", "leasing", "Lease equipment")]},
    {"id": "merchant", "who": "merch", "name": "Take payments",
     "why": "Romania's largest acceptance network, online checkout and RoPay at the till.",
     "steps": [("2.4", "pos", "Take cards on a BT terminal"), ("2.4", "btpos", "Or on a phone with BTPOS"), ("2.4", "ecomm", "Sell online with BTeComm"),
               ("2.5", "paywithbtpay", "Offer Pay with BT Pay"), ("2.6", "ropay", "Accept RoPay QR")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mastercard debit lines, Star Forte, the McLaren co-brand, Salt Bank and acceptance across BT's terminals.",
     "steps": [("2.1", "debitmc", "Mastercard debit"), ("2.2", "star", "Star Forte credit"), ("2.3", "mclaren", "McLaren F1 co-brand"),
               ("4.2", "saltbank", "Salt Bank's Mastercard"), ("2.4", "pos", "Acceptance on 177,000 terminals")]},
    {"id": "mcnext", "who": "mc", "name": "Where tokens, identity and offers could land",
     "why": "Where BT has needs and Mastercard is not yet in: agentic payments in BT Pay, identity against Visa's EU wallet lead, scam tools for instant payments, card-linked offers for STAR and commercial cards for 600,000 firms.",
     "steps": [("3.4", "chatbt", "Agent Pay behind Chat BT"), ("3.2", "eudi", "Identity and authentication"), ("3.3", "fraud", "Scam and fraud scoring"),
               ("3.1", "starloyalty", "Card-linked offers"), ("4.3", "smebank", "Commercial cards and spend controls"), ("2.6", "btpayitalia", "Cross-border for the diaspora")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Banca Transilvania's map",
    "title": "A two-scheme bank: Mastercard has the racing card, Visa the identity seat",
    "lead": "Banca Transilvania issues more than 8 million cards on both Mastercard and Visa and does not publish the split. Mastercard carries Star Forte, debit lines, business cards, all of Salt Bank and the McLaren F1 co-brand launched in July 2025. Visa carries the larger UNTOLD and Flying Blue co-brands and BT's EU Digital Identity Wallet work. RoPay instant payments now run in BT Pay. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are BT's own (H1 2026 results, 21 August 2026; 2025 preliminary results, 27 February 2026) or from BT releases reprinted in Romanian press. BT's website could not be read directly; networks for some STAR cards and the split by scheme are not public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Cards", "Mastercard and Visa", "8 million+; split not published"],
        ["Credit", "Star Forte on Mastercard", "Flying Blue on Visa (35,000)"],
        ["Co-brands", "McLaren on Mastercard", "About 80,000; UNTOLD on Visa 200,000+"],
        ["Salt Bank", "Mastercard", "Debit only; 400,000+ clients"],
        ["Identity", "Visa", "EU wallet payments, July 2025"],
        ["Instant", "RoPay", "In BT Pay from October 2025"],
        ["Acceptance", "BT", "177,000 POS, all schemes"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard debit lines, Star Forte, business cards, Salt Bank, the McLaren co-brand with Priceless, and acceptance across BT's terminals.",
                "deals": "What it does not do: the UNTOLD and Flying Blue co-brands, EU wallet identity, RoPay, STAR loyalty or Chat BT."},
        "snb": {"dir": "Visa's co-brands and EU wallet pilot, Transfond's RoPay, BT's own STAR loyalty, risk models and AI.",
                "deals": "Where they meet: BT Pay, which holds both schemes' cards."},
    },
    "tl": [
        ["2003", "Star Forte, BT's first credit card"],
        ["2015", "Remittances at ATMs with Western Union and Mastercard"],
        ["2018", "BT Pay, Romania's first bank wallet"],
        ["2023", "Animated BT Visa UNTOLD card"],
        ["2024", "Salt Bank launches on Mastercard"],
        ["Feb 2025", "OTP Bank Romania merged into BT"],
        ["Jul 2025", "EU wallet payments with Visa; McLaren Mastercard cards"],
        ["Oct 2025", "RoPay in BT Pay"],
        ["Mar 2026", "Physical McLaren Debit Gold"],
        ["Nov 2026", "Visa and BT host WE BUILD in Bucharest"],
    ],
    "l": {
        "U": {"d": 1, "s": "Many customers carry Mastercard, many carry Visa.",
              "gap": "BT does not publish the split; Salt Bank and McLaren holders are all on Mastercard, UNTOLD and Flying Blue holders on Visa.",
              "neo": "Salt Bank, McLaren, Star Forte and Mastercard debit holders.", "snb": "UNTOLD and Flying Blue holders, RoPay users."},
        "L5": {"d": 1, "s": "BT Pay holds both schemes' cards.", "gap": "Apps, branches and partners are BT's; McLaren is the Mastercard partner.",
               "neo": "McLaren partnership; cards in BT Pay.", "snb": "UNTOLD, Flying Blue, Netopia, branches."},
        "L4": {"d": 1, "s": "Salt Bank is Mastercard; the rest carries both schemes or none.", "gap": "Accounts come with cards on both schemes; lending, pensions and Moldova have no network role.",
               "neo": "Salt Bank; part of retail and SME cards.", "snb": "Loans, leasing, investments, pensions."},
        "L3": {"d": 0, "s": "Services are BT's own or Visa's.", "gap": "Identity work is with Visa; loyalty, fraud and AI are BT's; Priceless rides only on McLaren.",
               "neo": "Priceless benefits on McLaren.", "snb": "EU wallet with Visa, STAR, Chat BT, risk models."},
        "L2": {"d": 1, "s": "Both schemes, plus RoPay.", "gap": "Mastercard has Star Forte, McLaren and Salt; Visa has UNTOLD and Flying Blue; RoPay is domestic.",
               "neo": "Debit lines, Star Forte, McLaren, remittances, acceptance.", "snb": "UNTOLD, Flying Blue, RoPay."},
        "L1": {"d": 0, "s": "BT's own foundation.", "gap": "Nothing in the foundation is Mastercard's; BT holds Visa and Mastercard shares.", "neo": "None.", "snb": "Capital, owners, deals, strategy."},
    },
    "t": area_lens(LAYERS),
}
