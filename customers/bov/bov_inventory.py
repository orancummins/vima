"""Bank of Valletta's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 interim report (29 July 2026), the
Q1 2026 update and the FY2025 results (26 March 2026), all filed as Malta Stock Exchange company announcements.
bov.com refused automated reads, so its own pages are cited only where search results confirmed them.
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://cdn.borzamalta.com.mt/download/announcements/BOV599.pdf"
FY25 = "https://cdn.borzamalta.com.mt/download/announcements/BOV568.pdf"
Q1 = "https://cdn.borzamalta.com.mt/download/announcements/BOV576.pdf"
NOTES = "https://cdn.borzamalta.com.mt/download/announcements/BOV583.pdf"
AGM = "https://cdn.borzamalta.com.mt/download/announcements/BOV588.pdf"
SMFEB = "https://cdn.borzamalta.com.mt/download/announcements/BOV561.pdf"
CROOCT = "https://cdn.borzamalta.com.mt/download/announcements/BOV602.pdf"
CFO = "https://cdn.borzamalta.com.mt/download/announcements/BOV477.pdf"
HOLD = "https://cdn.borzamalta.com.mt/download/announcements/BOV600.pdf"
BUYBACK = "https://cdn.borzamalta.com.mt/download/announcements/BOV603.pdf"
MCEXIT = "https://businessnow.mt/bov-to-discontinue-mastercard-offering-from-1st-december"
SHIFT = "https://theshiftnews.com/2021/10/05/bov-ceases-relations-with-mastercard-clients-informed-visa-is-their-only-option"
CORP = "https://webiis10.mondaq.com/financial-services/1648742/bov-launches-full-suite-of-corporate-visa-cards"
SMARTPAY = "https://www.bov.com/bank-valletta-unveils-bov-smartpay"
BOVPAY = "https://www.openwaygroup.com/new-blog/2019/11/21/bov-pay-the-future-of-payments"
DESIGNS = "https://financemalta.org/news/bank-of-valletta-unveils-new-card-designs"
SEPAIN = "https://maltachamber.org.mt/bov-sets-new-standard-with-sepa-instant-payments-launch/"
SEPAOUT = "https://maltachamber.org.mt/bov-launches-instant-outward-sepa-payments/"
CBMPROXY = "https://businessnow.mt/central-bank-of-malta-considers-national-mobile-payment-platform-to-simplify-instant-transfers/"
BNFMC = "https://businessnow.mt/bnf-bank-and-mastercard-partner-to-bring-added-value-to-maltese-customers/"
SEASON = "https://businessnow.mt/highlights-from-interim-reporting-season/"
HSBCCB = "https://maltabusinessweekly.com/hsbc-malta-posts-resilient-first-half-results-as-ceo-expects-crediabank-takeover-to-close-in-q2-2027/30737/"
CURMI = "https://www.curmiandpartners.com/en/bank-of-valletta-plc-company-profile"
ROADSHOW = "https://www.bov.com/api/v1/download/post-earnings-non-deal-roadshow"
APPSTORE = "https://apps.apple.com/app/id484470116"
APPLEPAY = "https://www.bov.com/apple-pay"
MOBILEPOS = "https://financemalta.org/industry-updates/cashless-payments-even-more-accessible-with-bov-mobilepos-d0be3"
GOLD = "https://www.bov.com/sites/default/files/2026-02/bov-visa-gold-card-product-guide%20DEC%2025.pdf"
CASHLINK = "https://www.bov.com/sites/default/files/2026-02/bov-cashlink-visa-card-product-guide%20Dec%2025.pdf"
ACCEPT = "https://www.bov.com/api/v1/download/bov-card-acceptance-terms-and-conditions"
PREPAID = "https://www.maltatoday.com.mt/business/business_news/33716/bov-launches-limited-edition-uefa-champions-league-mastercard-prepaid-cards"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · state stake · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Malta's largest bank with €17.6 billion of assets, a quarter owned by the state, founded in 1974, rebuilding its technology and writing a 2027–29 strategy.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "€17.6bn assets, CET1 19%.", "div": "bov", "rev": "others", "products": [
            P("balance", "Balance sheet & earnings", "Profit before tax of €119.8 million in H1 2026 (down 11.3%) and €260.4 million in 2025; record operating income of €251.3 million in the half; total assets €17.6 billion, deposits €14.5 billion and net loans €8.6 billion at 30 June 2026; CET1 19.32%, NPE ratio 1.49%; guidance of €215–250 million profit before tax for 2026.",
              s=["con"], neo=[0, ""], src=[["H1 2026 interim report", H1], ["FY2025 results", FY25]]),
            P("ratings", "Ratings & funding", "Fitch upgraded BOV to BBB in March 2025 after an S&P upgrade the year before; a €300 million 4.467% senior preferred note in May 2026, its largest bond, was about twice oversubscribed; a second share buyback starts on 19 October 2026.",
              s=["corp"], st="new", ay="May 2026", neo=[0, ""], src=[["FY2025 results", FY25], ["€300m senior preferred notes", NOTES], ["Second buyback, Oct 2026", BUYBACK]]),
            P("visashares", "Visa shares", "Holds shares in 'a global payments technology company' valued on their conversion shares with a discount for liquidity and litigation risk, most likely Visa preferred stock from the 2016 Visa Europe sale ⚠.",
              s=["corp"], neo=[0, "Visa ⚠."], src=[["H1 2026 interim report", H1]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "State 25%, Farrugia CEO.", "div": "bov", "rev": "others", "products": [
            P("owners", "Ownership & heritage", "Founded in 1974 and listed on the Malta Stock Exchange in December 1992; the Government of Malta owns about 25% and UniCredit about 10% ⚠ (dated profile); Slingshot Global SICAV crossed 5% in August 2026; market value about €1.35 billion in early 2026.",
              s=["corp"], o="I", neo=[0, ""], src=[["Curmi & Partners: BOV profile", CURMI], ["BOV roadshow deck", ROADSHOW], ["Major holding, Aug 2026", HOLD], ["FY2025 results", FY25]]),
            P("board", "Board & executives", "Chair Dr Gordon Cordina, CEO Kenneth Farrugia, CFO Kevin Cardona (2024); the strategy and data, customer experience and risk chiefs left in 2026 and a proposed new chief risk officer was withdrawn on 9 October 2026 ⚠ interim arrangements.",
              s=["corp"], st="flux", neo=[0, ""], src=[["AGM resolutions, Jun 2026", AGM], ["Senior management, Feb 2026", SMFEB], ["CRO update, Oct 2026", CROOCT], ["CFO appointment, Apr 2024", CFO]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology & resilience", "blurb": "Core, cyber, DORA.", "div": "bov", "rev": "others", "products": [
            P("tech", "Technology modernisation", "Investment in core banking, data management, channel integration and cyber security, with operating costs up to €129.2 million in H1 2026 (cost:income 51.4%) and programmes under the EU's digital operational resilience rules.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 interim report", H1], ["Q1 2026 update", Q1]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy", "blurb": "2027–29 plan due late 2026.", "div": "bov", "rev": "others", "products": [
            P("strategy", "Strategy 2024–26 and 2027–29", "The 2024–26 cycle (Customer, Operations, Risk & Governance, People) ends this year; the 2027–29 strategy is due for Board approval in late 2026 as 'an evolution', and fee growth from payments, cards, bancassurance, trade finance and wealth is a stated 2026 pillar.",
              s=["corp"], st="new", neo=[0, ""], mc="A new strategy cycle is the natural moment to pitch services that do not depend on the card network.",
              src=[["H1 2026 interim report", H1], ["FY2025 results", FY25]]),
            P("esg", "ESG & climate", "A climate transition plan with Scope 1 and 2 targets, NGFS climate scenarios in capital planning, green lending, and a first CSRD sustainability report for 2026.",
              s=["corp", "home"], neo=[0, ""], src=[["H1 2026 interim report", H1]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Visa debit and credit cards since the Mastercard programme closed in 2021, a Visa corporate range, Apple Pay and BOV Pay, SmartPay terminals and MobilePOS, SEPA Instant with payee checks, and trade finance.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Cashlink Visa.", "div": "cards", "rev": "retail", "products": [
            P("debit", "BOV Cashlink Visa debit", "The personal debit card, contactless and on Visa, with a product guide updated in December 2025; card fees were €8.2 million in H1 2026.",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["BOV Cashlink Visa product guide", CASHLINK], ["H1 2026 interim report", H1]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "All Visa since Dec 2021.", "div": "cards", "rev": "retail", "products": [
            P("credit", "BOV Visa credit cards", "Visa Classic and Visa Gold (minimum limit €7,000, loyalty rewards), with Platinum and Skypass tiers in older sources ⚠; 'strong momentum in cards' lifted 2025 fees.", short="Visa credit",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["BOV Visa Gold product guide, Dec 2025", GOLD], ["FY2025 results", FY25]]),
            P("mcexit", "Mastercard credit programme (closed)", "BOV's only Mastercard product, held by 'thousands', closed on 1 December 2021; holders were moved to a Visa Classic free of charge. The bank called it 'purely a business and strategic' decision.", short="Mastercard credit (closed 2021)",
              s=["con"], lc="borrow", st="retired", ay="Dec 2021", o="P", at="Mastercard", neo=[0, "Moved to Visa, Dec 2021."],
              mc="The defining loss: Malta's largest issuer has had no Mastercard cards since 2021.",
              src=[["Business Now: BOV ends Mastercard, Oct 2021", MCEXIT], ["The Shift: BOV ceases Mastercard, Oct 2021", SHIFT]]),
            P("prepaid", "Prepaid gift cards", "BOV issued limited-edition UEFA Champions League Mastercard prepaid cards in 2011; no current prepaid range was found ⚠.",
              s=["con"], lc="everyday", st="unconf", ay="2011", neo=[None, "Mastercard in 2011; current network unknown."], src=[["MaltaToday: BOV prepaid Mastercard, 2011", PREPAID]]),
        ]},
        {"id": "2.3", "ic": "briefcase", "name": "Corporate cards", "blurb": "Visa suite, June 2025.", "div": "cards", "rev": "business", "products": [
            P("corpcards", "BOV corporate Visa cards", "Visa Business Debit, Corporate Credit and Corporate Premium Credit (Priority Pass lounge access), with cashback, replacing older business cards; rollout completed in June 2025.",
              s=["sme", "corp"], lc="everyday", st="new", ay="Jun 2025", o="P", at="Visa", neo=[0, "Visa."],
              mc="Mastercard has no commercial card at Malta's main business bank.",
              src=[["BOV corporate Visa cards, Jul 2025", CORP]]),
        ]},
        {"id": "2.4", "ic": "wallet", "name": "Wallets", "blurb": "Apple Pay, BOV Pay.", "div": "digital", "rev": "retail", "products": [
            P("applepay", "Apple Pay", "BOV Visa debit and credit cards in Apple Wallet, live by April 2021; Google Pay support not confirmed ⚠.",
              s=["con"], lc="everyday", o="P", at="Apple, Visa", neo=[0, "Visa tokens."], src=[["BOV: Apple Pay", APPLEPAY], ["FinanceMalta: new card designs, Apr 2021", DESIGNS]]),
            P("bovpay", "BOV Pay", "BOV's own Android NFC wallet for BOV Visa cards (2019), with Garmin Pay for watches.",
              s=["con"], lc="everyday", ay="2019", o="B", neo=[0, "Visa tokens."], src=[["OpenWay: BOV Pay, Nov 2019", BOVPAY]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "BOV SmartPay.", "div": "smartpay", "rev": "business", "products": [
            P("smartpay", "BOV SmartPay merchant services", "One brand for in-store ePOS terminals, an e-commerce gateway and MobilePOS, with a dedicated merchant support team and online applications ⚠ launch date about 2025; processor not named.", short="SmartPay acquiring",
              s=["merch", "sme"], lc="move", st="new", o="B", neo=[1, "Accepts Mastercard ⚠."],
              mc="Mastercard's only live touchpoint at BOV: its cards are accepted at BOV merchants.",
              src=[["BOV: SmartPay", SMARTPAY], ["BOV card acceptance terms", ACCEPT], ["BOV corporate Visa cards, Jul 2025", CORP]]),
            P("mobilepos", "BOV MobilePOS", "Card acceptance on an Android phone or tablet, taking the major card brands and Apple and Google wallets ⚠ date.",
              s=["merch"], lc="move", o="B", neo=[1, "Accepts Mastercard ⚠."], src=[["FinanceMalta: BOV MobilePOS", MOBILEPOS]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Instant payments", "blurb": "SEPA Instant, payee checks.", "div": "digital", "rev": "retail", "products": [
            P("sepainst", "SEPA Instant", "Incoming instant euro payments from December 2024 and outgoing from 6 October 2025, in under ten seconds at no extra charge, with Verification of Payee on every third-party SEPA payment.",
              s=["con", "sme"], lc="move", st="new", ay="Oct 2025", o="B", neo=[0, ""],
              mc="Account-to-account rails now compete with debit for transfers; fraud scoring on them is network-neutral.",
              src=[["BOV SEPA Instant, Dec 2024", SEPAIN], ["BOV outward instant SEPA, Oct 2025", SEPAOUT]]),
            P("mobilepay", "Payments to mobile numbers", "BOV Mobile sends money to a mobile number; the Central Bank of Malta is consulting on a national mobile-number look-up across banks (October 2025) ⚠ no date.",
              s=["con"], lc="move", st="flux", neo=[0, ""], src=[["App Store: BOV Mobile", APPSTORE], ["Business Now: CBM mobile payments, Oct 2025", CBMPROXY]]),
        ]},
        {"id": "2.7", "ic": "earth", "name": "Trade & cross-border", "blurb": "Trade finance, SWIFT.", "div": "bov", "rev": "business", "products": [
            P("trade", "Trade finance & international payments", "Documentary credits of €46.5 million outstanding at June 2026 and trade finance named as a fee driver; cross-border payments for Malta's exporters and tourism businesses.",
              s=["corp", "sme"], lc="move", neo=[0, ""], src=[["H1 2026 interim report", H1]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: payee checks and financial-crime controls, a CRM programme and measured use of AI, card loyalty, and the resilience work regulators expect.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & financial crime", "blurb": "Payee checks, AML.", "div": "bov", "rev": "retail", "products": [
            P("vop", "Verification of Payee", "Checks the IBAN and payee name on every third-party SEPA payment, instant or not, from October 2025 ⚠ provider not named.",
              s=["con", "sme"], lc="move", st="new", ay="Oct 2025", neo=[None, "Provider not named."],
              mc="Instant payments raise scam risk; network-neutral scam scoring could sit beside the payee check.",
              src=[["BOV outward instant SEPA, Oct 2025", SEPAOUT]]),
            P("fincrime", "Financial-crime prevention", "Programmes in financial-crime prevention, information and cyber security and third-party risk, with cybercrime and financial fraud named as emerging risks.",
              s=["con", "corp"], lc="everyday", neo=[0, "BOV's own."], src=[["H1 2026 interim report", H1]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data, CRM & AI", "blurb": "Personalisation first.", "div": "bov", "rev": "retail", "products": [
            P("crm", "Customer Relationship Management programme", "'One of the most important strategic investments' under way: a single customer view and data insights to make banking 'personalised, proactive and relationship-driven'.",
              s=["con", "sme"], lc="everyday", st="new", neo=[0, ""],
              mc="Transaction enrichment and open finance data would feed the personalisation BOV wants.",
              src=[["H1 2026 interim report", H1]]),
            P("ai", "AI & analytics", "A phased roll-out of AI applications for efficiency, staff training in data and AI, and a geopolitical dashboard for credit risk; no customer-facing AI product named ⚠.",
              s=["corp"], lc="everyday", st="new", neo=[None, ""], src=[["Q1 2026 update", Q1], ["H1 2026 interim report", H1]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty", "blurb": "Points and cashback.", "div": "cards", "rev": "retail", "products": [
            P("loyalty", "BOV Cards loyalty rewards", "Free automatic enrolment for credit cardholders, points on Gold and premium cards, and cashback paid into the account for the corporate range.",
              s=["con", "sme"], lc="grow", neo=[0, "Visa cards."], src=[["BOV Visa Gold product guide, Dec 2025", GOLD], ["BOV corporate Visa cards, Jul 2025", CORP]]),
        ]},
        {"id": "3.4", "ic": "gauge", "name": "Operations & resilience", "blurb": "DORA, third parties.", "div": "bov", "rev": "others", "products": [
            P("resilience", "Operational resilience", "Operational-resilience, third-party risk and regulatory-reporting programmes run under Board governance, with multi-year programmes re-sequenced where delivery slipped.",
              s=["corp"], lc="everyday", neo=[0, ""], src=[["H1 2026 interim report", H1]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail accounts and loans, home loans, business and commercial banking, wealth and investments, bancassurance with Mapfre, and a €7 billion treasury book.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Retail banking", "blurb": "Malta's main bank.", "div": "bov", "rev": "retail", "products": [
            P("accounts", "Accounts, savings & personal loans", "Current and savings accounts and personal credit for most Maltese households; retail fee income of €22.7 million in H1 2026, and deposits up €748 million in the half.",
              s=["con"], lc="everyday", neo=[0, "Visa debit."], src=[["H1 2026 interim report", H1], ["Business Now: interim season, Sep 2026", SEASON]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Home loans", "blurb": "New finance hubs.", "div": "bov", "rev": "retail", "products": [
            P("homeloans", "Home loans", "Residential mortgages with 'healthy' origination in 2025 and specialist Home Finance Hubs opened in Mosta and Gżira in H1 2026.",
              s=["home"], lc="borrow", st="new", neo=[0, ""], src=[["H1 2026 interim report", H1], ["FY2025 results", FY25]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Business banking", "blurb": "The Quad business hub.", "div": "bov", "rev": "business", "products": [
            P("business", "Business & SME banking", "Accounts, lending and payments for Malta's businesses, served from a Business Hub at The Quad Central in Mrieħel (late 2025) with a corporate outreach team; business fee income €13.7 million in H1 2026.",
              s=["sme"], lc="everyday", st="new", neo=[0, "Visa business cards."], src=[["H1 2026 interim report", H1], ["FY2025 results", FY25]]),
            P("corplending", "Commercial & corporate lending", "Corporate, infrastructure and working-capital lending drove net loans up €1.1 billion in 2025 and €544 million in H1 2026.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["FY2025 results", FY25], ["H1 2026 interim report", H1]]),
        ]},
        {"id": "4.4", "ic": "trending-up", "name": "Wealth & investments", "blurb": "€13.1m fees in H1.", "div": "funds", "rev": "wealth", "products": [
            P("wealth", "Wealth management & advice", "Investment services fees of €13.1 million in H1 2026, the largest fee line, from advice, wealth management and investment centres.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["H1 2026 interim report", H1]]),
            P("funds", "Fund management & fund services", "Valletta Fund Management and Valletta Fund Services, wholly owned ⚠ current names.",
              s=["saver"], lc="grow", o="B", neo=[0, ""], src=[["Curmi & Partners: BOV profile", CURMI]]),
            P("stockbroking", "Stockbroking", "An in-house stockbroking arm on the Malta Stock Exchange, which also executes BOV's buybacks.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["Second buyback, Oct 2026", BUYBACK]]),
        ]},
        {"id": "4.5", "ic": "chart-candlestick", "name": "Treasury", "blurb": "€7.0bn portfolio.", "div": "bov", "rev": "treasury", "products": [
            P("treasury", "Treasury portfolio", "€7.0 billion of mostly highly rated securities, about 40% of the balance sheet, earning €95.1 million of interest in H1 2026.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["H1 2026 interim report", H1]]),
        ]},
        {"id": "4.6", "ic": "hand-coins", "name": "Bancassurance", "blurb": "Mapfre, in branch.", "div": "mapfre", "rev": "wealth", "products": [
            P("insurance", "Life & general insurance", "Tied agent for Mapfre MSV Life and Mapfre Malta, both associates; travel, health and home insurance sold in branches from Q3 2025; associates contributed €3.4 million in H1 2026.",
              s=["con", "home"], lc="beyond", o="P", at="Mapfre", neo=[0, ""], src=[["FY2025 results", FY25], ["H1 2026 interim report", H1]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach BOV: BOV Mobile and a new omnichannel platform, branches, hubs and the contact centre, and investor channels.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "BOV Mobile & omnichannel", "blurb": "New platform rolling out.", "div": "digital", "rev": "retail", "products": [
            P("app", "BOV Mobile & Internet Banking", "The mobile app (version 4.13.0, June 2026) with Face ID, card stop, bills and mobile-number payments; more than 110,000 app clients in 2020 ⚠ dated.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["App Store: BOV Mobile", APPSTORE]]),
            P("omnichannel", "Omnichannel Banking Platform", "A new platform opened to more users through H1 2026, joining branch, contact centre and digital in one journey, with onboarding and more functions to follow.",
              s=["con", "sme"], lc="open", st="new", neo=[0, ""],
              mc="New onboarding and digital journeys are where open finance and identity checks would sit.",
              src=[["H1 2026 interim report", H1]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & hubs", "blurb": "28 branches ⚠.", "div": "bov", "rev": "retail", "products": [
            P("branches", "Branches & contact centre", "About 28 branches and 5 investment centres ⚠ undated, and a contact centre highly commended at the 2025 European Contact Centre & Customer Service Awards.",
              s=["con", "saver"], lc="everyday", neo=[0, ""], src=[["BOV roadshow deck", ROADSHOW], ["FY2025 results", FY25]]),
            P("hubs", "Business Hub & Home Finance Hubs", "Commercial specialists brought together at The Quad Central, and mortgage hubs in Mosta and Gżira.",
              s=["sme", "home"], lc="open", st="new", neo=[0, ""], src=[["H1 2026 interim report", H1]]),
        ]},
        {"id": "5.3", "ic": "presentation", "name": "Investors & community", "blurb": "20,000+ shareholders.", "div": "bov", "rev": "others", "products": [
            P("investors", "Investor channels", "More than 20,000 shareholders ⚠, first BOV Investor Days in 2025, a quarterly investor-relations report and retail bond issues.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["FY2025 results", FY25], ["BOV roadshow deck", ROADSHOW]]),
            P("foundation", "BOV Foundation", "Community, culture, financial literacy and inclusion work alongside the ESG agenda.",
              s=["con"], lc="beyond", neo=[0, ""], src=[["H1 2026 interim report", H1]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BOV", "blurb": "Gone from issuing since 2021.", "products": [
        P("mcatbov", "Mastercard at BOV", "BOV closed its only Mastercard programme, a credit card, on 1 December 2021 and moved holders to Visa. Every BOV card since, debit, credit and the 2025 corporate range, is Visa, with Visa tokens in Apple Pay and BOV Pay. Mastercard's live presence is acceptance at SmartPay merchants ⚠; rival BNF Bank signed a Mastercard partnership in February 2026.",
          s=["con"], div="bov", rev="others", mc="The relationship this map is drawn for.",
          src=[["Business Now: BOV ends Mastercard, Oct 2021", MCEXIT], ["BOV corporate Visa cards, Jul 2025", CORP], ["Business Now: BNF and Mastercard, Feb 2026", BNFMC]]),
    ]},
    {"id": "pillar-market", "name": "Maltese banking", "blurb": "BOV dominant, HSBC changing hands.", "products": [
        P("market", "The Maltese market", "BOV is larger than HSBC Malta, APS and Lombard combined and has the highest margin (2.49%); HSBC Malta is being sold to CrediaBank (closing about Q2 2027); SEPA Instant became mandatory in October 2025; the central bank is studying mobile-number payments.",
          s=["con"], div="bov", rev="others",
          src=[["Business Now: interim season, Sep 2026", SEASON], ["HSBC Malta H1 and CrediaBank", HSBCCB], ["Business Now: CBM mobile payments, Oct 2025", CBMPROXY]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
