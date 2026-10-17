"""TD Bank Group's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from tdbank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("TD Canada Trust and TD Bank in the US as five discs that stack into one platform, from C$2.1 trillion of assets "
       "and a US asset cap at the bottom to the TD app, branches, stores and partners at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in the "
       "order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers in Canada", "user-round"),
    ("card", "Cardholders & rewards members", "gift"),
    ("us", "U.S. customers", "flag"),
    ("inv", "Investors & policyholders", "trending-up"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Commercial & corporate clients", "factory"),
]
USERS_DESC = ("Six kinds of client, about 28 million in all: everyday customers in Canada, cardholders on TD, MBNA and partner "
              "cards, about 10 million clients in the US, investors and insurance customers, small businesses, and the "
              "commercial and corporate clients that TD Securities and TD Cowen serve.")

WHO = {"con": "A TD Canada Trust customer", "card": "A cardholder", "us": "A TD Bank customer in the US", "inv": "An investor",
       "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day in Canada",
     "why": "The everyday loop: an account, the Access Card with Interac and Visa Debit, e-Transfer, the app and MySpend.",
     "steps": [("4.1", "cpb", "Open a chequing account"), ("2.3", "accesscard", "Pay with the Access Card"),
               ("2.7", "etransfer", "Send an Interac e-Transfer"), ("5.1", "app", "Run it in the TD app"),
               ("3.3", "myspend", "Track spending in MySpend")]},
    {"id": "travel", "who": "card", "name": "Fly on points",
     "why": "TD's Aeroplan Visa cards and TD Rewards.",
     "steps": [("2.1", "aeroplan", "Take a TD Aeroplan Visa"), ("3.4", "tdrewards", "Earn Aeroplan points"),
               ("5.3", "partners", "Redeem with Air Canada")]},
    {"id": "mbna", "who": "card", "name": "Shop on an MBNA card",
     "why": "MBNA's Mastercard range and the Amazon.ca Rewards Mastercard.",
     "steps": [("2.2", "mbna", "Take an MBNA Mastercard"), ("2.2", "amazonca", "Or the Amazon.ca Rewards Mastercard"),
               ("3.4", "partnerloyalty", "Earn back at Amazon.ca")]},
    {"id": "us", "who": "us", "name": "Bank with TD in the US",
     "why": "A checking account, Visa debit, Zelle and a TD Visa credit card, in the app or a store.",
     "steps": [("4.3", "usbanking", "Open a TD Bank account"), ("2.4", "usdebit", "Pay with Visa debit"),
               ("2.7", "zelle", "Send money with Zelle"), ("2.4", "uscredit", "Add a TD Visa credit card"),
               ("5.2", "branches", "Visit a store")]},
    {"id": "retail", "who": "card", "name": "Shop at Target or Nordstrom",
     "why": "The partner cards TD Bank USA issues.",
     "steps": [("2.5", "target", "Take a Target Mastercard"), ("2.5", "nordstrom", "Or a Nordstrom card"),
               ("3.4", "partnerloyalty", "Get Target Circle and Nordstrom perks")]},
    {"id": "invest", "who": "inv", "name": "Invest and insure",
     "why": "TD Direct Investing, TD Wealth and TD Insurance, including home insurance on REALTOR.ca.",
     "steps": [("4.4", "wealth", "Invest with TD Direct Investing or TD Wealth"), ("4.4", "insurance", "Insure the home through REALTOR.ca"),
               ("5.1", "app", "See it in the app")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account, a TD business Visa, card acceptance on Clover and e-Transfer.",
     "steps": [("4.2", "commercial", "Open a business account"), ("2.1", "bizvisa", "Take a TD business Visa"),
               ("2.6", "tdms", "Take cards with TD Merchant Solutions"), ("2.6", "fiservdeal", "Run it on Fiserv's Clover"),
               ("2.7", "etransfer", "Collect by e-Transfer")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "TD Securities and TD Cowen, and TD's work on tokenised deposits and stablecoins.",
     "steps": [("4.5", "wholesale", "Work with TD Securities"), ("2.8", "cadtoken", "Settle in a CAD tokenised deposit"),
               ("2.8", "stablecoin", "Use the bank USD stablecoin")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The cards TD bought or issues for partners: MBNA and Amazon.ca in Canada, Target in the US, plus Maestro PIN debit ⚠ and acceptance.",
     "steps": [("2.2", "mbna", "MBNA Mastercard cards"), ("2.2", "amazonca", "Amazon.ca Rewards Mastercard"),
               ("2.5", "target", "Target Mastercard"), ("2.4", "usdebit", "US PIN debit on Maestro ⚠"),
               ("2.6", "tdms", "Acceptance at TD's merchants")]},
    {"id": "mcnext", "who": "mc", "name": "Where AML tools, agents and tokens could land",
     "why": "Where TD has needs and Mastercard is not yet in: AML and scam intelligence for a bank under a cap, issuer and offers tools for MBNA and Target, Agent Pay for TD's AI, cross-border payouts, deposit tokens, and the Visa-held TD card and commercial lines.",
     "steps": [("3.1", "monitoring", "AML and scam intelligence"), ("3.4", "partnerloyalty", "Card-linked offers for MBNA and Target"),
               ("3.2", "clari", "Agent Pay for TD's assistant"), ("2.7", "globaltransfer", "Mastercard Move for Global Transfer"),
               ("2.8", "cadtoken", "Multi-Token Network for deposit tokens"), ("4.2", "commercial", "Commercial and virtual cards")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across TD Bank Group's map",
    "title": "A Visa bank whose Mastercard business came with what it bought: MBNA and Target",
    "lead": "TD-branded credit, debit, business and gift cards run on Visa in both Canada and the US, Aeroplan included, and Interac carries Canadian in-person debit. Mastercard has the cards TD bought or issues for partners: MBNA and the Amazon.ca Rewards Mastercard in Canada, and the Target Mastercard in the US. Since 2016 TD Bank's US PIN debit has also run on Maestro ⚠. Meanwhile the US bank is under a US$434 billion asset cap and AML remediation, and TD is building tokenised deposits with other banks. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are TD's own (Q3 2026 results, 27 August 2026; fiscal 2025, 4 December 2025). Networks come from TD's, MBNA's and Target's card pages, read on 17 October 2026. sec.gov filings could not be read. No Visa or Mastercard contract terms are public, and the current Maestro routing and the date Target moved to Mastercard are unconfirmed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["TD credit (Canada)", "Visa", "Aeroplan, First Class, Cash Back, business"],
        ["MBNA (Canada)", "Mastercard", "True Line, Rewards, Amazon.ca; some Visa ⚠"],
        ["Canadian debit", "Interac + Visa Debit", "TD Access Card"],
        ["TD Bank (US) cards", "Visa", "Credit, debit, business, gift"],
        ["US PIN debit", "Maestro", "Since 2016 ⚠ current status"],
        ["US partner cards", "Target on Mastercard", "Nordstrom on Visa"],
        ["Acceptance", "TD Merchant Solutions", "Moving onto Fiserv's Clover"],
        ["Digital money", "Bank-led", "CAD tokens, USD stablecoin, Agorá"],
    ],
    "sides": {
        "neo": {"dir": "MBNA and Amazon.ca cards in Canada, the Target Mastercard in the US, Maestro PIN debit ⚠, and acceptance at TD's merchants.",
                "deals": "What it does not do: TD-branded credit, debit or business cards, Aeroplan, Nordstrom, transfers, AML tools, AI or tokenised money."},
        "snb": {"dir": "Visa for TD's own cards and Aeroplan, Interac for debit, e-Transfer and identity, Zelle in the US, Fiserv for merchant technology, and TD's own AML, AI and deposit tokens.",
                "deals": "Where they meet: TD Bank's US debit, which carries Visa but whose PIN payments ran on Maestro from 2016 ⚠."},
    },
    "tl": [
        ["Dec 2011", "MBNA Canada, the largest Mastercard issuer, joins TD"],
        ["Mar 2013", "Target card portfolio (then Visa) joins TD"],
        ["Jan 2014", "First TD Aeroplan Visa cards"],
        ["Jul 2015", "Maestro chosen for US PIN debit, from 2016"],
        ["Oct 2024", "US guilty plea; US$434bn asset cap"],
        ["Jul 2025", "Fiserv deal for TD Merchant Solutions"],
        ["Sep 2025", "Investor Day: ROE 16% by 2029"],
        ["Feb 2026", "Nordstrom servicing moves to TD"],
        ["Sep 2026", "Renu Gupta takes payments; USD stablecoin consortium"],
        ["Sep 2026", "CAD tokenised deposits with five banks"],
    ],
    "l": {
        "U": {"d": 1, "s": "MBNA, Amazon.ca and Target cardholders carry Mastercard; most TD clients carry Visa.",
              "gap": "TD-branded cardholders in both countries carry Visa, and Canadian debit users carry Interac; MBNA, Amazon.ca and Target cardholders carry Mastercard.",
              "neo": "MBNA, Amazon.ca and Target cardholders.", "snb": "TD Visa and Aeroplan cardholders, debit users, investors."},
        "L5": {"d": 1, "s": "The front doors are TD's; two partners issue on Mastercard.", "gap": "App, branches and stores are TD's; Amazon.ca and Target cards are Mastercard, while Aeroplan is Visa.",
               "neo": "Amazon.ca and Target partner cards.", "snb": "App, branches, stores, Aeroplan."},
        "L4": {"d": 0, "s": "The business lines carry Visa and Interac cards.", "gap": "Accounts come with Interac and Visa debit in Canada and Visa in the US; wealth, insurance and wholesale have no network role.",
               "neo": "None.", "snb": "Accounts, auto finance, US Banking, wealth, insurance, wholesale."},
        "L3": {"d": 1, "s": "Partner loyalty rides on Mastercard co-brands; the rest is TD's.", "gap": "Monitoring, AI, MySpend and TD Rewards are TD's own; Amazon.ca and Target rewards sit on Mastercard cards.",
               "neo": "Amazon.ca and Target rewards.", "snb": "AML monitoring, TD Clari, MySpend, Interac verification, TD Rewards."},
        "L2": {"d": 1, "s": "MBNA, Amazon.ca, Target and Maestro on Mastercard; everything TD-branded on Visa.", "gap": "Visa has TD's own credit, debit, business and gift cards in both countries; Mastercard has MBNA, Amazon.ca, Target and US PIN debit ⚠.",
               "neo": "MBNA, Amazon.ca, Target, Maestro PIN debit ⚠, acceptance.", "snb": "TD Visa cards, Aeroplan, Interac, Zelle, Fiserv, tokenised money."},
        "L1": {"d": 0, "s": "TD's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, asset cap, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
