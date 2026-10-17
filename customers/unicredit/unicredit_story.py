"""UniCredit's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from unicredit_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A pan-European bank of 13 banks as five discs that stack into one platform, from €443 billion of loans and "
       "a 49.65% position in Commerzbank at the bottom to buddy, the apps and 3,075 branches at the top. Click the stack "
       "to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young people", "graduation-cap"),
    ("inv", "Savers & investors", "trending-up"),
    ("sme", "Small businesses", "briefcase"),
    ("merch", "Merchants", "store"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer, about 17.5 million clients in all, 15 million of them active: everyday customers in Italy, "
              "Germany, Austria and CEE, young people, savers and investors, small businesses, merchants and corporates.")

WHO = {"con": "A UniCredit customer", "young": "A young customer", "inv": "An investor", "sme": "A small business",
       "merch": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day in Italy",
     "why": "A Genius account through buddy, a MyOne debit card, a phone wallet and the app.",
     "steps": [("5.1", "buddy", "Open an account with buddy"), ("2.2", "myone", "Pay with MyOne debit"), ("2.7", "wallets", "Add it to a phone wallet"),
               ("5.2", "apps", "Run it in the app"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "germany", "who": "con", "name": "Bank with HVB in Germany",
     "why": "The PlusKonto, the new Mastercard debit card, a girocard for home and valyou benefits.",
     "steps": [("4.2", "hvb", "Open a PlusKonto"), ("2.4", "ucard", "Switch to the UniCredit Card"), ("2.4", "girocard", "Keep a girocard"),
               ("3.3", "valyou", "Collect valyou benefits")]},
    {"id": "credit", "who": "con", "name": "Borrow and travel on a card",
     "why": "Flexia instalments, Flexia Gold with Miles & More, and Priceless.",
     "steps": [("2.3", "flexia", "Spread a purchase with Flexia"), ("2.3", "flexiagold", "Move up to Flexia Gold"), ("3.3", "priceless", "Book a Priceless experience")]},
    {"id": "young", "who": "young", "name": "Get a first card",
     "why": "Genius Pay buddy for 11–17-year-olds, run from the app.",
     "steps": [("2.2", "geniuspay", "Get Genius Pay buddy"), ("5.2", "apps", "Manage it in the app"), ("2.7", "wallets", "Pay by phone")]},
    {"id": "invest", "who": "inv", "name": "Invest and insure",
     "why": "onemarkets funds, bancassurance and a premium card.",
     "steps": [("5.3", "branches", "Meet an adviser"), ("4.5", "onemarkets", "Invest in onemarkets funds"), ("4.5", "insurance", "Insure with UniCredit Life"),
               ("2.3", "ferrari", "Carry the Ferrari Metal Card")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "HVB's embedded loans, instant payments and a business debit card.",
     "steps": [("4.2", "hvb", "Bank with HVB"), ("2.4", "ucard", "Pay with a business debit card"), ("4.2", "banxware", "Borrow inside a partner's platform"),
               ("2.8", "instant", "Pay suppliers instantly")]},
    {"id": "merch", "who": "merch", "name": "Take card payments",
     "why": "Bank Austria's in-house acquiring and Nexi-processed acquiring in Italy.",
     "steps": [("2.6", "baacq", "Take cards with Bank Austria"), ("2.6", "itacq", "Take cards in Italy"), ("2.8", "a2a", "Collect bills with CBILL and PagoPA")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Cash management in 100+ currencies, trade finance and the Qivalis stablecoin.",
     "steps": [("4.4", "cib", "Bank with CIB"), ("4.4", "trade", "Finance trade"), ("2.8", "gps", "Pay in 100+ currencies"),
               ("2.9", "qivalis", "Settle in a euro stablecoin")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The 2023 group deal, HVB's switch to Mastercard debit, Italian credit and prepaid, Priceless and the Touch Card.",
     "steps": [("2.1", "mcdeal", "One deal for 13 banks"), ("2.4", "ucard", "HVB debit on Mastercard"), ("2.3", "flexiagold", "Italian credit on Mastercard"),
               ("2.2", "geniuspay", "Genius Pay prepaid"), ("3.3", "priceless", "Priceless and Travel Rewards"), ("2.5", "touch", "Touch Card in Austria")]},
    {"id": "mcnext", "who": "mc", "name": "Where Commerzbank, acquiring and agents could land",
     "why": "Where UniCredit has needs and Mastercard is not yet in: Visa's share of MyOne, Commerzbank's card estate, scam scores, Bank Austria's acquirer, cross-border flows, agents and the euro stablecoin.",
     "steps": [("2.2", "myone", "The Visa share of MyOne debit"), ("1.5", "cbk", "Commerzbank and mBank cards"), ("3.1", "fraud", "Scam scores beside HVB's platform"),
               ("2.6", "baacq", "Gateway and tokens for Bank Austria"), ("2.8", "gps", "Mastercard Move for cross-border"), ("3.2", "aiagents", "Agent Pay"),
               ("2.9", "qivalis", "Stablecoin links to Qivalis")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across UniCredit's map",
    "title": "Mastercard's bank in 12 markets, with Commerzbank still to choose",
    "lead": "Since May 2023 one agreement has made Mastercard the card partner for 13 UniCredit banks and about 20 million cards. HVB is replacing Visa Debit and Maestro girocards with Mastercard debit, and Italy's credit and prepaid cards and Priceless run on Mastercard. Visa keeps part of Italian MyOne debit, girocard stays in Germany, and acquiring, instant payments and the Qivalis stablecoin are not Mastercard's. Commerzbank, at 49.65%, is the next big choice. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (2Q26 results, 23 July 2026; 2025 Annual Report) or from UniCredit, HVB and Mastercard pages. Network splits by country, Wero membership, Commerzbank's networks and the end date of the 2023 deal are not public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Group deal", "Mastercard", "13 banks, 12 markets, about 20m cards, May 2023"],
        ["Germany debit", "Mastercard", "Replacing Visa Debit and Maestro; girocard stays"],
        ["Italy debit", "Mastercard or Visa", "MyOne; split not disclosed"],
        ["Italy credit & prepaid", "Mastercard", "Flexia Gold, Ferrari, Genius Pay"],
        ["Rewards", "Priceless", "Mastercard's own"],
        ["Acquiring", "In-house and Nexi", "All networks accepted"],
        ["Stablecoin", "Qivalis", "Bank consortium, first issue 2H26"],
        ["Commerzbank", "Not public ⚠", "49.65% position; approvals pending"],
    ],
    "sides": {
        "neo": {"dir": "Issuing for 13 banks under one deal, HVB's new debit card, Italian credit and prepaid cards, Priceless and Travel Rewards, Click to Pay and the Touch Card.",
                "deals": "What it does not do: girocard, Visa's share of MyOne, acquiring processing, instant and account-to-account payments, fraud models, AI or the stablecoin."},
        "snb": {"dir": "Visa in part of Italian debit and legacy HVB cards, girocard and BANCOMAT at home, Nexi processing, in-house acquiring, SEPA instant, Qivalis and the digital euro.",
                "deals": "Where they meet: the Commerzbank and mBank card estate, if UniCredit takes control."},
    },
    "tl": [
        ["Feb 2018", "buddybank opens, Mastercard processing ⚠"],
        ["May 2023", "Mastercard deal for 13 banks"],
        ["Feb 2025", "Touch Card in Austria"],
        ["Jul 2025", "Bank Austria's own acquiring"],
        ["Sep 2025", "card complete sold; Qivalis formed"],
        ["Feb 2026", "UniCredit Unlimited"],
        ["Mar 2026", "Commerzbank exchange offer"],
        ["Oct 2026", "Clearances incl. EURO Kartensysteme"],
    ],
    "l": {
        "U": {"d": 1, "s": "Most cardholders carry Mastercard.",
              "gap": "Credit, prepaid and German debit are Mastercard; some Italian debit is Visa and girocard stays in Germany.",
              "neo": "Cardholders in 12 markets.", "snb": "Visa MyOne holders, girocard users, investors and corporates."},
        "L5": {"d": 0, "s": "The front doors are UniCredit's.", "gap": "buddy, the apps, branches and ATMs are the group's; buddybank used Mastercard processing at launch ⚠.",
               "neo": "None.", "snb": "buddy, apps, branches, ATMs."},
        "L4": {"d": 1, "s": "Accounts come with Mastercard cards.", "gap": "HVB and Italian accounts carry Mastercard debit, partly Visa in Italy; lending, CIB and funds have no network role.",
               "neo": "Card-linked current accounts.", "snb": "CIB, trade finance, onemarkets, insurance."},
        "L3": {"d": 1, "s": "Priceless is Mastercard's; fraud and AI are not.", "gap": "Priceless and Travel Rewards run on Mastercard; HVB's fraud platform and the AI agents are UniCredit's.",
               "neo": "Priceless, Travel Rewards.", "snb": "Fraud platform, AI agents, valyou."},
        "L2": {"d": 1, "s": "Cards mostly Mastercard; the rest is not.", "gap": "Issuing is Mastercard by group deal; acquiring, instant, A2A and the stablecoin are elsewhere.",
               "neo": "Group deal, HVB debit, Italian credit and prepaid, Touch Card.", "snb": "girocard, Visa MyOne, Nexi, SEPA instant, Qivalis."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's; Commerzbank's networks are unknown.",
               "neo": "None.", "snb": "Capital, banks, cloud, strategy."},
    },
    "t": area_lens(LAYERS),
}
