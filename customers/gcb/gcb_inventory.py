"""GCB Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own as reported: the H1 2026 statement (Daily Graphic, 29 July 2026) and the FY2025 results
(25 March 2026, via IC Securities and the Ghanaian Times). GCB's live website sits behind a bot check, so product
pages are cited from Internet Archive snapshots of gcbbank.com.gh (January to April 2026) and the 2025 tariff guide.
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://www.graphic.com.gh/business/business-news/ghana-news-gcb-posts-ghc1-23bn-half-year-profit.html"
FY25 = "https://cms.ic.africa/wp-content/uploads/2026/03/ICSGH_GCB_Bank_FY2025_Commentary.02.pdf"
FY25GT = "https://ghanaiantimes.com.gh/gcb-bank-posts-record-gh%c2%a23-17-bn-profit-for-2025/"
PWC = "https://ghanaiantimes.com.gh/gcb-takes-17-8-of-ghanas-credit-market-share-as-lending-lead-widens/"
GSE = "https://gse.com.gh/listed-company/gcb/"
WIKI = "https://en.wikipedia.org/wiki/GCB_Bank"
ABOUT = "https://web.archive.org/web/20260310234951/https://www.gcbbank.com.gh/about-us"
HOME = "https://web.archive.org/web/20260416212857/https://www.gcbbank.com.gh/"
DEBIT = "https://web.archive.org/web/20260316031048/https://www.gcbbank.com.gh/personal/eproducts-cards/debit-cards"
HNW = "https://web.archive.org/web/20260416203539/https://www.gcbbank.com.gh/personal/eproducts-cards/signature-infinite-cards"
MOBILE = "https://web.archive.org/web/20260316015930/https://www.gcbbank.com.gh/personal/eproducts-cards/mobile-banking"
REMIT = "https://web.archive.org/web/20260316025026/https://www.gcbbank.com.gh/remittance"
SMEPAGE = "https://web.archive.org/web/20260316022554/https://www.gcbbank.com.gh/business/business-critical/sme-solution"
FEES = "https://web.archive.org/web/20260122153553/https://gcbbank.com.gh/business/payment-solutions/fee-collection"
TARIFF = "https://web.archive.org/web/20250421111644/https://www.gcbbank.com.gh/downloads/informational/432-2025-tariff-guide/file"
GMFS = "https://gmfs.africa/who-we-are/"
GMFSDO = "https://gmfs.africa/what-we-do/"
MD = "https://gna.org.gh/2025/01/gcb-bank-appoints-farihan-alhassan-as-new-managing-director/"
MALC = "https://www.citinewsroom.com/?p=1321339"
FINTECH = "https://www.citinewsroom.com/?p=1326382"
MODEFIN = "https://citinewsroom.com/2023/12/gcb-modefin-receive-most-impactful-project-award-at-ibsi-gfia-2023/"
OUTLOOK = "https://www.graphic.com.gh/business/business-news/gcb-is-ready-to-deliver-more-value-greater-opportunities-in-2026.html"
VISA24 = "https://www.citinewsroom.com/2024/12/gcb-bank-partners-with-visa-to-launch-premium-cards-elevating-banking-experience-in-ghana/"
VISA26 = "https://www.citinewsroom.com/?p=1361445"
VISABIZ = "https://ghanaiantimes.com.gh/gcb-launches-visa-business-cards-in-accra/amp/"
MC2008 = "https://thepaypers.com/cards/ghana-commercial-banks-launches-mastercard-debit-card-line--735617"
INSTANT = "https://gna.org.gh/?p=123404"
LITEPAY = "https://graphic.com.gh/news/general-news/gcb-launches-card-payment-solution.html"
PAPSS1 = "https://ghanaiantimes.com.gh/gcb-completes-first-papss-client-transaction-in-ghana/amp/"
PAPSS26 = "https://myjoyonline.com/papss-applauds-gcb-banks-leadership-in-advancing-cross-border-payments-across-africa"
BEIJING = "https://www.citinewsroom.com/2025/10/gcb-bank-deepens-ghana-china-trade-ties-in-talks-with-chinese-officials/"
CHINA = "https://gna.org.gh/2026/03/gcb-bank-reaffirms-commitment-to-ghana-china-economic-ties/"
CIIE = "https://ghanaiantimes.com.gh/gcb-bank-lands-strategic-role-in-ghanas-global-trade-expansion-drive/"
GHIPSS = "https://ghipss.net/industry-performance/"
BOGMOMO = "https://ghanaiantimes.com.gh/mobile-money-transactions-hit-gh%c2%a24-54trn-in-2025-bog/"
GHIPSSVISA = "https://ghanaiantimes.com.gh/ghipss-signs-deal-with-visa-to-facilitate-digital-payments-in-ghana"
MCMTN = "https://techafricanews.com/2024/02/29/mastercard-mtn-group-fintech-forge-alliance-for-digital-payment-expansion-across-africa/"
MCOFFICE = "https://techafricanews.com/2025/01/13/mastercard-opens-first-office-in-ghana-expanding-west-africa-operations/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · state roots · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Ghana's largest lender and deposit taker, GH¢67 billion of assets and profit up 46% in the half, a 1953 state bank listed since 1996 with the government still its biggest holder, and a 2025–28 strategy turning towards transaction banking.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "GH¢67bn of assets.", "div": "gcb", "rev": "treasury", "products": [
            P("balance", "Balance sheet & earnings", "H1 2026: profit after tax GH¢1.23 billion (+46.4%), deposits GH¢51.5 billion, net loans GH¢22.2 billion, total assets GH¢67.4 billion, NPL ratio 4.7% and CAR 15.9%. FY2025: profit before tax GH¢3.17 billion and after tax about GH¢2.1 billion, cost-to-income 47.2%.",
              s=["corp"], neo=[0, ""], src=[["Daily Graphic: H1 2026, 29 Jul 2026", H1], ["IC Securities: FY2025, 27 Mar 2026", FY25], ["Ghanaian Times: FY2025, 31 Mar 2026", FY25GT]]),
            P("share", "Market position", "Ghana's largest lender (17.8% of industry loans in 2025, 17.9% at June 2026) and deposit taker (12.37%), per PwC's 2026 Ghana Banking Survey.",
              s=["corp"], neo=[0, ""], src=[["Ghanaian Times: PwC survey, 31 Aug 2026", PWC]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & ownership", "blurb": "Alhassan and Alabi; state-rooted.", "div": "gcb", "rev": "corporate", "products": [
            P("leadership", "Board & management", "Chair Prof. Joshua Alabi; Managing Director Farihan Alhassan since January 2025 (ex-Stanbic, ex-Barclays), who joined Mastercard's Africa Leadership Council in March 2026; Chief Digital Officer Patrick George Quantson.",
              s=["corp"], neo=[0, "The MD sits on Mastercard's Africa council."], src=[["GNA: new MD, Jan 2025", MD], ["GSE: GCB listing", GSE], ["Citi Newsroom: Mastercard council, Mar 2026", MALC]]),
            P("ownership", "Ownership & heritage", "Founded in 1953 as the Bank of the Gold Coast, listed on the Ghana Stock Exchange on 17 May 1996 with 265 million shares; the government holds about 21% ⚠. It took on UT Bank and Capital Bank assets in 2017. Market value about GH¢10.9 billion at March 2026 prices ⚠.",
              s=["corp"], o="I", neo=[0, ""], src=[["GSE: GCB listing", GSE], ["Wikipedia: GCB Bank", WIKI], ["GCB: about us", ABOUT]]),
        ]},
        {"id": "1.3", "ic": "target", "name": "Strategy 2025–28", "blurb": "Towards transaction banking.", "div": "gcb", "rev": "corporate", "products": [
            P("strategy", "Medium-term strategy 2025–2028", "Shift from a retail-funded model towards wholesale, commercial and transaction banking; grow fee income (37% of operating income in H1 2026); digital self-service and payments; 30% women in leadership by 2028; expansion into other African countries ⚠.",
              s=["corp"], st="new", neo=[0, ""], src=[["Ghanaian Times: FY2025, 31 Mar 2026", FY25GT], ["Graphic: GCB in 2026, Feb 2026", OUTLOOK]]),
            P("ddep", "Debt exchange & dividend", "Heavy holdings of government and COCOBOD paper hit by the 2022–23 debt exchange; the Bank of Ghana blocked the FY2024 dividend in May 2025 when COCOBOD exposure breached the single-obligor limit.",
              s=["corp"], st="flux", neo=[0, ""], src=[["IC Securities: FY2025, 27 Mar 2026", FY25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology", "blurb": "Modefin app, ISO 22301.", "div": "gcb", "rev": "retail", "products": [
            P("tech", "Core, channels & resilience", "A 2020 system migration that enabled instant card issuance at every branch, a mobile app built with India's Modefin (IBSi award, December 2023) and ISO 22301 business-continuity certification. No public AI programme ⚠.",
              s=["con"], o="P", at="Modefin", neo=[0, ""], src=[["GNA: instant issuance, Jul 2020", INSTANT], ["Citi Newsroom: Modefin award, Dec 2023", MODEFIN], ["GCB: about us", ABOUT]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: ReadyCash on gh-link and debit on both Visa and Mastercard, Visa's premium tier, the Corporate Mastercard and Visa business cards, Lite Pay acceptance, GhIPSS instant transfers, the G-Money wallet, and PAPSS and remittances across borders.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "gh-link, Visa, Mastercard.", "div": "personal", "rev": "retail", "products": [
            P("readycash", "ReadyCash", "GCB's own debit card, free with every new account, for GCB and other banks' ATMs and gh-link merchants.", short="ReadyCash (gh-link)",
              s=["con"], lc="everyday", o="B", neo=[0, "gh-link."], src=[["GCB: debit cards", DEBIT], ["GCB: tariff guide 2025", TARIFF]]),
            P("debit", "Visa & Mastercard debit", "Consumer, business and corporate debit in matching tiers: Mastercard Standard or Visa Classic, Gold and Platinum, with chip, PIN, contactless and 3-D Secure. GCB calls itself Ghana's largest card issuer; the split by network is not published ⚠. GCB has been a Mastercard principal since 2008.", short="Debit (Visa & Mastercard)",
              s=["con", "sme"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard, tier for tier."],
              mc="Mastercard's main volume at GCB; both networks are offered side by side.",
              src=[["GCB: debit cards", DEBIT], ["The Paypers: Mastercard launch, Oct 2008", MC2008]]),
            P("upi", "UnionPay card", "UnionPay cards issued since August 2020 and priced in the 2025 tariff guide.",
              s=["con", "trade"], lc="everyday", ay="Aug 2020", o="P", at="UnionPay", neo=[0, "UnionPay."], src=[["GNA: instant issuance, Jul 2020", INSTANT], ["GCB: tariff guide 2025", TARIFF]]),
        ]},
        {"id": "2.2", "ic": "gem", "name": "Premium cards", "blurb": "Visa Signature and Infinite.", "div": "private", "rev": "retail", "products": [
            P("hnw", "Visa Signature & Infinite", "High-net-worth debit cards for private-banking clients, launched with Visa on 18 December 2024: GH¢100,000 daily limit, 1,200+ airport lounges, concierge and travel insurance; Infinite by invitation for $20,000+ of annual spend.", short="Signature & Infinite (Visa)",
              s=["hnw"], lc="everyday", st="new", ay="Dec 2024", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa holds GCB's top tier; there is no Mastercard World or World Elite card.",
              src=[["Citi Newsroom: Visa premium cards, Dec 2024", VISA24], ["GCB: Signature & Infinite", HNW]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Business & corporate cards", "blurb": "Corporate Mastercard, Visa business.", "div": "business", "rev": "corporate", "products": [
            P("corpmc", "Corporate Mastercard", "A corporate card first launched in October 2008, still priced in the 2025 tariff guide, with its own corporate card portal ⚠.", short="Corporate (Mastercard)",
              s=["corp"], lc="move", ay="Oct 2008", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="The one programme that is wholly Mastercard's.",
              src=[["The Paypers: Mastercard launch, Oct 2008", MC2008], ["GCB: tariff guide 2025", TARIFF], ["GCB: homepage", HOME]]),
            P("visabiz", "Visa business debit & prepaid", "Debit and prepaid cards for commercial, SME and corporate clients, with partner-merchant discounts of up to 15%; launched about October 2022 ⚠.", short="Business & prepaid (Visa)",
              s=["sme", "corp"], lc="move", o="P", at="Visa", neo=[0, "Visa."], src=[["Ghanaian Times: Visa business cards", VISABIZ], ["GCB: tariff guide 2025", TARIFF]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acceptance", "blurb": "Lite Pay and POS.", "div": "business", "rev": "business", "products": [
            P("litepay", "Lite Pay & POS", "Smartphone card readers for taxis, delivery riders and mobile vendors (launched March 2016) and POS terminals, accepting ReadyCash, gh-link, Visa and Mastercard; merchant charge 3% on cards and 1.5% on mobile money (2025 tariff).",
              s=["sme"], lc="move", ay="Mar 2016", o="B", neo=[1, "Accepts every network."],
              mc="Ten years old; Tap on Phone and QR could replace it.",
              src=[["Graphic: Lite Pay launch, Mar 2016", LITEPAY], ["GCB: tariff guide 2025", TARIFF]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Instant payments", "blurb": "GhIPSS Instant Pay.", "div": "gcb", "rev": "retail", "products": [
            P("gip", "Instant interbank transfers", "Instant transfers to any Ghanaian bank over GhIPSS Instant Pay from the app and internet banking; GIP carried 202.8 million transactions worth GH¢712 billion across the market in 2025, doubling in value.",
              s=["con", "sme"], lc="move", o="P", at="GhIPSS", neo=[0, "GhIPSS."],
              mc="Account-to-account rails now carry far more value than cards in Ghana.",
              src=[["GCB: tariff guide 2025", TARIFF], ["GhIPSS: industry performance 2025", GHIPSS], ["Ghanaian Times: Bank of Ghana oversight report, Oct 2026", BOGMOMO]]),
        ]},
        {"id": "2.6", "ic": "wallet", "name": "G-Money", "blurb": "GCB's own mobile wallet.", "div": "gmoney", "rev": "retail", "products": [
            P("gmoney", "G-Money wallet", "A telco-agnostic wallet launched in 2020 (USSD *488#, app, agents) for transfers to any wallet or bank, merchant and GhQR payments, loans, G-Susu savings and loyalty points; now G-Money Financial Services, one of five Bank of Ghana dedicated e-money issuers. Passed 2 million users in 2023 ⚠.", short="G-Money (mobile money)",
              s=["wal"], lc="everyday", ay="Jan 2020", o="B", neo=[0, "Mobile money rails."],
              mc="Mastercard put a companion card on every MTN MoMo wallet in 2024; G-Money has none.",
              src=[["G-Money: who we are", GMFS], ["G-Money: what we do", GMFSDO], ["GCB: about us", ABOUT]]),
            P("gmoneybiz", "G-Money for business", "Bulk on-net and cross-net disbursements such as salaries, group collections, a corporate portal and an agent and merchant app.",
              s=["sme", "wal"], lc="move", o="B", neo=[0, ""], src=[["G-Money: what we do", GMFSDO]]),
        ]},
        {"id": "2.7", "ic": "earth", "name": "Cross-border", "blurb": "PAPSS, remittances, RMB.", "div": "afro", "rev": "treasury", "products": [
            P("papss", "PAPSS", "The first commercial bank to process a live payment on the Pan-African Payment and Settlement System (Ghana to Nigeria, about March 2023 ⚠) and PAPSS' gateway bank in Ghana for local-currency settlement; fee 1.5% (minimum $2, cap $100).",
              s=["trade", "sme"], lc="move", o="P", at="PAPSS (Afreximbank)", neo=[0, "PAPSS."], src=[["Ghanaian Times: first PAPSS transaction", PAPSS1], ["MyJoyOnline: PAPSS visit, Jul 2026", PAPSS26], ["GCB: tariff guide 2025", TARIFF]]),
            P("remit", "Remittances & transfers", "Inbound money-transfer operators, same-day SWIFT outbound, GCB Xpress branch-to-branch transfers and Link2Home accounts for Ghanaians abroad.",
              s=["dia"], lc="move", o="P", at="Money-transfer operators", neo=[0, "MTOs and SWIFT."],
              mc="Diaspora inflows run through MTOs and SWIFT; Mastercard Move is absent.",
              src=[["GCB: remittance", REMIT]]),
            P("rmb", "Cedi–RMB settlement", "Proposed in Beijing on 12 October 2025: direct cedi–RMB settlement and a framework with Chinese institutions over CIPS for Ghana–China trade ⚠ not yet live.",
              s=["trade"], lc="move", st="unconf", o="P", at="CIPS", neo=[0, "CIPS (planned)."], src=[["Citi Newsroom: Beijing talks, Oct 2025", BEIJING]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: chip, PIN and 3-D Secure on cards and Ghana Card biometrics for onboarding, Amber Club for top clients, collections and bill-payment platforms, and a data offer coming from Visa.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security & identity", "blurb": "3-D Secure, Ghana Card.", "div": "gcb", "rev": "retail", "products": [
            P("security", "Card security", "EMV chip, PIN, contactless limits and 3-D Secure on Visa and Mastercard cards; a published cyber-security policy. No named fraud-scoring partner ⚠.",
              s=["con"], lc="everyday", neo=[1, "Scheme 3-D Secure on both networks."],
              mc="No public fraud or scam tools at GCB; Mastercard runs a fraud forum in Ghana.",
              src=[["GCB: debit cards", DEBIT], ["GCB: homepage", HOME]]),
            P("ghcard", "Ghana Card onboarding", "Mobile account opening with the national Ghana Card and facial biometrics, plus a portal to link the Ghana Card to accounts.",
              s=["con"], lc="open", st="new", neo=[0, ""], src=[["Citi Newsroom: FinTech awards, Mar 2026", FINTECH], ["GCB: homepage", HOME]]),
        ]},
        {"id": "3.2", "ic": "gift", "name": "Loyalty & premium service", "blurb": "Amber Club.", "div": "private", "rev": "retail", "products": [
            P("amber", "Amber Club & rewards", "Relationship banking for the top 100 customers, Visa concierge and lounge benefits for Signature and Infinite holders, the Pa To Pa savers' promotion (2026) and G-Money loyalty points.",
              s=["hnw", "con"], lc="grow", st="new", neo=[0, "Visa benefits at the top."],
              mc="Priceless experiences and card-linked offers are untried here.",
              src=[["Ghanaian Times: FY2025, 31 Mar 2026", FY25GT], ["Graphic: GCB in 2026, Feb 2026", OUTLOOK], ["GCB: Signature & Infinite", HNW]]),
        ]},
        {"id": "3.3", "ic": "receipt-text", "name": "Collections & bill payments", "blurb": "GCB-Pay, Smart Pay, fees.", "div": "business", "rev": "business", "products": [
            P("gcbpay", "GCB-Pay, Smart Pay & ePay", "GCB's payment and bill-presentment portals for individuals and corporates, linked from the 2026 homepage.",
              s=["sme", "corp"], lc="move", o="B", neo=[None, "Nothing public."], src=[["GCB: homepage", HOME]]),
            P("fees", "School fee collection", "An electronic platform that collects fees for second-cycle schools at 183 branches with real-time credit to the school's account.",
              s=["corp"], lc="move", o="B", neo=[0, ""], src=[["GCB: fee collection", FEES]]),
        ]},
        {"id": "3.4", "ic": "brain", "name": "Data & insight", "blurb": "Visa offers insights.", "div": "gcb", "rev": "retail", "products": [
            P("data", "Customer data & marketing", "No public analytics or AI programme. In June 2026 Visa's Ghana team offered GCB data-driven insights, targeted communication and digital engagement ⚠.",
              s=["con"], lc="everyday", st="unconf", o="P", at="Visa", neo=[0, "Visa offers the insights."],
              mc="Visa is first in with data; Mastercard's data and offers tools are the counter.",
              src=[["Citi Newsroom: GCB and Visa, Jun 2026", VISA26]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: everyday accounts, salary loans and buy now pay later; SME banking; Ghana's largest corporate and state-enterprise loan book; trade finance and the Afro-Asia desk; and GCB Capital.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Personal banking", "blurb": "Accounts, loans, BNPL.", "div": "personal", "rev": "retail", "products": [
            P("accounts", "Current & savings accounts", "Current, salary, savings, KidiStar, student, Hajj and Link2Home accounts; 93% of deposits are current and savings (CASA).",
              s=["con", "dia"], lc="everyday", neo=[0, "ReadyCash on gh-link by default."], src=[["GCB: homepage", HOME], ["IC Securities: FY2025, 27 Mar 2026", FY25]]),
            P("loans", "Personal loans & Salary Advance", "24-hour personal loans, Salary Advance, the Easy Pick scheme and loans against investments.",
              s=["con"], lc="borrow", st="new", neo=[0, ""], src=[["GCB: homepage", HOME], ["Graphic: GCB in 2026, Feb 2026", OUTLOOK]]),
            P("bnpl", "Buy Now Pay Later", "Instalment finance at listed vendors, promoted on the 2026 homepage.",
              s=["con"], lc="borrow", st="new", o="B", neo=[0, "GCB's own credit."],
              mc="Instalments sit off the card rails.",
              src=[["GCB: homepage", HOME]]),
            P("bancassurance", "Bancassurance", "Homecall, Child Education, Wealth Master and Ultimate Protection plans.",
              s=["con"], lc="grow", o="P", neo=[0, ""], src=[["GCB: homepage", HOME]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "SME & commercial", "blurb": "SME Solution, Ewuraba.", "div": "business", "rev": "business", "products": [
            P("sme", "SME Solution & Ewuraba", "Accounts, business debit cards, loans and overdrafts, bulk cash collection, payroll, trade finance and advisory for small firms; Ewuraba for women in business.",
              s=["sme"], lc="everyday", neo=[0, "Visa business debit."], src=[["GCB: SME solution", SMEPAGE]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate, SOE & government", "blurb": "Ghana's largest lender.", "div": "gcb", "rev": "corporate", "products": [
            P("corporate", "Corporate & state-enterprise banking", "Lending to corporates, state-owned enterprises and COCOBOD, where GCB is the market's largest lender; net loans grew 56.8% in 2025 and 35.4% in the first half of 2026.",
              s=["corp"], lc="borrow", neo=[1, "Corporate Mastercard."], src=[["IC Securities: FY2025, 27 Mar 2026", FY25], ["Daily Graphic: H1 2026, 29 Jul 2026", H1]]),
        ]},
        {"id": "4.4", "ic": "globe", "name": "Trade & Afro-Asia", "blurb": "Ghana–China corridor.", "div": "afro", "rev": "treasury", "products": [
            P("trade", "Trade finance & treasury", "Letters of credit, bills for collection, GCB Express and FX; trading income GH¢701.9 million in H1 2026.",
              s=["trade", "corp"], lc="move", neo=[0, ""], src=[["Daily Graphic: H1 2026, 29 Jul 2026", H1], ["GCB: tariff guide 2025", TARIFF]]),
            P("afroasia", "Afro-Asia desk", "Links Ghanaian exporters and importers with Chinese buyers and suppliers (Ghana–China trade above $14.1 billion); GCB was named to Ghana's planning committee for CIIE 2026 in August 2026.",
              s=["trade"], lc="beyond", st="new", neo=[0, ""], src=[["GNA: Ghana–China ties, Mar 2026", CHINA], ["Ghanaian Times: CIIE role, Aug 2026", CIIE]]),
        ]},
        {"id": "4.5", "ic": "chart-candlestick", "name": "Investment banking", "blurb": "GCB Capital.", "div": "capital", "rev": "treasury", "products": [
            P("capital", "GCB Capital", "Capital raising, advisory and long-term assets for corporates, institutions and government; runs the Golden Eagle unit trust.",
              s=["corp", "hnw"], lc="grow", neo=[0, ""], src=[["GCB: about us", ABOUT], ["Wikipedia: GCB Bank", WIKI]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: 184 branches and Ghana's largest ATM network, an award-winning app with over a million active users, and G-Money agents and online portals.",
    "tiles": [
        {"id": "5.1", "ic": "building", "name": "Branches & ATMs", "blurb": "184 branches, 340+ ATMs.", "div": "gcb", "rev": "retail", "products": [
            P("branches", "Branches & ATMs", "184 branches and more than 340 ATMs, which GCB calls Ghana's largest ATM network; cards issued instantly in branch since 2020.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["GCB: homepage", HOME], ["GCB: mobile & ATM banking", MOBILE], ["GNA: instant issuance, Jul 2020", INSTANT]]),
        ]},
        {"id": "5.2", "ic": "smartphone", "name": "Mobile & internet banking", "blurb": "1m+ active app users.", "div": "personal", "rev": "retail", "products": [
            P("app", "GCB mobile app", "Over 1 million active users; transfers, bills, mobile money, investments and instant credit; Mobile Banking App of the Year at the Ghana FinTech Awards, March 2026.",
              s=["con"], lc="everyday", st="new", o="P", at="Modefin", neo=[0, ""],
              mc="No tokenised wallet or Click to Pay is visible.",
              src=[["Citi Newsroom: FinTech awards, Mar 2026", FINTECH], ["Citi Newsroom: Modefin award, Dec 2023", MODEFIN]]),
            P("ebank", "Internet banking & USSD", "Internet banking for individuals and corporates, SMS alerts and USSD services.",
              s=["con", "corp", "dia"], lc="everyday", neo=[0, ""], src=[["GCB: mobile & ATM banking", MOBILE]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Agents & portals", "blurb": "G-Money agents, card portals.", "div": "gmoney", "rev": "retail", "products": [
            P("agents", "G-Money agents & merchants", "Cash-in and cash-out through G-Money agents and merchants, in a market with 491,057 active mobile-money agents in 2025.",
              s=["wal"], lc="everyday", neo=[0, ""], src=[["G-Money: what we do", GMFSDO], ["Ghanaian Times: Bank of Ghana oversight report, Oct 2026", BOGMOMO]]),
            P("portals", "Online portals", "An account-opening portal and separate prepaid and corporate card portals.",
              s=["corp", "con"], lc="open", neo=[1, "Corporate Mastercard and Visa prepaid ⚠."], src=[["GCB: homepage", HOME]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at GCB", "blurb": "First in Ghana, now one of two.", "products": [
        P("mcatgcb", "Mastercard at GCB", "GCB became Ghana's first Mastercard principal in October 2008 and still issues Mastercard debit from Standard to Platinum and the Corporate Mastercard, and its MD joined Mastercard's Africa Leadership Council in March 2026. Visa holds the top tier (Signature and Infinite, December 2024), business debit and prepaid, and a June 2026 data and marketing collaboration. ReadyCash runs on gh-link.",
          s=["con"], div="gcb", rev="retail", mc="The relationship this map is drawn for.",
          src=[["The Paypers: Mastercard launch, Oct 2008", MC2008], ["Citi Newsroom: Mastercard council, Mar 2026", MALC], ["Citi Newsroom: GCB and Visa, Jun 2026", VISA26]]),
    ]},
    {"id": "pillar-market", "name": "Ghana's payments", "blurb": "Mobile money and GhIPSS.", "products": [
        P("market", "The Ghanaian market", "Mobile money moved GH¢4.54 trillion in 2025 for 26.7 million active users; GhIPSS Instant Pay GH¢712 billion; gh-link card switching fell. GhIPSS processes Visa's domestic transactions under a January 2024 deal. Mastercard opened an Accra office in January 2025 and put a card on every MTN MoMo wallet in 2024.",
          s=["con"], div="gcb", rev="retail",
          src=[["Ghanaian Times: Bank of Ghana oversight report, Oct 2026", BOGMOMO], ["GhIPSS: industry performance 2025", GHIPSS], ["Ghanaian Times: GhIPSS and Visa, Jan 2024", GHIPSSVISA], ["TechAfrica News: Mastercard Accra office, Jan 2025", MCOFFICE], ["TechAfrica News: Mastercard and MTN, Feb 2024", MCMTN]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
