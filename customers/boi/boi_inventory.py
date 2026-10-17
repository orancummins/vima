"""Bank of Ireland's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the FY2025 results and Strategy 2028
(2 March 2026) and the H1 2026 results (31 July 2026). ``neo`` is the Mastercard lens: [depth, note],
where 3 = Mastercard's own product or network runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

from boi_foundation import FOUNDATION

IR = "https://investorrelations.bankofireland.com/app/uploads/"
FY25 = IR + "D15699-BOI-FY-2025-Annual-Results-Announcement-Web-Feb26-FINAL-np.pdf"
HY26 = IR + "D15941-BOI-Key-Messages-HY26-Jul26-NP.pdf"
HY26T = IR + "Interim-Results-2026-Announcement-and-QA-Transcript.pdf"
PR = "https://www.bankofireland.com/about-bank-of-ireland/press-releases/"
PB = "https://personalbanking.bankofireland.com/"
BB = "https://businessbanking.bankofireland.com/"
SWITCH2015 = "https://www.irishtimes.com/business/bank-of-ireland-exits-visa-deal-and-changes-to-mastercard-1.2346061"
Q2_26 = PR + "2026/bank-of-ireland-digital-banking-growth-in-q2/"
APP = PR + "2026/simpler-faster-mobile-app-on-way-for-bank-of-ireland-customers/"
FRAUD = PR + "2026/ai-technology-sees-customer-payment-fraud-losses-at-bank-of-ireland-drop-25/"
STRIPE = PR + "2026/bank-of-ireland-deepens-partnership-with-stripe/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Visa debit cards in the wallet, Mastercard credit cards since 2015, SEPA Instant and Zippay between accounts, card acceptance through Global Payments, FX and Global Markets, and the cash the Access to Cash Act now guarantees. The bank says it powers 40% of payments in the Irish economy.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit & wallets", "blurb": "Visa debit, 125 million taps a quarter.", "div": "ri", "rev": "ri", "products": [
            P("visadebit", "Visa Debit cards", "Personal and business debit cards on Visa since Laser was retired in 2010, including a child's card on Smart Start; €50 contactless limit.",
              s=["con", "young", "sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="The debit book carries most Irish card volume and is Visa at all three pillar banks; Visa renewed and widened its PTSB deal in June 2026, so the next Bank of Ireland debit renewal will be contested.",
              src=[["Bank of Ireland: Visa Debit terms", PB + "bank/current-accounts/visa-debit/terms-conditions/"], ["Bank of Ireland: new debit card, 2010", PR + "2010/bank-ireland-announces-new-debit-card-one-million-personal-customers-offering-worldwide-access-cash-payments/"]]),
            P("wallets", "Apple Pay & Google Pay", "Google Pay from August 2020 and Apple Pay later that year, delayed by the core-banking overhaul; 125.5 million contactless payments in the second quarter of 2026, up 13%.",
              s=["con", "young"], lc="move", o="P", at="Apple, Google", neo=[1, "Mastercard tokens on the credit cards; Visa on debit."],
              src=[["Silicon Republic: Google Pay at Bank of Ireland, 2020", "https://siliconrepublic.com/?p=890926"], ["Bank of Ireland: digital banking growth in Q2, Jul 2026", Q2_26]]),
            P("clicktopay", "Click to Pay", "Click to Pay is 'coming soon' for Visa debit cardholders, under a joint-controller arrangement with Visa; nothing is announced for the Mastercard credit cards.",
              s=["con"], lc="move", st="new", o="P", at="Visa", neo=[0, "Visa's, on debit only."],
              mc="Mastercard Click to Pay and payment passkeys on the credit book would match what Visa is bringing to debit.",
              src=[["Bank of Ireland: Click to Pay", "https://www.bankofireland.com/click-to-pay/"]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Mastercard since 2015.", "div": "ri", "rev": "ri", "products": [
            P("mcswitch", "Mastercard for all credit cards", "In September 2015 the bank ended its Visa credit relationship and named Mastercard 'strategic partner for all credit cards', moving about 40% of its cards by June 2016; industry sources said Mastercard offered better terms. The term was not disclosed and no renewal has been reported.", short="Mastercard credit since 2015",
              s=["con", "aff", "sme"], lc="borrow", o="P", at="Mastercard", ay="Sep 2015", neo=[3, "The agreement itself."],
              mc="Mastercard's foothold among Ireland's pillar banks: Bank of Ireland's credit book. Eleven years on, renewal is the first conversation.",
              src=[["Irish Times: Bank of Ireland exits Visa deal for Mastercard, Sep 2015", SWITCH2015]]),
            P("creditcards", "Classic, Platinum, Affinity & Student", "Classic (no annual fee), Platinum Advantage (lowest rate, travel insurance), Affinity cards for six universities, and a Student card; all Mastercard, with Mastercard Priceless.", short="Classic, Platinum, Affinity",
              s=["con", "aff", "young"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["Bank of Ireland: compare credit cards", PB + "borrow/credit-cards/compare-credit-cards/"], ["Bank of Ireland: Classic and Platinum agreement", "https://form.bankofireland.com/app/uploads/2017/11/New-Classic-Credit-Card-Terms-Conditions-effective-13-January-2018.pdf"]]),
            P("aercard", "Aer Credit Card", "Co-branded with Aer Lingus since January 2019, earning Avios through AerClub; €6.50 a month.",
              s=["aff", "con"], lc="borrow", o="P", at="Aer Lingus", ay="Jan 2019", neo=[2, "Mastercard (not stated on the product page)."],
              src=[["Aer Lingus: Aer Credit Card launch, Jan 2019", "https://mediacentre.aerlingus.com/pressrelease/details/108/10542"]]),
            P("bizcredit", "Business & Gold business credit cards", "Credit cards for small businesses and corporates, the Gold card with online expense management; the terms provide for card updates to be sent to Mastercard.",
              s=["sme", "corp"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard per the terms; one FAQ says Visa."],
              src=[["Bank of Ireland: business credit card terms, Feb 2024", BB + "app/uploads/Terms-and-Conditions-for-Business-Credit-Cards-effective-8-February-2024.pdf"]]),
        ]},
        {"id": "2.3", "ic": "zap", "name": "Instant & P2P", "blurb": "SEPA Instant and Zippay.", "div": "ri", "rev": "ri", "products": [
            P("sepainst", "SEPA Instant", "Free instant euro transfers: receiving since January 2025, sending from August–October 2025 ahead of the EU deadline; more than 11 million in the second quarter of 2026, peaking around 250,000 a day.",
              s=["con", "sme"], lc="move", st="new", ay="2025", neo=[0, "Account-to-account."],
              src=[["Bank of Ireland: digital banking growth in Q2, Jul 2026", Q2_26], ["FY2025 results deck", FY25]]),
            P("zippay", "Zippay", "Pay by mobile number inside the AIB, Bank of Ireland and PTSB apps, built by Nexi and live from 10 March 2026 for more than 5 million customers; it replaced Synch Payments, the banks' joint venture wound up in 2023 without launching.",
              s=["con", "young"], lc="move", st="new", ay="Mar 2026", o="P", at="Nexi, AIB, PTSB", neo=[0, "No card network role."],
              src=[["Nexi: mobile payments land in Ireland, Mar 2026", "https://www.nexigroup.com/en/media-relations/news/2026/03/nexi-mobile-payments-land-in-ireland/"], ["The Paypers: Irish banks halt Synch Payments", "https://thepaypers.com/fintech/news/irish-banks-halt-plans-for-synch-payments"]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Merchant acquiring", "blurb": "BOIPA, with Global Payments.", "div": "cc", "rev": "cc", "products": [
            P("boipa", "BOI Payment Acceptance", "Card acceptance for business customers through an exclusive alliance with EVO from 2014, extended in 2021 and now with Global Payments; point of sale, e-commerce and dynamic currency conversion, run by Global Payments rather than the bank.", short="BOIPA",
              s=["sme", "corp"], lc="move", o="P", at="Global Payments", ay="2014", neo=[1, "Accepts Mastercard among networks."],
              src=[["BOIPA: about", "https://www.boipa.com/about/"], ["BusinessWire: EVO and Bank of Ireland renew, Nov 2021", "https://www.businesswire.com/news/home/20211130005232/en"]]),
        ]},
        {"id": "2.5", "ic": "globe", "name": "FX & international", "blurb": "Dublin, London, Belfast, Stamford.", "div": "cc", "rev": "cc", "products": [
            P("markets", "Global Markets", "FX and treasury dealing for business clients from Dublin, London, Belfast and Stamford, Connecticut.",
              s=["corp", "sme"], lc="move", neo=[0, ""], src=[["Bank of Ireland Corporate: products and services", "https://corporate.bankofireland.com/products-and-services/"]]),
            P("firstrate", "First Rate Exchange Services", "A 50/50 joint venture with the UK Post Office and the UK's largest consumer FX provider, confirmed to continue in December 2023.",
              s=["uk"], lc="move", o="P", at="Post Office", neo=[0, ""],
              src=[["Bank of Ireland: update on UK partnerships, Dec 2023", IR + "Update-on-UK-financial-services-partnerships.pdf"]]),
        ]},
        {"id": "2.6", "ic": "landmark", "name": "Cash", "blurb": "Guaranteed by law since 2025.", "div": "ri", "rev": "ri", "products": [
            P("cash", "Cash & the Access to Cash Act", "One of three designated banks under the Access to Cash Act (in force June 2025), with a new ATM fleet across the island from a €60 million programme; ATM transactions fell 6% a year to mid-2026.",
              s=["con", "sme"], lc="everyday", neo=[0, ""],
              src=[["Central Bank of Ireland: access to cash", "https://www.centralbank.ie/financial-system/access-to-cash"], ["Bank of Ireland: €60 million in branches and ATMs, Feb 2024", PR + "2024/bank-of-ireland-to-invest-over-e60-million-in-branches-and-atms/"]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account and payment: open an account in ten minutes, stop the fraud before the money goes, let fintechs and Stripe in, put AI under the contact centre and KYC, reward the card and the mortgage, and green the lending.",
    "tiles": [
        {"id": "3.1", "ic": "fingerprint", "name": "Identity & onboarding", "blurb": "An account in ten minutes.", "div": "ri", "rev": "ri", "products": [
            P("onboarding", "Digital account opening", "Open a current account online in under ten minutes with photo ID and a selfie; 'Coming to Ireland' (June 2025) opens accounts for emigrants, workers and students before they arrive; AI cut KYC handling time by 40% in 2026; the new app adds biometrics for payments and cards.",
              s=["con", "young"], lc="open", neo=[0, ""],
              src=[["Bank of Ireland: personal current account", PB + "bank/current-accounts/personal-current-account/"], ["Bank of Ireland: Coming to Ireland, Jun 2025", PR + "2025/bank-of-ireland-launches-new-account-opening-service-to-support-returning-emigrants-and-international-students/"]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud & payee checks", "blurb": "Losses down 25%.", "div": "grp", "rev": "grp", "products": [
            P("fraudai", "Fraud AI", "Featurespace ('a Visa solution') runs the bank's payment-fraud models: attempted fraud down 30% and customer losses down 25% since 2024, false positives down 87% (June 2026). AI screened about a billion card transactions in 2025, preventing €9.7 million of losses; €50 million and 225 people go to fraud prevention.",
              s=["con", "sme"], lc="everyday", o="P", at="Featurespace (Visa)", neo=[0, "Visa's Featurespace."],
              mc="Irish APP fraud nearly doubled in 2025; Featurespace is entrenched and award-winning, so Mastercard's angle is scam and mule-account intelligence on account-to-account payments, beside it.",
              src=[["Bank of Ireland: AI cuts payment fraud losses, Jun 2026", FRAUD], ["BPFI: fraud losses up 27%, Sep 2026", "https://bpfi.ie/consumers-warned-to-be-on-alert-for-scams-new-figures-show-27-jump-in-losses/"]]),
            P("vop", "Verification of Payee", "Name checks on every SEPA and SEPA Instant payment from 5 October 2025, ahead of the EU deadline; it warns but does not block. The UK bank was fined £3.78 million for a late Confirmation of Payee.",
              s=["con", "sme"], lc="move", st="new", ay="Oct 2025", neo=[0, ""],
              src=[["Bank of Ireland: Verification of Payee", PB + "ways-to-bank/mobile-banking/verification-of-payee-vop/"], ["FinTech Global: Confirmation of Payee fine, Apr 2026", "https://fintech.global/2026/04/30/bank-of-ireland-uk-fined-3-78m-for-cop-delay/"]]),
        ]},
        {"id": "3.3", "ic": "webhook", "name": "Open banking & partners", "blurb": "PSD2 APIs, and Stripe.", "div": "grp", "rev": "grp", "products": [
            P("openbanking", "Open banking APIs", "Account information, payment initiation and funds-confirmation APIs for Ireland and the UK on developer.bankofireland.com, with a sandbox since March 2019; no aggregator partner is disclosed.",
              s=["fin"], lc="beyond", ay="Mar 2019", neo=[0, ""],
              mc="PSD3 and FIDA will widen access; Mastercard's European open-banking business (formerly Aiia) is a fit, though nothing is public.",
              src=[["Open Banking: Bank of Ireland implementation guide", "https://openbanking.atlassian.net/wiki/spaces/AD/pages/110101240/Implementation+Guide+BoI"]]),
            P("stripe", "Stripe partnership", "A deeper partnership announced 9 September 2026 for faster payments, back-office automation and Stripe's AI tools in core platforms; Davy has used Stripe since 2021 for more than €2 billion of bank transfers, and New Ireland is following.",
              s=["con", "aff", "fin"], lc="move", st="new", ay="Sep 2026", o="P", at="Stripe", neo=[0, ""],
              src=[["Bank of Ireland: deepens partnership with Stripe, Sep 2026", STRIPE]]),
        ]},
        {"id": "3.4", "ic": "brain", "name": "Data & AI", "blurb": "A Chief AI Officer from Citi.", "div": "grp", "rev": "grp", "products": [
            P("aiplatform", "Enterprise AI platform", "An AI centre of excellence and responsible-AI framework, Microsoft 365 Copilot for about 9,500 colleagues, more than 500 adaptive models, and results so far: KYC and call transfers down 40%, chargeback handling down 38%. A Chief AI Officer, Prag Sharma, joined from Citi in October 2026.",
              s=["con", "sme"], lc="beyond", st="new", neo=[0, ""],
              src=[["H1 2026 key messages", HY26], ["FY2025 results deck", FY25]]),
        ]},
        {"id": "3.5", "ic": "gift", "name": "Loyalty & benefits", "blurb": "Priceless, Avios, cashback.", "div": "ri", "rev": "ri", "products": [
            P("priceless", "Mastercard Priceless", "Priceless experiences and offers on the Mastercard credit cards; Avios on the Aer card.",
              s=["con", "aff"], lc="beyond", o="P", at="Mastercard", neo=[3, "Mastercard's own."],
              src=[["Bank of Ireland: Classic credit card", PB + "borrow/credit-cards/classic-credit-card"]]),
            P("cashback", "Mortgage cashback & card offers", "2% cashback at drawdown on fixed-rate mortgages, or 'Cashback Plus' with another 1% in year five; Live Life Rewards, a Visa card-linked cashback scheme from 2018, may no longer run.",
              s=["home", "con"], lc="grow", neo=[0, "Live Life Rewards was Visa."],
              mc="With no current card-linked offers on the debit or credit book, merchant-funded offers in the new app are an open space.",
              src=[["Bank of Ireland: mortgage cashback", PB + "?p=125286"], ["Bank of Ireland: Live Life Rewards, 2018", PR + "2018/live-life-rewards-bank-ireland/"]]),
        ]},
        {"id": "3.6", "ic": "sparkles", "name": "Sustainability", "blurb": "94% of mortgages green.", "div": "grp", "rev": "grp", "products": [
            P("green", "Green lending", "EcoSaver green mortgages were about 94% of new mortgage lending in 2025, with 53% of drawdowns for A- or B-rated homes; green home and business loans and a sustainable-energy book; MSCI AAA.",
              s=["home", "sme", "corp"], lc="borrow", neo=[0, ""],
              mc="A carbon footprint on card spend would complete a green proposition already built on mortgages.",
              src=[["FY2025 results deck", FY25], ["H1 2026 key messages", HY26]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "The four segments the group reports (Retail Ireland, Wealth and Insurance, Retail UK, Corporate and Commercial) opened out into what more than 4 million customers buy: Ireland's largest mortgage lender, half its SME lending, its largest wealth manager, and a UK bank.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Everyday banking", "blurb": "A third of current accounts.", "div": "ri", "rev": "ri", "products": [
            P("pca", "Personal current accounts", "About a third of Irish personal current accounts (2.2 million retail customers), €6 a month, with 81% digitally active; Golden Years, Graduate, Third Level and basic accounts beside it.",
              s=["con"], lc="everyday", neo=[0, "Visa debit."], src=[["FY2025 results deck", FY25]]),
            P("smartstart", "Smart Start", "A free account for children aged 7 to 15 (June 2025) with a Visa debit card, parental controls and a 2% Money Pot, run in the new app.",
              s=["young"], lc="open", st="new", ay="Jun 2025", neo=[0, "Visa debit."],
              src=[["Bank of Ireland: Smart Start, Jun 2025", PR + "2025/bank-of-ireland-launches-smart-start-account/"]]),
            P("bca", "Business current accounts", "About 45% of Irish business current accounts and 280,000 small-business customers.",
              s=["sme"], lc="everyday", neo=[0, "Visa business debit."], src=[["FY2025 results deck", FY25]]),
        ]},
        {"id": "4.2", "ic": "coins", "name": "Savings", "blurb": "€87 billion of everyday deposits.", "div": "ri", "rev": "ri", "products": [
            P("savings", "Savings & the State's investment account", "MortgageSaver, SuperSaver, ChildSave and term deposits, now opened in the app; €87 billion of everyday deposits; Davy and New Ireland are preparing products for the State-sponsored Savings and Investment Account.",
              s=["con", "home", "aff"], lc="grow", neo=[0, ""], src=[["H1 2026 results transcript", HY26T], ["FY2025 results deck", FY25]]),
        ]},
        {"id": "4.3", "ic": "house", "name": "Mortgages", "blurb": "42% of new Irish lending.", "div": "ri", "rev": "ri", "products": [
            P("mortgages", "Home loans", "Ireland's largest mortgage lender every quarter since late 2022: €6.1 billion of new lending in 2025 (42% of the market), a €37 billion book growing 6% in the first half of 2026, about 96% fixed-rate, with automated credit decisions planned.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["FY2025 results deck", FY25], ["H1 2026 results transcript", HY26T]]),
            P("tradedown", "Trade Down Equity Release", "Bridging for older owners buying a smaller home: up to 60% loan-to-value with no repayments for up to a year while the old home sells (2026).",
              s=["home"], lc="borrow", st="new", ay="2026", neo=[0, ""],
              src=[["Bank of Ireland: housing supply initiatives, Nov 2025", PR + "2025/bank-of-ireland-announces-initiatives-to-accelerate-housing-supply/"]]),
        ]},
        {"id": "4.4", "ic": "hand-coins", "name": "Consumer & motor finance", "blurb": "Loans, cars, EVs.", "div": "ri", "rev": "ri", "products": [
            P("loans", "Personal loans", "A €2.6 billion consumer book in Ireland at the end of 2025.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["FY2025 results deck", FY25]]),
            P("motor", "Motor finance", "Hire purchase and PCP through dealers via Bank of Ireland Finance, with an EV marketplace and lower rates for battery-electric cars; asset and motor finance moved into Retail Ireland in 2026.",
              s=["con", "sme"], lc="borrow", neo=[0, ""],
              src=[["Bank of Ireland: motor finance", PB + "borrow/loans/motor-finance-loan/features-benefits/"]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Wealth & insurance", "blurb": "€65.5 billion under management.", "div": "wi", "rev": "wi", "products": [
            P("davy", "Davy", "Ireland's largest wealth manager and stockbroker, bought in June 2022 for about €427 million: €33 billion under management at the end of 2025, and the home of the former Bank of Ireland Private clients since 2023. Davy Select offers execution-only investing.",
              s=["aff"], lc="grow", o="A", ay="Jun 2022", neo=[0, ""],
              src=[["Davy: completion of sale to Bank of Ireland, 2022", "https://davy.ie/about-us/news/2022/completion-of-the-sale-of-davy-to-bank-of-ireland.html"], ["FY2025 results deck", FY25]]),
            P("newireland", "New Ireland Assurance", "Life, protection and pensions since 1997: €27 billion under management and about a fifth of the market; bancassurance sales up 24% in 2025. Wealth AUM overall €65.5 billion, aiming for €75 billion by 2028.",
              s=["con", "aff", "home"], lc="grow", o="A", neo=[0, ""],
              src=[["FY2025 results deck", FY25], ["H1 2026 results transcript", HY26T]]),
            P("insurance", "General insurance", "Car insurance underwritten by RSA since 2013, and home insurance, through Bank of Ireland Insurance Services; four in ten new mortgage borrowers take general cover.",
              s=["con", "home"], lc="beyond", o="P", at="RSA", neo=[0, ""],
              src=[["Bank of Ireland: car insurance documents", PB + "insure-and-protect/insurance/car-insurance/important-documents"]]),
        ]},
        {"id": "4.6", "ic": "building-2", "name": "Business & corporate", "blurb": "Half of SME lending.", "div": "cc", "rev": "cc", "products": [
            P("sme", "SME & agri lending", "More than half of Irish SME lending (a €7.1 billion book), decided on an nCino platform (about 20,000 applications since 2025), with State-backed SBCI schemes and an AI academy for SME customers.",
              s=["sme"], lc="borrow", o="P", at="nCino, SBCI", neo=[1, "Business credit cards on Mastercard."],
              src=[["FY2025 results deck", FY25], ["Bank of Ireland: €370 million in retail, 2025", PR + "2025/e370million-invested-in-bank-of-irelands-retail-division-during-three-year-strategic-cycle/"]]),
            P("corporate", "Corporate & Commercial", "A €22 billion corporate book (about 70% Irish): corporate, property and sustainable-energy lending, trade finance, cash management and agency; about 13,000 relationships. US leveraged acquisition finance is being exited.",
              s=["corp"], lc="borrow", neo=[0, ""],
              src=[["FY2025 results deck", FY25], ["Bank of Ireland Corporate: products and services", "https://corporate.bankofireland.com/products-and-services/"]]),
        ]},
        {"id": "4.7", "ic": "earth", "name": "UK", "blurb": "Over a million UK customers.", "div": "uk", "rev": "uk", "products": [
            P("ukbank", "Bank of Ireland UK", "£16.9 billion of loans (mortgages £12.9 billion, asset finance £3.1 billion) and a 16% return in 2025: GB mortgages through brokers and a Northern Ireland bank with 13 branches that still issues banknotes; UK credit cards and a commercial card are still offered.",
              s=["uk"], lc="borrow", neo=[None, "UK card networks not verified."],
              src=[["FY2025 results deck", FY25]]),
            P("northridge", "Northridge Finance", "Motor and asset finance in Great Britain through dealers and brokers; the UK motor-commission redress has cost about €435 million in provisions.",
              s=["uk"], lc="borrow", neo=[0, ""],
              src=[["Bank of Ireland: update on UK motor finance, Mar 2026", IR + "2026.03.31-BOIG-RNS-Further-update-on-UK-Motor-Finance.pdf"]]),
            P("postoffice", "Post Office partnership", "UK savings under the Post Office brand, extended to at least 2031 in December 2023; Post Office mortgages and loans, and the AA partnership, ended.",
              s=["uk"], lc="grow", o="P", at="Post Office", neo=[0, ""],
              src=[["Bank of Ireland: update on UK partnerships, Dec 2023", IR + "Update-on-UK-financial-services-partnerships.pdf"]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: a new app with 30 million log-ins a month, 169 branches in the Republic and 13 in Northern Ireland, more than 900 post offices, a new ATM fleet, Business On Line, and a contact centre where every agent uses AI.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App & 365 Online", "blurb": "30 million log-ins a month.", "div": "ri", "rev": "ri", "products": [
            P("app", "Bank of Ireland app", "About 30 million log-ins a month; a new native app rolling out from 30 July 2026 with card freeze, balance blur, biometric approvals, and savings and Smart Start opened in-app; 365 Online and 365 Phone beside it.",
              s=["con", "young", "sme"], lc="everyday", st="new", ay="Jul 2026", neo=[0, ""],
              src=[["Bank of Ireland: new mobile app, Jul 2026", APP]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & post offices", "blurb": "More than 1,000 places.", "div": "ri", "rev": "ri", "products": [
            P("branches", "Branches", "169 branches in the Republic after 88 closed in 2021, and 13 in Northern Ireland, being refurbished under a €60 million programme.",
              s=["con", "aff", "sme"], lc="everyday", neo=[0, ""],
              src=[["Bank of Ireland: service changes", "https://bankofireland.com/service-changes"]]),
            P("anpost", "An Post", "Lodgements, withdrawals and cheques at more than 900 post offices since 2021.",
              s=["con", "sme"], lc="everyday", o="P", at="An Post", ay="2021", neo=[0, ""],
              src=[["bonkers.ie: Bank of Ireland at An Post", "https://bonkers.ie/blog/banking/boi-customers-can-now-bank-through-an-post"]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "Business channels", "blurb": "Business On Line.", "div": "cc", "rev": "cc", "products": [
            P("bol", "Business On Line", "Online banking and payments for SMEs and corporates, with Gold Card Business Online for expenses; a new commercial digital platform is planned under Strategy 2028.",
              s=["sme", "corp"], lc="everyday", neo=[0, ""], src=[["FY2025 results deck", FY25]]),
        ]},
        {"id": "5.4", "ic": "headset", "name": "Contact centre", "blurb": "Every agent on GenAI.", "div": "ri", "rev": "ri", "products": [
            P("contact", "Contact centre", "1.25 million fewer calls than in 2022, GenAI used by 99% of agents and call hand-offs down more than 40%; a dedicated line for vulnerable customers.",
              s=["con", "sme"], lc="everyday", neo=[0, ""],
              mc="Consumer Clarity would answer card-transaction queries before they reach an agent.",
              src=[["FY2025 results deck", FY25]]),
        ]},
        {"id": "5.5", "ic": "plug", "name": "Wealth & partner platforms", "blurb": "myDavy, brokers, developers.", "div": "wi", "rev": "wi", "products": [
            P("platforms", "Davy, New Ireland & partner platforms", "myDavy and Davy Select for investors, a new digital wealth platform in pilot, New Ireland's broker channel, and the developer portal for fintechs.",
              s=["aff", "fin"], lc="grow", st="new", neo=[0, ""], src=[["H1 2026 key messages", HY26]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Bank of Ireland", "blurb": "Credit yes, debit no.", "products": [
        P("mcatboi", "Mastercard at Bank of Ireland", "Mastercard has carried all the bank's credit cards since 2015 and puts Priceless on them; Visa carries debit, the coming Click to Pay and, through Featurespace, the fraud models. Mastercard's European technology hub, now more than 2,000 people, is a few kilometres away in Leopardstown (second building opened October 2026). No joint announcement since 2015 has been found.",
          s=["fin"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Irish Times: Bank of Ireland moves to Mastercard, Sep 2015", SWITCH2015], ["RTÉ: Mastercard expands in Dublin, Oct 2026", "https://www.rte.ie/news/business/2026/1008/1594539-mastercard-expands-dublin-operations-with-second-office/"]]),
    ]},
    {"id": "pillar-market", "name": "Irish payments", "blurb": "Three banks and Revolut.", "products": [
        P("irishmarket", "The Irish payments market", "More than 1.2 billion card payments worth almost €50 billion in the first half of 2026, nine in ten point-of-sale payments contactless and nearly two-thirds of those by phone; Revolut reaches more than 80% of adults; Visa holds debit at all three pillar banks and renewed PTSB in June 2026; wero has not come to Ireland.",
          s=["con"], div="grp", rev="grp",
          src=[["RTÉ: BPFI card payment figures, Sep 2026", "https://www.rte.ie/news/business/2026/0911/1591127-bpfi-card-payment-figures/"], ["Visa: PTSB renewal, Jun 2026", "https://www.visa.ie/about-visa/newsroom/press-releases.3453390.html"]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
