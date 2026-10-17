"""Western Union's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Western Union's own: Q2 2026 results (30 July 2026), FY2025 results and the 2025 Form 10-K
(20 February 2026), the 2026 proxy and its 2025–26 releases. The Intermex deal had not closed by
17 October 2026. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q4CDN = "https://s21.q4cdn.com/100551446/files/"
Q2 = Q4CDN + "doc_financials/2026/q2/2Q26-Press-Release.pdf"
Q1 = Q4CDN + "doc_financials/2026/q1/Q1-2026-Press-Release-FINAL.pdf"
FY25 = Q4CDN + "doc_financials/2025/q4/4Q25-Press-Release.pdf"
BEYOND = Q4CDN + "doc_presentations/2025/11/Western-Union-Investor-Day-Press-Release_Final.pdf"
SEC = "https://www.sec.gov/Archives/edgar/data/1365135/"
TENK = SEC + "000119312526061340/wu-20251231.htm"
PROXY = SEC + "000120677426000167/wu4500131_def14a.htm"
HSR = SEC + "000119312526412336/d160759d8k.htm"
CLO = SEC + "000119312526314213/d856492d8k.htm"
PR = "https://ir.westernunion.com/news/archived-press-releases/press-release-details/"
IMX = PR + "2025/Western-Union-to-Acquire-International-Money-Express-Inc-/default.aspx"
IMXUPD = PR + "2026/Western-Union-and-Intermex-Provide-Update-on-Pending-Acquisition/default.aspx"
USDPT25 = PR + "2025/Western-Union-Announces-USDPT-Stablecoin-on-Solana-and-Digital-Asset-Network/default.aspx"
USDPT26 = PR + "2026/Western-Union-Launches-USDPT-on-Solana-Advancing-Regulated-Digital-Infrastructure-for-Global-Payments/default.aspx"
BYBIT = PR + "2026/Bybit-Becomes-First-Major-Crypto-Exchange-to-Integrate-Western-Unions-USDPT-Stablecoin-Bridging-Two-Financial-Worlds-Through-One-Stablecoin/default.aspx"
STABLECARD = PR + "2026/Western-Union-Launches-Stablecard-in-Partnership-with-Rain/default.aspx"
MC21 = PR + "2021/Western-Union-and-Mastercard-Expand-Global-Partnership/default.aspx"
VISA22 = PR + "2022/Western-Union-and-Visa-Bolster-Their-Global-Partnership/default.aspx"
VISA19 = PR + "2019/Visa-and-Western-Union-to-Bring-Speed-Simplicity-and-Transparency-to-Global-Payments/default.aspx"
WUBS = PR + "2021/Western-Union-Announces-Agreement-to-Sell-Western-Union-Business-Solutions-to-Goldfinch-Partners-and-The-Baupost-Group-for-Approximately-910-Million-in-Cash/default.aspx"
STC = PR + "2021/Western-Union-Expands-Global-Ecosystem-with-Completion-of-Investment-into-stc-Bank/default.aspx"
PUBLIX = PR + "2026/Western-Union-and-Publix-Extend-Relationship-to-Serve-Growing-Communities-Across-the-Southeast/default.aspx"
DPOST = PR + "2025/Western-Union-Partners-With-Deutsche-Post-Leader-in-the-German-Postal-Market/default.aspx"
CFO = PR + "2023/Western-Union-Appoints-Matthew-Cagwin-as-Chief-Financial-Officer/default.aspx"
OBAPI = PR + "2019/Western-Union-Delivers-Next-Evolution-of-Its-Open-Banking-API-for-Global-Payments/default.aspx"
LATAMWALLET = PR + "2022/Western-Union-Expands-its-Digital-Wallet-to-Latin-America/default.aspx"
THEBLOCK = "https://www.theblock.co/post/399890/western-union-launches-usdpt-stablecoin-anchorage-solana"
ANCHORAGE = "https://www.anchorage.com/insights/anchorage-digital-western-union-partner-launch-usdpt-federally-regulated-stablecoin-solana"
EUROCHANGE = "https://fxnewsgroup.com/forex-news/payments/corsair-closes-sale-of-eurochange-to-western-union/"
FXC = "https://www.fxcintel.com/research/analysis/western-union-q4-25-earnings"
PREPAIDVISA = "https://www.westernunion.com/us/en/prepaid/us-gpr-terms-and-conditions.html"
NETSPEND = "https://www.wunetspendprepaid.com/"
VIGO = "https://www.westernunion.com/us/en/wallet/terms-and-conditions.html"
REWARDS = "https://www.westernunion.com/us/en/rewards/home.html"
MOBILEWALLET = "https://www.westernunion.com/us/en/mobile-wallet.html"
MONEYORDER = "https://www.westernunion.com/us/en/money-order.html"
DIGIBANK = "https://www.westernunion.com/de/en/digitalbanking/german-account.html"
DIGIBANKEND = "https://www.fintechfutures.com/digital-banking/western-union-discontinues-european-digital-banking-service"
MCAP = "https://stockanalysis.com/stocks/wu/market-cap/"
DEADLINE = "https://www.paymentsdive.com/news/western-union-navigates-challenges/827976/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · licences · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $4.05 billion of revenue in 2025 and about $1 billion a quarter, licences in almost every US state and across Europe, about 360,000 active locations in more than 200 countries, the \"Beyond\" plan for $5 billion by 2028, and an Intermex deal still waiting for regulators.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "$4.05bn in 2025, shrinking.", "div": "grp", "rev": "grp", "products": [
            P("scale", "2025 results", "Revenue of $4,050.7 million in 2025, down 4% (down 2% adjusted, excluding Iraq); 285.9 million money transfers; GAAP operating margin 19%; GAAP EPS $1.52 and adjusted EPS $1.75; about $530 million returned to shareholders.",
              s=["send"], neo=[0, ""], src=[["Western Union: FY2025 results, Feb 2026", FY25]]),
            P("q2", "Q2 2026 and a cut outlook", "Revenue of $1,013.2 million in Q2 2026, down 1%; GAAP operating margin 13% (19% a year earlier); adjusted EPS $0.31. The 2026 outlook was cut to 3–5% revenue growth and adjusted EPS of $1.25–1.35, from $1.75–1.85 in February. Q3 results are due on 4 November 2026.",
              s=["send"], st="flux", neo=[0, ""], src=[["Western Union: Q2 2026 results, Jul 2026", Q2], ["Western Union: FY2025 results, Feb 2026", FY25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Licences & regulation", "blurb": "Every US state, PSD2, a bank.", "div": "grp", "rev": "grp", "products": [
            P("licences", "Licences", "Money-transmitter licences in almost every US state; Western Union Payment Services Ireland under PSD2; an Austrian bank (Western Union International Bank); an FCA payment institution in the UK; and a banking licence in Brazil.",
              s=["send", "ptnr"], neo=[0, ""], src=[["Western Union: 2025 Form 10-K", TENK]]),
            P("regulation", "Regulation and consent orders", "Western Union operates under consent orders and settlement agreements; since 1 January 2026 a 1% US excise tax applies to some cash-funded remittances; Iraq revenue fell from $115.3 million in 2024 to $15.8 million in 2025 after US action on Iraqi banks.",
              s=["send", "agent"], st="flux", neo=[0, ""], src=[["Western Union: 2025 Form 10-K", TENK], ["Western Union: FY2025 results, Feb 2026", FY25]]),
        ]},
        {"id": "1.3", "ic": "users-round", "name": "Ownership & leadership", "blurb": "NYSE, about $1.9bn.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Listing and leadership", "Listed on the NYSE (WU), worth about $1.92 billion at $6.17 a share on 16 October 2026 ⚠. CEO Devin McGranahan; CFO Matt Cagwin; COO Benjamin Hawksworth; Giovanni Angelini, President EMEA; Chief Legal Officer Benjamin Adams retires on 2 November 2026; independent chair Jeffrey Joerres. About 9,600 staff in more than 50 countries.",
              s=["send"], neo=[0, ""], src=[["Western Union: 2026 proxy", PROXY], ["SEC 8-K: CLO retirement, Jul 2026", CLO], ["StockAnalysis: market cap, Oct 2026", MCAP], ["Western Union: CFO appointment, Jan 2023", CFO]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy", "blurb": "Beyond: $5bn by 2028.", "div": "grp", "rev": "grp", "products": [
            P("beyond", "The \"Beyond\" strategy", "Set out at the November 2025 investor day: a digital-first, two-sided financial services network, with 2028 revenue of $4.8–5.3 billion and adjusted EPS of $2.15–2.45, double-digit growth in Consumer Services, and more stablecoin work. In July 2026 the company added faster cost cuts to a \"dual-track strategy\".",
              s=["send"], st="new", ay="Nov 2025", neo=[0, ""], src=[["Western Union: Investor Day, Nov 2025", BEYOND], ["Western Union: Q2 2026 results, Jul 2026", Q2]]),
        ]},
        {"id": "1.5", "ic": "briefcase", "name": "Deals", "blurb": "Intermex pending.", "div": "imx", "rev": "grp", "products": [
            P("intermex", "Intermex acquisition (pending)", "Agreed on 10 August 2025 for $16 a share in cash, about $500 million, with about $30 million of cost savings; Intermex serves about 6 million customers from Miami to more than 60 countries. New York approved it in August 2026, but California's regulator suspended its approval and the competition filing had to be redone on 2 October 2026. Either side can walk away after 10 November 2026 ⚠.", short="Intermex",
              s=["send", "agent"], st="flux", o="A", at="Intermex", neo=[None, "Intermex's card arrangements are not public."],
              mc="Card funding, push-to-card and fraud tools for a second US retail network once it closes.",
              src=[["Western Union: Intermex deal, Aug 2025", IMX], ["Western Union: Intermex update, Aug 2026", IMXUPD], ["SEC 8-K: HSR refiled, Oct 2026", HSR], ["Payments Dive: deadline", DEADLINE]]),
            P("eurochange", "Eurochange", "A UK travel-money chain bought from Corsair (completed 7 April 2025), with more than 230 stores; it drove Consumer Services growth in 2025 and early 2026.",
              s=["svc"], o="A", ay="Apr 2025", at="Corsair (seller)", div="euro", neo=[None, ""], src=[["FX News Group: Eurochange sale, Apr 2025", EUROCHANGE], ["Western Union: Q1 2026 results, Apr 2026", Q1]]),
            P("wubs", "Business Solutions (sold)", "Cross-border business payments, sold to Goldfinch Partners and The Baupost Group for about $910 million (agreed August 2021, completed 1 July 2023). It carried Mastercard Cross-Border Services payouts from 2021.",
              s=["ptnr"], st="retired", neo=[1, "Carried Mastercard Cross-Border Services payouts until the sale."],
              src=[["Western Union: Business Solutions sale, Aug 2021", WUBS], ["Western Union and Mastercard, Nov 2021", MC21], ["Western Union: 2025 Form 10-K", TENK]]),
            P("stcbank", "stc bank stake", "An investment in stc pay (November 2020), completed into stc bank, a Gulf digital bank, in October 2021.",
              s=["ptnr"], o="P", at="stc bank", neo=[0, ""], src=[["Western Union: stc bank, Oct 2021", STC]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: cash at about 360,000 agent locations, transfers from the app and website, payouts to Mastercard and Visa cards, payouts to bank accounts and mobile wallets, the USDPT stablecoin on Solana, and Western Union's own cards and wallets, most of them on Visa.",
    "tiles": [
        {"id": "2.1", "ic": "store", "name": "Retail money transfer", "blurb": "Cash, about 360,000 locations.", "div": "wu", "rev": "retail", "products": [
            P("retail", "Retail money transfer", "Cash-to-cash and cash-to-account transfers at agents and Western Union stores; about 360,000 locations did business in the last 12 months, 90% outside the US. Americas retail is shrinking: North America revenue fell 9% in Q2 2026.",
              s=["send", "recv", "agent"], lc="move", neo=[0, "Cash."], src=[["Western Union: 2025 Form 10-K", TENK], ["Western Union: Q2 2026 results, Jul 2026", Q2]]),
        ]},
        {"id": "2.2", "ic": "smartphone", "name": "Digital money transfer", "blurb": "43% of transfers.", "div": "wu", "rev": "digital", "products": [
            P("digital", "Branded Digital", "Transfers through westernunion.com, the app and partner sites under the Western Union brand: 32% of money-transfer revenue and 43% of transactions in Q2 2026, with transactions up 25% and revenue up 7%; branded digital customers grew 25% in 2025.",
              s=["send"], lc="move", neo=[1, "Funded by cards on both networks and by bank accounts."], src=[["Western Union: Q2 2026 results, Jul 2026", Q2], ["Western Union: 2026 proxy", PROXY]]),
            P("cardfund", "Card-funded transfers", "Senders pay online with Visa or Mastercard credit and debit cards or from a bank account; the share by network is not published.", short="Card funding",
              s=["send"], lc="move", neo=[1, "Both networks."], mc="Tokens, authorisation tools and BIN data for every card-funded send.",
              src=[["Western Union: 2025 Form 10-K", TENK]]),
        ]},
        {"id": "2.3", "ic": "send", "name": "Pay to card", "blurb": "Mastercard Send, Visa Direct.", "div": "wu", "rev": "digital", "products": [
            P("mcsend", "Pay to card on Mastercard Send", "Since November 2021: US receivers can redirect a domestic transfer to any US debit card, and senders in 16 European countries can pay to Mastercard debit cards in eight receive countries, near real time.", short="Mastercard Send",
              s=["recv", "send"], lc="move", ay="Nov 2021", o="P", at="Mastercard", neo=[3, "Mastercard Send."],
              mc="No update since 2021 is public; Mastercard Move could widen it to wallets and more corridors.",
              src=[["Western Union and Mastercard, Nov 2021", MC21]]),
            P("visadirect", "Pay to card on Visa Direct", "A Visa Direct agreement in June 2019, live first in more than 20 European countries and extended in August 2022 to US senders paying Visa debit cards in Colombia, El Salvador, Jamaica, the Philippines, Romania and Thailand.", short="Visa Direct",
              s=["recv", "send"], lc="move", ay="Jun 2019", o="P", at="Visa", neo=[0, "Visa."], src=[["Western Union and Visa, Jun 2019", VISA19], ["Western Union and Visa, Aug 2022", VISA22]]),
        ]},
        {"id": "2.4", "ic": "arrow-left-right", "name": "Account & wallet payout", "blurb": "Banks and mobile wallets.", "div": "wu", "rev": "digital", "products": [
            P("a2a", "Bank account and mobile-wallet payout", "Payouts to billions of bank accounts and millions of mobile wallets, through partners such as Bharti Airtel, Thunes and Coins.ph. Newer Middle East partnerships are mostly account-to-account, which pushed transactions in the region up 44% in Q2 2026 ⚠.",
              s=["recv", "ptnr"], lc="move", neo=[0, "Account-to-account and wallets."], src=[["Western Union: send to a mobile wallet", MOBILEWALLET], ["Western Union: Q2 2026 results, Jul 2026", Q2], ["FXC Intelligence: Q4 2025, Feb 2026", FXC]]),
        ]},
        {"id": "2.5", "ic": "coins", "name": "USDPT stablecoin", "blurb": "Live on Solana since May 2026.", "div": "stable", "rev": "assets", "products": [
            P("usdpt", "USDPT", "A US dollar stablecoin on Solana, issued by Anchorage Digital Bank. Announced in October 2025 and launched on 4 May 2026 for treasury and around-the-clock agent settlement, starting in the Philippines and Bolivia ⚠, with Fireblocks infrastructure ⚠. McGranahan: it \"will allow us to own the economics linked to stablecoins\".",
              s=["crypto", "agent"], lc="move", st="new", ay="May 2026", o="P", at="Anchorage Digital, Solana", neo=[0, "On Solana, off the card networks."],
              mc="Western Union's own coin; card spend on it went to Visa.",
              src=[["Western Union: USDPT announced, Oct 2025", USDPT25], ["Western Union: USDPT launched, May 2026", USDPT26], ["The Block: USDPT launch, May 2026", THEBLOCK], ["Anchorage Digital: USDPT", ANCHORAGE]]),
            P("dan", "Digital Asset Network", "Connects licensed exchanges, wallets and custodians to Western Union's payout network, so people can turn digital assets into cash. Announced in October 2025.",
              s=["crypto", "ptnr"], lc="move", st="new", ay="Oct 2025", neo=[0, "Off the card networks."], src=[["Western Union: USDPT announced, Oct 2025", USDPT25], ["Western Union: USDPT launched, May 2026", USDPT26]]),
        ]},
        {"id": "2.6", "ic": "credit-card", "name": "Cards & wallets", "blurb": "Mostly Visa.", "div": "wu", "rev": "cs", "products": [
            P("stablecard", "Stablecard by Western Union", "A wallet and Visa secured credit card that holds USDPT, built with Rain: live in 37 markets on 4 August 2026, aiming for more than 60 by the end of the year, with Apple Pay and Google Pay.", short="Stablecard",
              s=["crypto", "recv"], lc="move", st="new", ay="Aug 2026", o="P", at="Rain, Visa", div="stable", neo=[0, "Visa."],
              mc="The consumer face of the stablecoin went to Visa.",
              src=[["Western Union: Stablecard, Aug 2026", STABLECARD]]),
            P("prepaidvisa", "Western Union Prepaid Visa Card", "A US reloadable prepaid card issued by Pathward (terms dated 28 May 2026).",
              s=["recv", "svc"], lc="everyday", o="P", at="Pathward, Visa", neo=[0, "Visa."], src=[["Western Union: Prepaid Visa terms", PREPAIDVISA]]),
            P("netspend", "Western Union Netspend Prepaid Mastercard", "A US reloadable card with Netspend: receive Western Union transfers, direct deposit and mobile cheque loading.", short="Netspend Prepaid Mastercard",
              s=["recv", "svc"], lc="everyday", o="P", at="Netspend, Mastercard", neo=[2, "Rides wholly on Mastercard."], src=[["Western Union Netspend Prepaid Mastercard", NETSPEND]]),
            P("vigo", "Vigo Money and other wallets", "Vigo Money, a US wallet with a Pathward card (network not published ⚠; more than 30,000 users by February 2026 ⚠), and wallets in Brazil (May 2025), Argentina, Singapore, the Philippines and Israel, with Australia and Mexico planned ⚠.", short="Wallets",
              s=["recv", "send"], lc="everyday", st="new", div="vigo", neo=[None, "Card network not published."],
              mc="Wallets need a card and a payout rail; Mastercard is not named on any of them.",
              src=[["Western Union: Vigo Money terms", VIGO], ["FXC Intelligence: Q4 2025, Feb 2026", FXC], ["Western Union: wallet in Latin America, Sep 2022", LATAMWALLET]]),
            P("digibank", "Digital Banking in Europe (closed)", "An account with a Visa Platinum debit card from the Austrian bank, launched in 2022 in Germany, Poland, Romania and Italy; later closed ⚠ (date not confirmed).",
              s=["recv"], lc="everyday", st="retired", div="wuib", neo=[0, "Visa."], src=[["Western Union: Digital Banking, Germany", DIGIBANK], ["FinTech Futures: service discontinued", DIGIBANKEND]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every transfer: compliance and fraud controls under consent orders, identity checks for digital customers, treasury and agent settlement (now partly in USDPT), Western Union Rewards and a media network, and the platform that banks and wallets plug into.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Compliance & fraud", "blurb": "Consent orders, AI monitoring.", "div": "grp", "rev": "grp", "products": [
            P("compliance", "Compliance and consumer fraud", "Anti-money-laundering, sanctions and consumer-fraud controls across agents and digital, under consent orders and settlement agreements; AI is used in transaction monitoring and fraud detection. No Mastercard fraud tool is named.",
              s=["send", "agent"], lc="everyday", neo=[0, "Own controls."], mc="Scam and fraud scoring for card-funded sends and payouts.",
              src=[["Western Union: 2025 Form 10-K", TENK]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Identity", "blurb": "KYC for digital and wallets.", "div": "wu", "rev": "digital", "products": [
            P("kyc", "Identity verification", "Identity checks for digital sending, wallets and Stablecard; AI is used in identity verification. Providers are not disclosed ⚠.",
              s=["send", "crypto"], lc="open", neo=[None, ""], src=[["Western Union: 2025 Form 10-K", TENK]]),
        ]},
        {"id": "3.3", "ic": "database", "name": "Treasury & settlement", "blurb": "24/7 agent settlement in USDPT.", "div": "grp", "rev": "grp", "products": [
            P("treasury", "Treasury and agent settlement", "Settlement with agents in nearly 130 currencies; since May 2026 USDPT allows near-instant 24/7 settlement with agents. $1.4 billion of investment securities at the end of 2025, and a Bank of America-led loan for Intermex.",
              s=["agent"], lc="move", st="new", neo=[0, ""], src=[["Western Union: USDPT launched, May 2026", USDPT26], ["Western Union: 2025 Form 10-K", TENK]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards & media", "blurb": "Points on every send.", "div": "wu", "rev": "digital", "products": [
            P("rewards", "Western Union Rewards", "A loyalty programme: 100 points on every send and 250 for completing a profile, with shop deals from partners.",
              s=["send"], lc="grow", neo=[0, ""], mc="Card-linked offers could add to the shop deals.", src=[["Western Union: Rewards", REWARDS]]),
            P("media", "Media network", "Advertising across Western Union's stores, website and app, reported within Consumer Services.",
              s=["agent"], lc="grow", neo=[0, ""], src=[["Western Union: 2025 Form 10-K", TENK]]),
        ]},
        {"id": "3.5", "ic": "code-xml", "name": "Partner platform", "blurb": "Banks and wallets embed it.", "div": "wu", "rev": "retail", "products": [
            P("api", "Platform and APIs for partners", "An open-banking API for global payments (October 2019) and a platform that banks, postal networks and wallets use to offer Western Union transfers under their own names.",
              s=["ptnr"], lc="open", o="B", neo=[0, ""], src=[["Western Union: open banking API, Oct 2019", OBAPI]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What Western Union sells: cross-border money transfer (about 87% of revenue in 2025), and Consumer Services — bill payment, travel money, money orders, prepaid cards and insurance — growing fast, plus a new digital-asset line.",
    "tiles": [
        {"id": "4.1", "ic": "globe", "name": "Money transfer", "blurb": "$3.5bn, 286m transfers.", "div": "wu", "rev": "retail", "products": [
            P("cmt", "Consumer Money Transfer", "$3,507.4 million of revenue in 2025 (down 8%) from 285.9 million transfers; by region, North America 36%, Europe and CIS 30%, Middle East, Africa and South Asia 18%, Latin America 11% and Asia-Pacific 5% of revenue in Q2 2026.",
              s=["send", "recv"], lc="move", neo=[1, "Pay to card on both networks; mostly cash and accounts."], src=[["Western Union: FY2025 results, Feb 2026", FY25], ["Western Union: Q2 2026 results, Jul 2026", Q2]]),
        ]},
        {"id": "4.2", "ic": "receipt-text", "name": "Bill payment", "blurb": "US and Argentina.", "div": "wu", "rev": "cs", "products": [
            P("billpay", "Bill payment", "Walk-in and online bill payment in the US and Argentina; a main driver of Consumer Services, whose revenue grew 32% in 2025 to $543.3 million.",
              s=["svc"], lc="everyday", neo=[0, ""], src=[["Western Union: FY2025 results, Feb 2026", FY25], ["Western Union: 2025 Form 10-K", TENK]]),
        ]},
        {"id": "4.3", "ic": "plane", "name": "Travel money", "blurb": "Eurochange.", "div": "euro", "rev": "cs", "products": [
            P("travel", "Travel money", "Retail foreign exchange, led by Eurochange in the UK; with bill payment it lifted Consumer Services revenue 24% in Q1 2026.",
              s=["svc"], lc="everyday", neo=[None, ""], src=[["Western Union: Q1 2026 results, Apr 2026", Q1]]),
        ]},
        {"id": "4.4", "ic": "wallet", "name": "Money orders & insurance", "blurb": "No bank account needed.", "div": "wu", "rev": "cs", "products": [
            P("moneyorder", "Money orders", "US money orders sold at agents such as Publix, for people without a bank account.",
              s=["svc"], lc="everyday", neo=[0, ""], src=[["Western Union: money orders", MONEYORDER], ["Western Union and Publix, Oct 2026", PUBLIX]]),
            P("insurance", "Lending and insurance partnerships", "Partnerships for lending and insurance (AXA, 2020), reported in Consumer Services.",
              s=["svc"], lc="borrow", o="P", neo=[0, ""], src=[["Western Union: 2025 Form 10-K", TENK]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Digital assets", "blurb": "Bybit, exchanges.", "div": "stable", "rev": "assets", "products": [
            P("bybit", "Exchange partners", "Bybit became the first major exchange in the USDPT network (4 June 2026): users in Latin America buy and sell USDPT for local money; Western Union's Head of Digital Assets is Malcolm Clarke.",
              s=["crypto", "ptnr"], lc="beyond", st="new", ay="Jun 2026", o="P", at="Bybit", neo=[0, "Off the card networks."], src=[["Western Union and Bybit, Jun 2026", BYBIT]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How people reach Western Union: agents such as Publix and Deutsche Post, its own stores, westernunion.com and the app, and the banks, wallets and exchanges that embed it.",
    "tiles": [
        {"id": "5.1", "ic": "building-2", "name": "Retail network", "blurb": "Agents and own stores.", "div": "wu", "rev": "retail", "products": [
            P("agents", "Agents", "Its top 40 agents average more than 20 years with Western Union and bring about half of money-transfer revenue. Publix renewed in October 2026; Deutsche Post began in Q2 2026 in most of its 12,600 German branches.",
              s=["agent", "send"], lc="open", o="P", neo=[0, ""], src=[["Western Union: 2025 Form 10-K", TENK], ["Western Union and Publix, Oct 2026", PUBLIX], ["Western Union and Deutsche Post, Dec 2025", DPOST]]),
            P("owned", "Western Union stores", "Western Union expanded its own stores in 2025, which raised fixed costs when US retail volumes fell in 2026.",
              s=["send"], lc="open", st="flux", neo=[0, ""], src=[["Western Union: Q1 2026 results, Apr 2026", Q1], ["Western Union: FY2025 results, Feb 2026", FY25]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "App & web", "blurb": "westernunion.com, Stablecard app.", "div": "wu", "rev": "digital", "products": [
            P("app", "Website and apps", "westernunion.com and the Western Union app, Vigo Money and the Stablecard app; new digital customers grew 20% in 2025.",
              s=["send", "crypto"], lc="open", neo=[1, "Takes cards on both networks."], src=[["Western Union: 2026 proxy", PROXY], ["Western Union: Stablecard, Aug 2026", STABLECARD]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Partners", "blurb": "Banks, wallets, exchanges.", "div": "wu", "rev": "grp", "products": [
            P("banks", "Bank, wallet and exchange partners", "Banks, postal networks and wallets that offer Western Union transfers in their own channels, and exchanges such as Bybit on the Digital Asset Network.",
              s=["ptnr"], lc="open", o="P", neo=[0, ""], src=[["Western Union: open banking API, Oct 2019", OBAPI], ["Western Union and Bybit, Jun 2026", BYBIT]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Western Union", "blurb": "Send, Netspend, acceptance.", "products": [
        P("mcatwu", "Mastercard at Western Union", "Mastercard is in through Mastercard Send push-to-card (since November 2021), the Western Union Netspend Prepaid Mastercard, and acceptance of Mastercard cards for card-funded sends. Visa has the newer public wins: Visa Direct (2019 and 2022), the Prepaid Visa Card, the European debit card and Stablecard, the card for the USDPT stablecoin.",
          s=["send"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Western Union and Mastercard, Nov 2021", MC21], ["Western Union: Stablecard, Aug 2026", STABLECARD]]),
    ]},
    {"id": "pillar-market", "name": "Remittances", "blurb": "Digital rivals, stablecoins.", "products": [
        P("market", "The market", "Western Union is still the largest remitter by revenue, but its revenue has fallen since 2021 while digital rivals such as Remitly ($74.9 billion sent in 2025, revenue up 29%) and Wise grow; MoneyGram took Mastercard Move in 2025 ⚠; stablecoins and a US remittance tax change the costs.",
          s=["send"], div="grp", rev="grp", src=[["FinTech Futures: Remitly FY2025", "https://www.fintechfutures.com/press-releases/remitly-reports-fourth-quarter-and-full-year-2025-results-above-outlook"], ["Mastercard: MoneyGram and Move, Apr 2025", "https://www.mastercard.com/us/en/news-and-trends/press/2025/april/moneygram-and-mastercard-collaborate-to-advance-digital-money-movement.html"]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
