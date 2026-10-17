"""DBS Group's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from dbs_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Singapore's largest bank as five discs that stack into one platform, from S$966 billion of assets and a record "
       "quarter at the bottom to digibank, DBS IDEAL and partners from yuu to Alipay+ at the top. Click the stack to open "
       "it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined "
       "in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("card", "Cardholders", "credit-card"),
    ("mig", "Migrant workers", "plane"),
    ("wealth", "Wealth clients", "gem"),
    ("sme", "SMEs", "briefcase"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Six kinds of customer across 19 markets: everyday customers of DBS and POSB, cardholders in Singapore, Hong "
              "Kong and Taiwan, the migrant workers three-quarters of whom bank with POSB digibank, wealth clients with "
              "S$516 billion of assets, SMEs, and the corporates and institutions DBS IDEAL serves.")

WHO = {"con": "A DBS customer", "card": "A cardholder", "mig": "A migrant worker", "wealth": "A wealth client",
       "sme": "An SME", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "A POSB account, debit, PayLah! and PayNow, digibot and scam controls.",
     "steps": [("4.1", "posbbank", "Open a POSB account"), ("2.3", "debitcards", "Pay with debit"), ("2.5", "paylah", "Scan a QR with PayLah!"),
               ("2.5", "paynow", "Send by PayNow"), ("3.3", "digibot", "Ask digibot"), ("3.1", "scams", "Protected from scams")]},
    {"id": "card", "who": "card", "name": "Earn on a card",
     "why": "Miles on Visa, points on Mastercard, and instalments.",
     "steps": [("2.1", "altitude", "Earn miles on Altitude"), ("2.1", "womans", "Or points on Woman's World"),
               ("2.4", "installments", "Spread a purchase"), ("3.4", "points", "Redeem points"), ("3.4", "gamer", "Swap points for gaming credits")]},
    {"id": "agent", "who": "card", "name": "Let an agent pay",
     "why": "Agentic card payments on both networks in 2026.",
     "steps": [("3.2", "vic", "Pay through Visa Intelligent Commerce"), ("3.2", "agentpay", "Or through Mastercard Agent Pay"),
               ("3.3", "digibot", "Service the card by agent")]},
    {"id": "home", "who": "mig", "name": "Send money home",
     "why": "POSB digibank, DBS Remit, and PayNow and wallet corridors.",
     "steps": [("5.1", "digibank", "Bank on POSB digibank"), ("4.1", "posbbank", "Hold a POSB account"),
               ("2.6", "remit", "Send with DBS Remit"), ("2.5", "alipay", "Or to a WeChat wallet")]},
    {"id": "wealth", "who": "wealth", "name": "Grow wealth",
     "why": "Treasures, markets and tokenised assets.",
     "steps": [("4.2", "treasures", "Bank with Treasures"), ("4.4", "gfm", "Trade with the treasury desk"),
               ("2.7", "ddex", "Hold tokenised gold"), ("5.1", "digibank", "Watch it in digibank")]},
    {"id": "sme", "who": "sme", "name": "Pay suppliers abroad",
     "why": "DBS IDEAL, GlobeSend and PayNow.",
     "steps": [("5.2", "ideal", "Log in to DBS IDEAL"), ("2.6", "globesend", "Pay through GlobeSend"), ("2.5", "paynow", "Collect by PayNow")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Transaction services, an agentic assistant and tokenised settlement.",
     "steps": [("5.2", "ideal", "Log in to DBS IDEAL"), ("4.3", "ibg", "Bank with GTS"), ("3.3", "joy", "Ask Joy"),
               ("2.7", "tokens", "Settle with Treasury Tokens"), ("2.7", "partior", "Settle FX on Partior")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Half of Singapore's credit cards, POSB debit, Hong Kong's premium card, Agent Pay, Installments and loyalty.",
     "steps": [("2.1", "womans", "Woman's World Mastercard"), ("2.1", "posbeveryday", "POSB Everyday"),
               ("2.2", "hkcards", "Black World in Hong Kong"), ("3.2", "agentpay", "First live Agent Pay payments"),
               ("2.4", "installments", "Mastercard Installments ⚠"), ("3.4", "gamer", "Gamer Exchange"), ("3.4", "hotels", "Hotel points conversion")]},
    {"id": "mcnext", "who": "mc", "name": "Where miles, agents and tokens could land",
     "why": "Where DBS has needs and Mastercard is not yet in: the Visa miles and debit cards, agentic servicing, wallet tokens and passkeys, Move for remittances, the Citi Taiwan book and tokenised settlement.",
     "steps": [("2.1", "altitude", "The premium miles cards"), ("3.3", "digibot", "Agentic tokens for digibot"),
               ("3.1", "scams", "Tokens and passkeys against scams"), ("2.6", "remit", "Mastercard Move for remittances"),
               ("1.5", "deals", "The Citi Taiwan card book"), ("2.7", "tokens", "Multi-Token Network links")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across DBS's map",
    "title": "An even split, with Visa on the miles cards and Mastercard first with agents",
    "lead": "DBS splits Singapore's credit cards evenly: five Visa, five Mastercard and three Amex. Visa holds the premium miles cards, the youth card and the main debit cards; Mastercard holds Woman's World, POSB Everyday, Esso, SAFRA and PAssion debit, and Hong Kong's premium Black World. DBS piloted Visa Intelligent Commerce first, then ran Singapore's first live Mastercard Agent Pay payment three weeks later, and its CEO sits on Mastercard's Asia Pacific advisory board. PayNow and PayLah! carry everyday payments off card rails. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (2Q26 results, 6 August 2026) or from DBS, Mastercard, Visa and press. Networks were read from DBS card pages and card faces on 17 October 2026; Taiwan is partly inferred, and India, Indonesia and China card lineups were not found.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Singapore credit", "Even split", "5 Visa, 5 Mastercard, 3 Amex"],
        ["Premium miles", "Visa", "Altitude, Vantage"],
        ["Singapore debit", "Mostly Visa", "3 Visa, 2 Mastercard, 1 UnionPay"],
        ["Hong Kong premium", "Mastercard", "Black World, hotel points April 2026"],
        ["Agentic", "Both", "Visa pilot Feb 2026; Agent Pay live Mar 2026"],
        ["Instalments", "Mastercard Installments", "Since March 2022 ⚠"],
        ["QR & P2P", "PayLah!, PayNow", "60% of hawker QR"],
        ["Boardroom", "Mastercard", "CEO on its APAC advisory board"],
    ],
    "sides": {
        "neo": {"dir": "Woman's World, POSB Everyday, Esso, SAFRA, PAssion debit, Black World, Agent Pay, Installments ⚠ and Gamer Exchange.",
                "deals": "What it does not do: the miles and main debit cards, PayNow and PayLah!, remittances, tokenised deposits or scam controls."},
        "snb": {"dir": "Visa on the miles, youth and debit cards and its own agentic pilot, Amex alternatives, PayNow and PayLah!, Alipay+ and DBS's own tokens.",
                "deals": "Where they meet: agentic payments, where DBS works with both networks."},
    },
    "tl": [
        ["Mar 2022", "Mastercard Installments with Pine Labs"],
        ["Aug 2023", "Citi Taiwan consumer business joins"],
        ["Mar 2025", "Tan Su Shan becomes CEO"],
        ["2025", "Mastercard Gamer Exchange, first in Singapore"],
        ["Nov 2025", "Kinexys tokenised-deposit framework"],
        ["Feb 2026", "Visa Intelligent Commerce pilot"],
        ["Mar 2026", "Agent Pay live in Singapore and Hong Kong"],
        ["Apr 2026", "Black World hotel points"],
        ["Sep 2026", "Hong Kong assistants go agentic"],
    ],
    "l": {
        "U": {"d": 1, "s": "Half of Singapore's cardholders carry Mastercard.",
              "gap": "Miles and debit holders carry Visa; Woman's World, POSB Everyday and Black World holders carry Mastercard; PayLah! users need neither.",
              "neo": "Woman's, POSB, Esso, SAFRA and Black World cardholders.", "snb": "Miles, youth and debit cardholders, PayLah! users, wealth clients."},
        "L5": {"d": 1, "s": "Some partner cards run on Mastercard.", "gap": "digibank and IDEAL are DBS's; Esso and SAFRA cards are Mastercard, yuu and Takashimaya Visa or Amex.",
               "neo": "Esso and SAFRA.", "snb": "digibank, IDEAL, yuu, Alipay+."},
        "L4": {"d": 1, "s": "Consumer franchises carry both networks.", "gap": "Consumer banking in Singapore and Hong Kong carries Mastercard and Visa cards; wealth, IBG and markets have no network role.",
               "neo": "POSB and Hong Kong cards.", "snb": "Treasures, IBG, markets."},
        "L3": {"d": 1, "s": "Agent Pay and Gamer Exchange are Mastercard's; scam controls are DBS's.", "gap": "Agentic payments run on both networks; loyalty mixes DBS's own points with Mastercard features.",
               "neo": "Agent Pay, Gamer Exchange, hotel conversion.", "snb": "Scam controls, digibot, Joy, Visa pilot, DBS Points."},
        "L2": {"d": 1, "s": "An even card split, with account-to-account rails beside it.", "gap": "Visa holds miles and main debit; Mastercard holds women's, POSB and Hong Kong premium cards and Installments; PayNow, PayLah! and tokens are off card rails.",
               "neo": "Woman's, POSB Everyday, Black World, PAssion, Installments ⚠.", "snb": "Altitude, Vantage, Visa Debit, PayNow, PayLah!, Token Services."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's; the CEO advises it.", "neo": "None.", "snb": "Capital, heritage, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
