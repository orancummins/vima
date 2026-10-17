"""Banco Santander's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

SUB = ("The eurozone's most valuable bank as five discs that stack into one platform, from a €1.95 trillion balance sheet, "
       "nine core markets and the Gravity core at the bottom to One App, 6,496 branches and Openbank at the top. Click "
       "the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across "
       "the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("aff", "Select & private clients", "gem"),
    ("auto", "Car buyers", "target"),
    ("sme", "Small businesses", "briefcase"),
    ("merch", "Merchants", "store"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Seven kinds of customer, 182.5 million in all: everyday customers from Spain to Brazil, homebuyers, Select "
              "and private-banking clients, car buyers through Openbank, small businesses, Getnet's merchants and the "
              "corporates CIB serves.")

WHO = {
    "con": "A customer", "home": "A homebuyer", "aff": "A Select client", "auto": "A car buyer",
    "sme": "A small business", "merch": "A merchant", "corp": "A corporate treasurer",
}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop on One App and Gravity: a debit card, the phone wallet, Bizum and Pay Smarter.",
     "steps": [("5.1", "oneapp", "Open an account in One App"), ("2.1", "ukcards", "Pay with a Mastercard debit card"),
               ("2.2", "tokens", "Tap the phone"), ("2.4", "bizum", "Send money by Bizum"),
               ("3.3", "fraud", "Protected by fraud models")]},
    {"id": "agent", "who": "con", "name": "Let an AI agent buy for you",
     "why": "Santander was first in Europe: an agent pays with a Mastercard token, and Getnet accepts it.",
     "steps": [("3.1", "agentpay", "Authorise an agent with Agent Pay"), ("2.2", "tokens", "Pay with an agentic token"),
               ("2.3", "getnetagent", "Accepted through Getnet"), ("3.1", "visaagent", "Or on Visa, in the parallel pilot")]},
    {"id": "home", "who": "home", "name": "Buy a home in the UK",
     "why": "Third in UK current accounts and fourth in mortgages, now with TSB.",
     "steps": [("4.2", "ukretail", "Bank with Santander UK or TSB"), ("5.2", "branches", "See an adviser"),
               ("2.1", "ukcards", "Pay with Mastercard debit")]},
    {"id": "select", "who": "aff", "name": "Grow your wealth",
     "why": "Select for the affluent, private banking above it, and crypto at Openbank.",
     "steps": [("3.5", "select", "Join Select"), ("2.1", "groupcards", "Carry a Mastercard Black or Visa Infinite"),
               ("4.7", "wealth", "Invest with Private Banking"), ("4.7", "crypto", "Trade crypto at Openbank")]},
    {"id": "car", "who": "auto", "name": "Finance a car",
     "why": "Openbank's consumer finance in 26 countries and the US auto lender.",
     "steps": [("5.4", "partners", "Apply at the dealer or car maker"), ("4.5", "openbankeu", "Take a car loan or lease"),
               ("4.4", "us", "Or finance in the US")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account, growth analytics, card acceptance through Getnet, and Ebury for paying abroad.",
     "steps": [("4.1", "smegrowth", "Bank with Santander Growth"), ("2.3", "getnet", "Take cards with Getnet"),
               ("2.5", "ebury", "Pay suppliers abroad with Ebury"), ("3.4", "openbankpay", "Offer instalments")]},
    {"id": "merchant", "who": "merch", "name": "Accept payments across two continents",
     "why": "Getnet on one API across Latin America and Iberia, with account-to-account, agents and checkout lending.",
     "steps": [("2.3", "getnet", "Accept cards with Getnet"), ("2.4", "gplatforms", "Take account-to-account payments"),
               ("2.3", "getnetagent", "Accept AI-agent payments"), ("3.4", "openbankpay", "Add Openbank Pay at checkout"),
               ("3.3", "fraud", "Screen for fraud")]},
    {"id": "corp", "who": "corp", "name": "Run a company's money",
     "why": "CIB's transaction banking, lending and markets.",
     "steps": [("4.6", "cib", "Bank with CIB"), ("2.5", "ebury", "Hedge FX"), ("2.4", "gplatforms", "Collect by account-to-account")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "UK and Mexico debit, UK credit, top cards in Brazil, and the agentic firsts in Spain, Brazil and Getnet.",
     "steps": [("2.1", "ukcards", "UK debit and credit since 2018"), ("2.1", "mxcards", "Mexico debit and LikeU"),
               ("2.1", "groupcards", "Mastercard Black in Brazil"), ("3.1", "agentpay", "Europe's first agent payment"),
               ("2.3", "getnetagent", "Getnet on Agent Pay and Agent Pay for Machines")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, TSB and Webster could land",
     "why": "Where the group has needs and Mastercard is not yet in: agentic at scale, TSB's and Webster's cards, the UK renewal, cross-border payouts, tokens on Plard and account-to-account fraud.",
     "steps": [("3.1", "agentpay", "Agent Pay from pilot to product"), ("4.2", "ukretail", "TSB's cards and the UK renewal"),
               ("4.4", "us", "Webster's card portfolio"), ("2.5", "ebury", "Move for Ebury and Pay-in"),
               ("2.2", "plard", "Passkeys and tokens on Plard"), ("2.4", "bizum", "Fraud scores on account-to-account"),
               ("3.4", "openbankpay", "Installments next to Openbank Pay")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Santander's map",
    "title": "Debit in the UK and Mexico, first in agentic",
    "lead": "There is no group-wide network deal: Santander chooses country by country. Mastercard carries every Santander UK debit card (an eight-year deal from 2018) and its credit cards, Mexico's debit cards, and the Mastercard half of Brazil's top cards. It also has the group's agentic firsts: Europe's first live AI-agent payment, live Agent Pay at Santander Brasil, and Getnet as an Agent Pay acquirer. Visa runs parallel pilots in Latin America. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (Q2 2026 financial report, 22 July 2026) or come from Santander, Mastercard, Visa and press reports. The network split in Spain, Portugal, Chile and the US is not public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["UK debit", "Mastercard, since 2018", "Eight-year deal; more than 9 million cards; term ends around 2026–27"],
        ["Mexico debit", "Mastercard", "Touch Cards since 2023; LikeU credit on both networks"],
        ["Brazil", "Both networks", "Unique as Mastercard Black and Visa Infinite"],
        ["Agentic", "Mastercard first", "Europe's first live agent payment, 2 March 2026"],
        ["Visa", "Parallel pilots", "Five LatAm markets; Visa Destinations"],
        ["Acquiring", "Getnet", "€129 billion in H1 2026; Agent Pay partner"],
        ["Processing", "Plard, in-house", "500 million transactions a month"],
        ["BNPL", "Openbank Pay", "2.6 million customers"],
        ["New books", "TSB, Webster", "Networks in play"],
    ],
    "sides": {
        "neo": {"dir": "UK debit and credit, Mexico debit, half of Brazil's top cards, Agent Pay at the bank and at Getnet, and Agent Pay for Machines.",
                "deals": "What it does not do: processing (Plard), Bizum and account-to-account, Openbank Pay, fraud, cross-border, or any group-wide network deal."},
        "snb": {"dir": "Visa's parallel agentic pilot and Visa Destinations, Plard, Getnet Platforms, Bizum, Ebury, Openbank Pay and OpenAI.",
                "deals": "Where they meet: the cards in each country, Getnet's acceptance, and the race to make agentic payments a product."},
    },
    "tl": [
        ["May 2018", "Santander UK moves debit to Mastercard for eight years"],
        ["Feb 2023", "Santander México reissues debit as Mastercard Touch Cards"],
        ["Dec 2025", "Getnet named an early Agent Pay partner in Latin America"],
        ["2 Mar 2026", "Europe's first live AI-agent payment, with Mastercard"],
        ["Mar 2026", "Visa agentic pilot in five LatAm markets"],
        ["24 Mar 2026", "Agent Pay live at Santander Brasil"],
        ["Apr 2026", "TSB joins the group"],
        ["Jun 2026", "Getnet launches Agent Pay for Machines; Santander first on Visa Destinations"],
        ["Aug 2026", "Webster joins the group ⚠"],
    ],
    "l": {
        "U": {"d": 1, "s": "UK and Mexican customers carry Mastercard; elsewhere it is mixed.",
              "gap": "Mastercard reaches Santander UK and México debit customers, and agent-pay pilots; Brazil splits by card, and Spain, the US and Openbank's networks are not public.",
              "neo": "UK and Mexico cardholders, Brazil Mastercard Black holders, Getnet merchants on Agent Pay.", "snb": "Bizum users, Openbank Pay customers, car buyers, CIB clients."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "One App, branches, Openbank and partner channels are Santander's.",
               "neo": "None.", "snb": "One App, branches, Openbank, Amazon, Verizon."},
        "L4": {"d": 1, "s": "Mastercard in the UK and Mexico retail banks, partly in Brazil.",
               "gap": "The UK and Mexican retail banks run Mastercard debit; Brazil splits; CIB, wealth and consumer finance have no network role in public.",
               "neo": "Santander UK, Santander México, Brazil Select.", "snb": "CIB, wealth, Openbank consumer finance, Webster."},
        "L3": {"d": 1, "s": "Agent Pay is Mastercard's; the rest is Santander's.",
               "gap": "Agent Pay runs on Mastercard, with Visa piloting alongside; data, fraud and Openbank Pay are Santander's own.",
               "neo": "Agent Pay, agentic tokens and passkeys.", "snb": "Visa pilot, Cards Data Lab, fraud models, Openbank Pay, OpenAI."},
        "L2": {"d": 1, "s": "Cards partly Mastercard; processing, acquiring and account-to-account Santander's.",
               "gap": "Mastercard carries UK and Mexico debit; Plard processes in-house; Getnet accepts all networks; Bizum and Getnet Platforms are account-to-account.",
               "neo": "UK and Mexico cards, Getnet agentic acceptance.", "snb": "Plard, Bizum, Getnet Platforms, Ebury."},
        "L1": {"d": 0, "s": "The balance sheet, Gravity and strategy are Santander's.", "gap": "Nothing in the foundation is Mastercard's.",
               "neo": "None.", "snb": "Capital, leadership, markets, Gravity, OpenAI, deals."},
    },
    "t": {
        "1.1": {"d": 0, "why": "The group's own capital.", "v": [["Balance sheet", "No Mastercard role.", "0", ""]]},
        "1.2": {"d": 0, "why": "The board and leadership.", "v": [["Leadership", "No Mastercard role.", "0", ""]]},
        "1.3": {"d": 0, "why": "Heritage and markets.", "v": [["Markets", "No Mastercard role.", "0", ""]]},
        "1.4": {"d": 0, "why": "Gravity, the cloud and OpenAI.", "v": [["Technology", "No Mastercard role.", "0", ""]]},
        "1.5": {"d": 0, "why": "Strategy and deals.", "v": [["Group network deal", "None found.", "u", ""]]},
        "2.1": {"d": 2, "why": "UK and Mexico debit on Mastercard; elsewhere mixed or not public.", "v": [
            ["Santander UK", "Mastercard debit and credit.", "", ""], ["Santander México", "Mastercard debit.", "", ""], ["Brazil", "Both networks.", "u", ""]]},
        "2.2": {"d": 1, "why": "Plard is in-house; tokens are the networks'.", "v": [["Plard", "In-house.", "0", ""], ["Network tokens", "On Mastercard cards.", "", ""]]},
        "2.3": {"d": 1, "why": "Getnet accepts every network and leads with Agent Pay.", "v": [["Card acceptance", "All networks.", "", ""], ["Agent Pay", "Mastercard first.", "", ""]]},
        "2.4": {"d": 0, "why": "Bizum and Getnet Platforms are account-to-account.", "v": [["Bizum", "No card network.", "0", ""]]},
        "2.5": {"d": 0, "why": "Ebury and cross-border are Santander's.", "v": [["Mastercard Move", "Not used.", "0", ""]]},
        "3.1": {"d": 3, "why": "Mastercard Agent Pay ran Europe's first live agent payment; Visa pilots alongside.", "v": [
            ["Agent Pay", "Spain and Brazil.", "", ""], ["Visa Intelligent Commerce", "Five LatAm markets.", "0", ""]]},
        "3.2": {"d": 0, "why": "Santander's own data.", "v": [["Data", "No Mastercard role.", "0", ""]]},
        "3.3": {"d": 0, "why": "Santander's own fraud models.", "v": [["Fraud tools", "None announced.", "u", ""]]},
        "3.4": {"d": 0, "why": "Openbank Pay is Santander's.", "v": [["Installments", "Not used.", "0", ""]]},
        "3.5": {"d": 1, "why": "Premium cards on both networks; Visa Destinations.", "v": [["Mastercard Black", "Brazil.", "", ""]]},
        "4.1": {"d": 1, "why": "Spanish cards on both networks ⚠.", "v": [["Spain cards", "Split not public.", "u", ""]]},
        "4.2": {"d": 1, "why": "Santander UK is Mastercard; TSB is believed Visa.", "v": [["Santander UK", "Mastercard.", "", ""], ["TSB", "Believed Visa.", "u", ""]]},
        "4.3": {"d": 1, "why": "Mexico Mastercard debit; Brazil both; Chile and Argentina not public.", "v": [["Mexico", "Mastercard.", "", ""], ["Chile, Argentina", "Not public.", "u", ""]]},
        "4.4": {"d": None, "why": "The US network split is not public.", "v": [["Webster", "Not verified.", "u", ""]]},
        "4.5": {"d": None, "why": "Openbank's card network is not public.", "v": [["Openbank cards", "Not verified.", "u", ""]]},
        "4.6": {"d": 0, "why": "CIB.", "v": [["CIB", "No Mastercard role.", "0", ""]]},
        "4.7": {"d": 0, "why": "Wealth and insurance.", "v": [["Wealth", "No Mastercard role.", "0", ""]]},
        "5.1": {"d": 0, "why": "One App.", "v": [["App", "No Mastercard role.", "0", ""]]},
        "5.2": {"d": 0, "why": "Branches.", "v": [["Branches", "No Mastercard role.", "0", ""]]},
        "5.3": {"d": None, "why": "Openbank's digital banks; card network not public.", "v": [["Openbank cards", "Not verified.", "u", ""]]},
        "5.4": {"d": 0, "why": "Partner channels.", "v": [["Partners", "No Mastercard role.", "0", ""]]},
    },
}
