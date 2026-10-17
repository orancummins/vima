"""Capital One's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the company's own unless a source says otherwise: the 2Q26 results and 10-Q (July 2026) and
the FY2025 10-K (19 February 2026). ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's
own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

SEC = "https://www.sec.gov/Archives/edgar/data/927628/"
K25 = SEC + "000092762826000024/cof-20251231.htm"
Q2 = SEC + "000092762826000083/ex991q22026earningsrelease.htm"
Q2S = SEC + "000092762826000083/ex992q22026earningsrelease.htm"
Q2Q = SEC + "000092762826000089/cof-20260630.htm"
BREX = SEC + "000119312526019543/d97758dex991.htm"
BREXC = SEC + "000119312526145764/d85207d8k.htm"
PROXY = SEC + "000119312526124131/d701179ddef14a.htm"
Q2CALL = "https://www.investing.com/news/transcripts/earnings-call-transcript-capital-one-beats-q2-2026-profit-estimates-as-stock-edges-higher-93CH-4804418"
Q4CALL = "https://www.fool.com/earnings/call-transcripts/2026/01/22/capital-one-cof-q4-2025-earnings-call-transcript/"
MCRENEW = "https://www.paymentsdive.com/news/mastercard-reworks-cap-one-pact/810868/"
MIGRATE = "https://www.paymentsjournal.com/capital-one-starts-migrating-core-cards-to-discover-network/"
MIGRATE2 = "https://www.paymentsjournal.com/after-moving-debit-cards-to-discover-capital-one-turns-to-credit-card-migration/"
DOC = "https://www.doctorofcredit.com/is-capital-one-moving-their-credit-cards-to-discover-network/"
DEBIT = "https://www.capitalone.com/bank/debit-card/my-debit-card/"
MAQ1 = "https://www.fool.com/earnings/call-transcripts/2026/04/30/mastercard-ma-q1-2026-earnings-transcript/"
WALMART = "https://www.doctorofcredit.com/capital-one-walmart-end-partnership"
VX = "https://www.capitalone.com/credit-cards/venture-x/"
COMPARE = "https://www.capitalone.com/credit-cards/compare/"
DGN = "https://www.discoverglobalnetwork.com/"
DISCOVER = "https://www.discover.com/credit-cards/"
SOFTWARE = "https://capitalonesoftware.com/"
CLOUD = "https://www.capitalone.com/tech/cloud/"
CHECKING = "https://www.capitalone.com/bank/checking-accounts/online-checking-account/"
CAFES = "https://www.capitalone.com/local/"
CREDITWISE = "https://www.capitalone.com/creditwise/"
ENO = "https://www.capitalone.com/digital/eno/"
SHOPPING = "https://capitaloneshopping.com/"
LOUNGES = "https://www.capitalone.com/about/newsroom/capital-one-lounges-earn-top-honors-from-jd-power/"
HOPPER = "https://skift.com/2026/04/22/capital-one-closed-acquired-hopper-tech-employees-deal/"
AI = "https://www.euromoney.com/article/2eh2s01l11023kmxtleyo/fintech/prem-natarajan-on-capital-ones-ai-stairway-to-heaven/"
CCCA = "https://www.congress.gov/bill/119th-congress/senate-bill/3623/text"
MCAP = "https://companiesmarketcap.com/capital-one/marketcap/"
WIKI = "https://en.wikipedia.org/wiki/Capital_One"
NILSON = "https://wtop.com/news/2026/03/8-biggest-u-s-credit-card-companies-this-year/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · charter · cloud", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a $674 billion balance sheet and the largest US card book by loans, one national bank after Discover folded in, a founder still in charge, an all-in move to the cloud, and a thesis that Capital One is now a payments company.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & capital", "blurb": "$674 billion of assets.", "div": "grp", "rev": "grp", "products": [
            P("balance", "Balance sheet", "Total assets of $673.8 billion, loans of $457.2 billion and deposits of $484.3 billion at 30 June 2026; more than 100 million customers; the largest US card issuer by loans.",
              s=["inv"], neo=[0, ""], src=[["2Q26 results", Q2], ["FY2025 10-K", K25]]),
            P("earnings", "Earnings & capital", "Revenue of $53.4 billion in 2025 but net income of only $2.45 billion after the Discover allowance; 2Q26 net income $3.0 billion (ROTCE 18%), NIM 8.01%, CET1 13.7%; a $16 billion buyback; market value about $124 billion.",
              s=["inv"], neo=[0, ""], src=[["2Q26 supplement", Q2S], ["FY2025 10-K", K25], ["CompaniesMarketCap", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Charter & regulation", "blurb": "One national bank.", "div": "grp", "rev": "grp", "products": [
            P("charter", "Capital One, N.A. & obligations", "Discover Bank merged into Capital One, N.A. in May 2025; a UK card business and a Canadian branch; Discover's 2025 consent order and a $1.2 billion merchant restitution reserve; the $425 million 360 Savings settlement (approved April 2026, under appeal).",
              s=["inv"], neo=[0, ""], src=[["FY2025 10-K", K25], ["2Q26 10-Q", Q2Q]]),
        ]},
        {"id": "1.3", "ic": "users-round", "name": "Leadership", "blurb": "Fairbank since 1988.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Leadership", "Founder, chairman and CEO Richard Fairbank; CFO Andrew Young; Mark Mouadeb (Card), Lia Dean (Banking & Premium Products), Jason Hanson (Global Payment Network, also CEO of Discover Global Network), Neal Blinde (Commercial), Sanjiv Yajnik (Auto); Prem Natarajan heads AI.",
              s=["inv"], neo=[0, ""], src=[["2026 proxy statement", PROXY]]),
        ]},
        {"id": "1.4", "ic": "badge-check", "name": "Heritage", "blurb": "Signet 1988, ING Direct, Discover.", "div": "grp", "rev": "grp", "products": [
            P("heritage", "From Signet to Discover", "A card division of Signet Bank (1988), spun off in 1994–95; Hibernia, North Fork and Chevy Chase built the bank; ING Direct became Capital One 360 (2012); Discover closed 18 May 2025 ($51.8 billion at close).",
              s=["inv"], o="A", neo=[0, ""], src=[["Wikipedia: Capital One", WIKI], ["FY2025 10-K", K25]]),
        ]},
        {"id": "1.5", "ic": "database", "name": "Cloud & AI", "blurb": "All in on AWS.", "div": "grp", "rev": "grp", "products": [
            P("cloud", "Cloud & enterprise AI", "All in on AWS since the last data centre closed; TSYS card processing and FIS for parts of banking; enterprise AI under a chief scientist, including Chat Concierge, an agentic assistant for car dealers.",
              s=["inv"], o="P", at="AWS", neo=[0, ""], src=[["Capital One Tech: cloud", CLOUD], ["Euromoney: Prem Natarajan", AI], ["FY2025 10-K", K25]]),
        ]},
        {"id": "1.6", "ic": "target", "name": "Strategy", "blurb": "'A payments company'.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "The payments thesis", "'We set out to build a payments company': own the network (Discover, the 'crown jewel'), move debit and test credit onto it, push international acceptance, and add Brex for business payments; $2.5 billion of Discover synergies.",
              s=["inv"], neo=[0, ""], mc="The thesis is, in large part, to need Visa and Mastercard less.",
              src=[["Brex deal release, Jan 2026", BREX], ["Q4 2025 call", Q4CALL], ["Q2 2026 call", Q2CALL]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Five ways money moves: Capital One's own Discover, PULSE and Diners networks; 25 million debit cards moved onto them; consumer credit being tested on Discover with Venture X still on Visa; business and co-brand cards still on Mastercard; and Zelle and cross-border.",
    "tiles": [
        {"id": "2.1", "ic": "network", "name": "Discover Global Network", "blurb": "$190 billion a quarter.", "div": "network", "rev": "network", "products": [
            P("discover", "Discover, PULSE & Diners Club", "Capital One's own networks: Discover for credit and debit, PULSE for PIN debit and ATMs, Diners Club International abroad; 439 million cards and acceptance in 185 countries; $189.6 billion of network volume in 2Q26.", short="Discover network",
              s=["merch", "fin"], lc="move", o="A", ay="May 2025", neo=[0, "Capital One's own network."],
              mc="The direct competitor: every account that moves to Discover leaves Mastercard or Visa.",
              src=[["Discover Global Network", DGN], ["2Q26 10-Q", Q2Q]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Debit", "blurb": "25 million cards to Discover.", "div": "consumer", "rev": "consumer", "products": [
            P("debit", "Debit on Discover", "About 25 million debit cards moved from Mastercard to Discover from August 2025, 'basically complete' in the first quarter of 2026; Mastercard network benefits no longer apply.", short="Debit (now Discover)",
              s=["con"], lc="everyday", st="retired", neo=[0, "Moved from Mastercard to Discover."],
              mc="Cost Mastercard about 6–7 points of US debit volume growth in early 2026.",
              src=[["Capital One: debit card", DEBIT], ["Mastercard Q1 2026 call", MAQ1], ["PaymentsJournal, Mar 2026", MIGRATE]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Consumer credit", "blurb": "Moving to Discover, by test.", "div": "card", "rev": "card", "products": [
            P("migration", "Savor, Quicksilver & Venture on Discover", "New Savor, Quicksilver, Venture and VentureOne accounts originated on Discover from February–March 2026, and existing Quicksilver cards converted ⚠ by July; how much moves depends on tests of new and existing accounts. Savor holders lose World Elite benefits.", short="Credit moving to Discover",
              s=["con"], lc="everyday", st="flux", neo=[1, "Back book still partly Mastercard."],
              mc="Mastercard renewed its credit agreement in January 2026 for 'a large portion of newly acquired credit accounts', weeks before the flagships moved.",
              src=[["Doctor of Credit, Feb–Apr 2026", DOC], ["PaymentsJournal, Jul 2026", MIGRATE2], ["Payments Dive: Mastercard renewal, Jan 2026", MCRENEW]]),
            P("venturex", "Venture X (Visa)", "The $395 premium travel card stays on Visa Infinite 'for now', because travellers need acceptance abroad that Discover lacks.", short="Venture X (Visa)",
              s=["aff"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Capital One: Venture X", VX], ["PaymentsJournal, Mar 2026", MIGRATE]]),
        ]},
        {"id": "2.4", "ic": "briefcase", "name": "Business & co-brand cards", "blurb": "Still Mastercard.", "div": "card", "rev": "card", "products": [
            P("spark", "Spark & Venture X Business", "Small-business cards (Spark Cash Plus, Cash, Cash Select, Classic) and Venture X Business, on Mastercard; Discover does not serve a large business-card audience.", short="Business cards (Mastercard)",
              s=["sme"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Capital One: compare cards", COMPARE], ["PaymentsJournal, Mar 2026", MIGRATE]]),
            P("cobrands", "Co-brands", "REI, BJ's, Bass Pro and Cabela's on Mastercard, T-Mobile and Kohl's on Visa, kept off Discover 'for the time being'; Walmart left in 2024 for OnePay and Synchrony.", short="Co-brands",
              s=["con"], lc="everyday", neo=[1, "REI, BJ's, Bass Pro on Mastercard."],
              src=[["Capital One: compare cards", COMPARE], ["Doctor of Credit: Walmart ends partnership, Jul 2024", WALMART]]),
        ]},
        {"id": "2.5", "ic": "earth", "name": "Real-time & abroad", "blurb": "Zelle, UK, Canada.", "div": "cof", "rev": "card", "products": [
            P("zelle", "Zelle", "Zelle in 360 accounts.",
              s=["con"], lc="move", neo=[0, "Off the card networks."], src=[["Capital One: 360 Checking", CHECKING]]),
            P("intl", "UK & Canada cards", "$7.8 billion of card loans in the UK and Canada; the January 2026 Mastercard renewal covered Canada, and Fairbank wants Capital One's own issuing there to help Discover acceptance.",
              s=["con"], lc="everyday", neo=[2, "Mastercard ⚠."], src=[["2Q26 supplement", Q2S], ["Payments Dive: Mastercard renewal, Jan 2026", MCRENEW]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: Eno and CreditWise, enterprise AI, Capital One Travel rebuilt in-house, Capital One Shopping, the Mastercard services kept under the 2026 agreement, and the Discover integration.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Eno, CreditWise.", "div": "cof", "rev": "card", "products": [
            P("eno", "Eno & CreditWise", "Eno flags suspicious and recurring charges and answers questions in the app, by text and on watches; CreditWise gives anyone a free FICO score, dark-web alerts and a credit simulator.",
              s=["con"], lc="everyday", neo=[0, "Capital One's own."], src=[["Capital One: Eno", ENO], ["Capital One: CreditWise", CREDITWISE]]),
        ]},
        {"id": "3.2", "ic": "key-round", "name": "Mastercard services", "blurb": "'Several', unnamed.", "div": "cof", "rev": "card", "products": [
            P("mcservices", "Mastercard services", "Under the January 2026 renewal, 'Capital One will continue to use several of Mastercard's services'; neither side has named them.", short="Mastercard services",
              s=["con", "sme"], lc="everyday", o="P", at="Mastercard", neo=[3, "Mastercard's own, unnamed."],
              mc="Services not tied to which network carries the card: fraud, identity, tokens, data, Agent Pay.",
              src=[["Payments Dive: Mastercard renewal, Jan 2026", MCRENEW]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "AI", "blurb": "Chat Concierge.", "div": "cof", "rev": "consumer", "products": [
            P("ai", "Enterprise AI", "Reasoning, task-executing AI systems; Chat Concierge for car dealers; Brex's AI expense agents.",
              s=["auto", "sme"], lc="beyond", st="new", neo=[0, ""], src=[["Euromoney: Prem Natarajan", AI], ["Brex deal release, Jan 2026", BREX]]),
        ]},
        {"id": "3.4", "ic": "plane", "name": "Travel & rewards", "blurb": "Capital One Travel, rebuilt.", "div": "card", "rev": "card", "products": [
            P("travel", "Capital One Travel & Entertainment", "Venture miles (10x hotels and cars, 5x flights through Capital One Travel); the Hopper-built travel platform and about 150 Hopper staff brought in-house in April 2026; Capital One Entertainment.",
              s=["aff"], lc="grow", st="new", neo=[0, ""], src=[["Skift: Hopper technology, Apr 2026", HOPPER], ["Capital One: Venture X", VX]]),
        ]},
        {"id": "3.5", "ic": "gift", "name": "Shopping & offers", "blurb": "Capital One Shopping.", "div": "cof", "rev": "consumer", "products": [
            P("shopping", "Capital One Shopping", "Automatic coupons, price-drop alerts and cash-back deals in a browser extension and app, open to anyone.",
              s=["con", "merch"], lc="grow", neo=[0, ""],
              mc="Merchant-funded offers and benefits to replace the World Elite perks Savor holders lost.",
              src=[["Capital One Shopping", SHOPPING]]),
        ]},
        {"id": "3.6", "ic": "refresh-cw", "name": "Discover integration", "blurb": "14 of 24 months.", "div": "grp", "rev": "grp", "products": [
            P("integration", "Discover integration", "About a third of cost synergies realised by 2Q26 and the rest by the second half of 2027; Discover's back book converting in waves through January 2027; $298 million of integration costs in 2Q26.",
              s=["inv"], lc="beyond", st="flux", neo=[0, ""], src=[["2Q26 results", Q2], ["PaymentsJournal, Jul 2026", MIGRATE2]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Three segments opened out: consumer and small-business cards (with Brex), the 360 retail bank, auto finance, commercial banking, the network as a business, and Capital One Software.",
    "tiles": [
        {"id": "4.1", "ic": "credit-card", "name": "Consumer cards", "blurb": "$259 billion of loans.", "div": "card", "rev": "card", "products": [
            P("cards", "Venture, Quicksilver, Savor & Discover it", "The largest US card book by loans ($259 billion domestic; $249 billion of purchase volume in 2Q26), from Platinum Secured to Venture X, plus Discover it cards still sold on discover.com.",
              s=["con", "aff"], lc="borrow", neo=[1, "Partly Mastercard; moving to Discover."], src=[["2Q26 supplement", Q2S], ["Discover: credit cards", DISCOVER]]),
        ]},
        {"id": "4.2", "ic": "briefcase-business", "name": "Small business & Brex", "blurb": "Brex, $5.15 billion.", "div": "card", "rev": "card", "products": [
            P("brex", "Brex", "Corporate cards, expense management, bill pay, travel and business accounts for 35,000 companies, bought for $5.15 billion (closed 7 April 2026) and now part of the card segment.",
              s=["sme", "corp"], lc="everyday", st="new", ay="Apr 2026", o="A", neo=[None, "Network not verified."],
              mc="Commercial and virtual-card capabilities are the logical Mastercard pitch.",
              src=[["Brex closing 8-K, Apr 2026", BREXC], ["Brex deal release, Jan 2026", BREX]]),
        ]},
        {"id": "4.3", "ic": "wallet", "name": "Retail bank", "blurb": "360, $424 billion of deposits.", "div": "consumer", "rev": "consumer", "products": [
            P("bank360", "360 Checking & Savings", "No-fee checking with early paycheck and 70,000 fee-free ATMs, savings and CDs: $424 billion of consumer deposits.",
              s=["con"], lc="everyday", neo=[0, "Discover debit."], src=[["Capital One: 360 Checking", CHECKING], ["FY2025 10-K", K25]]),
        ]},
        {"id": "4.4", "ic": "target", "name": "Auto finance", "blurb": "$89 billion.", "div": "consumer", "rev": "consumer", "products": [
            P("auto", "Capital One Auto Finance", "$89.3 billion of auto loans, originations up 19% in 2Q26, Auto Navigator for buyers and first in J.D. Power's dealer satisfaction (non-captive subprime).",
              s=["auto"], lc="borrow", neo=[0, ""], src=[["2Q26 supplement", Q2S], ["2Q26 10-Q", Q2Q]]),
        ]},
        {"id": "4.5", "ic": "building-2", "name": "Commercial banking", "blurb": "$91 billion of loans.", "div": "commercial", "rev": "commercial", "products": [
            P("commercial", "Commercial Banking", "Lending, treasury and capital markets for companies with $20 million to $2 billion of revenue; $91.3 billion of loans.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["2Q26 supplement", Q2S]]),
        ]},
        {"id": "4.6", "ic": "network", "name": "The network business", "blurb": "Fees from issuers and acquirers.", "div": "network", "rev": "network", "products": [
            P("networkbiz", "Global Payment Network", "Discover, PULSE and Diners sold to other issuers, acquirers and partner networks; acceptance being pushed in Mexico, the Caribbean, Canada and the UK.",
              s=["fin", "merch"], lc="grow", neo=[0, "Capital One's own network."], src=[["Q2 2026 call", Q2CALL], ["FY2025 10-K", K25]]),
        ]},
        {"id": "4.7", "ic": "code-xml", "name": "Capital One Software", "blurb": "Slingshot, Databolt.", "div": "cof", "rev": "grp", "products": [
            P("software", "Capital One Software", "Slingshot for Snowflake cost and performance and Databolt for tokenising data for AI, sold to companies such as Sanofi and Asics.",
              s=["fin"], lc="beyond", o="B", neo=[0, ""], src=[["Capital One Software", SOFTWARE]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Capital One: the app with Eno, cafés and branches, the airport lounges, Capital One Travel and Shopping, and car dealers.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App & Eno", "blurb": "Digital first.", "div": "cof", "rev": "consumer", "products": [
            P("app", "Capital One app", "The app and website, with Eno built in.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["Capital One: Eno", ENO]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Cafés & branches", "blurb": "60-plus cafés.", "div": "consumer", "rev": "consumer", "products": [
            P("cafes", "Capital One Cafés & branches", "More than 60 cafés, some with branches, and ⚠ about 750 branches in New York, Louisiana, Texas, Maryland, Virginia, New Jersey and Washington DC.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Capital One: local", CAFES], ["FY2025 10-K", K25]]),
        ]},
        {"id": "5.3", "ic": "plane", "name": "Lounges", "blurb": "Top in J.D. Power.", "div": "card", "rev": "card", "products": [
            P("lounges", "Capital One Lounges & Landings", "Lounges at Dallas Fort Worth, Dulles, Denver, Las Vegas and JFK and Landings at Reagan and LaGuardia; joint first in J.D. Power's 2026 lounge study; free for Venture X holders.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["Capital One: lounges, Aug 2026", LOUNGES]]),
        ]},
        {"id": "5.4", "ic": "globe", "name": "Portals", "blurb": "Travel, Shopping, discover.com.", "div": "cof", "rev": "card", "products": [
            P("portals", "Capital One Travel, Shopping & discover.com", "Booking through Capital One Travel, Capital One Shopping's extension, and discover.com, now a Capital One site.",
              s=["con", "aff"], lc="open", neo=[0, ""], src=[["Capital One Shopping", SHOPPING], ["Discover: credit cards", DISCOVER]]),
        ]},
        {"id": "5.5", "ic": "users-round", "name": "Dealers & partners", "blurb": "Car dealers, co-brands.", "div": "consumer", "rev": "consumer", "products": [
            P("dealers", "Dealers & partners", "The car-dealer network through Auto Navigator and Chat Concierge, co-brand retailers, and the network's partner issuers and acquirers.",
              s=["auto", "fin"], lc="open", neo=[0, ""], src=[["Euromoney: Prem Natarajan", AI], ["FY2025 10-K", K25]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Capital One", "blurb": "Renewed, and shrinking.", "products": [
        P("mcatcof", "Mastercard at Capital One", "Mastercard lost about 25 million debit cards to Discover (done early 2026) and the flagship consumer credit originations from February–March 2026. It keeps a renewed credit agreement (January 2026) for 'a large portion' of new accounts, the business cards, Mastercard co-brands, Canada and probably the UK, the unconverted back book, and 'several' services.",
          s=["inv"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Payments Dive: Mastercard renewal, Jan 2026", MCRENEW], ["PaymentsJournal, Mar 2026", MIGRATE]]),
    ]},
    {"id": "pillar-market", "name": "US cards", "blurb": "Third by volume, first by loans.", "products": [
        P("market", "The US card market", "Capital One third by purchase volume in 2025 (about $800 billion with Discover) behind Chase and Amex; the Credit Card Competition Act reintroduced in January 2026 (exempting three-party networks such as Discover); a proposed 10% APR cap; and the Visa/Mastercard merchant settlement.",
          s=["inv"], div="grp", rev="grp", src=[["WTOP: biggest US card companies, Mar 2026", NILSON], ["Congress.gov: S.3623", CCCA]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
