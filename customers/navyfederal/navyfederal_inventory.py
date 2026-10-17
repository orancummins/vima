"""Navy Federal Credit Union's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the credit union's own unless a source says otherwise: the Q2 2026 statements of financial condition
and income (30 June 2026), the 2026 fact sheet (22 September 2026) and the 2025 annual report (May 2026).
Navy Federal is member-owned and reports no segments; ``rev`` follows its loan classes. ``neo`` is the Mastercard
lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

ABOUT = "https://www.navyfederal.org/about/about.html"
FACT = "https://www.navyfederal.org/content/dam/nfculibs/pdfs/fact-sheet/FactSheet-09-2026.pdf"
SFC = "https://www.navyfederal.org/content/dam/nfculibs/pdfs/financial-reports/SFC_Q2_26.pdf"
SOI = "https://www.navyfederal.org/content/dam/nfculibs/pdfs/financial-reports/SOI_Q2_26.pdf"
OPS = "https://www.navyfederal.org/about/operations.html"
AR25 = "https://www.navyfederal.org/content/dam/nfculibs/pdfs/financial-reports/2025-annual-report.pdf"
PRESS = "https://www.navyfederal.org/about/press-releases.html"
CEO = "https://www.navyfederal.org/about/press-releases/2024/dietrich-kuhlmann-new-navy-federal-ceo-effective-march-2024.html"
CARDS = "https://www.navyfederal.org/loans-cards/credit-cards.html"
CASHR = "https://www.navyfederal.org/loans-cards/credit-cards/cash-rewards.html"
GOR = "https://www.navyfederal.org/loans-cards/credit-cards/go-rewards.html"
PLAT = "https://www.navyfederal.org/loans-cards/credit-cards/platinum.html"
SECURED = "https://www.navyfederal.org/loans-cards/credit-cards/cash-rewards-secured.html"
SECPR = "https://www.navyfederal.org/about/press-releases/2025-press-releases/navy-federal-credit-union-launches-cashrewards-secured-credit-card.html"
FLAG = "https://www.navyfederal.org/about/press-releases/2026-press-releases/Flagship-Premier-Launch.html"
MORE = "https://www.navyfederal.org/loans-cards/credit-cards/more-rewards.html"
AMEX17 = "https://www.placera.se/pressmeddelanden/more-rewards-in-store-for-navy-federal-members-with-new-american-express-card-2017-05-09"
BIZCARDS = "https://www.navyfederal.org/services/business/credit-cards.html"
BIZCHK = "https://www.navyfederal.org/services/business/checking-savings.html"
PARTNERS = "https://www.navyfederal.org/services/business/partners.html"
DEBIT = "https://www.navyfederal.org/checking-savings/checking/debit.html"
PREPAID = "https://www.navyfederal.org/checking-savings/cards/go-prepaid.html"
GIFT = "https://www.navyfederal.org/checking-savings/cards/gift-cards.html"
ZELLE = "https://www.navyfederal.org/services/transfers/zelle.html"
MOBILE = "https://www.navyfederal.org/services/mobile-online-banking.html"
ENH = "https://www.navyfederal.org/about/press-releases/2025-press-releases/navy-federal-unveils-new-enhancements.html"
CURQL = "https://www.navyfederal.org/about/press-releases/2025-press-releases/navy-federal-credit-union-joining-curql-collective.html"
VISA09 = "https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.7971.html"
TSYS = "https://www.globalcustodian.com/navy-federal-credit-union-and-tsys-renew-processing-agreement/"
OBT = "https://openbankingtracker.com/mastercard-open-banking/navy-federal-credit-union"
CUBE = "https://www.americanbanker.com/payments/news/navy-fcu-adds-cube-ai-to-battle-payment-crime"
DIGI = "https://www.multimodal.dev/mainstreetai/inside-navy-federals-digital-banking-strategy-at-15-million-members"
DBX = "https://databricks.com/customers/navy-federal-credit-union"
DARK = "https://www.cuinsight.com/press-release/navy-federal-credit-union-renews-its-contract-with-dark-matter-technologies-to-serve-its-growing-membership/"
CFPB = "https://www.cpapracticeadvisor.com/2024/11/11/cfpb-orders-navy-federal-credit-union-to-pay-more-than-95-million-for-surprise-overdraft-fees/152157/"
CFPBEND = "https://www.militarytimes.com/pay-benefits/mil-money/2025/07/17/senators-criticize-cfpb-for-dropping-action-on-troops-overdraft-fees/"
SETTLE = "https://www.digitaltransactions.net/merchants-look-forward-to-their-day-in-court-after-judge-brodie-rejects-the-interchange-settlement/"
LAWSUIT = "https://blogs.duanemorris.com/classactiondefense/2024/06/06/virginia-federal-court-rejects-class-claims-in-navy-discrimination-suit/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "members · charter · balance sheet", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: 15.5 million members, $204 billion of assets and $1.4 billion of net income in the first half of 2026, a member-owned charter from 1933, a field of membership drawn from the military, a rebuilt app, and conduct cases from 2023–24.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & members", "blurb": "$204bn, 15.5 million members.", "div": "nfcu", "rev": "cu", "products": [
            P("balance", "Balance sheet & earnings", "Assets of $204.4 billion, loans of $147.7 billion, deposits of $173.4 billion and members' equity of $20.0 billion at 30 June 2026, with 15.5 million members; net income $1.41 billion in the half and $1.91 billion in 2025, when the net worth ratio was 11.36%. Not listed and not rated in public sources ⚠.",
              s=["mil", "vet"], neo=[0, ""], src=[["Q2 2026 statement of financial condition", SFC], ["Q2 2026 statement of income", SOI], ["Operating statistics, Q2 2026", OPS], ["2025 annual report", AR25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Kuhlmann and Cochrane.", "div": "nfcu", "rev": "cu", "products": [
            P("leadership", "Board & executives", "President and CEO Dietrich Kuhlmann, a retired rear admiral, since March 2024 (succeeding Mary McDuffie); Chair Edward Cochrane Jr.; CFO John Collins; chief lending officer Aaron Aggerwal; a volunteer board drawn largely from retired officers, with a Supervisory Committee and PwC as auditor.",
              s=["mil"], neo=[0, ""], src=[["Navy Federal: new CEO, Feb 2024", CEO], ["Q2 2026 statement of financial condition", SFC], ["Curql release, Mar 2025", CURQL], ["2025 annual report", AR25]]),
        ]},
        {"id": "1.3", "ic": "flag", "name": "Charter & membership", "blurb": "Seven members in 1933.", "div": "nfcu", "rev": "cu", "products": [
            P("heritage", "Charter & field of membership", "Founded in 1933 by seven Navy Department employees; now the world's largest credit union, member-owned and not-for-profit, open to Department of Defense and Coast Guard personnel, veterans, DoD civilians and contractors and their families. Members earned or saved about $4.53 billion in value in 2025, by its own study.",
              s=["mil", "vet"], o="I", neo=[0, ""], src=[["Navy Federal: about", ABOUT], ["Fact sheet, Sep 2026", FACT]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & partners", "blurb": "New app, Databricks, Curql.", "div": "nfcu", "rev": "cu", "products": [
            P("tech", "Digital platform, data & AI", "Mobile app and online banking rebuilt (2025 was the first full year on the new platform), features shipped about every two weeks, generative and agentic AI on Databricks on Azure ⚠ vendor case study, and Dark Matter's Empower system for about 8,000 home loans a month ⚠.",
              s=["mil"], st="new", o="P", at="Databricks, Dark Matter", neo=[0, ""], src=[["2025 annual report", AR25], ["Main Street AI: SVP Digital, Jun 2026", DIGI], ["Databricks: Navy Federal", DBX], ["CUInsight: Dark Matter renewal", DARK]]),
            P("curql", "Curql Collective", "Joined the Curql Collective and invested in Curql Fund II (March 2025), backing fintechs in lending automation, fraud prevention, cybersecurity and member experience.",
              s=["mil"], st="new", ay="Mar 2025", o="P", at="Curql", neo=[0, ""], src=[["Curql release, Mar 2025", CURQL]]),
        ]},
        {"id": "1.5", "ic": "scroll-text", "name": "Regulation & conduct", "blurb": "CFPB order, fair-lending suit.", "div": "nfcu", "rev": "cu", "products": [
            P("conduct", "Regulators & cases", "Supervised by the NCUA. The CFPB ordered more than $80 million of refunds and a $15 million penalty over overdraft fees (November 2024), then ended the order in mid-2025 ⚠ date varies by source; a fair-lending class action filed in December 2023 continues on disparate-impact claims.",
              s=["home", "mil"], st="flux", neo=[0, ""], src=[["CPA Practice Advisor: CFPB order, Nov 2024", CFPB], ["Military Times: order dropped, Jul 2025", CFPBEND], ["Duane Morris: fair-lending ruling, Jun 2024", LAWSUIT]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Five ways money moves: Visa debit for 11 million checking accounts, everyday credit cards issued on Visa or Mastercard, a new premium Visa Signature card and an Amex card, Zelle and instant payments, and the processors behind them.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit & prepaid", "blurb": "3.7bn Visa debit payments.", "div": "cards", "rev": "deposits", "products": [
            P("debit", "Visa debit card", "Every checking account comes with a contactless Visa debit card with an instant digital card number, in Apple Pay, Google Pay, Samsung Pay and Amazon One; a record 3.7 billion debit transactions in 2025, up 8.5%.", short="Debit (Visa)",
              s=["mil", "vet", "student"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="The largest flow of payments at the credit union, and Visa's.",
              src=[["Navy Federal: debit card", DEBIT], ["2025 annual report", AR25]]),
            P("prepaid", "GO Prepaid & gift cards", "A reloadable GO Prepaid card usable wherever Visa debit is accepted, and Navy Federal Visa Gift Cards, now also digital.",
              s=["student", "vet"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Navy Federal: GO Prepaid", PREPAID], ["Navy Federal: gift cards", GIFT]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Everyday credit", "blurb": "Visa or Mastercard.", "div": "cards", "rev": "card", "products": [
            P("cashrewards", "cashRewards & cashRewards Plus", "1.5% or 2% cash back with no annual fee; the most popular card, with 321,000 opened in 2025. Issued as cashRewards Visa or Mastercard, and cashRewards Plus as Visa Signature or World Mastercard; the split is not published ⚠.", short="cashRewards (Visa or Mastercard)",
              s=["mil", "vet"], lc="borrow", o="B", at="Visa, Mastercard", neo=[1, "Visa or Mastercard; split not published ⚠."],
              mc="The biggest Mastercard credit programme at Navy Federal.",
              src=[["Navy Federal: cashRewards", CASHR], ["2025 annual report", AR25]]),
            P("goplat", "GO REWARDS & Platinum", "GO REWARDS earns 3X at restaurants and 2X on gas; Platinum carries the lowest rate (from 10.24%) and no balance-transfer fees. Both have Visa and Mastercard versions (World Mastercard for GO REWARDS) ⚠ split unknown.", short="GO REWARDS & Platinum (Visa or Mastercard)",
              s=["vet", "driver"], lc="borrow", o="B", at="Visa, Mastercard", neo=[1, "Visa or Mastercard ⚠."], src=[["Navy Federal: GO REWARDS", GOR], ["Navy Federal: Platinum", PLAT], ["Navy Federal: credit cards", CARDS]]),
            P("secured", "cashRewards Secured", "Launched April 2025: 1% back from a $200 deposit, reviewed for an unsecured cashRewards card after six months; benefits listed for Visa and Mastercard versions ⚠.",
              s=["student"], lc="borrow", st="new", ay="Apr 2025", o="B", neo=[1, "Visa or Mastercard ⚠."], src=[["Navy Federal: cashRewards Secured launch, Apr 2025", SECPR], ["Navy Federal: cashRewards Secured", SECURED]]),
        ]},
        {"id": "2.3", "ic": "gem", "name": "Premium & Amex", "blurb": "Flagship Premier on Visa.", "div": "cards", "rev": "card", "products": [
            P("flagship", "Flagship Premier Visa Signature", "Launched 10 September 2026, Navy Federal's first metal card: $95 a year, 4X on travel, 3X on dining, a $100 airline credit and Global Entry or TSA PreCheck credit; Flagship Rewards holders can switch without applying.", short="Flagship Premier (Visa)",
              s=["vet", "mil"], lc="borrow", st="new", ay="Sep 2026", o="P", at="Visa", neo=[0, "Visa."],
              mc="The newest premium card went to Visa.",
              src=[["Navy Federal: Flagship Premier launch, Sep 2026", FLAG], ["Navy Federal: credit cards", CARDS]]),
            P("morerewards", "More Rewards American Express Card", "Announced May 2017 and serviced by Navy Federal on the Amex network: 3X at restaurants, supermarkets, gas and transit, no annual fee.",
              s=["vet"], lc="borrow", ay="May 2017", o="P", at="American Express", neo=[0, "American Express."], src=[["Amex and Navy Federal, May 2017", AMEX17], ["Navy Federal: More Rewards", MORE]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "Transfers & real-time", "blurb": "Zelle, RTP and FedNow.", "div": "nfcu", "rev": "deposits", "products": [
            P("zelle", "Zelle & member transfers", "Zelle in the app, with QR codes and no fee, alongside member-to-member transfers; 1 billion non-card transactions worth $689.2 billion in 2025.",
              s=["mil", "vet"], lc="move", o="P", at="Zelle", neo=[0, "Zelle."], src=[["Navy Federal: Zelle", ZELLE], ["2025 annual report", AR25]]),
            P("rtp", "RTP & FedNow", "21.4 million instant payments worth $7.7 billion through RTP and FedNow in 2025, and growing.",
              s=["mil", "biz"], lc="move", st="new", neo=[0, ""],
              mc="Instant payments bring scam risk that card-style fraud scores could cover.",
              src=[["2025 annual report", AR25]]),
        ]},
        {"id": "2.5", "ic": "network", "name": "Processing & acceptance", "blurb": "TSYS, Global Payments.", "div": "nfcu", "rev": "card", "products": [
            P("processing", "Card processing", "TSYS processed Navy Federal's Visa and MasterCard credit cards under a renewal in April 2009 (then 850,000 active accounts) ⚠ current status; Visa's February 2009 renewal covered consumer credit, debit, prepaid and small business.",
              s=["mil"], lc="move", ay="Feb 2009", o="P", at="TSYS, Visa", neo=[1, "Mastercard credit processed alongside Visa ⚠."], src=[["TSYS renewal, Apr 2009", TSYS], ["Visa: Navy Federal renewal, Feb 2009", VISA09]]),
            P("merchant", "Merchant services for members", "Global Payments Merchant Solutions for business members, with up to ten POS stations for $0 upfront (2026), plus Paychex payroll and Harland Clarke checks.",
              s=["biz"], lc="move", o="P", at="Global Payments", neo=[1, "Accepts every network."], src=[["Navy Federal: business partners", PARTNERS]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: 24/7 fraud monitoring and AI bots that chase scam accounts, generative AI with a human in the loop, credit-building and money tools including a Mastercard open-banking link, and card rewards worth billions to members.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & scams", "blurb": "AI bots chase scammers.", "div": "nfcu", "rev": "deposits", "products": [
            P("fraud", "Fraud monitoring & security", "24/7 fraud monitoring, real-time alerts, two-factor and voice authentication and new security hubs; 6,700 social-media scam accounts and posts removed in 2025, up 32%.",
              s=["mil", "vet"], lc="everyday", o="B", neo=[0, "Navy Federal's own."], src=[["2025 annual report", AR25], ["Fact sheet, Sep 2026", FACT]]),
            P("cube", "Cube AI scam bots", "AI bots that pose as victims on accounts flagged as likely scam accounts so payments to them are cut off, and that read context for unusual military payments (reported October 2026).",
              s=["mil"], lc="everyday", st="new", ay="Oct 2026", o="P", at="Cube", neo=[0, ""],
              mc="Buying scam tools now; Mastercard's account-to-account scam scoring is not in use.",
              src=[["American Banker: Cube AI, Oct 2026", CUBE]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "Data & AI", "blurb": "Human in the loop.", "div": "nfcu", "rev": "cu", "products": [
            P("ai", "Generative & agentic AI", "Generative and agentic AI on Databricks ⚠ vendor-stated, a chatbot that hands to staff, and AI disclosed to members with humans in the loop; the five-year aim is an 'interaction continuum' across digital, conversational and human channels.",
              s=["mil", "vet"], lc="everyday", st="new", o="P", at="Databricks", neo=[0, ""],
              mc="Agentic AI with no agentic payment tokens yet.",
              src=[["Main Street AI: SVP Digital, Jun 2026", DIGI], ["Databricks: Navy Federal", DBX]]),
        ]},
        {"id": "3.3", "ic": "chart-column", "name": "Money tools & open banking", "blurb": "Bloom+, Mastercard link.", "div": "nfcu", "rev": "deposits", "products": [
            P("bloom", "Bloom+ & Credit Confidence", "Bloom+ reports rent and utility payments from checking to a credit bureau (with Bloom Credit, April 2025), next to the Mission: Credit Confidence score dashboard.",
              s=["student", "vet"], lc="borrow", st="new", ay="Apr 2025", o="P", at="Bloom Credit", neo=[0, ""], src=[["Navy Federal: checking enhancements, Apr 2025", ENH], ["2025 annual report", AR25]]),
            P("makingcents", "My MakingCents", "Free money management: spending tracking, budgets, credit scores and accounts held at other banks in one view.",
              s=["vet", "saver"], lc="grow", o="B", neo=[0, ""], src=[["Navy Federal: checking enhancements, Apr 2025", ENH]]),
            P("openbanking", "Open-banking connections", "Navy Federal accounts connect to third-party apps through Mastercard Open Banking (formerly Finicity) as a direct API, according to trackers ⚠ not confirmed by either party.",
              s=["vet", "biz"], lc="open", o="P", at="Mastercard", neo=[3, "Mastercard Open Banking ⚠ third-party source."], src=[["Open Banking Tracker: Mastercard Open Banking", OBT]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards & member value", "blurb": "$976m interchange, net.", "div": "cards", "rev": "card", "products": [
            P("rewards", "Card rewards & member giveback", "Points and cash back on every rewards card, reported net of interchange: $975.7 million of net interchange income in 2025 and $528 million in the first half of 2026; members earned or saved about $4.53 billion in value in 2025.",
              s=["mil", "vet"], lc="grow", o="B", neo=[1, "Rewards ride whichever network the card is on."],
              mc="Card-linked offers could add to member value without adding rewards cost.",
              src=[["2025 annual report", AR25], ["Q2 2026 statement of income", SOI], ["Fact sheet, Sep 2026", FACT]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What members buy: 11 million checking accounts and $166.6 billion of savings, $107.8 billion of real estate lending, $43.3 billion of auto and personal loans, Business Solutions for 638,700 business members, and investments.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Checking & savings", "blurb": "11 million active accounts.", "div": "nfcu", "rev": "deposits", "products": [
            P("checking", "Checking", "11 million active checking accounts (up 8% in 2025): Active Duty, Flagship, Everyday, Easy and Campus Checking, early release of military direct deposits and no NSF fees.",
              s=["mil", "student"], lc="everyday", neo=[0, "Visa debit."], src=[["2025 annual report", AR25], ["Navy Federal: checking enhancements, Apr 2025", ENH], ["Fact sheet, Sep 2026", FACT]]),
            P("savings", "Savings & certificates", "Savings balances of $166.6 billion at end-2025, 40% in term products, with EasyStart certificates paying up to 4.4% from $50.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["2025 annual report", AR25]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Mortgages & equity", "blurb": "$107.8bn of real estate.", "div": "mortgage", "rev": "realestate", "products": [
            P("mortgage", "Mortgages & home equity", "Real estate lending of $107.8 billion (2025), with mortgages including serviced-sold loans at $98.6 billion and equity lending at $9.2 billion; VA loans, no-money-down options and no PMI, and Homebuyers Choice enhanced in April 2026.",
              s=["home", "mil"], lc="borrow", neo=[0, ""], src=[["2025 annual report", AR25], ["Navy Federal: press releases", PRESS]]),
        ]},
        {"id": "4.3", "ic": "trending-up", "name": "Auto, personal & student", "blurb": "$33.1bn of auto loans.", "div": "nfcu", "rev": "consumer", "products": [
            P("auto", "Auto loans", "Auto outstandings of $33.1 billion and originations of $15.2 billion in 2025 across 500,000 purchase and refinance loans.",
              s=["driver"], lc="borrow", neo=[0, ""], src=[["2025 annual report", AR25]]),
            P("personal", "Personal loans & shutdown advances", "Consumer lending of $43.3 billion including personal loans, and $352.4 million of paycheck advances to federal workers during the 43-day shutdown in late 2025.",
              s=["mil", "vet"], lc="borrow", neo=[0, ""], src=[["2025 annual report", AR25]]),
            P("student", "Student loans", "A $1.3 billion student portfolio, with a Graduate Student Loan launched in August 2025 that reached 24% of applications by year-end.",
              s=["student"], lc="borrow", st="new", ay="Aug 2025", neo=[0, ""], src=[["2025 annual report", AR25]]),
        ]},
        {"id": "4.4", "ic": "briefcase", "name": "Business Solutions", "blurb": "638,700 business members.", "div": "business", "rev": "deposits", "products": [
            P("business", "Business checking & loans", "638,700 business members (up 9.2% in 2025), $1.3 billion of business loans and $3.4 billion of business savings; three checking tiers with a GO BIZ debit card ⚠ network not stated.",
              s=["biz"], lc="everyday", neo=[None, "Debit network not stated."], src=[["2025 annual report", AR25], ["Navy Federal: business checking", BIZCHK]]),
            P("gobiz", "GO BIZ Rewards credit card", "A business credit card 'available as Visa or Mastercard', with no foreign transaction fees, unlimited points and Mastercard ID Theft Protection on the Mastercard version.", short="GO BIZ (Visa or Mastercard)",
              s=["biz"], lc="borrow", o="B", at="Visa, Mastercard", neo=[1, "Visa or Mastercard."],
              mc="Commercial controls and data could sit on the Mastercard version.",
              src=[["Navy Federal: business credit cards", BIZCARDS]]),
        ]},
        {"id": "4.5", "ic": "coins", "name": "Investments & insurance", "blurb": "NFIS, $7.4bn.", "div": "nfis", "rev": "cu", "products": [
            P("nfis", "Navy Federal Investment Services", "Brokerage, advice and insurance through Navy Federal Financial Group and its broker-dealer NFIS: $7.4 billion administered at end-2025, up 22%, and Digital Investor accounts up 15%.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["2025 annual report", AR25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How members reach Navy Federal: the app for 12.2 million, 392 branches with 178 on or near bases, banks on 60 overseas installations for the Department of Defense, and a 24/7 contact centre.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App & online", "blurb": "12.2 million users.", "div": "nfcu", "rev": "cu", "products": [
            P("app", "Mobile app & online banking", "Used by 12.2 million members, about 80%, 3.1 billion times in 2025; more than 10 million log in each month, with card freeze, digital wallets and Trusted User access for family and business users.",
              s=["mil", "vet", "student"], lc="everyday", o="B", neo=[0, ""], src=[["2025 annual report", AR25], ["Navy Federal: mobile and online banking", MOBILE], ["Main Street AI: SVP Digital, Jun 2026", DIGI]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "392 locations.", "div": "nfcu", "rev": "cu", "products": [
            P("branches", "Branches & ATMs", "392 locations worldwide at September 2026, 178 on or near military installations and 27 international, plus more than 30,000 free ATMs; 23 million branch visits in 2025.",
              s=["mil", "home"], lc="open", neo=[0, ""], src=[["Fact sheet, Sep 2026", FACT], ["2025 annual report", AR25]]),
        ]},
        {"id": "5.3", "ic": "earth", "name": "Overseas & military", "blurb": "60 bases abroad.", "div": "ombp", "rev": "cu", "products": [
            P("ombp", "Overseas Military Banking Program", "Since 2024 Navy Federal runs the Department of Defense's Community Bank locations on about 60 overseas installations, with branches and ATMs in 10 countries and territories; fees are reinvested in military charities.",
              s=["mil"], lc="open", st="new", o="P", at="Department of Defense", neo=[0, ""],
              mc="Members abroad need cross-border transfers and FX.",
              src=[["Fact sheet, Sep 2026", FACT], ["2025 annual report", AR25]]),
            P("msp", "Military Affairs & Strategic Partnerships", "A unit formed in May 2025 to unify outreach and partnerships with military organisations, led from October 2026 by SVP Elizabeth O'Brien.",
              s=["mil", "vet"], lc="beyond", st="new", ay="May 2025", neo=[0, ""], src=[["Navy Federal: press releases", PRESS], ["2025 annual report", AR25]]),
        ]},
        {"id": "5.4", "ic": "headset", "name": "Contact centre", "blurb": "46.2 million contacts.", "div": "nfcu", "rev": "cu", "products": [
            P("contact", "24/7 contact centre", "A US-based, 24/7 contact centre handled 46.2 million calls, chats and eMessages in 2025, resolved 95.7% of issues on the first call and averaged a 54-second wait.",
              s=["mil", "vet"], lc="everyday", o="B", neo=[0, ""], src=[["2025 annual report", AR25]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Navy Federal", "blurb": "The second network on credit.", "products": [
        P("mcatnavy", "Mastercard at Navy Federal", "Visa carries debit for 11 million checking accounts, prepaid and gift cards and the new Flagship Premier card, under an umbrella deal renewed in 2009. Mastercard is the second network on credit: cashRewards, GO REWARDS, Platinum, the secured card and GO BIZ Rewards all come in Mastercard versions, though the split is not published ⚠. Mastercard Open Banking links to member accounts ⚠; Amex has More Rewards.",
          s=["mil"], div="nfcu", rev="cu", mc="The relationship this map is drawn for.",
          src=[["Navy Federal: cashRewards", CASHR], ["Visa: Navy Federal renewal, Feb 2009", VISA09], ["Navy Federal: debit card", DEBIT]]),
    ]},
    {"id": "pillar-market", "name": "US credit unions", "blurb": "Scams, fees, interchange.", "products": [
        P("market", "The US market", "No domestic scheme: Visa and Mastercard run debit and credit, with Amex alongside. Overdraft enforcement was eased in 2025, the 2024 merchant interchange settlement was rejected in court ⚠ later status unconfirmed, and instant payments bring new scam risk.",
          s=["mil"], div="nfcu", rev="cu", src=[["Military Times: order dropped, Jul 2025", CFPBEND], ["Digital Transactions: settlement rejected, Jun 2024", SETTLE], ["American Banker: Cube AI, Oct 2026", CUBE]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
