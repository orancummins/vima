"""MUFG's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from mufg_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Japan's largest bank group as five discs that stack into one platform, from ¥434 trillion of assets and a record "
       "quarter at the bottom to the MUFG Bank app, Emut and a digital bank at the top. Click the stack to open it. Choose "
       "who you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("aff", "Savers & wealthy clients", "gem"),
    ("cf", "Consumer-finance borrowers", "hand-coins"),
    ("sme", "Small businesses & merchants", "store"),
    ("corp", "Corporates", "factory"),
    ("asia", "Customers across Asia", "earth"),
]
USERS_DESC = ("Six kinds of customer: about 34 million MUFG Bank retail customers and 60 million across the group, wealthy "
              "clients, ACOM's borrowers, small businesses and merchants, Japan's corporates, and the customers of partner "
              "banks and investees across Asia.")

WHO = {"con": "An MUFG customer", "aff": "A wealthy client", "cf": "An ACOM customer", "sme": "A small business",
       "corp": "A corporate treasurer", "asia": "A customer in Asia"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "An account, a Visa or JCB debit card, the app, transfers and fraud checks.",
     "steps": [("4.1", "accounts", "Open an account"), ("2.3", "debit", "Pay with Visa or JCB debit"), ("5.1", "bankapp", "Run it in the app"),
               ("2.6", "transfers", "Send money with Cotra"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "card", "who": "con", "name": "Pay and earn with a card",
     "why": "Mitsubishi UFJ Card on the network the customer picks, tapped in store, with up to 20% back.",
     "steps": [("2.1", "mucard", "Choose Mitsubishi UFJ Card's network"), ("2.5", "contactless", "Tap to pay"), ("3.4", "points", "Earn Global Points"),
               ("2.3", "gpwallet", "Spend points from the wallet")]},
    {"id": "emutbank", "who": "con", "name": "Bank digitally with Emut",
     "why": "The Emut brand, the digital bank opening in early 2027 and AI advice.",
     "steps": [("5.2", "emut", "Join Emut"), ("5.2", "emutbank", "Open an Emut Bank account"), ("3.2", "mapai", "Get advice from MAP AI"),
               ("3.2", "aiagents", "Ask an AI agent")]},
    {"id": "wealth", "who": "aff", "name": "Grow and pass on wealth",
     "why": "Investing on a card, the Emut Excellent Club and digital inheritance.",
     "steps": [("4.3", "wealth", "Invest with eSmart Securities and WealthNavi"), ("2.1", "gold", "Fund it with a Gold Prestige card"),
               ("3.4", "excellent", "Join Emut Excellent Club"), ("4.3", "inheritance", "Plan inheritance with Emut Sozoku")]},
    {"id": "borrow", "who": "cf", "name": "Borrow from ACOM",
     "why": "A loan and the AC Mastercard, run from an app.",
     "steps": [("4.2", "consumerfin", "Take an ACOM loan"), ("2.4", "acmc", "Get an AC Mastercard"), ("5.1", "cardapps", "Manage it in the app")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Card acceptance through NICOS, business cards and bank transfers.",
     "steps": [("2.5", "acquiring", "Take cards through NICOS"), ("4.4", "corpcard", "Pay with a business card"), ("2.6", "transfers", "Pay suppliers by transfer")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Corporate banking, a payments business in the making and tokenised settlement.",
     "steps": [("4.4", "jcib", "Bank with JCIB"), ("4.4", "globalpay", "Use MUFG's payments services"), ("2.7", "tokens", "Settle on-chain")]},
    {"id": "asia", "who": "asia", "name": "Bank with MUFG in Asia",
     "why": "Partner banks, digital lenders and wallets, and new JCB cards.",
     "steps": [("4.5", "danamon", "Bank with Danamon"), ("4.5", "digitalasia", "Pay with an MUFG-backed wallet"), ("4.5", "jcbasean", "Carry a premium JCB card")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "One of four networks on Mitsubishi UFJ Card, the only network on AC Mastercard and JAL CLUB-A, one of two on business cards, and accepted through NICOS.",
     "steps": [("2.1", "mucard", "Mitsubishi UFJ Card on Mastercard"), ("2.4", "acmc", "AC Mastercard"), ("2.2", "cobrand", "JAL Mastercard CLUB-A"),
               ("4.4", "corpcard", "Business cards on Mastercard"), ("2.5", "acquiring", "Acceptance through NICOS")]},
    {"id": "mcnext", "who": "mc", "name": "Where corporate cards, agents and the digital bank could land",
     "why": "Where MUFG has needs and Mastercard is not yet in: the corporate cashless push, the Emut Bank card, AI agents, fraud tokens, the premium club and payments across Asia.",
     "steps": [("4.4", "corpcard", "Commercial and virtual cards"), ("5.2", "emutbank", "A debit card for Emut Bank"), ("3.2", "aiagents", "Agent Pay for AI agents"),
               ("3.1", "fraud", "Tokens and fraud scores"), ("3.4", "excellent", "A premium card for the club"), ("4.5", "digitalasia", "Cross-border flows with Asian wallets")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across MUFG's map",
    "title": "One of four on the cards, while the 2026 alliance goes to JCB",
    "lead": "Mitsubishi UFJ NICOS lets customers pick Mastercard, Visa, JCB or American Express for its flagship card, and ACOM's AC Mastercard rides on Mastercard alone. But MUFG Bank's debit is Visa and JCB, its prepaid wallet is Visa, in-store Apple Pay runs on QUICPay, and in July 2026 MUFG Bank signed a strategic alliance in ASEAN with JCB, a scheme its predecessors founded. No MUFG–Mastercard agreement has been published. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (Q1 FY2026 highlights, 3 August 2026; Investors Day, September 2026) or from NICOS, MUFG Bank and ACOM product pages. MUFG publishes no split of cards or spending by network, and NICOS gives no member count.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Mitsubishi UFJ Card", "Mastercard, Visa, JCB, Amex", "Customer's choice; no split published"],
        ["AC Mastercard", "Mastercard", "About 1.05m holders, June 2026"],
        ["Bank debit", "Visa, JCB", "No Mastercard debit"],
        ["Prepaid wallet", "Visa", "Global Point Wallet"],
        ["Business cards", "Visa, Mastercard", "Corporate push from 2026"],
        ["Scheme alliance", "JCB", "ASEAN MOU, 6 July 2026"],
        ["Digital bank", "Not announced", "Opens January–March 2027"],
    ],
    "sides": {
        "neo": {"dir": "A network choice on NICOS's credit cards, the whole of AC Mastercard and JAL CLUB-A, half of business cards, and acceptance through NICOS and Airペイ.",
                "deals": "What it does not do: bank debit, prepaid, QUICPay, the JCB alliance, stablecoins, AI or open data."},
        "snb": {"dir": "Visa and JCB debit, Visa prepaid, JCB's QUICPay and ASEAN alliance, American Express platinum, and MUFG's own fraud, AI and data.",
                "deals": "Where they meet: the multi-network Mitsubishi UFJ Card and business cards."},
    },
    "tl": [
        ["1961", "Sanwa Bank and Nippon Shinpan found JCB"],
        ["Apr 2007", "Mitsubishi UFJ NICOS formed"],
        ["Dec 2022", "MUFG Union Bank sold to U.S. Bancorp"],
        ["Mar 2025", "EMV 3-D Secure mandatory in Japan"],
        ["Jun 2025", "Emut launched"],
        ["Jul 2025", "JFTC accepts Visa commitment plan"],
        ["Dec 2025", "DC Card merged into MUFG Card system"],
        ["Apr 2026", "Hanzawa becomes Group CEO"],
        ["Jul 2026", "MUFG Bank and JCB ASEAN alliance"],
        ["Sep 2026", "MUFG Emut Bank licensed"],
        ["Early 2027", "Emut Bank opens"],
    ],
    "l": {
        "U": {"d": 1, "s": "Card customers can carry Mastercard; debit holders cannot.",
              "gap": "Mitsubishi UFJ Card holders choose a network and ACOM's card holders carry Mastercard; MUFG Bank debit holders carry Visa or JCB.",
              "neo": "AC Mastercard holders, Mitsubishi UFJ Card holders who choose it, business cardholders.", "snb": "Debit holders, Amex platinum holders, Asian customers."},
        "L5": {"d": 1, "s": "Emut bundles a multi-network card; Emut Bank's network is open.", "gap": "The apps and branches are MUFG's; the digital bank has not named a card network.",
               "neo": "Emut through Mitsubishi UFJ Card.", "snb": "Bank app, branches, partners."},
        "L4": {"d": 1, "s": "Business cards and ACOM carry Mastercard; Asia leans to JCB.", "gap": "Business cards are Visa or Mastercard and ACOM's card is Mastercard; the ASEAN alliance is with JCB.",
               "neo": "Business cards, AC Mastercard.", "snb": "Accounts, home loans, wealth, JCIB, the JCB alliance."},
        "L3": {"d": 0, "s": "Services are MUFG's own.", "gap": "Fraud, AI, data and points are built in-house or with OpenAI, Google and Moneytree.",
               "neo": "None.", "snb": "NICOS fraud models, MAP AI, Moneytree, points."},
        "L2": {"d": 1, "s": "Mastercard is one of several on cards, absent from debit.", "gap": "Credit offers four networks, ACOM is Mastercard-only, debit is Visa and JCB, prepaid is Visa.",
               "neo": "Mitsubishi UFJ Card option, AC Mastercard, JAL CLUB-A, acquiring.", "snb": "Visa and JCB debit, Visa prepaid, QUICPay, Amex, Cotra, stablecoins."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's; JCB grew from MUFG's predecessors.", "neo": "None.", "snb": "Capital, leadership, Morgan Stanley, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
