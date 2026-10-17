"""Fiserv's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

SUB = ("America's largest merchant acquirer and a processor for 10,000 banks as five discs that stack into one platform, "
       "from $4.6 trillion of merchant volume and the Commerce Hub and Finxact platforms at the bottom to Clover devices, "
       "bank referrals and developer portals at the top. Click the stack to open it. Choose who you are and what you want "
       "to do, and the areas that deliver it light up across the layers, joined in the order they act. Switch to the "
       "Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("sme", "Small businesses", "store"),
    ("ent", "Enterprise merchants", "building-2"),
    ("fi", "Banks & credit unions", "landmark"),
    ("con", "Their customers", "user-round"),
    ("isv", "Software platforms & fintechs", "code-xml"),
    ("inv", "Investors & regulators", "chart-column"),
]
USERS_DESC = ("Six kinds of user: 3.9 million small businesses and about 900,000 Clover merchants, enterprise merchants, "
              "about 10,000 banks and credit unions and their customers, the software platforms that embed Fiserv, and "
              "the investors and regulators watching a turnaround.")

WHO = {
    "sme": "A small business", "ent": "An enterprise merchant", "fi": "A community bank", "con": "A bank customer",
    "isv": "A software platform", "inv": "An investor",
}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "clover", "who": "sme", "name": "Run a shop on Clover",
     "why": "The small-business loop: a Clover device, card acceptance, cash advances and an agent-ready checkout.",
     "steps": [("5.2", "bankchannel", "Get Clover through your bank"), ("5.1", "devices", "Set up the device"),
               ("4.1", "clover", "Run the business on Clover"), ("2.1", "acquiring", "Accept every card"),
               ("3.5", "smbfinance", "Take a Clover Capital advance")]},
    {"id": "agent", "who": "sme", "name": "Sell to AI agents",
     "why": "Fiserv signed both networks' agentic frameworks on the same day; Clover merchants get tokens and verified intent.",
     "steps": [("3.1", "agentpay", "Accept Mastercard Agent Pay"), ("3.1", "visaagent", "And Visa Intelligent Commerce"),
               ("2.1", "acquiring", "Settle through Fiserv")]},
    {"id": "enterprise", "who": "ent", "name": "Accept payments at enterprise scale",
     "why": "Commerce Hub and Carat, debit routed to STAR and Accel, and Mastercard Merchant Cloud behind one connection.",
     "steps": [("5.4", "developers", "Integrate Commerce Hub"), ("2.2", "carat", "Run acceptance on Carat"),
               ("2.4", "star", "Route debit to STAR or Accel"), ("2.2", "merchantcloud", "Add Mastercard Merchant Cloud"),
               ("3.6", "giftloyalty", "Run gift and loyalty")]},
    {"id": "bank", "who": "fi", "name": "Run a community bank on Fiserv",
     "why": "A core, digital banking, cards, Zelle and AI agents, all from one provider.",
     "steps": [("4.3", "core", "Run the core"), ("4.4", "xd", "Offer digital banking"),
               ("2.3", "issuing", "Process cards"), ("2.5", "zelle", "Offer Zelle"), ("3.3", "agentos", "Pilot agentOS")]},
    {"id": "cards", "who": "fi", "name": "Launch a card programme",
     "why": "Issuer processing, card production and debit networks for banks that want cards without building them.",
     "steps": [("4.5", "cardservices", "Design the programme"), ("2.3", "issuing", "Process on Optis or FirstVision"),
               ("2.4", "star", "Join STAR for PIN debit"), ("3.2", "fraud", "Score for fraud")]},
    {"id": "stablecoin", "who": "fi", "name": "Issue a stablecoin",
     "why": "The Digital Asset Platform, live since October 2026 with Bank of North Dakota.",
     "steps": [("2.6", "fiusd", "Issue on the Digital Asset Platform"), ("1.5", "finxact", "Keep the ledger on Finxact"),
               ("1.2", "licences", "Custody through StoneCastle Trust")]},
    {"id": "consumer", "who": "con", "name": "Pay bills and friends from your bank",
     "why": "What a bank customer sees: the app, Zelle, bill pay, ATMs and pay-over-time on debit.",
     "steps": [("4.4", "xd", "Bank in the app"), ("2.5", "zelle", "Send money by Zelle"),
               ("2.5", "checkfree", "Pay bills"), ("2.4", "moneypass", "Use a MoneyPass ATM")]},
    {"id": "embed", "who": "isv", "name": "Embed payments in your software",
     "why": "Ledger, payouts and acceptance as one stack.",
     "steps": [("5.4", "developers", "Use the APIs"), ("3.4", "embedded", "Embed accounts and payments"),
               ("4.6", "payouts", "Pay out to workers")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Four announcements in 14 months, each sponsored by Chiro Aikat: FIUSD, Agent Pay, Verifiable Intent and Merchant Cloud.",
     "steps": [("2.1", "acquiring", "Mastercard volume through the largest US acquirer"), ("2.2", "merchantcloud", "Merchant Cloud in Commerce Hub"),
               ("3.1", "agentpay", "Agent Pay and Verifiable Intent"), ("2.6", "fiusd", "FIUSD on the Multi-Token Network"),
               ("2.3", "issuing", "Mastercard programmes on Fiserv processors")]},
    {"id": "mcnext", "who": "mc", "name": "Where issuer services and the merchant pipe could land",
     "why": "Where Fiserv has needs and Mastercard is not yet in: named services through Merchant Cloud, live agentic volume, issuer services across 10,000 banks, Installments against Affirm, fraud and disputes, payouts, and a debit landscape that may shift if STAR is sold.",
     "steps": [("2.2", "merchantcloud", "Click to Pay, passkeys and Ethoca through Merchant Cloud"), ("3.1", "agentpay", "Live Agent Pay on Clover"),
               ("2.3", "issuing", "Tokens and Click to Pay for every issuer"), ("4.4", "xd", "Installments instead of Affirm"),
               ("3.2", "fraud", "Decision Intelligence and Consumer Clarity"), ("4.6", "payouts", "Move for payouts"),
               ("2.4", "star", "Debit, if STAR or Accel is sold")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Fiserv's map",
    "title": "A partner on the merchant side, a rival in debit",
    "lead": "Fiserv carries Mastercard volume as America's largest acquirer and processes Mastercard programmes for banks. Since 2025 the partnership has grown fast: FIUSD integration, the Agent Pay framework, Verifiable Intent and Mastercard Merchant Cloud inside Commerce Hub. But Fiserv signed Visa's agentic framework the same day, and its own STAR and Accel networks compete with Debit Mastercard. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Fiserv's own (2Q26 results, 6 August 2026; FY2025 10-K) or come from Fiserv, Mastercard, Visa and trade press. No live Agent Pay volume through Fiserv has been reported.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Acquiring", "Largest in the US", "$4.6 trillion in 2025; every network"],
        ["Merchant Cloud", "In Commerce Hub", "August 2026; services not yet named"],
        ["Agentic", "Both networks", "Mastercard and Visa frameworks, 22 December 2025"],
        ["Verifiable Intent", "Supporter", "March 2026"],
        ["Stablecoins", "FIUSD", "Mastercard integration announced June 2025"],
        ["Debit", "STAR & Accel", "Fiserv's own networks; sale talks reported"],
        ["BNPL", "Affirm", "Pay-over-time on debit for banks"],
        ["Issuer processing", "25 of the top 50", "Mastercard and Visa programmes"],
        ["Sponsor", "Chiro Aikat", "On every Mastercard announcement"],
    ],
    "sides": {
        "neo": {"dir": "Acceptance of Mastercard at a third of US merchant volume, Merchant Cloud in Commerce Hub, Agent Pay and Verifiable Intent, FIUSD integration, and Mastercard programmes on Fiserv's processors.",
                "deals": "What it does not do yet: named Merchant Cloud services, live agentic volume, issuer-side services, Installments, fraud tools, or payouts."},
        "snb": {"dir": "STAR and Accel debit, Visa's agentic framework, Affirm, Zelle and bill pay, agentOS and OpenAI, cores and digital banking.",
                "deals": "Where they meet: every merchant on Clover and Carat, every issuer on Optis, and every dual-routed debit transaction."},
    },
    "tl": [
        ["Jun 2025", "FIUSD launched; Mastercard to integrate it"],
        ["Oct 2025", "Guidance reset; shares fall 44% in a day"],
        ["Dec 2025", "Agent Pay framework with Mastercard, and Visa's the same day"],
        ["Mar 2026", "Verifiable Intent, with Fiserv a supporter"],
        ["Jun 2026", "Takis Georgakopoulos becomes CEO"],
        ["Jul 2026", "Big banks reported in talks for STAR or Accel"],
        ["Aug 2026", "Mastercard Merchant Cloud in Commerce Hub; guidance cut again"],
        ["Oct 2026", "Digital Asset Platform live with Roughrider Coin"],
    ],
    "l": {
        "U": {"d": 1, "s": "Every merchant takes Mastercard; banks issue on both networks.",
              "gap": "Mastercard reaches Fiserv's merchants through acceptance and agentic tokens, and banks' cardholders through processing; STAR and Accel compete for their debit.",
              "neo": "Clover and enterprise merchants, issuers on Fiserv processors.", "snb": "Banks' core and digital customers, Zelle users, ISVs."},
        "L5": {"d": 0, "s": "The front doors are Fiserv's.", "gap": "Clover devices, bank referrals, international partners and developer portals are Fiserv's.",
               "neo": "None.", "snb": "Clover, bank referrals, TD, Caixa, developer portals."},
        "L4": {"d": 1, "s": "Mastercard inside Clover, enterprise and card programmes; not in cores.",
               "gap": "Clover and enterprise merchants accept Mastercard and are getting Merchant Cloud; card programmes run Mastercard and Visa; cores, digital banking and Affirm have no Mastercard role.",
               "neo": "Clover acceptance, enterprise, card programmes.", "snb": "Cores, XD, Affirm, payouts."},
        "L3": {"d": 1, "s": "Agent Pay is Mastercard's; the rest is Fiserv's or Visa's.",
               "gap": "Agent Pay and Verifiable Intent are Mastercard's; Visa's framework sits alongside; fraud, AI, embedded finance and loyalty are Fiserv's.",
               "neo": "Agent Pay, Verifiable Intent, Secure Card on File.", "snb": "Visa TAP, fraud suites, agentOS, OpenAI, Clover Capital."},
        "L2": {"d": 1, "s": "Mastercard accepted and processed; STAR and Accel compete.",
               "gap": "Mastercard rides through acquiring and issuer processing and has Merchant Cloud in Commerce Hub; STAR, Accel, Zelle and FIUSD are Fiserv's own rails.",
               "neo": "Acceptance, Merchant Cloud, issuer programmes, FIUSD integration.", "snb": "STAR, Accel, MoneyPass, Zelle, CheckFree."},
        "L1": {"d": 0, "s": "Fiserv's own scale and platforms.", "gap": "Commerce Hub is gaining Merchant Cloud; nothing else in the foundation is Mastercard's.",
               "neo": "Commerce Hub integration.", "snb": "Charters, leadership, Finxact, strategy."},
    },
    "t": {
        "1.1": {"d": 0, "why": "Fiserv's own scale.", "v": [["Scale", "No Mastercard role.", "0", ""]]},
        "1.2": {"d": 0, "why": "Charters and licences.", "v": [["Charters", "No Mastercard role.", "0", ""]]},
        "1.3": {"d": 0, "why": "Leadership.", "v": [["Leadership", "No Mastercard role.", "0", ""]]},
        "1.4": {"d": 0, "why": "Heritage.", "v": [["Heritage", "No Mastercard role.", "0", ""]]},
        "1.5": {"d": 1, "why": "Merchant Cloud is integrating into Commerce Hub.", "v": [["Commerce Hub", "Merchant Cloud coming.", "", ""], ["Finxact", "No Mastercard role.", "0", ""]]},
        "1.6": {"d": 0, "why": "Strategy and portfolio.", "v": [["Strategy", "No Mastercard role.", "0", ""]]},
        "2.1": {"d": 1, "why": "Acquiring carries every network.", "v": [["Acceptance", "All networks.", "", ""]]},
        "2.2": {"d": 3, "why": "Mastercard Merchant Cloud runs inside Commerce Hub.", "v": [
            ["Merchant Cloud", "August 2026.", "", ""], ["Named services", "Not yet announced.", "u", ""], ["Carat debit routing", "STAR and Accel.", "0", ""]]},
        "2.3": {"d": 1, "why": "Fiserv processes Mastercard and Visa programmes.", "v": [["Mastercard programmes", "Processed.", "", ""], ["Issuer services", "None announced.", "u", ""]]},
        "2.4": {"d": 0, "why": "STAR and Accel compete with Debit Mastercard.", "v": [["STAR, Accel", "Fiserv's own.", "0", ""]]},
        "2.5": {"d": 0, "why": "Zelle and bill pay are account-to-account.", "v": [["Zelle", "No card network.", "0", ""]]},
        "2.6": {"d": 1, "why": "Mastercard committed to integrate FIUSD; not live.", "v": [["Multi-Token Network", "Announced.", "u", ""]]},
        "3.1": {"d": 3, "why": "Mastercard Agent Pay and Verifiable Intent; Visa alongside.", "v": [
            ["Agent Pay", "Framework adopted.", "", ""], ["Verifiable Intent", "Supporter.", "", ""], ["Visa TAP", "Same day.", "0", ""]]},
        "3.2": {"d": 0, "why": "Fiserv's own fraud suites.", "v": [["Fraud tools", "None announced.", "u", ""]]},
        "3.3": {"d": 0, "why": "agentOS and OpenAI.", "v": [["AI", "No Mastercard role.", "0", ""]]},
        "3.4": {"d": 0, "why": "Fiserv's embedded stack.", "v": [["Embedded", "No Mastercard role.", "0", ""]]},
        "3.5": {"d": 0, "why": "Fiserv's own lending.", "v": [["Small Business Navigator", "Unconfirmed.", "u", ""]]},
        "3.6": {"d": 0, "why": "Fiserv's stored value.", "v": [["Offers", "Not used.", "0", ""]]},
        "4.1": {"d": 1, "why": "Clover accepts Mastercard and has the Agent Pay framework.", "v": [["Clover", "Acceptance.", "", ""]]},
        "4.2": {"d": 1, "why": "Enterprise merchants get Merchant Cloud.", "v": [["Enterprise", "Merchant Cloud.", "", ""]]},
        "4.3": {"d": 0, "why": "Cores.", "v": [["Cores", "No Mastercard role.", "0", ""]]},
        "4.4": {"d": 0, "why": "Pay-over-time on debit is Affirm's.", "v": [["Installments", "Not used.", "0", ""]]},
        "4.5": {"d": 1, "why": "Card programmes on both networks.", "v": [["Card programmes", "Mixed.", "", ""]]},
        "4.6": {"d": None, "why": "Payout networks not public.", "v": [["Mastercard Move", "Not announced.", "u", ""]]},
        "5.1": {"d": 0, "why": "Clover devices.", "v": [["Devices", "No Mastercard role.", "0", ""]]},
        "5.2": {"d": 0, "why": "Bank referrals.", "v": [["Referrals", "No Mastercard role.", "0", ""]]},
        "5.3": {"d": 0, "why": "International partners.", "v": [["Partners", "No Mastercard role.", "0", ""]]},
        "5.4": {"d": 0, "why": "Developers and sales.", "v": [["Developers", "No Mastercard role.", "0", ""]]},
    },
}
