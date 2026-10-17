"""Commercial Bank of Ceylon's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the H1 2026 results release (13 August 2026), the
FY2025 results release (26 February 2026) and the 2025 integrated annual report. ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://www.combank.lk/news/news-events/combank-group-takes-deposits-past-rs-3-tn-threshold-in-solid-6-month-performance"
DMH1 = "https://www.dailymirror.lk/business/ComBank-posts-8-profit-growth-as-provisions-weigh-on-strong-income/215-348103"
FY25 = "https://www.combank.lk/news/news-events/combank-takes-lending-to-new-levels-in-mission-focused-2025"
AR = "https://combank2025.annualreports.lk/integrated_report/who_we_are_and_what_we_stand_for/about_commercial_bank_of_ceylon_plc.html"
SNAP = "https://combank2025.annualreports.lk/integrated_report/who_we_are_and_what_we_stand_for/snapshot_of_the_bank.html"
NFH = "https://combank2025.annualreports.lk/integrated_report/who_we_are_and_what_we_stand_for/non_financial_highlights.html"
GROUP = "https://combank2025.annualreports.lk/integrated_report/who_we_are_and_what_we_stand_for/group_structure.html"
IR = "https://combank2025.annualreports.lk/integrated_report/investor_information_and_performance_trends/investor_relations.html"
STRAT = "https://combank2025.annualreports.lk/integrated_report/strategic_priorities_and_value_creation.html"
MDR = "https://combank2025.annualreports.lk/integrated_report/leadership_and_their_perspectives/managing_director_chief_executive_officer_s_review.html"
MGMT = "https://combank2025.annualreports.lk/integrated_report/leadership_and_their_perspectives/corporate_management_and_profiles.html"
MODEL = "https://combank2025.annualreports.lk/integrated_report/our_business_model_for_sustainable_value_creation/our_business_model.html"
SUBS = "https://combank2025.annualreports.lk/integrated_report/analysis_of_financial_performance/performance_of_bangladesh_operations_and_subsidiaries.html"
CHAIR = "https://www.combank.lk/news/news-events/combank-appoints-new-chairman-and-deputy-chairman"
COO = "https://www.combank.lk/news/news-events/commercial-bank-appoints-hasrath-munasinghe-as-executive-directorchief-operating-officer"
AXON = "https://www.combank.lk/news/news-events/combank-showcases-global-first-in-digital-banking-architecture-with-axonect-at-dtw-ignite-2026"
DIFC = "https://www.combank.lk/news/news-events/combank-first-sl-bank-to-open-representative-office-in-dubai-international-financial-centre-difc"
IFC = "https://www.combank.lk/news/news-events/combank-to-boost-wsme-agri-sme-financing-with-ifcs-us-60mn-risk-sharing-facility"
MCAP = "https://www.combank.lk/news/news-events/combank-becomes-the-first-sri-lankan-bank-to-cross-us-1-bn-in-market-cap"
DEBIT = "https://www.combank.lk/personal-banking/cards/debit-cards"
CREDIT = "https://www.combank.lk/personal-banking/cards/credit-cards"
PLAT = "https://www.combank.lk/personal-banking/cards/platinum-cards"
WORLD = "https://www.combank.lk/personal-banking/cards/world-mastercard-card"
INFINITE = "https://www.combank.lk/personal-banking/cards/visa-infinite-card"
ANAGI = "https://www.combank.lk/personal-banking/cards/anagi-credit-card"
AFFINITY = "https://www.combank.lk/personal-banking/cards/affinity-credit-cards"
NEGC = "https://www.combank.lk/personal-banking/cards/negc-privilege-credit-card"
CORP = "https://www.combank.lk/personal-banking/cards/corporate-credit-card"
FUEL = "https://www.combank.lk/personal-banking/cards/corporate-fuel-credit-card"
SMECARD = "https://www.combank.lk/personal-banking/cards/sme-credit-cards"
BIZ = "https://www.combank.lk/personal-banking/cards/biz-club-business-debit-card"
TRAVEL = "https://www.combank.lk/personal-banking/cards/travel-card"
PREPAID = "https://www.combank.lk/personal-banking/cards/prepaid-cards"
REWARDS = "https://www.combank.lk/personal-banking/cards/max-loyalty-rewards"
EPP = "https://www.combank.lk/personal-banking/cards/easy-payment-plans"
ELITE = "https://www.combank.lk/news/news-events/combank-takes-elite-customers-to-new-heights-in-exclusivity-with-visa-signature-elite-debit-card"
VISACORP = "https://www.combank.lk/news/news-events/combank-and-visa-launch-corporate-credit-cards-in-sri-lanka"
VISAXB = "https://www.combank.lk/news/news-events/combank-wins-best-cross-border-salience-lmm-award-from-visa"
SPLENDOR = "https://www.combank.lk/news/news-events/combank-unionpay-launch-splendorplus-unlocking-superior-privileges-for-sri-lankan-travellers"
UPI3DS = "https://www.combank.lk/news/news-events/combank-pioneers-state-of-the-art-3ds-authentication-for-unionpay-cardholders"
LANKAPAY = "https://www.combank.lk/news/news-events/combank-launches-lankapay-cards-in-sri-lanka"
LP3DS = "https://www.combank.lk/news/news-events/combank-first-to-enable-3d-secure-authentication-for-lankapayjcb-cards"
LPDRIVE = "https://www.combank.lk/news/news-events/combank-unveils-island-wide-drive-to-boost-lankapay-jcb-debit-cards-adoption"
GPAYVISA = "https://www.combank.lk/news/news-events/visa-and-commercial-bank-are-pioneering-the-next-evolution-in-digital-payments-in-sri-lanka-by-enabling-google-pay-for-their-cardholders"
GPAYMC = "https://www.combank.lk/news/news-events/combank-makes-history-as-first-bank-in-sri-lanka-to-enable-google-pay-for-mastercard-cardholders"
IDEMIA = "https://www.idemia.com/news/idemia-secure-transactions-and-commercial-bank-ceylon-launch-google-pay-sri-lanka-2026-02-17/"
ABANS = "https://www.combank.lk/news/news-events/combank-and-abans-forge-landmark-partnership-with-pos-and-digital-payments-rollout"
PAX = "https://www.combank.lk/news/news-events/combank-cba-unveil-pax-e700-all-in-one-smart-pos-to-empower-smes-with-next-gen-payment-solutions"
SOUNDBOX = "https://www.combank.lk/news/news-events/combank-partners-payable-to-introduce-soundbox-for-small-business-digital-payments"
TAP = "https://www.combank.lk/services/tap-to-phone-facility-1"
DCC = "https://www.combank.lk/news/news-events/combank-and-mastercard-launch-sri-lankas-first-dynamic-currency-conversion-for-online-payments"
BANCSTAC = "https://www.combank.lk/news/news-events/combank-teams-up-with-bancstac-to-strengthen-digital-payment-infrastructure"
SIMPLE = "https://www.combank.lk/services/simple-pay"
QR = "https://www.combank.lk/services/qr-payments"
QJUST = "https://www.combank.lk/news/news-events/q-payment-app-opens-up-for-multi-bank-customers-via-justpay"
QJAFFNA = "https://www.combank.lk/news/news-events/combank-takes-q-digital-payments-drive-to-jaffna-ahead-of-nallur-festival"
QTRINCO = "https://www.combank.lk/news/news-events/commercial-bank-advances-national-cashless-payments-drive-at-cbsl-forum-in-trincomalee"
PAYMASTER = "https://www.combank.lk/services/paymaster-1"
GIG = "https://www.combank.lk/news/news-events/commercial-bank-launches-combank-gig-to-power-sri-lankas-growing-digital-workforce"
PAYPAL = "https://www.combank.lk/services/paypal"
GOLDNET = "https://www.combank.lk/news/news-events/combank-celebrates-16-years-of-providing-card-payment-solutions-via-goldnet"
ONBOARD = "https://www.combank.lk/news/news-events/combank-enables-seamless-account-opening-through-enhanced-self-onboarding-platform"
AISME = "https://www.combank.lk/news/news-events/combank-launches-sri-lankas-first-ai-powered-sme-credit-underwriting-solution"
MILES = "https://www.combank.lk/news/news-events/combanks-max-loyalty-rewards-soars-to-new-heights-with-airline-miles-option"
PRESTIGE = "https://www.combank.lk/news/news-events/combank-unveils-prestige-banking-to-empower-clients-to-craft-their-legacy-for-growth"
SMELEAD = "https://www.combank.lk/news/news-events/combank-leads-sri-lankas-sme-lending-for-fifth-consecutive-year"
TRADELINK = "https://www.combank.lk/news/news-events/combank-launches-tradelink-a-digital-platform-for-importers-and-exporters"
FLASH = "https://www.combank.lk/services/flash-digital-bank-account"
ATMS = "https://www.combank.lk/news/news-events/commercial-bank-expands-self-service-banking-network-to-support-sri-lankas-tourism-sector"
SHAKTHI = "https://www.combank.lk/news/news-events/commercial-bank-scales-combank-shakthi-agency-banking-network-to-26-strategic-locations"
RUGBY = "https://www.combank.lk/news/news-events/combank-mastercard-customer-wins-visit-for-2-to-rugby-world-cup-semi-final-in-paris"
FIFA = "https://www.combank.lk/news/news-events/combank-visa-cardholders-rewarded-with-unforgettable-fifa-world-cup-final-journey"
MCLEAD = "https://www.dailymirror.lk/print/business-news/Mastercard-announces-leadership-changes/273-342677"
CBSL = "https://www.cbsl.gov.lk/sites/default/files/Payments_Bulletin_1Q2026_e.pdf"
NQR = "https://english.newsfirst.lk/2026/04/06/sri-lanka-pushes-cash%E2%80%91lite-economy-with-lankaqr-launch"
SEYLAN = "https://www.ft.lk/financial-services/Seylan-Bank-enables-Google-Pay-for-Mastercard-cardholders/42-793821"
BOCTAP = "https://www.ft.lk/financial-services/BOC-marks-new-era-in-digital-payments-with-BOC-Flex-Tap-Pay/42-794683"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · systems", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Sri Lanka's largest private bank, with Rs 3.74 trillion of assets and a 20% ROE, a widely held register with IFC near 14%, a Euronet card switch and IDEMIA tokens, and a strategy of digital, SME and overseas growth.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & owners", "blurb": "Rs 3.74tn assets, ROE 20%.", "div": "group", "rev": "treasury", "products": [
            P("balance", "Balance sheet & earnings", "Group assets of Rs 3.74 trillion, deposits of Rs 3.02 trillion and gross loans of Rs 2.36 trillion at 30 June 2026; H1 2026 profit after tax Rs 35.4 billion (+13.7%), ROE 20.3%, Tier 1 13.2%. In 2025 the bank earned Rs 58.5 billion after tax and held about 13% of Sri Lanka's bank deposits and 15% of loans.",
              s=["con"], neo=[0, ""], src=[["H1 2026 results, Aug 2026", H1], ["Daily Mirror: Q2 2026, Aug 2026", DMH1], ["2025 results, Feb 2026", FY25], ["Annual report 2025: business model", MODEL]]),
            P("owners", "Ownership, listing & ratings", "Listed on the Colombo Stock Exchange with a 99.8% free float; the largest holders are two private investors and DFCC Bank (about 9.6–9.9% each), the Employees' Provident Fund (7.3%) and IFC funds (about 14% together). Market cap passed USD 1 billion in August 2025, the first Sri Lankan bank to do so; Fitch rates it AA-(lka). The only private-sector higher-tier D-SIB.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025: investor relations", IR], ["ComBank: USD 1bn market cap, Aug 2025", MCAP], ["Annual report 2025: snapshot", SNAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Muhseen and Manatunge.", "div": "bank", "rev": "treasury", "products": [
            P("leadership", "Board & corporate management", "Chairman Sharhan Muhseen (since April 2024, an ex-Credit Suisse investment banker), MD/CEO Sanath Manatunge, COO Hasrath Munasinghe (since 27 April 2026, formerly in charge of cards and retail), CFO Prasanna Indrajith, CIO Sumudu Gunawardhana and Chief Digital Officer Randil Boteju; 5,726 staff.",
              s=["corp"], st="new", neo=[0, ""], src=[["ComBank: new Chairman, Apr 2024", CHAIR], ["ComBank: COO appointment, Feb 2026", COO], ["Annual report 2025: corporate management", MGMT]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology", "blurb": "Euronet switch, Axonect APIs.", "div": "orysys", "rev": "nbfi", "products": [
            P("tech", "Core, switch & architecture", "A Euronet Worldwide card switch, IDEMIA as card supplier and token partner for 15 years, an open-digital-architecture and API layer from Axonect (shown August 2026), the in-house IT company Orysys, and a security operations centre adding AI-driven threat containment in 2026.",
              s=["corp"], neo=[0, "Euronet, IDEMIA, Axonect."], src=[["ComBank: Axonect at DTW Ignite, Aug 2026", AXON], ["IDEMIA: Google Pay with ComBank, Feb 2026", IDEMIA], ["Annual report 2025: MD/CEO review", MDR]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & moves", "blurb": "Digital, SME, overseas.", "div": "group", "rev": "treasury", "products": [
            P("strategy", "Strategy", "Five imperatives: market leadership, pervasive digital, customer centricity, talent and ESG. For cards: scale virtual cards, tokenisation, wallets and embedded finance, AI fraud detection, a lifestyle Q+ app, tap-on-phone and QR acceptance. A four-year retail transformation with McKinsey began in 2025.",
              s=["corp"], neo=[0, ""], mc="ComBank's own cards plan reads like a Mastercard services list: tokens, virtual cards, AI fraud and acceptance.",
              src=[["Annual report 2025: strategic priorities", STRAT], ["Annual report 2025: MD/CEO review", MDR]]),
            P("deals", "Deals & expansion", "DIFC representative office (licensed May 2025), a Rs 15 billion Tier II green bond (2025), a US$60 million IFC risk-sharing facility for women-led and agri SMEs (January 2026), a Port City Colombo branch (June 2026) and the sale of Equity Investments Lanka after year-end. No bank acquisitions since Bangladesh in 2003.",
              s=["corp", "sme"], st="new", o="P", at="IFC", neo=[0, ""], src=[["ComBank: DIFC, May 2025", DIFC], ["ComBank: IFC facility, Jan 2026", IFC], ["Annual report 2025: group structure", GROUP]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Ten ways money moves: debit and credit on four networks at once (Visa, Mastercard, UnionPay and LankaPay/JCB), Mastercard co-brands, Visa-led corporate cards, the national card scheme, Google Pay, the biggest acquiring business with Soundbox, an MPGS gateway now joined by Bancstac, Q+ on LANKAQR, and remittances.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit & prepaid", "blurb": "No. 1 in debit, four networks.", "div": "cards", "rev": "personal", "products": [
            P("debit", "Classic debit cards", "Shopping debit cards on Visa, Mastercard, UnionPay and LankaPay (JCB); ComBank says it is number one in Sri Lanka in debit card issuance and usage (2025). The split by network is not published ⚠.", short="Debit (four networks)",
              s=["con", "migr"], lc="everyday", o="B", at="Visa, Mastercard, UnionPay, LankaPay", neo=[1, "Visa, Mastercard, UnionPay and LankaPay; split not published ⚠."],
              src=[["ComBank: debit cards", DEBIT], ["Annual report 2025: strategic priorities", STRAT]]),
            P("elitedebit", "Visa Signature Elite debit", "The top debit tier for Elite (now Prestige) clients, launched February 2025 in place of Gold debit, with 1,000+ airport lounges and Max Rewards at one point per Rs 400.",
              s=["prem"], lc="everyday", ay="Feb 2025", o="P", at="Visa", neo=[0, "Visa."], src=[["ComBank: Visa Signature Elite debit, Feb 2025", ELITE]]),
            P("bizdebit", "BIZ Club business debit", "A Visa Business debit card that doubles as membership of ComBank's SME club, with discounts and Max Rewards.",
              s=["sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["ComBank: BIZ Club debit", BIZ]]),
            P("prepaid", "Prepaid & travel cards", "Pre-paid spend and web cards, a pre-paid fuel card and a Visa Travel Card billed in the traveller's chosen currency.",
              s=["con"], lc="move", o="P", at="Visa", neo=[0, "Visa."], src=[["ComBank: travel card", TRAVEL], ["ComBank: prepaid cards", PREPAID]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Visa on top, UnionPay rising.", "div": "cards", "rev": "personal", "products": [
            P("credit", "Gold, Silver & Platinum credit", "Credit cards on Visa, Mastercard, UnionPay and LankaPay (JCB); ComBank claims a leading position in a market of about 2.23 million credit cards (CBSL, March 2026). Network split not published ⚠.", short="Credit (four networks)",
              s=["con"], lc="borrow", o="B", at="Visa, Mastercard, UnionPay, LankaPay", neo=[1, "Visa, Mastercard, UnionPay and LankaPay ⚠ split."],
              src=[["ComBank: credit cards", CREDIT], ["ComBank: Platinum cards", PLAT], ["CBSL: Payments Bulletin Q1 2026", CBSL]]),
            P("premium", "Visa Infinite & Visa Signature", "The top consumer credit tiers, with Visa concierge, luxury hotels and lounges; Visa ran a FIFA World Cup Final spend campaign for Platinum, Signature and Infinite holders (March–May 2026).",
              s=["prem"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["ComBank: Visa Infinite", INFINITE], ["ComBank: Visa FIFA campaign, Jun 2026", FIFA]]),
            P("worldmc", "World Mastercard", "Mastercard's premium tier for incomes above Rs 375,000 a month, with lounges, hotel offers, concierge and travel cover; Priceless trips to the Rugby World Cup in 2019 and 2023.", short="World Mastercard",
              s=["prem"], lc="borrow", o="P", at="Mastercard", neo=[2, "World Mastercard."],
              mc="Mastercard's one premium card here sits beside two Visa tiers and two UnionPay tiers.",
              src=[["ComBank: World Mastercard", WORLD], ["ComBank: Rugby World Cup promotion, Sep 2023", RUGBY]]),
            P("unionpay", "UnionPay Asia Prestige & SplendorPlus", "Sri Lanka's first UnionPay issuer: Asia Prestige Diamond and Platinum, the first in the world with LoungeKey access (September 2025), SplendorPlus for China travel (January 2026, signed with China UnionPay's chairman) and UnionPay 3DS 2.x (May 2026).",
              s=["prem"], lc="borrow", st="new", ay="Jan 2026", o="P", at="UnionPay International", neo=[0, "UnionPay."], src=[["ComBank: SplendorPlus, Jan 2026", SPLENDOR], ["ComBank: UnionPay 3DS, May 2026", UPI3DS]]),
        ]},
        {"id": "2.3", "ic": "badge-check", "name": "Co-brand & affinity", "blurb": "All on Mastercard.", "div": "cards", "rev": "personal", "products": [
            P("cobrand", "Anagi, affinity, NEGC & Mobitel cards", "The co-brand book is Mastercard: the Anagi card for women (Gold and Platinum), school old-boys' affinity cards, the Nuwara Eliya Golf Club Privilege World Mastercard and the Mobitel Data+ card.", short="Co-brands (Mastercard)",
              s=["con", "prem"], lc="borrow", o="P", at="Mastercard", neo=[2, "All Mastercard."],
              src=[["ComBank: Anagi card", ANAGI], ["ComBank: affinity cards", AFFINITY], ["ComBank: NEGC card", NEGC]]),
        ]},
        {"id": "2.4", "ic": "briefcase-business", "name": "Commercial cards", "blurb": "Visa corporate, Mastercard fuel.", "div": "cards", "rev": "corporate", "products": [
            P("corpcard", "Corporate credit cards", "Corporate cards on Mastercard and Visa; Visa Signature and Visa Platinum Corporate launched February 2024, and Visa gave ComBank awards for the launch (April 2024) and for cross-border commercial spend (May 2025).",
              s=["corp"], lc="move", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard; Visa leads the new tiers."],
              mc="Visa owns the commercial-card story at Sri Lanka's biggest trade bank.",
              src=[["ComBank: corporate card", CORP], ["ComBank: Visa corporate cards, Feb 2024", VISACORP], ["ComBank: Visa cross-border award, May 2025", VISAXB]]),
            P("fuelcard", "Corporate fuel credit card", "A Mastercard Corporate card restricted to fuel, for company fleets and fuel allowances, with SMS alerts on every transaction.",
              s=["corp", "sme"], lc="move", o="P", at="Mastercard", neo=[2, "Mastercard Corporate."], src=[["ComBank: corporate fuel card", FUEL]]),
            P("smecard", "SME credit cards", "BIZ Club and Business credit cards for small firms; the page names Mastercard ⚠ for the international benefits.",
              s=["sme"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard ⚠."], src=[["ComBank: SME credit cards", SMECARD]]),
        ]},
        {"id": "2.5", "ic": "flag", "name": "National card scheme", "blurb": "LankaPay with JCB.", "div": "cards", "rev": "personal", "products": [
            P("lankapay", "LankaPay JCB cards", "First bank to issue LankaPay credit cards (March 2023): domestic payments routed locally to save foreign exchange, overseas on JCB. First to add 3DS (March 2026) and waiving the first-year fee on LankaPay JCB debit from May to December 2026.", short="LankaPay JCB",
              s=["con"], lc="everyday", st="new", ay="Mar 2023", o="P", at="LankaPay, JCB", neo=[0, "LankaPay and JCB."],
              mc="The state-backed domestic scheme ComBank is pushing hardest in 2026.",
              src=[["ComBank: LankaPay cards, Mar 2023", LANKAPAY], ["ComBank: LankaPay JCB 3DS, Mar 2026", LP3DS], ["ComBank: LankaPay debit drive, Apr 2026", LPDRIVE]]),
        ]},
        {"id": "2.6", "ic": "smartphone", "name": "Wallets & tokens", "blurb": "Google Pay first, Visa then Mastercard.", "div": "cards", "rev": "personal", "products": [
            P("gpayvisa", "Google Pay for Visa cards", "Sri Lanka's first Google Pay launch, 18 November 2025, with Visa Token Service through IDEMIA, for Visa debit and credit holders.",
              s=["con"], lc="everyday", st="new", ay="Nov 2025", o="P", at="Visa, Google, IDEMIA", neo=[0, "Visa."], src=[["ComBank: Google Pay with Visa, Nov 2025", GPAYVISA], ["IDEMIA: Google Pay with ComBank, Feb 2026", IDEMIA]]),
            P("gpaymc", "Google Pay for Mastercard cards", "Mastercard debit and credit cards in Google Pay from 9 February 2026, the first in Sri Lanka, with tokens replacing card numbers; Seylan, Sampath and BOC followed with Mastercard wallets by July 2026.", short="Google Pay (Mastercard)",
              s=["con"], lc="everyday", st="new", ay="Feb 2026", o="P", at="Mastercard, Google", neo=[2, "Mastercard tokens."],
              mc="Mastercard tokens are live; card-on-file and Click to Pay are the next step.",
              src=[["ComBank: Google Pay with Mastercard, Feb 2026", GPAYMC], ["Daily FT: Seylan Google Pay, Jun 2026", SEYLAN], ["Daily FT: BOC Flex Tap & Pay, Jul 2026", BOCTAP]]),
        ]},
        {"id": "2.7", "ic": "store", "name": "Merchant acquiring", "blurb": "POS +24%, Soundbox.", "div": "cards", "rev": "personal", "products": [
            P("pos", "POS acquiring", "A leading acquirer accepting Visa, Mastercard, UnionPay, JCB, LankaPay, LANKAQR, Alipay and WeChat Pay; POS volumes up 24% in 2025; DCC at the till since 2019; PAX E700 smart POS with CBA (October 2025).",
              s=["merch", "sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["Annual report 2025: strategic priorities", STRAT], ["ComBank: PAX E700, Oct 2025", PAX]]),
            P("abans", "Abans retail rollout", "2,500 EMV and QR terminals across Abans' 400+ outlets, tied into its ERP, with Easy Payment Plans (November 2025).",
              s=["merch"], lc="move", st="new", ay="Nov 2025", o="P", at="Abans", neo=[1, "All schemes."], src=[["ComBank: Abans, Nov 2025", ABANS]]),
            P("soundbox", "Soundbox", "An audio-confirming card and QR device for micro merchants, powered by Mastercard and delivered with Payable, launched 15 October 2026.", short="Soundbox (Mastercard)",
              s=["merch"], lc="move", st="new", ay="Oct 2026", o="P", at="Mastercard, Payable", neo=[3, "Powered by Mastercard; accepts all networks."],
              mc="The newest joint product: Mastercard's way into cash-heavy micro merchants.",
              src=[["ComBank: Soundbox, Oct 2026", SOUNDBOX]]),
            P("taptophone", "Tap to Phone", "Turns an Android phone into a terminal for contactless Mastercard and Visa cards.",
              s=["merch"], lc="move", o="B", neo=[1, "Mastercard and Visa."], src=[["ComBank: Tap to Phone", TAP]]),
        ]},
        {"id": "2.8", "ic": "code-xml", "name": "E-commerce gateway", "blurb": "MPGS since 2007, now Bancstac.", "div": "cards", "rev": "personal", "products": [
            P("ipg", "MPGS gateway & online DCC", "First Sri Lankan bank on Mastercard Payment Gateway Services (2007); added Sri Lanka's first online DCC on MPGS with FEXCO and Euronet (30 December 2025) for travel and hotel merchants; IPG volumes up 27% in 2025.", short="MPGS & DCC",
              s=["merch"], lc="move", ay="2007", o="P", at="Mastercard, FEXCO, Euronet", neo=[3, "Mastercard Payment Gateway Services."],
              mc="Mastercard's own gateway, with a new rival in the same bank.",
              src=[["ComBank: MPGS DCC, Dec 2025", DCC]]),
            P("bancstac", "Bancstac gateway technology", "A long-term agreement (17 April 2026) for a bank-controlled IPG on Bancstac technology; supports Visa, Mastercard, UnionPay and LankaQR, with JCB and the national scheme to come; authorisation stays on ComBank's Euronet switch. ⚠ Whether it replaces MPGS is not stated.",
              s=["merch"], lc="move", st="flux", ay="Apr 2026", o="P", at="Bancstac", neo=[0, "Bancstac; all networks ⚠."],
              src=[["ComBank: Bancstac, Apr 2026", BANCSTAC]]),
            P("simplepay", "Simple Pay", "An e-invoice and checkout service for SMEs selling online.",
              s=["sme"], lc="move", o="B", neo=[None, "Gateway not stated."], src=[["ComBank: Simple Pay", SIMPLE]]),
        ]},
        {"id": "2.9", "ic": "zap", "name": "QR & instant payments", "blurb": "Q+ is No. 1 on LANKAQR.", "div": "cards", "rev": "personal", "products": [
            P("qplus", "Q+ Payment App & ComBank QR", "The first LANKAQR-certified app, open to any bank's customers through JustPay since October 2024; reads LANKAQR, Visa QR, Mastercard QR, UnionPay QR, UPI QR and Alipay QR; number one on LANKAQR, with usage up 67% in 2025 and CBSL campaigns in Trincomalee and Jaffna (August–September 2026).", short="Q+ (LANKAQR)",
              s=["con", "merch"], lc="move", o="B", neo=[1, "LANKAQR first; Mastercard QR one of six."],
              src=[["ComBank: Q+ on JustPay, Oct 2024", QJUST], ["ComBank: QR payments", QR], ["ComBank: Q+ in Jaffna, Sep 2026", QJAFFNA], ["ComBank: CBSL forum Trincomalee, Aug 2026", QTRINCO]]),
            P("cefts", "CEFTS, JustPay & Paymaster", "Real-time transfers on LankaPay's CEFTS (Rs 23.1 trillion nationally in 2025), JustPay and GovPay through ComBank Digital, and Paymaster bulk salary and supplier payments.",
              s=["con", "corp"], lc="move", o="P", at="LankaPay", neo=[0, "LankaPay rails."], src=[["CBSL: Payments Bulletin Q1 2026", CBSL], ["ComBank: Paymaster", PAYMASTER]]),
        ]},
        {"id": "2.10", "ic": "send", "name": "Remittances & FX", "blurb": "Inflows, PayPal, GIG+.", "div": "bank", "rev": "intl", "products": [
            P("remit", "Inward remittances", "A large inward remittance franchise through exchange houses in the Gulf (20 years in Qatar and Kuwait) with RemitPlus prize draws and a Remittance Card, at a time of record USD 8 billion+ worker remittances to Sri Lanka in 2025.",
              s=["migr"], lc="move", o="P", neo=[0, "Exchange houses and correspondents."],
              mc="No Mastercard Move link found; remittance-to-card is open ground.",
              src=[["Annual report 2025: strategic priorities", STRAT]]),
            P("gig", "ComBank GIG+ & PayPal", "Accounts in rupees, dollars, euros, pounds and Australian dollars for freelancers and creators (June 2026), with instant PayPal withdrawals into ComBank accounts.",
              s=["migr"], lc="grow", st="new", ay="Jun 2026", o="P", at="PayPal", neo=[0, "PayPal."], src=[["ComBank: GIG+, Jun 2026", GIG], ["ComBank: PayPal", PAYPAL]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card and account: 3DS on every brand and video onboarding, AI underwriting with BCG, Max Rewards points and instalments, and Goldnet, which processes cards for eight other institutions.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud, 3DS & identity", "blurb": "3DS on every brand.", "div": "cards", "rev": "personal", "products": [
            P("threeds", "3DS & fraud monitoring", "First in Sri Lanka with 3DS on the global brands; its own ACS extended to UnionPay 3DS 2.x (May 2026) and CardinalCommerce for LankaPay/JCB (March 2026); fraud monitoring tightened in 2025, with AI fraud detection planned. No Mastercard fraud tool is named publicly ⚠.",
              s=["con"], lc="everyday", st="new", o="B", neo=[1, "3DS for all brands; no Mastercard fraud tool named ⚠."],
              mc="AI fraud detection is on the 2026 list with no vendor named.",
              src=[["ComBank: UnionPay 3DS, May 2026", UPI3DS], ["ComBank: LankaPay JCB 3DS, Mar 2026", LP3DS], ["Annual report 2025: strategic priorities", STRAT]]),
            P("onboarding", "Self-onboarding", "New customers, including Sri Lankans abroad, open accounts with real-time video identity checks and automated compliance screening (upgraded May 2026).",
              s=["con", "migr"], lc="open", st="new", ay="May 2026", o="B", neo=[0, ""], src=[["ComBank: self-onboarding, May 2026", ONBOARD]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data & AI", "blurb": "AI underwriting with BCG.", "div": "bank", "rev": "personal", "products": [
            P("ai", "AI credit underwriting", "Sri Lanka's first AI SME underwriting (July 2025, built with BCG) and AI models for personal loans, to be extended across all retail and SME lending.",
              s=["sme", "con"], lc="borrow", st="new", ay="Jul 2025", o="P", at="BCG", neo=[0, ""], src=[["ComBank: AI SME underwriting, Jul 2025", AISME], ["Annual report 2025: strategic priorities", STRAT]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & instalments", "blurb": "Max Rewards, airline miles.", "div": "cards", "rev": "personal", "products": [
            P("rewards", "Max Loyalty Rewards & COMDEALS", "Points on card spend and, since August 2024, on ComBank Digital transactions (one point = Rs 1); convertible to SriLankan FlySmiLes and other airline miles since June 2026; COMDEALS discounts of up to 70% at festivals.",
              s=["con", "prem"], lc="grow", st="new", o="B", neo=[0, "ComBank's own."],
              mc="Card-linked offers could feed Max Rewards and COMDEALS.",
              src=[["ComBank: Max Rewards", REWARDS], ["ComBank: airline miles, Jun 2026", MILES]]),
            P("epp", "Easy Payment Plans", "Instalments of 3 to 36 months on credit cards at registered merchants, also built into the Abans rollout.",
              s=["con"], lc="borrow", o="B", neo=[0, "ComBank's own instalments."], src=[["ComBank: Easy Payment Plans", EPP], ["ComBank: Abans, Nov 2025", ABANS]]),
        ]},
        {"id": "3.4", "ic": "network", "name": "Card processing", "blurb": "Goldnet for eight others.", "div": "cards", "rev": "personal", "products": [
            P("goldnet", "Goldnet", "Since 2007, card issuance, personalisation, ATM services and cardless cash for Dialog, SLT Mobitel, Amana Bank, Central Finance, Senkadagala Finance, Sanasa Development Bank, Citizens Development Bank and LOLC Finance, at 99.9% uptime.",
              s=["corp"], lc="beyond", ay="2007", o="B", neo=[1, "Processes every network."],
              mc="A channel to bring Mastercard services to smaller issuers.",
              src=[["ComBank: Goldnet 16 years, Feb 2024", GOLDNET]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: personal banking with the number one home-loan book and the new Prestige tier, the largest SME lending book, corporate and trade banking with a fifth of exports, and Bangladesh, the Maldives and Myanmar.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Personal & Prestige", "blurb": "37% of group profit.", "div": "bank", "rev": "personal", "products": [
            P("personal", "Personal banking", "Savings, home loans (number one), leasing and gold loans for more than 4 million customers; the segment earned Rs 34.4 billion before tax in 2025, 37% of the group.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["Annual report 2025: about", AR], ["Annual report 2025: strategic priorities", STRAT]]),
            P("prestige", "Prestige", "A three-tier private-banking programme for high-net-worth clients launched 7 October 2026, replacing the Elite brand, with wealth advice, lifestyle privileges and rewards.",
              s=["prem"], lc="grow", st="new", ay="Oct 2026", o="B", neo=[None, "Card mix not announced."],
              mc="World Mastercard and Priceless could anchor the Prestige card; Visa Signature Elite holds it today.",
              src=[["ComBank: Prestige, Oct 2026", PRESTIGE]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "SME banking", "blurb": "30% of SME lending.", "div": "bank", "rev": "personal", "products": [
            P("sme", "SME & development banking", "The largest SME lender for five years: Rs 330.9 billion lent in 2024, 30.3% of the 16 banks' total; BIZ Club, LEAP GlobalLinker and an IFC-backed facility for women-led and agri firms.",
              s=["sme"], lc="borrow", o="B", neo=[1, "BIZ Club debit on Visa; SME credit on Mastercard ⚠."], src=[["ComBank: SME lending lead, Dec 2025", SMELEAD], ["ComBank: IFC facility, Jan 2026", IFC]]),
        ]},
        {"id": "4.3", "ic": "factory", "name": "Corporate & trade", "blurb": "22% of exports.", "div": "bank", "rev": "corporate", "products": [
            P("trade", "Corporate, trade & treasury", "Corporate lending, syndications and treasury, and trade for 21.97% of Sri Lanka's exports and 15.91% of imports, run through the TradeLink platform (March 2025) and a dedicated corporate branch.",
              s=["corp"], lc="borrow", o="B", neo=[0, ""], src=[["ComBank: TradeLink, Mar 2025", TRADELINK], ["Annual report 2025: business model", MODEL]]),
        ]},
        {"id": "4.4", "ic": "earth", "name": "International", "blurb": "31% of group profit.", "div": "bd", "rev": "intl", "products": [
            P("intl", "Bangladesh, Maldives, Myanmar & DIFC", "CBC Bangladesh (20 units, AAA) earns most of the international profit; Commercial Bank of Maldives (55%) joined the Favara instant-payment system in 2025; CBC Myanmar Microfinance covers 13 townships. Overseas made 30.9% of group profit before tax in 2025.",
              s=["corp"], lc="beyond", o="A", neo=[None, "Card networks abroad not published."], src=[["Annual report 2025: Bangladesh and subsidiaries", SUBS], ["Annual report 2025: about", AR]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: ComBank Digital for 1.8 million and the Flash digital account, 272 branches and offsite ATMs in tourist towns, and agents and retail partners.",
    "tiles": [
        {"id": "5.1", "ic": "monitor", "name": "Digital apps", "blurb": "1.8m users, 56% digital.", "div": "bank", "rev": "personal", "products": [
            P("digital", "ComBank Digital", "Web plus iOS, Android and HarmonyOS apps: 1.8 million users, 56% digital penetration and 74 million transactions worth Rs 7.5 trillion in 2025.",
              s=["con", "sme", "corp"], lc="everyday", o="B", neo=[0, ""], src=[["Annual report 2025: MD/CEO review", MDR], ["Annual report 2025: non-financial highlights", NFH]]),
            P("flash", "Flash & Flash Fam", "A fully digital bank account with budgeting and investments, and a teen account (Flash Fam), in three languages.",
              s=["con"], lc="open", o="B", neo=[0, ""], src=[["ComBank: Flash", FLASH]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "272 branches.", "div": "bank", "rev": "personal", "products": [
            P("branches", "Branches, ATMs & CRMs", "272 branches, a Port City Colombo branch (June 2026) and new offsite ATMs and cash recyclers in Sigiriya, Ella, Weligama and other tourist towns (July 2026); about 1,000 machines ⚠.",
              s=["con", "migr"], lc="everyday", o="B", neo=[0, ""], src=[["Annual report 2025: about", AR], ["ComBank: tourist ATMs, Jul 2026", ATMS]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Agents & partners", "blurb": "Shakthi, Abans, Payable.", "div": "bank", "rev": "personal", "products": [
            P("shakthi", "ComBank Shakthi agency banking", "Trusted local agents with ComBank POS devices for deposits, withdrawals, transfers and bills: four in 2025, 26 by April 2026.",
              s=["con"], lc="everyday", st="new", ay="Apr 2026", o="P", neo=[0, ""], src=[["ComBank: Shakthi, Apr 2026", SHAKTHI]]),
            P("partners", "Retail & fintech partners", "Abans, Payable, CBA, Bancstac, PayPal, Dialog eZ Cash and Mobitel mCash connect customers and merchants to the bank.",
              s=["merch"], lc="beyond", o="P", neo=[1, "Payable's Soundbox runs on Mastercard."], src=[["ComBank: Abans, Nov 2025", ABANS], ["ComBank: Soundbox, Oct 2026", SOUNDBOX]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at ComBank", "blurb": "Co-brands, MPGS, Soundbox.", "products": [
        P("mcatcombank", "Mastercard at ComBank", "ComBank issues on four networks. Mastercard carries World Mastercard, every co-brand and affinity card and the corporate fuel card, ran ComBank's gateway since 2007 (online DCC from December 2025), joined Google Pay in February 2026 and powers Soundbox (October 2026). Visa holds the top consumer tiers, corporate cards and the first Google Pay launch; UnionPay and LankaPay/JCB are being pushed hard.",
          s=["con"], div="group", rev="personal", mc="The relationship this map is drawn for.",
          src=[["ComBank: MPGS DCC, Dec 2025", DCC], ["ComBank: Google Pay with Mastercard, Feb 2026", GPAYMC], ["ComBank: Soundbox, Oct 2026", SOUNDBOX], ["Daily Mirror: Mastercard leadership, Jun 2026", MCLEAD]]),
    ]},
    {"id": "pillar-market", "name": "Sri Lankan payments", "blurb": "Domestic rails rising.", "products": [
        P("market", "The Sri Lankan market", "About 2.23 million credit and 20.9 million debit cards, 144,046 POS terminals and 473,214 LANKAQR merchants (CBSL, March 2026); a national QR push launched by the President in April 2026 with fees waived on small LANKAQR payments ⚠; the LankaPay/JCB national card scheme; Google Pay live at several banks since 2025–26.",
          s=["con"], div="group", rev="personal", src=[["CBSL: Payments Bulletin Q1 2026", CBSL], ["News 1st: National QR launch, Apr 2026", NQR]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
