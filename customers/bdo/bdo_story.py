"""BDO Unibank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bdo_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The Philippines' largest bank as five discs that stack into one platform, from ₱3.9 trillion of loans and the "
       "SM Group at the bottom to more than 2,000 branches and the BDO Pay wallet at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in "
       "the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("ofw", "Overseas Filipinos & families", "earth"),
    ("aff", "Affluent & private clients", "gem"),
    ("merch", "Merchants", "store"),
    ("sme", "MSMEs", "briefcase"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer: everyday Filipinos, more than 4 million overseas Filipinos and their families, "
              "affluent and private clients, the merchants BDO acquires for, MSMEs and the corporates it lends to.")

WHO = {"con": "A BDO customer", "ofw": "An overseas Filipino", "aff": "A private client", "merch": "A merchant",
       "sme": "An MSME owner", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a deposit account, a Mastercard ATM card, BDO Pay and free instant transfers.",
     "steps": [("5.1", "branches", "Open an account at a branch"), ("4.2", "deposits", "Keep savings in a BDO account"),
               ("2.1", "debit", "Pay and withdraw with the ATM card"), ("5.2", "bdopay", "Run it in BDO Pay"),
               ("2.6", "instapay", "Send money free over InstaPay")]},
    {"id": "remit", "who": "ofw", "name": "Send money home",
     "why": "Twenty years of BDO remittances on Mastercard's infrastructure, for more than 4 million Filipinos abroad.",
     "steps": [("5.4", "intl", "Send through a BDO office abroad"), ("2.4", "remit", "Remit on Mastercard's rails"),
               ("2.1", "debit", "Family withdraws with a BDO ATM card"), ("5.1", "atms", "Cash out at any of 7,900 machines")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Credit cards on six networks, with points and promotions.",
     "steps": [("2.2", "credit", "Choose a BDO credit card"), ("3.2", "rewards", "Earn rewards and promos"),
               ("3.1", "emv", "Pay with a chip card")]},
    {"id": "wallet", "who": "con", "name": "Pay with my phone",
     "why": "BDO Pay, linked straight to BDO accounts and cards, with QR Ph and free transfers.",
     "steps": [("5.2", "bdopay", "Open BDO Pay"), ("2.6", "qrph", "Scan a QR Ph code"), ("2.6", "instapay", "Split a bill"),
               ("3.2", "payrewards", "Collect wallet rewards"), ("2.3", "paycard", "Get a BDO Pay Card")]},
    {"id": "wealth", "who": "aff", "name": "Grow and protect wealth",
     "why": "The country's largest trust business, BDO Private Bank and BDO Life.",
     "steps": [("4.3", "trust", "Invest through trust or the Private Bank"), ("4.3", "life", "Protect it with BDO Life"),
               ("4.4", "capital", "Trade with BDO Securities"), ("2.2", "diners", "Carry a Diners Club card")]},
    {"id": "merchant", "who": "merch", "name": "Take payments",
     "why": "A BDO terminal that takes every card brand, plus QR Ph.",
     "steps": [("2.5", "acquiring", "Accept every card brand"), ("2.6", "qrph", "Accept QR Ph"), ("4.2", "deposits", "Settle into a BDO account")]},
    {"id": "sme", "who": "sme", "name": "Grow a small business",
     "why": "MSME loans, leasing and rural branches, a named strategic focus.",
     "steps": [("4.1", "msme", "Borrow as an MSME"), ("4.4", "leasing", "Lease equipment"), ("4.5", "network", "Bank in the provinces with BDO Network Bank"),
               ("5.3", "online", "Pay suppliers online")]},
    {"id": "corp", "who": "corp", "name": "Fund a corporate",
     "why": "Corporate loans, bonds and investment banking from the largest balance sheet in the country.",
     "steps": [("4.1", "corp", "Borrow from BDO"), ("4.4", "capital", "Raise money with BDO Capital"), ("1.5", "bonds", "Join a sustainability bond")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "ATM debit cards, twenty years of remittances, Mastercard credit tiers and acceptance at BDO's merchants.",
     "steps": [("2.1", "debit", "ATM debit on Mastercard"), ("2.4", "remit", "Remittances on Mastercard"),
               ("3.1", "emv", "EMV Mastercard debit since 2016"), ("2.2", "credit", "Gold and Platinum Mastercard"),
               ("2.5", "acquiring", "Acceptance at BDO terminals")]},
    {"id": "mcnext", "who": "mc", "name": "Where BDO Pay, scams and remittances could land",
     "why": "Where BDO has needs and Mastercard is not yet in: cards tokenised inside BDO Pay, scam scoring for free instant transfers, cross-border money movement against Visa Direct, offers for wallet rewards and MSME cards.",
     "steps": [("5.2", "bdopay", "Tokenised Mastercard cards in BDO Pay"), ("3.1", "fraud", "Scam scoring for instant transfers"),
               ("2.4", "remit", "Mastercard Move against Visa Direct"), ("3.2", "payrewards", "Card-linked offers"),
               ("4.1", "msme", "Commercial cards for MSMEs")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across BDO Unibank's map",
    "title": "Twenty years of debit and remittances, one brand among six in credit",
    "lead": "Mastercard has carried BDO's ATM debit cards and remittances for twenty years, reaching more than 4 million Filipinos abroad, and BDO issued the country's first EMV Mastercard debit cards in 2016. In credit BDO issues six brands, and its own growth in payments runs on domestic rails: InstaPay, PESONet and QR Ph inside BDO Pay, free since July 2026. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own as reported in the Philippine press (H1 2026 results, 25 July 2026) or from Visa, JCB, Diners Club and the BSP. BDO's website refused automated requests, so card networks by programme are partly inferred and marked ⚠.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["ATM debit", "Mastercard", "\"Millions\" of cards; EMV since 2016"],
        ["Remittances", "Mastercard", "20 years; 4 million+ Filipinos abroad"],
        ["Credit", "Six brands", "Mastercard, Visa, Amex, JCB, UnionPay, Diners"],
        ["Other debit", "Visa ⚠", "EMV Visa debit from 2017"],
        ["Transfers", "InstaPay, PESONet", "Free in BDO Pay from July 2026"],
        ["In store", "QR Ph", "Passed cards nationally in 2025"],
        ["Switching", "BancNet", "2.37bn transactions in 2024"],
    ],
    "sides": {
        "neo": {"dir": "ATM debit and remittances, Gold and Platinum Mastercard credit, and acceptance at BDO's terminals.",
                "deals": "What it does not do: InstaPay, PESONet and QR Ph, BDO Pay's own rails, fraud tools, or rewards."},
        "snb": {"dir": "Visa, Amex, JCB, UnionPay and Diners credit, Visa debit ⚠, BancNet switching, and the national instant and QR rails.",
                "deals": "Where they meet: BDO Pay, which carries cards of every brand next to free transfers."},
    },
    "tl": [
        ["2006", "BDO and Mastercard remittance partnership begins"],
        ["Mar 2014", "Visa payWave on BDO credit cards"],
        ["Mar 2016", "First EMV Mastercard ATM debit in the country"],
        ["Oct 2016", "Exclusive Diners Club issuer"],
        ["2017", "EMV Visa debit ⚠; JCB contactless and Platinum"],
        ["Dec 2021", "Account hack ⚠"],
        ["Jan 2026", "Visa signs RCBC debit"],
        ["May 2026", "20 years of BDO and Mastercard"],
        ["Jul 2026", "Fees waived; H1 profit ₱40.7bn"],
        ["Aug 2026", "BDO Pay named best wallet"],
    ],
    "l": {
        "U": {"d": 1, "s": "Debit holders and remittance families carry Mastercard.",
              "gap": "ATM cardholders and overseas Filipinos use Mastercard; credit cardholders split across six brands.",
              "neo": "ATM debit holders, remittance senders and receivers.", "snb": "Visa, Amex, JCB, UnionPay and Diners cardholders; BDO Pay transfer users."},
        "L5": {"d": 1, "s": "ATMs and offices abroad serve Mastercard cards.", "gap": "Branches, BDO Pay and BDO Online are BDO's own.",
               "neo": "ATMs, remittance offices.", "snb": "Branches, BDO Pay, BDO Online."},
        "L4": {"d": 0, "s": "The business lines carry no network.", "gap": "Accounts come with Mastercard or Visa debit ⚠; loans, trust and insurance have no network role.",
               "neo": "Debit on deposit accounts.", "snb": "Corporate, MSME, trust, insurance, capital markets."},
        "L3": {"d": 1, "s": "EMV debit is Mastercard's; fraud and rewards are BDO's.", "gap": "No public Mastercard fraud, data or offers work.",
               "neo": "EMV chip debit.", "snb": "Fraud, rewards, BDO Pay promotions."},
        "L2": {"d": 1, "s": "Debit and remittances on Mastercard; credit split; transfers domestic.", "gap": "Mastercard holds debit and remittances; QR Ph and InstaPay carry the growth.",
               "neo": "ATM debit, remittances, Mastercard credit.", "snb": "Visa and four other credit brands, InstaPay, PESONet, QR Ph, BancNet."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, SM Group, strategy, bonds."},
    },
    "t": area_lens(LAYERS),
}
