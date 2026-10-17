"""PNC Financial Services Group's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the Q3 2026 results (15 October 2026), the 2025
results (16 January 2026) and the 2025 Form 10-K (20 February 2026). ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q3 = "https://pnc.mediaroom.com/2026-10-15-PNC-Reports-Third-Quarter-2026-Net-Income-of-2-1-Billion,-4-97-Diluted-EPS-or-5-09-as-Adjusted"
Q2 = "https://pnc.mediaroom.com/2026-07-15-PNC-Reports-Second-Quarter-2026-Net-Income-of-2-1-Billion,-4-81-Diluted-EPS-or-4-85-as-Adjusted"
FY25 = "https://pnc.mediaroom.com/2026-01-16-PNC-Reports-Full-Year-2025-Net-Income-of-7-0-Billion,-16-59-Diluted-EPS"
TENK = "https://www.sec.gov/Archives/edgar/data/713676/000071367626000020/pnc-20251231.htm"
WIKI = "https://en.wikipedia.org/wiki/PNC_Financial_Services"
WIEDMAN = "https://pnc.mediaroom.com/2025-04-07-Mark-Wiedman-Joins-PNC-As-President"
CRO = "https://pnc.mediaroom.com/2025-08-12-PNC-Announces-Leadership-Changes-in-Risk-and-Legal-Organizations"
BLK = "https://pnc.mediaroom.com/2020-05-15-PNC-Announces-Closing-of-Sale-of-BlackRock-Stock"
BBVA = "https://pnc.mediaroom.com/2020-11-16-PNC-Announces-Agreement-To-Buy-BBVA-USA-Bancshares-Inc"
BBVACONV = "https://pnc.mediaroom.com/2021-10-12-PNC-Achieves-National-Expansion-With-Conversion-Of-BBVA-USA"
AQUEDUCT = "https://pnc.mediaroom.com/2025-05-20-PNC-Bank-Agrees-to-Acquire-Aqueduct-Capital-Group-to-Complement-Harris-Williams-Capabilities"
FBDEAL = "https://pnc.mediaroom.com/2025-09-08-PNC-Announces-Agreement-to-Acquire-FirstBank,-Significantly-Growing-its-Presence-in-Colorado-and-Arizona"
FBCLOSE = "https://pnc.mediaroom.com/2026-01-05-PNC-Completes-Acquisition-of-FirstBank"
FBCONV = "https://pnc.mediaroom.com/2026-06-22-PNC-Completes-FirstBank-Customer-Conversion"
FBCBS = "https://www.cbsnews.com/colorado/news/former-customers-colorado-firstbank-adjustment-challenges-pnc-conversion/"
APP = "https://pnc.mediaroom.com/2026-07-07-PNCs-New-Mobile-App-Delivers-an-Intuitive,-Personalized-Experience-to-Help-Clients-Seamlessly-Manage-Their-Day-to-Day-Financial-Lives"
CISO = "https://pnc.mediaroom.com/2026-07-27-PNC-Names-Christian-Winward-Chief-Information-Security-Officer"
BR300 = "https://pnc.mediaroom.com/2025-11-07-PNC-Bank-Increases-New-Branch-Openings-to-More-Than-300-by-2030"
BR50 = "https://pnc.mediaroom.com/2026-08-03-PNC-Celebrates-50th-New-Branch-Opening-Since-Launch-of-Coast-to-Coast-Build-Out-of-More-Than-300-Branches"
DEBIT = "https://www.pnc.com/en/personal-banking/banking/debit-and-prepaid-cards/pnc-bank-visa-debit-card.html"
BIZDEBIT = "https://pnc.com/en/small-business/payments-and-processing/payment-cards/pnc-bank-visa-business-debit-card.html"
CARDS = "https://www.pnc.com/en/personal-banking/banking/credit-cards.html"
CASHUNL = "https://pnc.mediaroom.com/2024-05-07-PNC-Bank-Introduces-New-Cash-Unlimited-Visa-Signature-R-Credit-Card-Offering-2-Cash-Back-Across-All-Eligible-Purchases"
SPENDWISE = "https://pnc.mediaroom.com/2025-05-12-PNC-Bank-Introduces-PNC-Spend-Wise-,-A-No-Annual-Fee-Credit-Card-Offering-A-Purchase-APR-Reduction-to-Encourage-Responsible-Credit-Habits"
COUPA = "https://pnc.com/en/corporate-and-institutional/treasury-management/online-and-mobile-banking/digital-payments/corporate-coupa-pay.html"
EXTEND = "https://www.pymnts.com/partnerships/2025/pnc-and-extend-team-to-upgrade-commercial-cards/"
MOBACCEPT = "https://pnc.mediaroom.com/2025-06-11-PNC-Bank-Launches-PNC-Mobile-Accept-R-,-A-New-Pay-As-You-Go-Payment-Processing-Solution-for-Micro-Businesses"
TEMPUS = "https://pnc.mediaroom.com/2021-01-27-PNC-Bank-Announces-Definitive-Agreement-To-Acquire-Tempus-Technologies-Inc"
LINGA = "https://pnc.mediaroom.com/2022-09-26-PNC-ANNOUNCES-ACQUISITION-OF-POINT-OF-SALE-AND-PAYMENTS-SOLUTIONS-FIRM,-LINGA"
FEDNOW = "https://pnc.mediaroom.com/2025-10-21-PNC-Bank-Expands-Immediate-Payments-Solutions-by-Joining-the-FedNow-R-Service"
VISADIRECT = "https://pnc.mediaroom.com/2025-10-29-PNC-Bank-Visa-Announce-Collaboration-on-Immediate-Payment-Capabilities-Through-Visa-Direct"
POD = "https://www.bankingdive.com/news/mastercard-pnc-real-time-business-payment-pilot/565500/"
EWS = "https://en.wikipedia.org/wiki/Early_Warning_Services"
PAZE = "https://www.paze.com/"
GLOBAL = "https://pnc.mediaroom.com/2021-06-29-PNC-Announces-Expanded-Cross-Border-Payment-Capabilities-With-Rebranded-PNC-Global-Transfers-Inc"
COINBASE = "https://pnc.mediaroom.com/2025-07-22-PNC-Bank,-Coinbase-Announce-Strategic-Partnership-to-Advance-Digital-Asset-Solutions-and-Expand-Banking-Services"
BTC = "https://pnc.mediaroom.com/2025-12-09-PNC-First-Major-Bank-to-Launch-Direct-Bitcoin-Access-for-Clients,-Powered-by-Coinbases-Crypto-as-a-Service-Infrastructure"
AKOYA21 = "https://pnc.mediaroom.com/2021-09-30-PNC-Launches-Akoya-Solution-To-Increase-The-Security-Of-Connections-For-Consumers-To-Safely-Transact-With-Financial-Apps"
PLAID = "https://pnc.mediaroom.com/2024-09-20-PNC-Financial-Services-Group,-Plaid-Enter-Data-Access-Agreement"
AKOYA24 = "https://pnc.mediaroom.com/2024-10-03-PNC-Bank-Launches-Akoya-Integration-for-PINACLE-Connect-R-to-Provide-More-Secure,-Transparent-Data-Access-for-Corporate-Clients"
HEALTH = "https://pnc.mediaroom.com/2026-02-13-PNC-Launches-Monthly-Consumer-Health-Check-to-Deliver-Real-Time-Pulse-on-U-S-Spending-and-the-Economy"
CASHFC = "https://pnc.mediaroom.com/2021-11-09-PNC-Treasury-Management-Launches-Artificial-Intelligence,-Machine-Learning-Enabled-Cash-Forecasting-Application"
REWARDS = "https://pnc.mediaroom.com/2026-04-07-PNC-Bank-Debuts-Consumer-Loyalty-and-Rewards-Program"
SENTRAL = "https://pnc.mediaroom.com/2020-09-22-PNC-Fintech-Incubator-numo-Acquires-Sentral"
LOWCASH = "https://pnc.mediaroom.com/2021-04-13-PNC-Launches-Low-Cash-Mode-SM-To-Address-17-Billion-In-Industry-Overdraft-Fees"
SIMPLE = "https://pnc.mediaroom.com/2025-12-15-PNC-Simple-Checking-Offers-Straightforward,-Worry-Free-Banking"
PREMIER = "https://pnc.mediaroom.com/2026-02-11-PNC-Wealth-Management-Launches-Premier-Client-An-Integrated-Banking-and-Investing-Experience-for-the-Emerging-and-Mass-Affluent"
SBL = "https://pnc.mediaroom.com/2026-07-21-PNC-Wealth-Management-Launches-Securities-Based-Lending-Solution"
CPR = "https://pnc.mediaroom.com/2026-04-29-PNC-Bank-Expands-Treasury-Management-Capabilities-with-New-Property-and-Casualty-Insurance-Payments-Solution"
EARNEDIT = "https://pnc.mediaroom.com/2022-02-23-PNC-TREASURY-MANAGEMENT-LAUNCHES-INNOVATIVE-ON-DEMAND-PAY-SOLUTION-POWERED-BY-DAILYPAY"
TCW = "https://pnc.mediaroom.com/2024-05-06-PNC,-TCW-Partner-To-Expand-Capabilities,-Create-Private-Credit-Platform"
DIRDEP = "https://pnc.mediaroom.com/2025-07-08-PNC-Bank-Introduces-New-Digital-Direct-Deposit-Manager"
ORACLE = "https://pnc.mediaroom.com/2025-07-29-PNC-Bank-Announces-Integration-with-Oracle-Fusion-Cloud-ERP-for-Embedded-Banking"
WORKPLACE = "https://pnc.mediaroom.com/2026-09-08-PNC-Workplace-Advantage-to-Help-Employers-Strengthen-Benefit-Offerings-While-Supporting-Employees-Financial-Confidence"
IBD = "https://pnc.mediaroom.com/2026-10-07-PNC-Bank-Named-Most-Trusted-Bank-in-Investors-Business-Daily-2026-Trust-Survey"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · deals · technology", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $628 billion of assets and an 18% return on tangible equity, a Pittsburgh bank dating from 1845 grown coast to coast through BBVA USA and FirstBank, a Visa shareholding, and a new app built with agentic tools.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "$628bn assets, ROTCE 18.3%.", "div": "pnc", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of $627.8 billion, loans of $378.8 billion and deposits of $466.4 billion at 30 September 2026; Q3 net income $2.1 billion (ROTCE 18.3%, CET1 9.8%); record 2025 revenue of $23.1 billion and net income of $7.0 billion; 55,333 staff at end-2025; senior debt A3/A-/A.",
              s=["corp"], neo=[0, ""], src=[["Q3 2026 results", Q3], ["FY2025 results", FY25], ["2025 Form 10-K", TENK]]),
            P("visastake", "Visa shareholding", "A Visa USA member through National City, PNC holds Visa Class B stock: it monetised half in 2024 (a $754 million gain) and half the rest in Q2 2026 (a $448 million gain), keeping about 0.9 million Class B-3 shares, and indemnifies Visa for interchange litigation.",
              s=["corp"], o="I", at="Visa", neo=[0, "Visa equity."],
              mc="PNC has a financial stake in Visa's success that it has no equivalent of at Mastercard.",
              src=[["Q2 2026 results", Q2], ["2025 Form 10-K", TENK]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Demchak, Wiedman, Reilly.", "div": "pnc", "rev": "other", "products": [
            P("leadership", "Board & executive committee", "Chairman and CEO William S. Demchak; President Mark Wiedman (from BlackRock, April 2025); CFO Robert Reilly; Alex Overstrom runs Retail, Michael Thomas CIB, Stephanie Novosel Asset Management; Debbie Guild technology; Amy Wierenga risk (September 2025).",
              s=["corp"], neo=[0, ""], src=[["Wiedman joins as President, Apr 2025", WIEDMAN], ["Risk and legal changes, Aug 2025", CRO], ["2025 Form 10-K", TENK]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & deals", "blurb": "1845 to coast to coast.", "div": "pnc", "rev": "other", "products": [
            P("heritage", "Heritage", "Pittsburgh Trust and Savings (1845); PNC formed from Pittsburgh National and Provident National in 1982–83 ⚠; National City (2008) and RBC Bank USA (2012) made it a large regional bank.",
              s=["con"], o="I", neo=[0, ""], src=[["Wikipedia: PNC Financial Services", WIKI]]),
            P("deals", "Deals since 2020", "Sold its BlackRock stake for about $14.4 billion ⚠ (May 2020) and spent $11.6 billion on BBVA USA (closed June 2021; 2.6 million customers converted October 2021), reaching 29 of the 30 largest US markets; Aqueduct Capital added to Harris Williams (2025).",
              s=["corp"], o="A", neo=[0, ""], src=[["BlackRock sale, May 2020", BLK], ["BBVA USA deal, Nov 2020", BBVA], ["BBVA USA conversion, Oct 2021", BBVACONV], ["Aqueduct, May 2025", AQUEDUCT]]),
        ]},
        {"id": "1.4", "ic": "flag", "name": "FirstBank", "blurb": "$4.1bn; number one in Denver.", "div": "firstbank", "rev": "retail", "products": [
            P("firstbank", "FirstBank acquisition", "FirstBank of Lakewood, Colorado ($26 billion of assets, $23 billion of deposits, 95 branches) bought for $4.1 billion: announced September 2025, closed 5 January 2026, and 780,000 customers converted on 22 June 2026, making PNC number one in Denver by deposits (20%) and branches; some customers reported access problems that week.", short="FirstBank (2026)",
              s=["con", "sme"], lc="open", st="new", ay="Jan 2026", o="A", neo=[None, "FirstBank's network not found; cards now PNC Visa ⚠."],
              mc="780,000 customers reissued PNC cards in 2026: a network decision Mastercard did not win ⚠.",
              src=[["FirstBank deal, Sep 2025", FBDEAL], ["FirstBank closes, Jan 2026", FBCLOSE], ["FirstBank conversion, Jun 2026", FBCONV], ["CBS Colorado, Jun 2026", FBCBS]]),
        ]},
        {"id": "1.5", "ic": "database", "name": "Technology & AI", "blurb": "Agentic development.", "div": "pnc", "rev": "other", "products": [
            P("tech", "Technology, security & AI", "A patented data-streaming microservices architecture, an agentic software development system and access to frontier AI models for building and testing code; a Global Security Fusion Center joining cyber, physical, fraud and insider-threat intelligence, led by CISO Christian Winward (July 2026).",
              s=["corp"], st="new", neo=[0, ""], src=[["New mobile app, Jul 2026", APP], ["CISO appointment, Jul 2026", CISO]]),
        ]},
        {"id": "1.6", "ic": "target", "name": "Strategy", "blurb": "300 new branches by 2030.", "div": "bank", "rev": "retail", "products": [
            P("strategy", "National growth & primacy", "Scale coast to coast through organic growth and acquisition: more than 300 new branches by 2030 for about $2 billion (50 opened by August 2026, 55 in 2026), every branch renovated by 2029, and products built to make PNC clients' primary bank.",
              s=["con"], st="new", neo=[0, ""], src=[["300 new branches, Nov 2025", BR300], ["50th new branch, Aug 2026", BR50]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Visa debit and Visa credit cards, Visa commercial cards with Extend, PNC's own acquiring with Tempus, Linga and Mobile Accept, real-time rails from RTP and FedNow to Zelle and Visa Direct, and cross-border and bitcoin.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Visa debit, $717m of fees.", "div": "bank", "rev": "retail", "products": [
            P("debit", "PNC Bank Visa Debit Card", "Contactless debit with Zero Liability, Purchase Payback cash rewards and nearly 50 affinity designs; debit card fees were $717 million in 2025.", short="Debit (Visa)",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="PNC's largest card fee line runs on Visa.",
              src=[["PNC: Visa debit card", DEBIT], ["2025 Form 10-K", TENK]]),
            P("bizdebit", "PNC Visa Business Debit Card", "Full account access for small-business checking, alongside a deposit-only card.", short="Business debit (Visa)",
              s=["sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["PNC: Visa Business Debit Card", BIZDEBIT]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "All Visa.", "div": "bank", "rev": "retail", "products": [
            P("credit", "PNC credit cards", "Cash Rewards, Cash Unlimited Visa Signature (2% cash back, May 2024), Spend Wise (a 2-point APR cut for paying on time, May 2025) and Secured, all Visa; $6.6 billion of card loans at end-2025. PNC issued Mastercard cards through U.S. Bancorp from 2006 ⚠ before converting them after National City.", short="Credit (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              src=[["PNC: credit cards", CARDS], ["Cash Unlimited, May 2024", CASHUNL], ["Spend Wise, May 2025", SPENDWISE], ["Wikipedia: PNC Financial Services", WIKI]]),
        ]},
        {"id": "2.3", "ic": "briefcase-business", "name": "Commercial cards", "blurb": "Visa, virtual with Extend.", "div": "tm", "rev": "cib", "products": [
            P("comcard", "Commercial & virtual cards", "Purchasing, travel and virtual cards on Visa ⚠, with Visa Commercial Pay B2B through Conferma and Coupa Pay, and Extend (November 2025) for instant virtual cards from existing PNC commercial cards, usable in Apple Pay and Google Pay.", short="Commercial cards (Visa ⚠)",
              s=["corp", "sme"], lc="move", st="new", ay="Nov 2025", o="P", at="Visa, Extend, Coupa", neo=[0, "Visa ⚠."],
              mc="Virtual cards in client workflows is ground Mastercard contests with Visa Commercial Pay.",
              src=[["PNC: Coupa Pay", COUPA], ["PYMNTS: PNC and Extend, Nov 2025", EXTEND]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acceptance", "blurb": "Merchant Services, Linga.", "div": "merchant", "rev": "retail", "products": [
            P("merchant", "PNC Merchant Services & Tempus", "Card acquiring under agreements with Visa and Mastercard ($223 million of merchant fees in 2025), with the Tempus Technologies gateway (2021) linking cards to RTP, ACH, wires and Zelle.", short="Merchant Services",
              s=["merch", "sme"], lc="move", o="A", neo=[1, "Accepts Mastercard among all networks."],
              src=[["2025 Form 10-K", TENK], ["Tempus acquisition, Jan 2021", TEMPUS]]),
            P("linga", "Linga", "A cloud restaurant operating system with online ordering, payments, QR menus and kiosks, bought in September 2022, serving clients in 48 countries.",
              s=["merch"], lc="move", ay="Sep 2022", o="A", neo=[1, "Accepts every network."], src=[["Linga acquisition, Sep 2022", LINGA]]),
            P("mobileaccept", "PNC Mobile Accept", "Card acceptance inside the PNC app for micro-businesses taking under $300,000 a year: tap, dip or swipe with a reader, no monthly fee, all card brands, funds in about two days (June 2025).",
              s=["sme", "merch"], lc="move", st="new", ay="Jun 2025", o="B", neo=[1, "Accepts every network."], src=[["Mobile Accept, Jun 2025", MOBACCEPT]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Real-time payments", "blurb": "RTP, FedNow, Zelle, Visa Direct.", "div": "tm", "rev": "cib", "products": [
            P("rtp", "RTP & FedNow", "A founding member of The Clearing House's RTP network (2017) and on the Federal Reserve's FedNow from October 2025, behind Intelligent Routing, ePayments and Direct to Debit Card for business payouts.",
              s=["corp", "emp"], lc="move", st="new", ay="Oct 2025", o="P", at="The Clearing House, Federal Reserve", neo=[0, "Account-to-account."], src=[["FedNow, Oct 2025", FEDNOW]]),
            P("visadirect", "Visa Direct payouts", "A renewed collaboration (October 2025) giving Treasury Management clients instant payouts to cards for insurance claims, gig pay, earned wages and refunds.", short="Visa Direct",
              s=["corp", "emp"], lc="move", st="new", ay="Oct 2025", o="P", at="Visa", neo=[0, "Visa."],
              mc="The push-to-card slot Mastercard Move would compete for.",
              src=[["Visa Direct collaboration, Oct 2025", VISADIRECT]]),
            P("zelle", "Zelle & Paze", "PNC is one of seven bank owners of Early Warning Services, which runs Zelle (about $1 trillion in 2024) and the Paze checkout wallet, where PNC cards are listed.",
              s=["con", "sme"], lc="move", o="P", at="Early Warning Services", neo=[0, "Bank-owned rails; PNC cards are Visa."], src=[["Wikipedia: Early Warning Services", EWS], ["Paze", PAZE]]),
            P("pod", "Mastercard Payment on Delivery pilot", "In October 2019 Mastercard piloted real-time B2B payment on delivery with PNC in alcohol distribution, using PNC's access to the RTP network; no later status found ⚠.",
              s=["corp"], lc="move", st="unconf", ay="Oct 2019", o="P", at="Mastercard", neo=[3, "Mastercard Track pilot ⚠ status."], src=[["Banking Dive: Mastercard and PNC pilot, Oct 2019", POD]]),
        ]},
        {"id": "2.6", "ic": "earth", "name": "Cross-border & digital assets", "blurb": "Global Transfers, bitcoin.", "div": "wealth", "rev": "amg", "products": [
            P("globaltransfers", "PNC Global Transfers", "Formerly BBVA Transfer Services (rebranded June 2021): an API for money transmitters and banks paying into Mexico, Central and South America and the Caribbean.",
              s=["corp"], lc="move", o="A", neo=[0, ""], src=[["PNC Global Transfers, Jun 2021", GLOBAL]]),
            P("crypto", "Bitcoin with Coinbase", "A Coinbase Crypto-as-a-Service partnership (July 2025) and spot bitcoin buying, holding and selling for Private Bank clients from December 2025, the first among major US banks.",
              s=["aff"], lc="grow", st="new", ay="Dec 2025", o="P", at="Coinbase", neo=[0, ""], src=[["Coinbase partnership, Jul 2025", COINBASE], ["Bitcoin access, Dec 2025", BTC]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: data shared only through Akoya's APIs, AI cash forecasts and a monthly spending index, and TotalRewards tiers that reward the whole relationship.",
    "tiles": [
        {"id": "3.1", "ic": "plug", "name": "Open banking", "blurb": "Everything through Akoya.", "div": "bank", "rev": "retail", "products": [
            P("akoya", "Akoya & data access", "On the Akoya Data Access Network since September 2021 (more than nine million customers), used for all data recipients including Plaid (September 2024) and for PINACLE corporate data (October 2024); PNC was a founding member of FDX. Whether Mastercard Open Banking connects through Akoya is unconfirmed ⚠.",
              s=["con", "corp"], lc="open", o="P", at="Akoya, Plaid", neo=[None, "Mastercard Open Banking link unconfirmed ⚠."],
              mc="An API-first bank: Mastercard's open-finance services would plug in through Akoya.",
              src=[["Akoya launch, Sep 2021", AKOYA21], ["Plaid agreement, Sep 2024", PLAID], ["Akoya for PINACLE, Oct 2024", AKOYA24]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data & AI", "blurb": "Health Check, AI forecasts.", "div": "pnc", "rev": "other", "products": [
            P("healthcheck", "Monthly Consumer Health Check", "A monthly index of US spending, savings and cash flow built from PNC's anonymised transaction data, with category breakouts from groceries to AI (February 2026).",
              s=["corp", "aff"], lc="grow", st="new", ay="Feb 2026", o="B", neo=[0, ""],
              mc="Transaction enrichment and merchant data could sharpen it.",
              src=[["Consumer Health Check, Feb 2026", HEALTH]]),
            P("cashforecast", "PINACLE Cash Forecasting", "A bank-agnostic cash forecast that trains five AI and machine-learning models on a client's history to give 31-, 60- or 90-day forecasts (November 2021).",
              s=["corp"], lc="beyond", o="B", neo=[0, ""], src=[["PINACLE Cash Forecasting, Nov 2021", CASHFC]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty & offers", "blurb": "TotalRewards tiers.", "div": "bank", "rev": "retail", "products": [
            P("totalrewards", "PNC TotalRewards", "A relationship loyalty programme (national from spring 2026) with Silver, Gold and Platinum tiers at $25,000, $100,000 and $500,000, boosting credit card rewards, savings rates and lending cash back; military members start at Silver.",
              s=["con", "aff"], lc="grow", st="new", ay="Apr 2026", o="B", neo=[0, "Rewards on Visa cards."],
              mc="Card-linked offers could extend it to merchants.",
              src=[["TotalRewards, Apr 2026", REWARDS]]),
            P("sentral", "Purchase Payback & numo's Sentral", "Cash-back offers on Visa debit cards, and Sentral, a debit gateway for card-linked offers bought by PNC's numo incubator in 2020 ⚠ current status unknown.",
              s=["con"], lc="everyday", o="A", neo=[None, "Nothing public."], src=[["Sentral, Sep 2020", SENTRAL], ["PNC: Visa debit card", DEBIT]]),
        ]},
        {"id": "3.4", "ic": "shield-check", "name": "Fraud & security", "blurb": "A fusion centre.", "div": "pnc", "rev": "other", "products": [
            P("security", "Fraud & cyber protection", "The Global Security Fusion Center combines cyber, physical, fraud and insider-threat intelligence; Zero Liability on cards; alerts and controls in the app. No card-fraud vendor named ⚠.",
              s=["con", "corp"], lc="everyday", neo=[None, "Nothing public."],
              mc="No public Mastercard fraud or identity tools at PNC.",
              src=[["CISO appointment, Jul 2026", CISO], ["PNC: Visa debit card", DEBIT]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: Virtual Wallet and Simple Checking, mortgages, home equity and auto loans, Premier Client and the Private Bank, Treasury Management on PINACLE, and corporate banking with Harris Williams and TCW.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Accounts", "blurb": "Virtual Wallet, Simple Checking.", "div": "bank", "rev": "retail", "products": [
            P("accounts", "Virtual Wallet & Simple Checking", "Retail deposits averaged $267 billion in Q3 2026; Virtual Wallet with Low Cash Mode (2021) gives a day or more to fix an overdraft, and Simple Checking (December 2025) has no overdraft fees.",
              s=["con"], lc="everyday", neo=[0, "Visa debit."], src=[["Q3 2026 results", Q3], ["Low Cash Mode, Apr 2021", LOWCASH], ["Simple Checking, Dec 2025", SIMPLE]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Consumer lending", "blurb": "$97bn of retail loans.", "div": "bank", "rev": "retail", "products": [
            P("lending", "Mortgages, home equity & auto", "Retail loans of $97 billion at end-2025: residential mortgages $34.3 billion, home equity $24.6 billion, auto $15.9 billion, credit cards $6.6 billion and education loans.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["2025 Form 10-K", TENK]]),
        ]},
        {"id": "4.3", "ic": "gem", "name": "Wealth", "blurb": "Premier Client, Private Bank.", "div": "wealth", "rev": "amg", "products": [
            P("premier", "Premier Client & securities-based lending", "Banking and investing for clients with more than $100,000 (February 2026), with 200 branches becoming Premier branches through 2027 and securities-based credit lines from $100,000 (July 2026).",
              s=["aff"], lc="grow", st="new", ay="Feb 2026", neo=[0, ""], src=[["Premier Client, Feb 2026", PREMIER], ["Securities-based lending, Jul 2026", SBL]]),
            P("privatebank", "Asset Management Group & Private Bank", "Discretionary assets of $250 billion and $499 billion under administration (Q3 2026); the Private Bank has more than 100 offices for high and ultra-high net worth clients.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["Q3 2026 results", Q3], ["Bitcoin access, Dec 2025", BTC]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Treasury Management", "blurb": "$1.6bn of fees.", "div": "tm", "rev": "cib", "products": [
            P("tm", "PNC Treasury Management", "Payables, receivables, liquidity and information reporting for corporates: $1.59 billion of treasury management fees in CIB in 2025, and card and cash management fees of $769 million in Q3 2026.",
              s=["corp"], lc="move", neo=[0, ""], src=[["2025 Form 10-K", TENK], ["Q3 2026 results", Q3]]),
            P("cpr", "Claim Payments & EarnedIt", "Claim Payments & Remittances with ECHO Health for health (since 2018) and property and casualty insurers (April 2026), and PNC EarnedIt on-demand pay with DailyPay (2022).",
              s=["emp", "corp"], lc="move", st="new", ay="Apr 2026", o="P", at="ECHO Health, DailyPay", neo=[0, ""],
              mc="Multi-party payouts with instant options: a fit for push-to-card.",
              src=[["P&C insurance payments, Apr 2026", CPR], ["PNC EarnedIt, Feb 2022", EARNEDIT]]),
        ]},
        {"id": "4.5", "ic": "factory", "name": "Corporate & institutional", "blurb": "$248bn of loans.", "div": "hw", "rev": "cib", "products": [
            P("cib", "Corporate & Institutional Banking", "Corporate banking, real estate, asset-based lending and capital markets: average loans of $247.7 billion and segment earnings of $1.55 billion in Q3 2026; Harris Williams and Aqueduct for advisory; private credit with TCW (2024).",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Q3 2026 results", Q3], ["TCW partnership, May 2024", TCW]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach PNC: a rebuilt mobile app, about 2,400 branches with 300 more on the way, PINACLE inside clients' ERPs, and banking through the workplace.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Mobile app", "blurb": "Rebuilt in 2026.", "div": "bank", "rev": "retail", "products": [
            P("app", "PNC Mobile app", "A new app rolled out from July 2026, ready for embedded generative AI, with FirstBank customers among the first; in-app direct-deposit switching since July 2025.",
              s=["con", "sme"], lc="everyday", st="new", ay="Jul 2026", neo=[0, ""],
              mc="An AI-ready app with no Mastercard credential for Agent Pay.",
              src=[["New mobile app, Jul 2026", APP], ["Direct deposit, Jul 2025", DIRDEP]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "About 2,400 branches.", "div": "bank", "rev": "retail", "products": [
            P("branches", "Branches & ATMs", "About 2,400 branch locations and 58,000 PNC and partner ATMs after FirstBank, and more than 300 new branches by 2030 across about 19 markets; named most trusted bank by Investor's Business Daily (October 2026).",
              s=["con", "sme"], lc="open", st="flux", neo=[0, ""], src=[["FirstBank conversion, Jun 2026", FBCONV], ["50th new branch, Aug 2026", BR50], ["IBD trust survey, Oct 2026", IBD]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "PINACLE & ERP", "blurb": "Banking inside Oracle.", "div": "tm", "rev": "cib", "products": [
            P("pinacle", "PINACLE & PINACLE Connect", "Corporate online banking with embedded APIs: PINACLE Connect inside Oracle Fusion Cloud ERP (July 2025) and Coupa Pay, with balances, payments and reconciliation inside clients' own systems.",
              s=["corp"], lc="move", o="P", at="Oracle, Coupa", neo=[0, ""], src=[["Oracle integration, Jul 2025", ORACLE], ["PNC: Coupa Pay", COUPA]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Workplace", "blurb": "Banking as a benefit.", "div": "bank", "rev": "retail", "products": [
            P("workplace", "PNC Workplace Advantage", "Workplace banking for employers with 100 or more staff (September 2026): banking rewards for employees who move their pay, financial guidance and education.",
              s=["emp", "con"], lc="open", st="new", ay="Sep 2026", neo=[0, ""], src=[["Workplace Advantage, Sep 2026", WORKPLACE]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at PNC", "blurb": "Visa cards, Mastercard at the till.", "products": [
        P("mcatpnc", "Mastercard at PNC", "Every PNC card listed is Visa: debit, credit, business debit and, it appears, commercial ⚠. PNC also holds Visa shares and renewed its Visa Direct collaboration in October 2025. Mastercard reaches PNC through acquiring (Merchant Services, Linga, Mobile Accept), a 2019 Payment on Delivery pilot on RTP, and its share of the interchange litigation.",
          s=["con"], div="pnc", rev="other", mc="The relationship this map is drawn for.",
          src=[["PNC: credit cards", CARDS], ["Visa Direct collaboration, Oct 2025", VISADIRECT], ["Banking Dive: Mastercard and PNC pilot, Oct 2019", POD]]),
    ]},
    {"id": "pillar-market", "name": "US banking", "blurb": "Interchange, A2A, consolidation.", "products": [
        P("market", "The US market", "Regional consolidation (FirstBank, Capital One–Discover), Regulation II debit interchange revisions proposed in 2023, the risk of a second-network mandate on credit cards, account-to-account growth through RTP, FedNow and Zelle, and the long-running interchange litigation.",
          s=["con"], div="pnc", rev="other", src=[["2025 Form 10-K", TENK]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
