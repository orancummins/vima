"""BNP Paribas' kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bnpparibas_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A bank built on France, Belgium, Italy and Luxembourg as five discs that stack into one platform, from €939 billion of loans "
       "at the bottom to Mes Comptes, Easy Banking, branches and tobacconists at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in "
       "the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("borrower", "Credit & instalment customers", "hand-coins"),
    ("driver", "Drivers & fleets", "target"),
    ("saver", "Savers & investors", "coins"),
    ("sme", "Professionals & small businesses", "briefcase"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Six kinds of customer: everyday customers in four home markets and at Nickel, 25 million consumer-credit "
              "and instalment customers, drivers and fleets, savers and investors, professionals and small businesses, "
              "and the corporates and institutions CIB serves.")

WHO = {"con": "A BNP Paribas customer", "borrower": "A borrower", "driver": "A driver", "saver": "A saver",
       "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day in France",
     "why": "The everyday loop at BNP Paribas France: an account, a CB and Visa card, Mes Comptes, Wero and screening.",
     "steps": [("4.3", "retail", "Open an account"), ("2.1", "frcards", "Pay with a CB and Visa card"), ("5.1", "apps", "Run it in Mes Comptes"),
               ("2.6", "wero", "Pay friends and shops with Wero"), ("3.1", "screening", "Protected by screening")]},
    {"id": "belgium", "who": "con", "name": "Bank day to day in Belgium",
     "why": "BNP Paribas Fortis: Bancontact and Visa Debit, Easy Banking, Wero and Samy.",
     "steps": [("2.2", "fortisdebit", "Pay with Bancontact and Visa Debit"), ("5.1", "apps", "Run it in Easy Banking"),
               ("2.6", "wero", "Shop online with Wero"), ("3.2", "assistants", "Ask Samy")]},
    {"id": "nickel", "who": "con", "name": "Open an account at a tobacconist",
     "why": "Nickel: an account and a Mastercard in minutes, at more than 13,000 points of sale.",
     "steps": [("5.2", "branches", "Walk into a tobacconist"), ("2.5", "nickelcard", "Get a Nickel Mastercard"),
               ("5.3", "wallets", "Add it to Apple Pay or Google Pay"), ("2.6", "wero", "Send money with Wero")]},
    {"id": "borrow", "who": "borrower", "name": "Borrow or pay in instalments",
     "why": "Cetelem, Consors Finanz and Floa, mostly on Mastercard, with Cardif protection.",
     "steps": [("5.3", "partners", "Apply at a retailer"), ("4.1", "pf", "Borrow from Personal Finance"), ("2.5", "cpay", "Carry a Cpay Mastercard"),
               ("4.1", "floabnpl", "Split a purchase with Floa"), ("3.3", "protection", "Insure the repayments")]},
    {"id": "drive", "who": "driver", "name": "Finance or lease a car",
     "why": "Personal Finance's car-maker partners and Arval's 1.9 million vehicles.",
     "steps": [("4.1", "pf", "Finance through Stellantis or Chery"), ("4.2", "arval", "Lease with Arval"), ("3.3", "protection", "Add Cardif warranty cover")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Nickel Pro, card acceptance through Axepta, Wero for merchants and instant payments.",
     "steps": [("4.3", "nickelpro", "Open a Nickel Compte Pro"), ("2.7", "axepta", "Take payments with Axepta"),
               ("2.6", "wero", "Accept Wero"), ("2.6", "instant", "Get paid instantly")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Europe's leading cash-management franchise, Kantox and tokenised securities.",
     "steps": [("4.4", "cib", "Bank with CIB"), ("4.4", "cashmgmt", "Run cash and FX with Kantox"), ("2.8", "dtc", "Settle tokenised securities")]},
    {"id": "save", "who": "saver", "name": "Save and invest",
     "why": "BNP Paribas Asset Management, Cardif and Consorsbank.",
     "steps": [("4.5", "wealth", "Invest with BNP Paribas"), ("4.5", "cardif", "Save with Cardif"), ("5.1", "apps", "See it in the app")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Nickel, Cpay, Consors Finanz and Floa, BNL, Bank Polska with Priceless, and Estreem's processing.",
     "steps": [("2.5", "nickelcard", "Nickel on Mastercard"), ("2.5", "cpay", "Cpay"), ("2.5", "floacard", "Floa cards"),
               ("2.3", "bnlmc", "BNL debit and credit"), ("3.3", "priceless", "Priceless in Poland"), ("2.7", "estreem", "Processed by Estreem")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, Estreem and instalments could land",
     "why": "Where BNP Paribas has needs and Mastercard is not yet in: the group's agentic ambition, Estreem's new platform, fraud on instant payments, instalments on Mastercard credentials, Nickel Pro, Arval's fleet and cash management.",
     "steps": [("1.4", "ai", "Agent Pay for the agentic era"), ("2.7", "estreem", "Tokens and fraud tools in Estreem"), ("2.6", "instant", "Fraud scores on instant payments"),
               ("4.1", "floabnpl", "Instalments on Mastercard credentials"), ("4.3", "nickelpro", "Business debit for Nickel Pro"),
               ("4.2", "arval", "Fleet and fuel cards"), ("4.4", "cashmgmt", "Move and virtual cards for treasury")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across BNP Paribas' map",
    "title": "Mastercard on the challengers, Visa and domestic schemes at the home banks",
    "lead": "BNP Paribas France's cards are Cartes Bancaires and Visa, and its last Mastercard card went in December 2025; Fortis debit is Bancontact and Visa. Mastercard carries Nickel, Cpay, Consors Finanz and Floa, BNL in Italy, most of Bank Polska and BGL's premium credit. Meanwhile the group co-owns Wero, which reached every French customer for online shopping in September 2026. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (2Q26 results, 23 July 2026) or from BNP Paribas brands and press. The group and Mastercard newsrooms were blocked; Cpay rests on a search snippet, and Fortis credit, Hello bank! and commercial-card networks were not verified.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["France", "CB and Visa", "Mastercard Cirrus dropped December 2025"],
        ["Belgium", "Bancontact and Visa", "Visa Debit since 2021"],
        ["Italy", "Mastercard", "BNL debit and credit; Amex alongside"],
        ["Poland", "Mostly Mastercard", "Priceless on debit and credit"],
        ["Nickel", "Mastercard", "4.94 million accounts"],
        ["Consumer credit", "Mastercard", "Cpay ⚠, Consors Finanz, Floa"],
        ["Processing", "Estreem", "Visa, Mastercard and CB"],
        ["Wallet", "Wero", "57 million users"],
    ],
    "sides": {
        "neo": {"dir": "Nickel, Cpay, Consors Finanz and Floa, BNL, Bank Polska and Priceless, BGL premium credit, and Estreem's processing of Mastercard.",
                "deals": "What it does not do: French and Belgian debit, Wero, Floa's own credit, AI or the euro stablecoin."},
        "snb": {"dir": "Cartes Bancaires and Visa in France, Bancontact and Visa in Belgium, Wero, the group's own AI and screening, and a euro stablecoin.",
                "deals": "Where they meet: Estreem, which processes every scheme."},
    },
    "tl": [
        ["Feb 2014", "Nickel launches with a Mastercard"],
        ["Mar 2019", "Cetelem Cpay Mastercard ⚠"],
        ["Sep 2021", "Fortis moves from Maestro to Visa Debit"],
        ["Feb 2025", "Estreem joint venture with BPCE"],
        ["Apr 2025", "Mastercard launches Agent Pay"],
        ["Dec 2025", "Mastercard Cirrus card dropped in France"],
        ["Feb 2026", "Wero in Fortis' Easy Banking"],
        ["Sep 2026", "Wero e-commerce for all French customers"],
        ["Feb 2027", "2027–30 plan due"],
    ],
    "l": {
        "U": {"d": 1, "s": "Challenger and credit customers carry Mastercard.",
              "gap": "Nickel, Personal Finance, Floa, BNL and Polish customers carry Mastercard; French and Belgian customers carry Visa.",
              "neo": "Nickel, Cpay, Consors Finanz, Floa, BNL and Bank Polska cardholders.", "snb": "BNP Paribas France and Fortis customers, savers, corporates."},
        "L5": {"d": 0, "s": "The front doors are the group's.", "gap": "Apps, branches and partners are BNP Paribas'; the wallets' token service is not stated.", "neo": "None in public view.", "snb": "Apps, Hello bank!, branches, partners."},
        "L4": {"d": 1, "s": "Mastercard inside consumer credit and Nickel.", "gap": "Personal Finance and Nickel Pro carry Mastercard; retail banking at home is Visa; Arval, CIB and wealth have no network role in view.",
               "neo": "Cpay, Consors Finanz, Nickel Pro ⚠.", "snb": "Floa credit, Arval, CIB, wealth."},
        "L3": {"d": 1, "s": "Priceless and card benefits; the rest is the group's.", "gap": "Priceless in Poland and BGL's parcel cover are Mastercard's; screening and assistants are the group's own.",
               "neo": "Priceless, Assurance retour colis.", "snb": "Screening, Samy, Eva, Cardif."},
        "L2": {"d": 1, "s": "Mastercard on the challengers; Visa and CB at home; Wero rising.", "gap": "Mastercard carries Nickel, Personal Finance, Floa, BNL and Poland; Visa and domestic schemes hold France and Belgium; Wero and tokens are outside the card schemes.",
               "neo": "Nickel, Cpay, Consors, Floa, BNL, Poland, Estreem.", "snb": "CB and Visa, Bancontact and Visa, Wero, stablecoin."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, heritage, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
