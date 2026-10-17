"""Affirm Holdings' layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Affirm's own unless a source says otherwise: the fiscal Q4 2026 results (27 August 2026) and the
FY2026 10-K (year to 30 June 2026), with Affirm's product pages and partner releases. Fiscal Q1 2027 results
had not been released. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

TENK = "https://www.sec.gov/Archives/edgar/data/0001820953/000162828026059279/afrm-20260630.htm"
EIGHTK = "https://www.sec.gov/Archives/edgar/data/0001820953/000162828026059271/afrm-20260825.htm"
Q4CFI = "https://www.crowdfundinsider.com/2026/08/302674-bnpl-fintech-affirm-beats-revenue-estimates-and-lifts-outlook-as-afrm-stock-surge-in-after-hours/"
PULSE = "https://pulse2.com/affirm-revenue-less-transaction-costs-jumps-39-as-gmv-rises-36-and-operating-margin-reaches-13/"
CALL = "https://www.webull.com/news/15497663754789888"
MCAP = "https://stockanalysis.com/stocks/afrm/market-cap/"
WIKI = "https://en.wikipedia.org/wiki/Affirm_Holdings"
CARD = "https://www.affirm.com/card"
VCN = "https://docs.affirm.com/payments/docs/vcn-overview"
VISAFLEX = "https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.20966.html"
STRIDE = "https://www.nasdaq.com/press-release/stride-bank-announces-program-partnership-affirm-2025-04-01"
FISERV = "https://www.pymnts.com/bnpl/2026/affirm-and-fiserv-team-to-bring-bnpl-to-debit-programs/"
FISERVPR = "https://www.nasdaq.com/press-release/fiserv-and-affirm-join-forces-bring-flexible-payments-debit-2026-01-26"
BANK = "https://investors.affirm.com/news-releases/news-release-details/affirm-submits-applications-establish-industrial-loan-company"
BANKCFI = "https://www.crowdfundinsider.com/2026/01/258066-bnpl-fintech-affirm-advances-plans-for-banking-subsidiary-to-enhance-financial-services/"
AP2 = "https://www.businesswire.com/news/home/20251009636704/en/Affirm-extends-collaboration-with-Google-as-a-supporter-of-Agent-Payments-Protocol-AP2"
APPLEPAY = "https://www.nasdaq.com/articles/affirm-unveils-store-pay-later-option-through-apple-pay"
UK = "https://thepaypers.com/payments/news/affirm-introduces-pay-over-time-options-in-the-uk"
SHOPIFY = "https://www.tipranks.com/news/the-fly/affirm-shopify-expand-global-agreement"
WALMART = "https://www.paymentsdive.com/news/affirm-coo-walmart-deal-was-uneconomic/743944/"
Q1FY26 = "https://www.digitaltransactions.net/affirms-results-boost-its-bnpl-ranking/"
AMZ2021 = "https://www.digitaltransactions.net/a-fast-growing-affirm-looks-to-supercharge-its-expansion-with-an-exclusive-amazon-deal/"
CPP = "https://investors.affirm.com/news-releases/news-release-details/affirm-and-cpp-investments-renew-and-expand-capital-partnership"
NYL = "https://secure.businesswire.com/news/home/20251031384145/en/Affirm-expands-long-term-capital-partnership-with-New-York-Life-to-increase-access-to-flexible-and-transparent-payment-options"
MCGW = "https://developer.mastercard.com/mastercard-gateway/documentation/payment-methods/alt-pay-methods/a2a/affirm/"
MCINST = "https://www.nasdaq.com/articles/mastercards-stability-vs-affirms-velocity-which-has-more-upside"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · licences · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $50.2 billion of GMV in FY2026 for 27.8 million shoppers, a founder-led company lending through partner banks, a proposed Affirm Bank, and $30 billion of funding capacity.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "$50.2bn GMV, FY2026.", "div": "grp", "rev": "grp", "products": [
            P("results", "Volume & earnings", "FY2026 (to 30 June 2026): GMV $50.2 billion (+about 37%), revenue $4.26 billion, operating income $147 million. Q4 FY2026: GMV $14.1 billion (+36%), revenue about $1.17 billion (+33%), revenue less transaction costs $589 million (+39%), GAAP operating margin 13%. Market value $24.97 billion at 16 October 2026.",
              s=["inv"], neo=[0, ""], src=[["Crowdfund Insider: Q4 FY2026 results, Aug 2026", Q4CFI], ["Pulse 2.0: Q4 FY2026, Aug 2026", PULSE], ["StockAnalysis: AFRM market cap", MCAP]]),
            P("consumers", "Shoppers & merchants", "27.8 million active consumers (+21%) at 30 June 2026, about 7.0 transactions each a year, with repeat shoppers behind 96% of transactions; about 571,000 active merchants (+50%+); 2,358 staff.",
              s=["shop", "merch"], neo=[0, ""], src=[["Affirm 10-K FY2026", TENK], ["Crowdfund Insider: Q4 FY2026 results, Aug 2026", Q4CFI]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Levchin, two presidents.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Board & executives", "Max Levchin, founder, chair and CEO; Michael Linford, President from 27 August 2026 (previously COO and CFO); Libor Michalek, President for engineering, risk, product and operations; Rob O'Hare, CFO since November 2024; Pat Suh, head of global markets ⚠ single source. Class B shares carry 15 votes each.",
              s=["inv"], st="new", neo=[0, ""], src=[["Affirm 8-K, Aug 2026", EIGHTK], ["Affirm 10-K FY2026", TENK], ["Crowdfund Insider: Q4 FY2026 results, Aug 2026", Q4CFI]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Partner banks & licences", "blurb": "Celtic, Lead, Cross River.", "div": "affirm", "rev": "interest", "products": [
            P("partnerbanks", "Partner banks", "Celtic Bank and Lead Bank originate substantially all US partner-bank loans (rates up to 36%); Cross River Bank originates some (up to 30%) and holds Affirm Money deposits; Evolve Bank & Trust and Stride Bank issue the Affirm Card.",
              s=["shop"], o="P", at="Celtic, Lead, Cross River, Evolve, Stride", neo=[0, ""], src=[["Affirm 10-K FY2026", TENK], ["Affirm Card", CARD]]),
            P("licences", "Licences", "Affirm Payments, LLC holds state money-transmitter licences and is a FinCEN money services business; lending licences across US states and Canada; Affirm U.K. Limited is FCA-authorised; Affirm Australia holds an ASIC credit licence. Reincorporated in Nevada on 1 July 2025.",
              s=["shop"], neo=[0, ""], src=[["Affirm 10-K FY2026", TENK]]),
        ]},
        {"id": "1.4", "ic": "building-2", "name": "Affirm Bank", "blurb": "Nevada charter, pending.", "div": "bank", "rev": "interest", "products": [
            P("affirmbank", "Affirm Bank (proposed)", "A Nevada-chartered, FDIC-insured industrial loan company, applied for on 23 January 2026, with John Marion as president. Industry and advocacy groups oppose it; no decision found.",
              s=["shop", "bank"], st="new", ay="Jan 2026", neo=[None, "Network choice not public."],
              mc="A chartered bank could issue cards directly and pick its own network.",
              src=[["Affirm: Affirm Bank applications, Jan 2026", BANK], ["Crowdfund Insider: Affirm Bank, Jan 2026", BANKCFI], ["Affirm 10-K FY2026", TENK]]),
        ]},
        {"id": "1.5", "ic": "coins", "name": "Funding", "blurb": "$30bn of capacity.", "div": "grp", "rev": "loans", "products": [
            P("funding", "Funding capacity", "$30 billion of capacity at 30 June 2026 (up from $26.1 billion), from warehouse lines, securitisations, master trusts and forward flow; management says it could support more than $70 billion of annual GMV. Net cash about $1.5 billion.",
              s=["inv"], neo=[0, ""], src=[["Pulse 2.0: Q4 FY2026, Aug 2026", PULSE], ["Affirm 10-K FY2026", TENK]]),
            P("forwardflow", "Forward-flow partners", "CPP Investments renewed for 24 months in June 2026, $1.7 billion rising to $2.2 billion, about $8 billion of loans; New York Life expanded in October 2025. Two off-balance-sheet ABS deals in FY2026.",
              s=["inv"], o="P", at="CPP Investments, New York Life", neo=[0, ""], src=[["Affirm: CPP Investments, Jun 2026", CPP], ["Affirm: New York Life, Oct 2025", NYL], ["Q4 FY2026 earnings call", CALL]]),
        ]},
        {"id": "1.6", "ic": "target", "name": "Strategy & deals", "blurb": "A payment network.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "Strategy", "Build 'the next generation payment network' from pay-over-time, the Affirm Card and Affirm Money; grow 0% and Pay-in-X with merchant funding; reach banks through Fiserv and Affirm Edge; expand to the UK, Australia and then the Netherlands, France and Germany.",
              s=["inv"], neo=[0, ""], src=[["Affirm 10-K FY2026", TENK], ["Q4 FY2026 earnings call", CALL]]),
            P("deals", "Deals since 2020", "Nasdaq listing in January 2021 (about $1.2 billion raised); Returnly ($300 million, 2021); PayBright in Canada (2021) ⚠; lost Walmart's exclusive to Klarna in March 2025 (about 5% of GMV).",
              s=["inv"], o="A", neo=[0, ""], src=[["Wikipedia: Affirm Holdings", WIKI], ["Payments Dive: Walmart, Mar 2025", WALMART]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Five ways money moves: Affirm's own pay-over-time loans, the Affirm Card on Visa, one-time Visa virtual cards behind Apple Pay and Google Pay, merchant settlement and repayments, and plans on banks' own debit cards through Fiserv.",
    "tiles": [
        {"id": "2.1", "ic": "hand-coins", "name": "Pay over time", "blurb": "Monthly, Pay in 4, 0%.", "div": "affirm", "rev": "interest", "products": [
            P("monthly", "Monthly instalments", "Interest-bearing monthly plans at 0–36% APR with no late fees: 70% of FY2026 GMV. Over 80% of direct-to-consumer loans carry interest.",
              s=["shop"], lc="borrow", neo=[0, "Affirm's own credit, off the card networks."], src=[["Affirm 10-K FY2026", TENK], ["Affirm Card", CARD], ["Q4 FY2026 earnings call", CALL]]),
            P("payin4", "Pay in 4 (Pay-in-X)", "Up to four interest-free payments: 16% of FY2026 GMV, growing 41% in Q4 FY2026.",
              s=["shop"], lc="borrow", neo=[0, "Affirm's own credit, off the card networks."], src=[["Affirm 10-K FY2026", TENK], ["Crowdfund Insider: Q4 FY2026 results, Aug 2026", Q4CFI]]),
            P("zeroapr", "0% APR monthly", "Merchant-funded interest-free monthly plans: 14% of FY2026 GMV; the 'Big Nothing' promotion lifted the 0% share in Q4.",
              s=["shop", "ent"], lc="grow", neo=[0, "Merchant-funded, off the card networks."], src=[["Affirm 10-K FY2026", TENK], ["Q4 FY2026 earnings call", CALL]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Affirm Card", "blurb": "Visa debit, 5.2m users.", "div": "card", "rev": "card", "products": [
            P("affirmcard", "Affirm Card (Visa debit)", "A Visa debit card issued by Evolve Bank & Trust or Stride Bank: pay in full, or move a purchase to a plan in the app. 5.2 million active cardholders (+125%) and $2.8 billion of Q4 FY2026 GMV; 30% of card transactions are in store.", short="Affirm Card (Visa)",
              s=["card"], lc="everyday", o="P", at="Evolve, Stride, Visa", neo=[0, "Visa."],
              mc="Affirm's fastest-growing product is a Visa card.",
              src=[["Affirm Card", CARD], ["Crowdfund Insider: Q4 FY2026 results, Aug 2026", Q4CFI], ["Stride Bank and Affirm, Apr 2025", STRIDE]]),
            P("visaflex", "Visa Flexible Credential", "The Affirm Card was Visa's first US Flexible Credential partner (12 November 2024), switching between debit and pay-over-time on one card; it had more than 1.4 million users then.",
              s=["card"], lc="everyday", st="new", ay="Nov 2024", o="P", at="Visa", neo=[0, "Visa."],
              src=[["Visa: Flexible Credential goes global, Nov 2024", VISAFLEX], ["Q4 FY2026 earnings call", CALL]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Virtual cards & wallets", "blurb": "Visa cards behind wallets.", "div": "payments", "rev": "card", "products": [
            P("vcn", "Affirm virtual cards", "One-time-use Visa cards for an approved loan, used in store, by phone and in wallets; issued by Cross River, Sutton or Celtic, on Visa USA and Visa Canada BINs.",
              s=["shop", "merch"], lc="move", o="P", at="Cross River, Sutton, Celtic", neo=[0, "Visa."], src=[["Affirm docs: virtual cards", VCN], ["Affirm Card", CARD]]),
            P("applepay", "Affirm in Apple Pay", "Pay over time inside Apple Pay online (from 2024) and in store in the US (from 15 September 2025, iOS 26).",
              s=["shop"], lc="move", st="new", ay="Sep 2025", o="P", at="Apple", neo=[0, "Visa virtual cards ⚠."], src=[["Nasdaq: Affirm in-store with Apple Pay, Sep 2025", APPLEPAY], ["Wikipedia: Affirm Holdings", WIKI]]),
            P("googlepay", "Affirm in Google Pay", "Affirm offered at Google Pay checkout after a pilot in 2024; virtual cards carry their own Google Pay BINs.",
              s=["shop"], lc="move", o="P", at="Google", neo=[0, "Visa virtual cards ⚠."], src=[["Wikipedia: Affirm Holdings", WIKI], ["Affirm docs: virtual cards", VCN]]),
        ]},
        {"id": "2.4", "ic": "arrow-left-right", "name": "Settlement & repayment", "blurb": "Affirm pays merchants.", "div": "payments", "rev": "merchant", "products": [
            P("settlement", "Merchant settlement", "Affirm pays the merchant and takes the credit risk; merchants pay a fee (merchant network revenue). Revenue less transaction costs about 4.2% of GMV.",
              s=["merch"], lc="move", neo=[0, "Settled by Affirm, off the card networks ⚠."], src=[["Affirm 10-K FY2026", TENK], ["Q4 FY2026 earnings call", CALL]]),
            P("repay", "Repayments", "Shoppers repay in the app from a bank account or a debit card ⚠ networks not stated.",
              s=["shop"], lc="move", neo=[None, "Debit networks not stated."], src=[["Affirm Card", CARD]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Plans on bank debit", "blurb": "Fiserv, January 2026.", "div": "affirm", "rev": "interest", "products": [
            P("fiservdebit", "Affirm on bank debit cards (Fiserv)", "Exclusive with Fiserv from 26 January 2026: US banks and credit unions offer Affirm plans in their own app, and an approved plan attaches to the customer's existing debit card. Affirm underwrites, originates and funds.",
              s=["bank", "shop"], lc="borrow", st="new", ay="Jan 2026", o="P", at="Fiserv", neo=[1, "On banks' own debit cards, Mastercard or Visa ⚠ networks not named."],
              mc="Plans on bank-issued debit cards sit next to Mastercard Installments.",
              src=[["PYMNTS: Affirm and Fiserv, Jan 2026", FISERV], ["Fiserv and Affirm, Jan 2026", FISERVPR]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every loan: real-time underwriting on about 100 million requests a quarter, merchant promotion tools, agentic commerce with Google's AP2, and Affirm Edge for banks.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Underwriting & risk", "blurb": "100m requests a quarter.", "div": "affirm", "rev": "interest", "products": [
            P("underwriting", "Real-time underwriting", "Affirm decides each loan in real time, about 100 million transaction requests a quarter, with no late fees and fixed interest.",
              s=["shop", "bank"], lc="borrow", neo=[0, "Affirm's own models."], src=[["Q4 FY2026 earnings call", CALL], ["Affirm 10-K FY2026", TENK]]),
            P("fraud", "Fraud & identity", "Run in-house; no outside vendor is named ⚠.",
              s=["shop"], lc="borrow", neo=[None, "Nothing public."],
              mc="Identity and fraud tools fit a lender making 100 million decisions a quarter.",
              src=[["Affirm 10-K FY2026", TENK]]),
        ]},
        {"id": "3.2", "ic": "gift", "name": "Merchant promotions", "blurb": "Merchant-funded 0%.", "div": "affirm", "rev": "merchant", "products": [
            P("adaptive", "Adaptive Checkout", "Shows each shopper pre-approved plans tailored to the basket, bi-weekly or monthly.",
              s=["merch"], lc="grow", neo=[0, ""], src=[["Wikipedia: Affirm Holdings", WIKI]]),
            P("adaptai", "AdaptAI & BoostAI", "AI tools that let merchants fund 0% APR, special terms or savings and test them automatically; management likens 0% offers on the card to 8–15% cash back.",
              s=["merch", "ent"], lc="grow", st="new", ay="2025", neo=[0, ""], src=[["Wikipedia: Affirm Holdings", WIKI], ["Q4 FY2026 earnings call", CALL]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "Agentic commerce", "blurb": "Google AP2.", "div": "affirm", "rev": "merchant", "products": [
            P("ap2", "Google AP2", "Affirm backs Google's Agent Payments Protocol (9 October 2025), so its plans can be offered inside AI agents; Mastercard is also an AP2 supporter.",
              s=["shop", "ent"], lc="grow", st="new", ay="Oct 2025", o="P", at="Google", neo=[0, "Google's protocol."],
              mc="Agent Pay could carry Affirm plans in agent checkouts.",
              src=[["Affirm and Google AP2, Oct 2025", AP2]]),
        ]},
        {"id": "3.4", "ic": "plug", "name": "Affirm Edge", "blurb": "Bank programmes, pilots.", "div": "affirm", "rev": "interest", "products": [
            P("edge", "Affirm Edge", "A platform for bank partners to run their own financing programmes on Affirm's technology; first pilots expected in the second half of FY2027.",
              s=["bank"], lc="open", st="new", ay="2026", neo=[None, "Network not public."], src=[["Q4 FY2026 earnings call", CALL]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What Affirm sells: consumer loans on a book of 553 million loans to date, the card and Affirm Money, a 571,000-merchant network, enterprise partners from Amazon to Shopify, and Canada, the UK and Australia.",
    "tiles": [
        {"id": "4.1", "ic": "chart-column", "name": "Loan book", "blurb": "553m loans to date.", "div": "affirm", "rev": "interest", "products": [
            P("loanbook", "Consumer loans", "About 553 million loans facilitated to date; FY2026 GMV 70% interest-bearing, 14% 0% monthly and 16% Pay-in-X.",
              s=["shop", "inv"], lc="borrow", neo=[0, ""], src=[["Affirm 10-K FY2026", TENK]]),
            P("takerate", "Economics", "Revenue less transaction costs $589 million in Q4 FY2026 (+39%); guidance of about 4.2% of GMV for FY2027; adjusted operating margin 30%.",
              s=["inv"], lc="borrow", neo=[0, ""], src=[["Pulse 2.0: Q4 FY2026, Aug 2026", PULSE], ["Q4 FY2026 earnings call", CALL]]),
        ]},
        {"id": "4.2", "ic": "wallet-cards", "name": "Card & Money", "blurb": "19% of users carry it.", "div": "card", "rev": "card", "products": [
            P("money", "Affirm Money", "A high-yield savings account held with Cross River Bank, no minimum balance; paired with the Affirm Card.",
              s=["card"], lc="beyond", o="P", at="Cross River Bank", neo=[0, ""], src=[["Affirm Card", CARD], ["Affirm 10-K FY2026", TENK]]),
            P("cardoffers", "Card offers", "Merchant-funded 0% offers on the card; cardholders spend about twice the average user and make up 19% of active consumers.",
              s=["card"], lc="grow", neo=[0, "Visa."], src=[["Q4 FY2026 earnings call", CALL]]),
        ]},
        {"id": "4.3", "ic": "store", "name": "Merchant network", "blurb": "571,000 merchants.", "div": "affirm", "rev": "merchant", "products": [
            P("merchants", "Merchants", "About 571,000 active merchants, up more than 50%, mainly through platforms; about 10% of US e-commerce merchants and 80 of the top 250 US sites.",
              s=["merch"], lc="open", neo=[0, "Affirm pays merchants itself ⚠."],
              mc="Merchant data and risk tools for a fast-growing merchant base.",
              src=[["Crowdfund Insider: Q4 FY2026 results, Aug 2026", Q4CFI], ["Q4 FY2026 earnings call", CALL]]),
            P("verticals", "New verticals", "Professional services, elective medical and auto already bring billions of dollars of GMV and grow about twice as fast as the company; services volume nearly doubled.",
              s=["merch"], lc="grow", st="new", neo=[0, ""], src=[["Pulse 2.0: Q4 FY2026, Aug 2026", PULSE], ["Q4 FY2026 earnings call", CALL]]),
        ]},
        {"id": "4.4", "ic": "briefcase-business", "name": "Enterprise partners", "blurb": "Amazon, Shopify, Costco.", "div": "affirm", "rev": "merchant", "products": [
            P("amazon", "Amazon", "Partner since 2021 (exclusive US BNPL to January 2023); deal extended by five years in late 2025; Affirm's share of wallet there is low single digits.",
              s=["ent", "shop"], lc="grow", o="P", at="Amazon", neo=[0, ""], src=[["Digital Transactions: Q1 FY2026, Nov 2025", Q1FY26], ["Digital Transactions: Amazon, Nov 2021", AMZ2021]]),
            P("shopify", "Shopify (Shop Pay Installments)", "Exclusive pay-over-time provider for Shop Pay Installments in the US and Canada, renewed in February 2025; UK added in 2025 and Australia in August 2026.",
              s=["merch", "shop"], lc="grow", o="P", at="Shopify", neo=[0, ""], src=[["TipRanks: Affirm and Shopify, Feb 2025", SHOPIFY], ["Pulse 2.0: Q4 FY2026, Aug 2026", PULSE]]),
            P("costco", "Costco", "Affirm plans for Costco's online shoppers from May 2025.",
              s=["ent"], lc="grow", ay="May 2025", o="P", at="Costco", neo=[0, ""], src=[["Wikipedia: Affirm Holdings", WIKI]]),
            P("walmart", "Walmart", "A partner since 2019 that gave Klarna and OnePay its exclusive in March 2025; about 5% of Affirm's GMV in late 2024. Affirm stays a checkout option.",
              s=["ent"], lc="grow", st="flux", ay="Mar 2025", neo=[0, ""], src=[["Payments Dive: Walmart, Mar 2025", WALMART]]),
        ]},
        {"id": "4.5", "ic": "earth", "name": "International", "blurb": "Canada, UK, Australia.", "div": "intl", "rev": "interest", "products": [
            P("canada", "Canada", "Lending through Affirm Canada, with Shop Pay Installments; the Retail Payment Activities Act fully in force from 8 September 2025.",
              s=["shop"], lc="borrow", neo=[0, ""], src=[["Affirm 10-K FY2026", TENK]]),
            P("uk", "United Kingdom", "Launched 4 November 2024 with Alternative Airlines and Fexco; FCA-authorised; BNPL rules in force from 25 July 2026; Shop Pay in the UK.",
              s=["shop"], lc="borrow", st="new", ay="Nov 2024", neo=[0, ""],
              mc="The UK and Europe are debit markets where Mastercard is strong.",
              src=[["The Paypers: Affirm UK, Nov 2024", UK], ["Affirm 10-K FY2026", TENK]]),
            P("australia", "Australia & Europe", "Limited Australia launch in Q1 FY2027 under an ASIC licence; staff in Spain and Poland; the Netherlands, France and Germany planned.",
              s=["shop"], lc="borrow", st="new", ay="2026", neo=[0, ""], src=[["Affirm 10-K FY2026", TENK]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Affirm: the Affirm app, checkout integrations, processors from Stripe to Mastercard Gateway, and in-store paths through the card, virtual cards and Apple Pay.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App", "blurb": "Shop, pay, repay.", "div": "affirm", "rev": "grp", "products": [
            P("app", "Affirm app", "Where shoppers apply, manage plans and repay, run the card and Affirm Money, and move card purchases to plans.",
              s=["shop", "card"], lc="open", neo=[0, ""], src=[["Affirm Card", CARD]]),
        ]},
        {"id": "5.2", "ic": "code-xml", "name": "Checkout integrations", "blurb": "Buttons and SDKs.", "div": "affirm", "rev": "merchant", "products": [
            P("sdk", "Checkout integrations", "Affirm at checkout by direct integration or through e-commerce platforms; virtual cards let merchants take Affirm through their existing card processing.",
              s=["merch"], lc="open", neo=[0, ""], src=[["Affirm docs: virtual cards", VCN], ["Wikipedia: Affirm Holdings", WIKI]]),
        ]},
        {"id": "5.3", "ic": "network", "name": "Processors & platforms", "blurb": "Stripe, Worldpay, JPM.", "div": "affirm", "rev": "merchant", "products": [
            P("stripe", "Stripe", "Affirm available to Stripe merchants since May 2022.",
              s=["merch", "ent"], lc="open", o="P", at="Stripe", neo=[0, ""], src=[["Wikipedia: Affirm Holdings", WIKI]]),
            P("worldpay", "Worldpay", "Affirm for Worldpay merchants since May 2023.",
              s=["merch", "ent"], lc="open", o="P", at="Worldpay", neo=[0, ""], src=[["Wikipedia: Affirm Holdings", WIKI], ["Digital Transactions: Q1 FY2026, Nov 2025", Q1FY26]]),
            P("jpm", "J.P. Morgan Payments", "Affirm at checkout for J.P. Morgan's merchants from March 2025.",
              s=["ent"], lc="open", ay="Mar 2025", o="P", at="JPMorgan Chase", neo=[0, ""], src=[["Wikipedia: Affirm Holdings", WIKI]]),
            P("mcgw", "Mastercard Gateway", "Mastercard's developer documentation lists Affirm as a payment method on Mastercard Gateway, with Pay in 4 and 3–36-month plans, mainly in the US ⚠ date not found.",
              s=["merch"], lc="open", o="P", at="Mastercard", neo=[3, "Mastercard Gateway offers Affirm ⚠."],
              mc="Mastercard's one confirmed product touchpoint with Affirm.",
              src=[["Mastercard Developers: Affirm on Mastercard Gateway", MCGW]]),
        ]},
        {"id": "5.4", "ic": "store", "name": "In store", "blurb": "Card, VCN, Apple Pay.", "div": "card", "rev": "card", "products": [
            P("instore", "In-store paths", "Shoppers pay later in store with the Affirm Card (30% of card transactions are offline), a one-time Visa virtual card, or Affirm inside Apple Pay.",
              s=["shop", "card"], lc="move", neo=[0, "Visa."], src=[["Q4 FY2026 earnings call", CALL], ["Nasdaq: Affirm in-store with Apple Pay, Sep 2025", APPLEPAY]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Affirm", "blurb": "At the edges; Visa holds the cards.", "products": [
        P("mcataffirm", "Mastercard at Affirm", "Every Affirm card product runs on Visa: the Affirm Card, its Visa Flexible Credential and the one-time virtual cards. Mastercard Gateway lists Affirm as a payment method ⚠, both back Google's AP2, and Affirm plans on Fiserv banks' debit cards may ride Mastercard ⚠. No Mastercard issuing deal was found.",
          s=["shop"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Affirm Card", CARD], ["Visa: Flexible Credential goes global, Nov 2024", VISAFLEX], ["Mastercard Developers: Affirm on Mastercard Gateway", MCGW]]),
    ]},
    {"id": "pillar-market", "name": "Pay over time", "blurb": "BNPL, Klarna, Mastercard Installments.", "products": [
        P("market", "The market", "Affirm is the largest US BNPL lender, in a tender just over 1% of US spend. Klarna took Walmart in 2025; PayPal, Afterpay, Sezzle and Zip compete; banks and card issuers compete for the same credit; Mastercard Installments offers instalments to banks, fintechs and wallets on Mastercard cards.",
          s=["shop"], div="grp", rev="grp", src=[["Digital Transactions: Q1 FY2026, Nov 2025", Q1FY26], ["Nasdaq: Mastercard and Affirm, Nov 2025", MCINST], ["Payments Dive: Walmart, Mar 2025", WALMART]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
