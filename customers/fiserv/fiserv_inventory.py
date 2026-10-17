"""Fiserv's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the company's own unless a source says otherwise: the 2Q26 results (6 August 2026), the
FY2025 10-K (19 February 2026) and the May 2026 investor day. ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

SEC = "https://www.sec.gov/Archives/edgar/data/798354/"
Q2 = "https://www.sec.gov/Archives/edgar/data/0000798354/000079835426000028/fisvq226earningsrelease.htm"
Q2C = "https://vectorshift.ai/research/companies/fiserv/earnings/2026-q2"
FY25 = SEC + "000079835426000006/fisv4q25earningsrelease.htm"
K25 = SEC + "000079835426000009/fi-20251231.htm"
Q1C = "https://vectorshift.ai/research/companies/fiserv/earnings/2026-q1"
Q4C = "https://vectorshift.ai/research/companies/fiserv/earnings/2025-q4"
Q3 = SEC + "000079835425000168/fiq325earningsrelease.htm"
CEO = "https://www.sec.gov/Archives/edgar/data/798354/000119312526270336/d153349dex991.htm"
INVDAY = "https://finance.yahoo.com/markets/stocks/articles/fiserv-investor-day-sets-ai-010327577.html"
DAP = "https://finviz.com/news/397721/fiserv-digital-asset-platform-goes-live-with-financial-institution-clients-advancing-stablecoin-powered-banking-and-payments"
FIUSD = "https://thedigitalbanker.com/fiserv-launches-new-fiusd-stablecoin-for-financial-institutions/"
MCFIUSD = "https://decrypt.co/326731/mastercard-taps-fiserv-stablecoin-new-era-of-payments"
MCAGENT = "https://www.businesswire.com/news/home/20251222291522/en/"
VISAAGENT = "https://www.nasdaq.com/press-release/fiserv-collaborates-visa-accelerate-agentic-commerce-2025-12-22"
VI = "https://www.pymnts.com/mastercard/2026/mastercard-unveils-open-standard-to-verify-ai-agent-transactions/"
CLOUD = "https://www.stocktitan.net/news/FISV/fiserv-and-mastercard-deepen-global-partnership-to-help-merchants-hwriwkzgx6mp.html"
STARSALE = "https://www.fstech.co.uk/fst/Fiserv_Holding_Talks_With_US_Banks_For_Sale_Of_Debit_Card_Payments_Offering.php"
STAR = "https://www.fiserv.com/en/solutions/card-services/payment-networks/star-and-accel.html"
CARAT = "https://www.carat.fiserv.com/en-us/"
AFFIRM = "https://www.barchart.com/story/news/37228071/fiserv-and-affirm-join-forces-to-bring-flexible-payments-to-debit"
NILSON = "https://nilsonreport.com/articles/largest-merchant-acquirers-in-the-us-2025/"
ABOUT = "https://www.fiserv.com/en/about-fiserv.html"
MCAP = "https://stockanalysis.com/stocks/fisv/market-cap/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · charters · platforms", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $21 billion of revenue and $4.6 trillion of merchant volume, a merchant-acquirer bank charter, the First Data merger, Commerce Hub and Finxact underneath, a new CEO after a year of guidance cuts, and a plan to 2029.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & finances", "blurb": "$4.6 trillion of merchant volume.", "div": "fiserv", "rev": "grp", "products": [
            P("scale", "Scale", "$4.6 trillion of merchant transactions in 2025, about a third of US merchant volume, more than 6 million merchant locations, 1.6 billion issuing accounts on file and about 10,000 bank and credit-union clients; claims to be the largest US acquirer (Nilson, 2025 data).",
              s=["inv"], neo=[0, ""], src=[["Investor day coverage, May 2026", INVDAY], ["Fiserv: about", ABOUT], ["Nilson: largest US acquirers, Mar 2026", NILSON]]),
            P("finances", "Finances", "Revenue of $21.2 billion in 2025; 2Q26 adjusted revenue $4.96 billion (−4%) and adjusted EPS $1.84; 2026 guidance cut on 6 August to organic growth of −1% to 0% and EPS of $7.20–7.40; rated Baa2; market value about $25 billion, from $117 billion at the end of 2024.",
              s=["inv"], neo=[0, ""], src=[["2Q26 results", Q2], ["FY2025 results", FY25], ["StockAnalysis: market cap", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Charters & licences", "blurb": "A merchant-acquirer bank.", "div": "fiserv", "rev": "grp", "products": [
            P("licences", "Charters & supervision", "A Georgia merchant-acquirer limited-purpose bank, trust companies in New Hampshire and Colorado (StoneCastle, December 2025), money-transmitter and European e-money licences; examined by bank regulators as a significant service provider.",
              s=["fi", "inv"], neo=[0, ""], src=[["FY2025 10-K", K25]]),
        ]},
        {"id": "1.3", "ic": "users-round", "name": "Leadership", "blurb": "Georgakopoulos since June.", "div": "fiserv", "rev": "grp", "products": [
            P("leadership", "Leadership", "CEO Takis Georgakopoulos (15 June 2026; ex-J.P. Morgan Payments) after Mike Lyons left for Truist; CFO Paul Todd; chair Gordon Nixon; Sanjay Saraf runs merchant product and technology, Lia Cao merchant revenue, Sunil Sachdev embedded finance and digital assets; Financial Solutions under interim co-heads.",
              s=["inv"], neo=[0, ""], src=[["Fiserv: CEO transition, Jun 2026", CEO], ["Fiserv and Mastercard, Aug 2026", CLOUD]]),
        ]},
        {"id": "1.4", "ic": "badge-check", "name": "Heritage", "blurb": "Fiserv + First Data.", "div": "fiserv", "rev": "grp", "products": [
            P("heritage", "Fiserv & First Data", "Fiserv (1984, Wisconsin) took over First Data in 2019 ⚠, bringing merchant acquiring, Clover, STAR and the Optis and VisionPLUS issuer platforms; back on Nasdaq as FISV since November 2025.",
              s=["inv"], o="A", neo=[0, ""], src=[["FY2025 10-K", K25]]),
        ]},
        {"id": "1.5", "ic": "database", "name": "Platforms", "blurb": "Commerce Hub & Finxact.", "div": "fiserv", "rev": "grp", "products": [
            P("commercehub", "Commerce Hub", "The merchant gateway and orchestration layer: about $200 billion across 40 markets in 2025, North American volume up more than 200%; now the anchor of one merchant technology organisation.",
              s=["ent", "isv"], o="B", neo=[1, "Mastercard Merchant Cloud integrating."], src=[["Investor day coverage, May 2026", INVDAY], ["2Q26 call", Q2C]]),
            P("finxact", "Finxact", "A cloud-native core and ledger with more than 30 million accounts, the ledger behind embedded finance and the stablecoin platform.",
              s=["fi", "isv"], o="A", neo=[0, ""], src=[["4Q25 call", Q4C]]),
        ]},
        {"id": "1.6", "ic": "target", "name": "Strategy", "blurb": "One Fiserv, Project Elevate.", "div": "fiserv", "rev": "grp", "products": [
            P("strategy", "One Fiserv & Project Elevate", "After the October 2025 reset (shares down 44% in a day), a five-point plan, $500 million of AI-led cost savings and targets for 2029: 4–6% revenue growth, margins above 37% and EPS above $12.",
              s=["inv"], neo=[0, ""], src=[["3Q25 results", Q3], ["Investor day coverage, May 2026", INVDAY]]),
            P("portfolio", "Portfolio review", "Exiting student-loan servicing and unprofitable India businesses, ATMs moved into a MoneyPass joint venture with Bridgepoint (August 2026), and a review that includes the STAR and Accel debit networks.",
              s=["inv"], st="flux", neo=[0, ""], src=[["2Q26 results", Q2], ["2Q26 call", Q2C]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: merchant acquiring at a third of US volume, enterprise acceptance with Carat and now Mastercard Merchant Cloud, issuer processing for card programmes, the STAR and Accel debit networks, Zelle and bill pay for banks, and a stablecoin platform.",
    "tiles": [
        {"id": "2.1", "ic": "store", "name": "Merchant acquiring", "blurb": "A third of US volume.", "div": "fiserv", "rev": "merch", "products": [
            P("acquiring", "Merchant acquiring", "Authorisation, settlement and funding across Visa, Mastercard, STAR and Accel for small businesses and enterprises, and processing for bank joint ventures, ISOs and resellers (down 8% in 2Q26).",
              s=["sme", "ent"], lc="move", neo=[1, "Accepts every network."],
              src=[["FY2025 10-K", K25], ["2Q26 call", Q2C]]),
        ]},
        {"id": "2.2", "ic": "building-2", "name": "Enterprise acceptance", "blurb": "Carat & Merchant Cloud.", "div": "carat", "rev": "merch", "products": [
            P("carat", "Carat", "Enterprise commerce on Commerce Hub, with routing over Fiserv's own STAR and Accel debit networks; AT&T among recent wins.",
              s=["ent"], lc="move", neo=[1, "All networks; routes debit to STAR and Accel."], src=[["Carat", CARAT], ["4Q25 call", Q4C]]),
            P("merchantcloud", "Mastercard Merchant Cloud in Commerce Hub", "A global partnership (4 August 2026): one connection from Commerce Hub to Mastercard's merchant and value-added services, agentic included, across channels and countries; integration expected to take a couple of quarters.", short="Mastercard Merchant Cloud",
              s=["ent"], lc="grow", st="new", ay="Aug 2026", o="P", at="Mastercard", neo=[3, "Mastercard's own product."],
              mc="The pipe is built; the services that run through it (Click to Pay, passkeys, Ethoca, fraud scores) are not yet named.",
              src=[["Fiserv and Mastercard deepen partnership, Aug 2026", CLOUD]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Issuer processing", "blurb": "25 of the top 50 US issuers.", "div": "fin", "rev": "fin", "products": [
            P("issuing", "Optis, FirstVision & VisionPLUS", "Credit, debit and private-label processing for 25 of the top 50 US credit issuers and 80% of US private-label issuers (PNC and Atlanticus extended), VisionPLUS internationally and VisionNext in development; issuing revenue fell 10% in 2Q26.",
              s=["fi"], lc="everyday", neo=[1, "Processes Mastercard programmes among others."],
              mc="The least-evidenced and biggest white space: tokens, Click to Pay enrolment and Installments sold to thousands of issuers through one processor.",
              src=[["FY2025 10-K", K25], ["Investor day coverage, May 2026", INVDAY]]),
        ]},
        {"id": "2.4", "ic": "network", "name": "Debit networks", "blurb": "STAR & Accel.", "div": "star", "rev": "fin", "products": [
            P("star", "STAR & Accel", "Fiserv's own PIN and PINless debit networks: more than 300 million cardholders at over 5,000 institutions, the main alternatives to Visa and Mastercard on dual-routed debit. JPMorgan, Bank of America, Wells Fargo and PNC were reported in July 2026 to have discussed buying one.", short="STAR & Accel",
              s=["fi", "ent"], lc="move", st="flux", neo=[0, "Competes with Debit Mastercard."],
              mc="Volume routed to STAR or Accel is volume not on Debit Mastercard; bank ownership would change the debit landscape.",
              src=[["Fiserv: STAR and Accel", STAR], ["FStech: debit network sale talks, Jul 2026", STARSALE]]),
            P("moneypass", "MoneyPass & ATMs", "The surcharge-free ATM network and ATM services, moved into a joint venture with Bridgepoint in August 2026 (Fiserv keeps about 49%).",
              s=["con", "fi"], lc="everyday", st="flux", neo=[0, ""], src=[["2Q26 results", Q2]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Real-time & bill pay", "blurb": "Zelle, CheckFree.", "div": "fin", "rev": "fin", "products": [
            P("zelle", "Zelle, RTP & FedNow connections", "Turnkey Zelle for banks and credit unions (transactions up 18% in 1Q26) and connections to ACH, RTP and FedNow; consumer payment solutions used by 41 of the top 50 US banks.",
              s=["fi", "con"], lc="move", neo=[0, "Account-to-account."], src=[["1Q26 call", Q1C], ["Investor day coverage, May 2026", INVDAY]]),
            P("checkfree", "CheckFree bill pay", "Bill payment for banks' customers, with transactions falling by high single digits.",
              s=["fi", "con"], lc="move", neo=[0, ""], src=[["FY2025 10-K", K25], ["1Q26 call", Q1C]]),
        ]},
        {"id": "2.6", "ic": "coins", "name": "Digital assets", "blurb": "FIUSD & Roughrider.", "div": "fin", "rev": "fin", "products": [
            P("fiusd", "FIUSD & the Digital Asset Platform", "FIUSD (June 2025) for banks on Paxos and Circle infrastructure, with Mastercard committed to integrate it (Multi-Token Network, settlement, cards); the Digital Asset Platform went live on 1 October 2026 with Bank of North Dakota's Roughrider Coin for more than 90 North Dakota institutions.", short="FIUSD & stablecoins",
              s=["fi", "ent"], lc="move", st="new", ay="Oct 2026", o="P", at="Paxos, Circle, Mastercard", neo=[1, "Mastercard integration announced, not live."],
              mc="Merchant settlement and FIUSD-linked cards on Mastercard are still to ship.",
              src=[["FIUSD launch, Jun 2025", FIUSD], ["Decrypt: Mastercard and FIUSD, Jun 2025", MCFIUSD], ["Digital Asset Platform live, Oct 2026", DAP]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every transaction: agentic acceptance with both networks, fraud and risk, an AI operating layer for banks, embedded finance, small-business lending and gift and loyalty programmes.",
    "tiles": [
        {"id": "3.1", "ic": "bot", "name": "Agentic commerce", "blurb": "Mastercard and Visa, same day.", "div": "clover", "rev": "merch", "products": [
            P("agentpay", "Mastercard Agent Pay & Verifiable Intent", "Fiserv adopted Mastercard's Agent Pay acceptance framework 'at scale' on 22 December 2025, becoming a network token requestor with Secure Card on File for Clover and e-commerce, and backed Verifiable Intent (March 2026). No live volume has been reported.", short="Agent Pay",
              s=["sme", "ent"], lc="move", st="new", ay="Dec 2025", o="P", at="Mastercard", neo=[3, "Mastercard Agent Pay."],
              mc="From framework to live transactions on Clover and Carat.",
              src=[["Business Wire: Fiserv and Mastercard, Dec 2025", MCAGENT], ["PYMNTS: Verifiable Intent, Mar 2026", VI]]),
            P("visaagent", "Visa Intelligent Commerce & Trusted Agent Protocol", "Announced the same day as the Mastercard deal, for Clover, Fiserv merchants and ISV partners: Fiserv is network-neutral on agents.",
              s=["sme", "ent"], lc="move", st="new", ay="Dec 2025", o="P", at="Visa", neo=[0, "Visa."],
              src=[["Fiserv and Visa, Dec 2025", VISAAGENT]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud & risk", "blurb": "OpenAI for authorisations.", "div": "fiserv", "rev": "grp", "products": [
            P("fraud", "Fraud, risk & authorisations", "Fraud and risk suites for issuers and merchants, credit decisioning from Money Money (Brazil), and an OpenAI collaboration on authorisation rates and fraud ⚠ named products unverified.",
              s=["fi", "ent"], lc="everyday", neo=[0, "No Mastercard fraud product announced."],
              mc="Decision Intelligence for issuers and Ethoca and Consumer Clarity for merchants' disputes.",
              src=[["Investor day coverage, May 2026", INVDAY], ["FY2025 10-K", K25]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "AI", "blurb": "agentOS.", "div": "fiserv", "rev": "grp", "products": [
            P("agentos", "agentOS & AI", "agentOS (beta), a governed layer for AI agents across banks' systems of record, piloted at First Interstate and Boulder Dam Credit Union; a strategic collaboration with OpenAI; a quarter of merchant code written by AI.",
              s=["fi"], lc="beyond", st="new", o="P", at="OpenAI", neo=[0, ""], src=[["Investor day coverage, May 2026", INVDAY]]),
        ]},
        {"id": "3.4", "ic": "plug", "name": "Embedded finance", "blurb": "Ledgers, payouts, accounts.", "div": "fiserv", "rev": "fin", "products": [
            P("embedded", "Embedded finance", "Finxact's ledger, Payfare's payout orchestration (March 2025) and Commerce Hub acceptance sold as one stack for platforms, with a developer portal for agentic commerce.",
              s=["isv"], lc="beyond", st="new", neo=[0, ""], src=[["FY2025 10-K", K25], ["1Q26 call", Q1C]]),
        ]},
        {"id": "3.5", "ic": "hand-coins", "name": "Small-business finance", "blurb": "Clover Capital, CashFlow Central.", "div": "clover", "rev": "merch", "products": [
            P("smbfinance", "Clover Capital & CashFlow Central", "Merchant cash advances (Clover Capital, +30% in North America in 2025), Clover Savings via StoneCastle, and CashFlow Central, receivables and payables that 155 banks offer more than 100,000 small businesses.",
              s=["sme", "fi"], lc="borrow", neo=[0, ""], src=[["4Q25 call", Q4C], ["1Q26 call", Q1C]]),
        ]},
        {"id": "3.6", "ic": "gift", "name": "Gift & loyalty", "blurb": "Stored value for enterprises.", "div": "carat", "rev": "merch", "products": [
            P("giftloyalty", "Gift & loyalty", "Gift-card and loyalty stored-value programmes for enterprise merchants.",
              s=["ent", "con"], lc="grow", neo=[0, ""],
              mc="Card-linked offers through Merchant Cloud.",
              src=[["FY2025 10-K", K25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Two segments opened out into what clients buy: Clover and enterprise acceptance on the merchant side; cores, digital banking, card issuing and payouts for about 10,000 banks and credit unions on the other.",
    "tiles": [
        {"id": "4.1", "ic": "store", "name": "Clover", "blurb": "$3.3 billion, about 900,000 merchants.", "div": "clover", "rev": "merch", "products": [
            P("clover", "Clover", "Point of sale, payments and software for small businesses: $3.3 billion of revenue in 2025 (+23%), growth slowing to mid-single digits in 2026; value-added services a quarter of revenue; PracticePay for healthcare (2026).",
              s=["sme"], lc="everyday", neo=[1, "Accepts Mastercard; Agent Pay framework."], src=[["4Q25 call", Q4C], ["2Q26 call", Q2C]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Enterprise merchants", "blurb": "Restaurants to telecoms.", "div": "carat", "rev": "merch", "products": [
            P("enterprise", "Enterprise merchants", "Commerce Hub and Carat for large merchants, CardFree restaurant ordering (2025), and AT&T and Restaurant Depot among recent clients.",
              s=["ent"], lc="everyday", neo=[1, "Merchant Cloud coming."], src=[["4Q25 call", Q4C], ["FY2025 10-K", K25]]),
        ]},
        {"id": "4.3", "ic": "landmark", "name": "Core banking", "blurb": "Almost 3,000 banks.", "div": "fin", "rev": "fin", "products": [
            P("core", "DNA, Premier, Signature & Finxact", "Cores for almost 3,000 banks and credit unions, with 'no forced migrations'; wins at Mechanics Bancorp, OceanFirst and Truliant.",
              s=["fi"], lc="everyday", neo=[0, ""], src=[["1Q26 call", Q1C], ["Investor day coverage, May 2026", INVDAY]]),
        ]},
        {"id": "4.4", "ic": "smartphone", "name": "Digital banking", "blurb": "XD, and BNPL on debit.", "div": "fin", "rev": "fin", "products": [
            P("xd", "Experience Digital & debit pay-over-time", "XD, the digital channel for banks' consumers and small businesses, and pay-over-time on debit cards built in with Affirm (2026 ⚠ date unverified).",
              s=["fi", "con"], lc="borrow", st="new", o="P", at="Affirm", neo=[0, "Affirm."],
              mc="Mastercard Installments is the network-native answer.",
              src=[["FY2025 10-K", K25], ["Fiserv and Affirm", AFFIRM]]),
        ]},
        {"id": "4.5", "ic": "wallet-cards", "name": "Card programmes", "blurb": "Issuing services.", "div": "fin", "rev": "fin", "products": [
            P("cardservices", "Card issuing services", "Card production, programme management, co-brand mandates (Fidem) and credit-union card services.",
              s=["fi"], lc="everyday", neo=[1, "Mastercard and Visa programmes."], src=[["4Q25 call", Q4C], ["FY2025 10-K", K25]]),
        ]},
        {"id": "4.6", "ic": "send", "name": "Payouts & prepaid", "blurb": "Money Network, Payfare.", "div": "fin", "rev": "fin", "products": [
            P("payouts", "Money Network, Payfare & Thunes", "Prepaid payroll cards, earned-wage and gig payouts (Payfare) and real-time global payouts with Thunes (August 2026).",
              s=["isv", "con"], lc="move", neo=[None, "Network split not public."],
              mc="Mastercard Move for cross-border payouts.",
              src=[["FY2025 10-K", K25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How clients reach Fiserv: Clover devices and the App Market, banks that refer their merchants, partners abroad, and developers and salespeople.",
    "tiles": [
        {"id": "5.1", "ic": "monitor", "name": "Clover devices", "blurb": "Station to Go.", "div": "clover", "rev": "merch", "products": [
            P("devices", "Clover devices & App Market", "Countertop, handheld and kiosk devices and an app market; hardware weakness weighed on 2026 revenue.",
              s=["sme"], lc="open", neo=[0, ""], src=[["2Q26 call", Q2C]]),
        ]},
        {"id": "5.2", "ic": "landmark", "name": "Bank referrals", "blurb": "40 of the top 100 banks.", "div": "clover", "rev": "merch", "products": [
            P("bankchannel", "Bank referral channel", "Banks that sell Clover to their business customers: nearly 40 of the top 100 US banks after Western Alliance went live; 47 added in 2025.",
              s=["fi", "sme"], lc="open", neo=[0, ""], src=[["2Q26 call", Q2C], ["4Q25 call", Q4C]]),
        ]},
        {"id": "5.3", "ic": "earth", "name": "International", "blurb": "TD, Caixa, SMCC, AIB.", "div": "fiserv", "rev": "merch", "products": [
            P("intl", "International partners", "TD in Canada (80,000 merchants converting in 2027), Caixa in Brazil, SMCC in Japan, AIB Merchant Services (now wholly owned), CCV in the Netherlands and Pinch in New Zealand.",
              s=["sme", "fi"], lc="open", neo=[0, ""], src=[["FY2025 10-K", K25], ["2Q26 call", Q2C]]),
        ]},
        {"id": "5.4", "ic": "code-xml", "name": "Developers & sales", "blurb": "APIs and 600 sellers.", "div": "fiserv", "rev": "merch", "products": [
            P("developers", "Developer portals & direct sales", "Commerce Hub APIs, the agentic developer portal, and more than 600 direct salespeople in North America.",
              s=["isv", "ent"], lc="open", neo=[0, ""], src=[["1Q26 call", Q1C], ["4Q25 call", Q4C]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Fiserv", "blurb": "Four deals in 14 months.", "products": [
        P("mcatfiserv", "Mastercard at Fiserv", "Fiserv acquires and processes Mastercard volume at scale, and the partnership has escalated: FIUSD integration (June 2025), the Agent Pay acceptance framework (December 2025), Verifiable Intent (March 2026) and Mastercard Merchant Cloud inside Commerce Hub (August 2026), each sponsored by Chiro Aikat. Fiserv hedges with Visa on agents, and its STAR and Accel networks compete with Debit Mastercard.",
          s=["inv"], div="fiserv", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Fiserv and Mastercard, Aug 2026", CLOUD], ["Business Wire: Fiserv and Mastercard, Dec 2025", MCAGENT]]),
    ]},
    {"id": "pillar-market", "name": "US payments", "blurb": "Debit routing, agents, stablecoins.", "products": [
        P("market", "The US payments market", "Durbin dual routing and the litigation around it, the race to set agentic standards, stablecoins under the GENIUS Act, and rivals from JPMorgan and Global Payments to Stripe and Square.",
          s=["inv"], div="fiserv", rev="grp", src=[["FStech: debit network sale talks, Jul 2026", STARSALE], ["FY2025 10-K", K25]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
