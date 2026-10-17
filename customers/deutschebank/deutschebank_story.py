"""Deutsche Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from deutschebank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Germany's self-styled Global Hausbank as five discs that stack into one platform, from €491 billion of loans and a plan to 2028 "
       "at the bottom to the Deutsche Bank and Postbank apps, Autobahn and branches at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in "
       "the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("aff", "Wealth clients", "gem"),
    ("trav", "Frequent flyers", "plane"),
    ("sme", "Small businesses", "briefcase"),
    ("merch", "Merchants", "store"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Six kinds of client: about 19 million private clients in Germany, wealth clients, Miles & More "
              "cardholders, 800,000 small businesses, merchants, and the corporates and institutions of the Corporate "
              "and Investment Banks.")

WHO = {"con": "A Deutsche Bank customer", "aff": "A wealth client", "trav": "A frequent flyer", "sme": "A small business",
       "merch": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "An AktivKonto, a girocard with Debit Mastercard, a phone wallet and Wero.",
     "steps": [("4.1", "pbanking", "Open an account"), ("2.1", "dbcard", "Pay with the Deutsche Bank Card"), ("2.8", "wallets", "Add it to a phone wallet"),
               ("2.8", "wero", "Send money with Wero"), ("3.1", "bestsign", "Approve with BestSign")]},
    {"id": "postbank", "who": "con", "name": "Bank with Postbank",
     "why": "Postbank's cards, app and AI assistant.",
     "steps": [("5.1", "apps", "Use the Postbank app"), ("2.1", "pbcard", "Order a virtual Card plus"), ("2.2", "pbcredit", "Take a Postbank Mastercard"),
               ("3.2", "aiclient", "Ask the AI assistant")]},
    {"id": "fly", "who": "trav", "name": "Earn and spend miles",
     "why": "The Miles & More Mastercard, issued by Deutsche Bank since October 2025.",
     "steps": [("2.3", "milesmore", "Take a Miles & More card"), ("3.3", "milespay", "Pay with miles at the till"), ("3.1", "c2p", "Check out with Click to Pay")]},
    {"id": "wealth", "who": "aff", "name": "Grow wealth",
     "why": "Wealth Management, DWS funds and a premium card.",
     "steps": [("4.1", "wealth", "Invest with Wealth Management"), ("4.4", "dws", "Hold DWS funds"), ("2.2", "dbcredit", "Carry a Gold or Platin card")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Business Banking, a business Mastercard, a Clover terminal from Vert and AI onboarding.",
     "steps": [("3.2", "aicb", "Onboard in minutes"), ("4.2", "cb", "Open a business account"), ("2.4", "bizcard", "Pay with BusinessCard"),
               ("2.6", "vert", "Take cards with Vert")]},
    {"id": "merch", "who": "merch", "name": "Sell online and abroad",
     "why": "Merchant Solutions with cards, open-banking Request to Pay and Visa's fraud screening.",
     "steps": [("2.5", "ms", "Accept cards and 30+ methods"), ("2.5", "rtp", "Collect by Request to Pay"), ("3.1", "cybersource", "Screen orders with Cybersource"),
               ("2.5", "msextras", "Offer BNPL and local currency")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "The leading euro clearer, instant payments, dbX and corporate cards.",
     "steps": [("5.2", "autobahn", "Log in to Autobahn"), ("2.7", "cash", "Pay and clear across 140 countries"), ("2.7", "instant", "Send instant with payee checks"),
               ("2.4", "amex", "Give staff Amex corporate cards"), ("4.2", "trade", "Finance the supply chain")]},
    {"id": "digital", "who": "corp", "name": "Hold and settle digital assets",
     "why": "Custody, the AllUnity stablecoins and tokenised money.",
     "steps": [("2.9", "custody", "Hold crypto and stablecoins"), ("2.9", "allunity", "Settle in EURAU"), ("2.9", "agora", "Test tokenised deposits")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The Debit Mastercard co-badge, every credit card, Miles & More, business cards, Click to Pay and Request to Pay.",
     "steps": [("2.1", "dbcard", "Debit Mastercard on every girocard"), ("2.2", "dbcredit", "Mastercard credit"), ("2.3", "milesmore", "Miles & More, won together"),
               ("2.4", "bizcard", "Business cards"), ("3.1", "c2p", "Click to Pay"), ("2.5", "rtp", "Open-banking Request to Pay")]},
    {"id": "mcnext", "who": "mc", "name": "Where corporate cards, agents and stablecoins could land",
     "why": "Where Deutsche Bank has needs and Mastercard is not yet in: corporate cards held by Amex, B2B2C issuing, Agent Pay for the AI agents, merchant fraud screening held by Visa, cross-border and stablecoin settlement.",
     "steps": [("2.4", "amex", "Commercial cards against Amex"), ("2.4", "b2b2c", "B2B2C card issuing"), ("3.2", "aiclient", "Agent Pay for voice agents"),
               ("3.1", "cybersource", "Merchant risk against Cybersource"), ("2.7", "cash", "Mastercard Move for cross-border"), ("2.9", "allunity", "Stablecoin settlement")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Deutsche Bank's map",
    "title": "Mastercard on every card, with girocard and Wero at home",
    "lead": "Every Deutsche Bank and Postbank card programme found runs on Mastercard: Debit Mastercard co-badged on the girocards, all consumer and business credit, and the Miles & More card the two won together in 2023. Mastercard open banking powers Request to Pay in Merchant Solutions. But girocard carries domestic debit, Wero is growing, Amex holds corporate cards and Visa screens merchant fraud. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (Q2 2026 results, 29 July 2026; investor deep dive, 17 November 2025) or from Deutsche Bank, Postbank and Lufthansa pages. Mastercard's newsroom could not be read; the June 2025 open-banking deal rests on a search summary. No dated master agreement with Mastercard was found.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "girocard + Debit Mastercard", "Every Deutsche Bank and Postbank card"],
        ["Credit", "Mastercard", "Some legacy Postbank Visa ⚠"],
        ["Miles & More", "Mastercard", "Issued by Deutsche Bank since Oct 2025"],
        ["Business cards", "Mastercard", "BusinessCard Direct and BusinessCard"],
        ["Corporate T&E", "American Express", "Business Platinum, Corporate Card"],
        ["Merchant fraud", "Visa Cybersource", "Since Sep 2022"],
        ["Open banking", "Mastercard", "Request to Pay, Jun 2025 ⚠"],
        ["A2A", "Wero", "Deutsche Bank is an EPI shareholder"],
    ],
    "sides": {
        "neo": {"dir": "The debit co-badge, all consumer and business credit, Miles & More and MilesPay, wallet tokens and Click to Pay, and open-banking Request to Pay.",
                "deals": "What it does not do: domestic girocard spend, corporate T&E cards, merchant fraud screening, Wero, clearing or stablecoins."},
        "snb": {"dir": "girocard at home, Amex for corporates, Visa Cybersource for merchants, Fiserv behind Vert, Wero for account-to-account, and AllUnity and Taurus for digital assets.",
                "deals": "Where they meet: acceptance at Vert and Merchant Solutions, which take every network."},
    },
    "tl": [
        ["Feb 2021", "Wider payments partnership for business clients"],
        ["Sep 2022", "Visa Cybersource for merchant fraud"],
        ["Oct 2022", "Vert launched with Fiserv"],
        ["Jul 2023", "Miles & More won with Mastercard"],
        ["Dec 2024", "giropay closes; Wero takes over"],
        ["Jun 2025", "Request to Pay on Mastercard open banking ⚠"],
        ["Oct 2025", "Deutsche Bank issues Miles & More"],
        ["Sep 2026", "AllUnity stablecoins on Arc"],
    ],
    "l": {
        "U": {"d": 1, "s": "Every cardholder carries Mastercard, beside girocard.",
              "gap": "Private, flyer and business cardholders carry Mastercard; at home girocard takes debit and corporates carry Amex.",
              "neo": "Cardholders, Miles & More members, business cardholders.", "snb": "girocard spend, Wero users, Amex corporate holders, institutions."},
        "L5": {"d": 1, "s": "The front doors are the bank's; Miles & More is a Mastercard partner channel.", "gap": "Apps, portals and branches are Deutsche Bank's.",
               "neo": "Miles & More channel.", "snb": "Apps, Autobahn, branches, Fiserv."},
        "L4": {"d": 1, "s": "Accounts come with Mastercard cards.", "gap": "Personal and business accounts carry Mastercard; wealth, investment banking, custody and DWS do not.",
               "neo": "Card-linked accounts.", "snb": "Wealth, IB, trade, TSS, DWS."},
        "L3": {"d": 1, "s": "Click to Pay and MilesPay are Mastercard; fraud screening is Visa.", "gap": "Visa's Cybersource screens merchant orders; AI is Google's and the bank's.",
               "neo": "Click to Pay, MilesPay, Business Bonus.", "snb": "BestSign, Cybersource, AI tools."},
        "L2": {"d": 1, "s": "Cards on Mastercard; acceptance, clearing and Wero are not.", "gap": "All issuing is Mastercard; Amex holds corporate cards and Wero, clearing and digital assets run elsewhere.",
               "neo": "Debit co-badge, credit, Miles & More, business cards, Request to Pay.", "snb": "girocard, Amex, Wero, clearing, stablecoins."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, brands, Google Cloud, strategy."},
    },
    "t": area_lens(LAYERS),
}
