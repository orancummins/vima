"""Royal Bank of Canada's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from rbc_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Canada's biggest bank as five discs that stack into one platform, from C$2.5 trillion of assets at the bottom to the "
       "RBC Mobile app, branches and partners at the top. Click the stack to open it. Choose who you are and what you want to do, "
       "and the areas that deliver it light up across the layers, joined in the order they act. Switch to the Mastercard "
       "lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("card", "Cardholders & Avion members", "gift"),
    ("new", "Newcomers to Canada", "plane"),
    ("us", "U.S. & Caribbean clients", "flag"),
    ("inv", "Investors & savers", "trending-up"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Commercial & corporate clients", "factory"),
]
USERS_DESC = ("Seven kinds of client, more than 19 million in all: everyday customers in Canada, cardholders and Avion Rewards "
              "members, newcomers, clients of RBC Bank, City National and the Caribbean bank, investors and savers, small "
              "businesses, and the commercial and corporate clients that Commercial Banking, Global Transaction Banking and "
              "Capital Markets serve.")

WHO = {"con": "An RBC customer", "card": "A cardholder", "new": "A newcomer", "us": "A U.S. or Caribbean client",
       "inv": "An investor", "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day in Canada",
     "why": "The everyday loop: an account, Interac debit and e-Transfer, the app and card locks.",
     "steps": [("4.1", "personal", "Open an RBC account"), ("2.4", "interacdebit", "Pay with Interac debit"),
               ("2.5", "etransfer", "Send an Interac e-Transfer"), ("5.1", "app", "Run it in the RBC Mobile app"),
               ("3.5", "controls", "Lock a lost card")]},
    {"id": "rewards", "who": "card", "name": "Earn and travel with Avion",
     "why": "The Avion Visa line, linked partners and the new travel platform.",
     "steps": [("2.1", "avion", "Take an Avion Visa Infinite"), ("3.1", "avionrewards", "Earn in Avion Rewards"),
               ("3.2", "linked", "Link the card to Canadian Tire or Petro-Canada"), ("3.1", "aviontravel", "Book any flight with points")]},
    {"id": "westjet", "who": "card", "name": "Fly WestJet on a Mastercard",
     "why": "The WestJet RBC Mastercard cards, refreshed in November 2025, with DashPass and wallets.",
     "steps": [("2.2", "westjet", "Take a WestJet RBC World Elite Mastercard"), ("3.3", "wallets", "Add it to Apple Pay"),
               ("3.2", "doordash", "Get 12 months of DashPass"), ("5.3", "partners", "Fly and earn with WestJet")]},
    {"id": "newcomer", "who": "new", "name": "Arrive in Canada",
     "why": "Open before landing, get credit without a history, and send money home.",
     "steps": [("5.1", "newcomer", "Open an account before arriving"), ("2.1", "ion", "Take a first ION Visa"),
               ("3.5", "aicredit", "Get credit with AI underwriting"), ("2.5", "imt", "Send money abroad with no RBC fee")]},
    {"id": "us", "who": "us", "name": "Bank across the border",
     "why": "RBC Bank and City National for Canadians and businesses in the US, on Visa cards.",
     "steps": [("2.6", "uscards", "Take an RBC Bank U.S. Visa"), ("4.3", "citynational", "Bank with City National"),
               ("2.5", "imt", "Move US dollars abroad")]},
    {"id": "invest", "who": "inv", "name": "Plan, invest and insure",
     "why": "MyAdvisor, RBC Wealth Management and RBC Insurance.",
     "steps": [("5.1", "myadvisor", "Make a plan in MyAdvisor"), ("4.3", "wealth", "Invest with Dominion Securities or Direct Investing"),
               ("4.3", "insurance", "Insure with RBC Insurance")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business card, Moneris for acceptance, e-Transfer for Business and PayEdge.",
     "steps": [("2.3", "westjetbiz", "Take a WestJet World Elite Mastercard for Business"), ("2.8", "moneris", "Take cards through Moneris"),
               ("2.5", "etbiz", "Collect by e-Transfer for Business"), ("4.2", "payedge", "Pay suppliers through PayEdge")]},
    {"id": "corp", "who": "corp", "name": "Run treasury with GTB",
     "why": "Global Transaction Banking, commercial Visa cards and the CAD deposit token.",
     "steps": [("4.2", "gtb", "Bank with Global Transaction Banking"), ("2.3", "commercial", "Pay with a Commercial Visa"),
               ("4.4", "capmkts", "Work with RBC Capital Markets"), ("2.7", "cadtoken", "Settle in a CAD deposit token")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The WestJet cards, the cash back line, two business cards, DashPass on World Elite, and acceptance through Moneris.",
     "steps": [("2.2", "westjet", "WestJet RBC Mastercard cards"), ("2.2", "cashback", "RBC Cash Back Mastercard cards"),
               ("2.3", "westjetbiz", "WestJet World Elite Mastercard for Business"), ("2.3", "bizcards", "Business Cash Back Mastercard"),
               ("3.2", "doordash", "DashPass on the World Elite card"), ("2.8", "moneris", "Mastercard acceptance at Moneris")]},
    {"id": "mcnext", "who": "mc", "name": "Where offers, agents and transfers could land",
     "why": "Where RBC has needs and Mastercard is not yet in: offers inside Avion Rewards, agentic payments on its Mastercard cards, transfers abroad, open banking, the deposit token and acceptance after Moneris.",
     "steps": [("3.1", "avionrewards", "Card-linked offers inside Avion Rewards"), ("3.3", "wallets", "Agent Pay and Click to Pay on RBC's Mastercard cards"),
               ("2.5", "imt", "Mastercard Move for International Money Transfers"), ("5.1", "app", "Open finance as consumer-driven banking starts"),
               ("2.7", "cadtoken", "Multi-Token Network for the CAD deposit token"), ("2.8", "moneris", "Risk tools through Moneris's new owner")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Royal Bank of Canada's map",
    "title": "A Visa bank where Mastercard keeps WestJet and cash back",
    "lead": "Visa carries RBC's Avion flagship, the everyday ION cards, its grocery co-brands, every commercial card, Virtual Visa Debit and its US cards; Interac runs debit and e-Transfer. Mastercard keeps two durable programmes, the WestJet RBC cards and the Cash Back line, and gained a WestJet business card in August 2025. Most HSBC Canada Mastercard holders were moved to Visa in 2024 ⚠, and no joint product with Mastercard is public. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are RBC's own (Q3 2026 report, 27 August 2026; Annual Report 2025). Card networks come from RBC's card pages as at 17 October 2026. Mastercard's Canadian newsroom could not be reached, and the HSBC card mapping rests on secondary sources ⚠.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Personal credit", "Visa, plus Mastercard co-brands", "About 11 Visa and 4 Mastercard cards on offer"],
        ["Travel flagship", "Visa", "Avion Visa Infinite and Privilege"],
        ["Co-brands", "Mastercard and Visa", "WestJet on Mastercard; Metro and Pattison on Visa"],
        ["Business & commercial", "Visa, two Mastercards", "WestJet Business and Business Cash Back"],
        ["Debit", "Interac, Virtual Visa Debit", "No Debit Mastercard found"],
        ["US cards", "Visa", "RBC Bank and City National"],
        ["HSBC Canada cards", "Mastercard to mostly Visa ⚠", "Converted March–April 2024"],
        ["Acquiring", "Moneris", "For sale, about C$2bn"],
    ],
    "sides": {
        "neo": {"dir": "The WestJet RBC personal and business cards, the Cash Back Mastercard line, DashPass on the World Elite card, and acceptance through Moneris.",
                "deals": "What it does not do: Avion, the everyday and grocery cards, commercial cards, debit, instalments, transfers abroad, or RBC's own tokens and loyalty."},
        "snb": {"dir": "Visa for Avion, ION, co-brands, commercial cards, Virtual Visa Debit, instalments and US cards; Interac for debit and e-Transfer; RBC's own Avion Rewards, wallet and AI.",
                "deals": "Where they meet: Avion Rewards and the linked-card partners, which earn on Visa, Mastercard and Interac cards alike."},
    },
    "tl": [
        ["2009", "WestJet RBC MasterCard launched ⚠"],
        ["Sep 2012", "RBC Shoppers Optimum MasterCard and portfolio"],
        ["Jan 2014", "RBC Wallet with Interac and Visa"],
        ["Sep 2022", "Avion Rewards; ION Visa cards"],
        ["Nov 2022", "Installments enabled by Visa"],
        ["Mar 2024", "HSBC Canada's Mastercard cards move mostly to Visa ⚠"],
        ["Feb 2025", "More Rewards RBC Visa"],
        ["Aug 2025", "WestJet World Elite Mastercard for Business"],
        ["Nov 2025", "WestJet RBC Mastercard refresh"],
        ["Apr 2026", "McKay and Miebach at Mastercard's forum ⚠"],
        ["Aug 2026", "Moneris to be sold"],
        ["Sep 2026", "CAD tokenised deposit explored"],
    ],
    "l": {
        "U": {"d": 1, "s": "Most cardholders carry Visa; WestJet and cash back holders carry Mastercard.",
              "gap": "Avion, ION, commercial and US cardholders carry Visa; debit users carry Interac.",
              "neo": "WestJet and cash back cardholders, some small businesses.", "snb": "Avion and ION holders, debit users, US clients, investors."},
        "L5": {"d": 1, "s": "The front doors are RBC's; WestJet is a Mastercard partner.", "gap": "App, MyAdvisor, branches and newcomer onboarding have no network role; WestJet is the Mastercard partnership.",
               "neo": "WestJet.", "snb": "App, branches, MyAdvisor, Live Nation, IKEA, RBCx."},
        "L4": {"d": 1, "s": "Personal Banking's cards are partly Mastercard; the rest has no network role.", "gap": "Personal Banking's C$196.6bn of card spend is mostly on Visa ⚠; GTB, wealth, insurance and capital markets do not use the networks.",
               "neo": "WestJet and cash back cards in Personal Banking.", "snb": "Avion and commercial Visa, GTB, wealth, City National Visa."},
        "L3": {"d": 1, "s": "Loyalty, tokens and AI are RBC's own; they serve Mastercard cards too.", "gap": "Avion Rewards, linked offers, RBC Wallet, card locks and AI credit are RBC-built; instalments are Visa's.",
               "neo": "Linked offers and DashPass on Mastercard cards; Apple Pay.", "snb": "Avion Rewards, Visa Installments, PayPlan, RBC Wallet, AI."},
        "L2": {"d": 1, "s": "WestJet and cash back on Mastercard; Visa and Interac carry the rest.", "gap": "Mastercard has the WestJet and cash back cards and two business cards; Visa has Avion, ION, co-brands, commercial, Virtual Visa Debit and US cards; Interac has debit and e-Transfer.",
               "neo": "WestJet personal and business, Cash Back cards, Moneris acceptance.", "snb": "Visa credit and commercial, Interac, transfers abroad, deposit token."},
        "L1": {"d": 0, "s": "RBC's own foundation.", "gap": "Nothing in the foundation is Mastercard's; the HSBC integration moved Mastercard cards to Visa ⚠.", "neo": "None.", "snb": "Capital, charter, AI, strategy, HSBC Canada."},
    },
    "t": area_lens(LAYERS),
}
