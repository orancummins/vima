"""CIBC's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from cibc_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Canada's Big Six bank CIBC as five discs that stack into one platform, from C$1.18 trillion of assets at the bottom "
       "to the CIBC app, banking centres and Costco kiosks at the top. Click the stack to open it. Choose who you are and "
       "what you want to do, and the areas that deliver it light up across the layers, joined in the order they act. Switch "
       "to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("card", "Cardholders & rewards members", "gift"),
    ("new", "Newcomers & senders abroad", "plane"),
    ("inv", "Investors & affluent clients", "trending-up"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Commercial & corporate clients", "factory"),
]
USERS_DESC = ("Six kinds of client, about 15 million in all: everyday customers at CIBC and Simplii, cardholders and rewards "
              "members, newcomers and people sending money abroad, investors and Imperial Service clients, small businesses, "
              "and the commercial, U.S. and corporate clients served by Commercial Banking and Capital Markets.")

WHO = {"con": "A CIBC customer", "card": "A cardholder", "new": "A newcomer", "inv": "An investor",
       "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a Smart Account, Interac and Visa Debit, e-Transfer, the app and CRTeX.",
     "steps": [("4.1", "smartaccount", "Open a Smart Account"), ("2.4", "advdebit", "Pay with Interac or Visa Debit"),
               ("2.5", "etransfer", "Send an Interac e-Transfer"), ("5.1", "app", "Run it in the app"),
               ("3.4", "crtex", "Get offers chosen by CRTeX")]},
    {"id": "shop", "who": "card", "name": "Shop on a Mastercard",
     "why": "The Costco and Adapta cards, now with Click to Pay from 21 October 2026.",
     "steps": [("5.3", "costcooffer", "Sign up at a Costco kiosk"), ("2.2", "costco", "Take the Costco Mastercard"),
               ("2.2", "adapta", "Or Adapta, which rewards the top three categories"), ("3.2", "clicktopay", "Check out with Click to Pay"),
               ("3.2", "wallets", "Pay with a phone")]},
    {"id": "travel", "who": "card", "name": "Travel on points",
     "why": "Aventura and Aeroplan on Visa, redeemed through Expedia and Air Canada.",
     "steps": [("2.1", "aventura", "Take an Aventura Visa"), ("2.1", "aeroplan", "Or an Aeroplan Visa"),
               ("3.1", "rewards", "Book through CIBC by Expedia"), ("5.3", "travel", "Fly Air Canada")]},
    {"id": "newcomer", "who": "new", "name": "Arrive in Canada and send money home",
     "why": "Digital onboarding, the newcomer Smart Account, Pearson banking centres and Global Money Transfer.",
     "steps": [("5.2", "branches", "Meet CIBC at Toronto Pearson"), ("3.3", "digitalid", "Verify identity online"),
               ("4.1", "smartaccount", "Open a Smart Account for Newcomers"), ("2.6", "gmt", "Send money home with Global Money Transfer")]},
    {"id": "simplii", "who": "con", "name": "Bank with Simplii",
     "why": "The no-fee direct bank, with a Debit Mastercard and a new app.",
     "steps": [("4.2", "simplii", "Open a Simplii Account"), ("2.4", "simpliidebit", "Pay with the Debit Mastercard"),
               ("2.5", "etransfer", "Move money by e-Transfer")]},
    {"id": "invest", "who": "inv", "name": "Plan and invest",
     "why": "Imperial Service, GoalPlanner and Canadian wealth, with U.S. Private Wealth across the border.",
     "steps": [("4.1", "imperial", "Get advice from Imperial Service"), ("3.4", "insights", "Build a plan in GoalPlanner"),
               ("4.4", "wealth", "Invest with Wood Gundy or Investor's Edge"), ("4.5", "usbank", "Bank and invest in the US")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Business banking, Visa business cards or the Costco Business Mastercard, and Global Payments for acceptance.",
     "steps": [("4.3", "business", "Open a business account"), ("2.3", "bizvisa", "Take a business Visa card"),
               ("2.3", "costcobiz", "Or the Costco Business Mastercard"), ("2.7", "globalpay", "Take cards through Global Payments")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Commercial banking and cash management, Capital Markets, and the tokenised-money pilots.",
     "steps": [("4.3", "commercial", "Bank with Commercial Banking"), ("4.6", "capmkts", "Work with Capital Markets"),
               ("2.6", "cadtoken", "Settle in a CAD deposit token"), ("2.6", "agora", "Test cross-border settlement in Agorá")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The Costco cards, Adapta, Simplii and CIBC Bank USA debit, and Click to Pay on those cards.",
     "steps": [("2.2", "costco", "Costco Mastercard"), ("2.2", "adapta", "Adapta Mastercard"),
               ("2.3", "costcobiz", "Costco Business Mastercard"), ("2.4", "simpliidebit", "Simplii Debit Mastercard"),
               ("2.4", "usdebit", "CIBC Bank USA debit"), ("3.2", "clicktopay", "Click to Pay from 21 October")]},
    {"id": "mcnext", "who": "mc", "name": "Where Costco, Adapta and transfers could take Mastercard",
     "why": "Where CIBC has needs and Mastercard is not yet in: offers and data on the Costco book, enrichment for Adapta and CRTeX, dispute data, agentic checkout on CIBC's tokens, Move beside Visa Direct, a commercial card and deposit tokens.",
     "steps": [("3.1", "offers", "Card-linked offers on the Costco book"), ("3.4", "crtex", "Enriched transactions for CRTeX and Adapta"),
               ("3.3", "fraud", "Dispute data in the automated disputes flow"), ("3.2", "wallets", "Agent Pay on CIBC's tokens"),
               ("2.6", "gmt", "Mastercard Move in Global Money Transfer"), ("2.3", "bizvisa", "A commercial Mastercard beside the Visa line"),
               ("2.6", "cadtoken", "Multi-Token Network for the CAD deposit token")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across CIBC's map",
    "title": "A Visa bank with a Costco-sized Mastercard book",
    "lead": "Visa carries almost all of CIBC's own-brand credit cards (Aventura, Aeroplan, Dividend), every CIBC debit card alongside Interac, most business cards and Global Money Transfer's card payouts. Mastercard came in with the Costco portfolio in March 2022 and grew with Adapta in May 2025, and it also carries Simplii's and CIBC Bank USA's debit cards. From 21 October 2026 CIBC enrols its credit cards in Click to Pay on both networks. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are CIBC's own (Q3 2026 results, 27 August 2026; 2025 Annual Report). Networks come from CIBC, Simplii and CIBC Bank USA product pages fetched on 17 October 2026. Costco balances, the Simplii debit launch date, token services and fraud vendors are unconfirmed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Personal credit", "Visa", "Aventura, Aeroplan, Dividend: about 20 cards"],
        ["Costco & Adapta", "Mastercard", "Costco since 2022; Adapta May 2025"],
        ["Business cards", "Visa, plus Costco Business", "Visa Spend Clarity"],
        ["CIBC debit", "Interac + Visa Debit", "Every Advantage Debit Card"],
        ["Simplii & US debit", "Mastercard", "Interac + Debit Mastercard; CIBC Bank USA"],
        ["Money abroad", "Visa Direct, MoneyGram, Citi", "Global Money Transfer"],
        ["Click to Pay", "Both networks", "Auto-enrolment from 21 Oct 2026"],
        ["Acquiring", "Global Payments", "Referral partner"],
    ],
    "sides": {
        "neo": {"dir": "The Costco cards, Adapta, the Costco Business card, Simplii and CIBC Bank USA debit, and Click to Pay on those cards.",
                "deals": "What it does not do: the Aventura, Aeroplan and Dividend lines, CIBC debit, business cards, Global Money Transfer, instalments, acquiring or tokenised deposits."},
        "snb": {"dir": "Visa for most credit, debit and business cards, Visa Direct and Visa Installments; Interac for debit and e-Transfer; Global Payments for acceptance; MoneyGram and Citi abroad; CIBC's own AI and tokens.",
                "deals": "Where they meet: Click to Pay, wallets and the rewards centre, which serve both networks."},
    },
    "tl": [
        ["Sep 2013", "TD takes about half the Aeroplan Visa book"],
        ["Aug 2017", "Simplii Financial launched"],
        ["Nov 2020", "New Aeroplan Visa suite"],
        ["Jun 2021", "Visa Installments announced"],
        ["Dec 2021", "Global Money Transfer on Visa Direct"],
        ["Feb 2022", "Tyl by CIBC; Mastercard a fellow Pollinate shareholder"],
        ["Mar 2022", "Costco Mastercard portfolio acquired"],
        ["Apr 2024", "CARDS II opened to Mastercard accounts"],
        ["May 2025", "Adapta Mastercard with Touch Card"],
        ["Nov 2025", "Harry Culham becomes CEO"],
        ["Sep 2026", "CAD deposit token and Project Agorá"],
        ["Oct 2026", "Click to Pay on all credit cards"],
    ],
    "l": {
        "U": {"d": 1, "s": "Costco and Adapta holders carry Mastercard; most others carry Visa.",
              "gap": "Costco, Adapta, Simplii and US debit clients carry Mastercard; Aventura, Aeroplan, Dividend and CIBC debit clients carry Visa and Interac.",
              "neo": "Costco and Adapta cardholders, Simplii and US debit users.", "snb": "Most cardholders, CIBC debit users, businesses."},
        "L5": {"d": 1, "s": "Costco kiosks feed the Costco Mastercard; the rest is CIBC's.", "gap": "The app and banking centres are CIBC's; Air Canada and Expedia serve Visa cards.",
               "neo": "Costco Banking Offer.", "snb": "App, banking centres, Air Canada, Expedia."},
        "L4": {"d": 1, "s": "Simplii and US debit on Mastercard; the rest has no network role.", "gap": "Personal accounts come with Interac and Visa Debit; wealth, commercial and capital markets have no network role.",
               "neo": "Simplii, CIBC Bank USA debit.", "snb": "Smart Account, wealth, commercial, capital markets."},
        "L3": {"d": 1, "s": "Click to Pay on both networks; the rest is CIBC's or Visa's.", "gap": "Rewards, CRTeX, insights and identity are CIBC's; instalments are Pace It and Visa; token services are not named ⚠.",
               "neo": "Click to Pay on Costco and Adapta.", "snb": "Visa Installments, Paymi, Skip, MX, CRTeX."},
        "L2": {"d": 1, "s": "Costco, Adapta and two debit cards on Mastercard; Visa and Interac carry the rest.", "gap": "Mastercard has the Costco and Adapta cards and Simplii and US debit; Visa has own-brand credit, CIBC debit, business cards, prepaid and Visa Direct; Interac has debit and e-Transfer.",
               "neo": "Costco, Adapta, Costco Business, Simplii debit, US debit.", "snb": "Aventura, Aeroplan, Dividend, Visa Debit, Visa Direct, Global Payments."},
        "L1": {"d": 0, "s": "CIBC's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, charter, AI, cloud, strategy."},
    },
    "t": area_lens(LAYERS),
}
