"""Checkout.com's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from checkout_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("An enterprise payments platform as five discs that stack into one, from $300 billion of volume, ten acquiring "
       "licences and a new US bank charter at the bottom to one API and 19 offices at the top. Click the stack to open "
       "it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined "
       "in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("ent", "Enterprise merchants", "building-2"),
    ("mkt", "Marketplaces & platforms", "users-round"),
    ("travel", "Travel companies", "plane"),
    ("fin", "Fintechs & crypto", "coins"),
    ("shop", "Shoppers", "user-round"),
]
USERS_DESC = ("Five kinds of user: more than 1,700 enterprise merchants, the marketplaces and platforms that embed "
              "payments, travel companies, fintechs and crypto exchanges, and the shoppers who pay them.")

WHO = {"ent": "An enterprise merchant", "mkt": "A marketplace", "travel": "A travel company", "fin": "A fintech", "shop": "A shopper"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "accept", "who": "ent", "name": "Take payments in 50 countries",
     "why": "The core loop: one API, local acquiring, every method, AI optimisation and fraud screening.",
     "steps": [("5.1", "api", "Integrate one API"), ("2.1", "acquiring", "Acquire locally"), ("2.2", "apms", "Offer local methods and wallets"),
               ("3.1", "ia", "Lift approvals with Intelligent Acceptance"), ("3.3", "fraud", "Screen for fraud")]},
    {"id": "checkout", "who": "shop", "name": "Check out in one click",
     "why": "Flow and Remember Me: saved credentials across Checkout.com merchants, with tokens and 3DS behind them.",
     "steps": [("3.4", "flow", "Pay with Flow"), ("3.1", "tokens", "Paid with a network token"), ("3.2", "auth", "Authenticated without a redirect")]},
    {"id": "platform", "who": "mkt", "name": "Run a marketplace",
     "why": "Accept, hold, pay out and issue on one platform.",
     "steps": [("4.2", "platforms", "Embed payments with Platforms"), ("2.6", "account", "Hold funds in the Business Account"),
               ("2.4", "move", "Pay sellers to their cards"), ("2.3", "issuing", "Issue cards to sellers")]},
    {"id": "travel", "who": "travel", "name": "Pay hotels and airlines",
     "why": "Virtual cards for travel agents on Mastercard Wholesale, and travel issuing on Visa.",
     "steps": [("4.3", "travel", "Sell travel"), ("2.3", "wholesale", "Pay suppliers with Wholesale virtual cards"),
               ("2.3", "visatravel", "Or Visa travel cards")]},
    {"id": "fintech", "who": "fin", "name": "Move money for a fintech",
     "why": "Payouts, account funding and stablecoins.",
     "steps": [("4.4", "fintech", "Fund accounts in real time"), ("2.4", "payouts", "Pay out over Visa Direct, RTP and ACH"),
               ("2.5", "stablecoins", "Settle in stablecoins")]},
    {"id": "agent", "who": "ent", "name": "Sell to AI agents",
     "why": "Checkout.com supports every agentic protocol and launched Agent Pay with Mastercard.",
     "steps": [("3.5", "agentic", "Connect to ACP, UCP and AP2"), ("3.5", "agentpay", "Accept Agent Pay with Verifiable Intent"),
               ("3.1", "tokens", "Pay with agentic tokens")]},
    {"id": "us", "who": "ent", "name": "Grow in the US",
     "why": "Direct acquiring under its own charter since September 2026, with US issuing and payouts.",
     "steps": [("1.2", "malpb", "Acquire directly in the US"), ("2.1", "acquiring", "Route to every network"), ("2.4", "payouts", "Pay out by RTP")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Agent Pay launch partner, Move payouts in the UAE and Canada, Wholesale virtual cards, tokens and dual-network issuing.",
     "steps": [("3.5", "agentpay", "Agent Pay, Verifiable Intent, Agent Pay for Machines"), ("2.4", "move", "Mastercard Move payouts"),
               ("2.3", "wholesale", "Wholesale virtual cards"), ("3.1", "tokens", "Mastercard network tokens"), ("2.3", "issuing", "Issuing on Mastercard")]},
    {"id": "mcnext", "who": "mc", "name": "Where Click to Pay, disputes and the US could land",
     "why": "Where Checkout.com has needs and Mastercard is not yet in: Click to Pay against Remember Me, Ethoca beside Verifi, Move in the US, issuing in the US and UAE, live agentic volume and stablecoin settlement.",
     "steps": [("3.4", "flow", "Click to Pay and passkeys"), ("3.3", "fraud", "Ethoca and Consumer Clarity"),
               ("2.4", "payouts", "Move in the US"), ("2.3", "issuing", "US and UAE issuing"), ("2.5", "stablecoins", "Stablecoin settlement")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Checkout.com's map",
    "title": "An agentic partner, with Visa ahead in money movement",
    "lead": "Checkout.com accepts, tokenises and issues on Mastercard, pays out on Mastercard Move in the UAE and Canada, runs Wholesale virtual cards for travel agents, and was a launch partner of Agent Pay, Verifiable Intent and Agent Pay for Machines. Visa has more public firsts in money movement and issuing (Visa Direct, travel issuing, Verifi), and Checkout.com's own Remember Me, local methods and stablecoins work around both. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Checkout.com's own releases or come from Mastercard, Visa and trade press. Checkout.com is private and does not publish its network split.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Agentic", "Agent Pay launch partner", "Verifiable Intent, Agent Pay for Machines"],
        ["Payouts", "Mastercard Move", "UAE (2025), Canada (2026); Visa Direct too"],
        ["Issuing", "Both networks", "Visa travel issuing; Mastercard Wholesale"],
        ["Tokens", "Both networks", "Average 11% uplift"],
        ["Checkout", "Remember Me", "Its own saved-card network"],
        ["Disputes", "Visa's Verifi", "No Ethoca"],
        ["Stablecoins", "Coinbase, Fireblocks", "And a euro issuer"],
        ["US", "Direct acquiring", "Own charter since September 2026"],
    ],
    "sides": {
        "neo": {"dir": "Acceptance and tokens, issuing, Move payouts, Wholesale virtual cards, and Agent Pay, Verifiable Intent and Agent Pay for Machines.",
                "deals": "What it does not do: Click to Pay, disputes, US payouts, stablecoins or local methods."},
        "snb": {"dir": "Visa Direct and Visa travel issuing, Verifi, Remember Me, local methods and BNPL, stablecoins with Coinbase and Fireblocks, and Checkout.com's own fraud models.",
                "deals": "Where they meet: every card payment, and the standards for agentic commerce."},
    },
    "tl": [
        ["Mar 2023", "Issuing launched"],
        ["May 2024", "Mastercard Wholesale virtual cards for travel agents"],
        ["Feb 2025", "Visa Direct and Mastercard Move in the UAE"],
        ["Apr 2025", "Agent Pay launch partner"],
        ["Jul 2025", "Visa travel issuing"],
        ["Oct 2025", "Remember Me launched"],
        ["Mar 2026", "Verifiable Intent backer"],
        ["Jun 2026", "Agent Pay for Machines; stablecoins with Coinbase and Fireblocks"],
        ["Sep 2026", "US direct acquiring live"],
    ],
    "l": {
        "U": {"d": 1, "s": "Every merchant takes Mastercard; many also use the other rails.",
              "gap": "Every merchant accepts Mastercard and many use its tokens; travel agents use Wholesale cards; fintechs fund accounts on Visa.",
              "neo": "Merchants on Mastercard tokens, travel agents, Agent Pay merchants.", "snb": "Visa travel issuers, Remember Me shoppers, crypto firms."},
        "L5": {"d": 0, "s": "The front doors are Checkout.com's.", "gap": "API, regions and partners are its own.",
               "neo": "None.", "snb": "API, dashboard, offices, partners."},
        "L4": {"d": 1, "s": "Mastercard in every line through acceptance.", "gap": "All business lines accept Mastercard; none is Mastercard-only.",
               "neo": "Acceptance, Wholesale for travel.", "snb": "Visa funding for fintechs."},
        "L3": {"d": 1, "s": "Agent Pay is Mastercard's; the rest is Checkout.com's or Visa's.",
               "gap": "Agent Pay and tokens involve Mastercard; Remember Me, fraud and Verifi do not.",
               "neo": "Agent Pay, tokens, 3DS.", "snb": "Remember Me, Verifi, own fraud models."},
        "L2": {"d": 1, "s": "Shared with Visa, around local and digital rails.",
               "gap": "Mastercard is in acquiring, issuing, Move and Wholesale; Visa in Direct and travel issuing; local methods and stablecoins in neither.",
               "neo": "Acquiring, issuing, Move, Wholesale.", "snb": "Visa Direct, local methods, stablecoins."},
        "L1": {"d": 0, "s": "Checkout.com's own scale and licences.", "gap": "Nothing in the foundation is Mastercard's.",
               "neo": "None.", "snb": "Licences, charter, platform, strategy."},
    },
    "t": area_lens(LAYERS),
}
