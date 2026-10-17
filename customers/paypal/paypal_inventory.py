"""PayPal Holdings' layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are PayPal's own unless a source says otherwise: the Q2 2026 results (28 July 2026), the FY2025 results
and 10-K (3 February 2026) and the Q2 2026 10-Q, with PayPal's newsroom, product pages and press. Q3 2026 results
had not been released. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

NEWS = "https://newsroom.paypal-corp.com/"
Q2 = "https://www.sec.gov/Archives/edgar/data/0001633917/000163391726000080/pypl2q-26earningsrelease.htm"
Q2NL = "https://s205.q4cdn.com/875401827/files/doc_financials/2026/q2/PYPL-2Q-26-Earnings-IR-Newsletter.pdf"
TENQ = "https://www.sec.gov/Archives/edgar/data/0001633917/000163391726000082/pypl-20260630.htm"
FY25 = "https://s205.q4cdn.com/875401827/files/doc_financials/2025/q4/PYPL-4Q-25-Earnings-Release.pdf"
TENK = "https://www.sec.gov/Archives/edgar/data/1633917/000163391726000024/pypl-20251231.htm"
Q1NL = "https://s205.q4cdn.com/875401827/files/doc_financials/2026/q1/PYPL-1Q-26-Earnings-IR-Newsletter.pdf"
LORES = NEWS + "2026-02-03-PayPal-Appoints-Enrique-Lores-as-Chief-Executive-Officer-and-David-W-Dorman-as-Independent-Board-Chair"
REORG = NEWS + "2026-04-29-PayPal-Announces-Strategic-Reorganization-to-Accelerate-Growth"
SEMAFOR = "https://semafor.com/article/07/15/2026/stripe-and-advent-bid-53b-for-paypal"
PYMNTSBID = "https://www.pymnts.com/news/acquiring/2026/paypal-board-calls-53-billion-stripe-advent-bid-inadequate/"
MCAP = "https://stockanalysis.com/stocks/pypl/market-cap/"
AGENTPAY = NEWS + "2025-10-27-Mastercard-and-PayPal-Join-Forces-To-Accelerate-Secure-Global-Agentic-Commerce"
ONECRED = "https://www.mastercard.com/us/en/news-and-trends/press/2025/june/mastercard-paypal-one-credential.html"
MC2016 = "https://finchannel.com/paypal-and-mastercard-expand-partnership-to-benefit-consumers-merchants-and-financial-institutions/59576/american-business-trends/2016/09/"
MC2017 = "https://finchannel.com/?p=68444"
VISA2016 = NEWS + "PayPal-Visa-Enter-Partnership-to-Extend-Consumer-Payment-Choice"
DEBIT = "https://www.paypal.com/us/digital-wallet/manage-money/paypal-debit-card"
CASHBACK = "https://www.paypal.com/us/digital-wallet/manage-money/paypal-cashback-mastercard"
VENMOCREDIT = NEWS + "2026-10-05-The-Venmo-Credit-Card-Now-Pays-Up-to-4-Cash-Back-When-You-Split-with-Friends"
VENMODEBIT = "https://venmo.com/about/debitcard/"
PPCREDIT = NEWS + "2025-06-03-PayPal-Enhances-Popular-Online-Credit-Offering-with-New-Physical-Card-for-In-Store-Use"
VENMO25 = NEWS + "2025-06-04-Venmo-Unleashes-Next-Phase-of-Commerce-with-the-Venmo-Debit-Card-and-Venmo-Checkout"
VENMO26 = NEWS + "2026-04-15-Venmo-Continues-Its-Evolution-from-a-Peer-to-Peer-App-into-a-Money-Movement-App-for-the-Next-Generation"
PYUSD = NEWS + "2026-03-17-PAYPAL-BRINGS-PAYPAL-USD-TO-USERS-ACROSS-70-MARKETS"
WORLD = NEWS + "2025-07-23-Introducing-PayPal-World-a-global-platform-connecting-the-worlds-largest-payment-systems-and-digital-wallets,-starting-with-interoperability-to-PayPal-and-Venmo"
ACS = NEWS + "2025-10-28-PayPal-Launches-Agentic-Commerce-Services-to-Power-AI-Driven-Shopping"
OPENAI = NEWS + "2025-10-28-OpenAI-and-PayPal-Team-Up-to-Power-Instant-Checkout-and-Agentic-Commerce-in-ChatGPT"
COPILOT = NEWS + "2026-01-08-PayPal-Powers-Microsofts-Launch-of-Copilot-Checkout"
CYMBIO = NEWS + "2026-01-22-PayPal-to-Acquire-Cymbio,-Accelerating-Agentic-Commerce-Capabilities"
KKR = NEWS + "2025-11-17PayPal-and-KKR-Renew-Agreement-for-European-Pay-Later-Receivables"
UK = NEWS + "2025-11-12-paypal-relaunches-in-the-uk-smarter-way-to-pay-online-and-now-in-stores-with-game-changing-paypal-loyalty-programme"
GERMANY = NEWS + "2025-05-05-PayPal-announces-plans-to-revolutionize-in-store-payments-in-Germany"
BANK = NEWS + "2025-12-15-PayPal-Submits-Applications-to-Establish-an-Industrial-Bank-to-Expand-Access-to-Financial-Services-for-U-S-Small-Businesses"
FASTLANE = "https://www.paypal.com/us/business/accept-payments/guest-checkout"
CRYPTO = NEWS + "2025-07-28-PayPal-Drives-Crypto-Payments-into-the-Mainstream,-Reducing-Costs-and-Expanding-Global-Commerce"
OPEN = NEWS + "2025-06-21-From-Solopreneur-to-Large-Enterprise-PayPal-Open-Sparkles-in-Campaign-Unveiling-a-Unified-Platform-for-All-Business"
P2P = NEWS + "2025-09-15-PayPal-Ushers-in-a-New-Era-of-Peer-to-Peer-Payments,-Reimagining-How-Money-Moves-to-Anyone,-Anywhere"
VENMOINTL = NEWS + "2026-03-23-200-Million-More-Friends-on-Venmo-Send-Money-to-PayPal-Users-Around-the-World"
ANTHROPIC = NEWS + "2026-05-PayPal-partners-with-Anthropic-to-Close-the-AI-Gap-for-Small-Businesses"
INDEX = "https://newsroom.paypal-corp.com/news?l=100"
FXC = "https://www.fxcintel.com/research/analysis/ct-paypal-q4-25-earnings"
CALL = "https://www.aol.com/articles/paypal-pypl-q4-2025-earnings-143743423.html"
COINGECKO = "https://www.coingecko.com/en/coins/paypal-usd"
WIKI = "https://en.wikipedia.org/wiki/PayPal"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · licences · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: 439 million accounts and $1.79 trillion of volume in 2025, a new CEO and three businesses, a Luxembourg bank and a proposed US bank, and a turnaround under a Stripe and Advent bid.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "439m accounts, $1.79tn.", "div": "grp", "rev": "grp", "products": [
            P("results", "Volume & earnings", "Revenue of $33.17 billion in 2025 (+4%), TPV of $1.794 trillion (+7%) and transaction margin of $15.47 billion; Q2 2026 revenue of $8.68 billion (+5%) and TPV of $486.4 billion (+10%). 439 million active accounts in about 200 markets; about 23,800 staff. Market value about $48.5 billion at 16 October 2026 ⚠.",
              s=["con"], neo=[0, ""], src=[["PayPal: Q2 2026 results", Q2], ["PayPal: FY2025 results", FY25], ["StockAnalysis: PYPL market cap", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Lores, three businesses.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Board & executives", "Enrique Lores CEO from 1 March 2026 after Alex Chriss left, David Dorman independent chair, Jamie Miller CFO and COO ⚠ still CFO unconfirmed; Frank Keller, Alexis Sowa (interim) and Jeff Pomeroy (interim) lead the three businesses.",
              s=["con"], st="flux", neo=[0, ""], src=[["PayPal: Lores appointed, Feb 2026", LORES], ["PayPal: reorganisation, Apr 2026", REORG]]),
            P("reorg", "Three businesses", "Since 29 April 2026: Checkout Solutions & PayPal; Consumer Financial Services & Venmo; Payment Services & Crypto (Braintree, SMB processing, value-added services, crypto and PYUSD). PayPal still reports one segment.",
              s=["con"], st="new", ay="Apr 2026", neo=[0, ""], src=[["PayPal: reorganisation, Apr 2026", REORG], ["PayPal 10-Q Q2 2026", TENQ]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Licences & bank", "blurb": "Luxembourg bank, PayPal Bank.", "div": "europe", "rev": "grp", "products": [
            P("licences", "Licences", "PayPal (Europe), a Luxembourg credit institution passported across the EU; US money-transmitter licences and a New York BitLicense; an FCA e-money licence, a MAS Major Payment Institution licence (2023), and Paidy's Japanese instalment licences.",
              s=["con"], neo=[0, ""], src=[["PayPal 10-K FY2025", TENK]]),
            P("paypalbank", "PayPal Bank (proposed)", "A Utah industrial loan company applied for on 15 December 2025, for small-business loans, savings and 'direct membership in U.S. card networks'.",
              s=["smb"], st="new", ay="Dec 2025", neo=[None, "Network choice not yet made."],
              mc="Direct network membership would cut out sponsor banks and put network choice in PayPal's hands.",
              src=[["PayPal: bank application, Dec 2025", BANK]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & deals", "blurb": "$1.5bn savings, a bid.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "Turnaround & AI", "Rebuild the consumer network, modernise the platform and cut cost: at least $1.5 billion of gross run-rate savings over two to three years, with ChatGPT Enterprise for more than 24,000 staff; branded-checkout execution 'has not been where it needs to be'.",
              s=["con"], st="new", neo=[0, ""], src=[["PayPal: Q2 2026 IR newsletter", Q2NL], ["PayPal: Q1 2026 IR newsletter", Q1NL], ["PayPal: FY2025 results", FY25]]),
            P("bid", "Stripe and Advent bid", "A reported $60.50-a-share, about $53 billion, all-cash bid (15 July 2026) that the board reportedly found inadequate; a Braintree carve-out to Advent was discussed. No status found after early August ⚠.",
              s=["con"], st="flux", ay="Jul 2026", neo=[0, ""],
              mc="A takeover could reset every network contract.",
              src=[["Semafor: Stripe and Advent bid, Jul 2026", SEMAFOR], ["PYMNTS: board calls bid inadequate, Jul 2026", PYMNTSBID]]),
            P("deals", "Deals & funding", "Honey (2020) ⚠, Paidy ($2.7 billion, 2021) ⚠ and Cymbio (closed February 2026); Pay Later receivables sold to KKR (up to €65 billion to 2028) and Blue Owl.",
              s=["con"], o="A", neo=[0, ""], src=[["PayPal: Cymbio, Jan 2026", CYMBIO], ["PayPal: KKR renewal, Nov 2025", KKR], ["Wikipedia: PayPal", WIKI]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: the PayPal button and Fastlane, Braintree processing and payouts, P2P and cross-border transfers, debit cards on Mastercard, credit split between Mastercard and Visa, Pay Later, and PYUSD and crypto.",
    "tiles": [
        {"id": "2.1", "ic": "wallet", "name": "Branded checkout", "blurb": "31% of TPV, +2%.", "div": "paypal", "rev": "checkout", "products": [
            P("checkout", "PayPal checkout", "The PayPal wallet button, 31% of TPV in Q4 2025 and growing about 2% (FX-neutral) in 2026.",
              s=["con"], lc="move", neo=[1, "Cards on every network in the wallet."], src=[["FXC Intelligence: Q4 2025", FXC], ["PayPal: Q2 2026 IR newsletter", Q2NL]]),
            P("fastlane", "Fastlane", "Passwordless guest checkout from PayPal's vault: 37% higher conversion (April–June 2025) and 264 million cards (October 2024); US only.",
              s=["ent", "con"], lc="grow", neo=[1, "Vaulted cards on every network."],
              mc="Fastlane does what Click to Pay does.",
              src=[["PayPal: Fastlane", FASTLANE]]),
            P("venmocheckout", "Pay with Venmo", "Venmo at checkout with TikTok Shop, Uber, Instacart and Domino's, adding Sephora, Ulta, Taco Bell and Pizza Hut in April 2026.",
              s=["venmo"], lc="move", neo=[1, "Funded by card, bank or balance."], src=[["PayPal: Venmo, Apr 2026", VENMO26], ["PayPal: Venmo Checkout, Jun 2025", VENMO25]]),
        ]},
        {"id": "2.2", "ic": "store", "name": "Braintree & PayPal Open", "blurb": "43% of TPV.", "div": "braintree", "rev": "services", "products": [
            P("braintree", "Braintree", "Unbranded processing of cards, wallets, BNPL and local methods for enterprises: 43% of TPV in Q4 2025, growing in the mid-teens in Q2 2026.",
              s=["ent"], lc="move", neo=[1, "Processes every network."], src=[["FXC Intelligence: Q4 2025", FXC], ["PayPal: Q2 2026 IR newsletter", Q2NL]]),
            P("open", "PayPal Open & Complete Payments", "One platform from sole traders to enterprises (July 2025), live in the US, Germany and the UK.",
              s=["smb"], lc="open", st="new", neo=[1, "Accepts every network."], src=[["PayPal: PayPal Open, Jul 2025", OPEN]]),
            P("pos", "PayPal POS", "A point-of-sale app, card reader and integrations ⚠ Zettle not named in the 10-K.",
              s=["smb"], lc="move", neo=[1, "Accepts every network."], src=[["PayPal 10-K FY2025", TENK]]),
            P("hyperwallet", "Hyperwallet payouts & orchestration", "Mass payouts for platforms and payment orchestration, sold as value-added services ($3.4 billion of value-added services revenue in 2025).",
              s=["ent"], lc="move", neo=[None, "Rails not stated."], src=[["PayPal 10-K FY2025", TENK], ["Q4 2025 earnings call", CALL]]),
        ]},
        {"id": "2.3", "ic": "arrow-left-right", "name": "P2P & cross-border", "blurb": "Venmo, Xoom, PayPal World.", "div": "venmo", "rev": "consumer", "products": [
            P("venmop2p", "Venmo", "More than 100 million Americans use it; 67 million monthly actives in Q4 2025; Venmo users can pay PayPal users in 90 markets (March 2026).",
              s=["venmo"], lc="move", neo=[0, "Venmo's own ledger."], src=[["PayPal: Venmo to PayPal, Mar 2026", VENMOINTL], ["Q4 2025 earnings call", CALL]]),
            P("p2p", "PayPal P2P & links", "Domestic and international transfers between PayPal accounts, and shareable payment links (September 2025, US, then UK and Italy).",
              s=["con", "send"], lc="move", neo=[0, "PayPal's own ledger."], src=[["PayPal: P2P, Sep 2025", P2P]]),
            P("xoom", "Xoom", "Remittances to banks, wallets and cash pickup; no standalone figures published.",
              s=["send"], lc="move", neo=[None, "Rails not stated."],
              mc="Mastercard Move could carry Xoom's and PayPal World's payouts.",
              src=[["PayPal 10-K FY2025", TENK]]),
            P("world", "PayPal World & Pix", "Links PayPal, Venmo, Mercado Pago (MoU), UPI and Weixin Pay for about 2 billion users (announced July 2025; Weixin Pay live August 2026); Pix acceptance in Brazil (April 2026).",
              s=["send", "con"], lc="move", st="new", ay="Jul 2025", neo=[0, "Wallets and account rails."], src=[["PayPal: PayPal World, Jul 2025", WORLD], ["PayPal newsroom", INDEX]]),
            P("cashout", "Instant transfer to cards", "Cash-out to Mastercard debit (2016) and to cards over Visa Direct for PayPal and Venmo (2016).",
              s=["con", "venmo"], lc="move", ay="2016", o="P", at="Mastercard, Visa", neo=[1, "Mastercard debit and Visa Direct."],
              src=[["Mastercard and PayPal, Sep 2016", MC2016], ["PayPal and Visa, Jul 2016", VISA2016]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Debit cards", "blurb": "All on Mastercard.", "div": "paypal", "rev": "consumer", "products": [
            P("ppdebit", "PayPal Debit Mastercard (US)", "Issued by The Bancorp: 5% back in a chosen category, in Apple Pay, Google Pay and Samsung Pay; TPV up more than 50% in Q4 2025.", short="PayPal Debit (Mastercard)",
              s=["con"], lc="everyday", o="P", at="The Bancorp", neo=[2, "Mastercard, issued by The Bancorp."],
              src=[["PayPal: Debit Card", DEBIT], ["Q4 2025 earnings call", CALL]]),
            P("ukdebit", "PayPal Debit Card (UK)", "Contactless 'wherever Mastercard is accepted', relaunched on 12 November 2025 with the PayPal+ loyalty scheme ⚠ issuer not stated.",
              s=["con"], lc="everyday", ay="Nov 2025", neo=[2, "Mastercard."], src=[["PayPal: UK relaunch, Nov 2025", UK]]),
            P("detap", "In-store tap (Germany)", "Phone payments wherever Mastercard contactless is accepted (announced 5 May 2025).",
              s=["con"], lc="everyday", ay="May 2025", neo=[2, "Rides Mastercard contactless."], src=[["PayPal: Germany in-store, May 2025", GERMANY]]),
            P("venmodebit", "Venmo Debit Mastercard", "Issued by The Bancorp, with college co-brands (2025); monthly active cardholders up 40% in Q1 2025.", short="Venmo Debit (Mastercard)",
              s=["venmo"], lc="everyday", o="P", at="The Bancorp", neo=[2, "Mastercard, issued by The Bancorp."], src=[["Venmo: Debit Card", VENMODEBIT], ["PayPal: Venmo Checkout, Jun 2025", VENMO25]]),
            P("bizdebit", "PayPal Business Debit Mastercard", "A US business debit programme extended for several years in 2016.",
              s=["smb"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Mastercard and PayPal, Sep 2016", MC2016]]),
        ]},
        {"id": "2.5", "ic": "credit-card", "name": "Credit cards", "blurb": "Mastercard, but Venmo on Visa.", "div": "paypal", "rev": "consumer", "products": [
            P("cashback", "PayPal Cashback Mastercard", "Issued by Synchrony: 3% through PayPal checkout, 1.5% elsewhere.", short="Cashback (Mastercard)",
              s=["con"], lc="borrow", o="P", at="Synchrony", neo=[2, "Mastercard, issued by Synchrony."], src=[["PayPal: Cashback Mastercard", CASHBACK]]),
            P("ppcredit", "PayPal Credit card", "A physical PayPal Credit Mastercard from Synchrony (3 June 2025) with six-month promotional financing, and a Mastercard card in the UK.", short="PayPal Credit (Mastercard)",
              s=["con"], lc="borrow", ay="Jun 2025", o="P", at="Synchrony", neo=[2, "Mastercard, issued by Synchrony."],
              src=[["PayPal: PayPal Credit card, Jun 2025", PPCREDIT], ["PayPal: UK relaunch, Nov 2025", UK]]),
            P("venmocredit", "Venmo Credit Card", "Issued by Synchrony on Visa: up to 4% back on dining and entertainment, plus 1% when split, from 15 October 2026.", short="Venmo Credit (Visa)",
              s=["venmo"], lc="borrow", st="new", ay="Oct 2026", o="P", at="Synchrony, Visa", neo=[0, "Visa."],
              mc="The one PayPal-family card on Visa, and newly upgraded.",
              src=[["PayPal: Venmo Credit Card, Oct 2026", VENMOCREDIT]]),
        ]},
        {"id": "2.6", "ic": "hand-coins", "name": "Pay Later", "blurb": "More than $40bn.", "div": "paypal", "rev": "consumer", "products": [
            P("paylater", "PayPal Pay Later", "Pay in 4, Pay Monthly, Pay in 3 and Ratenzahlung in the US, Germany, France, the UK and Australia: more than $40 billion of TPV in 2025; Canada in November 2025; Amazon.de and Amazon.at instalments announced in July 2026.",
              s=["con"], lc="borrow", neo=[0, "PayPal's own lending."],
              mc="One Credential could put instalments on PayPal debit.",
              src=[["Q4 2025 earnings call", CALL], ["PayPal 10-K FY2025", TENK]]),
            P("paidy", "Paidy", "Buy now, pay later in Japan, bought in 2021 ⚠ for $2.7 billion.",
              s=["con"], lc="borrow", o="A", neo=[0, ""], src=[["PayPal 10-K FY2025", TENK], ["Wikipedia: PayPal", WIKI]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "PYUSD & crypto", "blurb": "PYUSD in 70 markets.", "div": "paypal", "rev": "services", "products": [
            P("pyusd", "PayPal USD (PYUSD)", "A stablecoin issued by Paxos, in 70 markets (March 2026), about $2.85 billion in circulation ⚠ undated.",
              s=["crypto"], lc="move", st="new", ay="Mar 2026", o="P", at="Paxos", neo=[0, "Paxos-issued stablecoin."],
              mc="Stablecoin settlement and the Crypto Credential are untested ground.",
              src=[["PayPal: PYUSD in 70 markets, Mar 2026", PYUSD], ["CoinGecko: PYUSD", COINGECKO]]),
            P("crypto", "Crypto & Pay with Crypto", "Buying, holding and sending crypto to external wallets, and Pay with Crypto for merchants (July 2025): more than 100 coins at 0.99%, pitched as up to 90% cheaper than international card processing.",
              s=["crypto", "smb"], lc="move", st="new", neo=[0, ""], src=[["PayPal: Pay with Crypto, Jul 2025", CRYPTO]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every payment: fraud and buyer protection, tokens and Mastercard's One Credential, agentic commerce with Agent Pay and every AI assistant, PayPal Ads, and Honey and rewards.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & protection", "blurb": "$397m of losses in Q2.", "div": "paypal", "rev": "grp", "products": [
            P("fraud", "Fraud, risk & protection", "Fraud prevention, buyer and seller protection, and AI scam alerts for Friends & Family payments (July 2025); transaction and credit losses of $397 million in Q2 2026.",
              s=["con", "smb"], lc="everyday", neo=[0, "PayPal's own."], src=[["PayPal 10-Q Q2 2026", TENQ], ["PayPal 10-K FY2025", TENK]]),
        ]},
        {"id": "3.2", "ic": "key-round", "name": "Tokens & credentials", "blurb": "One Credential.", "div": "paypal", "rev": "checkout", "products": [
            P("tokens", "Network tokens in the wallet", "Tokenised Mastercard cards in the wallet and in store under the 2016–17 agreements (no wallet operator fee, no steering to ACH), and Visa tokens under VDEP (2016).",
              s=["con"], lc="move", ay="Sep 2016", o="P", at="Mastercard, Visa", neo=[1, "Mastercard and Visa tokens."],
              src=[["Mastercard and PayPal, Sep 2016", MC2016], ["Mastercard and PayPal go global, Oct 2017", MC2017], ["PayPal and Visa, Jul 2016", VISA2016]]),
            P("onecredential", "Mastercard One Credential", "Co-developed with Mastercard (June 2025 ⚠ day): one credential that pays by debit, credit or instalments, to help PayPal users move 'from debit to structured credit'.", short="One Credential",
              s=["con"], lc="borrow", st="new", ay="Jun 2025", o="P", at="Mastercard", neo=[3, "Mastercard's own product ⚠."],
              src=[["Mastercard: One Credential, Jun 2025", ONECRED]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "Agentic commerce", "blurb": "Agent Pay in the wallet.", "div": "paypal", "rev": "checkout", "products": [
            P("agentpay", "Mastercard Agent Pay", "Agent Pay integrated into the PayPal wallet (27 October 2025): PayPal pilots the Agent Pay Acceptance Framework for Mastercard cards on file and its co-branded cards, with tokens, authentication and agent verification.", short="Agent Pay",
              s=["con", "ent"], lc="move", st="new", ay="Oct 2025", o="P", at="Mastercard", neo=[3, "Mastercard Agent Pay."],
              mc="A pilot; no live volume has been published.",
              src=[["PayPal: Mastercard and PayPal agentic commerce, Oct 2025", AGENTPAY]]),
            P("agentready", "Agent Ready & Store Sync", "Lets PayPal merchants accept payments on AI surfaces with fraud and dispute cover, and syndicates their catalogues to AI channels with Wix, Cymbio, BigCommerce and Shopware.",
              s=["smb", "ent"], lc="grow", st="new", neo=[0, ""], src=[["PayPal: Agentic Commerce Services, Oct 2025", ACS]]),
            P("aichannels", "PayPal in AI assistants", "The PayPal wallet in ChatGPT (October 2025), Google's AI Mode and Gemini (January 2026), Microsoft Copilot Checkout (January 2026), Perplexity, and a Claude plugin for small businesses (May 2026).",
              s=["con", "smb"], lc="move", st="new", neo=[1, "Cards on file on every network."],
              mc="Agent Pay could run across every assistant PayPal is in.",
              src=[["PayPal: OpenAI, Oct 2025", OPENAI], ["PayPal: Copilot Checkout, Jan 2026", COPILOT], ["PayPal: Anthropic, May 2026", ANTHROPIC]]),
        ]},
        {"id": "3.4", "ic": "presentation", "name": "PayPal Ads", "blurb": "Transaction-graph ads.", "div": "paypal", "rev": "services", "products": [
            P("ads", "PayPal Ads", "Commerce media built on transaction data: offsite ads (April 2025, then the UK and Germany), Transaction Graph Insights (January 2026) and identity for advertising (April 2026).",
              s=["smb", "ent"], lc="grow", st="new", neo=[0, ""], src=[["PayPal newsroom", INDEX]]),
        ]},
        {"id": "3.5", "ic": "gift", "name": "Rewards & Honey", "blurb": "PayPal+, Venmo Stash.", "div": "honey", "rev": "consumer", "products": [
            P("rewards", "PayPal+, Venmo Stash & offers", "PayPal+ in the UK (Blue, Gold and Black tiers; about 30 million eligible), Venmo Stash bundles of up to 5%, and cashback offers in the app.",
              s=["con", "venmo"], lc="grow", st="new", neo=[1, "Debit rewards ride Mastercard debit."],
              mc="Card-linked offers could feed PayPal+ and Venmo Stash.",
              src=[["PayPal: UK relaunch, Nov 2025", UK], ["PayPal: Venmo, Apr 2026", VENMO26]]),
            P("honey", "Honey", "A shopping and coupons extension, bought in 2020 for about $4 billion ⚠, criticised over affiliate cookies since December 2024 ⚠.",
              s=["con"], lc="grow", o="A", neo=[0, ""], src=[["Wikipedia: PayPal", WIKI]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What PayPal sells: the consumer wallet and balances, Venmo at about $1.7 billion of revenue, merchant services from sole traders to enterprises, and loans and Pay Later funded with partners.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Consumer accounts", "blurb": "439m accounts.", "div": "paypal", "rev": "checkout", "products": [
            P("consumer", "PayPal accounts & balances", "The consumer wallet, with interest on customer balances worth about $1.1 billion of 2025 transaction margin (implied) and 60 transactions per account a year.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["PayPal: FY2025 results", FY25], ["PayPal: Q2 2026 results", Q2]]),
        ]},
        {"id": "4.2", "ic": "users-round", "name": "Venmo", "blurb": "About $1.7bn of revenue.", "div": "venmo", "rev": "consumer", "products": [
            P("venmobiz", "Venmo monetisation", "About $1.7 billion of revenue in 2025 (about +20%), from checkout, debit, credit and instant transfers; TPV growing in the mid-teens in 2026.",
              s=["venmo"], lc="everyday", neo=[1, "Debit on Mastercard; credit on Visa."], src=[["Q4 2025 earnings call", CALL], ["PayPal: Q2 2026 IR newsletter", Q2NL]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Merchant services", "blurb": "SMB to enterprise.", "div": "braintree", "rev": "services", "products": [
            P("merchant", "Merchant services", "Payments for small businesses and enterprises, US 63% of TPV; value-added services up 14% to $3.4 billion in 2025.",
              s=["smb", "ent"], lc="everyday", neo=[1, "Accepts every network."], src=[["Q4 2025 earnings call", CALL], ["FXC Intelligence: Q4 2025", FXC]]),
        ]},
        {"id": "4.4", "ic": "landmark", "name": "Lending", "blurb": "$30bn+ to businesses.", "div": "paypal", "rev": "consumer", "products": [
            P("workingcapital", "Working Capital & Business Loans", "More than $30 billion lent to more than 420,000 businesses since 2013.",
              s=["smb"], lc="borrow", neo=[0, ""], src=[["PayPal: bank application, Dec 2025", BANK]]),
            P("bnplfunding", "Receivables funding", "Pay Later receivables sold to KKR (up to €65 billion of European loans to March 2028) and Blue Owl (US, up to $7.0 billion); $26.7 billion of loan sales in 2025.",
              s=["con"], lc="borrow", o="P", at="KKR, Blue Owl", neo=[0, ""], src=[["PayPal: KKR renewal, Nov 2025", KKR], ["PayPal 10-K FY2025", TENK]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach PayPal: the PayPal and Venmo apps, platform and software partners from Wix to Canva, sports deals, and banks.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "PayPal and Venmo.", "div": "paypal", "rev": "consumer", "products": [
            P("apps", "PayPal & Venmo apps", "The PayPal app and a redesigned Venmo app (May 2026), with Venmo in Google Play billing (August 2026).",
              s=["con", "venmo"], lc="open", neo=[0, ""], src=[["PayPal newsroom", INDEX]]),
        ]},
        {"id": "5.2", "ic": "plug", "name": "Partners", "blurb": "Wix, BigCommerce, NFL.", "div": "paypal", "rev": "checkout", "products": [
            P("isv", "Platform & software partners", "Wix (July 2025), BigCommerce Payments (October 2025), Rainforest, Paychex and Canva payment links (2026), tuition processors and Bilt rent on Venmo.",
              s=["smb"], lc="open", neo=[0, ""], src=[["PayPal newsroom", INDEX]]),
            P("sports", "Sports & college", "The NFL's P2P partner (April 2026), the Seahawks, Liverpool FC, and Big Ten and Big 12 deals.",
              s=["venmo"], lc="open", neo=[0, ""], src=[["PayPal newsroom", INDEX]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Banks", "blurb": "Deutsche Bank, EPC.", "div": "europe", "rev": "grp", "products": [
            P("banks", "Bank & scheme partners", "A Deutsche Bank partnership (January 2026) and membership of the European Payments Council, the SEPA scheme body (July 2026).",
              s=["ent"], lc="open", st="new", neo=[0, ""], src=[["PayPal newsroom", INDEX]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at PayPal", "blurb": "Every debit card, Agent Pay.", "products": [
        P("mcatpaypal", "Mastercard at PayPal", "Every PayPal and Venmo debit card in the US and UK runs on Mastercard, as do the PayPal Credit and Cashback cards. The 2016–17 agreements dropped the wallet fee and put tokenised Mastercard cards in the wallet; Agent Pay went into the wallet in October 2025 and One Credential is in co-development. Visa carries the Venmo Credit Card and Visa Direct cash-out, and has had wallet parity since 2016.",
          s=["con"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["PayPal: Mastercard and PayPal agentic commerce, Oct 2025", AGENTPAY], ["Mastercard and PayPal, Sep 2016", MC2016], ["PayPal: Venmo Credit Card, Oct 2026", VENMOCREDIT]]),
    ]},
    {"id": "pillar-market", "name": "Wallets & checkout", "blurb": "A bid, agents, stablecoins.", "products": [
        P("market", "The market", "Branded checkout growing about 2% while Braintree and Venmo grow faster; a reported $53 billion bid from Stripe and Advent; a race into AI assistants; account-to-account rails (Pix, UPI, SEPA) and stablecoins as cheaper routes than cards.",
          s=["con"], div="grp", rev="grp", src=[["PayPal: Q2 2026 IR newsletter", Q2NL], ["Semafor: Stripe and Advent bid, Jul 2026", SEMAFOR]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
