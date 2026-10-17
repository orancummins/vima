"""Revolut's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

SUB = ("Europe's most valuable fintech as five discs that stack into one platform, from $2.3 billion of profit and bank "
       "licences in more than 30 markets at the bottom to one app in 40 countries at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in the "
       "order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("travel", "Travellers & senders", "plane"),
    ("young", "Under-18s", "graduation-cap"),
    ("aff", "Premium & Metal investors", "gem"),
    ("crypto", "Crypto users", "coins"),
    ("sme", "Businesses", "briefcase"),
    ("merch", "Merchants", "store"),
]
USERS_DESC = ("Seven kinds of user, more than 80 million in 40 countries: everyday customers, travellers and senders, "
              "under-18s, premium and Metal subscribers who invest, 16 million crypto users, 767,000 businesses and the "
              "merchants who take Revolut Pay.")

WHO = {
    "con": "A Revolut customer", "travel": "A traveller", "young": "A teenager", "aff": "A Metal subscriber",
    "crypto": "A crypto user", "sme": "A small business", "merch": "A merchant",
}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day on Revolut",
     "why": "The everyday loop: a bank account, a card on Mastercard or Visa, RevPoints and AI fraud screening.",
     "steps": [("5.1", "app", "Open an account in the app"), ("4.1", "accounts", "Get a bank account"),
               ("2.1", "cards", "Pay with a card"), ("3.3", "revpoints", "Earn RevPoints"), ("3.1", "protection", "Protected by AI fraud checks")]},
    {"id": "travel", "who": "travel", "name": "Spend and send abroad",
     "why": "What Revolut was built for: FX at close to interbank, cards that work anywhere, and transfers to 90 countries.",
     "steps": [("2.3", "fx", "Exchange currency"), ("2.1", "cards", "Pay abroad with the card"),
               ("2.2", "payouts", "Send money to a card abroad"), ("3.4", "extras", "Add travel insurance")]},
    {"id": "young", "who": "young", "name": "Get a first account",
     "why": "Revolut <18, with parents in control.",
     "steps": [("4.1", "kids", "Open Revolut <18"), ("5.1", "app", "Manage it in the app")]},
    {"id": "wealth", "who": "aff", "name": "Invest and subscribe",
     "why": "Metal and Ultra plans, ETFs, an ISA and credit.",
     "steps": [("3.3", "revpoints", "Subscribe to Metal or Ultra"), ("2.1", "premium", "Carry a premium card"),
               ("4.3", "trading", "Invest in ETFs or an ISA"), ("4.4", "credit", "Borrow or take a mortgage")]},
    {"id": "crypto", "who": "crypto", "name": "Hold crypto and stablecoins",
     "why": "Crypto trading for 16 million, Revolut X, and EURR from August 2026.",
     "steps": [("2.6", "crypto", "Buy crypto"), ("2.6", "eurr", "Hold EURR"), ("2.5", "local", "Move euros by Wero")]},
    {"id": "business", "who": "sme", "name": "Run a business on Revolut",
     "why": "Accounts, cards, payouts and acceptance for 767,000 businesses.",
     "steps": [("4.2", "business", "Open Revolut Business"), ("2.1", "premium", "Issue Titan cards"),
               ("2.2", "payouts", "Pay out to cards"), ("2.4", "acquiring", "Take cards on Terminal")]},
    {"id": "merchant", "who": "merch", "name": "Take payments",
     "why": "Revolut Pay at checkout, and Terminal, Reader and Gateway for cards.",
     "steps": [("2.4", "revpay", "Add Revolut Pay"), ("2.4", "acquiring", "Accept every card"), ("5.2", "growth", "Reach Revolut's customers")]},
    {"id": "agent", "who": "con", "name": "Let AIR shop for you",
     "why": "AIR is getting autonomous shopping, with tests from December 2026.",
     "steps": [("3.2", "air", "Ask AIR to buy"), ("2.1", "cards", "Pay with a card token"), ("3.1", "protection", "Checked by fraud models")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Launch partner in 2015 and, under the 2019 deal, at least half of Revolut's European cards.",
     "steps": [("2.1", "cards", "Half of the European cards"), ("4.1", "accounts", "Cards on UK and EEA accounts"),
               ("2.4", "acquiring", "Acceptance on Revolut's terminals"), ("3.3", "revpoints", "RevPoints on card spend")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, payouts and the US could land",
     "why": "Where Revolut has needs and Mastercard is not yet in: AIR's agentic shopping, payouts held by Visa Direct, scam scoring for a new UK bank, US credit after the charter, new markets and stablecoin cards.",
     "steps": [("3.2", "air", "Agent Pay for AIR"), ("2.2", "payouts", "Move against Visa Direct"),
               ("3.1", "protection", "Consumer Fraud Risk for the UK bank"), ("4.4", "credit", "US credit cards from 2027"),
               ("5.3", "markets", "Network choice in new markets"), ("2.6", "eurr", "Stablecoin-linked cards")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Revolut's map",
    "title": "Launch partner, sharing the card book with Visa",
    "lead": "Mastercard launched Revolut's first cards in 2015, and a 2019 deal gave it at least half of Revolut's European cards and its first US cards. The same year Visa became lead issuer for Revolut's new markets, and today Visa carries Revolut's payouts, India, Canada and the US credit card. Revolut Pay, Wero and a euro stablecoin take payments off the networks altogether. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Revolut's own (2025 annual report) or from regulators, Mastercard, Visa and press. Revolut does not disclose its network split, and no joint Mastercard announcement since 2019 has been found.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["European cards", "At least half Mastercard", "2019 deal; current split undisclosed"],
        ["New markets", "Visa lead issuer", "Since 2019; India, Canada Visa"],
        ["Payouts", "Visa Direct", "P2P (2023) and Business (2024)"],
        ["US credit card", "Visa ⚠", "Via Cross River; own cards after the 2027 charter"],
        ["Checkout", "Revolut Pay", "Account-to-account, 0.5% + 2p"],
        ["Stablecoin", "EURR", "Issued by Bridge, August 2026"],
        ["Agentic", "AIR pilot", "December 2026; AP2 co-developer"],
        ["Card revenue", "$1.3bn", "2025, +45%"],
    ],
    "sides": {
        "neo": {"dir": "At least half of the European cards, cards on UK and EEA bank accounts, acceptance on Revolut's terminals, and the 2015 launch relationship.",
                "deals": "What it does not do in public: payouts, new-market issuing, fraud tools, agentic shopping or stablecoins."},
        "snb": {"dir": "Visa as lead issuer for new markets and on Visa Direct payouts, Revolut Pay, Wero and UPI, EURR with Bridge, and Revolut's own fraud, FX and credit.",
                "deals": "Where they meet: every card Revolut issues, and the US network choice coming with the charter."},
    },
    "tl": [
        ["2015", "Mastercard is Revolut's launch partner"],
        ["Jul 2017", "First Visa cards in Europe"],
        ["Sep 2019", "Visa becomes lead issuer for global expansion"],
        ["Oct 2019", "Mastercard deal: half of European cards, first US cards, Send"],
        ["2023–24", "Payouts on Visa Direct"],
        ["Mar 2026", "UK bank out of mobilisation"],
        ["Aug 2026", "EURR stablecoin with Bridge"],
        ["Sep 2026", "OCC conditional approval for a US bank"],
        ["Dec 2026", "AIR agentic shopping tests due"],
    ],
    "l": {
        "U": {"d": 1, "s": "Many customers carry a Mastercard; just as many carry Visa.",
              "gap": "Mastercard reaches perhaps half of European cardholders; Visa carries new markets, payouts and US credit; crypto and Revolut Pay users touch neither.",
              "neo": "European and UK cardholders on Mastercard.", "snb": "Visa cardholders, Revolut Pay users, crypto users."},
        "L5": {"d": 0, "s": "The front doors are Revolut's.", "gap": "The app, referrals and new markets are Revolut's; network choices in new markets are open.",
               "neo": "None.", "snb": "App, referrals, sponsorships."},
        "L4": {"d": 1, "s": "Accounts come with cards on both networks.",
               "gap": "Accounts carry Mastercard or Visa cards; Business, credit and Under-18s networks are undisclosed; wealth has no network.",
               "neo": "Cards on accounts.", "snb": "Wealth, credit (Visa in the US ⚠)."},
        "L3": {"d": 0, "s": "The engine room is Revolut's.", "gap": "Fraud, AIR, plans and extras are Revolut's; RevPoints are earned on network cards.",
               "neo": "RevPoints on card spend.", "snb": "Customer Protection Platform, AIR, plans."},
        "L2": {"d": 1, "s": "Cards shared; payouts Visa; much moves off the networks.",
               "gap": "Mastercard shares the card book; Visa Direct carries payouts; FX, Revolut Pay, Wero, UPI, crypto and EURR are off the card networks.",
               "neo": "European cards, acceptance.", "snb": "Visa cards and Direct, Revolut Pay, Wero, UPI, EURR."},
        "L1": {"d": 0, "s": "Revolut's own capital and licences.", "gap": "Nothing in the foundation is Mastercard's.",
               "neo": "None.", "snb": "Licences, ownership, technology, strategy."},
    },
    "t": {
        "1.1": {"d": 0, "why": "Revolut's scale; card revenue shared across networks.", "v": [["Card revenue", "Both networks.", "u", ""]]},
        "1.2": {"d": 0, "why": "Revolut's licences.", "v": [["Licences", "No Mastercard role.", "0", ""]]},
        "1.3": {"d": 0, "why": "Ownership and leadership.", "v": [["Ownership", "No Mastercard role.", "0", ""]]},
        "1.4": {"d": 0, "why": "In-house technology.", "v": [["Technology", "No Mastercard role.", "0", ""]]},
        "1.5": {"d": 0, "why": "Strategy.", "v": [["Strategy", "No Mastercard role.", "0", ""]]},
        "2.1": {"d": 1, "why": "At least half of European cards on Mastercard; new markets on Visa.", "v": [
            ["European cards", "At least half, 2019.", "", ""], ["New markets", "Visa.", "0", ""], ["Premium and Titan", "Not disclosed.", "u", ""]]},
        "2.2": {"d": 0, "why": "Payouts run on Visa Direct.", "v": [["Mastercard Send", "Promised 2019; not visible.", "u", ""]]},
        "2.3": {"d": 0, "why": "Revolut's own FX.", "v": [["FX", "No Mastercard role.", "0", ""]]},
        "2.4": {"d": 1, "why": "Terminals accept every network; Revolut Pay is account-to-account.", "v": [["Acceptance", "All networks.", "", ""], ["Revolut Pay", "Off the networks.", "0", ""]]},
        "2.5": {"d": 0, "why": "Wero and UPI are account-to-account.", "v": [["Wero, UPI", "No card network.", "0", ""]]},
        "2.6": {"d": 0, "why": "Crypto and EURR are off the networks.", "v": [["Stablecoin cards", "None.", "0", ""]]},
        "3.1": {"d": 0, "why": "Revolut's own fraud platform.", "v": [["Consumer Fraud Risk", "Not used.", "u", ""]]},
        "3.2": {"d": 0, "why": "AIR has no network partner named.", "v": [["Agent Pay", "Not announced.", "u", ""]]},
        "3.3": {"d": 1, "why": "RevPoints earned on network card spend.", "v": [["RevPoints", "Revolut's own.", "", ""]]},
        "3.4": {"d": 0, "why": "Mobile and insurance.", "v": [["Extras", "No Mastercard role.", "0", ""]]},
        "4.1": {"d": 1, "why": "Accounts carry Mastercard or Visa cards.", "v": [["Cards", "Both networks.", "", ""]]},
        "4.2": {"d": None, "why": "Business card network not disclosed.", "v": [["Business cards", "Not disclosed.", "u", ""]]},
        "4.3": {"d": 0, "why": "Wealth.", "v": [["Trading", "No Mastercard role.", "0", ""]]},
        "4.4": {"d": None, "why": "Credit card networks undisclosed; US Visa ⚠.", "v": [["Credit cards", "Undisclosed.", "u", ""]]},
        "5.1": {"d": 0, "why": "The app.", "v": [["App", "No Mastercard role.", "0", ""]]},
        "5.2": {"d": 0, "why": "Referrals and sponsorships.", "v": [["Growth", "No Mastercard role.", "0", ""]]},
        "5.3": {"d": None, "why": "Network choices in new markets are open.", "v": [["New markets", "Open.", "u", ""]]},
    },
}
