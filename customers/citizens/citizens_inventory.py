"""Citizens' layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Citizens' own unless a source says otherwise: the 3Q26 earnings release and financial
supplement (16 October 2026) and the FY2025 10-K. ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product or network runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not
Mastercard, None = nothing public.
"""
# ruff: noqa: E501

from citizens_foundation import FOUNDATION

SEC = "https://www.sec.gov/Archives/edgar/data/"
Q3R = SEC + "0000759944/000075994426000206/a3q26earningsrelease.htm"
Q3F = SEC + "0000759944/000075994426000206/q326financialsupplement.htm"
K10 = SEC + "759944/000075994426000028/cfg-20251231.htm"
NEWS = "https://investor.citizensbank.com/about-us/newsroom/latest-news/"
CB = "https://www.citizensbank.com/"
MC2023 = "https://newsroom.mastercard.com/news/press/2023/january/mastercard-and-citizens-financial-group-announce-exclusive-payments-partnership/"
DEBIT = NEWS + "2023/2023-12-12-140137819.aspx"
SUITE = NEWS + "2025/2025-06-12-142316922.aspx"
EDGE = NEWS + "2025/2025-10-09-140524810.aspx"
FDX = NEWS + "2025/2025-03-27.aspx"
SWITCH = NEWS + "2025/2025-07-28.aspx"
PAYEE = NEWS + "2025/2025-04-08a.aspx"
AB_ASSETS = "https://www.americanbanker.com/payments/news/how-citizens-is-placing-its-bets-in-digital-assets"
AB_PAY = "https://www.americanbanker.com/payments/news/citizens-payments-exec-discusses-fintech-competition"
CALL3Q = "https://www.gurufocus.com/news/9128248/citizens-financial-group-inc-cfg-q3-2026-earnings-call-highlights-record-revenue-34-eps-growth-and-a-clear-path-to-1618-rotce"
BD_AI = "https://www.bankingdive.com/news/citizens-ai-banking-reimagine-coughlin/815965/"
APPLE = "https://www.macrumors.com/2026/07/28/apple-upgrade-program-klarna/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves through Citizens: every card on Mastercard since 2023, commercial cards from Mastercard's mid-market programme, Zelle and RTP, the treasury rails and merchant acceptance, an embedded-payments business that settles for 50-plus payments companies, and a first look at stablecoins for cross-border.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Cards & wallets", "blurb": "Mastercard only, since 2023.", "div": "con", "rev": "con", "products": [
            P("mcexclusive", "Mastercard exclusive partnership", "Since 19 January 2023 Mastercard has been Citizens' only network for credit, debit and commercial cards, and its US services provider for open banking, digital identity, fraud, B2B and small-business tools and Priceless. It was the first time Citizens chose a single network; its president said acquisitions had left it with a fragmented set of network partners. The term was not disclosed.", short="Mastercard exclusive partnership",
              s=["con", "aff", "sme", "mid"], lc="move", o="P", at="Mastercard", ay="Jan 2023", neo=[3, "The agreement itself."],
              mc="The deepest Mastercard relationship of any US regional bank of this size: network and services in one contract, so every service in this map is something Citizens has already agreed in principle to buy from Mastercard.",
              rel=["debit", "suite", "edge"], src=[["Mastercard and Citizens: exclusive payments partnership, Jan 2023", MC2023], ["Mastercard: Citizens and the bank of the future, 2023", "https://newsroom.mastercard.com/news/perspectives/2023/citizens-bank-mastercard-expanded-partnership/"]]),
            P("debit", "Mastercard debit & ATM cards", "Every consumer and business debit and ATM card moved from Visa to Mastercard from January 2024, on 90% recycled plastic with Mastercard's Touch Card notch; Quest and Private Client customers get World Debit.", short="Mastercard debit",
              s=["con", "aff", "sme"], lc="everyday", o="P", at="Mastercard", ay="Jan 2024", neo=[2, "Converted from Visa."],
              mc="Debit is the bigger Mastercard volume at Citizens: around a thousand branches' worth of current accounts.",
              src=[["Citizens: recycled-plastic Mastercard debit cards, Dec 2023", DEBIT]]),
            P("wallets", "Apple Pay, Google Pay & Samsung Pay", "Credit and debit cards in all three phone wallets, as Mastercard tokens.",
              s=["con", "aff"], lc="move", o="P", at="Apple, Google, Samsung", neo=[2, "MDES tokens."],
              src=[["Citizens: digital wallets", CB + "digital-wallets/overview.aspx"]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Commercial & business cards", "blurb": "Citizens Edge, first from Mastercard's accelerator.", "div": "com", "rev": "com", "products": [
            P("edge", "Citizens Edge Mastercard", "A middle-market commercial card launched 9 October 2025, the first out of Mastercard's Mid-Market Accelerator (Citizens was its US launch partner, February 2025): 1.5% or more cash back, a virtual card, Navan travel and expense, Mastercard ID Theft Protection and VAT Reclaim.", short="Citizens Edge",
              s=["mid", "spon"], lc="move", st="new", ay="Oct 2025", o="P", at="Mastercard, Navan", neo=[3, "Built in Mastercard's Mid-Market Accelerator."],
              src=[["Citizens: Citizens Edge commercial card, Oct 2025", EDGE], ["FinTech Global: Mastercard Mid-Market Accelerator, Feb 2025", "https://fintech.global/?p=191855"]]),
            P("commcards", "Purchasing, virtual & business cards", "Purchasing, virtual and travel-and-expense cards for companies, and Everyday Points and Platinum business Mastercards for small businesses.",
              s=["sme", "mid"], lc="move", o="P", at="Mastercard", neo=[2, "Exclusive network; the P-card network is not stated publicly."],
              src=[["Citizens: credit card and payment services", CB + "corporate-finance/capability/credit-card-and-payment-services/overview.aspx"], ["Citizens: business Mastercard benefits", CB + "small-business/business-credit-cards/mastercard-benefits.aspx"]]),
        ]},
        {"id": "2.3", "ic": "zap", "name": "Real-time & P2P", "blurb": "Zelle, RTP, Payee Select.", "div": "com", "rev": "com", "products": [
            P("zelle", "Zelle", "Free person-to-person payments for consumers and, since February 2023, small businesses. Citizens is a participant, not one of Early Warning's owner banks.",
              s=["con", "sme"], lc="move", o="P", at="Early Warning Services", neo=[0, ""],
              src=[["Citizens: Zelle", CB + "mobile-and-online-banking/zelle.aspx"]]),
            P("rtp", "RTP instant payments", "A member-owner of The Clearing House, offering its RTP network to corporate clients since 2019; FedNow participation is not confirmed.",
              s=["mid", "fin"], lc="move", o="P", at="The Clearing House", ay="2019", neo=[0, ""],
              src=[["PYMNTS: Citizens and real-time payments, 2019", "https://www.pymnts.com/real-time-payments/2019/citizen-bank-corporate-real-time-rail-system/"], ["Citizens: instant vs real-time payments, 2025", CB + "corporate-finance/insights/comparing-instant-payments-and-real-time-payments.aspx"]]),
            P("payeeselect", "Citizens Payee Select", "A payouts platform (April 2025) where the payee chooses RTP, ACH or check through a portal in the client's brand, built with Verituity, in which Citizens took a stake.",
              s=["mid", "sme", "fin"], lc="move", st="new", ay="Apr 2025", o="P", at="Verituity", neo=[0, "No card payout option."],
              mc="Card and wallet endpoints through Mastercard Move would add the payout choice it lacks.",
              src=[["Citizens: Payee Select, Apr 2025", PAYEE]]),
        ]},
        {"id": "2.4", "ic": "arrow-left-right", "name": "Treasury rails & acceptance", "blurb": "accessOPTIMA, merchants, bills.", "div": "com", "rev": "com", "products": [
            P("accessoptima", "accessOPTIMA treasury", "The commercial cash-management portal for ACH, wires and high-volume payment files, with Citizens Account Validation to check payee accounts; Global Finance named Citizens a best treasury and cash management bank for 2026.", short="accessOPTIMA",
              s=["mid", "sme"], lc="everyday", neo=[0, ""],
              src=[["Citizens: cash management", CB + "small-business/cash-management/overview.aspx"], ["Citizens: Global Finance treasury award, Jun 2026", NEWS + "2026/2026-06-22.aspx"]]),
            P("merchant", "Merchant services", "Card acceptance for business clients through Fiserv, with Citizens Bank, N.A. as sponsor bank for First Data Merchant Services.",
              s=["sme", "mid"], lc="move", o="P", at="Fiserv", neo=[1, "Accepts Mastercard among other networks."],
              mc="A small-business acceptance book: merchant identification, Click to Pay and acceptance data fit.",
              src=[["Citizens: merchant services", CB + "small-business/merchant-services/overview.aspx"]]),
            P("billpay", "Bill Center", "Consumer bill pay and loan payments on Paymentus's instant payment network (February 2023).",
              s=["con"], lc="move", o="P", at="Paymentus", ay="Feb 2023", neo=[0, ""],
              src=[["BusinessWire: Paymentus and Citizens, Feb 2023", "https://www.businesswire.com/news/home/20230215005199/en"]]),
        ]},
        {"id": "2.5", "ic": "plug", "name": "Embedded payments", "blurb": "Banking for payments companies.", "div": "com", "rev": "com", "products": [
            P("embedded", "Embedded Payments", "Sponsor and settlement bank for US payments companies (payables, marketplaces, payroll, claims, card processors and wallets): more than 50 live partners and more than $1.5 trillion of third-party payments a year, by Citizens' count. In October 2026 Citizens named a head of treasury and wholesale payments strategy and partnerships, building or partnering case by case.",
              s=["fin"], lc="move", neo=[0, ""],
              src=[["Citizens: embedded payments", CB + "corporate-finance/capability/treasury-management/embedded-payments.aspx"], ["American Banker: Citizens payments exec on fintech competition, Oct 2026", AB_PAY]]),
        ]},
        {"id": "2.6", "ic": "globe", "name": "Cross-border & digital money", "blurb": "Stablecoins for 2027.", "div": "com", "rev": "com", "products": [
            P("stablecoin", "Stablecoins & tokenised deposits", "A member of Open Standard's Open USD stablecoin consortium (July 2026) and exploring The Clearing House's tokenised-deposit network and FIS's stablecoin work; Citizens says it is exploring Mastercard's stablecoin capabilities, with corporate products planned for 2027, cross-border and emerging-market payments first.", short="Stablecoins for 2027",
              s=["mid", "fin"], lc="move", st="new", ay="2026", o="P", at="Open Standard, The Clearing House, FIS", neo=[0, "Exploring Mastercard; nothing live."],
              mc="The strongest current lead: Mastercard Move for cross-border, BVNK's stablecoin payouts (Mastercard agreed to buy BVNK in March 2026) and the Multi-Token Network.",
              src=[["American Banker: how Citizens is placing its bets in digital assets, Jul 2026", AB_ASSETS], ["Banking Dive: Open Standard's Open USD consortium, Jul 2026", "https://www.bankingdive.com/news/stablecoin-open-standard-bridge-abrams-bny-stripe-mastercard-visa-coinbase-adyen/824200/"]]),
            P("fx", "FX & hedging", "Foreign exchange, interest-rate and commodity hedging for commercial clients.",
              s=["mid", "spon"], lc="move", neo=[0, ""],
              src=[["Citizens: commercial capabilities brochure", CB + "assets/CB_PDF/Commercial_Capabilities_Brochure.pdf"]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account and payment: prove who the customer is and keep their money safe, learn from the data, let other software in through Citizens' own open-banking API, reward the card, and serve the commercial client before they ask.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Identity, fraud & security", "blurb": "Mastercard named in the contract.", "div": "cfg", "rev": "oth", "products": [
            P("idfraud", "Digital identity & fraud", "The 2023 agreement names Mastercard as Citizens' provider of digital identity, authentication and fraud tools; the specific products have not been made public. Cardholders get Mastercard ID Theft Protection, and commercial clients Citizens Account Validation.",
              s=["con", "sme", "mid"], lc="open", o="P", at="Mastercard", neo=[1, "Contracted; deployments not named."],
              mc="Decision Intelligence for cards, and scam tools for Zelle and RTP, are the obvious deployments of a contract already signed.",
              src=[["Mastercard and Citizens: exclusive payments partnership, Jan 2023", MC2023]]),
            P("security", "Security & third-party risk", "A chief security officer since February 2024 (Brendan Goode); in April 2026 a vendor incident exposed mostly masked test data and a limited set of customer data.",
              s=["con", "mid"], lc="beyond", neo=[0, ""],
              src=[["Citizens: statement on a third-party vendor incident, Apr 2026", NEWS + "2026/2026-04-21.aspx"]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data & AI", "blurb": "A quarter of calls to AI by end-2026.", "div": "cfg", "rev": "oth", "products": [
            P("ai", "AI in Reimagine the Bank", "AI tools have made engineers about 30% more productive; the contact centre aims for 25% of calls handled by AI agents by the end of 2026 and 50% later; AI agents are rebuilding the commercial back office; and CiZi, an AI assistant, is in the new consumer mobile platform (2Q26). Microsoft Copilot and Anthropic's Claude are both in use or under evaluation.",
              s=["con", "mid"], lc="beyond", st="new", neo=[0, ""],
              src=[["Banking Dive: Coughlin on AI, Mar 2026", BD_AI], ["PYMNTS: Reimagine the Bank, Jul 2026", "https://www.pymnts.com/?p=3968233"]]),
            P("cfgindia", "CFG India", "An AI-first innovation hub and global capability centre in Bengaluru, supported by Infosys (February 2026); a managing director was named in July 2026.",
              s=["inst"], lc="beyond", st="new", ay="Feb 2026", o="P", at="Infosys", neo=[0, ""],
              src=[["Infosys: AI-first innovation hub with Citizens, Feb 2026", "https://www.infosys.com/newsroom/press-releases/2026/collaborates-ai-first-innovation-hub.html"]]),
        ]},
        {"id": "3.3", "ic": "webhook", "name": "Open banking & APIs", "blurb": "An FDX API, and switching on Mastercard.", "div": "cfg", "rev": "oth", "products": [
            P("openapi", "Citizens Open Banking API", "An FDX-standard API (March 2025) giving aggregators, fintechs and accounting platforms balances and transactions for retail, business, commercial and private-bank customers in place of screen-scraping; a Datos Insights gold medal in November 2025.",
              s=["fin", "con", "mid"], lc="beyond", st="new", ay="Mar 2025", neo=[1, "Citizens' own API; Mastercard is the contracted open-banking provider."],
              mc="Whatever the rewritten 1033 rule allows (a proposal went for review in August 2026, reopening data-access fees), Mastercard Open Finance is the contracted partner for pay-by-bank, verification and data on top of this API.",
              src=[["Citizens: open banking API, Mar 2025", FDX], ["Citizens: Datos Insights award, Nov 2025", NEWS + "2025/2025-11-05.aspx"], ["Consumer Finance Monitor: 1033 proposal to OIRA, Aug 2026", "https://www.consumerfinancemonitor.com/2026/08/06/cfpb-sends-new-section-1033-open-banking-proposal-to-oira-for-review/"]]),
            P("switchpay", "Switch Payments", "Move card-on-file payments with more than 70 billers (Netflix, Amazon, Spotify, Verizon) and redirect a paycheck from inside the Citizens app, powered by Mastercard open-finance technology (July 2025).",
              s=["con"], lc="open", st="new", ay="Jul 2025", o="P", at="Mastercard", neo=[3, "Mastercard open finance."],
              src=[["Citizens: Switch Payments, Jul 2025", SWITCH]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Loyalty & benefits", "blurb": "Cash back, and Priceless on top.", "div": "con", "rev": "con", "products": [
            P("cardrewards", "Cash-back rewards", "The 2025 card suite pays cash back (up to 3% on dining, groceries and entertainment on Summit Reserve) rather than a branded points currency; no card-linked offers platform such as Cardlytics is in evidence.",
              s=["con", "aff"], lc="grow", neo=[1, "Citizens' own rewards."],
              mc="With no offers platform of its own, Mastercard's card-linked offers and merchant-funded value are an open door.",
              src=[["Citizens: new credit card suite, Jun 2025", SUITE]]),
            P("priceless", "Priceless & World benefits", "Priceless rotating merchant offers on Amp, Lyft savings on Spring, and more than $750 of premium travel benefits on Summit Reserve (Priority Pass, Global Entry or TSA PreCheck, Lyft), plus World Debit benefits for Quest and Private Client.", short="Priceless & World benefits",
              s=["con", "aff", "pvt"], lc="beyond", o="P", at="Mastercard", neo=[3, "Mastercard's own benefits."],
              src=[["Citizens: new credit card suite, Jun 2025", SUITE], ["Citizens: credit cards", CB + "credit-cards/overview.aspx"]]),
        ]},
        {"id": "3.5", "ic": "sparkles", "name": "Commercial servicing", "blurb": "Serve before they ask.", "div": "com", "rev": "com", "products": [
            P("digitalbutler", "Citizens Digital Butler", "A proactive engagement platform for commercial clients; a Celent Model Bank award in March 2024.",
              s=["mid"], lc="everyday", neo=[0, ""], src=[["Citizens newsroom, 2024", NEWS + "2024.aspx"]]),
            P("cashflow", "Cash Flow Essentials", "A $49-a-month online cash-management tool for small businesses (2023) with cash-flow forecasting added in May 2024.",
              s=["sme"], lc="everyday", neo=[0, ""], src=[["Citizens: Cash Flow Essentials forecasting, Jul 2024", NEWS + "2024/2024-07-15.aspx"]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Citizens' 'three-legged stool' (a transformed Consumer Bank, the Commercial Bank and a premier Private Bank) opened out into what customers buy.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Everyday banking", "blurb": "$136 billion of consumer deposits.", "div": "con", "rev": "con", "products": [
            P("onedeposit", "One Deposit Checking", "Entry checking whose $9.99 monthly fee is waived with one deposit a statement period; up to $600 for new accounts in October 2026.",
              s=["con"], lc="open", neo=[2, "Mastercard debit."], src=[["Citizens: checking offer, 2026", CB + "promo/checking/drc-2026-q3.aspx"]]),
            P("quest", "Citizens Quest & Private Client", "The mass-affluent tiers: Quest (fee waived at $5,000 of monthly deposits or $25,000 of balances; Summit Reserve for $95) and Private Client (from $200,000; Summit Reserve free, and the Private Client World Elite Mastercard, the first US card with the Touch Card notch, May 2023).", short="Quest & Private Client",
              s=["aff"], lc="grow", neo=[2, "World Debit and World Elite Mastercard."],
              src=[["Citizens: checking offer, 2026", CB + "promo/checking/drc-2026-q3.aspx"], ["Citizens: Private Client World Elite Mastercard, May 2023", NEWS + "2023/2023-05-24-120030974.aspx"]]),
            P("deposits", "Savings, money market & CDs", "Across the bank, $22.4 billion of savings, $63.4 billion of money-market and $20.0 billion of time deposits at 3Q26; Consumer Banking averages $135.6 billion of deposits.",
              s=["con", "aff"], lc="grow", neo=[0, ""], src=[["3Q26 financial supplement", Q3F]]),
        ]},
        {"id": "4.2", "ic": "credit-card", "name": "Credit cards", "blurb": "A new suite, all Mastercard.", "div": "con", "rev": "con", "products": [
            P("suite", "The 2025 card suite", "Launched 12 June 2025: Amp (credit-builder), Spring World (lowest rate, 18 months 0% on transfers), Summit World (3% dining and groceries) and Summit Reserve World Elite ($295, metal, 3% on dining, groceries and entertainment), plus a Private Bank card; Cash Back Plus and other legacy cards closed to new applicants. New card originations were up more than 50% in early 2026 and card fees were $90 million in 3Q26.", short="Amp, Spring, Summit",
              s=["con", "aff"], lc="borrow", st="new", ay="Jun 2025", o="P", at="Mastercard", neo=[2, "World and World Elite Mastercard."],
              src=[["Citizens: new credit card suite, Jun 2025", SUITE], ["3Q26 earnings release", Q3R]]),
        ]},
        {"id": "4.3", "ic": "house", "name": "Home & education lending", "blurb": "#1 in home equity.", "div": "con", "rev": "con", "products": [
            P("mortgage", "Mortgages", "$37.0 billion of residential mortgages (up 7%), including the Private Bank's jumbo lending; Franklin American Mortgage was acquired in 2018.",
              s=["home", "pvt"], lc="borrow", neo=[0, ""], src=[["3Q26 financial supplement", Q3F]]),
            P("heloc", "Home equity", "$20.9 billion of home-equity lines (up 14%); management calls Citizens the largest US home-equity originator.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["3Q26 financial supplement", Q3F], ["Webull: 2Q26 call", "https://www.webull.com/news/15276538662233088"]]),
            P("student", "Student loans & refinancing", "National undergraduate, graduate and parent loans and refinancing for professional degrees: $8.0 billion, after about $1.9 billion of purchased loans were sold in 2025.",
              s=["home", "con"], lc="borrow", neo=[0, ""], src=[["3Q26 financial supplement", Q3F]]),
            P("runoff", "Auto & personal loans (exited)", "Indirect auto lending stopped in July 2023 and the book is down to $1.2 billion; personal loans are no longer originated. Both now sit in the run-off book.", short="Auto & personal (exited)",
              s=["con"], lc="borrow", st="retired", neo=[0, ""], src=[["American Banker: Citizens ends dealer financing, 2023", "https://americanbanker.com/news/citizens-to-end-car-dealer-financing-program-this-summer"], ["3Q26 financial supplement", Q3F]]),
        ]},
        {"id": "4.4", "ic": "hand-coins", "name": "Citizens Pay", "blurb": "Point-of-sale credit, after Apple.", "div": "pay", "rev": "con", "products": [
            P("citizenspay", "Citizens Pay", "A reusable point-of-sale credit line with fixed instalments, paid for by merchants: Microsoft and Xbox All Access (2019–21), BJ's, ADT, Vivint, Wyndham, Trek and Wisetack for home services. Card and point-of-sale loans together ('other retail') were $3.9 billion at 3Q26, down 5%, and Citizens Pay went unmentioned on the 2026 earnings calls.",
              s=["con", "fin"], lc="borrow", st="flux", o="P", at="Microsoft, Wyndham, Trek, Wisetack", neo=[0, "No public network role."],
              mc="Mastercard Installments would give Citizens Pay distribution at every Mastercard checkout instead of one merchant programme at a time.",
              src=[["American Banker: Citizens and Microsoft, Dec 2021", "https://americanbanker.com/news/beyond-xbox-citizens-expands-point-of-sale-relationship-with-microsoft"], ["Citizens: Trek, Sep 2023", NEWS + "2023/2023-09-13-130027301.aspx"], ["3Q26 financial supplement", Q3F]]),
            P("applelost", "Apple's iPhone financing (ended)", "Citizens (as Citizens One) financed Apple's iPhone Upgrade Program and iPhone Payments from 2015–16; on 28 July 2026 Apple replaced them with Apple Upgrade, leases from Klarna. Existing loans run off.", short="Apple iPhone financing (ended)",
              s=["con"], lc="borrow", st="retired", ay="Jul 2026", o="P", at="Apple", neo=[0, ""],
              src=[["MacRumors: Apple Upgrade with Klarna, Jul 2026", APPLE], ["Payments Dive: Apple's instalment payments, Jul 2026", "https://www.paymentsdive.com/news/apples-installment-payments-target-affordability/826721/"]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Private Bank & Wealth", "blurb": "$18.5 billion of deposits in three years.", "div": "pb", "rev": "con", "products": [
            P("privatebank", "Citizens Private Bank", "Built from about 150 First Republic hires in June 2023 under Sue deTray: $18.5 billion of deposits (up $6.1 billion in a year), $11.7 billion of loans and $12.4 billion of client assets at 3Q26, a 20–25% return on equity and 16 cents of quarterly EPS; about 700 people, ten offices and Philadelphia added in October 2026.",
              s=["pvt"], lc="grow", st="new", ay="Oct 2023", neo=[1, "A Private Bank World Elite card."],
              src=[["Citizens: Private Bank launch, Oct 2023", NEWS + "2023/2023-10-19-140111740.aspx"], ["Citizens: Private Bank enters Philadelphia, Oct 2026", NEWS + "2026/2026-10-15.aspx"], ["3Q26 earnings release", Q3R]]),
            P("startups", "Founders & private stock lending", "Citizens for Startups (May 2025), liquidity lines for private equity and venture funds (August 2025) and Private Stock Lending against private-company equity (October 2025).",
              s=["pvt", "spon"], lc="borrow", st="new", ay="2025", neo=[0, ""],
              src=[["Citizens: Private Stock Lending, Oct 2025", NEWS + "2025/2025-10-09.aspx"]]),
            P("wealth", "Citizens Wealth", "Client assets of $61.9 billion at the end of 2025 ($35.9 billion managed) and record wealth fees of $109 million in 3Q26, grown by lifting advisory teams (New York, Newport Beach, Tampa) and Family Office Solutions (May 2026). Clarfeld Financial Advisors (2019) serves the wealthiest clients; Citizens Trust Company of Delaware opened in February 2025.", short="Wealth, Clarfeld, trust",
              s=["aff", "pvt"], lc="grow", neo=[0, ""],
              src=[["FY2025 10-K", K10], ["Citizens: Tampa wealth team, Aug 2026", NEWS + "2026/2026-08-26.aspx"], ["Citizens: Delaware trust company, Feb 2025", NEWS + "2025/2025-02-03.aspx"]]),
        ]},
        {"id": "4.6", "ic": "building-2", "name": "Commercial Banking", "blurb": "Middle market, 4,000+ relationships.", "div": "com", "rev": "com", "products": [
            P("midmarket", "Middle-market & corporate banking", "Lending and treasury for companies with roughly $500 million to $3 billion of revenue and more than 4,000 corporate relationships: $53.9 billion of commercial and industrial loans (up 15%), with commercial real estate run down to $23.3 billion.",
              s=["mid", "spon"], lc="borrow", neo=[1, "Commercial cards on Mastercard."],
              src=[["3Q26 financial supplement", Q3F], ["Citizens statement, Jul 2026", NEWS + "2026/2026-07-17-a.aspx"]]),
            P("specialty", "Sponsor, fund & asset-based finance", "Sponsor finance and leveraged lending, subscription lines for funds, asset-based lending through Citizens Business Capital and equipment finance through Citizens Asset Finance.", short="Sponsor & fund finance",
              s=["spon", "mid"], lc="borrow", neo=[0, ""],
              src=[["Citizens: commercial capabilities brochure", CB + "assets/CB_PDF/Commercial_Capabilities_Brochure.pdf"]]),
            P("smallbiz", "Business banking", "Checking, SBA lending, business Mastercards and Zelle for small businesses.",
              s=["sme"], lc="everyday", neo=[2, "Business debit and credit on Mastercard."], src=[["FY2025 10-K", K10]]),
        ]},
        {"id": "4.7", "ic": "chart-candlestick", "name": "Capital markets & advisory", "blurb": "A top-five sponsor bookrunner.", "div": "jmp", "rev": "com", "products": [
            P("jmp", "Citizens JMP", "M&A advice, equity and debt capital markets, syndications, research and trading, built on JMP Group (2021, about $149 million): $149 million of fees in 3Q26, a record second quarter, and number two among middle-market sponsor bookrunners in 2Q26.",
              s=["spon", "mid"], lc="grow", o="A", ay="2021", neo=[0, ""],
              src=[["8-K: JMP closing, Nov 2021", SEC + "759944/000075994421000155/jmpclosingpressrelease.htm"], ["3Q26 call highlights", CALL3Q]]),
            P("matrix", "Matrix Capital Markets", "Advisory boutique for downstream energy and convenience retail, bought for cash (February 2026), adding to Willamette Management Associates and DH Capital (2021).",
              s=["spon", "mid"], lc="grow", st="new", ay="Feb 2026", o="A", neo=[0, ""],
              src=[["Citizens: Matrix Capital Markets Group, Feb 2026", NEWS + "2026/2026-02-17-130222090.aspx"]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Citizens: a new mobile platform with an AI assistant, about 1,000 branches and 3,000 ATMs in 14 states, Citizens Access as a national online bank, Private Bank offices from Menlo Park to Palm Beach, and a contact centre moving to AI.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Mobile & online", "blurb": "A new platform, with CiZi.", "div": "con", "rev": "con", "products": [
            P("mobileapp", "Citizens mobile app", "Rated 4.75 from about 750,000 App Store ratings; card freeze and disputes, Zelle, wallet provisioning, Switch Payments, and, since the 2Q26 move to a new consumer platform, the CiZi AI assistant.",
              s=["con", "aff", "sme"], lc="everyday", st="new", neo=[1, "Switch Payments and wallets on Mastercard."],
              src=[["App Store: Citizens Bank Mobile Banking", "https://apps.apple.com/us/app/id388082488"], ["Banking Dive: Coughlin on AI, Mar 2026", BD_AI]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "About 1,000 in 14 states.", "div": "con", "rev": "con", "products": [
            P("branches", "Branch network", "About 1,000 branches (117 in supermarkets) and about 3,000 ATMs in New England, the Mid-Atlantic, the Midwest and the New York metro, 14 states and DC. The 2026 'NEXT' plan closes 100–120 in-store branches and opens 50–60 standalone branches for advice, wealth and business banking.",
              s=["con", "aff", "sme"], lc="everyday", neo=[0, ""],
              src=[["FY2025 10-K", K10], ["Banking Dive: Citizens closing in-store branches, Jul 2026", "https://www.bankingdive.com/news/citizens-closing-100-120-in-store-branches-open-50-60-mass-affluent-advice-wealth-private-bank/825563/"]]),
        ]},
        {"id": "5.3", "ic": "globe", "name": "Citizens Access", "blurb": "A national online bank.", "div": "con", "rev": "con", "products": [
            P("access", "Citizens Access", "An online-only savings and CD bank, nationally since 2018, which absorbed HSBC's US online deposits in 2022; management now calls it a 'deposit optimisation tool'. Balances are not disclosed.",
              s=["con"], lc="grow", ay="2018", neo=[0, "No card."],
              src=[["Citizens: Citizens Access launch, May 2018", NEWS + "2018/2018-05-14-115000484.aspx"], ["3Q26 call highlights", CALL3Q]]),
        ]},
        {"id": "5.4", "ic": "landmark", "name": "Private Bank offices", "blurb": "Menlo Park to Palm Beach.", "div": "pb", "rev": "con", "products": [
            P("pboffices", "Private Bank offices", "Offices in New York, Boston, Palm Beach, West Palm Beach, San Francisco, Menlo Park, Marin, Newport Beach, Del Mar and Greenwich, with Philadelphia added in October 2026 and 15–16 expected by the end of 2027.",
              s=["pvt"], lc="grow", st="new", neo=[0, ""],
              src=[["Citizens: Private Bank enters Philadelphia, Oct 2026", NEWS + "2026/2026-10-15.aspx"], ["Greenwich Free Press: Greenwich office, Mar 2026", "https://greenwichfreepress.com/news/business/citizens-expands-private-banking-platform-to-greenwich-with-new-mason-street-office-245163/"]]),
        ]},
        {"id": "5.5", "ic": "headset", "name": "Contact centre", "blurb": "Half the calls to AI, in time.", "div": "cfg", "rev": "oth", "products": [
            P("contactcentre", "Contact centre", "A full-service contact centre, about 70% answered offshore by a vendor, with a target of 25% of calls handled by AI agents by the end of 2026 and 50% later.",
              s=["con", "sme"], lc="everyday", neo=[0, "Nothing public on Consumer Clarity."],
              mc="Consumer Clarity and Smart Subscriptions answer 'what is this charge?' before it becomes a call, which is what an AI-first contact centre needs.",
              src=[["Banking Dive: Coughlin on AI, Mar 2026", BD_AI]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Citizens", "blurb": "Network and services in one contract.", "products": [
        P("mcatcz", "Mastercard at Citizens", "From PayPass on Citizens and Charter One debit (2006) and the Cash Back Plus World Mastercard (2015) to the 2023 exclusive deal, the debit conversion (2024), the Mid-Market Accelerator and Citizens Edge (2025), the new card suite (2025), Switch Payments (2025) and stablecoin talks (2026). Mastercard's US issuer business is led by co-president John Levitsky, with Julie Schanzer (US financial institutions) and Ginger Siegel (small and medium business) on recent launches.",
          s=["fin"], div="cfg", rev="oth", mc="The relationship this map is drawn for.",
          src=[["Mastercard and Citizens: exclusive payments partnership, Jan 2023", MC2023], ["Citizens: new credit card suite, Jun 2025", SUITE], ["Citizens: Citizens Edge, Oct 2025", EDGE]]),
    ]},
    {"id": "pillar-market", "name": "Regional banks in 2026", "blurb": "The water Citizens swims in.", "products": [
        P("regional", "A consolidating field", "Citizens is about the 23rd-largest US bank holding company ($234 billion); Fifth Third–Comerica, Huntington–Cadence and PNC–FirstBank all closed in early 2026, moving Fifth Third and Huntington ahead. Citizens says it prefers organic growth and buybacks, and calls bank deals a high bar.",
          s=["inst"], div="cfg", rev="oth",
          src=[["Fifth Third completes Comerica merger, Feb 2026", "https://ir.53.com/news/news-details/2026/Fifth-Third-Completes-Merger-with-Comerica-to-Become-9th-Largest-U-S--Bank/default.aspx"], ["American Banker: Citizens downplays M&A, Oct 2025", "https://www.americanbanker.com/news/citizens-downplays-interest-in-participating-in-m-a-boom"]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
