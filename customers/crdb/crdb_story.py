"""CRDB Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from crdb_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Tanzania's largest bank as five discs that stack into one platform, from TZS 26.4 trillion of assets at the "
       "bottom to SimBanking, 243 branches and 38,000 agents at the top. Click the stack to open it. Choose who you "
       "are and what you want to do, and the areas that deliver it light up across the layers, joined in the order they "
       "act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("prem", "Premier & affluent customers", "gem"),
    ("sme", "Small businesses & merchants", "briefcase"),
    ("farm", "Farmers & cooperatives", "hand-coins"),
    ("corp", "Corporates & institutions", "factory"),
    ("xb", "Diaspora & cross-border clients", "earth"),
    ("inv", "Savers & investors", "trending-up"),
]
USERS_DESC = ("Seven kinds of user, about 7.95 million customers in all: everyday customers, Premier and affluent clients, "
              "small businesses and QR merchants, farmers and cooperatives, corporates and government bodies, Tanzanians "
              "abroad and cross-border traders, and savers and shareholders.")

WHO = {"con": "A CRDB customer", "prem": "A Premier customer", "sme": "A merchant", "farm": "A farmer",
       "corp": "A corporate treasurer", "xb": "A Tanzanian abroad", "inv": "A saver or investor"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a TemboCard Visa, SimBanking, transfers to wallets over TIPS and Tembo Points.",
     "steps": [("4.1", "accounts", "Open an account"), ("2.1", "tembovisa", "Pay with a TemboCard Visa"),
               ("5.1", "simbanking", "Run it in SimBanking"), ("2.5", "tips", "Send to a bank or wallet"),
               ("3.1", "cardcontrols", "Get alerts and block a card"), ("3.4", "tembopoints", "Earn Tembo Points")]},
    {"id": "premier", "who": "prem", "name": "Bank as a Premier client",
     "why": "Premier banking with a Visa Infinite debit card, a Mastercard World Rewards credit card and Visa travel benefits.",
     "steps": [("4.1", "premier", "Join Premier"), ("2.1", "tembovisa", "Carry a Visa Infinite card"),
               ("2.2", "mccredit", "Borrow on a Mastercard credit card"), ("3.4", "visaperks", "Use lounges and concierge")]},
    {"id": "online", "who": "con", "name": "Shop online and subscribe",
     "why": "A UnionPay virtual card made in the app, a TemboCard Visa linked to PayPal, or a prepaid card.",
     "steps": [("2.3", "upi", "Create a UnionPay virtual card"), ("2.1", "tembovisa", "Or pay with TemboCard Visa"),
               ("2.3", "prepaid", "Or load a prepaid card"), ("3.1", "fraud", "Protected by fraud monitoring")]},
    {"id": "merchant", "who": "sme", "name": "Get paid as a merchant",
     "why": "Lipa Hapa: TanQR and Lipa Namba, POS for every network, an online gateway, and MSME credit.",
     "steps": [("2.4", "tanqr", "Take TanQR and Lipa Namba"), ("2.4", "pos", "Take cards at a POS"),
               ("2.4", "gateway", "Sell online through the gateway"), ("4.2", "msme", "Borrow to grow"),
               ("5.4", "ib", "Reconcile in internet banking")]},
    {"id": "farmer", "who": "farm", "name": "Finance a harvest",
     "why": "Seasonal agribusiness loans, payments to farmers' wallets, livestock insurance and agents in the village.",
     "steps": [("4.2", "agri", "Take a seasonal loan"), ("2.5", "farmerpay", "Get paid into a wallet"),
               ("4.5", "insurance", "Insure livestock with Smart Mifugo"), ("5.3", "wakala", "Cash out at a CRDB Wakala")]},
    {"id": "corp", "who": "corp", "name": "Finance trade across the region",
     "why": "Corporate and trade finance, FX, the Dubai office and the Burundi and DRC banks.",
     "steps": [("4.3", "corporate", "Open letters of credit"), ("2.6", "forexatm", "Hedge and buy FX"),
               ("5.4", "dubaioffice", "Meet the bank in Dubai"), ("1.3", "drc", "Bank in DR Congo"),
               ("4.4", "treasury", "Place surplus in government securities")]},
    {"id": "diaspora", "who": "xb", "name": "Send money home",
     "why": "Money from abroad through Western Union, Ria, Upesi or NALA, into an account, a wallet or an agent token.",
     "steps": [("2.6", "remit", "Send through a remittance partner"), ("4.1", "accounts", "Into a Tanzanite account"),
               ("5.3", "agenttoken", "Or collect cash with a token"), ("2.6", "forexatm", "Change currency at a forex ATM")]},
    {"id": "invest", "who": "inv", "name": "Save and invest",
     "why": "Fixed deposits, CRDB shares and bonds through the Mwanahisa mini-app, and Islamic savings.",
     "steps": [("4.1", "accounts", "Open a fixed deposit"), ("3.3", "mwanahisa", "Buy shares in SimBanking"),
               ("1.2", "owners", "Hold CRDB shares"), ("4.5", "barakah", "Save Shariah-compliant")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mastercard credit cards for Premier clients, acceptance on Lipa Hapa, issuing on the SmartVista switch and alerts.",
     "steps": [("2.2", "mccredit", "Mastercard World Rewards and Gold credit"), ("4.1", "premier", "In the Premier bundle"),
               ("2.4", "pos", "Mastercard at Lipa Hapa POS"), ("2.4", "gateway", "Mastercard on the gateway"),
               ("1.4", "smartvista", "Mastercard issuing on SmartVista"), ("3.1", "cardcontrols", "Alerts on Mastercard use")]},
    {"id": "mcnext", "who": "mc", "name": "Where commercial cards, corridors and tokens could land",
     "why": "Where CRDB has needs and Mastercard is not yet in: business cards for SMEs and corporates, cross-border flows through Dubai, Burundi and the DRC, fraud tools for SimBanking, a tokenised credit card in the app, and merchant risk for 315,000 QR merchants.",
     "steps": [("4.2", "msme", "SME and trader cards"), ("4.3", "corporate", "Commercial and virtual cards"),
               ("2.6", "remit", "Cross-border sends through Mastercard Move"), ("3.1", "fraud", "Scam and fraud tools for SimBanking"),
               ("5.1", "simbanking", "A tokenised Mastercard credit card in SimBanking"), ("2.4", "tanqr", "Merchant risk and data for QR merchants"),
               ("2.2", "newcredit", "Keep the new credit cards on Mastercard")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across CRDB Bank's map",
    "title": "A Visa debit bank where Mastercard keeps a small credit book and mobile money moves the money",
    "lead": "CRDB's TemboCard debit cards, 8.9 million registered cards across Tanzania, Burundi and since April 2026 the DRC, are Visa, with UnionPay second and a UnionPay virtual card in the app. Mastercard holds the World Rewards and Gold credit cards launched in 2018, a book of only TZS 3.1 billion, plus acceptance on Lipa Hapa and issuing on the new SmartVista switch. Most retail money in Tanzania moves on mobile money, TIPS and TanQR. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (1H 2026 Investors' Briefing; 2025 Integrated Report) or from the Bank of Tanzania, TCRA and Tanzanian press. CRDB publishes no card counts by network, so the split is read from product pages.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "8.9m registered cards, 2025"],
        ["Credit", "Mastercard", "World Rewards and Gold; book TZS 3.1bn"],
        ["Virtual & online", "UnionPay", "Tembo UPI virtual card in SimBanking"],
        ["Acquiring", "All networks", "7,748 POS; gateway with 3-D Secure"],
        ["QR", "TanQR", "315,505 QR and Lipa Hapa merchants"],
        ["Instant & wallets", "TIPS, mobile money", "87m mobile-money subscriptions"],
        ["Subsidiaries", "Visa", "Burundi; DRC from April 2026"],
        ["Scheme fees", "Visa and Mastercard", "TZS 15.2bn paid in 2025"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard World Rewards and Gold credit cards, acceptance on Lipa Hapa POS and gateway, issuing on BPC SmartVista and card alerts.",
                "deals": "What it does not do: debit in any market, virtual cards, prepaid ⚠, remittance, QR, wallets, fraud tools or commercial cards."},
        "snb": {"dir": "Visa for all debit and premium benefits; UnionPay for virtual cards; TanQR, TIPS and mobile money for most payments; Western Union, Ria, Upesi and NALA for remittances.",
                "deals": "Where they meet: Premier bundles a Visa debit with a Mastercard credit card, and Lipa Hapa accepts every network."},
    },
    "tl": [
        ["2009", "Listed on the Dar es Salaam Stock Exchange"],
        ["Mar 2011", "TemboCard MasterCard debit ⚠"],
        ["2012", "CRDB Bank Burundi opens"],
        ["2014", "TemboCard Visa debit ⚠"],
        ["Feb 2018", "Mastercard World Rewards and Gold credit cards"],
        ["Sep 2022", "TanQR standard takes effect"],
        ["2023", "DR Congo bank, insurer and foundation"],
        ["Jun 2025", "BPC SmartVista switch for Visa, Mastercard and UnionPay"],
        ["2025", "T24 core goes live"],
        ["Oct 2025", "Agent tokens for cash without an account"],
        ["Jan 2026", "Dubai representative office opens"],
        ["Apr 2026", "TemboCard Visa launched in DR Congo"],
        ["Jul 2026", "1H 2026: TZS 417bn profit, TZS 26.4tn assets"],
    ],
    "l": {
        "U": {"d": 1, "s": "Premier credit-card holders carry Mastercard; most customers pay with Visa debit or mobile money.",
              "gap": "Mastercard reaches Premier clients through credit and every customer of a Lipa Hapa merchant; debit holders, wallet users and remitters are elsewhere.",
              "neo": "Premier credit-card holders, Mastercard-paying shoppers at CRDB merchants.", "snb": "Visa debit holders, UnionPay users, wallet payers, remitters."},
        "L5": {"d": 0, "s": "The front doors are CRDB's.", "gap": "SimBanking, branches, agents and the Dubai office carry no Mastercard product; ATM acceptance is not stated.",
               "neo": "None in public.", "snb": "SimBanking, branches and ATMs, CRDB Wakala, internet banking, Dubai office."},
        "L4": {"d": 1, "s": "Mastercard only in the Premier bundle.", "gap": "Retail, MSME, farm, corporate, treasury and Islamic banking have no card-network role; no commercial card is offered.",
               "neo": "Mastercard credit inside Premier.", "snb": "Loans, deposits, trade, treasury, Al Barakah, insurance."},
        "L3": {"d": 1, "s": "Card alerts cover Mastercard; the rest is CRDB's or Visa's.", "gap": "Fraud, data, AI, partner lending and Tembo Points are CRDB's own; premium benefits are Visa's.",
               "neo": "Alerts on Mastercard use.", "snb": "Fraud surveillance, CreditPro, Tembo Points, Visa Infinite benefits."},
        "L2": {"d": 1, "s": "Mastercard in credit and acceptance; Visa, UnionPay and national rails carry the rest.", "gap": "Visa carries all debit; UnionPay the virtual card; TanQR, TIPS and mobile money most payments; money-transfer operators remittances.",
               "neo": "Mastercard credit cards, POS and gateway acceptance.", "snb": "TemboCard Visa, UnionPay, TanQR, TIPS, Western Union and partners."},
        "L1": {"d": 1, "s": "The new card switch issues Mastercard among others.", "gap": "Capital, owners, T24 and strategy are CRDB's; SmartVista supports Mastercard issuing; Burundi and the DRC are Visa.",
               "neo": "Mastercard issuing on SmartVista.", "snb": "Balance sheet, owners, T24, EVOLVE, Visa in Burundi and the DRC."},
    },
    "t": area_lens(LAYERS),
}
