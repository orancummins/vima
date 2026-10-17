"""ICBC's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from icbc_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The world's largest bank as five discs that stack into one platform, from RMB57 trillion of assets and state "
       "ownership at the bottom to a mobile bank used by more than 300 million people a month at the top. Click the stack "
       "to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Personal customers", "user-round"),
    ("traveller", "Travellers abroad", "plane"),
    ("visitor", "Visitors to China", "earth"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
    ("abroad", "Customers abroad", "globe"),
]
USERS_DESC = ("Six kinds of customer, more than 780 million people and 15 million firms in all: personal customers, "
              "Chinese travellers going abroad, visitors to China, small businesses, corporates, and customers of "
              "ICBC's banks abroad.")

WHO = {"con": "An ICBC customer", "traveller": "A traveller", "visitor": "A visitor to China", "sme": "A small business",
       "corp": "A corporate treasurer", "abroad": "A customer in Hong Kong"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a deposit account, a debit card on UnionPay at home, the mobile bank, a wallet link and fraud checks.",
     "steps": [("4.1", "deposits", "Keep savings with ICBC"), ("2.1", "debit", "Pay with a debit card"), ("5.1", "app", "Run it in mobile banking"),
               ("5.4", "wallets", "Link it to WeChat Pay or Alipay"), ("3.1", "fraud", "Protected from telecom fraud")]},
    {"id": "travel", "who": "traveller", "name": "Travel to Europe",
     "why": "The European Travel card and multi-currency cards on Mastercard, with offers from ICBC Travel.",
     "steps": [("5.1", "app", "Apply in the app"), ("2.2", "etc", "Take the European Travel Mastercard"), ("2.2", "mc101", "Hold currency on the 10+1 debit card"),
               ("3.3", "elife", "Plan with ICBC Travel"), ("3.3", "ibonus", "Earn iBonus points")]},
    {"id": "card", "who": "con", "name": "Borrow on a card",
     "why": "Peony credit cards, mostly on UnionPay, and the China Mastercard, approved with AI.",
     "steps": [("2.1", "credit", "Take a Peony credit card"), ("2.2", "mcrmb", "Or a China Mastercard"),
               ("3.2", "cardai", "Approved with the AI assistant"), ("3.3", "ibonus", "Collect iBonus points")]},
    {"id": "visit", "who": "visitor", "name": "Pay as a visitor to China",
     "why": "Foreign cards at ICBC terminals and ATMs, Weixin Pay for overseas UnionPay cards, and Instant Refund on departure.",
     "steps": [("2.4", "inbound", "Tap a foreign card"), ("2.4", "weixin", "Link a card to Weixin Pay"),
               ("5.3", "outlets", "Withdraw cash at an ICBC ATM"), ("2.4", "acquiring", "Claim an Instant Refund")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Inclusive loans, the Operation+ platform, card acceptance and corporate online banking.",
     "steps": [("4.2", "inclusive", "Borrow with an e Loan"), ("5.2", "corpapp", "Bank online"),
               ("3.4", "operation", "Run payroll and tax on Operation+"), ("2.4", "acquiring", "Take card payments")]},
    {"id": "corp", "who": "corp", "name": "Move money across borders",
     "why": "IGPS, cross-border RMB and the e-CNY routes the state is building.",
     "steps": [("4.2", "corporate", "Bank with ICBC"), ("2.5", "igps", "Pay locally through IGPS"),
               ("2.5", "rmbclear", "Settle in RMB"), ("2.6", "mbridge", "Try mBridge and e-CNY")]},
    {"id": "hk", "who": "abroad", "name": "Bank with ICBC in Hong Kong",
     "why": "ICBC (Asia): credit cards on Mastercard, Visa and UnionPay, virtual cards and Click to Pay.",
     "steps": [("4.5", "asia", "Take an ICBC (Asia) Platinum Mastercard"), ("4.5", "macau", "Or a Macau co-brand"),
               ("2.6", "mbridge", "Use cross-border e-CNY")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "RMB-capable Mastercard cards since 2024, the European Travel card, Peony international debit, co-brands since 1995 and ICBC's banks abroad.",
     "steps": [("2.2", "mcrmb", "China Mastercard"), ("2.2", "mc101", "10+1 multi-currency debit"), ("2.2", "etc", "European Travel card"),
               ("2.3", "peonyintl", "Peony Mastercard"), ("4.5", "asia", "ICBC (Asia) and Macau cards")]},
    {"id": "mcnext", "who": "mc", "name": "Where travel, visitors and agents could land",
     "why": "Where ICBC has needs and Mastercard is barely in: more travel cards, acceptance for visitors, a shrinking credit book, fraud on cross-border cards, commercial cards and agentic payments.",
     "steps": [("3.3", "elife", "Travel offers inside ICBC Travel"), ("2.4", "inbound", "Mastercard acceptance for visitors"),
               ("2.1", "credit", "Data and offers to grow card spending"), ("3.1", "fraud", "Scoring on cross-border cards"),
               ("4.2", "inclusive", "Commercial cards"), ("3.2", "agents", "Agent Pay for ICBC's agents")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across ICBC's map",
    "title": "A UnionPay giant opening a Mastercard travel lane",
    "lead": "Most of ICBC's 1.3 billion cards run on UnionPay at home ⚠, and wallets and e-CNY carry much of everyday spending. Mastercard's lane is travel. Since Mastercard NUCC opened in May 2024, ICBC has issued a China Mastercard RMB card, a '10+1' multi-currency debit card (2025) and a European Travel co-brand (February 2026). Peony international debit comes on Visa and Mastercard, and ICBC's banks in Hong Kong, Macau and Argentina issue Mastercard alongside Visa and UnionPay. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are ICBC's own (2026 Interim Report, 24 September 2026; 2025 Annual Report) or from Mastercard, the European Travel Commission, UnionPay and press. ICBC does not disclose its card split by network; UnionPay's domestic share is inferred.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Domestic cards", "UnionPay ⚠", "1,196m debit, 143m credit"],
        ["RMB Mastercard", "China Mastercard", "Since NUCC opened, May 2024"],
        ["Multi-currency debit", "Mastercard 10+1", "2025, first of its kind"],
        ["Travel co-brand", "European Travel card", "With ETC, February 2026"],
        ["International debit", "Peony", "Visa and Mastercard"],
        ["Hong Kong", "ICBC (Asia)", "Mastercard, Visa, UnionPay"],
        ["Visitors", "Visa–UnionPay zone", "Beijing, March 2025 ⚠"],
        ["Digital money", "e-CNY, mBridge", "PBC rails"],
    ],
    "sides": {
        "neo": {"dir": "RMB and travel Mastercard cards, Peony Mastercard, co-brands since 1995, and ICBC's banks in Hong Kong, Macau and Argentina.",
                "deals": "What it does not do: domestic debit, most credit, wallets, e-CNY, cross-border RMB, fraud or AI."},
        "snb": {"dir": "UnionPay at home and in Hong Kong debit, Visa on every international product, Alipay and WeChat Pay, and PBC's e-CNY and mBridge.",
                "deals": "Where they meet: travel cards, visitor acceptance and ICBC's banks abroad."},
    },
    "tl": [
        ["1995", "First Mastercard co-brand in China"],
        ["Feb 2017", "Sands Lifestyle Mastercard in Hong Kong and Macau"],
        ["Nov 2023", "Mastercard NUCC licensed"],
        ["May 2024", "China Mastercard RMB card"],
        ["Nov 2024", "Weixin Pay for overseas UnionPay cards via ICBC"],
        ["Mar 2025", "Visa–UnionPay zone in Beijing"],
        ["2025", "Mastercard 10+1 debit card"],
        ["Feb 2026", "European Travel co-branded card"],
        ["Jun 2026", "Joint RMB clearing bank for Africa"],
    ],
    "l": {
        "U": {"d": 1, "s": "Travellers and customers abroad carry Mastercard; most others carry UnionPay.",
              "gap": "Mastercard reaches outbound travellers and customers in Hong Kong, Macau and Argentina; everyday customers carry UnionPay ⚠.",
              "neo": "Travellers, holders of ICBC's banks-abroad cards.", "snb": "Everyday customers, visitors, small businesses, corporates."},
        "L5": {"d": 0, "s": "The front doors are ICBC's.", "gap": "Mobile banking, outlets and corporate online banking are ICBC's; wallets carry its cards.",
               "neo": "Mastercard cards inside wallets.", "snb": "Mobile banking, outlets, Alipay and WeChat Pay."},
        "L4": {"d": 0, "s": "Banks abroad are split; the core lines are not card businesses.", "gap": "ICBC (Asia), Macau and Argentina issue Mastercard alongside Visa and UnionPay; loans, wealth and treasury have no network role.",
               "neo": "ICBC (Asia), ICBC (Macau), ICBC (Argentina).", "snb": "Deposits, loans, treasury, subsidiaries, ICBC USA."},
        "L3": {"d": 0, "s": "Fraud, AI and rewards are ICBC's own.", "gap": "No Mastercard fraud, data or offers tools found at ICBC.",
               "neo": "None found.", "snb": "Anti-fraud models, AI agents, iBonus, e-Life, open banking."},
        "L2": {"d": 1, "s": "A Mastercard travel lane beside UnionPay's domestic core.", "gap": "Mastercard carries the RMB, multi-currency and travel cards and half of Peony international debit; UnionPay, Visa and PBC rails carry the rest.",
               "neo": "China Mastercard, 10+1 debit, European Travel card, Peony Mastercard.", "snb": "UnionPay cards, Visa, e-CNY, mBridge, IGPS, RMB clearing."},
        "L1": {"d": 0, "s": "The state bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, state owners, AI, strategy, network."},
    },
    "t": area_lens(LAYERS),
}
