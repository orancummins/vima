"""Commonwealth Bank of Australia's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the FY26 results, profit announcement and
presentation (12 August 2026) and CommBank's product pages as read on 17 October 2026. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

ASX = "https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-ASX-Announcement.pdf"
PROFIT = "https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Profit-Announcement.pdf"
PRES = "https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Presentation.pdf"
COMPANY = "https://www.commbank.com.au/about-us/our-company.html"
ELTJUN = "https://www.commbank.com.au/articles/newsroom/2026/06/elt-update.html"
ELTSEP = "https://www.commbank.com.au/articles/newsroom/2026/09/commonwealth-bank-executive-team-update.html"
CREDIT = "https://www.commbank.com.au/credit-cards.html"
DEBIT = "https://www.commbank.com.au/banking/debit-mastercard.html"
BIZDEBIT = "https://www.commbank.com.au/business/bank-accounts/business-visa-debit-card.html"
BIZCREDIT = "https://www.commbank.com.au/business/business-credit-cards.html"
EFTPOS = "https://www.commbank.com.au/business/payments/eftpos-terminals.html"
PAYMENTS = "https://www.commbank.com.au/business/payments.html"
CTP = "https://www.commbank.com.au/digital-banking/click-to-pay.html"
BNPL = "https://www.commbank.com.au/banking/buy-now-pay-later.html"
YELLO = "https://www.commbank.com.au/commbank-yello.html"
VELOCITY = "https://travelweekly.com.au/velocity-frequent-flyer-and-commonwealth-bank-unveil-new-loyalty-offering/"
AGENTPAY = "https://www.mastercard.com/news/ap/en/newsroom/press-releases/en/2026/mastercard-accelerates-ai-powered-commerce-with-australia-s-first-authenticated-agentic-transactions-using-agent-pay/"
ACS = "https://ia.acs.org.au/article/2026/ai-shopping-arrives-in-australia--retailers-revolt.html"
RBAMR = "https://rba.gov.au/media-releases/2026/mr-26-10.html"
RBAIF = "https://www.rba.gov.au/payments-and-infrastructure/review-of-retail-payments-regulation/2026-03/conclusions-paper/interchange-fees.html"
APPLUS = "https://www.auspayplus.com.au/?p=8684"
OPENAI = "https://www.amlintelligence.com/2025/08/news-australias-commbank-partners-with-openai-to-fight-scams/"
SCAMS24 = "https://www.commbank.com.au/articles/newsroom/2024/11/CommBank-new-anti-scam-security-features.html"
BANKWEST = "https://www.bankwest.com.au/personal/credit-cards"
SAVVY = "https://www.savvy.com.au/bank-accounts/debit-cards/commbank/"
WIKI = "https://en.wikipedia.org/wiki/Commonwealth_Bank"
STEPPAY = "https://eastandpartners.com/news/cba-launches-steppay-bnpl-offering/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · brands · cloud core", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $1.45 trillion of assets and a 14.0% ROE, the main bank for one in three Australians, a bank founded in 1911, a core moved to the cloud, and AI partnerships with OpenAI and Anthropic.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Cash profit $11bn, ROE 14%.", "div": "cba", "rev": "corp", "products": [
            P("balance", "Balance sheet & earnings", "FY26 to 30 June 2026: cash NPAT $10,982 million (+7%), ROE 14.0%, NIM 2.05%, CET1 12.0%; total assets $1,452 billion, home loans $749 billion and customer deposits of about $1 trillion; dividend $5.05 a share. Rated AA/Aa2/AA-. Market value not confirmed ⚠.",
              s=["con"], neo=[0, ""], src=[["CBA FY26 results, Aug 2026", ASX], ["CBA FY26 profit announcement", PROFIT]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Comyn and O'Malley.", "div": "cba", "rev": "corp", "products": [
            P("leadership", "Board & executive team", "Chair Paul O'Malley, CEO Matt Comyn, CFO Alan Docherty, CRO Andrew Hinchliff; Angus Sullivan runs Retail, Michael Vacy-Lyle Business Banking; Victoria Ledda (CIO) and Rodrigo Castillo (CTO) from July 2026; Sinead Taylor leaves Institutional Banking to run ASB from 12 December 2026.",
              s=["corp"], st="flux", neo=[0, ""], src=[["CommBank: our company", COMPANY], ["CBA: ELT update, Jun 2026", ELTJUN], ["CBA: executive team update, Sep 2026", ELTSEP]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brands", "blurb": "Founded 1911.", "div": "cba", "rev": "rbs", "products": [
            P("brands", "Heritage & brands", "Founded under the Commonwealth Bank Act in 1911, privatised in the 1990s ⚠, Bankwest bought in 2008; today CommBank, Bankwest, Unloan, CommSec and ASB, with 51,714 staff and Australia's most valuable brand (Kantar, May 2026).",
              s=["con"], o="I", neo=[0, ""], src=[["CommBank: our company", COMPANY], ["Wikipedia: Commonwealth Bank", WIKI], ["CBA FY26 presentation", PRES]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Cloud core, $2.4bn a year.", "div": "cba", "rev": "corp", "products": [
            P("tech", "Cloud core & engineering", "SAP core banking migrated to the cloud, NetBank Next in staff pilot, a new CommBiz, and $2,428 million of investment spend in FY26 (to stay at about $2.4 billion in FY27); tech hubs in Seattle and San Francisco.",
              s=["corp"], neo=[0, ""], src=[["CBA FY26 presentation", PRES], ["CBA FY26 profit announcement", PROFIT]]),
            P("aipartners", "AI partnerships", "A multi-year OpenAI partnership (August 2025) on scam detection and ChatGPT Enterprise, an expanded Anthropic partnership, an AI Factory with AWS, and about 80% of staff using AI tools; ranked first in APAC for AI maturity ⚠.",
              s=["corp"], st="new", ay="Aug 2025", o="P", at="OpenAI, Anthropic, AWS", neo=[0, ""], src=[["AML Intelligence: CommBank and OpenAI, Aug 2025", OPENAI], ["CBA FY26 presentation", PRES]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & stakes", "blurb": "Grow at or above system.", "div": "cba", "rev": "corp", "products": [
            P("strategy", "Strategy", "Deepen main-bank relationships, keep discipline on volume and margin, raise productivity; in FY26 CBA grew at or above system in all five core domestic products, the first major bank to do so in 15 years.",
              s=["corp"], neo=[0, ""], src=[["CBA FY26 results, Aug 2026", ASX]]),
            P("stakes", "Stakes & disposals", "45% of Colonial First State, 42% of Lendi, 24% of PEXA, stakes in Payble, Gift Card Co and Silicon Quantum Computing, a Gemini stake revalued after its IPO; Vietnam International Bank and Bank of Hangzhou sold in 2025; CommInsure General Insurance sold.",
              s=["corp"], o="A", neo=[0, ""], src=[["CBA FY26 profit announcement", PROFIT], ["CBA FY26 presentation", PRES]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Debit Mastercard with eftpos on the card, Mastercard credit cards holding 29% of Australian balances, business cards split between Visa debit and Mastercard credit, terminals that take every network at 0.99%, PayTo and NPP payments, and Click to Pay and wallets.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Debit Mastercard, eftpos inside.", "div": "commbank", "rev": "rbs", "products": [
            P("debit", "CommBank Debit Mastercard", "The debit card for personal transaction accounts (Smart Access, Everyday Offset and others), from age 14, in Apple Pay, Google Pay and Samsung Pay; CBA is one of very few Australian banks with Mastercard on personal debit. eftpos sits on the card for domestic routing ⚠.", short="Debit Mastercard",
              s=["con"], lc="everyday", o="P", at="Mastercard, eftpos", neo=[1, "Mastercard, with eftpos on the card ⚠."],
              mc="Least-cost routing can send in-store debit to eftpos.",
              src=[["CommBank: Debit Mastercard", DEBIT], ["Savvy: CommBank debit cards, Oct 2022", SAVVY]]),
            P("worlddebit", "World Debit Mastercard", "A premium debit upgrade: Yello points on spend (up to 1.5 points per $1 abroad) and no international transaction fees for Yello Plus, Gold and Diamond customers.",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard World tier."], src=[["CommBank: Debit Mastercard", DEBIT]]),
            P("keycard", "Keycard", "An eftpos-only debit card that customers can upgrade to a Debit Mastercard.",
              s=["con"], lc="everyday", o="P", at="eftpos", neo=[0, "eftpos."], src=[["CommBank: Click to Pay", CTP]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit & instalments", "blurb": "29% of card balances.", "div": "commbank", "rev": "rbs", "products": [
            P("credit", "CommBank credit cards", "Low Rate, Low Fee, Interest-free Low Fee, CommBank Neo, Smart and Ultimate, all Mastercard, with 29.3% of Australian card balances (June 2026, up 1.1 points in a year); Smart and Ultimate earn Yello points, and their spend-based fee waiver ends on 1 January 2027.", short="Credit cards (Mastercard)",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "All on Mastercard."],
              mc="Australia's largest credit book, now under a 0.3% interchange cap.",
              src=[["CommBank: credit cards", CREDIT], ["CBA FY26 profit announcement", PROFIT]]),
            P("bankwestcards", "Bankwest credit cards", "Zero Platinum, Breeze Platinum, Bankwest Qantas and More World cards, all Mastercard.", short="Bankwest cards (Mastercard)",
              s=["con"], lc="borrow", o="A", at="Mastercard", div="bankwest", neo=[2, "Mastercard."], src=[["Bankwest: credit cards", BANKWEST]]),
            P("steppay", "StepPay, SurePay & Klarna", "StepPay splits purchases of $100 or more into four, anywhere, as a card in the app and wallets (launched 2021 ⚠); SurePay instalment plans on credit cards; and a Klarna partnership for pay-in-4.", short="StepPay (Mastercard ⚠)",
              s=["con"], lc="borrow", o="B", at="Klarna", neo=[1, "StepPay card on Mastercard ⚠; Klarna is not."], src=[["CommBank: buy now, pay later", BNPL], ["CommBank: Click to Pay", CTP], ["East & Partners: StepPay launch", STEPPAY]]),
        ]},
        {"id": "2.3", "ic": "briefcase-business", "name": "Business cards", "blurb": "Visa debit, Mastercard credit.", "div": "commbank", "rev": "bb", "products": [
            P("bizdebit", "Business Visa Debit Card", "The debit card for business transaction accounts, with Visa Commercial offers; a legacy Mastercard Business Debit card remains for some customers. Date of the move to Visa not found ⚠.", short="Business debit (Visa)",
              s=["sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="The one large Australian card programme Mastercard does not hold.",
              src=[["CommBank: Business Visa Debit Card", BIZDEBIT]]),
            P("bizcredit", "Business & corporate credit cards", "Business Low Rate, Interest-Free Days, Business Awards and Business Platinum, plus Corporate Low Rate, Corporate Interest-Free Days and Corporate Charge cards, with Yello points on business spend; Mastercard ⚠.", short="Business credit (Mastercard ⚠)",
              s=["sme", "corp"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard ⚠."], src=[["CommBank: business credit cards", BIZCREDIT]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acceptance", "blurb": "0.99% flat, every network.", "div": "merchant", "rev": "bb", "products": [
            P("acquiring", "EFTPOS terminals", "Smart, Smart Mini, Smart Integrated and Smart Hospitality terminals taking Mastercard, Visa, Amex, JCB, eftpos and UnionPay at a flat 0.99% (including Amex) from 1 October 2026, down from 1.10%, with same-day settlement and surcharging switched off. FY26 merchant income fell on higher scheme fees.", short="CommBank terminals",
              s=["sme"], lc="move", st="flux", o="B", neo=[1, "Accepts every network."],
              mc="Higher scheme fees cut merchant income in FY26.",
              src=[["CommBank: EFTPOS terminals, Oct 2026", EFTPOS], ["CBA FY26 profit announcement", PROFIT]]),
            P("online", "Online payments", "Payment gateways, billing and invoicing for e-commerce merchants, with same-day settlement before 5:30pm; acquiring market share not published ⚠.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["CommBank: business payments", PAYMENTS]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Account-to-account", "blurb": "PayTo, PayID, NameCheck.", "div": "commbank", "rev": "bb", "products": [
            P("payto", "PayTo", "Pre-authorised account-to-account collection for recurring, variable and one-off payments, offered to business customers on the NPP.",
              s=["sme", "corp"], lc="move", o="P", at="AP+", neo=[0, "NPP, run by AP+."],
              mc="An account-to-account alternative to cards for subscriptions and bills.",
              src=[["CommBank: business payments", PAYMENTS]]),
            P("fastpay", "Fast Payments & PayID", "Near real-time payments to NPP accounts by BSB and account number or PayID through CommBiz, and NameCheck to check account names before paying.",
              s=["sme", "con"], lc="move", o="P", at="AP+", neo=[0, "NPP."], src=[["CommBank: business payments", PAYMENTS]]),
        ]},
        {"id": "2.6", "ic": "smartphone", "name": "Wallets & Click to Pay", "blurb": "Tokens on every card.", "div": "commbank", "rev": "rbs", "products": [
            P("ctp", "Click to Pay", "Mastercard's online checkout for Debit Mastercard, World Debit Mastercard, Mastercard personal and business credit cards and the StepPay card, enrolled in the CommBank app with in-app approval on a new device (live by 2025 ⚠).", short="Click to Pay (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[3, "Mastercard Click to Pay."], src=[["CommBank: Click to Pay, Sep 2026", CTP]]),
            P("wallets", "Digital wallets & tokens", "Apple Pay, Google Pay and Samsung Pay on CommBank cards, a review of every wallet a card sits in, and alerts when a card is added to a new one (November 2024).",
              s=["con"], lc="everyday", o="P", at="Apple, Google, Samsung", neo=[1, "Mastercard tokens on Mastercard cards; Visa on business debit."],
              src=[["CommBank: anti-scam features, Nov 2024", SCAMS24], ["CommBank: Debit Mastercard", DEBIT]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: more than $1 billion a year against fraud and scams, ePassport checks, CommBank Companion and 1,000 machine-learning models, CommBank Yello with Velocity, and the first Agent Pay purchase in Australia.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud, scams & identity", "blurb": "$1bn+ a year.", "div": "cba", "rev": "rbs", "products": [
            P("fraud", "Fraud & scam defences", "More than $1 billion a year on fraud, scams, cyber and financial crime; about 52,000 payments blocked and 40,000 card alerts a day; AI cyber-defence agents and multi-agent fraud-rule tuning; intelligence shared through the Fintel Alliance.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, "CBA's own."],
              mc="No public Mastercard fraud or scam tool at CBA.",
              src=[["CBA FY26 presentation", PRES], ["CBA FY26 results, Aug 2026", ASX]]),
            P("warnings", "Payment warnings", "Intelligent warnings on certain first-time payments, more than 5.9 million since September 2024, plus wallet reviews and alerts.",
              s=["con"], lc="move", ay="Sep 2024", o="B", neo=[0, "CBA's own."], src=[["CBA FY26 results, Aug 2026", ASX], ["CommBank: anti-scam features, Nov 2024", SCAMS24]]),
            P("identity", "Identity & NameCheck", "ePassport verification in the app (an Australian banking first), new identity and verification platforms, and NameCheck for business payees.",
              s=["con", "sme"], lc="open", o="B", neo=[0, ""], src=[["CBA FY26 presentation", PRES], ["CommBank: business payments", PAYMENTS]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "AI & insights", "blurb": "CommBank Companion.", "div": "commbank", "rev": "rbs", "products": [
            P("companion", "CommBank Companion", "An AI-powered conversational experience in the app: in pilot with select retail customers and rolled out to about 100,000 small businesses, with straight-through lending for some products.",
              s=["con", "sme"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="An assistant that could pay on the customer's behalf.",
              src=[["CBA FY26 presentation", PRES]]),
            P("cee", "Customer Engagement Engine", "More than 1,000 machine-learning models choosing the next message or offer for each customer; agentic messaging resolves 86% of chats without a person.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["CBA FY26 presentation", PRES]]),
            P("insights", "Money management", "Benefit Finder, Bill Sense, Cash Flow View, budgets, goals and Money Insights, used by more than 3.4 million customers a month.",
              s=["con"], lc="grow", o="B", neo=[0, ""], src=[["CBA FY26 presentation", PRES]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Yello & offers", "blurb": "Velocity joins.", "div": "commbank", "rev": "rbs", "products": [
            P("yello", "CommBank Yello", "Four-tier rewards since November 2023 (more than $240 million of benefits): points on cards, World Debit Mastercard, insurance, loans and CommSec trading; transfers to airlines and Everyday Rewards; Mastercard Presale and Preferred Tickets; Yello for Business.",
              s=["con", "sme"], lc="grow", o="B", neo=[1, "Mastercard Presale tickets inside Yello."],
              mc="Higher loyalty costs already weigh on card fees.",
              src=[["CommBank: Yello, Oct 2026", YELLO], ["CBA FY26 presentation", PRES]]),
            P("velocity", "Velocity in Yello", "Virgin Australia's Velocity joins Yello for more than nine million customers; from 1 October 2026 points earned on savings, home loans, insurance and cards convert to Velocity Points.",
              s=["con"], lc="grow", st="new", ay="Oct 2026", o="P", at="Velocity", neo=[0, ""], src=[["Travel Weekly: Velocity and CommBank, Aug 2026", VELOCITY]]),
        ]},
        {"id": "3.4", "ic": "bot", "name": "Agentic commerce", "blurb": "Australia's first Agent Pay.", "div": "commbank", "rev": "rbs", "products": [
            P("agentpay", "Agent Pay on a CBA debit card", "On 28 January 2026 an AI agent used a CBA-issued debit card to buy Event Cinemas tickets, Australia's first authenticated agentic transaction on Mastercard Agent Pay; CBA, the merchant and Mastercard all saw it was agent-led.", short="Agent Pay (Mastercard)",
              s=["con"], lc="everyday", st="new", ay="Jan 2026", o="P", at="Mastercard, IPSI, Maincode", neo=[3, "Mastercard Agent Pay."],
              mc="The first proof point; not yet a CBA product.",
              src=[["Mastercard: Agent Pay in Australia, Jan 2026", AGENTPAY], ["ACS: AI shopping arrives, Jan 2026", ACS]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: a quarter of Australia's home loans and household deposits, everyday accounts and personal loans, business and institutional banking, CommSec, and ASB in New Zealand.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Home loans", "blurb": "$749bn, 25% share.", "div": "commbank", "rev": "rbs", "products": [
            P("homeloans", "Home loans", "$749 billion and 25.4% of the market; about 70% of proprietary applications decided the same day, 96% settled digitally, and 1.3 million customers managing their loan in the app.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["CBA FY26 profit announcement", PROFIT], ["CBA FY26 presentation", PRES]]),
            P("unloan", "Unloan", "A digital-only home-loan brand reported within Retail Banking Services; CBA and Unloan branded loans make up 64–65% of proprietary home-loan flows.",
              s=["home"], lc="borrow", o="B", div="unloan", neo=[0, ""], src=[["CBA FY26 profit announcement", PROFIT]]),
        ]},
        {"id": "4.2", "ic": "user-round", "name": "Everyday banking", "blurb": "1 in 3 Australians.", "div": "commbank", "rev": "rbs", "products": [
            P("accounts", "Transaction accounts & deposits", "Main bank for one in three Australians (retail MFI share 34.2%), 26.4% of household deposits and 655,000 more retail transaction accounts in FY26.",
              s=["con"], lc="everyday", neo=[1, "Debit Mastercard, eftpos inside ⚠."], src=[["CBA FY26 presentation", PRES], ["CBA FY26 profit announcement", PROFIT]]),
            P("personal", "Personal loans & consumer finance", "$17.4 billion of consumer finance; personal-loan arrears rose to 1.72% in FY26.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["CBA FY26 profit announcement", PROFIT]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Business Banking", "blurb": "1 in 4 businesses.", "div": "commbank", "rev": "bb", "products": [
            P("business", "Business Banking", "Main bank for one in four Australian businesses (MFI share 26.0%), $4.5 billion cash profit (+11%) and business lending 1.3 times system, across small business, commercial, regional and agribusiness clients.",
              s=["sme"], lc="everyday", neo=[1, "Visa debit, Mastercard credit."], src=[["CBA FY26 presentation", PRES], ["CBA FY26 profit announcement", PROFIT]]),
            P("stream", "Stream Working Capital & BizExpress", "Stream (more than $400 million committed), auto-decisioned small-business loans up more than two times since FY23, and simple annual reviews.",
              s=["sme"], lc="borrow", o="B", neo=[0, ""], src=[["CBA FY26 presentation", PRES]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "Institutional & markets", "blurb": "$66bn operational deposits.", "div": "cba", "rev": "ibm", "products": [
            P("ibm", "Institutional Banking and Markets", "Transaction banking, markets and CommBank iQ insights: $1.26 billion cash profit, operational deposits $66 billion (+13%) and 33 more transaction-banking mandates in FY26.",
              s=["corp"], lc="move", neo=[0, ""], src=[["CBA FY26 presentation", PRES]]),
        ]},
        {"id": "4.5", "ic": "chart-candlestick", "name": "CommSec", "blurb": "Investing from $2.", "div": "commsec", "rev": "bb", "products": [
            P("commsec", "CommSec & Everyday Investing", "Australia's leading retail broker (3.6% of all equities traded), CommSec Pocket and Everyday Investing from $2; net interest income up 34% in FY26.",
              s=["inv"], lc="grow", neo=[0, ""], src=[["CBA FY26 profit announcement", PROFIT], ["CBA FY26 presentation", PRES]]),
        ]},
        {"id": "4.6", "ic": "earth", "name": "ASB New Zealand", "blurb": "A$1.1bn profit.", "div": "asb", "rev": "nz", "products": [
            P("asb", "ASB Bank", "A$1,112 million cash profit, 21.3% of NZ home loans and 18.9% of deposits; Digital Bank of the Year four years running; cards income down on lower interchange. Cards believed to be on Visa ⚠.",
              s=["kiwi"], lc="everyday", st="flux", neo=[0, "Visa ⚠."], src=[["CBA FY26 profit announcement", PROFIT], ["CBA FY26 presentation", PRES]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the CommBank app for 9.6 million, NetBank and CommBiz, 640 branches and 1,770 ATMs, and brokers, Lendi and PEXA.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "CommBank app & online", "blurb": "9.6m app users.", "div": "commbank", "rev": "rbs", "products": [
            P("app", "CommBank app", "Australia's most popular banking app: more than 9.6 million active users and 14.3 million daily logins.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["CBA FY26 presentation", PRES]]),
            P("netbank", "NetBank & CommBiz", "NetBank Next in advanced staff pilot and a new mobile and web CommBiz for business and institutional clients.",
              s=["sme", "corp"], lc="everyday", st="new", neo=[0, ""], src=[["CBA FY26 presentation", PRES]]),
            P("travel", "Travel Booking & car buying", "Book flights, hotels and cars in the app (gross booking value up 2.7 times) and find, finance and manage a car; more than a million customers engaging.",
              s=["con"], lc="beyond", st="new", o="P", at="Hopper", neo=[0, ""], src=[["CBA FY26 presentation", PRES], ["CommBank: credit cards", CREDIT]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "640 branches.", "div": "commbank", "rev": "rbs", "products": [
            P("branches", "Branches, ATMs & contact centres", "About 640 branches and 1,770 ATMs, a further $140 million for the service network (June 2026), and messaging and voice support around the clock.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["CBA FY26 profit announcement", PROFIT], ["CBA FY26 results, Aug 2026", ASX]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Brokers & partners", "blurb": "Lendi, PEXA.", "div": "cba", "rev": "rbs", "products": [
            P("brokers", "Brokers & partners", "Mortgage brokers for about a third of home-loan flows, a 42% stake in Lendi, PEXA for digital settlement, and accredited POS vendors for merchants.",
              s=["home", "sme"], lc="open", o="P", at="Lendi, PEXA", neo=[0, ""], src=[["CBA FY26 profit announcement", PROFIT], ["CBA FY26 presentation", PRES]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at CommBank", "blurb": "Cards on Mastercard, eftpos alongside.", "products": [
        P("mcatcba", "Mastercard at CommBank", "Mastercard carries CBA's consumer debit and every consumer credit card (29.3% of Australian balances), Bankwest's cards, business credit and StepPay; Click to Pay is live and a CBA debit card made Australia's first Agent Pay purchase in January 2026. eftpos sits on the debit cards, Visa has business debit and ASB ⚠, and PayTo and NPP belong to AP+.",
          s=["con"], div="cba", rev="corp", mc="The relationship this map is drawn for.",
          src=[["CommBank: credit cards", CREDIT], ["CommBank: Debit Mastercard", DEBIT], ["Mastercard: Agent Pay in Australia, Jan 2026", AGENTPAY]]),
    ]},
    {"id": "pillar-market", "name": "Australian payments", "blurb": "Surcharge ban, lower caps.", "products": [
        P("market", "The Australian market", "From 1 October 2026 the RBA removed surcharging on eftpos, Mastercard and Visa cards and cut caps to 8 cents/0.16% for debit and 0.3% for consumer credit; a 1.0% cap on foreign cards follows on 1 April 2027. AP+ runs eftpos, NPP and PayTo, and least-cost routing cuts debit costs by nearly 20%.",
          s=["con"], div="cba", rev="corp",
          src=[["RBA: conclusions, Mar 2026", RBAMR], ["RBA: interchange fees, Mar 2026", RBAIF], ["AP+: eftpos zero-surcharge, Jun 2026", APPLUS]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
