"""Intesa Sanpaolo's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from intesa_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Italy's largest bank as five discs that stack into one platform, from €437 billion of loans and a cloud core at "
       "the bottom to the Intesa Sanpaolo and Isybank apps, 2,644 branches and 19,100 advisers at the top. Click the stack "
       "to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Isybank & young customers", "smartphone"),
    ("excl", "Exclusive & private clients", "gem"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
    ("intl", "Customers abroad", "globe"),
]
USERS_DESC = ("Six kinds of customer, about 21 million in all: about 13.9 million in Italy, from everyday and Isybank "
              "customers to Exclusive and private clients, small businesses and corporates, and about 7.5 million at the "
              "group's banks in twelve other countries.")

WHO = {"con": "An Intesa Sanpaolo customer", "young": "An Isybank customer", "excl": "An Exclusive client",
       "sme": "A small business", "corp": "A corporate treasurer", "intl": "A customer abroad"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "An XME account, a debit card that is Bancomat at home and Visa or Mastercard abroad, the app and Intesa's own security.",
     "steps": [("4.1", "accounts", "Open an XME account"), ("2.1", "debit", "Pay with XME Debit"), ("2.5", "wallets", "Pay by phone"),
               ("5.1", "app", "Run it in the app"), ("3.1", "fraud", "Set Geocontrol and 3-D Secure")]},
    {"id": "digital", "who": "young", "name": "Bank on Isybank",
     "why": "The app-only bank on isytech, with cards issued on Mastercard ⚠ and BANCOMAT Pay for friends.",
     "steps": [("4.2", "isybank", "Open an isyLight plan"), ("2.4", "isycards", "Get an Isybank card"), ("2.5", "bpay", "Send money with BANCOMAT Pay"),
               ("2.7", "instant", "Make instant transfers"), ("3.3", "rewards", "Collect isyReward")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "XME credit cards on Mastercard or Visa, with SpensieRata instalments.",
     "steps": [("2.2", "credit", "Choose Mastercard or Visa credit"), ("3.4", "spensierata", "Spread a purchase with SpensieRata"),
               ("3.3", "rewards", "Earn stars in the prize contest")]},
    {"id": "exclusive", "who": "excl", "name": "Live the Exclusive life",
     "why": "Mastercard-only Exclusive cards, a concierge, and advisers from Fideuram.",
     "steps": [("2.3", "exclusive", "Carry the Exclusive Mastercard"), ("3.3", "rewards", "Earn Exclusive Club points"),
               ("5.3", "advisers", "Meet an adviser"), ("4.5", "wealth", "Invest with Fideuram and Eurizon")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account and cards, Nexi POS and SoftPOS, and BANCOMAT Pay at the till.",
     "steps": [("4.3", "business", "Open a business account"), ("2.6", "accept", "Take cards with Nexi SoftPOS"),
               ("2.5", "bpay", "Accept BANCOMAT Pay"), ("5.2", "branches", "Bank with a branch")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "IMI CIB transaction banking and the stablecoin pilots.",
     "steps": [("4.4", "cib", "Bank with IMI CIB"), ("2.7", "digitalmoney", "Test euro stablecoin settlement")]},
    {"id": "abroad", "who": "intl", "name": "Bank with a group bank abroad",
     "why": "Twelve subsidiary banks, from Croatia to Egypt, each with its own network mix.",
     "steps": [("4.6", "intl", "Bank with PBZ, VUB or ALEXBANK"), ("4.6", "beograd", "Bank with Banca Intesa Beograd")]},
    {"id": "give", "who": "con", "name": "Give at the ATM",
     "why": "Micro-donations to Caritas on Mastercard cards, and the Exclusive card's fee donation.",
     "steps": [("5.2", "branches", "Withdraw at an Intesa ATM"), ("3.3", "donations", "Donate a euro with a Mastercard card")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The Exclusive cards and most prepaid cards, Isybank's cards ⚠, half of XME debit and credit by customer choice, and a history from MasterPass to the Caritas donations.",
     "steps": [("2.3", "exclusive", "Exclusive credit and debit on Mastercard"), ("2.4", "isycards", "Isybank cards on Mastercard ⚠"),
               ("2.3", "prepaid", "Prepaid cards on Mastercard"), ("2.1", "debit", "XME debit when Mastercard is chosen"),
               ("3.3", "donations", "Caritas donations, 2020–23")]},
    {"id": "mcnext", "who": "mc", "name": "Where Isybank, instalments and agents could land",
     "why": "Where Intesa has needs and Mastercard is not yet in: Isybank's growth, SpensieRata at checkout, agentic AI, card-linked offers against my Visa, commercial cards and stablecoin settlement.",
     "steps": [("4.2", "isybank", "Make Isybank a Mastercard showcase"), ("3.4", "spensierata", "Mastercard Installments for SpensieRata"),
               ("3.2", "ai", "Agent Pay for the AI projects"), ("3.3", "rewards", "Card-linked offers against my Visa"),
               ("4.3", "business", "Commercial cards against Visa"), ("2.7", "digitalmoney", "Stablecoin settlement")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Intesa Sanpaolo's map",
    "title": "Mastercard at the top of the book, Visa with the contract, Bancomat at home",
    "lead": "Intesa Sanpaolo lets customers choose Visa or Mastercard on its debit and most credit cards, while domestic debit runs on Bancomat, a scheme Intesa co-controls. Mastercard alone carries the Exclusive cards for affluent clients, most prepaid cards and, it appears, Isybank's cards. Visa renewed a multi-year strategic partnership in November 2024 and has the network offers. Mastercard's dated joint work runs from MasterPass in 2014 to Caritas ATM donations in 2020. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 results, 29 July 2026; 2026–2029 Business Plan, 2 February 2026) or from Intesa's product pages, Visa, Bancomat and press. Volumes by network are not published; Isybank's network rests on its own promotion.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Bancomat + Visa or Mastercard", "The customer chooses"],
        ["Credit", "Mastercard or Visa", "XME Credit Card and Credit Icon"],
        ["Exclusive", "Mastercard", "Credit May 2021, debit Nov 2021"],
        ["Isybank", "Mastercard ⚠", "About 1.2 million customers"],
        ["Strategic deal", "Visa", "Renewed 4 November 2024"],
        ["Domestic scheme", "Bancomat", "Intesa in the controlling pact"],
        ["Acceptance", "Nexi", "Exclusive partner since 2020"],
        ["Stablecoins", "Eur.Bank, Qivalis", "Testing from June 2026"],
    ],
    "sides": {
        "neo": {"dir": "Exclusive credit and debit, most prepaid, Isybank cards ⚠, half of XME debit and credit by choice, and acceptance on Nexi terminals.",
                "deals": "What it does not have: a current announced partnership, the domestic debit leg, offers, instalments or the AI projects."},
        "snb": {"dir": "Visa's renewed partnership, my Visa offers and business reporting; Bancomat and BANCOMAT Pay at home; Nexi for processing and acceptance; Eur.Bank and Qivalis for stablecoins.",
                "deals": "Where they meet: every XME card, where the customer picks the network."},
    },
    "tl": [
        ["Jul 2014", "Mastercard partnership; MasterPass from October"],
        ["May 2016", "Card processing sold to Mercury, now Nexi"],
        ["Dec 2019", "Acquiring to Nexi; 9.9% stake"],
        ["Jul 2020", "Caritas ATM donations with Mastercard"],
        ["May 2021", "Exclusive credit card on Mastercard"],
        ["2023", "Isybank launched; FSI joins Bancomat ⚠"],
        ["Nov 2024", "Visa strategic partnership renewed"],
        ["Feb 2026", "2026–2029 Business Plan"],
        ["Jun 2026", "Eur.Bank stablecoin tests; Qivalis"],
        ["Jul 2026", "H1: Isybank at 1.2 million"],
    ],
    "l": {
        "U": {"d": 1, "s": "Exclusive, prepaid and Isybank holders carry Mastercard; others choose.",
              "gap": "Exclusive clients and Isybank customers carry Mastercard ⚠; everyday customers pick Visa or Mastercard on top of Bancomat.",
              "neo": "Exclusive clients, prepaid holders, Isybank customers ⚠, XME holders who chose it.", "snb": "XME holders who chose Visa, Bancomat users, corporates, customers abroad."},
        "L5": {"d": 0, "s": "The front doors are Intesa's.", "gap": "Apps, branches and advisers are the group's own.", "neo": "None.", "snb": "Apps, branches, advisers, Nexi and Mooney."},
        "L4": {"d": 1, "s": "Isybank and the Exclusive book lean Mastercard.", "gap": "Isybank issues on Mastercard ⚠; business cards lean Visa ⚠; corporate, wealth and insurance have no network role.",
               "neo": "Isybank ⚠, Exclusive clients.", "snb": "Business cards, IMI CIB, Fideuram, Eurizon, insurance."},
        "L3": {"d": 0, "s": "Services are Intesa's, with Visa offers.", "gap": "Security, AI and SpensieRata are Intesa's own; Visa runs my Visa; the Caritas programme has ended.",
               "neo": "Isybank promotions; past ATM donations.", "snb": "Security, AI, SpensieRata, my Visa."},
        "L2": {"d": 1, "s": "Split card by card, Bancomat underneath.", "gap": "Mastercard alone on Exclusive, prepaid and Isybank ⚠; shared on XME; absent from BANCOMAT Pay, instant transfers and stablecoins.",
               "neo": "Exclusive, prepaid, Isybank cards, half of XME.", "snb": "Bancomat, BANCOMAT Pay, Visa, Nexi, Eur.Bank."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's; processing is Nexi's.", "neo": "None.", "snb": "Capital, isytech, Nexi processing, the plan."},
    },
    "t": area_lens(LAYERS),
}
