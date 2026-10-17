"""Banco do Brasil's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bancodobrasil_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Brazil's state-controlled bank, founded in 1808, as five discs that stack into one platform, from 92 million "
       "customers, R$1.31 trillion of loans and stakes in Elo and Cielo at the bottom to the BB app, 3,931 branches and "
       "18,221 correspondents at the top. Click the stack to open it. Choose who you are and what you want to do, and the "
       "areas that deliver it light up across the layers, joined in the order they act. Switch to the Mastercard lens to "
       "see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("prem", "Premium clients", "gem"),
    ("farm", "Farmers & agribusiness", "earth"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
    ("gov", "Public sector & servants", "landmark"),
]
USERS_DESC = ("Six kinds of customer, 92 million in all: everyday customers, premium and private clients, nearly 600,000 "
              "farm-credit clients, small businesses, corporates, and governments and the public servants who borrow "
              "against their pay.")

WHO = {"con": "A BB customer", "prem": "A premium client", "farm": "A farmer", "sme": "A small business",
       "corp": "A corporate treasurer", "gov": "A public servant"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The BB app, a debit card, Pix and Minhas Finanças, with fraud checks behind them.",
     "steps": [("5.1", "app", "Open the BB app"), ("2.3", "debit", "Pay with Ourocard debit"), ("2.4", "pix", "Send a Pix"),
               ("3.2", "minhasfinancas", "Track spending in Minhas Finanças"), ("3.1", "security", "Approve with BB Autenticador")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Ourocard on Visa, Elo or Mastercard, with Livelo points and Universo Ourocard.",
     "steps": [("2.1", "ourocard", "Take an Ourocard"), ("2.2", "smiles", "Or a Smiles co-brand"), ("3.3", "universo", "Play Universo Ourocard"),
               ("3.3", "livelo", "Earn Livelo points")]},
    {"id": "premium", "who": "prem", "name": "Travel as a premium client",
     "why": "Altus on Visa or Mastercard Black, Casa BB and investments.",
     "steps": [("2.2", "altus", "Carry Altus Liv"), ("2.2", "mcblack", "Or Ourocard Mastercard Black"), ("3.3", "casabb", "Wait in Casa BB"),
               ("4.5", "asset", "Invest with BB Asset")]},
    {"id": "farm", "who": "farm", "name": "Finance a harvest",
     "why": "Farm credit, renegotiation and rural insurance, through branches.",
     "steps": [("5.2", "branches", "Visit a branch"), ("4.1", "agro", "Finance a crop"), ("4.5", "seguridade", "Insure the harvest"),
               ("4.1", "regulariza", "Renegotiate a debt")]},
    {"id": "payroll", "who": "gov", "name": "Borrow against a salary",
     "why": "Payroll loans for public servants, retirees and private workers.",
     "steps": [("4.2", "payroll", "Take a payroll loan"), ("5.1", "app", "Manage it in the app")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Guaranteed credit, BB Pay and Cielo for acceptance, and the PJ app.",
     "steps": [("4.3", "sme", "Open a business account"), ("5.1", "apppj", "Run it in App BB PJ"), ("2.5", "bbpay", "Take payments with BB Pay"),
               ("2.5", "cielo", "Or a Cielo machine")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Corporate & IB, cash-management APIs and 84 countries.",
     "steps": [("4.3", "cib", "Bank with Corporate & IB"), ("2.7", "apis", "Integrate by API"), ("2.8", "fx", "Pay abroad")]},
    {"id": "public", "who": "gov", "name": "Fund a municipality",
     "why": "Public-sector lending through Eficiência Municipal.",
     "steps": [("4.4", "gov", "Borrow for a municipality"), ("2.7", "apis", "Collect and pay by API")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Ourocard Mastercard Black, Platinum and Gold, part of the credit book, Universo Ourocard since March 2026 and Casa BB.",
     "steps": [("2.2", "mcblack", "Ourocard Mastercard"), ("2.1", "ourocard", "Part of the credit book"), ("3.3", "universo", "Universo Ourocard"),
               ("3.3", "casabb", "Black holders at Casa BB")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, fraud and cross-border could land",
     "why": "Where BB has needs and Mastercard is not yet in: an Agent Pay pilot after Visa's, fraud and identity, card-portfolio analytics, cross-border, farm cards and government disbursement.",
     "steps": [("2.9", "agentic", "Agent Pay after Visa's pilot"), ("3.1", "security", "Fraud and identity"), ("2.1", "ourocard", "Portfolio analytics"),
               ("2.8", "fx", "Mastercard Move abroad"), ("4.1", "agro", "Farm input cards"), ("4.4", "gov", "Government disbursement")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Banco do Brasil's map",
    "title": "Mastercard third, behind the Elo it owns and Visa's premium cards",
    "lead": "Banco do Brasil co-owns Elo and a third of its network, and Visa carries its Altus premium cards and Brazil's first AI-agent purchase. Mastercard keeps the Ourocard Mastercard Black, Platinum and Gold, was added to Universo Ourocard in March 2026 and serves Black holders at Casa BB. No network split, contract or joint initiative is public. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (2Q26 results, 12 August 2026; institutional presentation, 1 September 2026) or from Brazilian card and travel press. BB's card pages could not be read, so networks by product rest on secondary sources; BB does not publish card counts or spending by network.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit", "Visa, Elo, Mastercard", "R$69.9bn book; split not published"],
        ["Elo", "Co-owned", "A third of the network"],
        ["Premium", "Visa Altus", "Altus Liv from 4Q25"],
        ["Mastercard cards", "Black, Platinum, Gold", "Still offered in 2026"],
        ["Debit", "Not disclosed", "Elo likely ⚠"],
        ["Agentic", "Visa", "First agent purchase, 11 Mar 2026"],
        ["Acceptance", "Cielo, BB Pay", "Cielo co-controlled with Bradesco"],
    ],
    "sides": {
        "neo": {"dir": "Ourocard Mastercard Black, Platinum and Gold, part of the credit book, Universo Ourocard and Casa BB access, and acceptance at Cielo.",
                "deals": "What it does not do: Elo, the Altus premium tier, agentic commerce, Pix, Livelo, farm or government lending."},
        "snb": {"dir": "Elo (co-owned), Visa Altus and the agentic pilot, Pix and Pix abroad, Livelo, and BB's own fraud and AI.",
                "deals": "Where they meet: Ourocard credit, premium travel and the next agentic pilot."},
    },
    "tl": [
        ["1987", "Ourocard launched"],
        ["2020", "Reports of BB halting new Mastercard credit ⚠"],
        ["Mar 2024", "IOF cut on Ourocard Mastercard Black"],
        ["Feb 2025", "Brazil Mastercard's second Click to Pay market"],
        ["Dec 2025", "Mastercard Agent Pay for Latin America"],
        ["Mar 2026", "Visa agentic purchase; Mastercard joins Universo Ourocard"],
        ["May 2026", "Guidance cut on farm losses"],
        ["Aug 2026", "2Q26: card business loses R$649m"],
    ],
    "l": {
        "U": {"d": 1, "s": "Some cardholders carry Mastercard.",
              "gap": "Mastercard Black, Platinum and Gold holders carry it; most see Elo or Visa, and Pix carries transfers.",
              "neo": "Ourocard Mastercard holders.", "snb": "Elo and Visa holders, Pix users, farmers, public servants."},
        "L5": {"d": 0, "s": "The front doors are BB's.", "gap": "The app, branches, correspondents and hubs are the bank's.", "neo": "None.", "snb": "App, branches, MaisBB, hubs."},
        "L4": {"d": 0, "s": "Business lines carry no network.", "gap": "Farm, payroll, company and government lending have no stated Mastercard role.",
               "neo": "None.", "snb": "Agro, payroll, companies, government, insurance."},
        "L3": {"d": 1, "s": "Universo and Casa BB now include Mastercard.", "gap": "Mastercard joined Universo Ourocard in 2026; fraud, AI and Livelo are BB's or Elopar's.",
               "neo": "Universo Ourocard, Casa BB access.", "snb": "Security, Minhas Finanças, CRM, Livelo."},
        "L2": {"d": 1, "s": "One network of three, behind Elo and Visa.", "gap": "Elo is co-owned, Visa leads premium and agentic; Mastercard keeps its Ourocard tier.",
               "neo": "Ourocard Mastercard, part of credit, Cielo acceptance.", "snb": "Elo, Visa, Pix, APIs, Drex."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's; its stakes are in Elo and Cielo.", "neo": "None.", "snb": "Capital, state control, strategy, stakes."},
    },
    "t": area_lens(LAYERS),
}
