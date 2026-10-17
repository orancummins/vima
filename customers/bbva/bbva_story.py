"""BBVA's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bbva_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Spain's second bank and Mexico's first as five discs that stack into one platform, from €965 billion of assets "
       "at the bottom to the BBVA app, branches and Banco de Barrio at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("newc", "First-time borrowers", "graduation-cap"),
    ("prem", "Affluent & private clients", "gem"),
    ("saver", "Digital-bank customers", "smartphone"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer, 82.8 million active in all: everyday customers in Spain and Mexico, first-time "
              "borrowers, affluent and private clients, customers of the Italian and German digital banks, small "
              "businesses and the corporates CIB serves.")

WHO = {"con": "A BBVA customer", "newc": "A first-time borrower", "prem": "A private-banking client",
       "saver": "A digital-bank customer", "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "mexico", "who": "con", "name": "Bank day to day in Mexico",
     "why": "The everyday loop at Mexico's largest bank: the app, a Visa debit card, SPEI transfers, Blue and a dynamic CVV.",
     "steps": [("5.1", "app", "Open an account in the app"), ("2.1", "mxdebit", "Pay with Visa debit"), ("2.6", "spei", "Send money by SPEI"),
               ("3.3", "blue", "Ask Blue"), ("3.1", "dyncvv", "Shop online with a dynamic CVV")]},
    {"id": "spain", "who": "con", "name": "Bank day to day in Spain",
     "why": "BBVA Spain with Aqua debit, Bizum and an agent that can pay.",
     "steps": [("4.1", "esretail", "Bank with BBVA Spain"), ("2.2", "esdebit", "Pay with Aqua debit"), ("2.6", "bizum", "Send or pay by Bizum"),
               ("3.2", "agentic", "Let an AI agent pay")]},
    {"id": "firstcard", "who": "newc", "name": "Get a first credit card",
     "why": "1.5 million new cards in H1 2026, 19% to people with no credit history.",
     "steps": [("5.3", "partners", "Join through Banco de Barrio"), ("2.1", "mxcredit", "Get a first Visa credit card"), ("3.4", "puntos", "Earn Puntos BBVA")]},
    {"id": "home", "who": "con", "name": "Buy a home in Mexico",
     "why": "More than a quarter of new Mexican mortgages.",
     "steps": [("4.2", "mxmortgage", "Take a mortgage"), ("5.2", "branches", "Sign at a branch")]},
    {"id": "premium", "who": "prem", "name": "Travel and invest as a private client",
     "why": "The Visa Infinite range of March 2026 and Spanish wealth management.",
     "steps": [("5.2", "branches", "See a banker"), ("2.2", "espremium", "Carry Visa Infinite"), ("4.1", "eswealth", "Invest and insure")]},
    {"id": "digital", "who": "saver", "name": "Bank with a digital bank in Germany or Italy",
     "why": "Free accounts, debit cashback and a Mastercard credit card.",
     "steps": [("4.5", "debank", "Open a German account"), ("2.3", "dedebit", "Get a debit card"), ("2.3", "decredit", "Add the Mastercard credit card"),
               ("3.1", "dyncvv", "Pay with a dynamic CVV")]},
    {"id": "sme", "who": "sme", "name": "Run a small business in Mexico",
     "why": "A terminal from Banco de Barrio, advances on card sales and SPEI collections.",
     "steps": [("4.3", "smes", "Open an SME account"), ("2.5", "barrio", "Take cards on a BBVA terminal"),
               ("2.4", "mxbizcards", "Borrow against terminal sales"), ("2.6", "spei", "Collect by SPEI")]},
    {"id": "corp", "who": "corp", "name": "Pay suppliers as a corporate",
     "why": "CIB, virtual cards for travel and a euro stablecoin.",
     "steps": [("4.4", "cib", "Bank with CIB"), ("2.4", "vcn", "Pay suppliers with virtual cards"), ("2.7", "qivalis", "Settle in a euro stablecoin")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The digital banks' credit cards, the Renfe co-brand and the Mexican virtual cards.",
     "steps": [("2.3", "itcredit", "Italy credit on Mastercard"), ("2.3", "decredit", "Germany credit on Mastercard"),
               ("2.2", "renfe", "Renfe Mastercard"), ("2.4", "vcn", "Virtual cards with Sabre")]},
    {"id": "mcnext", "who": "mc", "name": "Where digital banks, agents and virtual cards could land",
     "why": "Where BBVA has needs and Mastercard is not yet in: digital-bank debit, agentic payments, virtual cards beyond Mexico, account-to-account fraud on Bizum and SPEI, and the Spanish credit range.",
     "steps": [("2.3", "dedebit", "Digital-bank debit"), ("3.2", "agentic", "Agent Pay beside Visa's pilot"),
               ("2.4", "vcn", "Virtual cards to South America and Europe"), ("2.6", "spei", "Scam scores on SPEI and Bizum"),
               ("2.2", "escredit", "Compete for the Aqua credit range")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across BBVA's map",
    "title": "Two Visa home markets, with Mastercard at the digital edges",
    "lead": "BBVA México's credit and debit cards, Spain's debit and the premium range of March 2026 run on Visa, and BBVA's first AI-agent payment ran on Visa Intelligent Commerce. Mastercard has the newer edges: credit cards at the Italian and German digital banks, the Renfe co-brand in Spain and virtual cards for Mexican travel agencies. Bizum and SPEI take more volume each year. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (January–June 2026 report, 30 July 2026) or BBVA México's (2T26 report). Spanish, Italian and German product pages blocked automated reading; the Aqua networks rest on contracts and a comparison site ⚠. No group network agreement is public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Mexico cards", "Visa", "Credit and debit; 31% of credit cards"],
        ["Spain debit", "Visa ⚠", "Aqua, numberless"],
        ["Spain premium", "Visa", "Infinite and Platinum, March 2026"],
        ["Spain co-brand", "Mastercard", "Renfe, June 2022"],
        ["Digital banks", "Mastercard", "Italy 2024, Germany 2026"],
        ["Virtual cards", "Mastercard", "Sabre Direct Pay, Mexico, 2025"],
        ["Agentic", "Visa", "Intelligent Commerce, July 2026"],
        ["Account-to-account", "Bizum, SPEI", "30.6m users; 7.3bn transfers"],
    ],
    "sides": {
        "neo": {"dir": "Italian and German credit cards, the Renfe Mastercard, travel-agency virtual cards, and acceptance at BBVA's terminals.",
                "deals": "What it does not do: Mexican cards, Spanish debit and premium credit, agentic payments, Bizum, SPEI or the stablecoin."},
        "snb": {"dir": "Visa in Mexico and on Spanish debit and premium cards, Visa's agentic pilot, Bizum and SPEI, Qivalis and BBVA's own AI.",
                "deals": "Where they meet: the digital banks, where Mastercard has credit and debit is not confirmed."},
    },
    "tl": [
        ["Apr 1971", "Spain's first bank card, with BankAmericard"],
        ["Jun 2022", "Renfe Mastercard with BBVA Consumer Finance"],
        ["Nov 2024", "BBVA Italy credit card on Mastercard"],
        ["Jun 2025", "Visa World Cup alliance in Mexico; German digital bank opens"],
        ["Sep 2025", "Mastercard and Sabre virtual cards in Mexico"],
        ["Oct 2025", "Sabadell bid fails"],
        ["Dec 2025", "ChatGPT Enterprise for 120,000 staff"],
        ["Mar 2026", "Visa Infinite range in Spain"],
        ["Jun 2026", "BBVA Germany credit card on Mastercard"],
        ["Jul 2026", "First agent payment, on Visa"],
        ["Sep 2026", "Elechiguerra takes over BBVA México"],
    ],
    "l": {
        "U": {"d": 1, "s": "Digital-bank and Renfe cardholders carry Mastercard; most others carry Visa.",
              "gap": "Mexico's 34.5 million customers and Spain's debit and premium holders carry Visa; Italian and German credit cardholders carry Mastercard.",
              "neo": "Digital-bank credit holders, Renfe cardholders, travel agencies.", "snb": "Mexican cardholders, Spanish debit and premium holders, Bizum and SPEI users."},
        "L5": {"d": 0, "s": "The front doors are BBVA's.", "gap": "App, branches and Banco de Barrio are BBVA's; Renfe and Sabre are the Mastercard partners.",
               "neo": "Renfe and Sabre partnerships.", "snb": "App, branches, Banco de Barrio, Mexican co-brands."},
        "L4": {"d": 0, "s": "The business lines carry Visa cards, except the digital banks.", "gap": "Spain and Mexico sell Visa cards; the digital banks issue Mastercard credit.",
               "neo": "Digital banks' credit cards.", "snb": "Spain, Mexico, CIB, wealth, South America."},
        "L3": {"d": 0, "s": "Security, AI and rewards are BBVA's own or Visa's.", "gap": "Dynamic CVV is BBVA's; the agentic pilot and Mexican benefits are Visa's.",
               "neo": "Nothing in public.", "snb": "Visa Intelligent Commerce, Visa benefits, Blue on OpenAI."},
        "L2": {"d": 1, "s": "Visa carries the big books; Mastercard the digital banks and virtual cards.", "gap": "Visa has Mexico and most of Spain; Mastercard has Italy and Germany credit, Renfe and the travel virtual cards; Bizum and SPEI grow beside both.",
               "neo": "Italy and Germany credit, Renfe, virtual cards.", "snb": "Visa cards in Mexico and Spain, Bizum, SPEI, Qivalis."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's; its card heritage is Visa's.", "neo": "None.", "snb": "Capital, governance, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
