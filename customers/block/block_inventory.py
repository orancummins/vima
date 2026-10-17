"""Block's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Block's own: the Q2 2026 shareholder letter and investor presentation (5 August 2026), the Q1 2026 and
Q4 2025 letters, and the FY2025 10-K (26 February 2026), with Square, Cash App and Afterpay pages and press for the
card programmes. Q3 2026 results are due in early November. ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

Q2L = "https://www.sec.gov/Archives/edgar/data/1512673/000119312526335117/d91486dex991.htm"
Q2P = "https://s29.q4cdn.com/628966176/files/doc_financials/2026/q2/Block-Investor-Presentation-Q2-2026.pdf"
Q2R = "https://s29.q4cdn.com/628966176/files/doc_financials/2026/q2/Intro-Remarks-2Q26.pdf"
Q1L = "https://www.sec.gov/Archives/edgar/data/0001512673/000119312526212032/d132441dex991.htm"
Q4L = "https://www.sec.gov/Archives/edgar/data/1512673/000119312526076557/d108590dex991.htm"
Q3L = "https://www.sec.gov/Archives/edgar/data/1512673/000119312525269715/d48712dex991.htm"
TENK = "https://www.sec.gov/Archives/edgar/data/1512673/000162828026012254/xyz-20251231.htm"
IDAY = "https://businesswire.com/news/home/20251118908846/en/Block-Shares-Multi-Year-Financial-Outlook-at-Investor-Day"
MCAP = "https://companiesmarketcap.com/square/marketcap/"
CAO = "https://www.sec.gov/Archives/edgar/data/1512673/000119312526204101/d112286d8k.htm"
WEBER = "https://www.sec.gov/Archives/edgar/data/1512673/000119312526259540/d140803d8k.htm"
CFPB = "https://www.consumerfinance.gov/about-us/newsroom/cfpb-orders-operator-of-cash-app-to-pay-175-million-and-fix-its-failures-on-fraud/"
FDIC = "https://block.xyz/inside/square-financial-services-receives-FDIC-approval-to-offer-consumer-loan-product-cash-app-borrow"
SQBANK = "https://squareup.com/us/en/banking"
SQCC = "https://squareup.com/us/en/banking/credit-card"
CNBC = "https://www.cnbc.com/2019/01/17/square-takes-another-step-into-banking-with-a-debit-card-for-businesses-.html"
CACARD = "https://cash.app/legal/us/en-us/card-agreement"
MARQETA = "https://www.digitaltransactions.net/marqeta-will-process-for-blocks-cash-app-card-for-another-four-years"
FLEX = "https://www.digitaltransactions.net/afterpay-will-test-flex-payments-with-a-visa-debit-card-klarna-boosts-its-blackhawk-presence/"
AFTERPAYAU = "https://www.afterpay.com/en-AU/help/20249507136025-Which-cards-does-Afterpay-accept"
WESTPAC = "https://www.westpac.com.au/content/dam/public/wbc/documents/pdf/pb/bank-accounts/Afterpay_Apple_Pay_Terms_and_Conditions.pdf"
ANZCARD = "https://www.pymnts.com/bnpl/2021/marqeta-partners-with-afterpay-to-launch-virtual-cards-for-anz-market/"
OCT = "https://digitaltransactions.net/with-a-faster-square-cash-square-ties-fee-based-p2p-to-the-faster-payments-trend/"
INSTANT = "https://community.squareup.com/t5/Archived-Discussions-Read-Only/Instant-Transfer-Which-Cards-are-Supported/m-p/54610"
BTC = "https://squareup.com/us/en/press/square-bitcoin"
UBER = "https://squareup.com/us/en/press/uber-eats-partnership"
SCORE = "https://cash.app/press/cash-app-score-opens-to-lenders-with-nova-as-a-partner"
NBHD = "https://www.americanbanker.com/payments/news/how-block-added-30-000-merchants-to-its-payments-network"
BLOOMBERG = "https://www.bloomberg.com/news/articles/2025-10-10/jack-dorsey-s-block-targets-card-network-fees-in-latest-push"
AGENTIC = "https://www.digitalcommerce360.com/2026/07/01/square-agentic-commerce-integrations-chatgpt-claude/amp/"
KIOSK = "https://squareup.com/us/en/press/square-kiosk-self-service-reimagined"
PRESS = "https://squareup.com/us/en/press"
CASHPRESS = "https://cash.app/press"
AGENTPAY = "https://newsroom.mastercard.com/news/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai"
DTNEWS = "https://www.digitaltransactions.net/news/story/4224"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · bank · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $10.4 billion of gross profit in 2025 and $12.5 billion guided for 2026, a team cut to under 6,000 and run by Jack Dorsey, its own Utah industrial bank, and a plan to make AI the centre of the company.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "$10.4bn gross profit in 2025.", "div": "block", "rev": "grp", "products": [
            P("results", "Results & guidance", "Gross profit of $10.36 billion in 2025 (+17%; Cash App $6.34 billion, Square $3.94 billion) on revenue of $24.19 billion. Q2 2026 gross profit $3.17 billion (+25%) with a record 27% adjusted operating margin; 2026 guidance raised to $12.51 billion. Market value about $47 billion in October 2026.",
              s=["seller", "con"], neo=[0, ""], src=[["Block: Q2 2026 letter", Q2L], ["Block: Q4 2025 letter", Q4L], ["CompaniesMarketCap: Block, Oct 2026", MCAP]]),
        ]},
        {"id": "1.2", "ic": "users-round", "name": "Leadership & people", "blurb": "Dorsey; under 6,000 staff.", "div": "block", "rev": "grp", "products": [
            P("leadership", "Leadership", "Jack Dorsey (co-founder, Block Head and chair), Amrita Ahuja (COO and CFO), Owen Jennings (Business Lead), Thomas Templeton (Hardware Lead) and Andrea Acosta (Chief Accounting Officer from May 2026). Engineering reports to Dorsey since Arnaud Weber left in June 2026.",
              s=["seller", "con"], neo=[0, ""], src=[["Block: Q2 2026 prepared remarks", Q2R], ["Block 8-K, May 2026", CAO], ["Block 8-K, Jun 2026", WEBER]]),
            P("workforce", "AI-native reorganisation", "10,205 staff at the end of 2025; in February 2026 Block cut to just under 6,000 people in smaller, AI-native teams.",
              s=["seller", "con"], st="new", ay="Feb 2026", neo=[0, ""], src=[["Block 10-K FY2025", TENK], ["Block: Q4 2025 letter", Q4L]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Bank & licences", "blurb": "Square Financial Services.", "div": "sfs", "rev": "grp", "products": [
            P("sfs", "Square Financial Services", "A Utah-chartered, FDIC-insured industrial bank owned by Block, which makes Square Loans, holds Square Savings and, since FDIC approval in March 2025, makes Cash App Borrow loans in-house.",
              s=["seller", "con"], neo=[0, ""], src=[["Block 10-K FY2025", TENK], ["Block: FDIC approval, Mar 2025", FDIC]]),
            P("licences", "Licences & regulation", "Money-transmitter licences across the US, a New York BitLicense, a broker-dealer and Australian credit licences. A CFPB order of January 2025 required up to $175 million ($120 million redress, $55 million penalty) over Cash App fraud handling.",
              s=["con"], neo=[0, ""], mc="The CFPB findings show a need for stronger fraud and dispute tools.",
              src=[["Block 10-K FY2025", TENK], ["CFPB: Cash App order, Jan 2025", CFPB]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & targets", "blurb": "$15.8bn by 2028.", "div": "block", "rev": "grp", "products": [
            P("targets", "2028 targets", "Investor Day (November 2025): gross profit growing in the mid-teens to about $15.8 billion in 2028, adjusted operating income to $4.6 billion, adjusted EPS of $5.50, and the Rule of 40 from 2026; a further $5 billion buyback.",
              s=["seller", "con"], neo=[0, ""], src=[["Block: Investor Day, Nov 2025", IDAY]]),
            P("network", "Own network over card rails", "Block is pushing customers to pay from Cash App balances, through Cash App Pay and Neighborhoods, which cuts what it pays in card-network fees ⚠.",
              s=["con", "seller"], st="new", neo=[0, "Designed to bypass card networks."],
              mc="The strategic threat: Block's growth plan routes spend away from every network.",
              src=[["Bloomberg: Block targets card network fees, Oct 2025", BLOOMBERG], ["Block: Q3 2025 letter", Q3L]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Square acquiring at $250 billion a year, seller cards on Mastercard and Amex, the Cash App Card on Visa, Afterpay instalments, P2P and instant transfers to any debit card, and Cash App Pay with bitcoin and USDC off the networks.",
    "tiles": [
        {"id": "2.1", "ic": "store", "name": "Square payments", "blurb": "$250bn GPV, every network.", "div": "square", "rev": "square", "products": [
            P("acquiring", "Square payments", "Card-present and online acceptance of Visa, Mastercard, American Express, Discover and others for more than 4.5 million sellers: $250.5 billion of GPV in 2025 and $72.8 billion in Q2 2026 (+13%), with international markets 22% of the total.",
              s=["seller", "chain"], lc="move", neo=[1, "Accepts every network."], src=[["Block 10-K FY2025", TENK], ["Block: Q2 2026 investor presentation", Q2P]]),
            P("sqbitcoin", "Square Bitcoin", "Sellers take bitcoin at checkout and can convert sales to bitcoin (October 2025), with no processing fee through 2026 and 1% from 2027; US only, not New York.",
              s=["seller", "btc"], lc="move", st="new", ay="Oct 2025", neo=[0, "Off the card networks."], src=[["Square: Square Bitcoin, Oct 2025", BTC]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Seller cards", "blurb": "Mastercard debit, Amex credit.", "div": "square", "rev": "square", "products": [
            P("sqdebit", "Square Debit Card", "A free Mastercard business debit card launched in January 2019 and issued by Sutton Bank, spending Square sales straight from Square Checking.", short="Square Debit Card",
              s=["seller"], lc="everyday", ay="Jan 2019", o="P", at="Sutton Bank", neo=[2, "Mastercard."],
              mc="Block's one card programme on Mastercard.",
              src=[["Square: banking", SQBANK], ["CNBC: Square Card, Jan 2019", CNBC]]),
            P("sqcredit", "Square Credit Card", "A metal business credit card issued by Celtic Bank on American Express: 1.5% cash back, no fees ⚠ launch date not confirmed.",
              s=["seller"], lc="borrow", o="P", at="Celtic Bank", neo=[0, "American Express."], src=[["Square: credit card", SQCC]]),
        ]},
        {"id": "2.3", "ic": "wallet-cards", "name": "Cash App Card", "blurb": "26m actives on Visa.", "div": "cashapp", "rev": "cash", "products": [
            P("cashcard", "Cash App Card", "A Visa debit card issued by Sutton Bank and processed by Marqeta (renewed through June 2027). It had 26 million monthly actives in Q3 2025 and is a main driver of Cash App's gross profit growth.", short="Cash App Card",
              s=["con"], lc="everyday", o="P", at="Sutton Bank, Marqeta", neo=[0, "Visa."],
              mc="Block's largest consumer card is Visa's.",
              src=[["Cash App: card agreement", CACARD], ["Block: Q3 2025 letter", Q3L], ["Digital Transactions: Marqeta renewal, Aug 2023", MARQETA]]),
            P("tags", "Cash App Tags", "NFC tap-to-pay tags launched in Q2 2026 with 'a foundation for agentic commerce built in'. The network behind them is not stated ⚠.",
              s=["con", "seller"], lc="move", st="new", ay="2026", neo=[None, "Network not stated."], src=[["Block: Q2 2026 letter", Q2L]]),
        ]},
        {"id": "2.4", "ic": "hand-coins", "name": "Afterpay BNPL", "blurb": "Pay in 4, on the card.", "div": "afterpay", "rev": "cash", "products": [
            P("afterpay", "Afterpay Pay in 4 & Pay Monthly", "Buy now, pay later in the US, Australia, Canada, New Zealand and the UK (Clearpay). Customers repay with Mastercard and Visa cards issued in their own country. BNPL GMV was $9.7 billion in Q3 2025.",
              s=["shop"], lc="borrow", o="A", neo=[1, "Repaid on Mastercard and Visa cards."], src=[["Block 10-K FY2025", TENK], ["Afterpay AU: accepted cards", AFTERPAYAU], ["Block: Q3 2025 letter", Q3L]]),
            P("flex", "Afterpay on the Cash App Card", "Post-purchase BNPL on the Cash App Card passed $3 billion annualised in October 2025. A Visa Debit Flex Card pilot (Sutton Bank and The Bancorp) was announced in November 2025, and Pre-Purchase reached general availability in Q2 2026, at 17% of eligible card spend.", short="Afterpay on Cash App Card",
              s=["shop", "con"], lc="borrow", st="new", ay="Nov 2025", o="P", at="Visa", neo=[0, "Visa Flex."],
              mc="Instalments on a Visa flexible credential; Mastercard's instalment tools are not used.",
              src=[["Digital Transactions: Visa Debit Flex pilot, Nov 2025", FLEX], ["Block: Q2 2026 letter", Q2L]]),
            P("afterpaycard", "Afterpay Card abroad", "In Australia a 2021 Westpac-issued Afterpay card ran on Mastercard or eftpos, and Marqeta issued in-store virtual cards for Australia and New Zealand from May 2021. The current network is not confirmed ⚠.",
              s=["shop"], lc="move", st="unconf", ay="2021", o="P", at="Westpac, Marqeta", neo=[1, "Mastercard or eftpos in 2021 ⚠."],
              src=[["Westpac: Afterpay Apple Pay terms, 2021", WESTPAC], ["PYMNTS: Marqeta and Afterpay, May 2021", ANZCARD]]),
        ]},
        {"id": "2.5", "ic": "send", "name": "P2P & instant transfers", "blurb": "Push to any debit card.", "div": "cashapp", "rev": "cash", "products": [
            P("p2p", "Cash App P2P", "Free person-to-person payments between Cash App users. These help bring in $316 billion of inflows a year (2025) and 9.4 million accounts that receive paychecks or spend heavily.",
              s=["con"], lc="move", neo=[0, "Inside Cash App."], src=[["Block 10-K FY2025", TENK], ["Block: Q2 2026 investor presentation", Q2P]]),
            P("instant", "Instant transfers & Instant Deposit", "Cash App and Square push funds instantly to external Visa and Mastercard debit cards using original credit transactions (OCT). Whether Mastercard Send or Move is used is not stated ⚠.",
              s=["con", "seller"], lc="move", neo=[1, "OCT to Mastercard and Visa debit ⚠."],
              mc="Payout volume Mastercard Move could compete for with Visa Direct.",
              src=[["Digital Transactions: Square Cash OCT", OCT], ["Square Community: Instant Transfer cards", INSTANT]]),
        ]},
        {"id": "2.6", "ic": "coins", "name": "Cash App Pay & digital money", "blurb": "Balances, bitcoin, USDC.", "div": "cashapp", "rev": "cash", "products": [
            P("cashapppay", "Cash App Pay", "Pay from a Cash App balance at checkout. Uber and Uber Eats were added in the US in April 2026, alongside Instacart and Grubhub.",
              s=["con", "chain"], lc="move", st="new", neo=[0, "Closed loop on balances ⚠."],
              mc="Spend that would otherwise run on a card.",
              src=[["Square: Uber partnership, Apr 2026", UBER], ["Block: Q2 2026 letter", Q2L]]),
            P("cashbitcoin", "Bitcoin & USDC on Cash App", "Buy, sell and send bitcoin, with fees cut in 2026; USDC was added in Q2 2026, usable in the same way as dollar balances. Bitcoin revenue was $1.89 billion in Q2 2026.",
              s=["con", "btc"], lc="beyond", st="new", neo=[0, "Off the card networks."],
              mc="Mastercard's BVNK unit launched Mastercard Global Money for stablecoins in October 2026.",
              src=[["Block: Q2 2026 letter", Q2L], ["Digital Transactions, Oct 2026", DTNEWS]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every payment: fraud controls under a CFPB order, a cash-flow credit score now sold to lenders, Moneybot and Managerbot, the Neighborhoods loyalty network, and Square selling inside ChatGPT and Claude.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & risk", "blurb": "Under a CFPB order.", "div": "cashapp", "rev": "cash", "products": [
            P("fraud", "Fraud & disputes", "Cash App's own fraud and dispute controls, under a January 2025 CFPB order that found weak security and incomplete investigations of unauthorised transfers. No Mastercard fraud tools have been found ⚠.",
              s=["con", "seller"], lc="everyday", neo=[None, "No public tools."],
              mc="Consumer Clarity and Ethoca could help with disputes.",
              src=[["CFPB: Cash App order, Jan 2025", CFPB]]),
        ]},
        {"id": "3.2", "ic": "gauge", "name": "Credit data", "blurb": "Cash App Score.", "div": "cashapp", "rev": "cash", "products": [
            P("score", "Cash App Score", "A near real-time credit score built from cash flow, which customers can see in the app. It runs Block's lending, and from September 2026 is offered to outside lenders through Nova Credit; 55% of customers come back to check it within 30 days.",
              s=["con"], lc="borrow", st="new", ay="Sep 2026", o="P", at="Nova Credit", neo=[0, ""],
              mc="Mastercard Open Finance offers a similar cash-flow data service.",
              src=[["Cash App: Score and Nova Credit, Sep 2026", SCORE]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "AI", "blurb": "Moneybot, Managerbot, goose.", "div": "block", "rev": "grp", "products": [
            P("moneybot", "Moneybot", "Cash App's proactive money assistant: generally available, with over 1 million weekly engaged accounts (Q2 2026).",
              s=["con"], lc="everyday", st="new", neo=[0, ""], src=[["Block: Q2 2026 letter", Q2L]]),
            P("managerbot", "Managerbot & Square AI", "An AI agent that runs operations for Square sellers. It reached over 1 million sellers, with US general availability from June 2026; Square AI added business insights in October 2025.",
              s=["seller"], lc="grow", st="new", neo=[0, ""], src=[["Block: Q1 2026 letter", Q1L], ["Square press", PRESS]]),
            P("goose", "goose, Builderbot & Buzz", "In-house agent tools: goose (open source, since early 2024); Builderbot, which makes about 15% of production code changes; and Buzz, launched publicly in July 2026.",
              s=["dev"], lc="beyond", st="new", neo=[0, ""], src=[["Block: Q1 2026 letter", Q1L], ["Block: Q2 2026 prepared remarks", Q2R]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Neighborhoods & loyalty", "blurb": "$1bn annualised GPV.", "div": "square", "rev": "square", "products": [
            P("neighborhoods", "Neighborhoods", "A loyalty network that links Square sellers with Cash App's 59 million actives. Customers earn local cash of 10% of an order, up to $10, and sellers pay 1% on in-app orders. Sellers on it reached $1 billion of annualised GPV in June 2026, and 30,000 joined by September.",
              s=["seller", "con"], lc="grow", st="new", ay="2025", neo=[0, "Block's own network."],
              mc="An offers network built outside the card schemes.",
              src=[["Block: Q2 2026 letter", Q2L], ["American Banker: Neighborhoods, Sep 2026", NBHD], ["Block: Q3 2025 letter", Q3L]]),
            P("green", "Cash App Green", "A status programme that rewards customers who bank with Cash App, and the group Cash App Borrow was opened to (2026).",
              s=["con"], lc="everyday", st="new", neo=[0, ""], src=[["Block: Q1 2026 letter", Q1L]]),
        ]},
        {"id": "3.5", "ic": "sparkles", "name": "Agentic commerce", "blurb": "ChatGPT, Claude, UCP.", "div": "square", "rev": "square", "products": [
            P("agentic", "Square in AI assistants", "Square apps went live in ChatGPT and Claude on 1 July 2026 for US food and beverage sellers. Square takes part in UCP and is working with Amazon on Alexa+. No link to Mastercard Agent Pay has been found ⚠.",
              s=["seller", "con"], lc="grow", st="new", ay="Jul 2026", neo=[0, "UCP, not Agent Pay."],
              mc="Agent Pay could carry these orders on agentic tokens.",
              src=[["Digital Commerce 360: Square agentic, Jul 2026", AGENTIC], ["Mastercard: Agent Pay, Apr 2025", AGENTPAY]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What Block sells: Square software for millions of sellers, seller banking and loans, Cash App banking for 9.4 million primary customers, Cash App Borrow, and bitcoin, Proto, Bitkey and TIDAL.",
    "tiles": [
        {"id": "4.1", "ic": "monitor", "name": "Square software", "blurb": "POS for every vertical.", "div": "square", "rev": "square", "products": [
            P("software", "Square point of sale & software", "One point-of-sale app (April 2025) with restaurant, retail, and beauty and wellness software, AI voice ordering and simpler pricing (October 2025). Square gross profit was $1.16 billion in Q2 2026 (+13%).",
              s=["seller", "chain"], lc="everyday", neo=[0, ""], src=[["Block: Q2 2026 investor presentation", Q2P], ["Block: Q4 2025 letter", Q4L], ["Square press", PRESS]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Seller banking & loans", "blurb": "$300m a quarter.", "div": "sfs", "rev": "square", "products": [
            P("sqbanking", "Square Checking & Savings", "Square Checking (Sutton Bank) with instant access to sales and the Mastercard debit card, and Square Savings at Square Financial Services earning up to 4.25%.",
              s=["seller"], lc="everyday", o="P", at="Sutton Bank", neo=[1, "Its debit card is Mastercard."], src=[["Square: banking", SQBANK]]),
            P("sqloans", "Square Loans", "Loans to sellers, repaid from sales, made by Square Capital and Square Financial Services. Square Financial Solutions (loans, Instant Deposit, Square Card) made $300 million of gross profit in Q2 2026 (+22%).",
              s=["seller"], lc="borrow", neo=[0, ""], src=[["Block: Q2 2026 investor presentation", Q2P], ["Square: banking", SQBANK]]),
        ]},
        {"id": "4.3", "ic": "wallet", "name": "Cash App banking", "blurb": "9.4m primary actives.", "div": "cashapp", "rev": "cash", "products": [
            P("cashbanking", "Cash App banking", "Paycheck deposits, savings, managed accounts for children aged 6–12 (April 2026) and Cash App Mobile at $40 a month. There were 9.4 million primary banking actives in June 2026 (+17%), and inflows per active were $1,494.",
              s=["con"], lc="everyday", neo=[0, "Spending runs on the Visa card."], src=[["Block: Q2 2026 investor presentation", Q2P], ["Block: Q2 2026 letter", Q2L], ["Block: Q1 2026 letter", Q1L]]),
        ]},
        {"id": "4.4", "ic": "hand-coins", "name": "Cash App Borrow", "blurb": "$18.9bn lending a quarter.", "div": "sfs", "rev": "cash", "products": [
            P("borrow", "Cash App Borrow", "Small short-term loans averaging under $100 for about a month, made by Square Financial Services since FDIC approval in March 2025. Borrow and BNPL originated $18.9 billion in Q2 2026 (+59%).",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Block: FDIC approval, Mar 2025", FDIC], ["Block: Q2 2026 investor presentation", Q2P]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Bitcoin, Proto, Bitkey & TIDAL", "blurb": "Beyond payments.", "div": "proto", "rev": "other", "products": [
            P("proto", "Proto & Bitkey", "Proto designs bitcoin mining chips and rigs, and its first units have shipped. Bitkey is a self-custody bitcoin wallet combining an app, a hardware device and recovery options.",
              s=["btc"], lc="beyond", st="new", neo=[0, ""], src=[["Block: Q4 2025 letter", Q4L], ["Block 10-K FY2025", TENK]]),
            P("investing", "Cash App Investing", "Stock investing through Cash App Investing LLC, an SEC-registered broker-dealer.",
              s=["con"], lc="grow", neo=[0, ""], src=[["Block 10-K FY2025", TENK]]),
            P("tidal", "TIDAL", "A majority-owned music streaming service with more than 250 million songs and listeners in over 60 countries.",
              s=["con"], lc="beyond", div="tidal", o="A", neo=[0, ""], src=[["Block 10-K FY2025", TENK]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Block: the Cash App and Afterpay apps, Square's own hardware from Handheld to the new Kiosk, and a sales push through more than 200 ISO partners and platforms such as Uber, OpenTable, Google and Apple.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "Cash App, Afterpay, Square.", "div": "cashapp", "rev": "grp", "products": [
            P("apps", "Cash App, Afterpay & Square apps", "Cash App had 59 million monthly transacting actives in June 2026, alongside the Afterpay app, the Square POS app and Dashboard, and twice-yearly Square and Cash App Releases.",
              s=["con", "seller", "shop"], lc="open", neo=[0, ""], src=[["Block: Q2 2026 letter", Q2L], ["Square press", PRESS], ["Cash App press", CASHPRESS]]),
        ]},
        {"id": "5.2", "ic": "factory", "name": "Hardware", "blurb": "Register, Handheld, Kiosk.", "div": "square", "rev": "square", "products": [
            P("hardware", "Square hardware", "Square Handheld (May 2025), the second-generation Register (February 2026) and Square Kiosk (14 October 2026), which has an agentic voice layer and takes tap and dip payments without extra devices.",
              s=["seller", "chain"], lc="open", st="new", neo=[1, "Takes every network's cards."], src=[["Square: Kiosk, Oct 2026", KIOSK], ["Square press", PRESS]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Sales & partners", "blurb": "200+ ISOs, Uber, Google.", "div": "square", "rev": "square", "products": [
            P("iso", "Field sales & ISOs", "Self-serve sign-up, a field sales team and more than 200 active ISO partners. New sellers from the ISO channel grew more than 150% quarter on quarter in Q2 2026.",
              s=["seller", "chain"], lc="open", st="new", neo=[0, ""],
              mc="New ISO sellers need merchant screening such as MATCH.",
              src=[["Block: Q2 2026 prepared remarks", Q2R]]),
            P("partners", "Platform partners", "Uber (Square–Uber Eats integration in six more countries; Cash App Pay on Uber, April 2026), OpenTable (August 2026), Google Maps ordering (August 2026), Apple Business (September 2026) and the Sherwin-Williams Digital Alliance (June 2026).",
              s=["seller", "chain"], lc="grow", st="new", o="P", neo=[0, ""], src=[["Square: Uber partnership, Apr 2026", UBER], ["Square press", PRESS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Block", "blurb": "Seller debit, acceptance, payouts.", "products": [
        P("mcatblock", "Mastercard at Block", "Mastercard runs the Square Debit Card and is accepted everywhere Square and Afterpay take payments. It is also one of the two debit networks Block pushes instant transfers to. Visa holds the Cash App Card (26 million actives) and Afterpay's Flex pilot, and American Express holds the Square Credit Card. Block is moving more spending onto its own balances and Neighborhoods network.",
          s=["seller", "con"], div="block", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Square: banking", SQBANK], ["Cash App: card agreement", CACARD], ["Digital Transactions: Visa Debit Flex pilot, Nov 2025", FLEX]]),
    ]},
    {"id": "pillar-market", "name": "US payments & fintech", "blurb": "Toast, Clover, PayPal, Chime.", "products": [
        P("market", "The market", "Square competes with Clover, Toast, Stripe and Shopify for sellers. Cash App competes with PayPal and Venmo, Chime and Zelle for consumers, and Afterpay with Affirm and Klarna ⚠. The CFPB is active, stablecoin rules are new, and card fees face pressure.",
          s=["seller", "con"], div="block", rev="grp", src=[["Block 10-K FY2025", TENK]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
