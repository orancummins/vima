"""ANZ Group's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 1H26 results and investor pack (1 May 2026),
the 3Q26 trading update (12 August 2026), ANZ's 2026 newsroom and ANZ, ANZ Plus, ANZ NZ and Suncorp Bank
product pages as read on 17 October 2026. ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

HY26 = "https://www.anz.com.au/newsroom/media/2026/may/2026-half-year-result---proposed-final-dividend/"
PRES = "https://www.anz.com/content/dam/anzcom/shareholder/1H26-results-announcement/1H26-ANZ-Results-presentation-and-IDP.pdf"
Q3 = "https://www.anz.com.au/newsroom/media/2026/august/2026-thirdquarter-trading-update/"
FY25 = "https://www.anz.com.au/bluenotes/2025/november/anz-full-year-results-2025-full-coverage-fy25/"
STRAT = "https://filingreader.com/news-wire/newzealand/2025-10-13/anz-targets-13-rote-by-2030-announces-cost-cuts"
EXCO = "https://www.anz.com/shareholder/centre/about/executive-committee/"
BOARD = "https://www.anz.com/shareholder/centre/about/board-of-directors/"
NZCEO = "https://www.anz.com.au/newsroom/media/2026/june/anz-nz-ceo-antonia-watson-to-retire--ben-kelleher-to-take-over/"
SUNWELCOME = "https://www.anz.com.au/newsroom/media/2026/september/ANZ-prepares-to-welcome-suncorp-bank-customers/"
SUNHOME = "https://www.suncorpbank.com.au/"
SUNACCT = "https://www.suncorpbank.com.au/bank-and-save/everyday-accounts.html"
SUNCC = "https://www.suncorpbank.com.au/help-support/credit-cards.html"
WLAGREE = "https://www.anz.com.au/newsroom/media/2026/april/anz-to-acquire-worldline-sas-share-of-anz-worldlinejjoint-venture/"
WLDONE = "https://www.anz.com.au/newsroom/media/2026/july/anz-completes-acquisition-of-anz-worldline/"
WLJV = "https://anz.com.au/content/dam/anzcomau/mediacentre/pdfs/mediareleases/2020/December/201215%20-%20ANZ%20enters%20joint-venture%20with%20Worldline%20to%20provide%20leading%20payments%20technology%20and%20merchant%20services%20in%20Australia.FINAL.pdf"
CREDIT = "https://www.anz.com.au/personal/credit-cards/"
CCCHANGE = "https://www.creditcard.com.au/anz-credit-card-changes-october-2026/"
BIZCC = "https://www.anz.com.au/business/credit-cards/"
BIZBLACK = "https://finder.com.au/anz-business-black-card"
DEBIT = "https://www.anz.com.au/personal/bank-accounts/everyday-accounts/visa-debit-card/"
PLUS = "https://www.anz.com.au/plus/"
PLUS24 = "https://www.bankingday.com/anz-upbeat-on-plus"
IMT = "https://www.anz.com.au/newsroom/media/2026/april/ANZ-introduces-safer-faster-International-Money-Transfers/"
SCAMS = "https://www.anz.com.au/newsroom/media/2026/august/anz-customer-scam-losses-fall-despite-increased-scam-activity/"
BIZSCAMS = "https://www.anz.com.au/newsroom/media/2026/october/anz-urges-businesses-to-stay-vigilant-as-ai-enabled-scams-and-identity-fraud-evolve/"
FALCON = "https://www.anz.com.au/newsroom/media/2026/may/ANZ-brings-Falcon-to-life-in-show-stopping-symbol-of-customer-protection/"
CRM = "https://www.anz.com.au/newsroom/media/2026/february/anz-launches-agentic-ai-powered-crm-to-transform-business-banking/"
TOKEN = "https://www.anz.com.au/newsroom/media/2026/september/anz-completes-landmark-cross-border-tokenised-deposit-payment-wi/"
NZCC = "https://www.anz.co.nz/personal/credit-cards/"
LOOP = "https://www.anz.com.au/content/dam/anzcomau/news/New-Zealand/2026/April/news-release-anz-loop-puts-cash-back-into-the-wallets-of-our-visa-debit-and-credit-card-customers.pdf"
NZMC = "https://www.interest.co.nz/banking/98063/anz-nz-stop-offering-mastercard-credit-cards-april-it-goes-exclusive-rival-visa"
VISA10 = "https://eastandpartners.com/news/anz-expands-visa-debit/"
AMEX17 = "https://executivetraveller.com/anz-stops-issuing-american-express-credit-cards"
EDR = "https://woolworthsgroup.com.au/au/en/our-newsroom/media-releases/latest-news/2025/everyday-rewards-and-anz-team-up-to-unlock-more-savings-for-cred.html"
SPAY = "https://anz.com.au/content/dam/anzcomau/mediacentre/pdfs/mediareleases/2017/July/18-07-2017_ANZ%20partners%20with%20Samsung%20Pay%20to%20give%20customers%20more%20choice%20in%20mobile%20payments.pdf"
UPI = "https://www.electronicpaymentsinternational.com/news/anz-teams-up-with-cr2-to-accept-unionpay-cards-at-its-atms-and-merchant-terminals-180615-4603682"
RBAMR = "https://rba.gov.au/media-releases/2026/mr-26-10.html"
RBAIF = "https://www.rba.gov.au/payments-and-infrastructure/review-of-retail-payments-regulation/2026-03/conclusions-paper/interchange-fees.html"
APPLUS = "https://www.auspayplus.com.au/?p=8684"
PNG = "https://www.anz.com.au/newsroom/media/2026/february/ANZ-strengthens-leadership-to-support-growth/"
SAT = "https://www.anz.com.au/newsroom/media/2026/june/anz-announces-saturday-trading-at-27-branches-nationwide/"
QLDNSW = "https://www.anz.com.au/newsroom/media/2026/march/ANZ-invests-in-Queensland-and-NSW-branches/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · brands · reset", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: A$1.3 trillion of assets and an 11.6% return, more than 11 million customers in 29 markets, a bank dating from 1828, a new leadership team, and the ANZ 2030 reset with Suncorp Bank and ANZ Worldline folded in.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Cash profit A$3.78bn in 1H26.", "div": "group", "rev": "centre", "products": [
            P("balance", "Balance sheet & earnings", "1H26 to 31 March 2026: cash profit A$3,780 million (+14% excluding 2H25 one-offs), statutory A$3,650 million, cash RoTE 11.6%, cost-to-income 49.4%, CET1 12.39%; assets A$1,314 billion, net loans A$822 billion, deposits A$771 billion; market value A$108.4 billion. 3Q26 cash profit A$1.90 billion; FY25 cash profit A$6,896 million before A$1,109 million of one-offs. AA band at all three agencies.",
              s=["con"], neo=[0, ""], src=[["ANZ 1H26 result, May 2026", HY26], ["ANZ 1H26 presentation", PRES], ["ANZ 3Q26 update, Aug 2026", Q3], ["ANZ FY25 result, Nov 2025", FY25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Matos and O'Sullivan.", "div": "group", "rev": "centre", "products": [
            P("leadership", "Board & executive committee", "Chair Paul O'Sullivan, CEO Nuno Matos, CFO Farhan Faruqui, CRO Christine Palmer; Pedro Rodeia runs Australia Retail, Tammy Medard Business & Private Bank, Mark Whelan Institutional; Ben Kelleher replaced Antonia Watson as ANZ NZ CEO on 1 October 2026; Bruce Rush runs Suncorp Bank.",
              s=["corp"], st="flux", neo=[0, ""], src=[["ANZ: executive committee", EXCO], ["ANZ: board", BOARD], ["ANZ NZ CEO change, Jun 2026", NZCEO]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brands", "blurb": "Since 1828; Suncorp becomes ANZ.", "div": "group", "rev": "centre", "products": [
            P("brands", "Heritage & brands", "A history dating to 1828, a Big Four bank in Australia and the largest in New Zealand; brands ANZ, ANZ Plus, ANZ NZ and Suncorp Bank, which is becoming ANZ by June 2027; more than 11 million customers in 29 markets.",
              s=["con", "sun"], o="I", st="flux", neo=[0, ""], src=[["ANZ 1H26 presentation", PRES], ["ANZ: welcoming Suncorp Bank customers, Sep 2026", SUNWELCOME]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology", "blurb": "One front end by 2027.", "div": "plus", "rev": "retail", "products": [
            P("tech", "Single customer front-end", "ANZ Plus becomes the one digital front end for all 8 million retail and small-business customers by September 2027 (45% complete targeted by September 2026); automation and AI are one of four simplification programmes.",
              s=["con", "sme"], st="flux", neo=[0, ""], src=[["ANZ 1H26 presentation", PRES], ["ANZ 3Q26 update, Aug 2026", Q3]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "ANZ 2030", "blurb": "RoTE 13% by FY30.", "div": "group", "rev": "centre", "products": [
            P("strategy", "ANZ 2030", "Set out on 13 October 2025: customer first, simplicity, resilience, value. RoTE 12% by FY28 and 13% by FY30 ⚠, cost-to-income in the mid-40s by FY28, about A$800 million of gross savings in FY26 and 3,500 roles cut (84% gone by 30 June 2026).",
              s=["corp"], st="new", neo=[0, ""], src=[["FilingReader: ANZ 2030 targets, Oct 2025", STRAT], ["ANZ 1H26 presentation", PRES], ["ANZ 3Q26 update, Aug 2026", Q3]]),
            P("deals", "Deals", "Suncorp Bank bought 31 July 2024 (A$500 million of yearly synergies by FY29, A$745 million integration cost); Worldline's 51% of ANZ Worldline bought for A$89 million enterprise value, completed 31 July 2026.",
              s=["sun", "sme"], o="A", neo=[0, ""], src=[["Suncorp Bank", SUNHOME], ["ANZ: ANZ Worldline completed, Jul 2026", WLDONE], ["ANZ 1H26 presentation", PRES]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Visa debit with eftpos, seven Visa credit cards being trimmed for the RBA's 0.3% cap, Visa business cards, Suncorp Bank's Visa debit, ANZ Worldline acquiring every network, NPP and PayTo, and cross-border transfers and tokenised deposits.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit & wallets", "blurb": "Visa debit, with eftpos.", "div": "anz", "rev": "retail", "products": [
            P("debit", "ANZ Access Visa Debit", "The debit card on ANZ's classic everyday accounts, on Visa; customers can also choose savings or cheque at the terminal, which runs on eftpos ⚠. Visa Debit has been exclusive since a 2010 deal.", short="Access Visa Debit",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["ANZ: Visa Debit card", DEBIT], ["East & Partners: ANZ expands Visa Debit, 2010", VISA10]]),
            P("plusdebit", "ANZ Plus Visa Debit", "The card on ANZ Plus accounts, opened only in the ANZ Plus app; works wherever Visa is accepted.", short="ANZ Plus Visa Debit",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["ANZ: Visa Debit card", DEBIT], ["ANZ Plus", PLUS]]),
            P("wallets", "Mobile wallets", "Apple Pay, Google Pay and Samsung Pay (since July 2017) for ANZ Visa cards.",
              s=["con"], lc="move", o="P", at="Apple, Google, Samsung", neo=[0, "Visa tokens."], src=[["ANZ: Samsung Pay, Jul 2017", SPAY], ["ANZ: Visa Debit card", DEBIT]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Seven cards, all Visa.", "div": "anz", "rev": "retail", "products": [
            P("credit", "ANZ credit cards", "Rewards Black and Platinum, Frequent Flyer Black and Platinum, Platinum, First and Low Rate, all on Visa; Amex companion cards were dropped in 2017.", short="Credit (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="A Big Four bank with no Mastercard credit card.",
              src=[["ANZ: credit cards", CREDIT], ["Executive Traveller: ANZ drops Amex, 2017", AMEX17]]),
            P("cardchanges", "Points caps & insurance cuts", "From 28 October 2026 points stop above A$25,000 a statement on Platinum and A$50,000 on Black cards, and the cash-advance fee rises to 3.5%; travel insurance is cut from 9 December 2026 and 24 March 2027, as the RBA's credit interchange cap falls from 0.8% to 0.3%.",
              s=["con"], lc="borrow", st="flux", ay="Oct 2026", neo=[0, "Visa."], src=[["creditcard.com.au: ANZ card changes, 2026", CCCHANGE], ["RBA: interchange conclusions, Mar 2026", RBAIF]]),
        ]},
        {"id": "2.3", "ic": "briefcase-business", "name": "Business cards", "blurb": "Visa business cards.", "div": "anz", "rev": "bpb", "products": [
            P("bizcards", "ANZ business credit cards", "Qantas Business Rewards, Business Black, Business 55 Interest Free Days and Business Low Rate; ANZ's page names no network, but Business Black is sold as Visa ⚠.",
              s=["sme"], lc="borrow", o="P", at="Visa", neo=[0, "Visa ⚠."], src=[["ANZ: business credit cards", BIZCC], ["Finder: ANZ Business Black", BIZBLACK]]),
            P("commercial", "Corporate & purchasing cards", "Corporate and purchasing cards for larger clients; the Australian network was not confirmed ⚠, while ANZ NZ sells Visa Corporate and Visa Purchasing cards. The RBA kept the commercial credit cap at 0.8%.",
              s=["corp"], lc="move", neo=[None, "Network not confirmed in Australia."],
              mc="Commercial interchange stays at 0.8%, the one card line the RBA left alone.",
              src=[["ANZ NZ: credit cards", NZCC], ["RBA: interchange conclusions, Mar 2026", RBAIF]]),
        ]},
        {"id": "2.4", "ic": "wallet", "name": "Suncorp Bank cards", "blurb": "Visa debit; credit gone to NAB.", "div": "suncorp", "rev": "suncorp", "products": [
            P("sundebit", "Suncorp Bank Visa Debit", "The card on Suncorp Bank everyday accounts, on Visa, with Apple Pay and Google Pay; customers move to ANZ's systems by June 2027.",
              s=["sun"], lc="everyday", st="flux", o="A", at="Visa", neo=[0, "Visa."], src=[["Suncorp Bank: everyday accounts", SUNACCT], ["ANZ: welcoming Suncorp Bank customers, Sep 2026", SUNWELCOME]]),
            P("suncredit", "Suncorp Clear Options credit cards", "Issued by NAB under the Suncorp name; the arrangement ended on 24 November 2025 and the cards became NAB MyCard cards. New applicants are sent to ANZ's Visa range. Network not confirmed ⚠.",
              s=["sun"], lc="borrow", st="retired", ay="Nov 2025", o="P", at="NAB", neo=[None, "Left the group; network ⚠."], src=[["Suncorp Bank: credit card changes", SUNCC]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "ANZ Worldline, now wholly ANZ's.", "div": "worldline", "rev": "bpb", "products": [
            P("worldline", "ANZ Worldline Payment Solutions", "In-store, online and integrated payments for Australian businesses; a joint venture since 2022 (ANZ then about 20% of acquiring volumes), fully owned from 31 July 2026 with about 270 staff. Accepts all networks, including Mastercard and UnionPay; must apply the surcharging ban from 1 October 2026.", short="ANZ Worldline (all networks)",
              s=["sme"], lc="move", st="new", ay="Jul 2026", o="A", at="Worldline", neo=[1, "Acquires Mastercard among all networks."],
              mc="The one place Mastercard runs through ANZ today, and now under ANZ's sole control.",
              src=[["ANZ: ANZ Worldline completed, Jul 2026", WLDONE], ["ANZ: agreement with Worldline, Apr 2026", WLAGREE], ["ANZ: Worldline JV, Dec 2020", WLJV], ["EPI: ANZ and UnionPay, 2018", UPI]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Account-to-account", "blurb": "NPP, PayTo, Confirmation of Payee.", "div": "anz", "rev": "retail", "products": [
            P("npp", "NPP, PayID, PayTo & BPAY", "Real-time payments on AP+'s rails through ANZ Plus, Internet Banking and Transactive ⚠; eftpos, NPP and BPAY are all run by AP+.",
              s=["con", "sme"], lc="move", o="P", at="AP+", neo=[0, "AP+ rails."], src=[["AP+: eftpos zero surcharge, Jun 2026", APPLUS]]),
            P("cop", "Confirmation of Payee", "Name checks on transfers: more than 476,000 payments abandoned after a mismatch warning between October 2025 and June 2026.",
              s=["con", "sme"], lc="move", st="new", neo=[0, ""],
              mc="A2A scam scoring would sit beside the name check.",
              src=[["ANZ: scam losses fall, Aug 2026", SCAMS]]),
        ]},
        {"id": "2.7", "ic": "earth", "name": "Cross-border & digital money", "blurb": "Transfers, tokenised deposits.", "div": "inst", "rev": "inst", "products": [
            P("imt", "International Money Transfers", "Upgraded on ANZ Plus in April 2026: 250+ destinations, near-real-time to some regions, in-app tracking and Falcon fraud checks; popular routes are New Zealand, India, the UK and the Pacific.",
              s=["con"], lc="move", st="new", ay="Apr 2026", neo=[0, ""],
              mc="Mastercard Move could carry part of migrants' remittances.",
              src=[["ANZ: International Money Transfers, Apr 2026", IMT]]),
            P("tokenised", "Tokenised deposits", "One of the world's first live corporate treasury payments in tokenised deposits on Swift's ledger, with BHP and Citi, US dollars Melbourne to New York (September 2026).",
              s=["corp"], lc="move", st="new", ay="Sep 2026", o="P", at="Swift, Citi", neo=[0, "Swift ledger."], src=[["ANZ: tokenised deposit payment, Sep 2026", TOKEN]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: Falcon fraud monitoring and a 24% fall in scam losses, an agentic AI CRM for bankers, and rewards that move into Everyday Rewards and, in New Zealand, Visa card-linked cashback.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & scams", "blurb": "Scam losses down 24%.", "div": "anz", "rev": "retail", "products": [
            P("falcon", "ANZ Falcon", "ANZ's fraud monitoring, branded Falcon, screening card and payment activity in real time, including international transfers.",
              s=["con", "sme"], lc="everyday", neo=[0, "ANZ's own."], src=[["ANZ: Falcon, May 2026", FALCON], ["ANZ: International Money Transfers, Apr 2026", IMT]]),
            P("scams", "Scam prevention", "Customer scam losses down 24% from October 2025 to June 2026, more than A$100 million prevented and recovered, and a First Responders team resolving 94% of about 170,000 scam calls at first contact.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["ANZ: scam losses fall, Aug 2026", SCAMS]]),
            P("security", "Identity & mule controls", "Behavioural biometrics, fraud analytics and tighter onboarding against accounts opened with stolen identities for mule activity; ANZ Shield codes.",
              s=["con", "sme"], lc="open", st="new", neo=[0, ""],
              mc="Identity and mule-account scoring are a stated need.",
              src=[["ANZ: business scam warning, Oct 2026", BIZSCAMS]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI", "blurb": "Agentforce for bankers.", "div": "anz", "rev": "bpb", "products": [
            P("agentforce", "Agentic AI CRM", "Salesforce Agentforce 360 in a new business-banking CRM, the first in APAC at scale (February 2026), joining 20 platforms and saving bankers about a working month a year.",
              s=["sme"], lc="everyday", st="new", ay="Feb 2026", o="P", at="Salesforce", neo=[0, ""],
              mc="Agentic tools for staff, none yet for customers' payments.",
              src=[["ANZ: agentic AI CRM, Feb 2026", CRM]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & offers", "blurb": "Everyday Rewards; Loop in NZ.", "div": "anz", "rev": "retail", "products": [
            P("rewards", "ANZ Rewards & Qantas Points", "ANZ Reward Points convert to Everyday Rewards (October 2025) and Velocity; Qantas Points on Frequent Flyer cards; earning capped from 28 October 2026.",
              s=["con"], lc="grow", st="flux", o="P", at="Woolworths, Qantas", neo=[0, "Visa cards."],
              mc="Merchant-funded offers could replace rewards squeezed by the 0.3% cap.",
              src=[["Woolworths: Everyday Rewards and ANZ, Oct 2025", EDR], ["creditcard.com.au: ANZ card changes, 2026", CCCHANGE]]),
            P("loop", "ANZ Loop", "Card-linked cashback in ANZ NZ's goMoney app for Visa Debit and credit holders, a first for New Zealand banking, built on Visa Offers Exchange with The Warehouse, Noel Leeming and others (30 April 2026).",
              s=["kiwi"], lc="grow", st="new", ay="Apr 2026", o="P", at="Visa", neo=[0, "Visa Offers Exchange."], src=[["ANZ NZ: ANZ Loop, Apr 2026", LOOP]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: A$348 billion of Australian home loans and A$101 billion of retail deposits, business banking for 580,000, Institutional across 29 markets, ANZ New Zealand, and Suncorp Bank's 1.26 million customers on their way to ANZ.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Home loans & deposits", "blurb": "A$348bn, 13.2% share.", "div": "anz", "rev": "retail", "products": [
            P("homeloans", "Home loans", "A$348 billion in Australia at March 2026, a 13.2% share (excluding Suncorp), with about a third originated by ANZ's own lenders and up to 50% more branch lenders planned.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["ANZ 1H26 presentation", PRES]]),
            P("accounts", "Everyday accounts & savings", "6.5 million Australia Retail customers and A$101 billion of save-and-transact deposits; main bank for 11.6% of Australians (including ANZ Plus).",
              s=["con"], lc="everyday", neo=[0, "Visa debit."], src=[["ANZ 1H26 presentation", PRES]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Business & Private Bank", "blurb": "580,000 customers.", "div": "anz", "rev": "bpb", "products": [
            P("bpb", "Business & Private Bank", "580,000 customers, A$68 billion of loans and A$87 billion of deposits; a 16.4% main-bank share; bankers up by close to 50% and the ANZ Plus front end for small businesses by late 2027.",
              s=["sme"], lc="everyday", neo=[0, "Visa cards; Worldline acquiring."], src=[["ANZ 1H26 presentation", PRES], ["ANZ: agentic AI CRM, Feb 2026", CRM]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Institutional", "blurb": "No.1 in Australia and NZ.", "div": "inst", "rev": "inst", "products": [
            P("institutional", "Institutional banking", "Transaction banking, markets (A$1,108 million revenue in 1H26) and corporate finance across about 29 markets; A$133 billion of operational deposits; ranked first for relationship strength in Australia and New Zealand.",
              s=["corp"], lc="move", neo=[0, ""], src=[["ANZ 1H26 presentation", PRES], ["ANZ: tokenised deposit payment, Sep 2026", TOKEN]]),
            P("pacific", "Pacific", "Banking in eight Pacific markets and Papua New Guinea (since 1910), where clients use Transactive Global.",
              s=["corp"], lc="move", neo=[None, "Card networks not checked."], src=[["ANZ: PNG leadership, Feb 2026", PNG]]),
        ]},
        {"id": "4.4", "ic": "flag", "name": "ANZ New Zealand", "blurb": "Largest NZ bank, all Visa.", "div": "anznz", "rev": "nz", "products": [
            P("anznz", "ANZ Bank New Zealand", "2.69 million customers, NZ$141 billion of loans and NZ$64 billion of deposits; main bank for 33.3% of personal and 31.6% of business customers. Every card is Visa since ANZ NZ dropped Mastercard credit cards in April 2019; a NZ$125 million class-action provision in 3Q26.", short="ANZ NZ (Visa)",
              s=["kiwi"], lc="everyday", o="P", at="Visa", neo=[0, "Visa since 2019."],
              mc="Mastercard left ANZ NZ in 2019.",
              src=[["ANZ 1H26 presentation", PRES], ["ANZ NZ: credit cards", NZCC], ["interest.co.nz: ANZ NZ leaves Mastercard, 2019", NZMC], ["ANZ 3Q26 update, Aug 2026", Q3]]),
        ]},
        {"id": "4.5", "ic": "refresh-cw", "name": "Suncorp Bank", "blurb": "1.26m moving by June 2027.", "div": "suncorp", "rev": "suncorp", "products": [
            P("suncorpbank", "Suncorp Bank", "1.26 million customers, A$74 billion of loans and A$34 billion of deposits; retail NPS +17.8. Customers were told in September 2026 that they move to ANZ's systems by June 2027; branch numbers and jobs held for three years after the July 2024 purchase.",
              s=["sun"], lc="everyday", st="flux", o="A", neo=[0, "Visa debit."], src=[["ANZ 1H26 presentation", PRES], ["ANZ: welcoming Suncorp Bank customers, Sep 2026", SUNWELCOME]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: ANZ Plus becoming the one app for 8 million, the classic ANZ app and goMoney in New Zealand, branches, brokers, and Transactive for institutions.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "ANZ Plus & apps", "blurb": "One front end by 2027.", "div": "plus", "rev": "retail", "products": [
            P("plusapp", "ANZ Plus", "The digital bank launched in 2022: about 850,000 customers and A$16 billion of deposits at September 2024, about a million by 2025 ⚠; becoming the front end for all retail and small-business customers by September 2027.",
              s=["con", "sme"], lc="open", st="flux", neo=[0, "Visa debit."], src=[["Banking Day: ANZ upbeat on Plus, Nov 2024", PLUS24], ["ANZ 1H26 presentation", PRES]]),
            P("anzapp", "ANZ App & Internet Banking", "The classic app and Internet Banking, being replaced by ANZ Plus; ANZ Plus Coaches help customers move.",
              s=["con"], lc="everyday", st="flux", neo=[0, ""], src=[["ANZ 1H26 presentation", PRES], ["ANZ: International Money Transfers, Apr 2026", IMT]]),
            P("gomoney", "goMoney (New Zealand)", "ANZ NZ's app, where ANZ Loop's Visa offers appear under the Cards tab.",
              s=["kiwi"], lc="everyday", neo=[0, "Visa offers."], src=[["ANZ NZ: ANZ Loop, Apr 2026", LOOP]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "Saturday trading, Queensland.", "div": "anz", "rev": "retail", "products": [
            P("branches", "Branches", "Saturday trading at 27 branches (June 2026), branch investment in Queensland and New South Wales, and regional branch numbers held for three years after the Suncorp purchase.",
              s=["con", "sun"], lc="everyday", neo=[0, ""], src=[["ANZ: Saturday trading, Jun 2026", SAT], ["ANZ: Queensland and NSW branches, Mar 2026", QLDNSW], ["ANZ: welcoming Suncorp Bank customers, Sep 2026", SUNWELCOME]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Brokers", "blurb": "Most home-loan flow.", "div": "anz", "rev": "retail", "products": [
            P("brokers", "Mortgage brokers", "ANZ's own lenders originated only 31–32% of Australian home loans in 1H26, so most come through brokers ⚠; ANZ plans up to 50% more branch lenders.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["ANZ 1H26 presentation", PRES]]),
        ]},
        {"id": "5.4", "ic": "monitor", "name": "Transactive Global", "blurb": "Institutional and mid-market.", "div": "inst", "rev": "inst", "products": [
            P("transactive", "ANZ Transactive Global", "The cash-management portal for institutions, being extended to the middle market.",
              s=["corp", "sme"], lc="move", neo=[0, ""], src=[["ANZ 1H26 presentation", PRES]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at ANZ", "blurb": "A Visa group; Mastercard in acquiring.", "products": [
        P("mcatanz", "Mastercard at ANZ", "Every ANZ, ANZ Plus, ANZ NZ and Suncorp Bank card found is Visa: debit has been Visa-exclusive since 2010, ANZ NZ dropped Mastercard credit cards in 2019, and ANZ Loop runs on Visa Offers Exchange. No ANZ–Mastercard initiative was found from 2020 to 2026 ⚠. Mastercard reaches ANZ through ANZ Worldline, which acquires every network and has been wholly ANZ's since July 2026.",
          s=["con"], div="group", rev="centre", mc="The relationship this map is drawn for.",
          src=[["East & Partners: ANZ expands Visa Debit, 2010", VISA10], ["interest.co.nz: ANZ NZ leaves Mastercard, 2019", NZMC], ["ANZ: ANZ Worldline completed, Jul 2026", WLDONE]]),
    ]},
    {"id": "pillar-market", "name": "Australian payments", "blurb": "Surcharge ban, 0.3% cap, AP+.", "products": [
        P("market", "The Australian market", "From 1 October 2026 surcharges are banned on eftpos, Mastercard and Visa, the debit cap falls to 8c or 0.16% and the consumer credit cap to 0.3%; commercial stays at 0.8%; foreign cards are capped at 1.0% from April 2027; wallets, BNPL and three-party schemes are next. AP+ runs eftpos, NPP and BPAY and promotes least-cost routing.",
          s=["con"], div="group", rev="centre", src=[["RBA: conclusions, Mar 2026", RBAMR], ["RBA: interchange conclusions, Mar 2026", RBAIF], ["AP+: eftpos zero surcharge, Jun 2026", APPLUS]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
