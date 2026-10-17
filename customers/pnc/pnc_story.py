"""PNC Financial Services Group's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from pnc_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A coast-to-coast US bank as five discs that stack into one platform, from $628 billion of assets and the FirstBank "
       "deal at the bottom to a rebuilt app, 2,400 branches and PINACLE at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("aff", "Affluent & private clients", "gem"),
    ("sme", "Small businesses", "briefcase"),
    ("merch", "Merchants", "store"),
    ("corp", "Corporate treasurers", "factory"),
    ("emp", "Employers & payers", "users-round"),
]
USERS_DESC = ("Six kinds of customer: everyday customers across about 2,400 branches, including 780,000 from FirstBank; affluent "
              "and private clients; small businesses; the merchants PNC acquires for; corporate treasurers on PINACLE; and "
              "employers and insurers who pay people.")

WHO = {"con": "A PNC customer", "aff": "A Premier or Private Bank client", "sme": "A small business", "merch": "A merchant",
       "corp": "A corporate treasurer", "emp": "An employer or insurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: Virtual Wallet or Simple Checking, a Visa debit card, the new app and Zelle.",
     "steps": [("4.1", "accounts", "Open a checking account"), ("5.1", "app", "Switch my pay in the app"), ("2.1", "debit", "Pay with Visa debit"),
               ("2.5", "zelle", "Send money with Zelle"), ("3.4", "security", "Protected from fraud")]},
    {"id": "credit", "who": "con", "name": "Borrow and earn on a card",
     "why": "PNC's Visa credit cards, with TotalRewards tiers on top.",
     "steps": [("2.2", "credit", "Take a PNC Visa card"), ("3.3", "totalrewards", "Earn more with TotalRewards"), ("4.2", "lending", "Borrow for a home or car")]},
    {"id": "firstbank", "who": "con", "name": "Move from FirstBank to PNC",
     "why": "780,000 Colorado and Arizona customers converted in June 2026.",
     "steps": [("1.4", "firstbank", "Become a PNC customer"), ("2.1", "debit", "Get a PNC Visa debit card"), ("5.1", "app", "Move to the new app"),
               ("5.2", "branches", "Keep my branch")]},
    {"id": "wealth", "who": "aff", "name": "Grow and borrow against wealth",
     "why": "Premier Client, securities-based lending, the Private Bank and bitcoin.",
     "steps": [("4.3", "premier", "Join Premier Client"), ("3.3", "totalrewards", "Reach Gold or Platinum"), ("4.3", "privatebank", "Use the Private Bank"),
               ("2.6", "crypto", "Buy bitcoin through PNC")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Business checking with a Visa debit card, Mobile Accept in the app and real-time payments.",
     "steps": [("2.1", "bizdebit", "Use a Visa business debit card"), ("2.4", "mobileaccept", "Take cards in the PNC app"), ("2.5", "zelle", "Get paid by Zelle")]},
    {"id": "merchant", "who": "merch", "name": "Take payments in a restaurant or shop",
     "why": "PNC Merchant Services, Tempus and Linga.",
     "steps": [("2.4", "linga", "Run the restaurant on Linga"), ("2.4", "merchant", "Settle cards through PNC Merchant Services"), ("4.4", "tm", "Manage cash with Treasury Management")]},
    {"id": "treasury", "who": "corp", "name": "Run treasury on PINACLE",
     "why": "PINACLE inside the ERP, commercial cards, real-time rails and AI cash forecasts.",
     "steps": [("5.3", "pinacle", "Bank inside Oracle or Coupa"), ("2.3", "comcard", "Pay suppliers with virtual cards"), ("2.5", "rtp", "Pay instantly on RTP or FedNow"),
               ("3.2", "cashforecast", "Forecast cash with AI"), ("3.1", "akoya", "Share data through Akoya")]},
    {"id": "payouts", "who": "emp", "name": "Pay claims, wages and payouts",
     "why": "Claim payments, earned-wage access, Visa Direct and workplace banking.",
     "steps": [("4.4", "cpr", "Pay claims and earned wages"), ("2.5", "visadirect", "Push to cards with Visa Direct"), ("2.5", "rtp", "Or pay account to account"),
               ("5.4", "workplace", "Offer PNC as a benefit")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "On the acceptance side, plus a 2019 real-time pilot: PNC's own cards are Visa.",
     "steps": [("2.4", "merchant", "Mastercard accepted at PNC merchants"), ("2.4", "linga", "Mastercard through Linga"),
               ("2.4", "mobileaccept", "Mastercard through Mobile Accept"), ("2.5", "pod", "Payment on Delivery pilot, 2019")]},
    {"id": "mcnext", "who": "mc", "name": "Where open finance, offers and payouts could land",
     "why": "Where PNC has needs and Mastercard is not yet in: open finance through Akoya, card-linked offers for TotalRewards, data for the new app, virtual cards, payouts, and a second network if rules require one.",
     "steps": [("3.1", "akoya", "Open finance through Akoya"), ("3.3", "totalrewards", "Card-linked offers for TotalRewards"),
               ("5.1", "app", "Insights and Agent Pay in the new app"), ("2.3", "comcard", "Commercial and virtual cards"),
               ("2.5", "visadirect", "Mastercard Move for payouts"), ("2.1", "debit", "A second debit network ⚠")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across PNC's map",
    "title": "Visa on every PNC card; Mastercard only at the till",
    "lead": "Every card PNC lists is Visa: debit, credit, business debit and, it appears, commercial. PNC holds Visa shares and renewed its Visa Direct collaboration in October 2025. Mastercard reaches PNC through the merchants PNC acquires for, a 2019 real-time pilot and a shared stake in interchange litigation. The FirstBank conversion in June 2026 put 780,000 more customers on PNC's Visa cards ⚠. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are PNC's own (Q3 2026 results, 15 October 2026; 2025 Form 10-K) or from PNC, Visa and press releases. The commercial-card network rests on one PNC page, and FirstBank's card network before conversion was not found.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "$717m of debit fees, 2025"],
        ["Credit", "Visa", "Cash Rewards, Cash Unlimited, Spend Wise"],
        ["Commercial", "Visa ⚠", "Virtual cards with Extend, Nov 2025"],
        ["Payouts", "Visa Direct", "Renewed Oct 2025"],
        ["Real-time", "RTP, FedNow, Zelle", "FedNow from Oct 2025"],
        ["Acceptance", "PNC Merchant Services", "All networks, Mastercard included"],
        ["Mastercard", "Payment on Delivery", "RTP pilot, Oct 2019 ⚠"],
        ["Visa equity", "Class B shares", "$448m gain, Q2 2026"],
    ],
    "sides": {
        "neo": {"dir": "Acceptance at PNC's merchants (Merchant Services, Linga, Mobile Accept), the 2019 Payment on Delivery pilot, and the interchange litigation-sharing agreements.",
                "deals": "What it does not do: issue any PNC card, carry payouts, open-banking data, loyalty or fraud tools."},
        "snb": {"dir": "Visa on debit, credit and commercial cards and on payouts; RTP, FedNow and Zelle for account-to-account; Akoya for data; PNC's own AI and rewards.",
                "deals": "Where they meet: the merchants PNC acquires for, who take both networks."},
    },
    "tl": [
        ["Aug 2006", "PNC Mastercard credit cards via U.S. Bancorp ⚠"],
        ["Oct 2019", "Mastercard Payment on Delivery pilot on PNC's RTP access"],
        ["Jun 2021", "BBVA USA joins; converted October 2021"],
        ["Sep 2022", "Linga POS acquired"],
        ["Jun 2025", "PNC Mobile Accept"],
        ["Oct 2025", "FedNow; Visa Direct collaboration renewed"],
        ["Nov 2025", "Extend virtual commercial cards"],
        ["Jan 2026", "FirstBank closes"],
        ["Apr 2026", "PNC TotalRewards"],
        ["Jun 2026", "FirstBank converted; Visa share exchange"],
        ["Jul 2026", "New PNC Mobile app"],
    ],
    "l": {
        "U": {"d": 0, "s": "PNC's customers carry Visa cards.", "gap": "Cardholders carry Visa; Mastercard reaches PNC's merchants, not its customers.",
              "neo": "Merchants accepting Mastercard.", "snb": "Cardholders, FirstBank converts, corporates, Private Bank clients."},
        "L5": {"d": 0, "s": "The front doors are PNC's.", "gap": "The app, branches, PINACLE and workplace banking are PNC's own.", "neo": "None.", "snb": "App, branches, PINACLE, Workplace Advantage."},
        "L4": {"d": 0, "s": "The business lines come with Visa cards.", "gap": "Accounts carry Visa debit; lending, wealth and treasury have no Mastercard role.",
               "neo": "None.", "snb": "Accounts, lending, wealth, Treasury Management, CIB."},
        "L3": {"d": None, "s": "Nothing public from Mastercard.", "gap": "Data flows through Akoya; rewards, AI and fraud are PNC's own. Mastercard Open Banking is unconfirmed ⚠.",
               "neo": "Possibly open banking via Akoya ⚠.", "snb": "Akoya, Plaid, TotalRewards, the fusion centre."},
        "L2": {"d": 1, "s": "Mastercard at the till and in one old pilot.", "gap": "Visa has every card and payouts; Mastercard is accepted by PNC's merchants and piloted Payment on Delivery in 2019.",
               "neo": "Acceptance, Payment on Delivery ⚠.", "snb": "Visa cards, Visa Direct, RTP, FedNow, Zelle."},
        "L1": {"d": 0, "s": "The foundation leans to Visa.", "gap": "PNC holds Visa shares; nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, deals, Visa equity, technology."},
    },
    "t": area_lens(LAYERS),
}
