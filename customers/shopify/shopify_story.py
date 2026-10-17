"""Shopify's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from shopify_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The commerce platform behind more than 14% of US e-commerce, read through payments, as five discs that stack "
       "into one platform, from $378.4 billion of GMV at the bottom to the admin, the Shop app and AI channels at the "
       "top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it "
       "light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep "
       "Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("mer", "Merchants", "store"),
    ("ent", "Enterprise brands", "building-2"),
    ("retail", "Store owners", "house"),
    ("shop", "Shoppers", "user-round"),
    ("biz", "Business buyers", "briefcase-business"),
    ("dev", "Developers & AI builders", "code-xml"),
]
USERS_DESC = ("Six kinds of user: the millions of merchants who run their business on Shopify, the enterprise brands on "
              "Plus, store owners using POS, the shoppers who check out with Shop Pay, business buyers on B2B stores, "
              "and the developers and AI builders working with Catalog and UCP.")

WHO = {"mer": "A merchant", "ent": "An enterprise brand", "retail": "A store owner", "shop": "A shopper",
       "biz": "A business buyer", "dev": "A developer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "launch", "who": "mer", "name": "Start selling online",
     "why": "Open a store, pick a plan, take cards with Shopify Payments and grow with apps.",
     "steps": [("5.1", "admin", "Set up in the admin"), ("4.1", "plans", "Choose a plan"),
               ("2.1", "shoppayments", "Turn on Shopify Payments"), ("5.3", "appstore", "Add apps")]},
    {"id": "checkout", "who": "shop", "name": "Check out fast",
     "why": "Shop Pay remembers the card; Affirm spreads the cost.",
     "steps": [("5.2", "shopapp", "Find it in the Shop app"), ("2.2", "shoppay", "Pay with Shop Pay"),
               ("2.3", "installments", "Or split it with Shop Pay Installments")]},
    {"id": "instore", "who": "retail", "name": "Sell in my shop",
     "why": "POS on the same back office, with Tap to Pay and the same payouts.",
     "steps": [("2.4", "pos", "Ring it up on POS"), ("2.4", "taptopay", "Take a tap on the phone"),
               ("2.1", "shoppayments", "Settle through Shopify Payments")]},
    {"id": "global", "who": "ent", "name": "Sell across borders",
     "why": "Local prices and methods, Global-e for duties, payouts in more currencies.",
     "steps": [("2.5", "markets", "Open new markets"), ("2.1", "localmethods", "Offer local methods"),
               ("2.5", "multicurrency", "Get paid in more currencies")]},
    {"id": "money", "who": "mer", "name": "Manage and borrow money",
     "why": "Payouts land in Balance, spending goes on Visa cards, growth is funded by Capital.",
     "steps": [("4.5", "balance", "Hold sales in Shopify Balance"), ("4.5", "balancecard", "Spend with the Balance card"),
               ("4.5", "credit", "Use Shopify Credit"), ("4.4", "capital", "Take Shopify Capital")]},
    {"id": "agent", "who": "shop", "name": "Buy through an AI assistant",
     "why": "Products syndicated to AI channels, bought in Copilot or ChatGPT, approved through Shop.",
     "steps": [("5.4", "aichannels", "Find it in an AI chat"), ("3.2", "copilot", "Buy in Copilot with Shop Pay"),
               ("3.2", "chatgpt", "Or in ChatGPT"), ("3.2", "agentapprove", "Approve my agent's purchase")]},
    {"id": "b2b", "who": "biz", "name": "Buy wholesale",
     "why": "B2B catalogs with cards on file or ACH.",
     "steps": [("4.3", "b2b", "Order from a B2B catalog"), ("4.3", "ach", "Pay by ACH")]},
    {"id": "dev", "who": "dev", "name": "Build agentic shopping",
     "why": "Catalog to find products, UCP and Checkout Kit to buy them.",
     "steps": [("3.3", "catalog", "Search Shopify Catalog"), ("3.2", "ucp", "Speak UCP"),
               ("3.3", "checkoutkit", "Embed checkout"), ("2.6", "usdc", "Accept USDC")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Acceptance at every Shopify checkout, Mastercard cards in Shop Pay, the 2020 Digital Doors programme and a seat among UCP's endorsers.",
     "steps": [("2.1", "shoppayments", "Mastercard accepted through Shopify Payments"), ("2.2", "shoppay", "Mastercard cards in Shop Pay"),
               ("2.4", "pos", "Mastercard taps in store"), ("5.3", "digitaldoors", "Digital Doors, 2020"),
               ("3.2", "ucp", "Endorser of UCP")]},
    {"id": "mcnext", "who": "mc", "name": "Where agent payments, fraud tools and cards could land",
     "why": "Where Shopify has needs and Mastercard is not yet in: Agent Pay behind Shop Pay in AI channels, agent identity beside Visa's protocol, tools against card testing, a second network for Shopify's own cards, and cross-border and B2B volume.",
     "steps": [("3.2", "copilot", "Agent Pay tokens behind Shop Pay in agents"), ("3.2", "visatap", "Agent identity beside Visa's protocol"),
               ("3.1", "fraud", "Fraud and dispute tools against card testing"), ("4.5", "balancecard", "A Mastercard option for Balance and Credit"),
               ("2.5", "markets", "Cross-border and FX"), ("4.3", "b2b", "Virtual cards for B2B buyers")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Shopify's map",
    "title": "Accepted at every checkout, but Shopify's own cards and agent work lean to Visa",
    "lead": "Every Shopify Payments, Shop Pay and POS checkout takes Mastercard, and Mastercard cards sit in Shop Pay's 250 million+ wallets. But Shopify's own cards, Balance and Credit, are Visa from Celtic Bank, Shopify gave feedback on Visa's agent protocol, and instalments, USDC, Klarna and local methods run off the card networks. Mastercard's public work with Shopify is Digital Doors in 2020 and an endorsement of UCP. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Shopify's own (Q2 2026 results, 5 August 2026; FY2025 10-K) or from its help centre, Editions and partners; Q2 2026 operating metrics are from a call summary ⚠. Shopify does not publish a network split.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Acceptance", "Every network", "Shopify Payments, 41 countries"],
        ["Shop Pay", "Visa, Mastercard, Amex", "250m+ shoppers"],
        ["Balance card", "Visa", "Celtic Bank, powered by Stripe"],
        ["Shopify Credit", "Visa", "Celtic Bank"],
        ["Instalments", "Affirm", "US, Canada, UK"],
        ["Agent identity", "Visa", "Trusted Agent Protocol, Oct 2025"],
        ["UCP", "Endorser", "Mastercard, Visa and Amex, Jan 2026"],
        ["Stablecoins", "USDC on Base", "Coinbase and Stripe, Jun 2025"],
    ],
    "sides": {
        "neo": {"dir": "Acceptance at every Shopify checkout and in store, Mastercard cards saved in Shop Pay, Digital Doors in 2020, and a seat among UCP's endorsers.",
                "deals": "What it does not do: Shopify's own cards, agent identity, instalments, stablecoins, or a named role in UCP's payment handlers."},
        "snb": {"dir": "Visa cards for Balance and Credit and Visa's agent protocol, Affirm and Klarna, USDC with Coinbase and Stripe, ACH and local methods, and Stripe and PayPal as processors.",
                "deals": "Where they meet: every card checkout, and agent-made purchases through Shop Pay that will need a network token."},
    },
    "tl": [
        ["Jul 2020", "Mastercard Digital Doors with Shopify in the US"],
        ["2023", "Shopify Credit on Visa ⚠ date"],
        ["Feb 2025", "Affirm partnership extended to Canada"],
        ["Jun 2025", "USDC on Base in Shopify Payments"],
        ["Sep 2025", "ChatGPT Instant Checkout announced"],
        ["Oct 2025", "Visa Trusted Agent Protocol; Shopify a partner"],
        ["Dec 2025", "Agentic Storefronts; Shop Pay Installments in the UK"],
        ["Jan 2026", "UCP with Google; Mastercard among endorsers"],
        ["Spring 2026", "Copilot checkout with Shop Pay; Shop Pay on any platform"],
        ["Aug 2026", "Q2 2026: GMV $115.6bn"],
    ],
    "l": {
        "U": {"d": 1, "s": "Shoppers pay with Mastercard; merchants' Shopify cards are Visa.",
              "gap": "Any shopper can pay with Mastercard; merchants who take Balance or Credit cards carry Visa.",
              "neo": "Shoppers with Mastercard cards in Shop Pay.", "snb": "Balance and Credit card holders, Affirm and USDC users."},
        "L5": {"d": 1, "s": "Front doors are Shopify's; Digital Doors was a 2020 Mastercard programme.", "gap": "Admin, Shop app, apps and AI channels are Shopify's; Mastercard's Digital Doors is the one Mastercard programme with Shopify on record.",
               "neo": "Digital Doors, Mastercard cards in the Shop app.", "snb": "Admin, App Store, partners, AI channels."},
        "L4": {"d": 0, "s": "Shopify's own cards are Visa.", "gap": "Balance and Credit are Visa from Celtic Bank; Capital and ACH are off the networks; only merchant-solutions card fees touch Mastercard.",
               "neo": "Card fees in merchant solutions, cards on file in B2B.", "snb": "Balance Visa card, Shopify Credit Visa, Capital, ACH."},
        "L3": {"d": 0, "s": "Visa has the agent-identity link; UCP names no network.", "gap": "Shopify gave feedback on Visa's agent protocol; Mastercard endorses UCP but is not a payment handler; fraud tools name no network.",
               "neo": "UCP endorsement, cards saved in Shop Pay for agent checkout.", "snb": "Visa Trusted Agent Protocol, Stripe's ACP, Catalog, Sidekick."},
        "L2": {"d": 1, "s": "Mastercard accepted everywhere; much new volume is off-network.", "gap": "Shopify Payments, Shop Pay and POS take every network; instalments, Klarna, USDC and local methods do not use cards.",
               "neo": "Acceptance online and in store, Shop Pay cards.", "snb": "Affirm, Klarna, USDC, local schemes, Stripe and PayPal processing."},
        "L1": {"d": 0, "s": "Shopify's own scale and partners.", "gap": "Nothing in the foundation is Mastercard's beyond the network fees Shopify pays.", "neo": "Network fees.", "snb": "GMV, leadership, Stripe, Fifth Third and Celtic Bank."},
    },
    "t": area_lens(LAYERS),
}
