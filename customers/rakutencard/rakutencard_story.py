"""Rakuten Card's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from rakutencard_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Japan's biggest card issuer as five discs that stack into one platform, from 34 million cards and ¥26.5 trillion "
       "of spend at the bottom to the Rakuten Card app, the Rakuten ecosystem and partner banks at the top. Click the stack "
       "to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Cardholders", "user-round"),
    ("prem", "Premium cardholders & travellers", "plane"),
    ("shop", "Rakuten shoppers", "store"),
    ("bank", "Bank & securities customers", "landmark"),
    ("sme", "Sole proprietors & SMEs", "briefcase"),
    ("corp", "Large companies", "factory"),
    ("merch", "Merchants", "receipt-text"),
]
USERS_DESC = ("Seven kinds of user around 34 million cards: everyday cardholders, premium cardholders and travellers, "
              "Rakuten shoppers, Rakuten Bank and Securities customers, sole proprietors and SMEs, large companies, and "
              "the merchants Rakuten Card acquires.")

WHO = {"con": "A cardholder", "prem": "A premium cardholder", "shop": "A Rakuten shopper", "bank": "A Rakuten Bank customer",
       "sme": "A small business", "corp": "A large company", "merch": "A merchant"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Pay every day with Rakuten Card",
     "why": "The everyday loop: pick one of four brands, tap with Apple Pay, earn points, check it in the app.",
     "steps": [("2.1", "classic", "Choose Visa, Mastercard, JCB or Amex"), ("2.6", "applepay", "Tap with Apple Pay"),
               ("3.3", "points", "Earn 1% in Rakuten Points"), ("5.1", "app", "Check it in the app"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "shop", "who": "shop", "name": "Shop across the Rakuten ecosystem",
     "why": "Ichiba, Travel and Rakuten Pay, all funded by the card and paid back in points.",
     "steps": [("5.2", "ichiba", "Shop on Rakuten Ichiba or Travel"), ("2.7", "revolving", "Spread the cost in instalments"),
               ("2.6", "paycharge", "Top up Rakuten Pay"), ("3.3", "points", "Collect points")]},
    {"id": "travel", "who": "prem", "name": "Travel on a premium card",
     "why": "Premium, Black and ANA cards, the tiers where Mastercard is strongest.",
     "steps": [("2.2", "premium", "Hold a Premium Card"), ("2.2", "black", "Move up to the Black Card"), ("2.3", "ana", "Earn ANA miles")]},
    {"id": "bank", "who": "bank", "name": "Bank, card and invest in one group",
     "why": "Rakuten Bank now owns the card; settling from it raises balances 4.3 times.",
     "steps": [("4.4", "rakutenbank", "Open a Rakuten Bank account"), ("3.4", "banklink", "Settle the card from it"),
               ("4.4", "securities", "Invest with Rakuten Securities"), ("2.3", "mizuhocard", "Or bank with Mizuho")]},
    {"id": "ask", "who": "con", "name": "Ask about my spending",
     "why": "The AI agent in Rakuten Card Lite, and AI in chat support.",
     "steps": [("5.1", "lite", "Open Rakuten Card Lite"), ("3.2", "aiagent", "Ask the AI agent"), ("3.2", "chatai", "Get help in chat")]},
    {"id": "sme", "who": "sme", "name": "Run business spend on a card",
     "why": "The Business Card and the new Business Card Platinum with UPSIDER, both on Visa.",
     "steps": [("4.1", "bizcard", "Add a Business Card as a sole proprietor"), ("4.1", "bizplat", "Move to Business Platinum"),
               ("3.3", "points", "Earn points on Ichiba and Travel")]},
    {"id": "corp", "who": "corp", "name": "Equip a large company",
     "why": "The Rakuten Corporate Card, launched 1 October 2026.",
     "steps": [("5.3", "partners", "Come through the Mizuho relationship"), ("4.1", "corporate", "Issue Rakuten Corporate Cards")]},
    {"id": "merch", "who": "merch", "name": "Take card payments",
     "why": "Rakuten Card acquires merchants, and plans shared acquiring with Mizuho's card companies.",
     "steps": [("2.5", "acquiring", "Accept cards through Rakuten Card"), ("3.1", "fraud", "Share fraud controls")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Principal membership, Mastercard cards on most tiers, Mastercard-only co-brands, acquiring, and the parent's debit card.",
     "steps": [("2.4", "netmc", "Principal member of Mastercard"), ("2.2", "black", "Black Card without Visa"),
               ("2.3", "alpen", "Mastercard-only co-brands"), ("2.5", "acquiring", "Mastercard acquiring"),
               ("4.4", "rakutenbank", "Rakuten Bank debit on Mastercard")]},
    {"id": "mcnext", "who": "mc", "name": "Where corporate cards, agents and tokens could land",
     "why": "Where Rakuten Card has needs and Mastercard is not yet in: the new Corporate Card, agentic payments for Rakuten's AI agents, tokens and passkeys against number theft, and a debit-plus-credit offer under Rakuten Bank.",
     "steps": [("4.1", "corporate", "Commercial cards for the Corporate Card"), ("3.2", "aiagent", "Agent Pay for Rakuten's agents"),
               ("3.1", "fraud", "Tokens and passkeys against number theft"), ("3.4", "banklink", "Debit and credit together under Rakuten Bank"),
               ("2.2", "black", "Premium travel benefits")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Rakuten Card's map",
    "title": "One of four brands at Japan's biggest issuer, with Visa taking the new launches",
    "lead": "Rakuten Card is a principal member of both Mastercard and Visa and also issues JCB and Amex, on 34 million cards. Mastercard is on most consumer tiers, alone on the Alpen and My Color Selection cards, and on the Black Card where Visa is absent. It is acquired by Rakuten Card and runs the debit card of Rakuten Bank, the owner since 1 October 2026. But Visa looks like the majority choice and has every new programme of 2024–26. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Rakuten's own (Q2 2026 presentation; reorganisation agreement, 20 May 2026; business-card release, 30 September 2026). Rakuten Card's site could not be read, so brands per card rest partly on secondary sources, and no network split is published.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Consumer cards", "Four brands", "Visa, Mastercard, JCB, Amex; 34.3 million cards"],
        ["Mix", "Visa ahead", "About 55.5% choose Visa ⚠"],
        ["Black Card", "No Visa", "Mastercard, JCB or Amex ⚠"],
        ["Co-brands", "Split", "Alpen on Mastercard; Mizuho on Visa"],
        ["Business cards", "Visa", "Business Platinum, 1 October 2026"],
        ["Apple Pay", "Mastercard first", "2016; Visa in 2021"],
        ["Acquiring", "Mastercard since 2011 ⚠", "Shared acquiring with Mizuho planned"],
        ["Parent's debit", "Mastercard", "Rakuten Bank, since 2020"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard cards on most tiers, the Black Card, the Alpen and My Color Selection cards, acquiring, Rakuten Bank's debit and the 2014 US card ⚠.",
                "deals": "What it does not have: the new co-brands and business cards, brand campaigns, AI, or the Corporate Card decision so far."},
        "snb": {"dir": "Visa as the majority choice, the Mizuho and business cards and 2026 campaigns; JCB on the bank card; Amex since 2018; Rakuten's own points, wallet and AI.",
                "deals": "Where they meet: the standard, Gold, Premium and ANA cards, where every brand is offered."},
    },
    "tl": [
        ["Dec 2011", "Mastercard acquiring begins ⚠"],
        ["Apr 2014", "Rakuten Rewards MasterCard in the US"],
        ["Oct 2016", "Apple Pay for Mastercard and JCB"],
        ["Sep 2018", "American Express cards"],
        ["May 2020", "Rakuten Bank debit on Mastercard"],
        ["Jul 2021", "Visa on Apple Pay"],
        ["Dec 2024", "Mizuho takes 14.99%; Mizuho Rakuten Card on Visa"],
        ["Feb 2026", "AI agent in Rakuten Card Lite"],
        ["Sep 2026", "Visa Apple Pay cashback"],
        ["Oct 2026", "Under Rakuten Bank; Business Platinum on Visa"],
    ],
    "l": {
        "U": {"d": 1, "s": "Some cardholders carry Mastercard; most appear to choose Visa ⚠.",
              "gap": "Every consumer tier but Academy offers Mastercard; business users are on Visa.",
              "neo": "Mastercard cardholders, Black and Alpen holders, Rakuten Bank debit users.", "snb": "Visa majority, JCB and Amex holders, business cardholders."},
        "L5": {"d": 0, "s": "The front doors are Rakuten's.", "gap": "Apps, the ecosystem and partner banks are Rakuten's or partners'.", "neo": "None.", "snb": "Rakuten Card app, Rakuten Pay, Mizuho channel."},
        "L4": {"d": 1, "s": "Business cards on Visa; the parent's debit on Mastercard.", "gap": "The Business Card and Business Platinum are Visa; the Corporate Card network is not stated.",
               "neo": "Rakuten Bank debit, the 2014 US card ⚠.", "snb": "Business cards on Visa, loans, securities."},
        "L3": {"d": 0, "s": "Fraud, AI and points are Rakuten's own.", "gap": "No Mastercard service is named in fraud, AI or loyalty.",
               "neo": "None public.", "snb": "Own AI agent, Rakuten Points, Mizuho fraud sharing, Visa Business Offers."},
        "L2": {"d": 1, "s": "Mastercard is one of four brands, alone on a few cards.", "gap": "Visa holds the new launches; Mastercard keeps the Black Card, co-brands and acquiring.",
               "neo": "Mastercard cards, Alpen and My Color Selection, acquiring.", "snb": "Visa, JCB and Amex cards, Rakuten Pay and Edy."},
        "L1": {"d": 0, "s": "The foundation is Rakuten's and Mizuho's.", "gap": "Nothing in ownership, funding or strategy is Mastercard's.", "neo": "None.", "snb": "Rakuten Bank, Rakuten Group, Mizuho."},
    },
    "t": area_lens(LAYERS),
}
