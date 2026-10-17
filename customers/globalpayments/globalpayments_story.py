"""Global Payments' kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

SUB = ("A pure merchant company since it bought Worldpay and sold its issuer business, as five discs that stack into one "
       "platform: $3.7 trillion of volume and the network rules it lives by at the bottom, Genius devices, developer "
       "hubs and bank channels at the top. Click the stack to open it. Choose who you are and what you want to do, and "
       "the areas that deliver it light up across the layers, joined in the order they act. Switch to the Mastercard "
       "lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("sme", "Small businesses", "store"),
    ("ent", "Enterprise merchants", "building-2"),
    ("plat", "Software platforms", "code-xml"),
    ("con", "Shoppers & taxpayers", "user-round"),
    ("bank", "Bank partners", "landmark"),
    ("inv", "Investors & regulators", "chart-column"),
]
USERS_DESC = ("Six kinds of user around 6 million merchant locations: small businesses, enterprise merchants, the software "
              "platforms that embed payments, the shoppers and taxpayers who pay them, the banks that refer merchants, and "
              "the investors and regulators watching the Worldpay integration.")

WHO = {
    "sme": "A small business", "ent": "An enterprise merchant", "plat": "A software platform", "con": "A shopper",
    "bank": "A partner bank", "inv": "An investor",
}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "genius", "who": "sme", "name": "Run a restaurant or shop on Genius",
     "why": "The small-business loop: a Genius device, card acceptance, fraud screening and a loyalty programme.",
     "steps": [("5.3", "sales", "Sign up with a sales rep"), ("5.1", "genius", "Set up Genius"),
               ("4.3", "smb", "Run the business"), ("2.2", "smbacq", "Accept every card"), ("3.6", "loyalty", "Add gift and loyalty")]},
    {"id": "enterprise", "who": "ent", "name": "Take payments in 175 countries",
     "why": "Worldpay for the enterprise: acquiring, local methods, tokens, fraud and disputes on one platform.",
     "steps": [("4.1", "enterprise", "Contract with Worldpay"), ("2.1", "wpenterprise", "Acquire in every market"),
               ("2.3", "gateway", "Offer wallets and local methods"), ("3.2", "tokens", "Lift authorisations"),
               ("3.1", "ravelin", "Stop fraud with Ravelin"), ("3.3", "disputes", "Defend chargebacks")]},
    {"id": "agent", "who": "ent", "name": "Sell to AI agents",
     "why": "Worldpay supports Visa's Trusted Agent Protocol, OpenAI's ACP and Google's UCP, and runs its own MCP server.",
     "steps": [("5.2", "developers", "Connect through MCP"), ("3.4", "agentic", "Accept agent payments"),
               ("3.2", "tokens", "Keep card data in the vault"), ("3.3", "disputes", "Defend agent disputes")]},
    {"id": "platform", "who": "plat", "name": "Embed payments in your software",
     "why": "Global Payments for Platforms: from referral to managed payfac, with payouts and working capital.",
     "steps": [("4.2", "platforms", "Choose a payfac model"), ("2.5", "fx", "Split payments in a marketplace"),
               ("2.4", "move", "Pay out to cards"), ("3.5", "embedded", "Offer working capital")]},
    {"id": "payout", "who": "plat", "name": "Pay out to workers and customers",
     "why": "Push-to-Card on Mastercard Move in the UAE, Push-to-Card elsewhere, and stablecoins with BVNK.",
     "steps": [("2.4", "move", "Push to card with Mastercard Move"), ("2.4", "stablecoinpayouts", "Or pay out in stablecoins"),
               ("2.5", "fx", "Convert currency")]},
    {"id": "tax", "who": "con", "name": "Pay your taxes by card",
     "why": "Link2Gov, the IRS's preferred digital payment partner for 2026.",
     "steps": [("2.6", "link2gov", "Pay the IRS with Pay1040")]},
    {"id": "bank", "who": "bank", "name": "Refer your business customers",
     "why": "Banks and joint ventures that sell Global Payments' acceptance to their merchants.",
     "steps": [("5.4", "banks", "Join the bank channel"), ("2.2", "smbacq", "Merchants accept cards"), ("5.1", "genius", "And run Genius")]},
    {"id": "deal", "who": "inv", "name": "Follow the Worldpay integration",
     "why": "The swap that made a pure merchant company, and what it has to deliver.",
     "steps": [("1.5", "swap", "Worldpay in, TSYS out"), ("1.6", "strategy", "$600 million of synergies"),
               ("1.1", "finances", "The 2026 outlook"), ("4.6", "divested", "What was sold")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Every merchant accepts Mastercard; Worldpay pays out on Mastercard Move in the UAE and co-ran Thrive Street.",
     "steps": [("2.1", "wpenterprise", "Acceptance at every merchant"), ("2.4", "move", "Mastercard Move in the UAE"),
               ("5.5", "events", "Thrive Street in the UK"), ("1.2", "licences", "Network rules and registration")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, payouts and data could land",
     "why": "Where the company has needs and Mastercard is not yet in: Agent Pay and Verifiable Intent at Worldpay, Move beyond the UAE, Click to Pay and tokens, disputes and fraud data, and travel.",
     "steps": [("3.4", "agentic", "Agent Pay and Verifiable Intent"), ("2.4", "move", "Move in the UK, EU, US and Australia"),
               ("2.3", "gateway", "Click to Pay and tokens, on the record"), ("3.3", "disputes", "Consumer Clarity and Ethoca"),
               ("3.1", "ravelin", "Decision Intelligence beside Ravelin"), ("2.4", "stablecoinpayouts", "Stablecoin settlement")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Global Payments' map",
    "title": "Accepted everywhere, partnered in one place",
    "lead": "Every Global Payments and Worldpay merchant accepts Mastercard, and Worldpay pays out on Mastercard Move in the UAE. Beyond that, the public record is thin. Visa has the dated commitments (Click to Pay and tokens in 2020, the Trusted Agent Protocol in 2025), Worldpay supports OpenAI's and Google's agentic protocols, and the TSYS issuer business that processed Mastercard programmes now belongs to FIS. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the company's own (Q2 2026 results, 5 August 2026; completion release, 12 January 2026) or come from Worldpay, Mastercard, Visa and trade press. Mastercard's logo on Worldpay's agentic page is not backed by an announcement.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Acceptance", "Every network", "$3.7 trillion, 6 million locations"],
        ["Payouts", "Mastercard Move", "UAE, August 2025"],
        ["Marketing", "Thrive Street", "UK independent retail, 2025"],
        ["Agentic", "Visa TAP, ACP, UCP", "No Agent Pay announcement"],
        ["Tokens", "Visa since 2020", "Click to Pay and Visa Token Service"],
        ["Stablecoins", "BVNK, USDC", "Payouts and settlement"],
        ["Fraud", "Ravelin", "Bought 2025"],
        ["Issuing", "Sold to FIS", "TSYS, January 2026"],
    ],
    "sides": {
        "neo": {"dir": "Acceptance at every merchant, Push-to-Card on Mastercard Move in the UAE, Thrive Street, and the network rules Global Payments works under.",
                "deals": "What it does not do: agentic acceptance, Click to Pay or tokens on the record, fraud or dispute data, or payouts outside the UAE."},
        "snb": {"dir": "Visa's Click to Pay, tokens and Trusted Agent Protocol, OpenAI's ACP and Google's UCP, BVNK stablecoins, Ravelin, Genius, and FIS for issuing.",
                "deals": "Where they meet: every card transaction, payouts, and the agentic standards race."},
    },
    "tl": [
        ["Dec 2020", "Worldpay and Visa: Click to Pay and tokens"],
        ["Apr 2025", "Worldpay deal agreed; Mastercard launches Agent Pay"],
        ["May 2025", "Worldpay stablecoin payouts with BVNK"],
        ["Aug 2025", "Worldpay on Mastercard Move in the UAE"],
        ["Oct 2025", "Thrive Street with Mastercard; Visa's Trusted Agent Protocol with Worldpay"],
        ["Jan 2026", "Worldpay deal closes; TSYS issuing to FIS"],
        ["Mar 2026", "Mastercard Verifiable Intent (Worldpay not confirmed)"],
        ["Aug 2026", "2026 outlook cut on travel"],
    ],
    "l": {
        "U": {"d": 1, "s": "Every merchant accepts Mastercard; few use its services.",
              "gap": "Mastercard reaches every merchant through acceptance and some platforms through Move in the UAE; agentic, token and fraud services are not in public.",
              "neo": "Every accepting merchant; UAE payout platforms.", "snb": "Genius users, ISVs on Payrix, taxpayers, bank partners."},
        "L5": {"d": 0, "s": "The front doors are the company's.", "gap": "Genius, developer hubs, sales and bank channels are Global Payments'; Thrive Street was joint.",
               "neo": "Thrive Street.", "snb": "Genius, MCP servers, direct sales, bank channel."},
        "L4": {"d": 1, "s": "Acceptance in every segment.", "gap": "Enterprise, Platforms and SMB all accept Mastercard; restaurant software and vertical software do not involve it.",
               "neo": "Acceptance.", "snb": "Genius restaurants, vertical software."},
        "L3": {"d": 0, "s": "The engine room is Worldpay's, Ravelin's and Visa's.", "gap": "Fraud is Ravelin's, agentic leans to Visa's protocol, ACP and UCP; tokens are generic.",
               "neo": "Network tokens (unannounced).", "snb": "Ravelin, Visa TAP, ACP, UCP, Disputes Defender."},
        "L2": {"d": 1, "s": "Acceptance and Move; stablecoins and local methods elsewhere.",
               "gap": "Mastercard rides through acquiring and powers UAE payouts; BVNK, USDC, wallets and local methods are other rails.",
               "neo": "Acquiring, Mastercard Move (UAE).", "snb": "BVNK, USDC, wallets, local methods, Link2Gov."},
        "L1": {"d": 0, "s": "The company's own scale and strategy.", "gap": "Mastercard appears as network rules and registration only.",
               "neo": "Network rules.", "snb": "Scale, leadership, heritage, the Worldpay swap, synergies."},
    },
    "t": {
        "1.1": {"d": 0, "why": "The company's own scale.", "v": [["Scale", "No Mastercard role.", "0", ""]]},
        "1.2": {"d": 1, "why": "Mastercard rules and registration.", "v": [["Network rules", "A risk factor.", "", ""]]},
        "1.3": {"d": 0, "why": "Leadership.", "v": [["Leadership", "No Mastercard role.", "0", ""]]},
        "1.4": {"d": 0, "why": "Heritage.", "v": [["Heritage", "No Mastercard role.", "0", ""]]},
        "1.5": {"d": 0, "why": "TSYS's Mastercard issuer ties went to FIS.", "v": [["Issuer processing", "Now FIS.", "0", ""]]},
        "1.6": {"d": 0, "why": "Strategy.", "v": [["Strategy", "No Mastercard role.", "0", ""]]},
        "2.1": {"d": 1, "why": "Worldpay accepts every network.", "v": [["Acceptance", "All networks.", "", ""]]},
        "2.2": {"d": 1, "why": "Small-business acquiring accepts every network.", "v": [["Acceptance", "All networks.", "", ""]]},
        "2.3": {"d": 1, "why": "Mastercard among methods; Visa's Click to Pay on the record.", "v": [["Click to Pay", "Visa since 2020.", "0", ""], ["Mastercard tokens", "Not announced.", "u", ""]]},
        "2.4": {"d": 1, "why": "Mastercard Move in the UAE; stablecoins elsewhere.", "v": [["Mastercard Move", "UAE.", "", ""], ["BVNK", "Stablecoins.", "0", ""]]},
        "2.5": {"d": 0, "why": "Currency and marketplaces.", "v": [["FX", "No Mastercard role.", "0", ""]]},
        "2.6": {"d": 1, "why": "Cards among government payment methods.", "v": [["Card payments", "All networks.", "", ""]]},
        "3.1": {"d": 0, "why": "Ravelin is in-house.", "v": [["Decision Intelligence", "Not used.", "0", ""]]},
        "3.2": {"d": 1, "why": "Network tokens surely supported, none announced.", "v": [["Network tokens", "Unannounced.", "u", ""]]},
        "3.3": {"d": 0, "why": "Disputes Defender is Worldpay's.", "v": [["Consumer Clarity, Ethoca", "Not used.", "0", ""]]},
        "3.4": {"d": 0, "why": "Visa TAP, ACP and UCP; no Agent Pay announcement.", "v": [["Agent Pay", "Not announced.", "u", ""], ["Visa TAP", "October 2025.", "0", ""]]},
        "3.5": {"d": None, "why": "Embedded card network not public.", "v": [["Embedded cards", "Not verified.", "u", ""]]},
        "3.6": {"d": 0, "why": "Gift and loyalty.", "v": [["Offers", "Not used.", "0", ""]]},
        "4.1": {"d": 1, "why": "Acceptance.", "v": [["Enterprise", "All networks.", "", ""]]},
        "4.2": {"d": 1, "why": "Acceptance through platforms.", "v": [["Platforms", "All networks.", "", ""]]},
        "4.3": {"d": 1, "why": "Acceptance for small businesses.", "v": [["SMB", "All networks.", "", ""]]},
        "4.4": {"d": 0, "why": "Restaurant software.", "v": [["Genius restaurants", "No Mastercard role.", "0", ""]]},
        "4.5": {"d": 0, "why": "Vertical software.", "v": [["Software", "No Mastercard role.", "0", ""]]},
        "4.6": {"d": 0, "why": "Divested businesses.", "v": [["Issuer Solutions", "Sold to FIS.", "0", ""]]},
        "5.1": {"d": 0, "why": "Genius devices.", "v": [["Genius", "No Mastercard role.", "0", ""]]},
        "5.2": {"d": 0, "why": "Developer hubs.", "v": [["MCP", "No Mastercard role.", "0", ""]]},
        "5.3": {"d": 0, "why": "Direct sales.", "v": [["Sales", "No Mastercard role.", "0", ""]]},
        "5.4": {"d": 0, "why": "Bank channels.", "v": [["Banks", "No Mastercard role.", "0", ""]]},
        "5.5": {"d": 1, "why": "Thrive Street with Mastercard.", "v": [["Thrive Street", "With Mastercard.", "", ""]]},
    },
}
