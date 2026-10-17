"""JPMorgan Chase's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the firm's own unless a source says otherwise: the 3Q26 results (13 October 2026), the 2025
Form 10-K (13 February 2026) and the 2026 Company Update (23 February 2026). ``neo`` is the Mastercard
lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

SEC = "https://www.sec.gov/Archives/edgar/data/19617/"
Q3 = "https://www.sec.gov/Archives/edgar/data/0000019617/000162828026065582/a3q26erfexhibit991narrative.htm"
Q3S = SEC + "000162828026065582/a3q26erfex992supplement.htm"
Q3P = SEC + "000162828026065616/a3q26_earningsxpresentat.htm"
Q4S = SEC + "000162828026001902/a4q25erfex992supplement.htm"
K25 = SEC + "000162828026008131/jpm-20251231.htm"
UPD = SEC + "000162828026010693/firmoverview.htm"
COPRES = SEC + "000001961726000241/jpm-20260624.htm"
LETTER = "https://www.jpmorganchase.com/ir/annual-report/2025/ar-ceo-letters"
HIST = "https://www.jpmorganchase.com/about/our-history"
MEDIA = "https://media.chase.com/news/"
APPLE = "https://www.jpmorganchase.com/newsroom/press-releases/2026/chase-to-become-new-issuer-of-apple-card"
SAPPHIRE = MEDIA + "the-most-rewarding-cards-are-here"
BRANCHES = MEDIA + "chase-to-open-more-than-160-branches-in-over-30-states-in-2026"
GERMANY = MEDIA + "chase-launches-in-germany-with-top-rate-savings-account"
IHG = MEDIA + "ihg-premier-select-card-portfolio-updates"
FRAUD = MEDIA + "jpmc-announces-largest-financial-fraud-and-scam-prevention-effort-in-firms-history"
MCCARDS = "https://creditcards.chase.com/mastercard-credit-cards"
FLEX = "https://creditcards.chase.com/cash-back-credit-cards/freedom/flex"
VISA13 = "https://investor.visa.com/news/news-details/2013/Visa-Inc-and-JPMorgan-Chase-Sign-Letter-of-Intent-for-New-and-Expanded-Partnership-Agreement/default.aspx"
JPMD = "https://www.jpmorgan.com/payments/newsroom/jpm-coin-usd-deposit-token-institutional-clients"
KINEXYS = "https://www.jpmorgan.com/kinexys/index"
MTN = "https://paymentsindustryintelligence.com/mastercard-and-jpmorgan-revolutionise-cross-border-payments-with-blockchain/"
COMMCARDS = "https://www.jpmorgan.com/payments/solutions/commercial-cards"
MIRAKL = "https://www.mirakl.com/news/mirakl-and-j-p-morgan-payments-to-power-agentic-commerce-at-enterprise-scale"
PLAID = "https://news.bloomberglaw.com/banking-law/jpmorgan-plaid-data-fee-deal-shifts-open-banking-battlefield"
LLM = "https://connect.cefpro.com/article/view/inside-jpmorgan-llm-suite-as-ai-agents-spread-across-the-bank"
NILSON = "https://nilsonreport.com/articles/j-p-morgans-merchant-acquiring-global-expansion/"
NILSONISS = "https://markets.financialcontent.com/stocks/article/gnwcq-2025-3-6-jp-morgan-tops-nilson-report-ranking-of-us-credit-card-issuers"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "fortress balance sheet · charters · technology", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a $5.1 trillion fortress balance sheet earning 20% on tangible equity, banks in the US, UK and Germany, two centuries of predecessors, a $19.8 billion technology budget, and a $1.5 trillion bet on American security and resilience.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Fortress balance sheet", "blurb": "$5.1 trillion, ROTCE 20%.", "div": "jpmc", "rev": "corp", "products": [
            P("balance", "Balance sheet", "Total assets of $5.09 trillion, deposits of $2.78 trillion and loans of $1.58 trillion at 30 September 2026; $1.5 trillion of cash and marketable securities; 94 million customers.",
              s=["inst"], neo=[0, ""], src=[["3Q26 results", Q3], ["3Q26 supplement", Q3S]]),
            P("earnings", "Earnings & capital", "Managed revenue of $185.6 billion and net income of $57.0 billion in 2025; 3Q26 net income $15.3 billion on $50.9 billion of revenue (ROTCE 20%); CET1 13.9%; market value about $879 billion; parent rated A1, A and AA-.",
              s=["inst"], neo=[0, ""], src=[["3Q26 results", Q3], ["4Q25 supplement", Q4S], ["2025 Form 10-K", K25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Entities & leadership", "blurb": "Dimon and two co-presidents.", "div": "jpmc", "rev": "corp", "products": [
            P("entities", "Legal entities", "JPMorgan Chase Bank, N.A.; J.P. Morgan Securities; J.P. Morgan SE in Germany (which also runs Chase Germany); J.P. Morgan Europe Ltd for Chase UK.",
              s=["inst"], neo=[0, ""], src=[["2025 Form 10-K", K25]]),
            P("leadership", "Leadership & succession", "Chairman and CEO Jamie Dimon; co-presidents Doug Petno (CIB) and Troy Rohrbaugh (CCB) since June 2026, with Marianne Lake retiring; Mary Erdoes (AWM), Jennifer Piepszak (COO), Jeremy Barnum (CFO); Allison Beer runs Card & Connected Commerce.",
              s=["inst"], neo=[0, ""], src=[["8-K: co-presidents, Jun 2026", COPRES], ["2025 Form 10-K", K25]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "Manhattan Co., 1799.", "div": "jpmc", "rev": "corp", "products": [
            P("heritage", "Heritage", "The Manhattan Company (1799), Drexel, Morgan & Co. (1871) and Chase Manhattan (1955), merged in 2000; Bank One, Bear Stearns and Washington Mutual followed ⚠, and First Republic in 2023.",
              s=["inst"], o="I", neo=[0, ""], src=[["JPMorganChase: our history", HIST], ["2025 Form 10-K", K25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "$19.8 billion a year.", "div": "jpmc", "rev": "corp", "products": [
            P("tech", "Technology & LLM Suite", "About $19.8 billion on technology in 2026; 80% of applications on modern infrastructure; LLM Suite on OpenAI and Anthropic models, refreshed every eight weeks, used weekly by about 150,000 employees.",
              s=["inst"], neo=[0, ""], src=[["2026 Company Update", UPD], ["CeFPro: LLM Suite", LLM]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy", "blurb": "Complete, global, diversified.", "div": "jpmc", "rev": "corp", "products": [
            P("strategy", "Targets & the Security and Resiliency Initiative", "A through-the-cycle ROTCE of 17%; targets of 20% of US card outstandings (17.5% in 2025) and 15% of retail deposits (11.1%); a $1.5 trillion, ten-year Security and Resiliency Initiative with $10 billion of direct investment.",
              s=["inst"], neo=[0, ""], src=[["2026 Company Update", UPD], ["Shareholder letter, Apr 2026", LETTER]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: J.P. Morgan Payments ($12 trillion a day), Merchant Services, America's largest credit-card book (mostly Visa, with eight Mastercards and Apple Card on the way), Visa debit, Zelle and RTP, Kinexys and JPMD on chain, and commercial cards on both networks.",
    "tiles": [
        {"id": "2.1", "ic": "arrow-left-right", "name": "J.P. Morgan Payments", "blurb": "$12 trillion a day.", "div": "pay", "rev": "cib", "products": [
            P("treasury", "Treasury & payments", "Nearly $12 trillion a day in 120-plus currencies and 160 countries, first in US dollar payments; payments revenue of $19.3 billion in 2025 and $5.6 billion in 3Q26 (+14%).",
              s=["corp", "inst"], lc="move", neo=[0, ""], src=[["Shareholder letter, Apr 2026", LETTER], ["3Q26 supplement", Q3S]]),
        ]},
        {"id": "2.2", "ic": "store", "name": "Merchant Services", "blurb": "Largest US acquirer by transactions.", "div": "pay", "rev": "cib", "products": [
            P("acquiring", "Merchant acquiring", "The largest US acquirer by transactions in 2024 (41 billion), heritage Paymentech and WePay, with the ChaseNet link into Visa agreed in 2013.",
              s=["merch"], lc="move", neo=[1, "Accepts every network."], src=[["Nilson: J.P. Morgan acquiring", NILSON], ["Visa and JPMorgan Chase, Feb 2013", VISA13]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Chase credit cards", "blurb": "$1.35 trillion of spend.", "div": "chase", "rev": "ccb", "products": [
            P("visacards", "Sapphire, Freedom, Ink & co-brands (Visa)", "Thirty-five Visa cards: Sapphire Reserve ($795, refreshed 2025), Sapphire Preferred, Freedom Unlimited, Ink, United (to 2029), Southwest, Marriott, Hyatt, Disney and Prime Visa.", short="Visa cards",
              s=["con", "aff", "sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Chase: Sapphire Reserve, Jun 2025", SAPPHIRE], ["Visa and JPMorgan Chase, Feb 2013", VISA13]]),
            P("mccards", "Freedom Flex, IHG, Aeroplan, DoorDash & Instacart (Mastercard)", "Eight Mastercards: Freedom Flex (World Elite, 2020; foreign fees dropped September 2026), four IHG cards (range overhauled 1 October 2026), Aeroplan, DoorDash and Instacart.", short="Mastercard cards",
              s=["con", "aff"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["Chase: Mastercard credit cards", MCCARDS], ["Chase: Freedom Flex", FLEX], ["Chase: IHG cards, Oct 2026", IHG]]),
            P("applecard", "Apple Card (from about 2028)", "Chase will replace Goldman Sachs as Apple Card's issuer (announced 7 January 2026): more than $20 billion of balances, about 24 months to move, Mastercard staying the network; a $2.2 billion reserve in 4Q25.", short="Apple Card",
              s=["con"], lc="everyday", st="new", ay="Jan 2026", o="P", at="Apple, Mastercard", neo=[2, "Mastercard."],
              mc="Will probably become Chase's largest Mastercard book by far, and needs tokens, fraud, disputes and benefits at Apple's standard.",
              src=[["JPMorganChase: Chase to issue Apple Card, Jan 2026", APPLE]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Debit", "blurb": "Visa.", "div": "chase", "rev": "ccb", "products": [
            P("debit", "Chase debit", "Debit cards for 87 million consumers and 7.5 million small businesses ⚠ on Visa; debit and credit sales of $1.94 trillion in 2025.",
              s=["con", "sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa ⚠."], src=[["4Q25 supplement", Q4S]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Zelle & real-time", "blurb": "Account-to-account.", "div": "chase", "rev": "ccb", "products": [
            P("zelle", "Zelle, RTP & Paze", "Zelle since 2017 and record RTP volumes in 2025; JPMorgan co-owns Early Warning (Zelle, Paze) and The Clearing House (RTP) ⚠.",
              s=["con", "sme", "corp"], lc="move", neo=[0, "Off the card networks."], src=[["2026 Company Update", UPD]]),
        ]},
        {"id": "2.6", "ic": "network", "name": "Kinexys & JPMD", "blurb": "$7 billion a day on chain.", "div": "kinexys", "rev": "cib", "products": [
            P("kinexys", "Kinexys", "Blockchain deposit accounts, programmable payments and on-chain FX: more than $7 billion a day and $3 trillion in all; linked to Mastercard's Multi-Token Network for B2B cross-border settlement (November 2024).",
              s=["corp", "inst"], lc="move", o="B", neo=[1, "Connected to Mastercard's Multi-Token Network."],
              src=[["Kinexys", KINEXYS], ["Payments Industry Intelligence: Mastercard and Kinexys, Dec 2024", MTN]]),
            P("jpmd", "JPM Coin (JPMD)", "A US-dollar deposit token live on Base for institutions (12 November 2025), with Mastercard among the proof-of-concept participants and planning to add JPMD to its token network.",
              s=["inst"], lc="move", st="new", ay="Nov 2025", neo=[1, "Mastercard Token Network planned."],
              src=[["J.P. Morgan: JPMD live, Nov 2025", JPMD]]),
        ]},
        {"id": "2.7", "ic": "briefcase", "name": "Commercial cards", "blurb": "First in the US.", "div": "pay", "rev": "cib", "products": [
            P("commcards", "Commercial cards", "One Card, travel, purchasing and virtual cards; J.P. Morgan calls itself the largest US commercial card issuer on both Visa and Mastercard.",
              s=["corp"], lc="move", neo=[1, "Both networks; split not disclosed."],
              mc="Room to win share in virtual cards and accounts payable.",
              src=[["J.P. Morgan: commercial cards", COMMCARDS]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account and payment: $12 billion of fraud stopped a year, AI for 250,000 people, fees for the aggregators that pull customer data, Ultimate Rewards and Sapphire lounges, Chase Offers, and agentic checkout with Mirakl.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & scams", "blurb": "$12 billion stopped.", "div": "chase", "rev": "ccb", "products": [
            P("fraud", "Fraud & scam prevention", "$12 billion of fraud and scam losses prevented in 2024; the firm's largest anti-scam effort (November 2025) with warnings, trusted contacts and a scam-interruption team; AI fraud advice in 700 branches (October 2026).",
              s=["con", "sme"], lc="everyday", neo=[0, "Chase's own."], src=[["Chase: fraud and scam prevention, Nov 2025", FRAUD]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "AI", "blurb": "LLM Suite for 250,000.", "div": "jpmc", "rev": "corp", "products": [
            P("llmsuite", "LLM Suite & AI in production", "Access for about 250,000 employees, about half using it daily; AI solutions in production doubled in 2025; a quarter of technology growth goes to AI.",
              s=["inst"], lc="beyond", neo=[0, ""], src=[["CeFPro: LLM Suite", LLM], ["2026 Company Update", UPD]]),
        ]},
        {"id": "3.3", "ic": "database", "name": "Data access", "blurb": "Aggregators now pay.", "div": "chase", "rev": "ccb", "products": [
            P("dataaccess", "Data-access agreements", "Chase began charging aggregators for customer data in 2025; Plaid agreed in September 2025, and contracts now cover more than 95% of pulls; the CFPB's open-banking rule is being rewritten.",
              s=["con", "merch"], lc="beyond", st="new", neo=[None, "Finicity's status not public."],
              mc="Finicity needs a commercial agreement with Chase; whether it has one is not public.",
              src=[["Bloomberg Law: JPMorgan and Plaid, Sep 2025", PLAID]]),
        ]},
        {"id": "3.4", "ic": "plane", "name": "Rewards & travel", "blurb": "Ultimate Rewards, lounges.", "div": "chase", "rev": "ccb", "products": [
            P("rewards", "Ultimate Rewards, Chase Travel & Sapphire Lounges", "Points Boost, Chase Travel and The Edit's 1,100 hotels, and Sapphire Lounges (Dallas Fort Worth opened July 2026, with Las Vegas and Los Angeles announced).",
              s=["aff"], lc="grow", neo=[0, "Chase's own."], src=[["Chase: Sapphire Reserve, Jun 2025", SAPPHIRE], ["Chase media centre", MEDIA]]),
        ]},
        {"id": "3.5", "ic": "gift", "name": "Offers & media", "blurb": "Chase Offers.", "div": "chase", "rev": "ccb", "products": [
            P("offers", "Chase Offers & Chase Media Solutions", "Card-linked merchant statement credits since 2018, and a retail-media network on Chase spend data ⚠.",
              s=["con", "merch"], lc="grow", neo=[0, "Chase's own."],
              mc="World Elite benefits and merchant-funded offers on the Mastercard cards.",
              src=[["Chase media centre", MEDIA]]),
        ]},
        {"id": "3.6", "ic": "bot", "name": "Agentic commerce", "blurb": "Mirakl.", "div": "pay", "rev": "cib", "products": [
            P("agentic", "Agentic checkout", "A global agreement with Mirakl (March 2026) for agentic checkout for merchants, network-agnostic; no Chase tie-up with Mastercard Agent Pay or Visa Intelligent Commerce on record.",
              s=["merch", "con"], lc="move", st="new", neo=[0, "Nothing announced."],
              mc="Agent Pay for Chase-issued Mastercards and through J.P. Morgan Payments.",
              src=[["Mirakl and J.P. Morgan Payments, Mar 2026", MIRAKL]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Three segments opened out into what customers buy: Chase's banking, wealth, home and auto, and business banking; J.P. Morgan's investment banking, markets and commercial banking; asset and wealth management; and Chase abroad.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Banking & wealth", "blurb": "$1.08 trillion of deposits.", "div": "chase", "rev": "ccb", "products": [
            P("checking", "Checking & savings", "First in US retail deposits (11.1%): $1.08 trillion of average deposits, 1.7 million net new checking accounts in 2025.",
              s=["con"], lc="everyday", neo=[0, "Visa debit."], src=[["3Q26 supplement", Q3S], ["2026 Company Update", UPD]]),
            P("jpmwm", "J.P. Morgan Wealth Management", "$1.42 trillion of client investment assets with 6,433 advisors and self-directed investing.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["3Q26 supplement", Q3S]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Home & auto", "blurb": "Mortgages and car loans.", "div": "chase", "rev": "ccb", "products": [
            P("homeauto", "Home Lending & Chase Auto", "$46.9 billion of mortgages originated in nine months of 2026 and $652 billion serviced; $10.8 billion of auto loans in 3Q26.",
              s=["home", "con"], lc="borrow", neo=[0, ""], src=[["3Q26 supplement", Q3S]]),
        ]},
        {"id": "4.3", "ic": "store", "name": "Business banking", "blurb": "First for small businesses.", "div": "chase", "rev": "ccb", "products": [
            P("business", "Chase Business Banking", "The primary bank for more small businesses than any other: 7.5 million of them, with Ink cards and Merchant Services.",
              s=["sme"], lc="everyday", neo=[0, "Visa debit and Ink."], src=[["2026 Company Update", UPD]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Investment banking & markets", "blurb": "First in fees and markets.", "div": "cib", "rev": "cib", "products": [
            P("ibmarkets", "Investment Banking & Markets", "First globally in investment-banking fees (9.2% share in 2026) and markets (11.8% in 2025); $44.1 trillion under custody.",
              s=["corp", "inst"], lc="grow", neo=[0, ""], src=[["3Q26 results", Q3], ["2026 Company Update", UPD]]),
        ]},
        {"id": "4.5", "ic": "building-2", "name": "Commercial & corporate banking", "blurb": "Middle market to multinationals.", "div": "cib", "rev": "cib", "products": [
            P("commercial", "Commercial & Global Corporate Banking", "Middle-market and real-estate banking ($11.9 billion of revenue in 2025) and corporate banking for 8,000 clients in 40 countries.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["2025 Form 10-K", K25], ["2026 Company Update", UPD]]),
        ]},
        {"id": "4.6", "ic": "gem", "name": "Asset & Wealth Management", "blurb": "$5.2 trillion managed.", "div": "awm", "rev": "awm", "products": [
            P("awm", "Asset Management & Private Bank", "$5.21 trillion under management, first in active ETFs, 22 years of positive flows, and the Global Private Bank.",
              s=["aff", "inst"], lc="grow", neo=[0, ""], src=[["3Q26 presentation", Q3P], ["2026 Company Update", UPD]]),
        ]},
        {"id": "4.7", "ic": "flag", "name": "Chase abroad", "blurb": "UK and Germany.", "div": "chase", "rev": "corp", "products": [
            P("intl", "Chase UK & Chase Germany", "App-only banks: Chase UK (2021, more than 3 million customers) and Chase Germany (20 May 2026), with J.P. Morgan Personal Investing (formerly Nutmeg).",
              s=["intl"], lc="open", st="new", neo=[None, "Card network not verified."], src=[["Chase: Germany launch, May 2026", GERMANY]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the firm: the Chase app for 65 million, 5,164 branches and still opening, 11,000 advisors, partners from Apple to United, and J.P. Morgan's wholesale portals.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Chase app", "blurb": "65 million mobile users.", "div": "chase", "rev": "ccb", "products": [
            P("app", "Chase mobile & chase.com", "64.9 million active mobile users and 78 million digital.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["3Q26 supplement", Q3S]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "5,164 and opening 160 more.", "div": "chase", "rev": "ccb", "products": [
            P("branches", "Branches", "5,164 branches in all lower 48 states, more than 160 opening in 2026, and 19 community centres.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["Chase: 2026 branch plan, Feb 2026", BRANCHES], ["3Q26 supplement", Q3S]]),
        ]},
        {"id": "5.3", "ic": "headset", "name": "Advisors", "blurb": "About 11,000.", "div": "awm", "rev": "awm", "products": [
            P("advisors", "Advisors & bankers", "6,433 J.P. Morgan Wealth Management advisors and 4,460 Private Bank advisors.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["3Q26 supplement", Q3S]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners", "blurb": "Apple, Amazon, United, IHG.", "div": "chase", "rev": "ccb", "products": [
            P("partners", "Co-brand partners", "Apple, Amazon, Disney, airlines and hotels, on contracts of five to ten years.",
              s=["con", "aff"], lc="open", neo=[1, "Apple, IHG, Aeroplan, DoorDash, Instacart on Mastercard."], src=[["2025 Form 10-K", K25]]),
        ]},
        {"id": "5.5", "ic": "monitor", "name": "Wholesale portals", "blurb": "For corporates.", "div": "pay", "rev": "cib", "products": [
            P("portals", "J.P. Morgan Access & APIs", "Online and API access to J.P. Morgan Payments for corporate and institutional clients ⚠ names unverified.",
              s=["corp", "inst"], lc="open", neo=[0, ""], src=[["J.P. Morgan: commercial cards", COMMCARDS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at JPMorgan Chase", "blurb": "Apple Card, eight cards, Kinexys.", "products": [
        P("mcatjpm", "Mastercard at JPMorgan Chase", "Chase is mostly a Visa issuer (a ten-year renewable agreement from 2013, terms since not public), with eight Mastercard credit cards and Apple Card arriving on Mastercard around 2028. J.P. Morgan issues commercial cards on both networks, and Kinexys and JPMD connect to Mastercard's token network. Allison Beer and Naveen Mallela on the Chase side; Linda Kirkpatrick and Raj Dhamodharan on Mastercard's.",
          s=["inst"], div="jpmc", rev="corp", mc="The relationship this map is drawn for.",
          src=[["JPMorganChase: Chase to issue Apple Card, Jan 2026", APPLE], ["Visa and JPMorgan Chase, Feb 2013", VISA13], ["J.P. Morgan: JPMD live, Nov 2025", JPMD]]),
    ]},
    {"id": "pillar-market", "name": "US cards", "blurb": "Issuing, fees, rates.", "products": [
        P("market", "The US card market", "Chase first by purchase volume ($1.34 trillion in 2024) ahead of Amex and Citi; a proposed 10% APR cap (January 2026); open-banking fees; the interchange settlement and the Credit Card Competition Act ⚠ status unverified.",
          s=["inst"], div="jpmc", rev="corp", src=[["Nilson via FinancialContent, Mar 2025", NILSONISS]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
