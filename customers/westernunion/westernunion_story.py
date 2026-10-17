"""Western Union's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from westernunion_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The world's best-known remitter as five discs that stack into one, from $4.05 billion of revenue, licences in "
       "almost every US state and about 360,000 active locations at the bottom to agents, the app and partner banks at "
       "the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it "
       "light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep "
       "Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("send", "Senders", "user-round"),
    ("recv", "Receivers", "users-round"),
    ("agent", "Agents & retailers", "store"),
    ("ptnr", "Banks, wallets & exchanges", "network"),
    ("svc", "Bill payers & travellers", "receipt-text"),
    ("crypto", "Digital-dollar users", "coins"),
]
USERS_DESC = ("Six kinds of user: the migrants and families who send money, the people who receive it, the agents and "
              "retailers who serve them, the banks, wallets and exchanges that plug in, people paying bills or buying "
              "travel money, and the new users of digital dollars.")

WHO = {"send": "A sender", "recv": "A receiver", "agent": "An agent", "ptnr": "A partner",
       "svc": "A customer", "crypto": "A digital-dollar user"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "sendcash", "who": "send", "name": "Send cash from a store",
     "why": "Still most of the revenue: cash in at an agent, checked, and collected or paid into an account abroad.",
     "steps": [("5.1", "agents", "Walk into an agent"), ("2.1", "retail", "Send cash"), ("3.1", "compliance", "Checked for fraud and sanctions"),
               ("4.1", "cmt", "Paid out in about 130 currencies")]},
    {"id": "senddigital", "who": "send", "name": "Send from the app",
     "why": "Branded Digital: 43% of transfers, paid by card or bank account, with points on every send.",
     "steps": [("5.2", "app", "Open the app"), ("3.2", "kyc", "Verify identity"), ("2.2", "cardfund", "Pay by card or bank account"),
               ("2.4", "a2a", "Deliver to a bank account or wallet"), ("3.4", "rewards", "Earn points")]},
    {"id": "tocard", "who": "recv", "name": "Get money on a card",
     "why": "Push-to-card on Mastercard Send and Visa Direct, or into a Western Union prepaid card.",
     "steps": [("2.3", "mcsend", "Receive on a Mastercard debit card"), ("2.3", "visadirect", "Or on a Visa debit card"),
               ("2.6", "netspend", "Or load a Netspend Prepaid Mastercard")]},
    {"id": "stable", "who": "crypto", "name": "Hold and spend digital dollars",
     "why": "Stablecard: receive a transfer, hold it as USDPT, spend it on a Visa card.",
     "steps": [("2.2", "digital", "Receive a transfer"), ("2.5", "usdpt", "Hold it as USDPT"), ("2.6", "stablecard", "Spend with Stablecard")]},
    {"id": "offramp", "who": "ptnr", "name": "Cash out digital assets",
     "why": "The Digital Asset Network links exchanges such as Bybit to Western Union's payout network.",
     "steps": [("4.5", "bybit", "Sell USDPT on an exchange"), ("2.5", "dan", "Route through the Digital Asset Network"),
               ("2.1", "retail", "Collect cash at an agent")]},
    {"id": "agentsettle", "who": "agent", "name": "Settle with Western Union around the clock",
     "why": "USDPT lets agents settle 24/7 rather than on bank business days.",
     "steps": [("5.1", "agents", "Run a Western Union counter"), ("3.3", "treasury", "Settle the day's transfers"),
               ("2.5", "usdpt", "Settle in USDPT")]},
    {"id": "bills", "who": "svc", "name": "Pay a bill or buy travel money",
     "why": "Consumer Services, up 32% in 2025.",
     "steps": [("4.2", "billpay", "Pay a bill"), ("4.4", "moneyorder", "Buy a money order"), ("4.3", "travel", "Buy travel money at Eurochange")]},
    {"id": "intermex", "who": "agent", "name": "Join two US retail networks",
     "why": "The Intermex deal adds about 6 million customers and Latin American corridors, once regulators allow it.",
     "steps": [("1.5", "intermex", "Close the Intermex deal"), ("5.1", "agents", "Combine the agents"), ("2.1", "retail", "Serve Latin American corridors")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mastercard Send push-to-card, the Netspend Prepaid Mastercard and card-funded sends; Cross-Border Services payouts left with Business Solutions in 2023.",
     "steps": [("2.3", "mcsend", "Mastercard Send push-to-card"), ("2.6", "netspend", "Netspend Prepaid Mastercard"),
               ("2.2", "cardfund", "Mastercard cards fund transfers"), ("1.5", "wubs", "Cross-Border Services payouts, until 2023")]},
    {"id": "mcnext", "who": "mc", "name": "Where Move, stablecoin cards and Intermex could land",
     "why": "Where Western Union has needs and Mastercard is not yet in: Move to wallets and cards, stablecoin cards beyond Stablecard's Visa markets, wallet cards, services for Intermex, fraud tools and card-linked offers.",
     "steps": [("2.3", "mcsend", "Mastercard Move to more wallets and corridors"), ("2.6", "stablecard", "Stablecoin cards where Stablecard is not"),
               ("2.6", "vigo", "Cards for the wallets"), ("1.5", "intermex", "Card and fraud services for Intermex"),
               ("3.1", "compliance", "Scam and fraud scoring"), ("3.4", "rewards", "Card-linked offers")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Western Union's map",
    "title": "An old Send partner, while the stablecoin card went to Visa",
    "lead": "Mastercard is in Western Union through Mastercard Send push-to-card (since 2021), the Western Union Netspend Prepaid Mastercard and the cards that fund digital sends. Visa has the newer public wins: Visa Direct, the Prepaid Visa Card, a European debit card and, in August 2026, Stablecard, the card for Western Union's USDPT stablecoin. Most money still moves as cash, to bank accounts and wallets, and now on Solana. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Western Union's own releases and filings, with Mastercard, Visa and trade press. Western Union does not publish its network split.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Push-to-card", "Mastercard Send and Visa Direct", "Send since 2021; Visa Direct since 2019"],
        ["Prepaid", "Both", "Netspend Mastercard; Prepaid Visa"],
        ["Stablecoin card", "Visa", "Stablecard with Rain, 37 markets"],
        ["Stablecoin", "USDPT on Solana", "Anchorage issues; live May 2026"],
        ["Wallets", "Network not published", "Vigo Money, Brazil, Argentina"],
        ["Payout", "Cash, accounts, wallets", "Most of it off the card networks"],
        ["Intermex", "Pending", "California and HSR still open"],
        ["2026", "Outlook cut", "Adjusted EPS $1.25–1.35"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard Send push-to-card in the US and Europe, the Netspend Prepaid Mastercard, and Mastercard cards that fund digital transfers; before 2023, Cross-Border Services payouts.",
                "deals": "What it does not do: the stablecoin card, wallet cards, Move, fraud tools or offers."},
        "snb": {"dir": "Visa Direct, the Prepaid Visa Card, the European debit card and Stablecard; cash, bank and wallet payout; USDPT on Solana with Anchorage, Fireblocks and Bybit.",
                "deals": "Where they meet: every card-funded send and every payout to a card."},
    },
    "tl": [
        ["2011", "Global agreement with Mastercard ⚠"],
        ["Jun 2019", "Visa Direct agreement"],
        ["Nov 2021", "Mastercard Send added"],
        ["Aug 2022", "Visa Direct extended to the US"],
        ["Jul 2023", "Business Solutions sold"],
        ["Aug 2025", "Intermex deal agreed"],
        ["Oct 2025", "USDPT and Digital Asset Network announced"],
        ["Nov 2025", "Beyond strategy"],
        ["May 2026", "USDPT live on Solana"],
        ["Aug 2026", "Stablecard on Visa; Intermex held up in California"],
        ["Oct 2026", "Intermex competition filing redone"],
    ],
    "l": {
        "U": {"d": 1, "s": "Some receivers and senders use Mastercard; most use cash, accounts and wallets.",
              "gap": "Card receivers and card-funded senders touch Mastercard; Stablecard users, wallet users and cash customers mostly do not.",
              "neo": "Mastercard Send receivers, Netspend cardholders, card-funded senders.", "snb": "Cash customers, Stablecard users, Visa Direct receivers."},
        "L5": {"d": 0, "s": "The front doors are Western Union's.", "gap": "Agents, stores, the app and partners are its own.",
               "neo": "None beyond card acceptance in the app.", "snb": "Agents, stores, app, partners."},
        "L4": {"d": 0, "s": "Mastercard reaches the lines only through payouts.",
               "gap": "Money transfer pays out to cards on both networks; bill pay, travel money, money orders and digital assets do not run on Mastercard.",
               "neo": "Card payouts in money transfer.", "snb": "Bill pay, travel money, money orders, exchanges."},
        "L3": {"d": 0, "s": "Western Union runs its own services.", "gap": "Compliance, identity, treasury, rewards and the partner platform are its own; no Mastercard service is named.",
               "neo": "None found.", "snb": "Own fraud models, USDPT settlement, Rewards."},
        "L2": {"d": 1, "s": "Shared with Visa, around cash, accounts and a stablecoin.",
               "gap": "Mastercard has Send and the Netspend card; Visa has Visa Direct, Prepaid Visa and Stablecard; cash, accounts, wallets and USDPT are on neither.",
               "neo": "Mastercard Send, Netspend Prepaid Mastercard, card funding.", "snb": "Visa Direct, Stablecard, USDPT, cash."},
        "L1": {"d": 0, "s": "Western Union's own scale and licences.", "gap": "Nothing in the foundation is Mastercard's.",
               "neo": "None.", "snb": "Licences, strategy, Intermex."},
    },
    "t": area_lens(LAYERS),
}
