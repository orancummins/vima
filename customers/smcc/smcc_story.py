"""Sumitomo Mitsui Card's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from smcc_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("SMBC Group's card and payments business as five discs that stack into one platform, from 43 million card holders "
       "and ¥42 trillion of shopping at the bottom to Vpass, the SMBC app, partner channels and SMBC branches at the top. "
       "Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up "
       "across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Cardholders", "user-round"),
    ("olive", "Olive & SMBC customers", "landmark"),
    ("prem", "Premium cardholders & travellers", "plane"),
    ("shop", "Amazon & partner shoppers", "store"),
    ("sme", "Small companies", "briefcase"),
    ("corp", "Large companies & lenders", "factory"),
    ("merch", "Merchants & transport operators", "receipt-text"),
]
USERS_DESC = ("Seven kinds of user around 43 million card holders: everyday cardholders, Olive and SMBC customers, premium "
              "cardholders and travellers, Amazon and partner shoppers, small companies, large companies and the lenders "
              "SMCC guarantees, and the merchants and transport operators it acquires.")

WHO = {"con": "A cardholder", "olive": "An Olive customer", "prem": "A premium cardholder", "shop": "An Amazon shopper",
       "sme": "A small company", "corp": "A large company", "merch": "A merchant"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Pay every day with a numberless card",
     "why": "The everyday loop: an NL card on Visa or Mastercard, a phone tap for extra points, V Point, Vpass.",
     "steps": [("2.1", "nl", "Choose Visa or Mastercard on an NL card"), ("2.8", "wallets", "Tap with a phone"),
               ("3.3", "campaign", "Earn up to 8% at named shops"), ("3.3", "vpoint", "Collect V Point"),
               ("5.1", "vpass", "Check it in Vpass"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "olive", "who": "olive", "name": "Bank and pay with Olive",
     "why": "One Visa card that switches between credit, debit and points, run from the SMBC app.",
     "steps": [("5.1", "smbcapp", "Open Olive in the SMBC app"), ("2.2", "olive", "Switch credit, debit or points"),
               ("4.4", "smbcdebit", "Pay by Visa debit"), ("3.2", "aiolive", "Get help from AI")]},
    {"id": "travel", "who": "prem", "name": "Travel on a premium card",
     "why": "Platinum Preferred and Visa Infinite on Visa; ANA cards on either brand.",
     "steps": [("2.3", "platpref", "Hold Platinum Preferred"), ("2.3", "infinite", "Move up to Visa Infinite"),
               ("2.4", "ana", "Earn ANA miles"), ("5.3", "branches", "Get advice at SMBC")]},
    {"id": "amazon", "who": "shop", "name": "Shop on Amazon with its card",
     "why": "The Amazon Mastercard, issued by SMCC since 2014.",
     "steps": [("5.2", "partnerch", "Apply through Amazon"), ("2.4", "amazon", "Pay with the Amazon Mastercard"),
               ("4.1", "revolve", "Spread the cost")]},
    {"id": "commute", "who": "con", "name": "Ride trains and buses with a card",
     "why": "stera transit at 200-plus operators, Mastercard and Visa touch alike.",
     "steps": [("2.8", "wallets", "Set up a card on the phone"), ("2.7", "transit", "Tap in at the gate"),
               ("2.7", "passcase", "Plan with Pass Case")]},
    {"id": "merch", "who": "merch", "name": "Take card payments",
     "why": "stera terminals now, Clover with Fiserv from late 2026, and transit for operators.",
     "steps": [("2.6", "stera", "Install a stera terminal"), ("2.6", "clover", "Run the shop on Clover"),
               ("2.7", "transit", "Open gates to card fares"), ("3.4", "data", "Read the data")]},
    {"id": "sme", "who": "sme", "name": "Run a small company's money",
     "why": "Trunk with SMBC, and business cards for owners.",
     "steps": [("4.3", "trunk", "Open Trunk"), ("4.3", "bizcard", "Issue business cards"), ("2.6", "clover", "Take payments on Clover")]},
    {"id": "borrow", "who": "con", "name": "Borrow when needed",
     "why": "Revolving and cash advances on the card, and Promise and Mobit loans.",
     "steps": [("4.1", "revolve", "Revolve or take a cash advance"), ("4.1", "promise", "Take a Promise or Mobit loan"),
               ("4.2", "guarantee", "Or borrow from a bank SMCC guarantees")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Dual issuing since 1989, the NL choice, the Amazon co-brand, Apple Pay first, and Mastercard acceptance on stera and transit.",
     "steps": [("2.5", "netmc", "Mastercard issuer since 1989"), ("2.1", "nl", "Equal choice on the NL card"),
               ("2.4", "amazon", "Amazon Mastercard"), ("2.8", "wallets", "First on Apple Pay, 2016"),
               ("2.7", "transit", "Mastercard touch on transit")]},
    {"id": "mcnext", "who": "mc", "name": "Where tokens, agents and acquiring tools could land",
     "why": "Where SMCC has needs and Mastercard is not yet in: Android wallet tokens, agentic payments, fraud against number theft, risk tools for stera and Clover, and the Trunk card.",
     "steps": [("2.8", "wallets", "Mastercard tokens in Google Pay"), ("3.2", "agentic", "Agent Pay alongside Visa"),
               ("3.1", "fraud", "Tokens and passkeys against number theft"), ("2.6", "stera", "Acquirer risk tools for stera and Clover"),
               ("4.3", "trunk", "Commercial cards for Trunk")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across SMBC Card's map",
    "title": "Japan's original Visa issuer, where Mastercard is a real second brand but not the flagship",
    "lead": "SMCC has issued Mastercard since 1989 and offers it as an equal choice on its numberless cards. It runs the Mastercard-only Amazon co-brand, put Mastercard first on Apple Pay in 2016, and acquires Mastercard on stera and on transit at more than 200 operators. But Visa is the house brand: Olive, Platinum Preferred, Visa Infinite, stera's design and the agentic pilot all sit with Visa. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are SMBC Group's own (FY3/26 presentation and data book, May 2026; 1Q FY3/27 overview, July 2026). SMCC's site could not be read, so brands per card rest partly on Japanese Wikipedia and consumer sites, and no network split is published.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Card holders", "43.35m", "March 2026; ¥41.95tn shopping in FY3/26"],
        ["NL cards", "Visa or Mastercard", "Equal choice ⚠"],
        ["Olive", "Visa", "8.0m accounts, June 2026"],
        ["Top tiers", "Visa", "Platinum Preferred, Visa Infinite"],
        ["Amazon co-brand", "Mastercard", "Since 2014"],
        ["Apple Pay", "Mastercard first", "2016; Visa in 2021"],
        ["Acquiring", "Visa, Mastercard, UnionPay", "stera and stera transit"],
        ["Agentic", "Visa", "Agentic Ready, May 2026"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard on the NL, Gold, Platinum, ANA and FS cards, the Amazon Mastercard, Apple Pay since 2016, and acceptance on stera and stera transit.",
                "deals": "What it does not have: Olive, the premium tiers, stera's design, Google Pay touch, the agentic pilot, or a joint announcement since 2015 ⚠."},
        "snb": {"dir": "Visa as house brand since 1980, Olive, Visa Infinite, stera with Visa and GMO, Visa Agentic Ready; JCB on legacy cards and on transit; iD, PayPay and V Point.",
                "deals": "Where they meet: the NL and standard cards, ANA co-brands and transit gates, where both brands are offered."},
    },
    "tl": [
        ["Feb 1980", "Japan's first Visa card"],
        ["Apr 1989", "Mastercard issuing begins"],
        ["Feb 2014", "Amazon MasterCard co-brand"],
        ["Oct 2016", "Apple Pay with Mastercard"],
        ["Oct 2019", "stera with GMO and Visa"],
        ["Jul 2020", "stera transit"],
        ["Feb 2021", "Numberless NL cards"],
        ["Mar 2023", "Olive on Visa's flexible credential"],
        ["Apr 2024", "SMBC Finance Service absorbed; V Point with T Point"],
        ["May 2025", "SoftBank and PayPay alliance; Trunk"],
        ["Sep 2025", "Visa Infinite"],
        ["Jan 2026", "Clover with Fiserv"],
        ["May 2026", "Visa Agentic Ready; Mastercard agentic live in Japan"],
        ["Jun 2026", "Sasaki president; Olive at 8.0m"],
    ],
    "l": {
        "U": {"d": 1, "s": "Many cardholders can choose Mastercard; Olive customers cannot.",
              "gap": "Mass cards offer both brands; Olive and the top tiers are Visa only.",
              "neo": "NL and Amazon Mastercard holders, transit riders.", "snb": "Olive, Platinum Preferred and Visa Infinite holders."},
        "L5": {"d": 0, "s": "The front doors are SMBC's and partners'.", "gap": "Vpass, the SMBC app and branches carry no Mastercard service.", "neo": "Amazon as a channel.", "snb": "Vpass, SMBC app, PayPay, V Point stores."},
        "L4": {"d": 0, "s": "Loans, guarantees, debit and business lines are not Mastercard's.", "gap": "Debit and prepaid are Visa; Trunk and corporate card networks are not stated.",
               "neo": "Revolving on Mastercard cards.", "snb": "Visa debit and prepaid, Promise, guarantees."},
        "L3": {"d": 0, "s": "Points, AI and partnerships are SMCC's or Visa's.", "gap": "No Mastercard service is named in fraud, AI or loyalty; agentic work is with Visa.",
               "neo": "Mastercard touch in reward campaigns.", "snb": "V Point, PayPay, Visa Agentic Ready."},
        "L2": {"d": 1, "s": "Mastercard is a real second brand on cards and acceptance.", "gap": "Visa holds Olive, the top tiers and stera's design; Mastercard keeps NL choice, Amazon and acceptance.",
               "neo": "NL, Amazon, Apple Pay, stera and transit acceptance.", "snb": "Olive, Visa Infinite, JCB, UnionPay, iD."},
        "L1": {"d": 0, "s": "The foundation is SMBC Group's.", "gap": "Ownership and strategy are SMBC's; the heritage is Visa's.", "neo": "Dual issuing since 1989.", "snb": "SMBC Group, Visa heritage."},
    },
    "t": area_lens(LAYERS),
}
