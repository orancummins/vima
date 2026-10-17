"""Standard Chartered's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 2026 half-year results (29 July 2026), the
2025 results (24 February 2026) and the investor event (19–21 May 2026). Card networks are read from the
bank's local card pages as at 17 October 2026. ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

HY26 = "https://www.sc.com/en/press-release/half-year-2026-results/"
HY26RNS = "https://data.fca.org.uk/artefacts/NSM/RNS/5058eb6c-d446-4505-b15a-d1a8581d6901.html"
HY26RPT = "https://www.sc.com/en/uploads/sites/66/content/docs/standard-chartered-plc-hy-2026-report.pdf"
FY25 = "https://data.fca.org.uk/artefacts/NSM/RNS/4f6a69d1-ad5b-4c71-884b-0313d27a8592.html"
FY25PR = "https://www.sc.com/en/press-release/full-year-2025-results/"
PLAN = "https://www.sc.com/en/press-release/growth-plan-targets-2026-investor-event/"
MCAP = "https://companiesmarketcap.com/standard-chartered/marketcap/"
CFO = "https://www.sc.com/en/press-release/manus-costello-group-chief-financial-officer/"
BOARD = "https://www.sc.com/en/press-release/standard-chartered-plc-board-tanate-phutrakul/"
MGMT = "https://www.sc.com/en/press-release/management-team-update/"
CIBCEO = "https://www.sc.com/en/press-release/roberto-hoornweg-to-lead-corporate-investment-banking-at-standard-chartered/"
ABOUT = "https://www.sc.com/en/about/"
SAUDI = "https://sc.com/sa-en/about"
SAUDI2 = "https://gulfbusiness.com/standard-chartered-opens-first-branch-in-saudi-arabia/"
ALIBABA = "https://www.sc.com/en/press-release/standard-chartered-and-alibaba-group-sign-strategic-technology-and-growth-partnership/"
GCC = "https://www.sc.com/en/press-release/standard-chartered-to-rename-global-business-services-to-global-capability-centres/"
CDO = "https://www.sc.com/en/press-release/standard-chartered-appoints-shebani-baweja-as-group-chief-data-officer/"
EXITS = "https://www.retailbankerinternational.com/news/standard-chartered-ugandan-retail-banking-absa/"
SOLV = "https://www.sc.com/en/press-release/sc-ventures-incubated-solv-india-acquired-by-jumbotail/"
ZODIA = "https://www.sc.com/en/press-release/standard-chartered-to-acquire-zodia-custodys-custody-business/"
HKCARDS = "https://www.sc.com/hk/credit-cards/"
HKSMART = "https://www.sc.com/hk/credit-cards/smart/"
HKSIMPLY = "https://www.sc.com/hk/credit-cards/simply-cash/"
CATHAY = "https://www.mastercard.com/news/ap/en-hk/newsroom/press-releases/en-hk/2021/july/standard-chartered-cathay-and-mastercard-deepen-cooperation-with-launch-of-a-brand-newrange-of-mastercard-credit-cards/"
SGCARDS = "https://www.sc.com/sg/credit-cards/"
SGBEYOND = "https://www.sc.com/sg/credit-cards/beyond-credit-card/"
SGSIMPLY = "https://www.sc.com/sg/credit-cards/simply-cash-credit-card/"
SGJOURNEY = "https://www.sc.com/sg/credit-cards/journey-credit-card/"
SGSMART = "https://www.sc.com/sg/credit-cards/smart-credit-card/"
SGVI = "https://mainlymiles.com/2026/05/22/standard-chartered-visa-infinite-review-2026/"
INCARDS = "https://www.sc.com/in/credit-cards/"
INSMART = "https://www.sc.com/in/credit-cards/smart-credit-card/"
PKCARDS = "https://www.sc.com/pk/credit-cards/"
PKMC = "https://www.brandsynario.com/featured/standard-chartered-and-mastercard-partner-for-payment-innovation-in-pakistan/"
IDCARDS = "https://www.sc.com/id/credit-cards/"
BDCARDS = "https://www.sc.com/bd/credit-cards/"
AECARDS = "https://www.sc.com/ae/credit-cards/"
KECARDS = "https://www.sc.com/ke/credit-cards/"
GHCARDS = "https://www.sc.com/gh/debit-cards/"
MOXCREDIT = "https://mox.com/features/mox-credit/"
TRUST = "https://trustbank.sg/"
TRUSTVISA = "https://dollarsandsense.sg/complete-guide-trust-banks-products-services"
PAYHEAD = "https://www.sc.com/en/press-release/standard-chartered-appoints-naveen-mallela-as-global-head-of-payments/"
VISAB2B = "https://www.sc.com/en/press-release/standard-chartered-joins-forces-with-visa-to-enhance-cross-border-payments/"
SEND = "https://www.theasianbanker.com/press-releases/standard-chartered-bank-selects-mastercard-to-transform-cross-border-payments"
ANTSWIFT = "https://www.sc.com/en/press-release/ant-international-standard-chartered-and-swift-have-collaborated-to-pioneer-bank-to-wallet-payment-solution-backed-by-iso-20022/"
TOKDEP = "https://www.sc.com/en/press-release/standard-chartered-launches-blockchain-based-tokenised-deposits-solution-in-sgd-and-usd/"
SWIFTTD = "https://www.sc.com/en/press-release/standard-chartered-and-hsbc-execute-first-live-tokenised-deposit-transaction-on-swifts-blockchain-based-ledger/"
ANCHOR = "https://www.sc.com/en/press-release/standard-chartered-backed-anchorpoint-granted-stablecoin-issuer-licence-by-the-hong-kong-monetary-authority/"
HKDAP = "https://www.sc.com/en/press-release/standard-chartered-becomes-first-bank-distributor-of-hkdap-to-unlock-real-economy-benefits-of-hkd-stablecoins/"
CIRCLE = "https://www.sc.com/en/press-release/standard-chartered-and-circle-launch-first-g-sib-led-integrated-access-to-usdc-minting-and-redemption/"
DECARD = "https://www.sc.com/en/press-release/standard-chartered-to-power-decard-in-singapore-through-partnership-with-dcs/"
MTN = "https://www.mastercard.com/news/ap/en/newsroom/press-releases/en/2024/mastercard-standard-chartered-mox-and-libeara-successfully-complete-a-proof-of-concept-pilot-on-tokenized-deposits-and-tokenized-carbon-credits-through-regulatory-sandbox/"
TEMPO = "https://investor.visa.com/news/news-details/2026/Visa-Launches-Validator-Node-on-Tempo-Blockchain/default.aspx"
ALADDIN = "https://www.sc.com/en/press-release/standard-chartered-announces-global-collaboration-with-blackrocks-aladdin-wealth-to-enhance-mywealth-advisor/"
ANTAI = "https://www.sc.com/en/press-release/standard-chartered-and-ant-international-collaborate-on-ai-powered-treasury-and-fx-management-solutions/"
CAMPAIGN = "https://www.sc.com/en/press-release/standard-chartered-deepens-nows-your-time-for-wealth-campaign-with-ai-powered-innovation-wealth-and-advisory-capabilities/"
FINMO = "https://www.sc.com/en/press-release/finmo-and-standard-chartered-partner-to-integrate-global-currency-accounts-and-api-driven-treasury-connectivity/"
AGENTIC = "https://www.visa.com.sg/about-visa/newsroom/press-releases/visa-launches-agentic-ready-programme-in-singapore-with-13-banks-and-fintech-partners.html"
F1 = "https://www.sc.com/en/press-release/formula1-official-partnership-announcement/"
LFC = "https://www.sc.com/en/press-release/liverpool-partnership-announcement-2026/"
HKCUSTODY = "https://www.sc.com/en/press-release/standard-chartered-powers-hong-kongs-first-g-sib-institutional-crypto-custody/"
SGCUSTODY = "https://www.sc.com/en/press-release/standard-chartered-advances-into-digital-asset-custody-offering-in-singapore/"
RLUSD = "https://www.sc.com/en/press-release/standard-chartered-launches-rlusd-custody-and-joins-planned-collateral-integration-with-ripple-and-lmax-group/"
INSTTRADE = "https://www.sc.com/en/press-release/standard-chartered-launches-digital-assets-trading-for-institutional-clients/"
UAESPOT = "https://www.sc.com/en/press-release/standard-chartered-becomes-first-global-systemically-important-bank-g-sib-to-launch-institutional-bitcoin-and-ether-spot-trading-in-the-uae/"
AFFCRYPTO = "https://www.sc.com/en/press-release/standard-chartered-unveils-first-of-its-kind-cryptocurrency-trading-solution-for-affluent-clients/"
FPS = "https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/financial-market-infrastructure/faster-payment-system-fps/"
PAYNOW = "https://www.mas.gov.sg/development/e-payments/paynow"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · network · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a $993 billion balance sheet earning 17.6% RoTE, a network of 55 markets across Asia, Africa and the Middle East, retail exits in smaller markets, and a plan to reach about 18% RoTE by 2030.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "$993bn of assets, RoTE 17.6%.", "div": "group", "rev": "co", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of $993.4 billion, customer loans of $299.3 billion and customer accounts of $552.6 billion at 30 June 2026; a record $4.8 billion profit before tax in the half (RoTE 17.6%, CET1 14.2%); income of $20.9 billion and underlying RoTE of 14.7% in 2025; Standard Chartered Bank rated AA-/A+/A1; market value about $61 billion ⚠.",
              s=["corp"], neo=[0, ""], src=[["HY 2026 results", HY26], ["Half Year Report 2026", HY26RPT], ["FY 2025 results", FY25], ["Market cap (third party)", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Ramos and Winters.", "div": "group", "rev": "co", "products": [
            P("leadership", "Board & management team", "Chair Maria Ramos, Group Chief Executive Bill Winters, CFO Manus Costello (confirmed July 2026), COO Tanuj Kapilashrami; Roberto Hoornweg runs CIB and Judy Hsu runs WRB; Noelle Eder heads technology and Alex Manson SC Ventures.",
              s=["corp"], neo=[0, ""], src=[["Board change, Jun 2026", BOARD], ["CFO appointment, May 2026", CFO], ["CIB leadership, Oct 2025", CIBCEO], ["Management update, Aug 2026", MGMT]]),
        ]},
        {"id": "1.3", "ic": "earth", "name": "Network & heritage", "blurb": "55 markets, 170 years.", "div": "group", "rev": "cib", "products": [
            P("footprint", "Footprint & heritage", "A presence in 55 markets, listed in London and Hong Kong, with about 170 years of history (Chartered Bank 1853 and Standard Bank 1862, merged 1969 ⚠); 61.5% of CIB income is cross-border.",
              s=["corp", "fi"], neo=[0, ""], src=[["FY 2025 results", FY25PR], ["About Standard Chartered", ABOUT], ["FY 2025 RNS", FY25]]),
            P("saudi", "Saudi Arabia branch", "Licensed in 2019; the branch began banking operations in June 2021 and serves global corporates, subsidiaries and financial institutions, not retail customers.",
              s=["corp"], ay="Jun 2021", neo=[0, ""], src=[["SC Saudi Arabia: about", SAUDI], ["Gulf Business: first Saudi branch", SAUDI2]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology, data & AI", "blurb": "Alibaba Cloud, GCCs, a data chief.", "div": "group", "rev": "co", "products": [
            P("tech", "Technology, data & AI", "Alibaba Cloud as strategic AI partner (MoU, July 2025); Global Business Services renamed Global Capability Centres (October 2026); a Group Chief Data Officer appointed (May 2026); and AI, automation and analytics to lift income per employee by about 20% by 2028.",
              s=["corp"], st="new", o="P", at="Alibaba Cloud", neo=[0, ""], src=[["Alibaba partnership, Jul 2025", ALIBABA], ["GCC rename, Oct 2026", GCC], ["Group CDO, May 2026", CDO], ["Growth plan, May 2026", PLAN]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy, exits & ventures", "blurb": "About 18% RoTE in 2030.", "div": "group", "rev": "co", "products": [
            P("strategy", "2028–30 targets", "RoTE above 15% in 2028 and about 18% in 2030, 5–7% income growth a year, cost:income about 57% in 2028, and $200 billion of wealth net new money by 2028, with affluent clients 75% of WRB income.",
              s=["corp", "aff"], st="new", ay="May 2026", neo=[0, ""], src=[["Growth plan, May 2026", PLAN]]),
            P("exits", "Retail exits", "Exits from Zimbabwe, Angola, Sierra Leone, Cameroon and the Gambia; Tanzania retail sold to Access Bank (June 2025) and Uganda's to Absa (October 2025); Botswana and Zambia retail being sold ⚠ buyers unconfirmed.",
              s=["con"], st="retired", neo=[0, ""], src=[["FY 2025 RNS", FY25], ["Retail Banker International, Oct 2025", EXITS]]),
            P("scv", "SC Ventures", "Almost 30 ventures and more than 30 investments in digital banking, trade and digital assets; Solv India sold to Jumbotail ($238 million gain, 2025); Zodia Custody's custody business being bought into the bank (May 2026).",
              s=["fi"], o="B", neo=[0, ""], src=[["FY 2025 RNS", FY25], ["Solv India sale, Jun 2025", SOLV], ["Zodia Custody deal, May 2026", ZODIA]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: cards split market by market, with Mastercard in Hong Kong, Pakistan and Mox and Visa in the UAE, India, Africa and Trust; cash management and B2B rails; and tokenised deposits and stablecoins.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Hong Kong cards", "blurb": "Cathay on Mastercard.", "div": "hk", "rev": "wrb", "products": [
            P("hkcathay", "Standard Chartered Cathay Mastercard", "The bank's flagship Hong Kong card, in three tiers (standard, Priority Banking, Priority Private), launched with Cathay and Mastercard in July 2021 to replace the Asia Miles Mastercard; a multi-currency Mastercard debit card sits alongside.", short="Cathay (Mastercard)",
              s=["aff", "con"], lc="everyday", ay="Jul 2021", o="P", at="Cathay, Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's anchor programme at the bank in its second-largest market.",
              src=[["Mastercard: Cathay range, Jul 2021", CATHAY], ["SC Hong Kong: credit cards", HKCARDS]]),
            P("hkvisa", "Smart & Simply Cash cards", "Smart Credit Card on Visa Signature and Simply Cash on Visa, with the A. Point Card also accepted at Visa merchants.", short="Smart & Simply Cash (Visa)",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["SC HK: Smart card", HKSMART], ["SC HK: Simply Cash", HKSIMPLY]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Singapore cards", "blurb": "Split about evenly.", "div": "sg", "rev": "wrb", "products": [
            P("sgmc", "Beyond, Simply Cash & Bonus$aver", "Beyond Credit Card, Simply Cash, Bonus$aver World Mastercard and Manhattan World Mastercard: the Mastercard half of the Singapore range.", short="SG Mastercard cards",
              s=["aff", "con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["SC SG: Beyond card", SGBEYOND], ["SC SG: Simply Cash", SGSIMPLY], ["SC SG: credit cards", SGCARDS]]),
            P("sgvisa", "Journey, Smart, Rewards+ & Visa Infinite", "Journey, Smart and Rewards+ (Visa Signature), Prudential Visa Signature and Visa Infinite (S$599.50 a year): the Visa half of the range.", short="SG Visa cards",
              s=["aff", "con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["SC SG: Journey card", SGJOURNEY], ["SC SG: Smart card", SGSMART], ["MainlyMiles: Visa Infinite, May 2026", SGVI]]),
        ]},
        {"id": "2.3", "ic": "globe", "name": "Cards across the network", "blurb": "Pakistan Mastercard, the rest mostly Visa.", "div": "ame", "rev": "wrb", "products": [
            P("pkcards", "Pakistan cards", "Mastercard has been the 'preferred and only partner' for all consumer and business debit and credit cards since a renewal on 18 May 2023, adding World and World Elite; the range includes Saadiq Islamic Mastercards.", short="Pakistan (Mastercard)",
              s=["con", "aff", "sme"], lc="everyday", ay="May 2023", o="P", at="Mastercard", neo=[2, "Mastercard exclusive."],
              mc="The one market where the bank has committed every card to Mastercard.",
              src=[["Brandsynario: Pakistan deal, May 2023", PKMC], ["SC Pakistan: credit cards", PKCARDS]]),
            P("indiacards", "India cards", "Smart Credit Card 'offered on Visa Network', Priority Visa Infinite, Ultimate, Rewards, EaseMyTrip and Beyond cards; public pages name only Visa ⚠.", short="India (Visa)",
              s=["con", "aff"], lc="everyday", o="P", at="Visa", neo=[0, "Visa ⚠."], src=[["SC India: credit cards", INCARDS], ["SC India: Smart card", INSMART]]),
            P("mecards", "UAE cards", "Infinite, Cashback, Manhattan Rewards+, X and Saadiq credit cards, all on Visa.", short="UAE (Visa)",
              s=["con", "aff"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["SC UAE: credit cards", AECARDS]]),
            P("africacards", "Africa & other Asian cards", "Kenya and Ghana debit and credit on Visa (Gold, Platinum, Infinite); Bangladesh mostly Visa with Simply Cash on Mastercard; Indonesia mostly Mastercard.", short="Africa & Asia (mixed)",
              s=["con"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Mostly Visa; Indonesia mostly Mastercard."], src=[["SC Kenya: cards", KECARDS], ["SC Ghana: cards", GHCARDS], ["SC Bangladesh: cards", BDCARDS], ["SC Indonesia: cards", IDCARDS]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Digital-bank cards", "blurb": "Mox on Mastercard, Trust on Visa.", "div": "mox", "rev": "wrb", "products": [
            P("moxcard", "Mox Credit", "A Mastercard credit card that switches between Asia Miles and unlimited cashback with no FX fees; Hong Kong's seventh-largest card portfolio, used in nearly 157 million transactions and paying out 1.8 billion Asia Miles to date.", short="Mox Credit (Mastercard)",
              s=["dig"], lc="everyday", ay="Sep 2020", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mox is taking on part of the bank's Hong Kong retail book, so its Mastercard spend should grow.",
              src=[["Mox: Mox Credit", MOXCREDIT], ["FY 2025 RNS", FY25]]),
            P("trustcard", "Trust card", "Trust Bank's credit and debit cards on Visa ⚠ (secondary source); card spend grew 39% in 2025.", short="Trust (Visa)",
              s=["dig"], lc="everyday", o="P", at="Visa", neo=[0, "Visa ⚠."], src=[["Dollars and Sense: Trust guide", TRUSTVISA], ["FY 2025 RNS", FY25]]),
        ]},
        {"id": "2.5", "ic": "send", "name": "Payments & cross-border", "blurb": "$2.1bn in a half.", "div": "group", "rev": "cib", "products": [
            P("payments", "Cash management & payments", "Payments & Liquidity income of about $2.1 billion in H1 2026; collections, clearing and payments merged under a new Global Head of Payments (May 2026) covering traditional and on-chain flows.",
              s=["corp", "fi", "sme"], lc="move", st="new", neo=[None, "No card-network role disclosed."], src=[["HY 2026 RNS", HY26RNS], ["Global Head of Payments, Mar 2026", PAYHEAD]]),
            P("visab2b", "Visa B2B Connect", "Participant and Visa's settlement partner for B2B Connect (April 2024), settling in the UAE and Singapore with the US planned.",
              s=["corp"], lc="move", ay="Apr 2024", o="P", at="Visa", neo=[0, "Visa."], src=[["SC: Visa B2B Connect, Apr 2024", VISAB2B]]),
            P("mcsend", "Mastercard Send", "Chosen in October 2017 for cross-border push payments to cards, wallets and cash-out points across the Middle East and Africa ⚠ current use unknown.",
              s=["con", "sme"], lc="move", ay="Oct 2017", o="P", at="Mastercard", neo=[3, "Mastercard's own ⚠ status."], src=[["Asian Banker: Mastercard Send, Oct 2017", SEND]]),
            P("banktowallet", "Bank-to-wallet payments", "Live trials with Ant International and Swift (August 2025) sending from Standard Chartered accounts to wallets on Alipay+, which reaches 36 wallets and 1.7 billion accounts.",
              s=["con", "corp"], lc="move", st="new", o="P", at="Ant International, Swift", neo=[0, ""], src=[["Ant, SC and Swift, Aug 2025", ANTSWIFT]]),
        ]},
        {"id": "2.6", "ic": "coins", "name": "Digital money", "blurb": "Tokenised deposits, HKDAP, USDC.", "div": "group", "rev": "cib", "products": [
            P("tokdep", "Tokenised deposits", "SGD and USD tokenised balances for Ant International's treasury (December 2025) and the first live interbank tokenised-deposit trade on Swift's ledger, with HSBC (August 2026).",
              s=["corp", "fi"], lc="move", st="new", o="P", at="Ant International, Swift, HSBC", neo=[0, ""], src=[["Tokenised deposits, Dec 2025", TOKDEP], ["HSBC and SC on Swift, Aug 2026", SWIFTTD]]),
            P("stablecoins", "Stablecoins: HKDAP & USDC", "Anchorpoint (with HKT and Animoca) licensed to issue the HKDAP stablecoin (April 2026) and Standard Chartered Hong Kong its first bank distributor (August 2026); USDC minting and redemption with Circle from DIFC (July 2026); banking partner for DCS's DeCard stablecoin card (November 2025).",
              s=["corp", "fi"], lc="move", st="new", o="P", at="Anchorpoint, Circle, DCS", neo=[0, "DeCard's network not stated."],
              mc="Stablecoin spend on cards and stablecoin settlement are open ground here.",
              src=[["Anchorpoint licence, Apr 2026", ANCHOR], ["HKDAP distributor, Aug 2026", HKDAP], ["Circle USDC, Jul 2026", CIRCLE], ["DeCard, Nov 2025", DECARD]]),
            P("mtn", "Mastercard tokenisation pilot", "A proof of concept on tokenised deposits and tokenised carbon credits with Mastercard, Mox and Libeara in the HKMA sandbox (May 2024).",
              s=["fi"], lc="move", ay="May 2024", o="P", at="Mastercard, Libeara", neo=[3, "Mastercard Multi-Token Network; pilot only."], src=[["Mastercard: MTN pilot, May 2024", MTN]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: financial-crime controls, AI for wealth advice and treasury, APIs, rewards built on Cathay and sport, an agentic pilot with Visa, and digital-asset custody and trading.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Financial crime & risk", "blurb": "No named partner.", "div": "group", "rev": "co", "products": [
            P("fincrime", "Fraud, cyber & financial crime", "The 2026 risk review flags AI-enabled cyber threats and the new risks of stablecoins; no named fraud-scoring partner is public ⚠.",
              s=["con", "corp"], lc="everyday", neo=[None, "Nothing public."], src=[["HY 2026 RNS", HY26RNS]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "AI for clients", "blurb": "Aladdin Wealth, AI treasury.", "div": "group", "rev": "wrb", "products": [
            P("wealthai", "myWealth Advisor & AI marketing", "myWealth Advisor upgraded with BlackRock's Aladdin Wealth (July 2026), and an AI-driven campaign for affluent clients (September 2026).",
              s=["aff"], lc="grow", st="new", o="P", at="BlackRock", neo=[0, ""], src=[["Aladdin Wealth, Jul 2026", ALADDIN], ["Wealth campaign, Sep 2026", CAMPAIGN]]),
            P("treasuryai", "AI treasury & FX", "AI-powered treasury and FX management tools built with Ant International (August 2025).",
              s=["corp"], lc="move", o="P", at="Ant International", neo=[0, ""], src=[["Ant International AI, Aug 2025", ANTAI]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "APIs & connectivity", "blurb": "Virtual accounts, Finmo.", "div": "group", "rev": "cib", "products": [
            P("apis", "APIs & virtual accounts", "API treasury connectivity and global currency accounts with Finmo (November 2025), and virtual accounts and APIs for fintech clients such as DCS.",
              s=["corp", "fi"], lc="move", o="P", at="Finmo", neo=[0, ""], src=[["Finmo, Nov 2025", FINMO], ["DeCard, Nov 2025", DECARD]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards & loyalty", "blurb": "Asia Miles, F1, Liverpool.", "div": "group", "rev": "wrb", "products": [
            P("rewards", "Rewards & partnerships", "Card points with miles transfer cut to KrisFlyer and Asia Miles in Singapore (2024), the Cathay co-brand in Hong Kong, and Formula 1 (from 2026) and Liverpool FC (Global Partner from 2027/28) for client experiences.",
              s=["aff", "con"], lc="grow", st="flux", o="P", at="Cathay, Formula 1, Liverpool FC", neo=[1, "The Cathay co-brand is Mastercard."],
              mc="Priceless experiences could sit with the F1 and Liverpool deals.",
              src=[["MainlyMiles, May 2026", SGVI], ["Formula 1 partnership, Jan 2026", F1], ["Liverpool FC, Sep 2026", LFC]]),
            P("agentic", "Agentic payments pilot", "Standard Chartered and Trust Bank are among 13 issuers testing agent-initiated payments in Visa Agentic Ready in Singapore (April 2026).",
              s=["con", "dig"], lc="everyday", st="new", ay="Apr 2026", o="P", at="Visa", neo=[0, "Visa."],
              mc="Agent Pay has no foothold yet; Visa ran the first pilot.",
              src=[["Visa Agentic Ready, Apr 2026", AGENTIC]]),
        ]},
        {"id": "3.5", "ic": "key-round", "name": "Digital-asset custody & trading", "blurb": "Bitcoin to RLUSD.", "div": "group", "rev": "cib", "products": [
            P("custody", "Digital-asset custody", "Institutional custody in Hong Kong (first G-SIB, May 2026), Singapore (October 2026), Luxembourg and DIFC, RLUSD custody with Ripple (October 2026), and Zodia Custody's business being folded in.",
              s=["fi"], lc="grow", st="new", neo=[0, ""], src=[["HK custody, May 2026", HKCUSTODY], ["Singapore custody, Oct 2026", SGCUSTODY], ["RLUSD custody, Oct 2026", RLUSD], ["Zodia Custody deal, May 2026", ZODIA]]),
            P("cryptotrade", "Crypto trading", "Bitcoin and ether spot trading for institutions in the UK (July 2025) and UAE (September 2026), and for affluent clients in the UAE through their bank accounts, licensed by VARA (October 2026).",
              s=["fi", "aff"], lc="grow", st="new", o="P", at="Zodia Markets", neo=[0, ""], src=[["Institutional trading, Jul 2025", INSTTRADE], ["UAE spot, Sep 2026", UAESPOT], ["Affluent crypto, Oct 2026", AFFCRYPTO]]),
            P("tempo", "Zodia Custody on Tempo", "Zodia Custody by Standard Chartered is among the first external validators on the Tempo payments blockchain alongside Visa and Stripe (2026 ⚠ date).",
              s=["fi"], lc="move", st="new", o="P", at="Visa, Stripe", neo=[0, "Visa's node."], src=[["Visa: Tempo validator", TEMPO]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What clients buy: affluent wealth management, the growth engine; retail and SME banking; the Mox and Trust digital banks; and corporate and investment banking for 17,000 cross-border clients.",
    "tiles": [
        {"id": "4.1", "ic": "gem", "name": "Wealth", "blurb": "$33bn NNM in a half.", "div": "group", "rev": "wrb", "products": [
            P("wealth", "Affluent wealth management", "Wealth Solutions income of $2.1 billion in H1 2026 (+39%), record affluent net new money of $33 billion and 150,000 new affluent clients; Priority, Priority Private and Private Bank tiers; the third-largest wealth manager in Asia, by its own account.",
              s=["aff"], lc="grow", neo=[1, "Premium cards split by market."], src=[["HY 2026 RNS", HY26RNS], ["Growth plan, May 2026", PLAN]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Retail & SME", "blurb": "Reshaped toward affluent.", "div": "group", "rev": "wrb", "products": [
            P("retail", "Personal & SME banking", "Deposits, mortgages, cards and personal loans (CCPL income down 2% in H1 2026 after portfolio optimisation) and SME banking for entrepreneurs; mass retail is being reshaped to feed future affluent clients.",
              s=["con", "sme"], lc="everyday", st="flux", neo=[1, "Cards split by market."], src=[["HY 2026 RNS", HY26RNS], ["FY 2025 RNS", FY25]]),
        ]},
        {"id": "4.3", "ic": "rocket", "name": "Digital banks", "blurb": "Mox and Trust.", "div": "mox", "rev": "wrb", "products": [
            P("mox", "Mox Bank", "Hong Kong digital bank launched in September 2020 with HKT, PCCW and Trip.com: about 750,000 customers (end-2025), deposits up 21% and unsecured loans up 115%, Mox Invest and Mox Insure; taking on part of the bank's Hong Kong retail clients from 2026.",
              s=["dig"], lc="everyday", st="flux", ay="Sep 2020", o="P", at="HKT, PCCW, Trip.com", neo=[1, "Mox Credit is Mastercard."], src=[["FY 2025 RNS", FY25], ["Growth plan, May 2026", PLAN]]),
            P("trust", "Trust Bank", "Singapore digital bank launched in 2022 with FairPrice Group: more than one million customers, over 20% of adults, the fourth-largest retail bank there; TrustInvest funds and US stocks added in 2025.",
              s=["dig"], lc="everyday", ay="2022", o="P", at="FairPrice Group", neo=[0, "Visa ⚠."], src=[["FY 2025 RNS", FY25], ["Trust Bank", TRUST]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Corporate & Investment Banking", "blurb": "$6.9bn in a half.", "div": "group", "rev": "cib", "products": [
            P("cib", "Transaction Services, Global Banking & Markets", "CIB income of $6.9 billion in H1 2026, Global Banking up 20%; more than 17,000 clients across trade, payments, lending, capital markets and markets, with RMB, Islamic and sustainable finance.",
              s=["corp", "fi"], lc="borrow", neo=[0, ""], src=[["HY 2026 RNS", HY26RNS], ["FY 2025 RNS", FY25]]),
            P("fss", "Financing & Securities Services", "Custody, clearing and settlement, merged with transaction banking and digital assets under Ole Matthiessen (March 2026).",
              s=["fi"], lc="grow", st="new", neo=[0, ""], src=[["Zodia Custody deal, May 2026", ZODIA], ["HY 2026 RNS", HY26RNS]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How clients reach the bank: SC Mobile in each market, Straight2Bank for companies, branches and four wealth hubs, and partners from Cathay to Alipay+.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "SC Mobile & apps", "blurb": "Plus Mox and Trust.", "div": "group", "rev": "wrb", "products": [
            P("scmobile", "SC Mobile & online banking", "Market-by-market apps and online banking; Mox's app is rated 4.8 out of 5 in Hong Kong. Group app-user numbers are not published ⚠.",
              s=["con", "aff", "dig"], lc="everyday", neo=[0, ""], src=[["FY 2025 RNS", FY25]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Straight2Bank", "blurb": "The corporate portal.", "div": "group", "rev": "cib", "products": [
            P("s2b", "Straight2Bank", "The corporate banking portal and onboarding channel, with API links for treasuries.",
              s=["corp", "sme"], lc="open", neo=[0, ""], src=[["About Standard Chartered", ABOUT], ["Finmo, Nov 2025", FINMO]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & wealth hubs", "blurb": "Four global wealth hubs.", "div": "ame", "rev": "wrb", "products": [
            P("branches", "Branches & wealth hubs", "Branches in each market and four global wealth hubs, the UAE among them; branches are closing in markets the bank is leaving.",
              s=["aff", "con"], lc="open", st="flux", neo=[0, ""], src=[["Affluent crypto, Oct 2026", AFFCRYPTO], ["Retail Banker International, Oct 2025", EXITS]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners", "blurb": "Cathay, FairPrice, Alipay+.", "div": "group", "rev": "wrb", "products": [
            P("partners", "Partners & ecosystems", "Cathay (Hong Kong co-brand), HKT and Trip.com (Mox), FairPrice (Trust), Ant International and Alipay+, Circle, DCS and Alibaba Cloud.",
              s=["con", "dig", "corp"], lc="open", o="P", neo=[1, "The Cathay co-brand is Mastercard."], src=[["Mastercard: Cathay range, Jul 2021", CATHAY], ["FY 2025 RNS", FY25], ["Ant, SC and Swift, Aug 2025", ANTSWIFT]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Standard Chartered", "blurb": "Hong Kong, Pakistan and Mox.", "products": [
        P("mcatstanchart", "Mastercard at Standard Chartered", "Mastercard carries the Cathay co-brand in Hong Kong (2021), Mox Credit, half of the Singapore range, all cards in Pakistan under a 2023 exclusive, and most of Indonesia; it ran a tokenisation pilot with Mox and Libeara (2024) and Send in the Middle East and Africa (2017 ⚠). Visa has the UAE, India, Kenya, Ghana, Trust Bank, B2B Connect and the agentic pilot.",
          s=["con"], div="group", rev="wrb", mc="The relationship this map is drawn for.",
          src=[["Mastercard: Cathay range, Jul 2021", CATHAY], ["Brandsynario: Pakistan deal, May 2023", PKMC], ["SC: Visa B2B Connect, Apr 2024", VISAB2B]]),
    ]},
    {"id": "pillar-market", "name": "Markets & regulation", "blurb": "Stablecoins, instant rails.", "products": [
        P("market", "The footprint's markets", "Hong Kong's stablecoin regime (from August 2025) and FPS, Singapore's PayNow and Project Guardian, the UAE's VARA, and instant rails such as UPI and Raast ⚠ that compete with cards.",
          s=["corp"], div="group", rev="co", src=[["HKMA: FPS", FPS], ["MAS: PayNow", PAYNOW], ["Anchorpoint licence, Apr 2026", ANCHOR]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
