"""TD Bank Group's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the Q3 2026 results (27 August 2026), the fiscal 2025
results (4 December 2025) and the September 2025 Investor Day. Card networks come from TD's, MBNA's and Target's
own card pages, read on 17 October 2026. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own
product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q3 = "https://www.newswire.ca/news-releases/td-bank-group-reports-third-quarter-2026-results-878614719.html"
FY25 = "https://www.newswire.ca/news-releases/td-bank-group-reports-fourth-quarter-and-fiscal-2025-results-805506481.html"
Q1CALL = "https://www.marketbeat.com/earnings/reports/2026-2-26-the-toronto-dominion-bank-stock/"
INVDAY = "https://www.bankingdive.com/news/td-investor-day-ceo-chun-salom-cost-cuts-branches/761458/"
CEFPRO = "https://connect.cefpro.com/article/view/td-slashes-costs-with-ai---c25-billion-plan"
LEAD26 = "https://pulse2.com/td-bank-group-announces-senior-leadership-appointments-to-accelerate-strategy-and-ai-execution/"
EXECS = "https://www.td.com/ca/en/about-td/corporate-profile/executive-profiles"
CHAIR = "https://www.td.com/ca/en/about-td/corporate-profile/chairman-of-the-board"
PROFILE = "https://www.td.com/ca/en/about-td/corporate-profile"
CACARDS = "https://www.td.com/ca/en/personal-banking/products/credit-cards"
BIZCARDS = "https://www.td.com/ca/en/business-banking/small-business/credit-cards"
VISADEBIT = "https://www.td.com/ca/en/personal-banking/ways-to-bank/ways-to-pay/visa-debit-card"
APP = "https://www.td.com/ca/en/personal-banking/solutions/ways-to-bank/td-mobile-app"
MYSPEND = "https://www.td.com/ca/en/personal-banking/solutions/ways-to-bank/td-myspend"
GT = "https://www.td.com/ca/en/personal-banking/ways-to-bank/ways-to-send/international-money-transfer/td-global-transfer"
MERCHANT = "https://www.td.com/ca/en/business-banking/small-business/payment-options/processing-solutions"
MBNA = "https://www.mbna.ca/en"
AMAZON = "https://www.mbna.ca/en/credit-cards/retail-store/amazon-rewards-mastercard"
MBNA2011 = "https://digitaldealer.com/news/td-bank-group-completes-acquisition-of-mbna-canadas-credit-card-business/27186/"
USCARDS = "https://www.td.com/us/en/personal-banking/credit-cards"
USDEBIT = "https://www.td.com/us/en/personal-banking/personal-debit-cards"
USWALLET = "https://www.td.com/us/en/personal-banking/digital-wallet"
USGIFT = "https://www.td.com/us/en/personal-banking/prepaid-cards/gift-card"
USCHK = "https://www.td.com/us/en/personal-banking/checking-accounts"
TARGET = "https://www.target.com/circlecard"
TARGET13 = "https://www.newswire.ca/news-releases/td-bank-group-completes-acquisition-of-targets-us-credit-card-portfolio-and-enters-into-a-seven-year-program-agreement-512066281.html"
NORD15 = "https://www.retailbankerinternational.com/news/td-bank-agrees-to-acquire-nordstrom-us-credit-card-portfolio-270515-4586154/"
MAESTRO = "https://www.pymnts.com/news/2015/td-bank-picks-mastercards-maestro-network/"
FISERV = "https://www.businesswire.com/news/home/20250723065040/en/Fiserv-Announces-Strategic-Relationship-With-TD"
LOGIC = "https://thelogic.co/briefing/td-sells-part-of-its-payment-processing-business-to-fintech-fiserv/"
AEROPLAN = "https://www.paxnews.com/news/other/td-air-canada-celebrate-10-years-aeroplan-partnership-share-top-travel-trends"
OCC = "https://www.occ.gov/news-issuances/news-releases/2024/nr-occ-2024-116.html"
ABA = "https://www.abajournal.com/syndicated/article/doj-announces-3b-in-fines-for-landmark-money-laundering-case"
CADTOK = "https://newsroom.bmo.com/2026-09-22-Six-Canadian-banks-explore-development-of-a-secure-CAD-tokenized-deposit-solution"
NCFA = "https://ncfacanada.org/td-scotiabank-global-usd-stablecoin/"
NILSON = "https://nilsonreport.com/articles/canada-card-issuers-and-networks-2025/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · asset cap · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: C$2.1 trillion of assets and 28 million clients, a bank founded in 1855, a US asset cap of US$434 billion since the 2024 money-laundering plea, and a plan for a 16% ROE by 2029.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "C$2.1tn, ROE 16%.", "div": "td", "rev": "corp", "products": [
            P("balance", "Balance sheet & earnings", "Sixth-largest bank in North America by assets: C$2.11 trillion at 31 July 2026 and 28.2 million clients. Q3 2026 net income C$4.6 billion (adjusted ROE 16.0%), CET1 14.3%; fiscal 2025 adjusted net income C$15.0 billion, plus a C$8.6 billion gain on selling the Schwab stake. More than 100,000 colleagues.",
              s=["con"], neo=[0, ""], src=[["Q3 2026 results", Q3], ["Fiscal 2025 results", FY25], ["TD: corporate profile", PROFILE]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Chun and MacIntyre.", "div": "td", "rev": "corp", "products": [
            P("leadership", "Board & senior executive team", "Chair John MacIntyre (since September 2025), CEO Raymond Chun (since February 2025), CFO Kelvin Tran, CRO Ajai Bambawale; Leo Salom runs U.S. Banking, Sona Mehta Canadian Personal Banking, Barbara Hooper Canadian Commercial Banking. From September 2026 Renu Gupta, Chief Strategy and Commercial Officer, owns payments and digital assets.",
              s=["corp"], st="flux", neo=[0, ""], mc="Renu Gupta is the group-level owner of payments.",
              src=[["TD: executive profiles", EXECS], ["TD: Board Chair", CHAIR], ["Pulse 2.0: appointments, Sep 2026", LEAD26]]),
        ]},
        {"id": "1.3", "ic": "gauge", "name": "US asset cap & AML", "blurb": "US$434bn cap since 2024.", "div": "tdus", "rev": "usb", "products": [
            P("assetcap", "US guilty plea & asset cap", "In October 2024 TD's US bank pleaded guilty to Bank Secrecy Act and money-laundering conspiracy charges. It paid US$3.09 billion in all, including a US$450 million OCC penalty. The OCC capped TD Bank, N.A. and TD Bank USA, N.A. at US$434 billion of average assets. The cap was still in place at 17 October 2026 ⚠.",
              s=["us"], o="I", st="flux", ay="Oct 2024", neo=[0, ""],
              mc="A bank under an asset cap needs AML and fraud intelligence more than most.",
              src=[["OCC: release 2024-116", OCC], ["ABA Journal: $3B plea, Oct 2024", ABA], ["Fiscal 2025 results", FY25]]),
            P("remediation", "AML remediation programme", "About US$550 million of US BSA/AML remediation in fiscal 2026, up from US$500 million guidance. The suspicious-activity look-back runs into 2027. Monitorships run three years (DOJ) and four years (FinCEN) ⚠. FINTRAC is reviewing the Canadian programme.",
              s=["us", "corp"], st="active", neo=[0, "TD's own."], src=[["Q3 2026 results", Q3], ["Fiscal 2025 results", FY25]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "Technology & AI", "blurb": "C$1bn from AI.", "div": "td", "rev": "corp", "products": [
            P("tech", "Technology & AI", "A target of C$1 billion a year from AI, half revenue and half cost. Agentic AI cut mortgage pre-adjudication from about 15 hours to minutes. A generative-AI knowledge tool runs in more than 1,000 Canadian branches. Global Technology and Solutions is under Vlad Shpilsky; enterprise AI is under Paul Whitehead.",
              s=["corp"], st="new", neo=[0, ""], src=[["Q1 2026 call summary ⚠", Q1CALL], ["Pulse 2.0: appointments, Sep 2026", LEAD26]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "ROE 16% by 2029.", "div": "td", "rev": "corp", "products": [
            P("strategy", "Investor Day plan", "Set in September 2025: adjusted ROE about 16% by fiscal 2029, up from about 13% in 2026. Adjusted EPS growth of 7–10%. Efficiency ratio from 58% to the mid-50s. C$2.0–2.5 billion of annual savings, and growth in wealth and wholesale.",
              s=["corp"], st="new", ay="Sep 2025", neo=[0, ""], src=[["Banking Dive: Investor Day, Sep 2025", INVDAY], ["CeFPro: C$2.5bn plan", CEFPRO], ["Fiscal 2025 results", FY25]]),
            P("deals", "Deals 2020–2026", "TD Ameritrade folded into Schwab (2020). First Horizon purchase terminated (2023); Cowen bought (2023). Schwab stake sold for C$21.0 billion (February 2025). US point-of-sale finance put into run-off (May 2025). Part of TD Merchant Solutions sold to Fiserv (July 2025).",
              s=["corp"], o="A", st="flux", neo=[0, ""], src=[["Fiscal 2025 results", FY25], ["Banking Dive: Investor Day, Sep 2025", INVDAY], ["The Logic: Fiserv deal, Jul 2025", LOGIC]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves. TD-branded credit and debit cards run on Visa in both countries. MBNA and Amazon.ca cards in Canada and the Target card in the US run on Mastercard. Interac carries debit in person. TD Merchant Solutions is moving onto Fiserv's Clover. Transfers go by Interac e-Transfer, Zelle and Global Transfer, and new tokenised-deposit and stablecoin projects are under way.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "TD credit cards (Canada)", "blurb": "All Visa.", "div": "tdct", "rev": "cpcb", "products": [
            P("tdvisa", "TD Visa credit cards", "TD First Class Travel Visa Infinite, TD Cash Back Visa Infinite, TD U.S. Dollar Visa and the rest of the TD Canada Trust range. The catalogue lists only Visa. Canadian cards had their best quarter for new accounts in a decade (Q1 2026).", short="TD credit (Visa)",
              s=["con", "card"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["TD: credit cards", CACARDS], ["Q1 2026 call summary ⚠", Q1CALL]]),
            P("aeroplan", "TD Aeroplan Visa", "Aeroplan Visa Infinite and Visa Infinite Privilege. TD has been Aeroplan's primary card issuer since January 2014, with more than a million Canadians served. The 2020 Air Canada deal keeps TD and Visa in Aeroplan to at least 2030 ⚠.", short="Aeroplan (Visa)",
              s=["card"], lc="borrow", ay="Jan 2014", o="P", at="Air Canada, Visa", neo=[0, "Visa."], src=[["PAX News: 10 years of TD Aeroplan, Jan 2024", AEROPLAN], ["TD: credit cards", CACARDS]]),
            P("bizvisa", "TD small-business Visa cards", "TD Business Travel Visa, TD Aeroplan Visa Business, TD Business Cash Back Visa and TD Business Select Rate Visa, with Visa SavingsEdge discounts.",
              s=["sme"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["TD: small-business credit cards", BIZCARDS]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "MBNA", "blurb": "TD's Mastercard book.", "div": "mbna", "rev": "cpcb", "products": [
            P("mbna", "MBNA Mastercard cards", "MBNA True Line, Rewards Platinum Plus and Smart Cash Platinum Plus Mastercards. MBNA Canada was the country's largest Mastercard issuer when TD bought it from Bank of America in December 2011. The site also has Visa benefit pages ⚠.", short="MBNA (Mastercard)",
              s=["card"], lc="borrow", ay="Dec 2011", o="A", at="Mastercard", neo=[2, "Mastercard; some MBNA Visa ⚠."],
              mc="Mastercard's main foothold in TD's Canadian card business.",
              src=[["MBNA Canada", MBNA], ["Digital Dealer: MBNA deal closes, Dec 2011", MBNA2011]]),
            P("amazonca", "Amazon.ca Rewards Mastercard", "Issued by MBNA in Platinum and World tiers. It pays back at Amazon.ca, Whole Foods Market, grocery stores and restaurants.", short="Amazon.ca (Mastercard)",
              s=["card", "con"], lc="borrow", o="P", at="Amazon.ca, Mastercard", neo=[2, "Mastercard."],
              mc="An e-commerce co-brand on Mastercard, a fit for tokenised card-on-file and offers.",
              src=[["MBNA: Amazon.ca Rewards Mastercard", AMAZON]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Debit (Canada)", "blurb": "Interac plus Visa Debit.", "div": "tdct", "rev": "cpcb", "products": [
            P("accesscard", "TD Access Card", "Interac for paying in person. Visa Debit for paying online, paying bills and paying abroad.", short="Access Card (Interac + Visa)",
              s=["con"], lc="everyday", o="P", at="Interac, Visa", neo=[0, "Interac and Visa Debit."], src=[["TD: Access Card with Visa Debit", VISADEBIT]]),
        ]},
        {"id": "2.4", "ic": "credit-card", "name": "TD Bank cards (US)", "blurb": "Visa, with Maestro PIN.", "div": "tdus", "rev": "usb", "products": [
            P("uscredit", "TD Bank Visa credit cards", "TD Cash, TD Double Up, TD Clear, TD FlexPay, TD First Class Visa Signature and TD Cash Secured. US proprietary card balances were up 15%, and unit sales up 33%, year on year in Q1 2026 ⚠.", short="US credit (Visa)",
              s=["us"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="A growing card book, all on Visa.",
              src=[["TD Bank: credit cards", USCARDS], ["Q1 2026 call summary ⚠", Q1CALL]]),
            P("usdebit", "TD Bank Visa debit & digital wallets", "A personal Visa debit card that can be added to digital wallets from the TD Bank app. Since 2016, under a July 2015 deal, Mastercard's Maestro network has carried TD Bank's PIN debit and prepaid transactions ⚠ current status.", short="US debit (Visa; Maestro PIN ⚠)",
              s=["us"], lc="everyday", ay="Jul 2015", o="P", at="Visa, Mastercard", neo=[1, "Visa debit; PIN on Maestro ⚠."],
              src=[["TD Bank: debit cards", USDEBIT], ["TD Bank: digital wallet", USWALLET], ["PYMNTS: TD picks Maestro, Jul 2015", MAESTRO]]),
            P("usgift", "TD Bank Visa Gift Card", "A prepaid Visa gift card.",
              s=["us"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["TD Bank: Visa Gift Card", USGIFT]]),
            P("usbiz", "TD Business Solutions Visa", "Small-business credit card in the US.",
              s=["sme"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["TD Bank: credit cards", USCARDS]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Retail partner cards (US)", "blurb": "Target and Nordstrom.", "div": "partner", "rev": "usb", "products": [
            P("target", "Target Mastercard & Target Circle Card", "Issued by TD Bank USA, N.A. Applicants are considered for the Target Mastercard first, then the private-label Target Circle Credit Card. TD took the portfolio in 2013, when it held more than 5 million Visa and private-label accounts and US$5.7 billion of balances. The date of the move to Mastercard is unknown ⚠.", short="Target (Mastercard)",
              s=["card", "us"], lc="borrow", ay="Mar 2013", o="A", at="Target, Mastercard", neo=[1, "Target Mastercard; private label is closed-loop."],
              mc="TD's US Mastercard co-brand, with Target Circle loyalty.",
              src=[["Target: Circle Card", TARGET], ["TD: Target portfolio closes, Mar 2013", TARGET13]]),
            P("nordstrom", "Nordstrom cards", "A Nordstrom Visa Signature and private-label card, bought in 2015 with about US$2.2 billion of balances. Servicing moved onto TD's platform in February 2026, and a US$144 million receivable adjustment followed in Q2 2026.", short="Nordstrom (Visa)",
              s=["card", "us"], lc="borrow", st="flux", ay="Feb 2026", o="A", at="Nordstrom, Visa", neo=[0, "Visa; private label closed-loop."],
              src=[["Retail Banker International: Nordstrom deal, May 2015", NORD15], ["Q3 2026 results", Q3], ["Q1 2026 call summary ⚠", Q1CALL]]),
        ]},
        {"id": "2.6", "ic": "receipt-text", "name": "Merchant acceptance", "blurb": "TD Merchant Solutions on Clover.", "div": "tdms", "rev": "cpcb", "products": [
            P("tdms", "TD Merchant Solutions", "Card processing in store and online with TD Clover point of sale, Clover online, and Ingenico and Equinox devices, plus TD Merchant Insights. TD is the only big Canadian bank that wholly owns its merchant processor.", short="TD Merchant Solutions",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["TD: Merchant Solutions", MERCHANT], ["The Logic: Fiserv deal, Jul 2025", LOGIC]]),
            P("fiservdeal", "Fiserv managed services", "Announced July 2025. Fiserv bought about 3,400 TD merchant relationships (30,000 locations), and TD's merchant business moves onto Fiserv technology and Clover under a multi-year managed-services deal.",
              s=["sme"], lc="move", st="new", ay="Jul 2025", o="P", at="Fiserv", neo=[0, "Fiserv."], src=[["Fiserv: relationship with TD, Jul 2025", FISERV], ["The Logic: Fiserv deal, Jul 2025", LOGIC]]),
        ]},
        {"id": "2.7", "ic": "send", "name": "Transfers & cross-border", "blurb": "e-Transfer, Zelle, 200 countries.", "div": "td", "rev": "cpcb", "products": [
            P("etransfer", "Interac e-Transfer", "Person-to-person and bill payments inside Canada from the TD app and EasyWeb.",
              s=["con", "sme"], lc="move", o="P", at="Interac", neo=[0, "Interac."], src=[["TD: app", APP]]),
            P("zelle", "Zelle", "Person-to-person payments for TD Bank checking customers in the US.",
              s=["us"], lc="move", o="P", at="Zelle", neo=[0, "Zelle."], src=[["TD Bank: checking", USCHK]]),
            P("globaltransfer", "TD Global Transfer", "International transfers from Canada to more than 200 countries, plus TD US-to-TD Canada transfers, in the app and EasyWeb.",
              s=["con"], lc="move", neo=[None, "Rails not public."],
              mc="A cross-border payout line that Mastercard Move could serve ⚠.",
              src=[["TD: Global Transfer", GT]]),
        ]},
        {"id": "2.8", "ic": "coins", "name": "Digital money", "blurb": "Tokenised deposits, stablecoins.", "div": "td", "rev": "wholesale", "products": [
            P("cadtoken", "CAD tokenised deposits", "One of six Canadian banks (with BMO, CIBC, National Bank, RBC and Scotiabank) exploring a CAD tokenised deposit, starting with transfers between banks (September 2026).",
              s=["corp"], lc="move", st="new", ay="Sep 2026", o="P", at="Canadian banks", neo=[0, "Bank-led tokens."], src=[["Six banks: CAD tokenised deposits, Sep 2026", CADTOK]]),
            P("stablecoin", "Stablecoins & Project Agorá", "Joined the bank consortium planning a USD stablecoin for H1 2027 (September 2026). Completed a Project Agorá test with BNY (31 August 2026). Custodian of the reserves behind Stablecorp's QCAD (July 2026).",
              s=["corp"], lc="move", st="new", ay="Sep 2026", o="P", at="Bank consortium, BNY, Stablecorp", neo=[0, ""],
              mc="Mastercard's stablecoin settlement and multi-token work could link these ⚠.",
              src=[["NCFA: TD and Scotiabank join USD stablecoin, Sep 2026", NCFA]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: transaction monitoring rebuilt after the US plea, TD Clari and agentic AI in lending, MySpend and Interac verification, and loyalty through TD Rewards, Aeroplan, Amazon.ca, Target Circle and Nordstrom.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & financial crime", "blurb": "New monitoring, new KYC.", "div": "td", "rev": "corp", "products": [
            P("monitoring", "Transaction monitoring & KYC", "A next-generation transaction-monitoring system, the first phase of AI and machine-learning models, stronger investigations, and a new KYC platform for business clients.",
              s=["us", "corp"], lc="everyday", st="new", o="B", neo=[0, "TD's own."],
              mc="Network-level AML and scam intelligence fits a bank in remediation ⚠.",
              src=[["Banking Dive: Investor Day, Sep 2025", INVDAY], ["Q1 2026 call summary ⚠", Q1CALL]]),
            P("fraudalerts", "Card fraud alerts", "Fraud alerts on TD credit cards, and card fraud reporting in the US app.",
              s=["con", "sme"], lc="everyday", neo=[None, "Provider not public."], src=[["TD: small-business credit cards", BIZCARDS], ["TD Bank: debit cards", USDEBIT]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI for clients & colleagues", "blurb": "TD Clari, agentic lending.", "div": "td", "rev": "cpcb", "products": [
            P("clari", "TD Clari", "An AI chatbot for customer service inside the TD app.",
              s=["con"], lc="everyday", o="B", neo=[0, ""],
              mc="Agent Pay could let an assistant like this pay ⚠.",
              src=[["TD: app", APP]]),
            P("aitools", "Agentic lending & branch AI", "Agentic AI in mortgage pre-adjudication (from about 15 hours to minutes), a generative-AI knowledge tool in more than 1,000 branches, and more than C$150 million of expected claims savings at TD Insurance.",
              s=["con", "inv"], lc="borrow", st="new", o="B", neo=[0, ""], src=[["Q1 2026 call summary ⚠", Q1CALL]]),
        ]},
        {"id": "3.3", "ic": "fingerprint", "name": "Insights & identity", "blurb": "MySpend, Interac verification.", "div": "tdct", "rev": "cpcb", "products": [
            P("myspend", "TD MySpend", "An app that tracks spending and saving.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["TD: MySpend", MYSPEND]]),
            P("interacverify", "Interac verification service", "Digital identity verification with Interac inside the TD app.",
              s=["con"], lc="open", o="P", at="Interac", neo=[0, "Interac."], src=[["TD: app", APP]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Loyalty", "blurb": "TD Rewards, Aeroplan, partners.", "div": "td", "rev": "cpcb", "products": [
            P("tdrewards", "TD Rewards & Aeroplan points", "TD Rewards points on TD Visa cards, and Aeroplan points on TD Aeroplan Visa cards.",
              s=["card"], lc="grow", o="P", at="Air Canada", neo=[0, "Visa cards."], src=[["TD: credit cards", CACARDS], ["PAX News: 10 years of TD Aeroplan, Jan 2024", AEROPLAN]]),
            P("partnerloyalty", "Partner rewards", "Amazon.ca Rewards (MBNA), Target Circle benefits such as extra return days and free shipping, and Nordstrom rewards. The partners run their own loyalty programmes.",
              s=["card", "us"], lc="grow", o="P", at="Amazon.ca, Target, Nordstrom", neo=[1, "Amazon.ca and Target on Mastercard; Nordstrom on Visa."],
              mc="Card-linked offers and merchant data suit these co-brands.",
              src=[["MBNA: Amazon.ca Rewards Mastercard", AMAZON], ["Target: Circle Card", TARGET]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What clients buy: personal and commercial banking in Canada (net income C$2.1 billion in Q3 2026), U.S. Banking under the cap, TD Auto Finance in both countries, TD Wealth, TD Direct Investing and TD Insurance, and TD Securities with TD Cowen.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Canadian personal banking", "blurb": "Record loans and deposits.", "div": "tdct", "rev": "cpcb", "products": [
            P("cpb", "Accounts, mortgages & lending", "Chequing, savings, real-estate secured lending and personal loans under TD Canada Trust. Q3 2026: record deposit and loan volumes, average loans up C$30 billion (5%), digital sales up 17%, ROE 32.3%.",
              s=["con"], lc="everyday", neo=[0, "Interac and Visa Debit cards."], src=[["Q3 2026 results", Q3]]),
            P("autoca", "TD Auto Finance Canada", "Car finance through dealers in Canada.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Q3 2026 results", Q3]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Canadian commercial banking", "blurb": "Clients up 10%.", "div": "tdct", "rev": "cpcb", "products": [
            P("commercial", "Small business & commercial banking", "Business accounts, lending and cards. New commercial clients in Canadian Business Banking were up 10% year to date in Q3 2026, and business loans up 8%.",
              s=["sme", "corp"], lc="everyday", neo=[0, "Visa business cards."],
              mc="Commercial and virtual cards are untested ground for Mastercard here.",
              src=[["Q3 2026 results", Q3]]),
        ]},
        {"id": "4.3", "ic": "flag", "name": "U.S. Banking", "blurb": "10 million clients, capped.", "div": "tdus", "rev": "usb", "products": [
            P("usbanking", "TD Bank, America's Most Convenient Bank", "About 10 million clients and 1,048 stores on the East Coast. Q3 2026 net income US$771 million (ROE 10.2%). Core loans are up 3% while non-core loans run off. Plans for 100 new stores by 2028 need OCC approval.",
              s=["us", "sme"], lc="everyday", st="flux", neo=[0, "Visa debit and credit."], src=[["Q3 2026 results", Q3], ["Banking Dive: Investor Day, Sep 2025", INVDAY]]),
            P("usauto", "TD Auto Finance U.S.", "Ranked first for dealer satisfaction among non-captive national prime lenders for the seventh year running.",
              s=["us"], lc="borrow", neo=[0, ""], src=[["Q3 2026 results", Q3]]),
            P("posfin", "US point-of-sale finance", "A portfolio of about US$3 billion, put into run-off in May 2025.",
              s=["us"], lc="borrow", st="retired", ay="May 2025", neo=[0, ""], src=[["Banking Dive: Investor Day, Sep 2025", INVDAY]]),
        ]},
        {"id": "4.4", "ic": "trending-up", "name": "Wealth & insurance", "blurb": "C$831bn under administration.", "div": "wealth", "rev": "wmi", "products": [
            P("wealth", "TD Wealth & TD Direct Investing", "AUA C$831 billion and AUM C$644 billion. New wealth accounts up 26%, and daily trades at TD Direct Investing up 20%, in Q3 2026. A plan to hire 500 US advisers.",
              s=["inv"], lc="grow", neo=[0, ""], src=[["Q3 2026 results", Q3], ["Banking Dive: Investor Day, Sep 2025", INVDAY]]),
            P("insurance", "TD Insurance", "Home, car and life insurance. Home insurance was built into REALTOR.ca's home-buying journey in 2026.",
              s=["inv", "con"], lc="beyond", st="new", o="P", at="REALTOR.ca", neo=[0, ""], src=[["Q3 2026 results", Q3]]),
        ]},
        {"id": "4.5", "ic": "chart-candlestick", "name": "Wholesale banking", "blurb": "TD Securities, TD Cowen.", "div": "tds", "rev": "wholesale", "products": [
            P("wholesale", "TD Securities & TD Cowen", "Q3 2026 net income C$743 million (up 87%), revenue C$2.6 billion and ROE 16.7%. Synthetic prime launched in the US and Europe.",
              s=["corp"], lc="beyond", o="A", neo=[0, ""], src=[["Q3 2026 results", Q3], ["Q1 2026 call summary ⚠", Q1CALL]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How clients reach TD: the TD app, rated first for satisfaction by J.D. Power, with more than 14 million active mobile users; about 1,040 Canadian branches and 1,050 US stores; and partners from Air Canada and Amazon.ca to Target and REALTOR.ca.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "TD app", "blurb": "14m+ mobile users.", "div": "td", "rev": "cpcb", "products": [
            P("app", "TD app & EasyWeb", "More than 14 million active mobile users in Canada and the US. Ranked first by J.D. Power for customer satisfaction with mobile banking apps (2026).",
              s=["con", "us"], lc="everyday", neo=[0, ""], src=[["Q3 2026 results", Q3], ["TD: app", APP]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & stores", "blurb": "1,037 + 1,048.", "div": "td", "rev": "cpcb", "products": [
            P("branches", "Branches & stores", "1,037 branches in Canada and 1,048 US stores at 31 July 2026. In the US, 174 stores have closed since 2020 and another 10% will close or move.",
              s=["con", "us"], lc="open", st="flux", neo=[0, ""], src=[["Q3 2026 results", Q3], ["Banking Dive: Investor Day, Sep 2025", INVDAY]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "Aeroplan, Amazon.ca, Target.", "div": "td", "rev": "cpcb", "products": [
            P("partners", "Partners & dealers", "Air Canada (Aeroplan), Amazon.ca, Target, Nordstrom, REALTOR.ca and car dealers in both countries.",
              s=["card", "us"], lc="open", o="P", neo=[1, "Amazon.ca and Target cards are Mastercard; Aeroplan is Visa."],
              src=[["PAX News: 10 years of TD Aeroplan, Jan 2024", AEROPLAN], ["MBNA: Amazon.ca Rewards Mastercard", AMAZON], ["Target: Circle Card", TARGET]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at TD", "blurb": "MBNA and Target; TD's own cards on Visa.", "products": [
        P("mcattd", "Mastercard at TD", "TD-branded credit, debit, business and gift cards run on Visa in Canada and the US, and Interac carries Canadian in-person debit. Mastercard has the cards TD bought or issues for partners: MBNA and the Amazon.ca Rewards Mastercard in Canada, and the Target Mastercard in the US. Maestro has carried US PIN debit since 2016 ⚠.",
          s=["card"], div="td", rev="corp", mc="The relationship this map is drawn for.",
          src=[["TD: credit cards", CACARDS], ["MBNA Canada", MBNA], ["Target: Circle Card", TARGET], ["PYMNTS: TD picks Maestro, Jul 2015", MAESTRO]]),
    ]},
    {"id": "pillar-market", "name": "Canada & US market", "blurb": "Cap, Interac, tokens.", "products": [
        P("market", "The market", "Visa passed Interac in Canadian purchase transactions in 2025 ⚠. US asset cap and monitorships, and FINTRAC's review in Canada. Canadian banks are working on tokenised deposits, and a bank stablecoin is planned for 2027.",
          s=["con"], div="td", rev="corp", src=[["Nilson: Canada issuers and networks 2025 ⚠", NILSON], ["OCC: release 2024-116", OCC], ["Six banks: CAD tokenised deposits, Sep 2026", CADTOK]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
