"""Česká spořitelna's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from ceskasporitelna_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The largest Czech bank by clients as five discs that stack into one platform, from 4.6 million clients and "
       "CZK 1,259 billion of loans at the bottom to George, George Business and 332 branches at the top. Click the stack "
       "to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday clients", "user-round"),
    ("young", "Children & students", "graduation-cap"),
    ("home", "Homebuyers", "house"),
    ("saver", "Savers & investors", "coins"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates & public sector", "factory"),
]
USERS_DESC = ("Six kinds of client, 4.6 million in all: everyday clients, children and students, homebuyers, savers and "
              "investors, small businesses, and the corporates and public bodies the bank lends to.")

WHO = {"con": "A ČS client", "young": "A student", "home": "A homebuyer", "saver": "A saver", "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Visa debit card, George, Hey George and security checks.",
     "steps": [("4.2", "accounts", "Open Účet Plus"), ("2.1", "debit", "Pay with a Visa debit card"), ("5.1", "george", "Run it in George"),
               ("3.3", "heygeorge", "Ask Hey George"), ("3.1", "security", "Approve payments in George")]},
    {"id": "travel", "who": "con", "name": "Pay by phone and abroad",
     "why": "Wallets, virtual cards and a ten-currency account.",
     "steps": [("2.4", "wallets", "Add the card to Apple Pay or Google Pay"), ("2.4", "virtual", "Shop online with a virtual card"),
               ("2.1", "multicurrency", "Pay abroad in the local currency"), ("3.4", "moneyback", "Collect Moneyback")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card or loan",
     "why": "A Visa credit card with cashback, and consumer loans.",
     "steps": [("2.2", "credit", "Take a credit card"), ("4.2", "consumer", "Or take a loan in George"), ("3.4", "levelup", "Earn Level Up points")]},
    {"id": "young", "who": "young", "name": "Start out with money",
     "why": "Children's and students' accounts, round-up saving and financial education.",
     "steps": [("4.2", "accounts", "Open a student account"), ("5.1", "george", "Use George"), ("3.4", "fithealth", "Save with every payment")]},
    {"id": "home", "who": "home", "name": "Buy or rent a home",
     "why": "28% of new Czech mortgages, building savings and affordable rental flats.",
     "steps": [("5.3", "branches", "Talk to a branch adviser"), ("4.1", "mortgages", "Take a mortgage"), ("4.3", "buildsav", "Save with building savings"),
               ("4.1", "housing", "Or rent an affordable flat")]},
    {"id": "save", "who": "saver", "name": "Save and invest",
     "why": "Pensions, funds and private banking.",
     "steps": [("4.3", "pensions", "Save for retirement"), ("4.4", "invest", "Invest in funds through George"), ("4.4", "private", "Move up to Private Banking")]},
    {"id": "idnt", "who": "con", "name": "Prove who you are online",
     "why": "Bank iD opens state and private services with the George login.",
     "steps": [("5.1", "george", "Log in with George"), ("3.2", "bankid", "Use Bank iD for taxes and prescriptions")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account, Visa business cards, George Business and card acceptance through Global Payments.",
     "steps": [("4.5", "sme", "Open a business account"), ("5.2", "georgebiz", "Move to George Business"),
               ("2.2", "corpcards", "Pay with a Visa business card"), ("2.5", "acquiring", "Take cards with Global Payments")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Acceptance at ČS merchants and ATMs, and the Banka roku award; the cards left in 2023.",
     "steps": [("2.5", "acquiring", "Mastercard accepted at Global Payments terminals"), ("2.5", "atms", "ČS ATMs take Mastercard"),
               ("1.3", "awards", "Mastercard Banka roku 2024 and 2025"), ("2.3", "switch", "Cards moved to Visa in 2023")]},
    {"id": "mcnext", "who": "mc", "name": "Where services beyond the card could land",
     "why": "Where ČS has needs that do not depend on the card network: open finance for George Business, identity and scam checks, merchant data and agents for Hey George, offers for Moneyback, and risk tools for its acquirer.",
     "steps": [("5.2", "georgebiz", "Open finance for George Business"), ("3.2", "bankid", "Identity and scam checks"),
               ("3.3", "heygeorge", "Merchant data and Agent Pay for Hey George"), ("3.4", "moneyback", "Merchant offers for Moneyback"),
               ("2.5", "acquiring", "Acquirer risk tools"), ("2.2", "credit", "A bid at the next card tender")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Česká spořitelna's map",
    "title": "A Visa-only bank that hands Mastercard its trophies",
    "lead": "Česká spořitelna has issued only Visa cards since the end of 2023, when it moved about 15% of its card clients off Mastercard and Maestro; Visa named it its top Czech issuer. Mastercard reaches ČS's clients only where they are paid, through Global Payments terminals and ČS's ATMs, and ČS has twice won the Mastercard Banka roku award. Its parent's Austrian bank is the opposite: Mastercard debit for everyone. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (Half-Year Report 2026) or from ČS, Visa, Global Payments and Czech press. ČS's card pages do not name the network; the Visa-only policy of April 2023 is the basis. Mastercard's Czech newsroom could not be read.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "About 4.3 million cards"],
        ["Credit", "Visa ⚠", "239,760 cards"],
        ["Switch", "Mastercard to Visa", "Apr–Nov 2023; 15% of card clients"],
        ["Wallets", "Apple, Google, Garmin", "On Visa cards"],
        ["Acceptance", "Global Payments", "JV since 2016; all schemes"],
        ["Award", "Mastercard Banka roku", "Won 2024 and 2025"],
        ["AI", "Hey George", "OpenAI GPT-4o, Dec 2024"],
    ],
    "sides": {
        "neo": {"dir": "Acceptance at Global Payments merchants and ČS ATMs, and the Banka roku award.",
                "deals": "What it does not do: any ČS card, wallet token, Click to Pay, rewards, AI or identity."},
        "snb": {"dir": "Visa on every debit, credit, Premier and corporate card, its tokens and Click to Pay; ČS's own George, Bank iD and Moneyback; OpenAI for Hey George.",
                "deals": "Where they meet: Global Payments' terminals, which take both."},
    },
    "tl": [
        ["Jun 2016", "Acquiring moves into the Global Payments JV"],
        ["Apr 2023", "Visa-only cards announced"],
        ["Apr 2023", "Visa names ČS its top Czech issuer"],
        ["Aug 2023", "Personal Mastercard and Maestro cards end"],
        ["Nov 2023", "Premier, Private Banking and corporate cards end"],
        ["Dec 2024", "Hey George on GPT-4o"],
        ["Nov 2025", "Mastercard Banka roku, second year running"],
        ["End-2026", "George Business migration due"],
    ],
    "l": {
        "U": {"d": 0, "s": "ČS clients carry Visa.",
              "gap": "Every ČS card has been Visa since November 2023; Mastercard meets ČS clients only as merchants.",
              "neo": "None as cardholders.", "snb": "All 4.5 million cardholders."},
        "L5": {"d": 0, "s": "The front doors are ČS's.", "gap": "George, George Business and branches are the bank's own.", "neo": "None.", "snb": "George, George Business, branches."},
        "L4": {"d": 0, "s": "The business lines carry Visa cards.", "gap": "Accounts and business banking come with Visa cards; mortgages, pensions and funds have no network role.",
               "neo": "None.", "snb": "Accounts, mortgages, pensions, funds, corporate lending."},
        "L3": {"d": 0, "s": "Services are ČS's own.", "gap": "Security, Bank iD, Hey George and Moneyback are ČS's or partners'; none is Mastercard's.",
               "neo": "None.", "snb": "George security, Bank iD, Hey George, Moneyback."},
        "L2": {"d": 1, "s": "Acceptance takes Mastercard; issuing is Visa.", "gap": "Visa has every card; Mastercard is accepted at Global Payments terminals and ČS ATMs.",
               "neo": "Acceptance, ATMs.", "snb": "Visa debit and credit, wallets, Click to Pay."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's; its name is on an award.", "neo": "None.", "snb": "Capital, Erste, heritage, technology."},
    },
    "t": area_lens(LAYERS),
}
