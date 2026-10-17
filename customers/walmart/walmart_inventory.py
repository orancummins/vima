"""Walmart's layers, areas and products, read through payments, as at 17 October 2026 (see page_data.py for the format).

Figures are Walmart's own unless a source says otherwise: the Q2 FY27 results (20 August 2026), the FY26 10-K
(13 March 2026) and the Q2 FY27 10-Q, with OnePay's newsroom, Synchrony's and Klarna's releases and press for the
card, lending and fintech programmes. Walmart's fiscal year ends on 31 January; Q3 FY27 results are due in
mid-November. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

SEC = "https://www.sec.gov/Archives/edgar/data/104169/"
TENK = SEC + "000010416926000055/wmt-20260131.htm"
TENQ = SEC + "000010416926000154/wmt-20260731.htm"
Q2 = SEC + "000010416926000145/earningsreleasefy27q2.htm"
Q2P = SEC + "000010416926000145/earningspresentationfy27.htm"
Q4 = SEC + "000010416926000032/earningsreleasefy26q4.htm"
NASDAQ = SEC + "000010416925000177/wmt-20251119.htm"
CEOUS = SEC + "000010416926000023/wmt-20260115.htm"
WMTQ2 = "https://corporate.walmart.com/news/2026/08/20/walmart-releases-q2-fy27-earnings"
MCAP = "https://companiesmarketcap.com/walmart/marketcap/"
SYFONE = "https://www.synchrony.com/contenthub/newsroom/onepay-and-synchrony-to-launch-new-industry-leading-credit-card.html"
SAMS = "https://www.synchrony.com/contenthub/newsroom/synchrony-renews-30-year-relationship-dedicated-to-enhancing.html"
CARD = "https://www.onepay.com/credit-card"
CNBC = "https://www.nbcdfw.com/news/business/money-report/walmart-is-using-its-own-fintech-firm-to-provide-credit-cards-after-dumping-capital-one/3859191/"
DT = "https://www.digitaltransactions.net/?p=1329081"
KLARNA = "https://www.klarna.com/international/press/klarna-announces-partnership-with-onepay-to-exclusively-power-installment/"
AFFIRM = "https://www.paymentsdive.com/news/affirm-coo-walmart-deal-was-uneconomic/743944/"
OP = "https://www.onepay.com/newsroom"
BUILDER = OP + "/builder-card"
TEMPO = OP + "/tempo-partnership"
FCD = OP + "/financial-crimes-detective"
AGENTS = OP + "/onepay-for-agents"
OPENUSD = OP + "/introducing-open-usd"
APPLEPAY = OP + "/onepay-apple-pay"
CHATGPT = OP + "/onepay-chatgptanddots"
SIXM = "https://www.shopifreaks.com/walmart-backed-fintech-onepay-hits-6m-monthly-users-and-50b-in-annualized-payments-as-it-pushes-to-become-a-payment-super-app/"
CRYPTO = "https://www.crowdfundinsider.com/?p=254009"
TAP = "https://www.supermarketnews.com/grocery-technology/walmart-rolls-out-tap-to-pay-checkout"
SAMSUNG = "https://www.sammyfans.com/2026/08/24/walmart-will-finally-let-customers-pay-with-samsung-pay/"
PDOUT = "https://www.paymentsdive.com/news/walmart-wants-out-of-card-class/807972/"
PDSLAM = "https://www.paymentsdive.com/news/walmart-slams-card-fee-pact-again/830395/"
PDURGE = "https://www.paymentsdive.com/news/visa-mastercard-urge-court-to-approve-fee-settlement/833241/"
DRHP = "https://entrackr.com/news/phonepe-files-updated-drhp-walmart-to-sell-9-stake-via-ofs-11020697"
PPIPO = "https://www.chittorgarh.com/ipo/phonepe-ipo/2634/"
PPDELAY = "https://www.jainam.in/blog/phonepe-ipo-details-review/"
SUPER = "https://www.outlookbusiness.com/start-up/news/flipkart-pumps-30-mn-into-supermoney-as-fintech-push-gains-momentum"
CASHI = "https://www.peru-retail.com/walmart-lanza-cuenta-cashi-y-tarjeta-de-debito-para-competir-con-nu-y-spin/"
CASHIPILOT = "https://www.bloomberglinea.com/latinoamerica/mexico/walmart-de-mexico-comienza-pruebas-de-cuentas-de-debito-con-clientes/"
MONEYCARD = "https://www.walmartmoneycard.com/"
CARECREDIT = "https://www.grocerydive.com/press-release/20260413-synchronys-carecredit-credit-card-now-accepted-on-walmartcom/"
SPARKY = "https://ppc.land/walmarts-chatgpt-checkout-flopped-heres-what-comes-next/"
UCP = "https://www.theregister.com/2026/01/12/google_gemini_agentic_ai_shopping_protocol/"
BMO = "https://newsroom.bmo.com/2025-12-03-BMO-and-Walmart-Canada-Team-Up-to-Make-Shopping-Fast,-Convenient-and-Affordable"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "sales · people · licences · the fee fight", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $713.2 billion of revenue in FY26 and 2.1 million associates, a new chief executive, the partner banks and licences behind its money services, the fight over card fees, and a strategy that leans on advertising, membership and financial services.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "$713.2bn in FY26.", "div": "grp", "rev": "grp", "products": [
            P("results", "Revenue & segments", "Revenue of $713.2 billion in the year to 31 January 2026 (+4.7%): Walmart U.S. $483.0 billion, International $130.4 billion, Sam's Club U.S. $93.0 billion; operating income $29.8 billion. Q2 FY27 revenue of $187.9 billion (+5.9%), with global eCommerce up 23%. Market value about $943 billion at 16 October 2026; about 2.1 million associates and 11,000 stores and clubs.",
              s=["shop"], neo=[0, ""], src=[["Walmart: Q2 FY27 results", Q2], ["Walmart 10-K FY26", TENK], ["CompaniesMarketCap: Walmart, Oct 2026", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Furner, Rainey, Guggina.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Executive officers & board", "John Furner, CEO since 1 February 2026 in succession to Doug McMillon; John David Rainey, CFO since 2022 and formerly PayPal's CFO; David Guggina (Walmart U.S.), Chris Nicholas (International), Latriece Watkins (Sam's Club), Daniel Danker (AI Acceleration); Greg Penner chairs the board. Omer Ismail runs OnePay. Listing moved from the NYSE to Nasdaq on 8 December 2025.",
              s=["shop"], neo=[0, ""], src=[["Walmart 10-K FY26", TENK], ["Walmart 8-K, Jan 2026", CEOUS], ["Walmart 8-K: Nasdaq, Nov 2025", NASDAQ]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Licences & partner banks", "blurb": "Banks behind OnePay and Cashi.", "div": "onepay", "rev": "grp", "products": [
            P("partnerbanks", "Partner banks & licences", "OnePay's accounts sit with Coastal Community Bank and Lead Bank and it is not seeking a charter; its credit cards are Synchrony's. Walmex's Cashi holds a Mexican e-money (IFPE) licence. The 10-K lists money transfers, prepaid, co-branded cards, instalment lending, earned wage access and 'limited access to cryptocurrency' as regulated services.",
              s=["onepay", "intl"], o="P", at="Coastal Community Bank, Lead Bank, Synchrony", neo=[0, ""], src=[["Shopifreaks: OnePay, Jun 2026", SIXM], ["Perú Retail: Cuenta Cashi, Mar 2025", CASHI], ["Walmart 10-K FY26", TENK]]),
            P("mtaml", "Money transfer compliance review", "A US Attorney's review of the anti-fraud and anti-money-laundering programme for the money transfers Walmart sells as an agent; the last subpoena was in August 2020 and Walmart says it will defend the matter if pursued.",
              s=["shop"], st="flux", neo=[0, ""], src=[["Walmart 10-K FY26", TENK]]),
        ]},
        {"id": "1.4", "ic": "flag", "name": "The card-fee fight", "blurb": "Lead objector to the settlement.", "div": "grp", "rev": "grp", "products": [
            P("objection", "Walmart's objection", "Walmart asked Judge Brian Cogan in December 2025 to decertify the merchant class or let large national merchants opt out, and to negotiate interchange with issuers directly; its 299-page objection in September 2026 calls the relief 'temporary and meager'. Visa and Mastercard call the objectors 'a vocal minority'. Final approval hearing: 16 November 2026.", short="Settlement objection",
              s=["shop"], st="flux", ay="Dec 2025", neo=[0, "Against Visa and Mastercard."],
              mc="Mastercard's largest US merchant is its loudest courtroom critic.",
              src=[["Payments Dive: Walmart wants out, Dec 2025", PDOUT], ["Payments Dive: Walmart slams pact, Sep 2026", PDSLAM], ["Payments Dive: networks urge approval, Oct 2026", PDURGE]]),
            P("settlement", "The Visa–Mastercard settlement", "Proposed in November 2025 and preliminarily approved in June 2026: credit interchange cut by 10 basis points for five years, standard consumer cards at 1.25% for eight years, merchants may decline some premium and commercial cards, and new surcharge and discount rights.",
              s=["shop"], st="flux", ay="Nov 2025", o="P", at="Visa, Mastercard", neo=[1, "A Visa and Mastercard settlement."],
              src=[["Payments Dive: Walmart slams pact, Sep 2026", PDSLAM], ["Payments Dive: networks urge approval, Oct 2026", PDURGE]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Ads, membership, money.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "Strategy", "Advertising, membership, marketplace and fulfilment, and financial services as 'mutually reinforcing' parts of the store model; advertising grew 46% to nearly $6.4 billion in FY26 and membership fees reached $4.4 billion. FY27 guidance was raised in August 2026 to net sales growth of 4% to 5%.",
              s=["shop", "plus"], neo=[0, ""], src=[["Walmart 10-K FY26", TENK], ["Walmart: Q4 FY26 results", Q4], ["Walmart: Q2 FY27 results", Q2]]),
            P("deals", "Deals since 2018", "Majority stakes in Flipkart and PhonePe (2018); OnePay set up with Ribbit Capital (2021); Walmex's purchase of Trafalgar, the fintech behind Cashi (March 2023); an early exit from Capital One (2023–24); VIZIO for advertising ⚠ completion date not re-verified.",
              s=["shop"], o="A", neo=[0, ""], src=[["Walmart 10-K FY26", TENK], ["CNBC: OnePay and Capital One, Jun 2025", CNBC], ["Bloomberg Línea: Cashi, Apr 2025", CASHIPILOT]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: OnePay's cards, a Mastercard card back with Synchrony, the Sam's Club Mastercard, checkout that is turning contactless, Klarna and Upgrade for credit, prepaid and money services, and a first step into crypto and stablecoins.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "OnePay cards", "blurb": "CashRewards on Mastercard.", "div": "onepay", "rev": "us", "products": [
            P("cashrewards", "OnePay CashRewards Mastercard", "Synchrony-issued Mastercard inside the OnePay app since autumn 2025: 3% back at Walmart (5% for Walmart+ members), 1.5% elsewhere, no annual fee. Announced on 9 June 2025 with Linda Kirkpatrick, Mastercard's President, Americas; in Apple Pay since 21 August 2026.", short="CashRewards (Mastercard)",
              s=["onepay", "plus", "shop"], lc="borrow", st="new", ay="Sep 2025", o="P", at="Synchrony, Mastercard", neo=[2, "Mastercard, issued by Synchrony."],
              mc="Walmart's flagship US credit card stayed on Mastercard through two issuers.",
              src=[["Synchrony: OnePay card, Jun 2025", SYFONE], ["OnePay CashRewards card", CARD], ["OnePay: Apple Pay, Aug 2026", APPLEPAY]]),
            P("spendcard", "OnePay Walmart Spend Card", "A closed-loop card for Walmart and Walmart.com only, offered to applicants who do not qualify for CashRewards; Synchrony issues it.", short="Spend Card (closed loop)",
              s=["onepay", "shop"], lc="borrow", st="new", ay="Sep 2025", o="P", at="Synchrony", neo=[0, "Closed loop, no network."], src=[["OnePay CashRewards card", CARD], ["Synchrony: OnePay card, Jun 2025", SYFONE]]),
            P("buildercard", "OnePay Builder Card", "A credit-builder card for OnePay Cash customers with no deposit, credit check, interest or late fees, reported to all three bureaus (23 April 2026); Apple Wallet support due in autumn 2026. Issuer and network not stated ⚠.", short="Builder Card",
              s=["onepay"], lc="borrow", st="new", ay="Apr 2026", neo=[None, "Network not stated ⚠."],
              mc="An open network choice for a card aimed at people building credit.",
              src=[["OnePay: Builder Card, Apr 2026", BUILDER]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Sam's & past cards", "blurb": "Sam's Club Mastercard.", "div": "sams", "rev": "sams", "products": [
            P("samsmc", "Sam's Club Mastercard", "Synchrony's Sam's Club consumer Mastercard plus business and commercial cards, renewed in January 2025 after 30 years.", short="Sam's Club (Mastercard)",
              s=["sams"], lc="borrow", o="P", at="Synchrony", neo=[2, "Consumer card on Mastercard."], src=[["Synchrony: Sam's Club renewal, Jan 2025", SAMS]]),
            P("capone", "Capital One Walmart Rewards Mastercard", "Walmart's card with Capital One from 2019, about 10 million customers and $8.5 billion of loans; Walmart sued to leave in 2023 and the partnership ended in 2024 ⚠ dates vary by source.", short="Capital One card (retired)",
              s=["shop"], lc="borrow", st="retired", ay="2019", o="P", at="Capital One", neo=[2, "Mastercard."], src=[["CNBC: OnePay and Capital One, Jun 2025", CNBC], ["Digital Transactions: Synchrony and OnePay, Jun 2025", DT]]),
        ]},
        {"id": "2.3", "ic": "store", "name": "Checkout", "blurb": "Contactless from August 2026.", "div": "walmart", "rev": "us", "products": [
            P("accept", "Card acceptance", "Cash, checks, credit and debit cards, EBT, mobile payments, private-label and gift cards; network rules named for Visa, Mastercard, American Express and Discover, with PCI standards. CareCredit has been accepted on Walmart.com since April 2026.",
              s=["shop", "sams"], lc="move", neo=[1, "Accepts every network."], src=[["Walmart 10-K FY26", TENK], ["Grocery Dive: CareCredit on Walmart.com, Apr 2026", CARECREDIT]]),
            P("taptopay", "Tap to pay", "NFC checkout from 24 August 2026 at selected stores, all US Walmart and Sam's Club stores by the end of 2026 and fuel stations by the end of 2027: Apple Pay, Google Pay, Samsung Pay, Garmin Pay and contactless cards. Scan & Go does not take wallets.", short="Tap to pay",
              s=["shop", "sams"], lc="move", st="new", ay="Aug 2026", neo=[1, "Every network's contactless cards and tokens."],
              mc="Brings tokenised wallet payments to about 5,200 US stores and clubs for the first time.",
              src=[["Supermarket News: tap to pay, Aug 2026", TAP], ["Sammy Fans: Samsung Pay, Aug 2026", SAMSUNG]]),
            P("walmartpay", "Walmart Pay", "QR-code payment in the Walmart app since 2016, funded by cards or gift cards, with digital receipts and Walmart+ fuel discounts; it stays alongside tap to pay.",
              s=["shop", "plus"], lc="move", ay="2016", neo=[1, "Card on file, any network."], src=[["Supermarket News: tap to pay, Aug 2026", TAP]]),
        ]},
        {"id": "2.4", "ic": "hand-coins", "name": "Credit & instalments", "blurb": "Klarna, Upgrade.", "div": "onepay", "rev": "us", "products": [
            P("klarna", "Klarna instalments via OnePay", "OnePay's exclusive instalment loans at Walmart, online and in store, 3 to 36 months, managed in the OnePay app and powered by Klarna (17 March 2025). Affirm lost its exclusive, about 5% of its volume.", short="Klarna (OnePay)",
              s=["onepay", "shop"], lc="borrow", ay="Mar 2025", o="P", at="Klarna", neo=[0, "Klarna's loans."],
              mc="Instalments sit off the card networks.",
              src=[["Klarna: OnePay, Mar 2025", KLARNA], ["Payments Dive: Affirm and Walmart, Mar 2025", AFFIRM]]),
            P("upgrade", "OnePay personal loans", "Larger, more flexible personal loans powered by Upgrade, launched 20 July 2026.",
              s=["onepay"], lc="borrow", st="new", ay="Jul 2026", o="P", at="Upgrade", neo=[0, ""], src=[["OnePay newsroom", OP]]),
        ]},
        {"id": "2.5", "ic": "send", "name": "Prepaid & money services", "blurb": "MoneyCard, transfers.", "div": "walmart", "rev": "us", "products": [
            P("moneycard", "Walmart MoneyCard", "Green Dot Bank's account and card: 3% back on Walmart.com, 2% at Walmart fuel and 1% in stores up to $75 a year, 2.00% on savings (January 2026). The site names Visa and Mastercard; which programme runs on which is not stated ⚠.", short="MoneyCard (Visa/Mastercard)",
              s=["shop"], lc="everyday", o="P", at="Green Dot", neo=[1, "Visa and Mastercard named ⚠."], src=[["Walmart MoneyCard", MONEYCARD]]),
            P("moneyservices", "Money services", "Money transfers as an agent, bill payment, money orders and check cashing in US stores; partners are not named in the 10-K ⚠.",
              s=["shop"], lc="move", neo=[None, "Partners not named."],
              mc="Cross-border transfers are open ground for Mastercard Move.",
              src=[["Walmart 10-K FY26", TENK]]),
        ]},
        {"id": "2.6", "ic": "coins", "name": "Crypto & stablecoins", "blurb": "Zerohash, Tempo, Open USD.", "div": "onepay", "rev": "us", "products": [
            P("crypto", "OnePay crypto", "Bitcoin and ether trading and custody in the OnePay app through Zerohash, reported in October 2025 ⚠; the 10-K confirms 'limited access to cryptocurrency'.",
              s=["onepay"], lc="grow", st="new", o="P", at="Zerohash", neo=[0, ""], src=[["Crowdfund Insider: OnePay crypto, Oct 2025", CRYPTO], ["Walmart 10-K FY26", TENK]]),
            P("tempo", "Tempo validator", "OnePay runs a validator on Tempo, the payments blockchain incubated by Stripe and Paradigm, starting with stablecoin payouts and instant account funding (28 April 2026).",
              s=["onepay"], lc="move", st="new", ay="Apr 2026", o="P", at="Tempo", neo=[0, "Stablecoin rails."], src=[["OnePay: Tempo, Apr 2026", TEMPO]]),
            P("openusd", "Open USD", "A stablecoin from the independent Open Standard, announced in OnePay's newsroom on 30 June 2026 with more than 140 partners including Mastercard, Visa, American Express, Stripe and Shopify; launch 'later this year'. OnePay's exact role is not stated ⚠.",
              s=["onepay"], lc="move", st="new", ay="Jun 2026", o="P", at="Open Standard", neo=[0, "Mastercard is one of 140+ partners."],
              src=[["Open USD, Jun 2026", OPENUSD]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every purchase: Walmart+ and Sam's Club memberships, Sparky and OnePay's tools for AI agents, AI agents that fight financial crime at OnePay, and Walmart Connect advertising.",
    "tiles": [
        {"id": "3.1", "ic": "gift", "name": "Memberships", "blurb": "Walmart+, Sam's Club.", "div": "walmart", "rev": "us", "products": [
            P("walmartplus", "Walmart+", "Free shipping with no minimum, delivery from store, fuel discounts, Scan & Go and other benefits; fee revenue grew by double digits and Q2 FY27 net adds were a second-quarter record. Members get 5% back at Walmart on the OnePay card. Member numbers are not published ⚠.",
              s=["plus"], lc="grow", neo=[0, ""], src=[["Walmart 10-K FY26", TENK], ["Walmart: Q2 FY27 results", Q2], ["OnePay CashRewards card", CARD]]),
            P("samsmembership", "Sam's Club membership", "Membership-only clubs with Scan & Go and Just Go; membership fees rose on 1 May 2026 and fee income grew 6% in Q2 FY27 with more Plus members.",
              s=["sams"], lc="grow", neo=[0, ""], src=[["Walmart 10-Q Q2 FY27", TENQ], ["Walmart: Q2 FY27 results", Q2]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "Agents & AI shopping", "blurb": "Sparky, UCP, OnePay for Agents.", "div": "walmart", "rev": "us", "products": [
            P("sparky", "Sparky", "Walmart's own assistant. Walmart launched OpenAI's Instant Checkout in September 2025, found in-chat conversion three times lower than click-out, and from March 2026 put Sparky inside ChatGPT and then Gemini; Sparky users spend about 35% more per order ⚠ secondary.",
              s=["shop", "plus"], lc="grow", st="new", ay="Mar 2026", neo=[None, "Payment rail not stated."],
              mc="Agent-made purchases are what Agent Pay and agentic tokens are for.",
              src=[["PPC Land: Walmart and ChatGPT, Mar 2026", SPARKY]]),
            P("ucp", "Universal Commerce Protocol", "An open standard for agents to find, buy and handle after-sales, co-developed by Google with Walmart, Shopify, Etsy, Wayfair and Target (January 2026) and supported by Mastercard, Visa and American Express.",
              s=["shop"], lc="move", st="new", ay="Jan 2026", o="P", at="Google, Shopify, Target", neo=[1, "Mastercard, Visa and Amex all support it."], src=[["The Register: UCP, Jan 2026", UCP]]),
            P("onepayagents", "OnePay for Agents", "An MCP server (30 June 2026) that lets customers share balances, spending, credit and investments with AI tools, with consent; no payment rail is named.",
              s=["onepay"], lc="open", st="new", ay="Jun 2026", neo=[None, "No payment rail named."],
              mc="A permissioned data layer that Mastercard's agent credentials could sit behind.",
              src=[["OnePay for Agents, Jun 2026", AGENTS]]),
        ]},
        {"id": "3.3", "ic": "shield-check", "name": "Fraud & AML", "blurb": "OnePay's AI investigators.", "div": "onepay", "rev": "us", "products": [
            P("fincrimes", "Financial Crimes Detective", "An AI agent that opens on each transaction alert, gathers profile, risk and transaction data and open-source checks, and drafts a report and recommendation for a human analyst; it handles 'thousands of alerts' (7 May 2026).",
              s=["onepay"], lc="everyday", st="new", ay="May 2026", o="B", neo=[0, ""],
              mc="In-house AML today; network-level fraud and identity signals are not used publicly.",
              src=[["OnePay: Financial Crimes Detective, May 2026", FCD]]),
            P("aiops", "AI operations at OnePay", "Arnab, an AI operator (May 2026), a next-best-action engine (May 2026) and a real-time data platform (April 2026), built in-house.",
              s=["onepay"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["OnePay newsroom", OP]]),
        ]},
        {"id": "3.4", "ic": "presentation", "name": "Advertising & data", "blurb": "$6.4bn in FY26.", "div": "walmart", "rev": "us", "products": [
            P("connect", "Walmart Connect & global ads", "Nearly $6.4 billion of global advertising in FY26 (+46%, including VIZIO); +38% in Q2 FY27 with Walmart Connect up 43% and Flipkart Ads leading International. VIZIO is under an FTC data order until 2037.",
              s=["seller"], lc="grow", neo=[0, ""], src=[["Walmart: Q4 FY26 results", Q4], ["Walmart: Q2 FY27 results", Q2], ["Walmart 10-K FY26", TENK]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What Walmart sells: Walmart U.S. stores and eCommerce with a fast-growing marketplace, Sam's Club, OnePay's consumer banking, and payments businesses abroad in India (PhonePe, super.money), Mexico (Cashi) and Canada.",
    "tiles": [
        {"id": "4.1", "ic": "store", "name": "Walmart U.S.", "blurb": "$483.0bn in FY26.", "div": "walmart", "rev": "us", "products": [
            P("walmartus", "Stores & eCommerce", "$483.0 billion of net sales in FY26, about $99.6 billion of it eCommerce, and $125.2 billion in Q2 FY27 (comp +2.6%, eCommerce +24%); grocery is $285.5 billion a year.",
              s=["shop", "plus"], lc="everyday", neo=[1, "Accepts every network."], src=[["Walmart 10-K FY26", TENK], ["Walmart: Q2 FY27 results", Q2]]),
            P("marketplace", "Marketplace & fulfilment", "Third-party marketplace sales up 52% in Q2 FY27, with nearly half through Walmart's fulfilment services. How sellers are paid is not covered in the sources ⚠.",
              s=["seller"], lc="everyday", neo=[None, "Seller payout rails not found ⚠."], src=[["Walmart: Q2 FY27 presentation", Q2P], ["Walmart: Q2 FY27 news", WMTQ2]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Sam's Club U.S.", "blurb": "$93.0bn in FY26.", "div": "sams", "rev": "sams", "products": [
            P("samsclub", "Sam's Club", "601 clubs; $93.0 billion of net sales in FY26 (about $15.0 billion eCommerce) and $25.7 billion in Q2 FY27, comp +4.4% excluding fuel.",
              s=["sams"], lc="everyday", neo=[1, "Accepts every network; Sam's card on Mastercard."], src=[["Walmart 10-K FY26", TENK], ["Walmart: Q2 FY27 results", Q2]]),
        ]},
        {"id": "4.3", "ic": "wallet", "name": "OnePay", "blurb": "6m monthly users ⚠.", "div": "onepay", "rev": "us", "products": [
            P("onepaycash", "OnePay Cash banking", "Debit card, high-yield savings, early pay and peer-to-peer payments including international, through Coastal Community Bank and Lead Bank; about 6 million monthly users and $50 billion of annualised payments in June 2026, valued at more than $4 billion ⚠ Bloomberg, people familiar. Debit network not stated ⚠.", short="OnePay Cash",
              s=["onepay"], lc="everyday", o="P", at="Coastal Community Bank, Lead Bank", neo=[None, "Debit network not stated ⚠."],
              mc="The debit programme behind Walmart's fintech is an open question.",
              src=[["Shopifreaks: OnePay, Jun 2026", SIXM], ["Digital Transactions: Synchrony and OnePay, Jun 2025", DT]]),
            P("family", "Teen & family banking", "Banking for teens and families inside OnePay (28 September 2026), and GameChanger's official banking partner for 2027.",
              s=["onepay"], lc="open", st="new", ay="Sep 2026", neo=[None, ""], src=[["OnePay newsroom", OP]]),
        ]},
        {"id": "4.4", "ic": "smartphone", "name": "India", "blurb": "PhonePe, super.money.", "div": "india", "rev": "intl", "products": [
            P("phonepe", "PhonePe", "India's UPI app: 618 million registered users and 44.9 million merchants (March 2025), 9.8 billion transactions in December 2025; FY25 income ₹7,631 crore with a ₹1,727 crore loss. A SEBI-cleared IPO (January 2026) would sell about 9% held by Walmart's unit, which owns about 72%; it was postponed in March 2026 ⚠.", short="PhonePe (UPI)",
              s=["intl"], lc="move", st="flux", o="A", neo=[0, "UPI."], src=[["Entrackr: PhonePe DRHP, Jan 2026", DRHP], ["Chittorgarh: PhonePe IPO", PPIPO], ["Jainam: PhonePe IPO ⚠", PPDELAY]]),
            P("supermoney", "super.money", "Flipkart's UPI app, the fifth largest at about 257 million transactions a month, with a RuPay SuperCard from Utkarsh Small Finance Bank and more than $700 million lent through partners; Flipkart invested $30 million in September 2025.", short="super.money (UPI, RuPay)",
              s=["intl"], lc="move", st="new", o="B", at="Utkarsh Small Finance Bank", neo=[0, "UPI and RuPay."], src=[["Outlook Business: super.money, Sep 2025", SUPER]]),
            P("flipkartaxis", "Flipkart Axis Bank card", "Flipkart's co-brand credit card with Axis Bank; network not confirmed ⚠ (Mastercard and Visa variants from prior knowledge).",
              s=["intl"], lc="borrow", st="unconf", o="P", at="Axis Bank", neo=[None, "Network not confirmed ⚠."]),
        ]},
        {"id": "4.5", "ic": "wallet-cards", "name": "Mexico", "blurb": "Cashi, co-brands.", "div": "walmex", "rev": "intl", "products": [
            P("cashi", "Cashi & Cuenta Cashi", "Walmex's wallet (open loop since buying Trafalgar in 2023) and a debit account with physical and digital cards, a MXN 24,000 monthly cap, cash in and out at stores and US remittances; piloted from April 2025 for a national launch ⚠ not confirmed. Card network not stated ⚠.", short="Cashi",
              s=["intl"], lc="everyday", st="new", o="A", neo=[None, "Network not stated ⚠."],
              mc="A debit card for millions of store customers, with no network named in public.",
              src=[["Perú Retail: Cuenta Cashi, Mar 2025", CASHI], ["Bloomberg Línea: Cashi, Apr 2025", CASHIPILOT]]),
            P("walmexcards", "Walmex co-brand cards", "Credibodega with Bradesco and Walmart and Sam's Club cards with Inbursa, sold through Walmex; networks not stated ⚠.",
              s=["intl"], lc="borrow", o="P", at="Inbursa, Bradesco", neo=[None, "Networks not stated ⚠."], src=[["Perú Retail: Cuenta Cashi, Mar 2025", CASHI]]),
        ]},
        {"id": "4.6", "ic": "earth", "name": "Canada & other markets", "blurb": "Canada, Chile, China.", "div": "intl", "rev": "intl", "products": [
            P("canada", "Walmart Canada cards", "The Walmart Rewards Mastercard is known only from prior knowledge ⚠ (issuer and network not verified).",
              s=["intl"], lc="borrow", st="unconf", neo=[None, "Mastercard from prior knowledge ⚠."]),
            P("bmo", "BMO and Walmart Canada", "BMO chequing products in Walmart Canada stores and a 12-month Walmart+ Delivery Pass for new clients (3 December 2025).",
              s=["intl"], lc="open", st="new", ay="Dec 2025", o="P", at="BMO", neo=[0, "Interac debit."], src=[["BMO: Walmart Canada, Dec 2025", BMO]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Walmart: 11,000 stores and clubs, the Walmart, Sam's Club and OnePay apps and phone wallets, and AI assistants that now carry Sparky and OnePay.",
    "tiles": [
        {"id": "5.1", "ic": "building", "name": "Stores & clubs", "blurb": "11,000 worldwide.", "div": "walmart", "rev": "us", "products": [
            P("stores", "Stores & clubs", "10,955 retail units at 31 January 2026: 4,611 Walmart U.S., 601 Sam's Club and 5,743 International in 18 countries; 11,000 at 31 July 2026; pickup or delivery at more than 8,400 locations.",
              s=["shop", "sams", "intl"], lc="open", neo=[0, ""], src=[["Walmart 10-K FY26", TENK], ["Walmart 10-Q Q2 FY27", TENQ]]),
        ]},
        {"id": "5.2", "ic": "smartphone", "name": "Apps & wallets", "blurb": "Walmart, OnePay, Apple Pay.", "div": "walmart", "rev": "us", "products": [
            P("walmartapp", "Walmart & Sam's Club apps", "Walmart.com and the Walmart app with Walmart Pay, Walmart+ and Sparky; the Sam's Club app with Scan & Go.",
              s=["shop", "plus", "sams"], lc="open", neo=[0, ""], src=[["Walmart 10-K FY26", TENK]]),
            P("onepayapp", "OnePay app", "Banking, cards, Klarna loans, crypto and rewards in one app; about two-thirds of users who sign up through Walmart add another product ⚠ Bloomberg.",
              s=["onepay"], lc="open", neo=[0, ""], src=[["Shopifreaks: OnePay, Jun 2026", SIXM]]),
            P("wallets", "Phone wallets", "Apple Pay, Google Pay, Samsung Pay and Garmin Pay at Walmart's tills from August 2026; OnePay's debit card in Apple Pay since 2022 and CashRewards since August 2026.",
              s=["shop", "onepay"], lc="move", st="new", ay="Aug 2026", o="P", at="Apple, Google, Samsung", neo=[1, "Tokens on every network."],
              src=[["Supermarket News: tap to pay, Aug 2026", TAP], ["OnePay: Apple Pay, Aug 2026", APPLEPAY]]),
        ]},
        {"id": "5.3", "ic": "sparkles", "name": "AI front doors", "blurb": "ChatGPT, Gemini, Dots.", "div": "onepay", "rev": "us", "products": [
            P("aiplugins", "Walmart and OnePay inside AI assistants", "Sparky inside ChatGPT (from March 2026) and Gemini (April 2026); OnePay's plugin on every ChatGPT tier and in OpenAI's Dots assistant (12 October 2026), sharing balances, card details, credit and rewards with consent.",
              s=["shop", "onepay"], lc="open", st="new", ay="Oct 2026", o="P", at="OpenAI, Google", neo=[None, "Payment rail not stated."],
              src=[["OnePay: ChatGPT and Dots, Oct 2026", CHATGPT], ["PPC Land: Walmart and ChatGPT, Mar 2026", SPARKY]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Walmart", "blurb": "Its cards; its critic.", "products": [
        P("mcatwalmart", "Mastercard at Walmart", "Mastercard carries Walmart's two flagship US credit cards, the OnePay CashRewards Mastercard (Synchrony, autumn 2025) and the Sam's Club Mastercard (Synchrony, renewed 2025), and carried the Capital One card before them. Every store and site accepts Mastercard, now with contactless from August 2026, and Mastercard sits beside Walmart in UCP and Open USD. Walmart is also the lead objector to the Visa–Mastercard fee settlement, and OnePay sends instalments to Klarna and stablecoin payouts to Tempo.",
          s=["shop"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Synchrony: OnePay card, Jun 2025", SYFONE], ["Synchrony: Sam's Club renewal, Jan 2025", SAMS], ["Payments Dive: Walmart slams pact, Sep 2026", PDSLAM]]),
    ]},
    {"id": "pillar-market", "name": "The fee fight and the agents", "blurb": "Interchange, NFC, AI.", "products": [
        P("market", "The market", "US merchants paid an average 2.35% on Visa and Mastercard in 2024 and swipe fees reached about $198 billion; the settlement's final hearing is on 16 November 2026 and the Credit Card Competition Act has the Administration's backing. Meanwhile checkout is moving to phones and AI agents, with Walmart's NFC rollout, UCP and OnePay inside ChatGPT.",
          s=["shop"], div="grp", rev="grp", src=[["Payments Dive: Walmart slams pact, Sep 2026", PDSLAM], ["Payments Dive: networks urge approval, Oct 2026", PDURGE], ["The Register: UCP, Jan 2026", UCP]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
