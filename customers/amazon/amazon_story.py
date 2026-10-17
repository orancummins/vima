"""Amazon's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from amazon_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The world's largest online store, read through payments, as five discs that stack into one platform, from "
       "$716.9 billion of sales at the bottom to the app, Alexa+ and partners' sites at the top. Click the stack to open "
       "it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined "
       "in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("shop", "Shoppers", "user-round"),
    ("prime", "Prime members", "gift"),
    ("seller", "Sellers", "store"),
    ("mer", "Merchants using Amazon Pay", "plug"),
    ("biz", "Business buyers", "briefcase-business"),
    ("dev", "Developers & AI builders", "code-xml"),
]
USERS_DESC = ("Six kinds of user: shoppers in more than 20 countries, Prime members, the sellers who ship 61% of units, "
              "merchants who add Amazon Pay or Buy with Prime to their own sites, business buyers, and the developers "
              "building agents on AWS.")

WHO = {"shop": "A shopper", "prime": "A Prime member", "seller": "A seller", "mer": "A merchant",
       "biz": "A business buyer", "dev": "A developer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "shop", "who": "shop", "name": "Shop on Amazon",
     "why": "The everyday loop: the app, the store, any card, and instalments if wanted.",
     "steps": [("5.1", "app", "Open the app"), ("4.1", "onlinestores", "Buy from Amazon"), ("2.5", "accept", "Pay with any card"),
               ("2.4", "affirm", "Or spread it with Affirm")]},
    {"id": "prime", "who": "prime", "name": "Get the most from Prime",
     "why": "Prime, the Prime Visa and Prime checkout on other sites.",
     "steps": [("3.1", "prime", "Join Prime"), ("2.2", "primevisa", "Earn 5% with the Prime Visa"), ("3.2", "bwp", "Use Prime on a brand's own site")]},
    {"id": "agent", "who": "shop", "name": "Let an agent buy for me",
     "why": "Alexa for Shopping watches prices and buys; Buy for Me checks out on other sites.",
     "steps": [("5.2", "alexa", "Ask Alexa+"), ("3.3", "rufus", "Set Auto-Buy"), ("3.3", "buyforme", "Buy for Me on a brand's site")]},
    {"id": "seller", "who": "seller", "name": "Sell on Amazon",
     "why": "The marketplace, ads, seller loans and supply-chain services.",
     "steps": [("4.2", "marketplace", "List on the marketplace"), ("4.3", "ads", "Advertise"), ("4.2", "lending", "Borrow"),
               ("4.2", "supplychain", "Ship with Amazon")]},
    {"id": "merchant", "who": "mer", "name": "Add Amazon to my checkout",
     "why": "Amazon Pay and Buy with Prime on a merchant's own site.",
     "steps": [("5.3", "partners", "Install through Shopify or Stripe"), ("2.1", "amazonpay", "Offer Amazon Pay"), ("3.2", "bwp", "Add Buy with Prime")]},
    {"id": "india", "who": "shop", "name": "Pay with Amazon in India",
     "why": "UPI, the wallet, the ICICI card, Pay Later and deposits.",
     "steps": [("4.6", "upi", "Pay by UPI"), ("4.6", "wallet", "Top up Amazon Pay Balance"), ("4.6", "icici", "Use the Amazon Pay ICICI card"),
               ("4.6", "paylater", "Borrow with Pay Later")]},
    {"id": "biz", "who": "biz", "name": "Buy for a business",
     "why": "Amazon Business and its American Express cards.",
     "steps": [("4.5", "business", "Buy on Amazon Business"), ("2.2", "bizamex", "Pay with the business card")]},
    {"id": "dev", "who": "dev", "name": "Build an agent that pays",
     "why": "AgentCore, its USDC wallets and Visa's tools on AWS.",
     "steps": [("3.4", "agentcore", "Build on AgentCore"), ("2.6", "agentcorepay", "Give it a USDC wallet"),
               ("3.4", "visaaws", "Use Visa's agentic blueprints"), ("5.3", "awsmkt", "Find tools in AWS Marketplace")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Acceptance everywhere, the Japan co-brand, the Mexico prepaid card and Mastercard cards saved in Amazon Pay.",
     "steps": [("2.5", "accept", "Mastercard accepted in every store"), ("2.3", "japanmc", "Amazon Mastercard in Japan"),
               ("2.3", "recargable", "Amazon Recargable in Mexico"), ("2.1", "amazonpay", "Mastercard cards on file")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, co-brands and B2B cards could land",
     "why": "Where Amazon has needs and Mastercard is not yet in: Agent Pay beside Visa on AWS, a card bridge for AgentCore's USDC wallets, tokens for Buy for Me, co-brands still open, and virtual cards for Amazon Business.",
     "steps": [("3.4", "visaaws", "Agent Pay at parity with Visa on AWS"), ("2.6", "agentcorepay", "Agent Pay for Machines beside USDC"),
               ("3.3", "buyforme", "Agentic tokens for Buy for Me"), ("2.3", "canbra", "Co-brands in Canada, Brazil and Mexico"),
               ("4.5", "business", "Virtual cards for Amazon Business")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Amazon's map",
    "title": "Accepted everywhere, but Visa holds the cards that matter",
    "lead": "Every Amazon store takes Mastercard, and Mastercard carries the Japan co-brand and the Mexico prepaid card. Visa holds the co-brands in the US, the UK (taken from Mastercard in 2024) and Germany, signed a global agreement with Amazon in 2022, and is the only network inside AWS's agentic tools. Synchrony's closed-loop Store Card and Affirm's instalments run off the networks, and AgentCore's agent wallets use USDC. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Amazon's own (Q2 2026 results, 30 July 2026; FY2025 10-K) or from issuers, Synchrony, Affirm, AWS and press. Amazon does not publish a network split. Canada, Brazil and India card networks are unconfirmed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["US co-brand", "Visa", "Prime Visa, from Chase"],
        ["UK co-brand", "Mastercard to Visa", "Barclaycard since August 2024"],
        ["Germany", "Visa", "Zinia, from August 2024"],
        ["Japan", "Mastercard", "SMBC Card since 2014"],
        ["Mexico", "Mastercard prepaid", "Banorte, since 2018"],
        ["Store Card", "Closed loop", "Synchrony, extended 2025"],
        ["Agentic on AWS", "Visa", "December 2025; 'multi-network' to come"],
        ["Agent wallets", "USDC", "Coinbase and Stripe, May 2026"],
    ],
    "sides": {
        "neo": {"dir": "Acceptance in every store, the Japan co-brand, the Mexico prepaid card, and Mastercard cards saved in Amazon's wallets.",
                "deals": "What it does not do: US, UK or German co-brands, agentic tools on AWS, agent wallets, instalments or B2B cards."},
        "snb": {"dir": "Visa co-brands in the US, UK and Germany and Visa's agentic tools on AWS, Synchrony's closed-loop cards, Affirm, American Express for business, UPI in India, and USDC through Coinbase and Stripe.",
                "deals": "Where they meet: every card checkout, and agent-made purchases that will need a network."},
    },
    "tl": [
        ["Feb 2014", "Amazon Mastercard in Japan with SMBC Card"],
        ["Mar 2018", "Amazon Recargable prepaid Mastercard in Mexico"],
        ["Nov 2021", "Amazon UK to stop taking Visa credit; Mastercard stays"],
        ["Feb 2022", "Global Amazon–Visa agreement"],
        ["Aug 2024", "UK co-brand moves to Visa with Barclays; Germany to Zinia"],
        ["Apr 2025", "Buy for Me beta"],
        ["Dec 2025", "Visa and AWS agentic commerce"],
        ["May 2026", "AgentCore Payments preview with USDC"],
        ["Jun 2026", "Amazon One palm payments end"],
    ],
    "l": {
        "U": {"d": 1, "s": "Shoppers pay with Mastercard; Amazon's own cards are mostly Visa.",
              "gap": "Every shopper can pay with Mastercard; Japanese and Mexican card holders carry it; US, UK and German co-brand holders carry Visa.",
              "neo": "Shoppers with Mastercard cards, Japan and Mexico card holders.", "snb": "Prime Visa, Barclaycard and German card holders, Store Card holders, UPI users."},
        "L5": {"d": 0, "s": "The front doors are Amazon's.", "gap": "App, Alexa+ and partner sites are Amazon's; Visa is listed in AWS Marketplace, Mastercard is not.",
               "neo": "None.", "snb": "App, Alexa+, partners, Visa in AWS Marketplace."},
        "L4": {"d": 1, "s": "Stores take Mastercard; the other lines do not use it.", "gap": "Online and physical stores accept every network; the marketplace, ads, AWS, Amazon Business and India have no Mastercard role.",
               "neo": "Card acceptance in stores.", "snb": "UPI and Axio in India, American Express for business."},
        "L3": {"d": 1, "s": "Buy for Me uses any saved card; Visa is inside AWS.", "gap": "Agent purchases use the customer's card; AWS's only agentic network partner is Visa.",
               "neo": "Saved Mastercard cards in Buy for Me.", "snb": "Visa Intelligent Commerce, AgentCore, payment cryptography."},
        "L2": {"d": 1, "s": "Mastercard in Japan, Mexico and acceptance; Visa in the big co-brands.", "gap": "Visa has the US, UK and German co-brands; Mastercard has Japan and Mexico; Store Card, Affirm and USDC are off the networks.",
               "neo": "Acceptance, Japan co-brand, Mexico prepaid.", "snb": "Prime Visa, Barclaycard, Zinia, Synchrony, Affirm, USDC."},
        "L1": {"d": 0, "s": "Amazon's own scale and entities.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Sales, leadership, payments entities, AI bets."},
    },
    "t": area_lens(LAYERS),
}
