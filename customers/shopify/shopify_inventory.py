"""Shopify's layers, areas and products, read through payments, as at 17 October 2026 (see page_data.py for the format).

Figures are Shopify's own unless a source says otherwise: the Q2 2026 results (5 August 2026), the Q1 2026
results (5 May 2026) and the FY2025 10-K (February 2026), with Shopify's help centre and Editions pages for the
products. Q2 2026 operating metrics (payments penetration, Shop Pay, regional, offline and B2B growth) come from
a call summary and are marked ⚠. Q3 2026 results are due on 3 November 2026. ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://www.shopify.com/investors/press-releases/shopify-delivers-big-30-growth-across-gmv-revenue-gross-profit"
Q1 = "https://www.shopify.com/investors/press-releases/shopify-delivers-again-merchants-clear-100-billion-q1-gmv"
TENK = "https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm"
CALL = "https://transcripts.platformaeronaut.com/summaries/SHOP-2Q26-AI-Summary"
DC360 = "https://www.digitalcommerce360.com/2026/02/17/shopify-revenue-gmv-q4-2025/"
IR = "https://www.shopify.com/investors"
MCAP = "https://companiesmarketcap.com/shopify/marketcap/"
BUYBACK = "https://www.shopify.com/investors/press-releases/shopify-announces-3-billion-increase-share-repurchase-program"
LOGIC = "https://thelogic.co/news/shopify-overhauls-leadership-with-new-coo-cfo/"
COUNTRIES = "https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries"
SHOPPAY = "https://www.shopify.com/shop-pay"
SPI = "https://help.shopify.com/en/manual/payments/shop-pay-installments"
AFFIRM = "https://fintech.global/2025/02/24/affirm-and-shopify-expand-global-partnership-to-bring-shop-pay-installments-to-new-markets/"
AFFIRMUK = "https://thepaypers.com/payments/news/affirm-shopify-launch-shop-pay-installments-in-the-uk"
WINTER = "https://www.shopify.com/editions/winter2026"
SPRING = "https://www.shopify.com/editions/spring2026"
USDC = "https://www.shopify.com/news/stablecoins-on-shopify"
BLOCK = "https://www.theblock.co/news/markets/2025-06-12-shopify-coinbase-stripe-usdc-357967"
POS = "https://www.shopify.com/pos"
UCP = "https://www.shopify.com/ucp"
UCPNEWS = "https://www.shopifreaks.com/google-and-shopify-launch-universal-commerce-protocol/"
VISATAP = "https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21716.html"
NATURAILY = "https://naturaily.com/blog/agentic-commerce-shopify-guide"
HOLIDAY = "https://www.shopify.com/news/agentic-holiday-2026"
BALANCE = "https://help.shopify.com/en/manual/finance/shopify-balance"
BALCARD = "https://help.shopify.com/en/manual/finance/shopify-balance/shopify-balance-card"
CREDIT = "https://help.shopify.com/en/manual/finance/shopify-credit"
CAPITAL = "https://help.shopify.com/en/manual/finance/shopify-capital"
ABOUT = "https://www.shopify.com/about"
NEWS = "https://www.shopify.com/news"
DOORS = "https://newsroom.mastercard.com/news/press/2020/july/mastercard-expands-shopopenings-com/"
MA10K = "https://www.sec.gov/Archives/edgar/data/0001141391/000114139126000025/ma12312025-10xkasfiled.pdf"
PAYPALMA = "https://www.emarketer.com/content/paypal-taps-mastercard--openai-agentic-commerce-dominance"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "GMV · people · partners", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $378.4 billion of GMV in 2025 and $115.6 billion in Q2 2026, a founder-controlled company in Ottawa, the banks and payment firms that hold its licences, and a strategy built on payments penetration and AI.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "$378.4bn GMV in 2025.", "div": "grp", "rev": "grp", "products": [
            P("results", "GMV, revenue & 2025", "GMV of $378.4 billion in 2025 (+29%) and revenue of $11,556 million (+30%): subscription solutions $2,752 million, merchant solutions $8,804 million; operating income $1,468 million; MRR $205 million. About 7,600 staff; market value about $218 billion in October 2026.",
              s=["mer", "ent"], neo=[0, ""], src=[["Shopify 10-K FY2025", TENK], ["CompaniesMarketCap: Shopify, Oct 2026", MCAP]]),
            P("q22026", "Q2 2026", "GMV of $115.6 billion (+32%), revenue of $3,583 million (+34%), operating income of $488 million and free cash flow of $654 million (18% margin). Q1 2026 GMV passed $100 billion for a first quarter. Q3 results are due on 3 November 2026.",
              s=["mer", "ent"], st="new", neo=[0, ""], src=[["Shopify: Q2 2026 results", Q2], ["Shopify: Q1 2026 results", Q1]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & control", "blurb": "Lütke, Finkelstein, Hoffmeister.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Executive team", "Tobi Lütke (founder and CEO), Harley Finkelstein (President), Jeff Hoffmeister (CFO since late 2022). Jessica Hertz as COO and Mikhail Parakhin as CTO are not confirmed in the sources read ⚠.",
              s=["mer"], neo=[0, ""], src=[["Shopify: Q2 2026 results", Q2], ["The Logic: new COO and CFO, Sep 2022", LOGIC]]),
            P("founder", "Founder Share & listing", "Lütke held or controlled 40.09% of the votes at 31 December 2025 through Class B shares and a single Founder Share. Class A shares trade on Nasdaq as SHOP (also TSX ⚠).",
              s=["mer"], neo=[0, ""], src=[["Shopify 10-K FY2025", TENK]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Regulated partners", "blurb": "Stripe, Fifth Third, Celtic.", "div": "payments", "rev": "mer", "products": [
            P("regpartners", "Licensed partners", "'Shopify is a tech company, not a bank.' Stripe and PayPal process Shopify Payments; Stripe Payments Company provides money transmission for Shopify Balance, funds sit at Fifth Third Bank, and Celtic Bank issues the cards.",
              s=["mer"], o="P", at="Stripe, PayPal, Fifth Third, Celtic Bank", neo=[0, ""], src=[["Shopify 10-K FY2025", TENK], ["Shopify Balance", BALANCE]]),
            P("netrules", "Card rules & network fees", "The 10-K says card networks 'have discretion to both set and interpret the card rules', and counts network fees from 'Visa, Mastercard and American Express' in merchant-solutions costs.",
              s=["mer"], neo=[1, "Pays fees to every network."], src=[["Shopify 10-K FY2025", TENK]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy", "blurb": "Penetration, AI, buybacks.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "Growth plan", "About 30% growth with cash discipline: more GMV through Shopify Payments, international, offline, B2B and enterprise, and agentic commerce. Shopify licenses AI from third parties rather than building its own models. Q3 2026 guide: revenue growth in the low thirties.",
              s=["mer", "ent"], neo=[0, ""], src=[["Shopify: Q2 2026 results", Q2], ["Shopify 10-K FY2025", TENK]]),
            P("buyback", "Capital return", "A $2 billion buyback authorised in February 2026, increased by $3 billion on 2 June 2026; $1,420 million bought back in Q2 2026.",
              s=["mer"], st="new", neo=[0, ""], src=[["Shopify: $3bn buyback increase, Jun 2026", BUYBACK], ["Shopify: Q2 2026 results", Q2]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Shopify Payments in 41 countries, the Shop Pay wallet, instalments with Affirm and Klarna, in-store payments, cross-border selling, and USDC on Base.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Shopify Payments", "blurb": "65.6% of GMV.", "div": "payments", "rev": "mer", "products": [
            P("shoppayments", "Shopify Payments", "The built-in processor in 41 countries, with the UAE added for Plus in 2026. It handled $248.1 billion of GMV in 2025, 65.6% of the total, and about 68% in Q2 2026 ⚠. Visa, Mastercard, American Express and other brands are accepted.",
              s=["mer", "ent"], lc="move", o="P", at="Stripe, PayPal", neo=[1, "Accepts every network."],
              mc="The acquiring flow for millions of merchants: tokens, data and risk tools all start here.",
              src=[["Shopify 10-K FY2025", TENK], ["Shopify Payments countries", COUNTRIES], ["Q2 2026 call summary", CALL]]),
            P("psps", "Stripe & PayPal processing", "The 10-K names two payment service providers behind Shopify Payments, Stripe and PayPal. Stripe has run Shopify Payments since its launch ⚠ and also powers Shopify Balance.",
              s=["mer"], lc="move", o="P", at="Stripe, PayPal", neo=[1, "Processes every network."], src=[["Shopify 10-K FY2025", TENK]]),
            P("localmethods", "Local payment methods", "Bancontact, iDEAL, Twint, Blik, Przelewy24, MobilePay and EPS, Cartes Bancaires on POS in France, and Meses Sin Intereses in Mexico, with managed ordering by likelihood to convert.",
              s=["mer", "shop"], lc="move", st="new", neo=[0, "Local schemes and wallets."], src=[["Shopify Editions Winter '26", WINTER], ["Shopify Editions Spring '26", SPRING]]),
        ]},
        {"id": "2.2", "ic": "wallet", "name": "Shop Pay", "blurb": "250m+ shoppers.", "div": "shoppay", "rev": "mer", "products": [
            P("shoppay", "Shop Pay", "The saved-details checkout: 250 million+ shoppers, 1 in 5 buyers choose it, and up to 50% better conversion than guest checkout (consultancy study, April 2023). It stores Visa, Mastercard and American Express cards; Apple Pay added in Winter '26. Shop Pay GMV +53% in Q2 2026 ⚠.",
              s=["shop", "mer"], lc="move", neo=[1, "Stores cards on every network."],
              mc="Network tokens and Click to Pay could sit behind Shop Pay's stored cards.",
              src=[["Shop Pay", SHOPPAY], ["Shopify Editions Spring '26", SPRING], ["Q2 2026 call summary", CALL]]),
            P("shoppayanywhere", "Shop Pay on any platform", "From Spring '26 any brand on any platform can offer Shop Pay, with simpler onboarding; Shop Pay also reminds subscribers before a card expires.",
              s=["mer", "shop"], lc="open", st="new", neo=[1, "Cards on every network."], src=[["Shopify Editions Spring '26", SPRING], ["Shopify Editions Winter '26", WINTER]]),
        ]},
        {"id": "2.3", "ic": "hand-coins", "name": "Instalments", "blurb": "Affirm; Klarna.", "div": "shoppay", "rev": "mer", "products": [
            P("installments", "Shop Pay Installments", "Lent by Affirm's partners in the US, Canada and the UK: interest-free or monthly plans up to 24 months, APR 0–36%, $35 to $30,000. Affirm became exclusive in the US and Canada in February 2025; the UK followed on 10 December 2025, with Australia and Western Europe planned.",
              s=["shop"], lc="borrow", o="P", at="Affirm", neo=[0, "Affirm loan, off the card networks."],
              src=[["Shop Pay Installments", SPI], ["fintech.global: Affirm and Shopify, Feb 2025", AFFIRM], ["The Paypers: UK launch, Dec 2025", AFFIRMUK]]),
            P("klarna", "Klarna in Shopify Payments", "Klarna offered inside Shopify Payments in eight more countries, including Belgium, France and Ireland (Winter '26).",
              s=["shop"], lc="borrow", st="new", o="P", at="Klarna", neo=[0, ""], src=[["Shopify Editions Winter '26", WINTER]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "In-store", "blurb": "POS, Tap to Pay.", "div": "shopify", "rev": "mer", "products": [
            P("pos", "Shopify POS", "Point of sale on the same back office, with POS Pro, POS Hub and the Verifone Victa Mobile reader (US and Canada). Offline GMV +32% in Q2 2026 ⚠.",
              s=["retail"], lc="move", o="P", at="Verifone", neo=[1, "Accepts every network."], src=[["Shopify POS", POS], ["Shopify Editions Spring '26", SPRING], ["Q2 2026 call summary", CALL]]),
            P("taptopay", "Tap to Pay", "Tap to Pay on iPhone, added in Germany, Ireland, Spain and New Zealand in Winter '26, and Tap to Pay on Android.",
              s=["retail"], lc="move", st="new", o="P", at="Apple", neo=[1, "Contactless cards on every network."], src=[["Shopify Editions Winter '26", WINTER], ["Shopify POS", POS]]),
        ]},
        {"id": "2.5", "ic": "earth", "name": "Cross-border", "blurb": "Markets, Global-e.", "div": "payments", "rev": "mer", "products": [
            P("markets", "Shopify Markets & Managed Markets", "Selling abroad with local prices and checkout; Managed Markets and Shop Pay with Global-e, where international orders go through Global-e. International GMV +37% in Q2 2026 ⚠.",
              s=["mer", "ent"], lc="move", o="P", at="Global-e", neo=[None, "Network split not stated."],
              mc="Cross-border card volume is where FX and currency tools earn.",
              src=[["Shopify Editions Winter '26", WINTER], ["Q2 2026 call summary", CALL]]),
            P("multicurrency", "Multi-currency payouts", "Payouts in more than one currency in the US, Hong Kong and Singapore (Spring '26).",
              s=["mer"], lc="everyday", st="new", neo=[0, ""], src=[["Shopify Editions Spring '26", SPRING]]),
        ]},
        {"id": "2.6", "ic": "coins", "name": "Stablecoins", "blurb": "USDC on Base.", "div": "payments", "rev": "mer", "products": [
            P("usdc", "USDC payments", "USDC on Base in Shopify Payments from 12 June 2025, with Coinbase and Stripe: 'authorise now, capture later', local-currency settlement by default; Stripe said 34 countries. Spring '26 added cashback for USDC payers and other chains.",
              s=["shop", "mer"], lc="move", st="new", ay="Jun 2025", o="P", at="Coinbase, Stripe", neo=[0, "USDC on Base."],
              mc="Shopify calls Base 'like a credit card network'; stablecoin settlement is a direct alternative to the card rails.",
              src=[["Shopify: stablecoins, Jun 2025", USDC], ["The Block: Shopify USDC, Jun 2025", BLOCK], ["Shopify Editions Spring '26", SPRING]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every sale: fraud and chargeback tools against rising losses, agentic commerce through UCP and AI channels, the Catalog and checkout tools developers build on, and Sidekick, the merchant's AI assistant.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & risk", "blurb": "$417m of losses in 2025.", "div": "payments", "rev": "mer", "products": [
            P("fraud", "Fraud scoring & chargeback alerts", "Better fraud scoring against card-testing attacks and chargeback monitoring alerts (Spring '26). No network partner is named ⚠.",
              s=["mer"], lc="everyday", st="new", neo=[None, "No network named."],
              mc="Card testing and disputes are what Decision Intelligence and Ethoca alerts address.",
              src=[["Shopify Editions Spring '26", SPRING]]),
            P("losses", "Transaction & loan losses", "$417 million in 2025 (+84%) and $141 million in Q2 2026 (from $80 million), covering payments and Capital lending.",
              s=["mer"], lc="everyday", neo=[0, ""], src=[["Shopify 10-K FY2025", TENK], ["Shopify: Q2 2026 results", Q2]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "Agentic commerce", "blurb": "UCP, Copilot, ChatGPT.", "div": "ai", "rev": "mer", "products": [
            P("ucp", "Universal Commerce Protocol", "An open standard co-developed with Google, launched on 12 January 2026 with Etsy, Wayfair, Target and Walmart, and endorsed by more than 20 firms including Mastercard, Visa, American Express, Stripe and Adyen. Payment handlers are negotiated per cart; Shop Pay is built in.",
              s=["dev", "mer"], lc="move", st="new", ay="Jan 2026", o="P", at="Google", neo=[0, "Mastercard an endorser, not a named handler."],
              mc="Mastercard backs UCP but has no named role in its payment handlers.",
              src=[["Shopify: UCP", UCP], ["Shopifreaks: UCP launch, Jan 2026", UCPNEWS]]),
            P("copilot", "Checkout in Copilot", "Shoppers buy inside Microsoft Copilot through UCP, with Shop Pay; Meta ads to follow (Spring '26).",
              s=["shop"], lc="move", st="new", o="P", at="Microsoft", neo=[1, "Shop Pay's saved cards, any network."],
              mc="Agent-made card payments are what Agent Pay and agentic tokens are for.",
              src=[["Shopify Editions Spring '26", SPRING]]),
            P("chatgpt", "ChatGPT Instant Checkout", "OpenAI said on 29 September 2025 that more than a million Shopify merchants would 'soon' sell through Instant Checkout on Stripe's Agentic Commerce Protocol; fewer than 30 Shopify stores had true in-chat checkout by mid-2026 ⚠.",
              s=["shop"], lc="move", st="flux", o="P", at="OpenAI, Stripe", neo=[1, "Cards on any network via Stripe."], src=[["Naturaily: agentic commerce on Shopify", NATURAILY]]),
            P("agentapprove", "Approvals for personal agents", "Shoppers using personal AI agents such as OpenClaw and Hermes approve purchases through Shop (Spring '26).",
              s=["shop"], lc="move", st="new", neo=[None, ""], src=[["Shopify Editions Spring '26", SPRING]]),
            P("visatap", "Visa Trusted Agent Protocol", "Shopify was among the early partners giving feedback on Visa's protocol for recognising AI agents, launched with Cloudflare on 14 October 2025.", short="Visa agent protocol",
              s=["dev"], lc="move", st="new", ay="Oct 2025", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa is on record with Shopify on agent identity; Mastercard is not.",
              src=[["Visa: Trusted Agent Protocol, Oct 2025", VISATAP]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "Catalog & checkout tools", "blurb": "MCP, Checkout Kit.", "div": "ai", "rev": "mer", "products": [
            P("catalog", "Shopify Catalog", "Billions of products from Shopify merchants, searchable through MCP tools or REST; the Catalog API adds image search, 50-product lookup and sponsored products (developer preview).",
              s=["dev"], lc="grow", st="new", neo=[0, ""], src=[["Shopify Editions Winter '26", WINTER], ["Shopify Editions Spring '26", SPRING]]),
            P("checkoutkit", "Checkout Kit & Checkout MCP", "Shopify checkout inside apps and AI conversations, opening in a pop-up or new tab; UCP's Embedded Commerce Protocol grew out of Checkout Kit.",
              s=["dev"], lc="move", st="new", neo=[0, ""], src=[["Shopify Editions Winter '26", WINTER], ["Shopify: UCP", UCP]]),
        ]},
        {"id": "3.4", "ic": "sparkles", "name": "Sidekick", "blurb": "The merchant's AI.", "div": "ai", "rev": "sub", "products": [
            P("sidekick", "Sidekick", "Shopify's AI assistant for merchants: Sidekick Pulse recommendations, custom app generation, multi-step tasks, and checking Shopify Balance and moving money with approval (not in all regions).",
              s=["mer"], lc="everyday", st="new", neo=[0, ""], src=[["Shopify Editions Winter '26", WINTER], ["Shopify 10-K FY2025", TENK]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What Shopify sells: subscriptions from Basic to Plus, merchant solutions led by payments, B2B selling, Shopify Capital, the Balance account and Visa cards, and Collective and Catalog for brands beyond Shopify.",
    "tiles": [
        {"id": "4.1", "ic": "receipt-text", "name": "Subscriptions", "blurb": "$2,752m in 2025.", "div": "shopify", "rev": "sub", "products": [
            P("plans", "Plans & apps", "Basic, Grow, Advanced and Plus plans, POS Pro, themes and apps: $2,752 million in 2025 (+17%) and $802 million in Q2 2026 (+22%); MRR $221 million.",
              s=["mer"], lc="open", neo=[0, ""], src=[["Shopify 10-K FY2025", TENK], ["Shopify: Q2 2026 results", Q2]]),
            P("plus", "Shopify Plus & enterprise", "Most GMV comes from Plus and enterprise merchants; 2025 wins included Starbucks, Estée Lauder and Coach, and Q4 2025 added General Motors, L'Oréal and Sonos.",
              s=["ent"], lc="open", neo=[0, ""], src=[["Shopify 10-K FY2025", TENK], ["Digital Commerce 360, Feb 2026", DC360]]),
        ]},
        {"id": "4.2", "ic": "chart-column", "name": "Merchant solutions", "blurb": "$8,804m in 2025.", "div": "payments", "rev": "mer", "products": [
            P("mersol", "Merchant solutions", "Payments and currency conversion, lending, shipping labels, POS hardware, referral fees and advertising: $8,804 million in 2025 (+35%) and $2,781 million in Q2 2026 (+37%).",
              s=["mer", "ent"], lc="everyday", neo=[1, "Card fees on every network."], src=[["Shopify 10-K FY2025", TENK], ["Shopify: Q2 2026 results", Q2]]),
            P("campaigns", "Shop Campaigns & ads", "Advertising products inside merchant solutions; Shop Campaigns now reach ChatGPT (Spring '26).",
              s=["mer"], lc="grow", st="new", neo=[0, ""], src=[["Shopify 10-K FY2025", TENK], ["Shopify Editions Spring '26", SPRING]]),
        ]},
        {"id": "4.3", "ic": "briefcase-business", "name": "B2B", "blurb": "B2B GMV +76%.", "div": "shopify", "rev": "mer", "products": [
            P("b2b", "Shopify B2B", "Wholesale selling on every plan since Spring '26, with company catalogs, vaulted cards charged through Shopify Flow, and ERP links. B2B GMV +96% in 2025 and +76% in Q2 2026 ⚠.",
              s=["biz", "ent"], lc="move", neo=[1, "Cards on file, any network, and ACH."],
              mc="Virtual cards and payment controls for business buyers are open ground.",
              src=[["Shopify Editions Spring '26", SPRING], ["Digital Commerce 360, Feb 2026", DC360], ["Q2 2026 call summary", CALL]]),
            P("ach", "ACH at checkout", "ACH bank payments at checkout through Shopify Payments for B2B (US, Plus).",
              s=["biz"], lc="move", st="new", neo=[0, "ACH."], src=[["Shopify Editions Winter '26", WINTER]]),
        ]},
        {"id": "4.4", "ic": "trending-up", "name": "Shopify Capital", "blurb": "$2.2bn of loans.", "div": "capital", "rev": "mer", "products": [
            P("capital", "Shopify Capital", "Merchant cash advances and loans in nine countries (Australia, Canada, France, Germany, Ireland, the Netherlands, Spain, the UK, the US), repaid from sales or the Payments balance, with Capital Flex in the US; $2,184 million outstanding at 30 June 2026. The lending bank is not named ⚠.",
              s=["mer"], lc="borrow", neo=[0, ""], src=[["Shopify Capital", CAPITAL], ["Shopify: Q2 2026 results", Q2], ["Shopify Editions Spring '26", SPRING]]),
        ]},
        {"id": "4.5", "ic": "wallet-cards", "name": "Balance & Credit", "blurb": "Visa cards, Celtic Bank.", "div": "finance", "rev": "mer", "products": [
            P("balance", "Shopify Balance", "A US money account for sales payouts, with automatic payout splits, same-day ACH and cash deposits at retailers; Stripe Payments Company provides money transmission and funds sit at Fifth Third Bank.",
              s=["mer"], lc="everyday", o="P", at="Stripe, Fifth Third Bank", neo=[0, ""], src=[["Shopify Balance", BALANCE], ["Shopify Editions Winter '26", WINTER]]),
            P("balancecard", "Shopify Balance Visa Commercial card", "Powered by Stripe and 'issued by Celtic Bank pursuant to a license from Visa U.S.A. Inc.', with cashback, partner offers and staff cards with spend controls. Whether an earlier card was on another network is not verified ⚠.", short="Balance card (Visa)",
              s=["mer"], lc="everyday", o="P", at="Celtic Bank, Stripe, Visa", neo=[0, "Visa."],
              mc="Shopify's own merchant card is Visa's.",
              src=[["Shopify Balance card", BALCARD], ["Shopify Editions Winter '26", WINTER]]),
            P("credit", "Shopify Credit", "A US pay-in-full business charge card, 'issued by Celtic Bank pursuant to a license from Visa U.S.A. Inc.': 3% cashback on up to $250,000 in a top category, then 1%, with repayment from sales over 10 months for a fee. Launched in 2023 ⚠.", short="Shopify Credit (Visa)",
              s=["mer"], lc="borrow", o="P", at="Celtic Bank, Visa", neo=[0, "Visa."], src=[["Shopify Credit", CREDIT], ["Shopify Editions Winter '26", WINTER]]),
        ]},
        {"id": "4.6", "ic": "network", "name": "Beyond Shopify stores", "blurb": "Collective, agentic plan.", "div": "ai", "rev": "sub", "products": [
            P("collective", "Shopify Collective", "Merchants sell each other's products; extended to 35 more countries in Winter '26 and to Australia in Spring '26.",
              s=["mer"], lc="grow", neo=[0, ""], src=[["Shopify Editions Winter '26", WINTER], ["Shopify Editions Spring '26", SPRING]]),
            P("agenticplan", "Agentic plan", "Businesses not on Shopify can sync products to Shopify Catalog and sell in AI channels and the Shop app (Spring '26).",
              s=["ent", "dev"], lc="grow", st="new", neo=[0, ""], src=[["Shopify Editions Spring '26", SPRING]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How merchants and shoppers reach Shopify: the admin and twice-yearly Editions, the Shop app, more than 21,000 apps and the partners behind them, and AI channels from ChatGPT to Copilot.",
    "tiles": [
        {"id": "5.1", "ic": "monitor", "name": "Admin & Editions", "blurb": "150+ updates twice a year.", "div": "shopify", "rev": "sub", "products": [
            P("admin", "Shopify admin & app", "The back office for millions of merchants in more than 175 countries; 44% of merchants are in the US, 31% in EMEA, 16% in Asia-Pacific and 5% in Canada.",
              s=["mer", "retail"], lc="open", neo=[0, ""], src=[["Shopify 10-K FY2025", TENK], ["Shopify investors", IR]]),
            P("editions", "Shopify Editions", "150+ product updates twice a year; Winter '26 'Renaissance' and Spring '26 'Everywhere'.",
              s=["mer", "dev"], lc="open", neo=[0, ""], src=[["Shopify Editions Spring '26", SPRING], ["About Shopify", ABOUT]]),
        ]},
        {"id": "5.2", "ic": "smartphone", "name": "Shop app", "blurb": "Where shoppers return.", "div": "shoppay", "rev": "mer", "products": [
            P("shopapp", "Shop app", "The shopper app behind Shop Pay, with order tracking and a 9% higher repurchase rate; its feed is being reworked for discovery in 2026.",
              s=["shop"], lc="open", neo=[1, "Holds Shop Pay cards on every network."], src=[["Shop Pay", SHOPPAY], ["Digital Commerce 360, Feb 2026", DC360]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Apps & partners", "blurb": "21,000+ apps.", "div": "shopify", "rev": "sub", "products": [
            P("appstore", "Shopify App Store", "More than 21,000 apps at the end of 2025.",
              s=["dev", "mer"], lc="open", neo=[0, ""], src=[["Shopify 10-K FY2025", TENK]]),
            P("partners", "Partner ecosystem", "Agencies, developers and payment partners (Stripe, PayPal, Affirm, Klarna, Global-e, Coinbase); 'The next era of commerce, built by partners' (28 July 2026).",
              s=["dev"], lc="open", o="P", at="Stripe, PayPal, Affirm", neo=[0, ""], src=[["Shopify news", NEWS], ["Shopify 10-K FY2025", TENK]]),
            P("digitaldoors", "Mastercard Digital Doors", "Mastercard rolled out Digital Doors for US small businesses with BigCommerce, Hello Alice and Shopify on 8 July 2020, with Click to Pay and cybersecurity tools. No later activity was found ⚠.",
              s=["mer"], lc="open", st="unconf", ay="Jul 2020", o="P", at="Mastercard", neo=[3, "Mastercard's own programme."],
              src=[["Mastercard: Digital Doors, Jul 2020", DOORS]]),
        ]},
        {"id": "5.4", "ic": "globe", "name": "AI channels", "blurb": "ChatGPT, Copilot, Google.", "div": "ai", "rev": "mer", "products": [
            P("aichannels", "Agentic Storefronts", "One setup places products in ChatGPT, Copilot, Perplexity and Google's AI channels; Shopify says its syndicated data drives twice the conversion in AI chats. Orders from AI search were up 15 times from January 2025 to early 2026; 65% of shoppers plan to use AI this holiday season.",
              s=["mer", "shop"], lc="grow", st="new", neo=[0, ""],
              mc="The storefront where agent payments start.",
              src=[["Shopify Editions Winter '26", WINTER], ["Shopify Editions Spring '26", SPRING], ["Shopify: agentic holiday, Oct 2026", HOLIDAY], ["Digital Commerce 360, Feb 2026", DC360]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Shopify", "blurb": "Accepted everywhere, no card of its own.", "products": [
        P("mcatshopify", "Mastercard at Shopify", "Every Shopify Payments, Shop Pay and POS checkout takes Mastercard, and Mastercard cards sit in Shop Pay's 250 million+ wallets. Mastercard worked with Shopify on Digital Doors in 2020 and endorses UCP. Shopify's own cards, Balance and Credit, are Visa from Celtic Bank, and Shopify gave feedback on Visa's agent protocol. No Shopify announcement on Agent Pay, tokens or Click to Pay since 2020 was found.",
          s=["mer"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Shop Pay", SHOPPAY], ["Mastercard: Digital Doors, Jul 2020", DOORS], ["Shopify Balance card", BALCARD], ["Visa: Trusted Agent Protocol, Oct 2025", VISATAP]]),
    ]},
    {"id": "pillar-market", "name": "Agentic commerce", "blurb": "Protocols, tokens, stablecoins.", "products": [
        P("market", "The market", "Commerce is moving into AI agents: UCP from Google and Shopify, OpenAI and Stripe's Agentic Commerce Protocol, Visa's Trusted Agent Protocol, and USDC on Base. Mastercard's Agent Pay launched in April 2025, reached all US issuers in November 2025 and went global from early 2026; PayPal, one of Shopify's two processors, plans to integrate it.",
          s=["dev"], div="grp", rev="grp", src=[["Mastercard 10-K FY2025", MA10K], ["eMarketer: PayPal and Mastercard", PAYPALMA], ["Shopifreaks: UCP launch, Jan 2026", UCPNEWS]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
