"""Bank of China's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bankofchina_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("China's oldest and most international bank as five discs that stack into one platform, from RMB40 trillion of "
       "assets and a state owner at the bottom to a mobile bank with 105 million monthly users and BOCHK's wallet at the "
       "top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light "
       "up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes "
       "in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Personal customers", "user-round"),
    ("traveller", "Travellers & students abroad", "plane"),
    ("visitor", "Visitors to China", "earth"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates & traders", "factory"),
    ("hk", "Customers in Hong Kong", "globe"),
]
USERS_DESC = ("Six kinds of customer, about 554 million people and 8.4 million firms in all: personal customers, Chinese "
              "travellers and students going abroad, visitors to China, small businesses, corporates and traders, and "
              "BOCHK's customers in Hong Kong and Southeast Asia.")

WHO = {"con": "A BOC customer", "traveller": "A traveller", "visitor": "A visitor to China", "sme": "A small business",
       "corp": "A corporate treasurer", "hk": "A customer in Hong Kong"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: savings, a debit card on UnionPay at home, quick payments, the mobile bank, a wallet link and fraud checks.",
     "steps": [("4.1", "wealth", "Keep savings with BOC"), ("2.1", "debit", "Pay with a debit card"), ("2.1", "quickpay", "Use quick payments"),
               ("5.1", "app", "Run it in mobile banking"), ("5.4", "wallets", "Link it to WeChat Pay or Alipay"), ("3.1", "fraud", "Protected by Cyber Defence")]},
    {"id": "card", "who": "con", "name": "Borrow on a card",
     "why": "Great Wall credit cards, mostly on UnionPay, with a Great Wall Mastercard for use at home and abroad.",
     "steps": [("2.1", "credit", "Take a Great Wall credit card"), ("2.2", "gwmc", "Or a Great Wall Mastercard"),
               ("3.3", "benefits", "Use BOC Benefits offers")]},
    {"id": "travel", "who": "traveller", "name": "Study or travel abroad",
     "why": "Currency, cross-border cards, Visa and Mastercard credit cards in Apple Pay, and remittances home.",
     "steps": [("2.3", "xborder", "Take a cross-border card"), ("2.2", "mcdual", "Carry a Mastercard dual-application card"),
               ("2.3", "applepay", "Add it to Apple Pay"), ("2.5", "remit", "Send money with BOC Instant Remittance")]},
    {"id": "visit", "who": "visitor", "name": "Pay as a visitor to China",
     "why": "Foreign cards at BOC's merchants and ATMs, and a tax refund on departure.",
     "steps": [("2.4", "foreigncard", "Tap a foreign card"), ("5.3", "outlets", "Withdraw cash at a BOC ATM"),
               ("2.4", "taxrefund", "Claim a departure tax refund")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Inclusive loans, online banking and card acceptance.",
     "steps": [("4.2", "inclusive", "Borrow from BOC"), ("5.2", "corpapp", "Bank online"),
               ("3.4", "openbank", "Use Corporate e-Manager"), ("2.4", "foreigncard", "Take card payments")]},
    {"id": "corp", "who": "corp", "name": "Trade across borders",
     "why": "International settlement, CIPS, RMB clearing and the e-CNY routes the state is building.",
     "steps": [("4.2", "corporate", "Bank with BOC"), ("5.2", "corpapp", "Pay through corporate online banking"),
               ("2.5", "cips", "Settle in RMB through CIPS"), ("2.5", "mbridge", "Try mBridge")]},
    {"id": "hk", "who": "hk", "name": "Bank with BOCHK",
     "why": "Hong Kong cards on Visa, Mastercard and UnionPay, BoC Pay+ and BOCHK's rewards.",
     "steps": [("4.5", "bochk", "Open an account with BOCHK"), ("2.6", "cheers", "Take a Cheers Visa"), ("2.6", "chill", "Or a Chill Mastercard"),
               ("5.4", "bocpay", "Pay with BoC Pay+"), ("3.3", "hkrewards", "Earn Amazing Rewards")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Great Wall Mastercard RMB cards since 2024, dual-application and debit cards, Apple Pay, visitor acceptance and BOCHK's Chill Card.",
     "steps": [("2.2", "gwmc", "Great Wall Mastercard"), ("2.2", "mcdual", "Dual-application credit cards"), ("2.2", "mcdebit", "Mastercard RMB debit"),
               ("2.3", "applepay", "Apple Pay on Mastercard"), ("2.4", "foreigncard", "Acceptance for visitors' cards"), ("2.6", "chill", "BOC Chill Card")]},
    {"id": "mcnext", "who": "mc", "name": "Where travel, visitors and agents could land",
     "why": "Where BOC has needs and Mastercard is thin: student and travel cards, risk tools for the leading foreign-card acquirer, a shrinking credit book, commercial cards for exporters, and agentic payments.",
     "steps": [("2.3", "xborder", "Mastercard benefits for students and travellers"), ("2.4", "foreigncard", "Risk and data for visitor acquiring"),
               ("2.1", "credit", "Data and offers to grow card spending"), ("4.2", "corporate", "Commercial cards for exporters"),
               ("1.4", "ai", "Agent Pay for BOCAI's assistants"), ("2.6", "hkbiz", "A Mastercard business card at BOCHK")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Bank of China's map",
    "title": "Mastercard's first Chinese member, now a small RMB lane in a UnionPay bank",
    "lead": "BOC joined Mastercard in 1987 and issued China's first international credit card on it in 1988. Today UnionPay carries most of its 750 million debit and 152 million credit cards ⚠, and wallets and e-CNY carry much of everyday spending. Since Mastercard NetsUnion opened in May 2024, BOC has issued Great Wall Mastercard RMB cards, added dual-application cards in 2025 and Mastercard debit and Apple Pay in 2026. It leads foreign-card acquiring for visitors. In Hong Kong the Chill Card is Mastercard, while Visa holds BOCHK's flagship and business cards, and Visa won approval to prepare domestic clearing on 13 October 2026. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are BOC's own (2026 Interim Report, 28 August 2026; 2025 Annual Report) and BOCHK's (2026 interim results), or from Mastercard, Visa and press. BOC does not disclose its card split by network; UnionPay's domestic share is inferred.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Domestic cards", "UnionPay ⚠", "750m debit, 152m credit issued"],
        ["RMB Mastercard", "Great Wall Mastercard", "Since NetsUnion opened, May 2024"],
        ["Dual-application", "Mastercard", "Home and abroad, 2025"],
        ["Dual-brand", "Visa–UnionPay", "Chip upgrade from May 2025"],
        ["Visitors", "Foreign-card acquiring", "+64% in H1 2026"],
        ["Hong Kong", "Chill (Mastercard)", "Cheers and business cards on Visa"],
        ["Visa in China", "Approval to prepare", "13 October 2026"],
        ["Digital money", "e-CNY, mBridge", "PBOC rails"],
    ],
    "sides": {
        "neo": {"dir": "Great Wall Mastercard RMB, dual-application and debit cards, Apple Pay on Mastercard, acceptance of visitors' cards, and the BOCHK Chill, Taobao and Esso Mastercards.",
                "deals": "What it does not do: domestic debit, most credit, wallets, e-CNY, cross-border RMB, fraud, AI or rewards."},
        "snb": {"dir": "UnionPay at home and in BoC Pay+, Visa on dual-brand, Olympic and BOCHK flagship and business cards, WeChat Pay and Alipay, and PBOC's e-CNY and mBridge.",
                "deals": "Where they meet: travel and student cards, visitor acceptance and BOCHK."},
    },
    "tl": [
        ["1987", "First Chinese member of Mastercard and Visa"],
        ["1988", "Great Wall International Card on Mastercard"],
        ["1992", "Card centre acquires Mastercard and Visa in China"],
        ["Oct 2011", "BOC Private Bank American Express Card"],
        ["Sep 2021", "Visa and BOC at Beijing 2022"],
        ["Jun 2022", "BOC Chill Card with Mastercard"],
        ["Nov 2023", "Mastercard NetsUnion licensed"],
        ["May 2024", "Great Wall Mastercard RMB cards"],
        ["May 2025", "Visa–UnionPay cards move to chip"],
        ["2025", "Mastercard dual-application credit cards"],
        ["H1 2026", "Mastercard RMB debit; Apple Pay"],
        ["Oct 2026", "Visa approved to prepare domestic clearing"],
    ],
    "l": {
        "U": {"d": 1, "s": "Travellers and some Hong Kong customers carry Mastercard; most others carry UnionPay.",
              "gap": "Mastercard reaches travellers, students and Chill cardholders, and visitors at BOC's terminals; everyday customers carry UnionPay ⚠.",
              "neo": "Travellers, visitors, Chill cardholders.", "snb": "Everyday customers, small businesses, corporates."},
        "L5": {"d": 0, "s": "The front doors are BOC's and the wallets'.", "gap": "Mobile banking, outlets and corporate online banking are BOC's; BoC Pay+ runs on UnionPay.",
               "neo": "Mastercard cards inside wallets.", "snb": "Mobile banking, outlets, WeChat Pay, Alipay, BoC Pay+."},
        "L4": {"d": 0, "s": "Only BOCHK's card arm touches Mastercard.", "gap": "BOCHK issues Mastercard beside Visa and UnionPay; loans, wealth, treasury and insurance have no network role.",
               "neo": "BOCHK cards.", "snb": "Deposits, loans, treasury, BOCI, BOC Life, BOC Aviation."},
        "L3": {"d": 0, "s": "Fraud, AI and rewards are BOC's own.", "gap": "No Mastercard fraud, data or offers tools found at BOC.",
               "neo": "None found.", "snb": "Cyber Defence, BOCAI, BOC Benefits, Amazing Rewards, open banking."},
        "L2": {"d": 1, "s": "A Mastercard travel and RMB lane beside UnionPay's domestic core.", "gap": "Mastercard carries the Great Wall Mastercard, dual-application and debit cards and the Chill Card; UnionPay, Visa and PBOC rails carry the rest.",
               "neo": "Great Wall Mastercard, dual-application, debit, Chill, acceptance.", "snb": "UnionPay cards, Visa–UnionPay, Cheers, e-CNY, mBridge, CIPS."},
        "L1": {"d": 0, "s": "The state bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's, though the card history began with it.", "neo": "None.", "snb": "Capital, state owners, AI, global network."},
    },
    "t": area_lens(LAYERS),
}
