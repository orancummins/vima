"""Marqeta's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Marqeta's own unless a source says otherwise: the Q2 2026 results (4 August 2026), the FY2025
results and 10-K (February 2026) and the company's product pages. ``neo`` is the Mastercard lens: [depth, note],
where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://www.01net.it/marqeta-reports-second-quarter-2026-financial-results/"
Q2CALL = "https://www.marketbeat.com/earnings/reports/2026-8-3-marqeta-inc-stock/"
Q1CALL = "https://www.marketbeat.com/earnings/reports/2026-5-5-marqeta-inc-stock/"
FY25 = "https://seekingalpha.com/pr/20412039"
TENK = "https://www.sec.gov/Archives/edgar/data/1522540/000152254026000017/mq-20251231.htm"
ABOUT = "https://www.marqeta.com/company/about-us"
PLATFORM = "https://www.marqeta.com/platform/overview"
MC20 = "https://newsroom.mastercard.com/news/press/2020/october/mastercard-and-marqeta-expand-strategic-global-partnership/"
MCAP22 = "https://newsroom.mastercard.com/news/ap/en/newsroom/press-releases/en/2022/marqeta-among-the-first-to-join-mastercard-s-network-enablement-partner-program-in-asia-pacific"
VFC = "https://www.marqeta.com/blog/marqeta-announces-certification-for-visa-flexible-credential"
KLARNAEU = "https://www.marqeta.com/blog/marqeta-powers-expansion-of-klarna-debit-card-across-europe"
TPAY = "https://www.marqeta.com/blog/marqeta-completes-transactpay-acquisition-strengthening-european-payment"
JUNIPER = "https://www.marqeta.com/blog/marqeta-recognized-in-juniper-research-2026-embedded-finance-leaderboard"
RAILS = "https://www.marqeta.com/blog/marqeta-unifies-card-and-non-card-payments-on-a-single-platform"
FOUND = "https://www.marqeta.com/blog/the-foundation-the-worlds-leading-payment-programs-are-built-on"
ZEROHASH = "https://www.marqeta.com/blog/marqeta-partners-with-zerohash-for-stablecoin-cards-heres-what-it-means-for-card-programs"
BVNK = "https://www.stocktitan.net/news/MQ/bvnk-and-marqeta-partner-to-power-stablecoin-card-9hfgpmvjk3yt.html"
COINBASE = "https://www.stocktitan.net/news/MQ/marqeta-and-coinbase-collaborate-to-enable-stablecoin-backed-card-v2m5qopu49ib.html"
GOOGLE = "https://www.stocktitan.net/news/MQ/marqeta-expands-collaboration-with-google-to-launch-new-offering-in-wh86x9q9cnto.html"
EXPENSIFY = "https://www.stocktitan.net/news/MQ/expensify-expands-collaboration-with-marqeta-to-bring-its-card-fi78dmwft3z6.html"
CPO = "https://www.stocktitan.net/news/MQ/marqeta-announces-appointment-of-eugenia-gibbons-as-chief-product-bobz9ydirzsi.html"
RISKIFIED = "https://www.stocktitan.net/news/MQ/riskified-and-marqeta-partner-to-sharpen-card-issuer-authorization-6bq9c3pwln79.html"
CEO25 = "https://investors.marqeta.com/news-releases/news-release-details/marqeta-announces-leadership-transition"
CEOPERM = "https://paymentexpert.com/2025/09/09/marqeta-appoints-new-ceo/"
MCBVNK = "https://theblock.co/post/410521/mastercard-completes-bvnk-acquisition"
RTD = "https://www.marqeta.com/platform/real-time-decisioning"
RTDAI = "https://thepaypers.com/fraud-and-fincrime/news/marqeta-improves-real-time-decisioning-with-ai-powered-fraud-risk-scoring"
MCP = "https://www.marqeta.com/platform/mcp-server"
FLEX = "https://www.marqeta.com/platform/flexible-credentials"
DEBIT = "https://www.marqeta.com/platform/debit"
CREDIT = "https://www.marqeta.com/platform/credit"
AMM = "https://www.marqeta.com/platform/accounts-money-movement"
JIT = "https://www.marqeta.com/platform/jit-funding"
UX = "https://www.marqeta.com/platform/ux-toolkit"
RISK = "https://www.marqeta.com/platform/risk-fraud"
PM = "https://www.marqeta.com/payment-solutions/program-management"
VCARD = "https://www.marqeta.com/platform/virtual-cards"
COMMBANK = "https://www.marqeta.com/payment-solutions/commercial-banking"
DIGBANK = "https://www.marqeta.com/payment-solutions/digital-banking"
CUSTOMERS = "https://www.marqeta.com/customers"
WU = "https://www.marqeta.com/resources/western-union-case-study"
CASHAPP = "https://cash.app/card"
SQUARE = "https://squareup.com/us/en/banking/checking"
AFFIRM = "https://www.affirm.com/card"
KLARNAUS = "https://www.klarna.com/us/card/"
RAMP = "https://ramp.com/"
NEWSROOM = "https://www.marqeta.com/company/newsroom"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "volume · banks · networks", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $383 billion of volume in 2025 and two profitable quarters in 2026, a Nasdaq listing worth about $2 billion, Sutton Bank and other issuing banks, an e-money licence in Europe, and direct agreements with Visa, Mastercard and PULSE.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & profit", "blurb": "$120bn a quarter, now profitable.", "div": "grp", "rev": "grp", "products": [
            P("scale", "Volume & revenue", "Total processing volume of $382.5 billion in 2025 (+31%) and $120.4 billion in Q2 2026 (+32%); net revenue of $624.9 million in 2025 (+23%) and $176.0 million in Q2 2026 (+17%); a take rate of about 10 basis points.",
              s=["fin", "lend"], neo=[0, ""], src=[["Q2 2026 results, Aug 2026", Q2], ["FY2025 results, Feb 2026", FY25], ["10-K FY2025", TENK]]),
            P("profit", "Profit & guidance", "GAAP net income of $8 million in Q1 and $7.6 million in Q2 2026, its first profitable quarters, after a $14 million loss in 2025; adjusted EBITDA $37.4 million in Q2 (21% margin); 2026 guided to 12–13% revenue growth and net income in the high $20 millions.",
              s=["ent"], neo=[0, ""], src=[["Q2 2026 results, Aug 2026", Q2], ["Q2 2026 call, Aug 2026", Q2CALL]]),
        ]},
        {"id": "1.2", "ic": "users-round", "name": "Ownership & leadership", "blurb": "Nasdaq, Milotich as CEO.", "div": "grp", "rev": "grp", "products": [
            P("listing", "Listing & capital", "Nasdaq-listed as MQ since June 2021; worth about $1.95 billion in October 2026 ⚠; a one-for-four reverse split on 30 June 2026; $391 million of buybacks in 2025 and a new $150 million authorisation (August 2026); insiders hold about 48% of votes; Mastercard took a minority stake in 2020 ⚠ size undisclosed.",
              s=["ent"], neo=[0, "Mastercard holds an undisclosed minority stake."], src=[["Q2 2026 results, Aug 2026", Q2], ["Coinbase release (market data), Oct 2026", COINBASE], ["Mastercard: partnership and investment, Oct 2020", MC20]]),
            P("leadership", "Executives & board", "CEO Mike Milotich (CFO from 2022, interim CEO after Simon Khalaf left in February 2025, permanent from September 2025); CFO Patti Kangwankij; CPO Eugenia Gibbons (from 31 August 2026, ex-Intuit); CRO Todd Pollak; CTO Lukasz Strozek; CSO Anthony Peculic; chair Jud Linville; founder Jason Gardner on the board; 938 staff.",
              s=["ent"], neo=[0, ""], src=[["Marqeta: about us", ABOUT], ["Leadership transition, Feb 2025", CEO25], ["Payment Expert: new CEO, Sep 2025", CEOPERM], ["Gibbons appointed CPO, Aug 2026", CPO]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Banks & licences", "blurb": "Sutton Bank, a European EMI.", "div": "grp", "rev": "grp", "products": [
            P("banks", "Issuing banks", "Marqeta is not a bank: issuing banks hold the cards. Sutton Bank settled 64% of volume in 2025 (76% in 2023) under a contract to 2029; Durbin-exempt banks carry debit and prepaid programmes for higher interchange.",
              s=["fin"], o="P", at="Sutton Bank", neo=[0, ""], src=[["10-K FY2025", TENK]]),
            P("licences", "Licences", "TransactPay holds e-money licences and BIN sponsorship in the UK, Gibraltar and the EEA (Gibraltar FSC, Malta FSA); Marqeta Payments LLC is a registered payment service provider in Canada; Marqeta Services LLC holds US state servicing licences.",
              s=["fin", "biz"], o="A", neo=[0, ""], src=[["10-K FY2025", TENK], ["TransactPay acquisition, Aug 2025", TPAY]]),
        ]},
        {"id": "1.4", "ic": "network", "name": "Network agreements", "blurb": "Visa 2017, Mastercard 2020.", "div": "grp", "rev": "grp", "products": [
            P("visaagr", "Visa alliance", "A strategic alliance framework from 2017; the card partner agreement was extended five years in February 2023, with tiered incentives on volume routed over Visa. Visa can end it early if performance targets are missed.",
              s=["fin"], o="P", at="Visa", ay="2017", neo=[0, "Visa."], src=[["10-K FY2025", TENK]]),
            P("mcagr", "Mastercard strategic relationship", "Working together since 2014; a strategic relationship agreement and minority investment in October 2020, with tiered incentives on Mastercard volume and a term to 2028, or earlier if a volume milestone is reached.", short="Mastercard agreement",
              s=["fin"], o="P", at="Mastercard", ay="Oct 2020", neo=[2, "Mastercard's own agreement."],
              mc="The 2028 milestone gives Mastercard a lever to win programmes as Cash App issuance moves away.",
              src=[["Mastercard: partnership and investment, Oct 2020", MC20], ["10-K FY2025", TENK]]),
            P("pulse", "PULSE processor agreement", "A direct processor agreement with PULSE, the debit network, from 2013, running to 2031 with tiered incentives.",
              s=["fin"], o="P", at="PULSE", ay="2013", neo=[0, "PULSE."], src=[["10-K FY2025", TENK]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Beyond Block.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "Strategy", "Grow beyond Block through multinational issuing (international 20% of volume in Q2 2026), credit and flexible credentials, accounts and non-card rails, stablecoin cards and AI risk tools; 12 of the top 15 customers use Marqeta in more than one country.",
              s=["ent"], neo=[0, ""], src=[["Q2 2026 call, Aug 2026", Q2CALL], ["Q1 2026 call, May 2026", Q1CALL]]),
            P("deals", "Acquisitions", "Power Finance (February 2023), the base for credit issuing from October 2023, and TransactPay, a UK and EEA e-money institution and BIN sponsor (closed 31 July 2025; price not disclosed ⚠).",
              s=["lend", "biz"], o="A", neo=[0, ""], src=[["10-K FY2025", TENK], ["TransactPay acquisition, Aug 2025", TPAY]]),
            P("blockshift", "Block concentration", "Block (Cash App, Square, Afterpay) was 68% of net revenue in 2023, 45% in 2025 and 41% in Q2 2026. Block began cutting new Cash App card issuance on Marqeta in mid-June 2026 and is expected to issue little or none by year-end; existing cardholders stay, and the contract runs to June 2028.",
              s=["fin"], st="flux", neo=[0, "Cash App is a Visa card."], src=[["Q2 2026 call, Aug 2026", Q2CALL], ["10-K FY2025", TENK]]),
        ]},
    ],
}

RAILS_L = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: issuer processing for physical, virtual and tokenised cards; debit and prepaid; credit; flexible credentials; accounts and non-card rails; multinational issuing with a European licence; and stablecoin-backed cards.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Issuing & processing", "blurb": "Every network, 40+ countries.", "div": "mq", "rev": "fin", "products": [
            P("processing", "Card issuing & processing", "Issuer processing for physical, virtual and tokenised cards, with transaction-level authorise, decline and route rules changed in real time; 1,000+ transactions a second at peak and 99.99% uptime in 2025; certified across Visa, Mastercard and PULSE.",
              s=["fin", "lend", "biz"], lc="move", neo=[1, "Visa, Mastercard and PULSE."], src=[["Marqeta: platform", PLATFORM], ["10-K FY2025", TENK]]),
            P("jit", "Just-in-Time Funding", "Cards held at $0 and funded at the moment of authorisation, with Managed and Gateway JIT; launched with the open APIs in 2014.",
              s=["biz", "gig"], lc="move", ay="2014", o="B", neo=[0, "Marqeta's own; any network."], src=[["Marqeta: JIT Funding", JIT], ["Marqeta: about us", ABOUT]]),
            P("virtual", "Virtual cards", "Instant virtual cards for point-of-sale loans, gig payouts and supplier payments, usable wherever Visa and Mastercard are accepted.",
              s=["lend", "biz", "gig"], lc="move", neo=[1, "Visa and Mastercard."], src=[["Marqeta: virtual cards", VCARD]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Debit & prepaid", "blurb": "Cash App on Visa, Square on Mastercard.", "div": "mq", "rev": "fin", "products": [
            P("debit", "Debit & prepaid cards", "Branded debit and prepaid cards with wallet provisioning, issued through Durbin-exempt banks.",
              s=["fin", "card"], lc="everyday", neo=[1, "By programme."], src=[["Marqeta: debit & prepaid", DEBIT], ["10-K FY2025", TENK]]),
            P("cashapp", "Cash App Card", "Block's Cash App Visa Debit Flex card, issued by Sutton Bank: Marqeta's largest programme. Block has run it with Visa directly since July 2023 and is moving new issuance away in 2026.",
              s=["card"], lc="everyday", st="flux", o="P", at="Block", neo=[0, "Visa."], src=[["Cash App Card", CASHAPP], ["Q2 2026 call, Aug 2026", Q2CALL]]),
            P("squaredebit", "Square Debit Card", "The business debit card for Square sellers, issued by Sutton Bank on Mastercard; the Square Card was cited in the 2020 Mastercard deal.",
              s=["biz", "card"], lc="everyday", o="P", at="Block", neo=[2, "Mastercard."], src=[["Square Checking", SQUARE], ["Mastercard: partnership and investment, Oct 2020", MC20]]),
        ]},
        {"id": "2.3", "ic": "hand-coins", "name": "Credit", "blurb": "Three new programmes coming.", "div": "mq", "rev": "lend", "products": [
            P("credit", "Credit card issuing", "Revolving credit cards and BINs with credit ledgers, underwriting, rewards, collections and servicing; launched in October 2023 after buying Power Finance.",
              s=["lend", "fin"], lc="borrow", ay="Oct 2023", o="A", neo=[None, "Networks by programme; not disclosed."], src=[["Marqeta: credit", CREDIT], ["10-K FY2025", TENK]]),
            P("creditnew", "New credit programmes", "Three launching over the coming quarters (August 2026): a consumer co-brand revolving card, a secured credit-builder with BNPL on Mastercard One Credential, and a commercial charge card; a large US bank already provisions a credit line into a consumer wallet.",
              s=["lend", "ent"], lc="borrow", st="new", neo=[1, "The credit-builder is on Mastercard."], src=[["Q2 2026 call, Aug 2026", Q2CALL], ["Q1 2026 call, May 2026", Q1CALL]]),
        ]},
        {"id": "2.4", "ic": "refresh-cw", "name": "Flexible credentials", "blurb": "Visa first; One Credential next.", "div": "mq", "rev": "lend", "products": [
            P("vfc", "Visa Flexible Credential", "The first US issuer processor certified (May 2024, announced July 2024): one card that toggles between debit, credit, pay-in-four and points, live with Affirm, Klarna and Block.",
              s=["lend", "card"], lc="borrow", ay="Jul 2024", o="P", at="Visa", neo=[0, "Visa."],
              mc="Marqeta expects its Visa lead to last several more quarters.",
              src=[["Marqeta: Visa Flexible Credential, Jul 2024", VFC], ["Juniper leaderboard release, Oct 2026", JUNIPER], ["Q1 2026 call, May 2026", Q1CALL]]),
            P("onecred", "Mastercard One Credential", "Supported in 2026: a personal-finance app migrating its portfolio is an early adopter (Q1 2026), and a secured credit-builder with BNPL is launching on it.", short="One Credential",
              s=["lend", "card"], lc="borrow", st="new", o="P", at="Mastercard", neo=[3, "Mastercard One Credential."],
              mc="Mastercard's answer to the Visa lead, with only early programmes so far.",
              src=[["Q1 2026 call, May 2026", Q1CALL], ["Q2 2026 call, Aug 2026", Q2CALL], ["Juniper leaderboard release, Oct 2026", JUNIPER]]),
            P("hub", "Marqeta Hub", "Formerly Marqeta Flex: shows several BNPL providers inside an app or wallet at payment, through one integration.",
              s=["lend", "card"], lc="borrow", o="B", neo=[0, ""], src=[["10-K FY2025", TENK]]),
        ]},
        {"id": "2.5", "ic": "arrow-left-right", "name": "Accounts & money movement", "blurb": "ACH, RTP, FedNow, push to card.", "div": "mq", "rev": "exp", "products": [
            P("accounts", "Accounts & cash access", "Branded checking and savings accounts, direct deposit, fee-free ATM access, cash deposits and mobile cheque capture.",
              s=["fin", "card"], lc="everyday", neo=[0, ""], src=[["Marqeta: accounts & money movement", AMM], ["Marqeta: digital banking", DIGBANK]]),
            P("payouts", "Card and non-card payouts", "ACH, same-day ACH, push to card, RTP and FedNow (September 2026), with UK Faster Payments and SEPA in Europe, for supplier payments, gig pay, refunds and reimbursements.",
              s=["biz", "gig"], lc="move", st="new", ay="Sep 2026", neo=[1, "Push to card on both networks; bank rails off them."],
              mc="Push to card could ride on Mastercard Move.",
              src=[["Marqeta: card and non-card payments, Sep 2026", RAILS]]),
        ]},
        {"id": "2.6", "ic": "earth", "name": "Multinational & Europe", "blurb": "TransactPay, Banking Circle.", "div": "tpay", "rev": "exp", "products": [
            P("europe", "Europe on one integration", "TransactPay's e-money licence and BIN sponsorship (July 2025) plus Banking Circle for accounts in 30 more European countries; Klarna's card in 15 more markets (November 2025), Expensify's corporate card in the UK and EU (July 2026), and Western Union's multi-currency banking.",
              s=["lend", "biz", "ent"], lc="open", st="new", o="A", at="TransactPay", neo=[1, "Klarna on Visa; others not stated ⚠."],
              src=[["TransactPay acquisition, Aug 2025", TPAY], ["Klarna Card across Europe, Nov 2025", KLARNAEU], ["Expensify to Europe, Jul 2026", EXPENSIFY], ["Q2 2026 call, Aug 2026", Q2CALL]]),
            P("multinational", "40+ countries", "Certified in more than 40 countries; among the first in Mastercard's Network Enablement Partner programme in Asia Pacific (June 2022, Singapore hub); Ramp expanding to Australia, Japan, Singapore, Brazil and Mexico, and Sezzle to Canada (2026).",
              s=["biz", "lend"], lc="open", neo=[1, "Mastercard enablement in APAC; Visa too."],
              src=[["Mastercard: Network Enablement Partner, Jun 2022", MCAP22], ["Q1 2026 call, May 2026", Q1CALL]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Stablecoin cards", "blurb": "zerohash, BVNK, Coinbase.", "div": "mq", "rev": "fin", "products": [
            P("stablecoin", "Stablecoin-backed cards", "Cards that spend stablecoin balances wherever cards are accepted: with zerohash (August 2026) and Coinbase, with settlement on Base (16 October 2026); crypto cards already live for Coinbase in the US and Bitpanda in Europe.",
              s=["fin", "card"], lc="move", st="new", o="P", at="zerohash, Coinbase", neo=[None, "Network not named."],
              mc="The network role on these cards is still open.",
              src=[["Marqeta: zerohash, Aug 2026", ZEROHASH], ["Marqeta and Coinbase, Oct 2026", COINBASE], ["Q2 2026 call, Aug 2026", Q2CALL]]),
            P("bvnk", "BVNK stablecoin cards", "Stablecoin-backed cards on BVNK's infrastructure, accepted wherever Mastercard is (9 September 2026); BVNK became part of Mastercard in August 2026.", short="BVNK cards",
              s=["fin", "card"], lc="move", st="new", ay="Sep 2026", o="P", at="BVNK (Mastercard)", neo=[3, "Mastercard's BVNK, on Mastercard."],
              src=[["BVNK and Marqeta, Sep 2026", BVNK], ["The Block: Mastercard completes BVNK, Aug 2026", MCBVNK]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card: Real-Time Decisioning with an AI risk score and merchant data, KYC, 3-D Secure and disputes, tokens and wallets, programme management and rewards, and an MCP server for AI agents.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Real-Time Decisioning", "blurb": "AI risk score, 300+ signals.", "div": "mq", "rev": "fin", "products": [
            P("rtd", "Real-Time Decisioning", "Issuer authorisation rules on hundreds of data attributes, including card network risk scores, approving or declining each transaction in real time.",
              s=["fin", "lend", "biz"], lc="everyday", o="B", neo=[1, "Uses network risk scores ⚠."], src=[["Marqeta: Real-Time Decisioning", RTD]]),
            P("riskscore", "AI risk score", "A machine-learning score added in March 2026 that weighs 300+ attributes against past behaviour in milliseconds, to cut fraud and false declines.",
              s=["fin", "lend"], lc="everyday", st="new", ay="Mar 2026", o="B", neo=[0, "Marqeta's own model."],
              mc="Decision Intelligence scores could sit beside it.",
              src=[["The Paypers: AI risk score, Mar 2026", RTDAI], ["Juniper leaderboard release, Oct 2026", JUNIPER]]),
            P("merchantdata", "Merchant data partners", "Adyen, Riskified and Signifyd feed device, location, order and account data into the risk score (August 2026).",
              s=["fin"], lc="everyday", st="new", o="P", at="Adyen, Riskified, Signifyd", neo=[0, "Off the networks."],
              src=[["Q2 2026 results, Aug 2026", Q2], ["Riskified and Marqeta, Aug 2026", RISKIFIED]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "KYC, 3DS & disputes", "blurb": "Identity to chargeback.", "div": "mq", "rev": "fin", "products": [
            P("risk", "KYC, 3-D Secure & disputes", "Know-your-customer checks, 3-D Secure, and disputes and chargebacks created and sent to the card networks by API.",
              s=["fin", "card"], lc="open", neo=[1, "Disputes go to each network."], src=[["Marqeta: risk & fraud", RISK], ["Marqeta: platform", PLATFORM]]),
        ]},
        {"id": "3.3", "ic": "smartphone", "name": "Tokens & wallets", "blurb": "Google Wallet, kids' cards.", "div": "mq", "rev": "fin", "products": [
            P("tokens", "Tokenisation & wallet provisioning", "Tokenised cards pushed into mobile wallets at issuance, a value-added service since the early Google work.",
              s=["card"], lc="everyday", neo=[1, "Both networks' token services."], src=[["10-K FY2025", TENK], ["Marqeta: platform", PLATFORM]]),
            P("googlewallet", "Google Wallet for kids", "Under-18s receive and spend allowances in Google Wallet on Android phones and Wear OS, with parental limits (August 2026), building on the Google Pay balance card.",
              s=["card", "ent"], lc="everyday", st="new", ay="Aug 2026", o="P", at="Google", neo=[None, "Network not stated."],
              src=[["Marqeta and Google, Aug 2026", GOOGLE], ["Marqeta: customers", CUSTOMERS]]),
        ]},
        {"id": "3.4", "ic": "briefcase", "name": "Programme management", "blurb": "Banks, compliance, rewards.", "div": "mq", "rev": "fin", "products": [
            P("pm", "Programme management", "Bank selection, compliance with bank and network rules, cardholder support and collections; European programme management planned on TransactPay.",
              s=["fin", "lend", "biz"], lc="open", neo=[1, "Network rules for every scheme."], src=[["Marqeta: programme management", PM], ["Q2 2026 call, Aug 2026", Q2CALL]]),
            P("rewards", "Rewards", "Configurable accrual, categories and redemption for consumer and business cards.",
              s=["lend", "biz"], lc="grow", neo=[0, ""],
              mc="Card-linked offers could feed it.",
              src=[["Marqeta: credit", CREDIT], ["Marqeta: digital banking", DIGBANK]]),
        ]},
        {"id": "3.5", "ic": "bot", "name": "Agentic payments", "blurb": "An MCP server.", "div": "mq", "rev": "exp", "products": [
            P("mcp", "MCP server", "Lets AI agents issue virtual cards on demand, enforce spend and velocity controls, raise disputes and review transactions through Marqeta's APIs; management says issuers are best placed to lead agentic payments.",
              s=["biz", "ent"], lc="move", st="new", o="B", neo=[0, "No Agent Pay link announced."],
              mc="Agent Pay tokens would fit the cards it issues.",
              src=[["Marqeta: MCP server", MCP], ["Q1 2026 call, May 2026", Q1CALL]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Who buys: digital banks and fintechs (Block, Coinbase, Google), lenders and BNPL firms (Klarna, Affirm), expense and commercial platforms (Ramp, Expensify, Bill), and on-demand and enterprise brands (DoorDash, Instacart, Uber, Western Union).",
    "tiles": [
        {"id": "4.1", "ic": "users-round", "name": "Digital banking & fintech", "blurb": "Block, Coinbase, Google.", "div": "mq", "rev": "fin", "products": [
            P("digbank", "Digital banking & fintech", "Cash App (Visa) and Square (Mastercard), Coinbase, Shakepay and Google Pay balance cards; Block was 41% of net revenue in Q2 2026.",
              s=["fin"], lc="everyday", neo=[1, "Cash App on Visa; Square Debit on Mastercard."], src=[["Marqeta: customers", CUSTOMERS], ["Cash App Card", CASHAPP], ["Square Checking", SQUARE], ["Q2 2026 call, Aug 2026", Q2CALL]]),
        ]},
        {"id": "4.2", "ic": "receipt-text", "name": "Lending & BNPL", "blurb": "Klarna, Affirm, Afterpay.", "div": "mq", "rev": "lend", "products": [
            P("bnpl", "Lending & BNPL", "Klarna and Affirm cards (both Visa), Afterpay, Sezzle and Four; lending including BNPL grew nearly 60% in Q1 2026 and over 40% in Q2; Klarna moved nearly 3 million cards to Marqeta with no downtime (2026).",
              s=["lend"], lc="borrow", neo=[0, "Klarna and Affirm on Visa."], src=[["Klarna Card (US)", KLARNAUS], ["Affirm Card", AFFIRM], ["Q1 2026 call, May 2026", Q1CALL], ["Q2 2026 call, Aug 2026", Q2CALL], ["Marqeta: customers", CUSTOMERS]]),
        ]},
        {"id": "4.3", "ic": "briefcase-business", "name": "Expense & commercial", "blurb": "Ramp, Expensify, Bill.", "div": "mq", "rev": "exp", "products": [
            P("expense", "Expense management", "Ramp (Visa corporate and business cards), Expensify, Bill and Divvy; expense-management volume grew over 50% in Q2 2026. Visa's sunset of Level 2 commercial interchange (April 2026) lowers revenue here.",
              s=["biz"], lc="everyday", neo=[0, "Ramp on Visa; others not stated."],
              mc="Commercial cards are where Visa's interchange change bites.",
              src=[["Ramp", RAMP], ["Q2 2026 call, Aug 2026", Q2CALL], ["10-K FY2025", TENK]]),
            P("commbank", "Embedded business banking", "Business accounts, co-branded business debit and commercial credit with rewards for software platforms; Found is a customer.",
              s=["biz"], lc="everyday", neo=[None, ""], src=[["Marqeta: commercial banking", COMMBANK]]),
        ]},
        {"id": "4.4", "ic": "store", "name": "On-demand & enterprise", "blurb": "DoorDash, Uber, Western Union.", "div": "mq", "rev": "od", "products": [
            P("ondemand", "On-demand & gig", "DoorDash, Instacart and Uber, including Uber's UK driver programme with fast free access to earnings, savings and rewards (2025).",
              s=["gig"], lc="move", neo=[None, "Networks not stated."], src=[["FY2025 results, Feb 2026", FY25], ["Juniper leaderboard release, Oct 2026", JUNIPER]]),
            P("enterprise", "Enterprises & banks", "A Fortune 500 company's payroll-linked stored-value card (2026), a large US bank's credit line in a consumer wallet, and Western Union's multi-currency digital banking in Europe.",
              s=["ent"], lc="everyday", neo=[None, ""], src=[["Q2 2026 call, Aug 2026", Q2CALL], ["Q1 2026 call, May 2026", Q1CALL], ["Marqeta: Western Union", WU]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Marqeta: open APIs and a sandbox, a dashboard, UX Toolkit and white-label app, and an enterprise sales team with partners from Banking Circle to BVNK.",
    "tiles": [
        {"id": "5.1", "ic": "code-xml", "name": "APIs & developers", "blurb": "Open APIs since 2014.", "div": "mq", "rev": "grp", "products": [
            P("api", "Open APIs & sandbox", "Open APIs, developer guides and a sandbox since 2014, on one integration that reaches 40+ countries.",
              s=["fin", "biz"], lc="open", o="B", neo=[0, ""], src=[["Marqeta: platform", PLATFORM], ["Marqeta: about us", ABOUT]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Dashboard & UX Toolkit", "blurb": "SDKs, white-label app.", "div": "mq", "rev": "grp", "products": [
            P("ux", "UX Toolkit", "APIs, SDKs and a white-label app so a brand can ship a card experience without building the front end.",
              s=["fin", "biz"], lc="open", o="B", neo=[0, ""], src=[["Marqeta: UX Toolkit", UX]]),
            P("dashboard", "Dashboard", "The operations console for programmes, with RiskControl tools.",
              s=["fin"], lc="everyday", o="B", neo=[0, ""], src=[["10-K FY2025", TENK]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Sales & partners", "blurb": "Banking Circle to BVNK.", "div": "grp", "rev": "grp", "products": [
            P("partners", "Enterprise sales & partners", "An enterprise team under CRO Todd Pollak, with partners Banking Circle, zerohash, BVNK, Coinbase, Riskified and Adyen; average deal size up over 90% in Q2 2026.",
              s=["ent"], lc="open", neo=[1, "BVNK is Mastercard's; the rest are neutral."], src=[["Q2 2026 call, Aug 2026", Q2CALL], ["Marqeta newsroom", NEWSROOM]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Marqeta", "blurb": "Square, One Credential, BVNK.", "products": [
        P("mcatmq", "Mastercard at Marqeta", "A partner since 2014 with an investment and strategic agreement from 2020 (term to 2028), Mastercard enablement in Europe and Asia Pacific, the Square Debit Card, the first One Credential programmes and BVNK's stablecoin cards. Visa carries the biggest programmes (Cash App, Klarna, Affirm, Ramp), leads in flexible credentials, and competes with Marqeta through Visa DPS and Pismo.",
          s=["fin"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Mastercard: partnership and investment, Oct 2020", MC20], ["10-K FY2025", TENK], ["BVNK and Marqeta, Sep 2026", BVNK]]),
    ]},
    {"id": "pillar-market", "name": "Modern issuer processing", "blurb": "FIS, Fiserv, Galileo, Visa DPS.", "products": [
        P("market", "The market", "Competitors named by Marqeta: FIS and Fiserv (legacy), Galileo, i2c and Visa DPS (modern), Adyen and Stripe (emerging); Juniper ranked Marqeta a top Established Leader in embedded finance (October 2026).",
          s=["ent"], div="grp", rev="grp", src=[["10-K FY2025", TENK], ["Juniper leaderboard release, Oct 2026", JUNIPER]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS_L, SERVICES, LINES, ACCESS]
