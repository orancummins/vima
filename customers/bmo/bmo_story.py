"""BMO Financial Group's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bmo_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Canada's first bank as five discs that stack into one platform, from C$1.54 trillion of assets at the bottom to the "
       "BMO app, branches and partners at the top. Click the stack to open it. Choose who you are and what you want to do, "
       "and the areas that deliver it light up across the layers, joined in the order they act. Switch to the Mastercard "
       "lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("card", "Cardholders & rewards members", "gift"),
    ("us", "U.S. customers", "flag"),
    ("inv", "Investors & savers", "trending-up"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Commercial & corporate clients", "factory"),
]
USERS_DESC = ("Six kinds of client, about 13 million in all: everyday customers in Canada, cardholders and Blue Rewards members, "
              "customers in the US, investors and savers, small businesses, and the commercial and corporate clients that TPS "
              "and Capital Markets serve.")

WHO = {"con": "A BMO customer", "card": "A cardholder", "us": "A U.S. customer", "inv": "An investor",
       "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day in Canada",
     "why": "The everyday loop: a chequing account, Interac debit and e-Transfer, the app and card controls.",
     "steps": [("4.1", "chequing", "Open a chequing account"), ("2.4", "interacdebit", "Pay with Interac debit"),
               ("2.6", "etransfer", "Send an Interac e-Transfer"), ("5.1", "app", "Run it in the app"),
               ("3.3", "controls", "Lock or manage the card")]},
    {"id": "rewards", "who": "card", "name": "Earn with Blue Rewards",
     "why": "The new coalition and the Mastercard cards built for it, from June 2026.",
     "steps": [("2.1", "bluecard", "Take a Blue Rewards World Elite Mastercard"), ("3.1", "bluerewards", "Earn at 400+ brands"),
               ("3.2", "pushprov", "Add the card to Google Wallet"), ("5.3", "instacart", "Use the Instacart+ perk")]},
    {"id": "travel", "who": "card", "name": "Fly and spend on a card",
     "why": "VIPorter on Mastercard, or the eclipse line on Visa, with instalments and True Name.",
     "steps": [("2.1", "viporter", "Take a VIPorter Mastercard"), ("2.1", "eclipse", "Or an eclipse Visa"),
               ("3.3", "instalments", "Split a purchase with PaySmart"), ("3.3", "truename", "Show a chosen name")]},
    {"id": "us", "who": "us", "name": "Bank with BMO in the US",
     "why": "U.S. Banking after the branch sale: an account, Mastercard debit and credit, and card controls.",
     "steps": [("4.3", "usbanking", "Open an account with BMO Bank"), ("2.5", "usdebit", "Pay with Mastercard debit"),
               ("2.5", "uscashback", "Earn with the Cash Back Mastercard"), ("3.3", "controls", "Manage it in the Digital Card Control Suite")]},
    {"id": "invest", "who": "inv", "name": "Invest and insure",
     "why": "InvestorLine, Nesbitt Burns, Burgundy and BMO Insurance.",
     "steps": [("4.4", "investorline", "Trade commission-free on InvestorLine"), ("4.4", "privatewealth", "Get advice from Nesbitt Burns or Burgundy"),
               ("4.4", "insurance", "Insure health and dental")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A World Elite business card, Moneris for acceptance, e-Transfer and online banking.",
     "steps": [("2.2", "commercial", "Take a World Elite Business Mastercard"), ("2.9", "moneris", "Take cards through Moneris"),
               ("2.6", "etransfer", "Collect by Interac e-Transfer"), ("5.1", "olbb", "Run it in Online Banking for Business")]},
    {"id": "corp", "who": "corp", "name": "Pay suppliers from the ERP",
     "why": "TPS, Payment APIs, Commercial Express virtual cards and Global Pay.",
     "steps": [("4.2", "tps", "Bank with TPS"), ("2.6", "apis", "Pay through the Payment APIs"),
               ("2.3", "commexpress", "Pay by virtual card inside the ERP"), ("2.7", "globalpay", "Pay abroad with Global Pay")]},
    {"id": "tokens", "who": "corp", "name": "Settle in tokenised money",
     "why": "BMO's bank-led digital money: CME Group, the CAD deposit token and Project Agorá.",
     "steps": [("4.5", "capmkts", "Work with BMO Capital Markets"), ("2.8", "tokcash", "Move tokenised cash on CME's network"),
               ("2.8", "tokdeposits", "Settle in a CAD deposit token")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Most Canadian credit cards, business, commercial and corporate cards, US cards, Global Pay and True Name.",
     "steps": [("2.1", "bluecard", "Blue Rewards Mastercard cards"), ("2.2", "commercial", "Commercial Mastercard cards"),
               ("2.3", "commexpress", "Commercial Express in the ERP"), ("2.5", "usdebit", "US debit and credit"),
               ("2.7", "globalpay", "Global Pay on Cross-Border Services"), ("3.3", "truename", "True Name")]},
    {"id": "mcnext", "who": "mc", "name": "Where offers, debit and agents could land",
     "why": "Where BMO has needs and Mastercard is not yet in: offers inside Blue Rewards, debit beside Interac, agentic checkout on BMO's Google tokens, dispute data in card controls, deposit tokens and acceptance after Moneris.",
     "steps": [("3.1", "bluerewards", "Card-linked offers inside Blue Rewards"), ("2.4", "debitmc", "Debit Mastercard beside Interac"),
               ("3.2", "pushprov", "Agent Pay and Click to Pay on BMO's tokens"), ("3.3", "controls", "Consumer Clarity in the card controls"),
               ("2.8", "tokdeposits", "Multi-Token Network for the CAD deposit token"), ("2.9", "moneris", "Acceptance through Moneris's new owner")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across BMO Financial Group's map",
    "title": "A Mastercard bank, with Visa's premium line and Interac's debit",
    "lead": "Mastercard carries most of BMO's Canadian credit cards, including the new Blue Rewards range of June 2026, all of its business, commercial and corporate cards, and its US credit and debit. Global Pay runs on Mastercard Cross-Border Services, and in October 2026 BMO became the first Canadian issuer of Mastercard Commercial Express. Visa has held the premium eclipse line since 2020, Interac runs Canadian debit and e-Transfer, and BMO's tokenised-money work names no card network. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are BMO's own (Q3 2026 results, 25 August 2026; fiscal 2025, 4 December 2025). BMO's product pages and Mastercard's newsroom could not be reached, so card networks come from BMO press releases; debit Mastercard in Canada and the legacy Bank of the West cards are unverified.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Canadian credit", "Mastercard, plus Visa eclipse", "Blue Rewards, VIPorter, Ascend; eclipse since 2020"],
        ["Commercial cards", "Mastercard", "World Elite Business, commercial suite"],
        ["Corporate & virtual", "Mastercard Commercial Express", "Canada and US, October 2026"],
        ["Canadian debit", "Interac", "Debit Mastercard ⚠ unverified"],
        ["US cards", "Mastercard", "Cash Back credit; debit since 2019 ⚠"],
        ["Cross-border", "Mastercard Cross-Border Services", "Global Pay, 2020"],
        ["Tokenised money", "Bank-led", "CME Group, CAD deposit token, Agorá"],
        ["Acquiring", "Moneris", "For sale, about C$2.0bn"],
    ],
    "sides": {
        "neo": {"dir": "Most Canadian credit cards, all business, commercial and corporate cards, US credit and debit, Global Pay, True Name and Identity Check.",
                "deals": "What it does not do: Canadian debit and e-Transfer, the eclipse line, Blue Rewards itself, instalments, AI or tokenised deposits."},
        "snb": {"dir": "Visa for eclipse, Interac for debit and e-Transfer, The Clearing House and Zelle in the US, Google for tokens, and BMO's own loyalty, AI and deposit tokens.",
                "deals": "Where they meet: Blue Rewards, which earns on Mastercard and Visa cards and on Interac debit."},
    },
    "tl": [
        ["Sep 2015", "BMO Perks offers for Mastercard holders"],
        ["Mar 2016", "Biometric corporate card with Identity Check"],
        ["Oct 2020", "Global Pay on Mastercard Cross-Border Services"],
        ["Nov 2020", "eclipse Visa Infinite: Visa enters the line-up"],
        ["Mar 2022", "True Name on Canadian credit cards"],
        ["Aug 2023", "Extend virtual cards on Mastercard tokens"],
        ["Mar 2025", "VIPorter Mastercard launched"],
        ["Jun 2026", "Blue Rewards Mastercard range"],
        ["Aug 2026", "Moneris to be sold"],
        ["Oct 2026", "Mastercard Commercial Express"],
    ],
    "l": {
        "U": {"d": 1, "s": "Cardholders mostly carry Mastercard; debit users carry Interac.",
              "gap": "Credit, business and US cardholders carry Mastercard; eclipse holders carry Visa and Canadian debit users Interac.",
              "neo": "Most credit cardholders, business and corporate clients, US customers.", "snb": "eclipse holders, Interac debit users, investors."},
        "L5": {"d": 1, "s": "The front doors are BMO's; Instacart treats both networks alike.", "gap": "App, branches and Walmart are BMO's; the Instacart perk covers World Elite Mastercard and Visa Infinite.",
               "neo": "Instacart perk for Mastercard holders.", "snb": "App, branches, Walmart, Visa Infinite holders."},
        "L4": {"d": 1, "s": "US Banking's cards are Mastercard; the rest has no network role.", "gap": "Canadian accounts come with Interac debit; wealth, insurance and capital markets have no network role.",
               "neo": "U.S. Banking cards.", "snb": "Chequing, TPS, wealth, insurance, capital markets."},
        "L3": {"d": 1, "s": "True Name and Perks are Mastercard's; Blue Rewards and AI are BMO's.", "gap": "Blue Rewards, instalments, controls and AI are BMO's own; the token service behind Google provisioning is not named ⚠.",
               "neo": "True Name, Perks ⚠, Masterpass.", "snb": "Blue Rewards, PaySmart, controls, Lumi, Google."},
        "L2": {"d": 1, "s": "Most cards and Global Pay on Mastercard; debit and A2A elsewhere.", "gap": "Mastercard has most credit, commercial, corporate and US cards and cross-border; Visa has eclipse, Interac has debit and e-Transfer, and tokens are bank-led.",
               "neo": "Credit and commercial cards, Commercial Express, Extend, US cards, Global Pay.", "snb": "eclipse Visa, Interac, RTP and Zelle, tokenised money, Moneris."},
        "L1": {"d": 0, "s": "BMO's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, charter, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
