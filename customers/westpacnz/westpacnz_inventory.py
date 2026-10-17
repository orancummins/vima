"""Westpac New Zealand's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Westpac NZ's own unless a source says otherwise: the half-year release for the six months to
31 March 2026 (5 May 2026), the parent's 2025 annual report, and Westpac NZ media releases as republished
by Scoop (westpac.co.nz blocked automated reading). ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

HY26 = "https://business.scoop.co.nz/2026/05/05/westpac-nz-strongly-positioned-to-help-customers-through-challenging-times/"
NZH26 = "https://www.nzherald.co.nz/business/companies/banking-finance/westpac-profit-up-4-but-warns-on-economy-ocr-cuts-and-fuel-costs/premium/IZGJN7HPGFDYJPO65DJTWOHMM4/"
DS26 = "https://filingreader.com/news-wire/newzealand/2026-05-12/westpac-new-zealand-profit-falls-to-nz517m-amid-capital-changes"
DS25 = "https://filingreader.com/news-wire/newzealand/2025-11-11/westpac-nz-reports-slight-profit-dip-solid-asset-growth-in-annual-statement"
AR25 = "https://www.westpac.com.au/content/dam/public/wbc/documents/pdf/aw/ic/wbc-annual-report-2025.pdf"
GEXCO = "https://www.westpac.com.au/about-westpac/westpac-group/executive-team/"
NZEXCO = "https://westpac.co.nz/about-us/executive-team"
APPT26 = "https://announcements.nzx.com/announcement/474068"
HY25 = "https://business.scoop.co.nz/2025/05/05/westpac-nz-posts-resilient-half-year-result/"
FY24 = "https://business.scoop.co.nz/2024/11/04/westpac-nz-reports-broadly-flat-underlying-profit/"
CCKEY = "https://assets.dam.westpac.co.nz/is/content/wnzl/dist/cards/personal-credit-cards/general-personal-credit-cards/General-Personal-Credit-Cards_Key-information-about-your-credit-card_brochure.pdf"
MC14 = "https://interest.co.nz/business/69364/westpacs-mastercard-deal-feature-focus-products-business-and-institutional-customers"
DEBIT15 = "https://interest.co.nz/personal-finance/78007/westpac-unveils-debit-card-earns-its-user-airpoints-also-throws-paytag"
AIRNZ15 = "https://traveldaily.com.au/?p=217908"
AIRNZ26 = "https://www.westpac.co.nz/about-us/media/westpac-nz-plans-new-and-better-customer-experiences-after-extending-air-new-zealand-koru-partnership/"
GPAY = "https://www.westpac.co.nz/help/what-westpac-mastercard-cards-are-eligible-for-google-pay/"
MERCH = "https://www.westpac.co.nz/business/accepting-payments/westpac-merchant-facility/"
CUSCAL = "https://www.interest.co.nz/banking/138093/australias-cuscal-acquiring-electronic-payments-processor-worldline-new-zealand-and"
PAYMARK = "https://www.goodreturns.co.nz/article/976515847/westpac-nz-annual-profit-rises-3-rbnz-releases-it-from-capital-purgatory.html"
IFEE = "https://blog.eftpos.co.nz/blog/interchange-fee-changes-what-they-mean-for-your-business"
SURCH = "https://blog.eftpos.co.nz/blog/2026-surcharge-ban-guide-for-nz-businesses"
OBFEE = "https://business.scoop.co.nz/2025/05/16/westpac-nz-supports-open-banking-rollout-by-not-charging-fintechs-for-standard-api-calls/"
OBMILE = "https://business.scoop.co.nz/2024/05/30/westpac-nz-hits-open-banking-milestone/"
POLI = "https://www.mpamag.com/nz/news/general/westpac-poli-partner-to-launch-secure-open-banking/541125"
APIEND = "https://www.apicentre.paymentsnz.co.nz/news/articles/open-banking-moves-into-its-next-phase/"
APICLOSE = "https://www.apicentre.paymentsnz.co.nz/news/articles/payments-nz-announces-closure-of-api-centre/"
INTL = "https://business.scoop.co.nz/2025/12/01/westpac-nz-removes-international-transfer-fees-from-online-banking-payments/"
SUBS = "https://www.rnz.co.nz/news/business/567718/westpac-warns-of-multi-million-dollar-subscription-trap"
FBSCAM = "https://www.mpamag.com/nz/specialty/residential/fake-facebook-complaints-pages-used-to-scam-westpac-nz-customers/586447"
COP = "https://www.westpac.co.nz/personal/ways-to-bank/westpac-one-online-banking/confirmation-of-payee-checks-your-digital-banking-payments/"
GAMB = "https://business.scoop.co.nz/2025/10/30/westpac-nz-introduces-gambling-and-online-spending-controls-to-support-customers/"
CCAAS = "https://business.scoop.co.nz/2026/04/14/westpac-nz-becomes-first-major-nz-company-to-launch-microsoft-ai-tool-to-support-human-to-human-customer-conversations/"
VANS = "https://business.scoop.co.nz/2025/11/04/banking-vans-and-longer-branch-hours-as-westpac-strengthens-community-support/"
TOWER = "https://business.scoop.co.nz/2025/09/26/westpac-nz-announces-new-general-insurance-partnership-with-tower/"
TOWER26 = "https://business.scoop.co.nz/2026/07/02/westpac-nz-offers-customers-in-app-access-to-information-about-a-propertys-natural-hazard-risks/"
FIDELITY = "https://business.scoop.co.nz/2025/06/12/westpac-nz-and-fidelity-life-launch-new-digital-guide-to-make-life-insurance-easier/"
DOSH = "https://business.scoop.co.nz/2025/03/11/dosh-teams-up-with-westpac-nz-to-offer-innovative-home-loan-solution/"
START = "https://business.scoop.co.nz/2025/10/16/westpac-nz-announces-100m-commitment-to-support-start-up-businesses/"
PENALTY = "https://business.scoop.co.nz/2025/11/28/westpac-nz-penalised-3-64-million-for-not-being-a-responsible-lender-system-design-called-foreseeably-deficient/"
BASIC = "https://business.scoop.co.nz/2026/03/12/westpac-nz-supports-hybrid-approach-to-basic-bank-accounts/"
GRPAI = "https://www.westpac.com.au/about-westpac/media/media-releases/2026/5-february"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · parent · licence", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: NZ$108 billion of lending and NZ$545 million of half-year profit, a wholly owned subsidiary of Australia's oldest bank, about a sixth of the NZ market, a rebuilt technology base and a push to grow from fourth place.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "NZ$545m in the half.", "div": "wnz", "rev": "central", "products": [
            P("results", "Balance sheet & earnings", "Net profit of NZ$545 million in the half to 31 March 2026 (+4%), NIM 2.29%, home lending NZ$73.3 billion, business lending NZ$35.0 billion and deposits NZ$83.7 billion; NZ$1,197 million in the year to September 2025 (+13%). The WNZL banking group had NZ$144.1 billion of assets ⚠.",
              s=["corp"], neo=[0, ""], src=[["Westpac NZ: HY26 result, May 2026", HY26], ["Westpac 2025 annual report", AR25], ["WNZL disclosure HY26 (summary)", DS26]]),
        ]},
        {"id": "1.2", "ic": "building-2", "name": "Parent & entities", "blurb": "100% Westpac Group.", "div": "wbc", "rev": "central", "products": [
            P("parent", "Westpac Group & legal entities", "Westpac New Zealand Limited is wholly owned by Westpac Banking Corporation (founded 1817; 13 million customers, 35,000 staff). Westpac NZ also covers BT Funds Management (NZ) and WBC's NZ Branch; New Zealand earned 16% of group profit in 2025.",
              s=["corp"], o="I", neo=[0, ""], src=[["Westpac 2025 annual report", AR25]]),
            P("share", "Market position", "The smallest of the four largest banks by its own account, with 18% of consumer lending, 17% of deposits and 16% of business lending (RBNZ, September 2025).",
              s=["con", "sme"], neo=[0, ""], src=[["Westpac 2025 annual report", AR25], ["Westpac NZ: HY25 result, May 2025", HY25]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Leadership", "blurb": "McGrath since 2021.", "div": "wnzl", "rev": "central", "products": [
            P("leadership", "Board & executive team", "Chair Pip Greenwood; CEO Catherine McGrath since November 2021, formerly a payments executive at Barclays and Lloyds TSB; Russell Jones became Chief Data, Digital and AI Officer and James Pretty CIO in June 2026 ⚠; Helen Ryder and Reuben Tucker run the two banking divisions ⚠.",
              s=["corp"], neo=[0, ""], src=[["Westpac 2025 annual report", AR25], ["NZX: executive appointments, Jun 2026", APPT26], ["Westpac NZ: executive team", NZEXCO], ["Westpac Group: executive team", GEXCO]]),
        ]},
        {"id": "1.4", "ic": "shield-check", "name": "Capital & conduct", "blurb": "RBNZ rules, CCCFA fine.", "div": "wnzl", "rev": "central", "products": [
            P("capital", "Capital & regulation", "CET1 12.5% at September 2025 ⚠; the RBNZ's 2025 capital review sets a 12% CET1 minimum ⚠; its Branch Standard (from 2028) limits WBC's NZ Branch to large clients; a record NZ$3.64 million CCCFA penalty in November 2025 for lending-system failures.",
              s=["corp"], st="flux", neo=[0, ""], src=[["WNZL disclosure FY25 (summary)", DS25], ["WNZL disclosure HY26 (summary)", DS26], ["Westpac 2025 annual report", AR25], ["Commerce Commission: CCCFA penalty, Nov 2025", PENALTY]]),
        ]},
        {"id": "1.5", "ic": "database", "name": "Technology & AI", "blurb": "Rebuilt stack, AI in service.", "div": "wnz", "rev": "central", "products": [
            P("tech", "Infrastructure & data", "Network, computing platforms and mainframe overhauled and new data centres built; the group gave all staff Microsoft AI tools in February 2026; a Chief Data, Digital and AI Officer role created in June 2026 ⚠.",
              s=["corp"], neo=[0, ""], src=[["Westpac NZ: Microsoft CCaaS, Apr 2026", CCAAS], ["Westpac: Microsoft AI for staff, Feb 2026", GRPAI], ["NZX: executive appointments, Jun 2026", APPT26]]),
            P("ccaas", "AI contact centre (Microsoft CCaaS)", "The first NZ bank on Microsoft Dynamics 365 Contact Centre as a Service, whose AI surfaces the customer's profile and product details in real time; rollout from April 2026 to all NZ-based contact centres by August 2026.",
              s=["con", "sme"], lc="everyday", st="new", ay="Apr 2026", o="P", at="Microsoft", neo=[0, ""], src=[["Westpac NZ: Microsoft CCaaS, Apr 2026", CCAAS]]),
        ]},
        {"id": "1.6", "ic": "target", "name": "Strategy", "blurb": "Grow from fourth.", "div": "wnz", "rev": "central", "products": [
            P("strategy", "Growth plan", "Grow business lending, invest in digital, improve market position and returns. SME lending has grown faster than the market for two years; total lending +6% in the half to March 2026.",
              s=["corp", "sme"], neo=[0, ""], src=[["Westpac 2025 annual report", AR25], ["Westpac NZ: HY26 result, May 2026", HY26]]),
            P("partnerships", "Partnerships & deals", "Sold its Paymark stake (gain NZ$40 million, 2019); Fidelity Life for life cover; Dosh home loans (March 2025); Tower replacing IAG for general insurance from July 2026; POLi on its open-banking APIs (July 2025).",
              s=["con", "home"], o="P", at="Fidelity Life, Tower, Dosh, POLi", neo=[0, ""], src=[["Good Returns: Paymark gain, Nov 2019", PAYMARK], ["Westpac NZ: Tower, Sep 2025", TOWER], ["Dosh: home loans, Mar 2025", DOSH], ["NZ Adviser: POLi, Jul 2025", POLI]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: debit Mastercard with domestic EFTPOS on the same card, an all-Mastercard credit range, business cards, wallets and digital cards, merchant acceptance over Verifone and Worldline, open-banking payments, and fee-free international transfers.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Mastercard plus EFTPOS.", "div": "wnz", "rev": "cbw", "products": [
            P("debit", "Westpac Debit Mastercard", "Debit on Mastercard for online, phone, contactless and overseas use, with domestic EFTPOS (cheque or savings) on the same card for insert-and-PIN payments.", short="Debit (Mastercard + EFTPOS)",
              s=["con", "sme"], lc="everyday", o="P", at="Mastercard", neo=[1, "Mastercard, with EFTPOS for PIN payments."],
              mc="Mastercard carries Westpac's contactless and online debit; EFTPOS keeps the PIN payments.",
              src=[["interest.co.nz: Airpoints debit, Oct 2015", DEBIT15], ["Westpac NZ: Google Pay cards", GPAY]]),
            P("airdebit", "Airpoints Debit Mastercard", "New Zealand's first Airpoints-earning debit card (October 2015): one Airpoints dollar per NZ$250, with at least NZ$500 deposited a month; launched with the PayTag contactless sticker ⚠ current status.",
              s=["con"], lc="everyday", ay="Oct 2015", o="P", at="Mastercard, Air New Zealand", neo=[2, "Mastercard debit."], src=[["interest.co.nz: Airpoints debit, Oct 2015", DEBIT15]]),
            P("eftpos", "EFTPOS (domestic debit)", "Insert-and-PIN EFTPOS from cheque or savings carries no merchant service fee, unique to New Zealand; switched by Worldline NZ (Paymark), which Cuscal agreed to buy in April 2026.",
              s=["con"], lc="everyday", st="flux", o="P", at="Worldline NZ (Paymark)", neo=[0, "Domestic EFTPOS."], src=[["EFTPOS NZ: interchange caps, May 2026", IFEE], ["interest.co.nz: Cuscal buys Worldline NZ, Apr 2026", CUSCAL]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "All Mastercard.", "div": "wnz", "rev": "cbw", "products": [
            P("airpoints", "Airpoints Mastercard range", "Airpoints, Airpoints Platinum and Airpoints World Mastercard (annual fee up to NZ$310), earning Air New Zealand Airpoints since Westpac replaced BNZ as partner in 2015.", short="Airpoints (Mastercard)",
              s=["con"], lc="borrow", ay="2015", o="P", at="Mastercard, Air New Zealand", neo=[2, "Mastercard credit."],
              mc="The premium end of an all-Mastercard book.",
              src=[["Westpac NZ: credit card key information, Jul 2026", CCKEY], ["Travel Daily: Air NZ picks Westpac, Mar 2015", AIRNZ15]]),
            P("hotpoints", "hotpoints Mastercard range", "hotpoints, hotpoints Platinum and hotpoints World Mastercard, with hotpoints Pay letting customers spend points like cash (NZ$11 million redeemed by late 2024).", short="hotpoints (Mastercard)",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard credit."], src=[["Westpac NZ: credit card key information, Jul 2026", CCKEY], ["Westpac NZ: FY24 result, Nov 2024", FY24]]),
            P("feefree", "Westpac Fee Free Mastercard", "A no-annual-fee credit card, the entry point to the range (terms effective 31 July 2026).",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard credit."], src=[["Westpac NZ: credit card key information, Jul 2026", CCKEY]]),
        ]},
        {"id": "2.3", "ic": "briefcase-business", "name": "Business cards", "blurb": "BusinessPLUS, Airpoints Business.", "div": "wnz", "rev": "ibb", "products": [
            P("bizcards", "BusinessPLUS & Airpoints Business Mastercard", "Business credit cards with limits up to NZ$100,000 and annual fees of NZ$100 and NZ$145; the 2014 Mastercard deal was pitched at business and institutional products.", short="Business cards (Mastercard)",
              s=["sme", "agri"], lc="move", ay="2014", o="P", at="Mastercard", neo=[2, "Mastercard commercial."],
              mc="Commercial interchange is still uncapped in NZ; virtual cards are open ground.",
              src=[["Westpac NZ: credit card key information, Jul 2026", CCKEY], ["interest.co.nz: Mastercard deal, Apr 2014", MC14]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Wallets & digital cards", "blurb": "Instant cards, dynamic codes.", "div": "wnz", "rev": "cbw", "products": [
            P("wallets", "Apple Pay & Google Pay", "Available on eligible Westpac debit, credit and business Mastercards ⚠ start dates not found.",
              s=["con", "sme"], lc="everyday", o="P", at="Apple, Google, Mastercard", neo=[2, "Mastercard tokens."], src=[["Westpac NZ: Google Pay cards", GPAY]]),
            P("digicard", "Instant digital cards with dynamic security codes", "New debit cards usable straight away through digital issuance (2024); digital credit and debit cards with dynamic security codes from March 2025, a first for a New Zealand bank.",
              s=["con"], lc="everyday", st="new", ay="Mar 2025", o="B", neo=[2, "Digital Mastercards ⚠ code provider not named."],
              mc="A natural base for Click to Pay and full tokenisation.",
              src=[["Westpac NZ: HY25 result, May 2025", HY25], ["Westpac NZ: FY24 result, Nov 2024", FY24]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Merchant acceptance", "blurb": "Verifone or Worldline terminals.", "div": "wnz", "rev": "ibb", "products": [
            P("merchant", "Westpac merchant facility", "Card acceptance for businesses on terminals connected to the Verifone or Worldline networks from an approved list ⚠; in-person NZ credit interchange capped at 0.3% from 1 December 2025.",
              s=["sme"], lc="move", o="P", at="Verifone, Worldline", neo=[1, "Accepts every network."], src=[["Westpac NZ: merchant facility", MERCH], ["EFTPOS NZ: interchange caps, May 2026", IFEE]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Open-banking payments", "blurb": "Free APIs, POLi.", "div": "wnz", "rev": "cbw", "products": [
            P("openbanking", "Open-banking payment APIs", "Payment initiation to Payments NZ standards (v2.1 in 2024 ⚠, v2.3 by May 2025), standard API calls free to accredited fintechs for at least 12 months from May 2025; an Online EFTPOS participant since 2019.",
              s=["con", "sme"], lc="move", st="new", ay="May 2025", o="B", neo=[0, "Bank rails."],
              mc="NZ open-banking payments rose 36% in a month to 545,681 in August 2026.",
              src=[["Westpac NZ: free API calls, May 2025", OBFEE], ["Westpac NZ: open-banking milestone, May 2024", OBMILE], ["API Centre: next phase, Sep 2026", APIEND]]),
            P("poli", "POLi on Westpac APIs", "POLi's 2,000+ merchants moved onto Westpac's bank-approved APIs in July 2025, so customers approve payments inside Westpac's own banking.",
              s=["con"], lc="move", st="new", ay="Jul 2025", o="P", at="POLi", neo=[0, "Account-to-account."], src=[["NZ Adviser: POLi, Jul 2025", POLI]]),
        ]},
        {"id": "2.7", "ic": "earth", "name": "International payments", "blurb": "No fee, 137 countries.", "div": "wnz", "rev": "cbw", "products": [
            P("intl", "International transfers", "The NZ$5 fee on international payments through Westpac One was removed from 1 December 2025; 23 currencies to more than 137 countries, two-thirds in Australian and US dollars.",
              s=["con", "sme"], lc="move", st="new", ay="Dec 2025", o="B", neo=[0, "Bank rails."],
              mc="Pacific and Asian remittance corridors are where Mastercard Move could compete.",
              src=[["Westpac NZ: international fees removed, Dec 2025", INTL]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud and scam defences that cut losses by 15%, payee name checks, card controls for gambling and online spending, blocks on subscription traps, Akahu-enriched transactions, and Airpoints and hotpoints rewards.",
    "tiles": [
        {"id": "3.1", "ic": "fingerprint", "name": "Fraud & scams", "blurb": "Losses down 15%.", "div": "wnz", "rev": "cbw", "products": [
            P("fraud", "Fraud & scam prevention", "Biometric software and enhanced monitoring: NZ$9 of every NZ$10 of known fraud prevented, recovered or reimbursed; customer losses down 15% in the half to March 2026; 64% of scam cases now start on social media.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, "Westpac's own ⚠."],
              mc="Scam scoring and identity checks are not public at Westpac NZ.",
              src=[["Westpac NZ: HY26 result, May 2026", HY26], ["Westpac NZ: HY25 result, May 2025", HY25], ["NZ Adviser: fake complaints pages, Aug 2026", FBSCAM]]),
            P("cop", "Confirmation of Payee", "Name checks for new and changed payees in Westpac One and Westpac One Business; not available for international payments ⚠.",
              s=["con", "sme"], lc="move", st="new", o="P", at="NZ banking industry", neo=[0, "Bank rails."], src=[["Westpac NZ: Confirmation of Payee", COP], ["Westpac NZ: international fees removed, Dec 2025", INTL]]),
        ]},
        {"id": "3.2", "ic": "key-round", "name": "Card controls & insights", "blurb": "Gambling blocks, Akahu data.", "div": "wnz", "rev": "cbw", "products": [
            P("controls", "Gambling & online spending controls", "In-app switches (October 2025) stop a debit or credit card being used for gambling, including overseas sites, or for any online or phone purchase; used more than 6,500 times in two weeks.",
              s=["con"], lc="everyday", st="new", ay="Oct 2025", o="B", neo=[1, "Runs on Mastercard card data."], src=[["Westpac NZ: card controls, Oct 2025", GAMB]]),
            P("substrap", "Subscription-trap block", "Since April 2024 Westpac blocks card charges from merchants that bury recurring subscriptions in fine print: more than NZ$25 million stopped.",
              s=["con"], lc="everyday", ay="Apr 2024", o="B", neo=[1, "Card-data based."],
              mc="Merchant data and recurring-payment tools could sharpen this.",
              src=[["RNZ: subscription traps, Jul 2025", SUBS]]),
            P("enrich", "Enriched transactions", "A partnership with local fintech Akahu adds enriched transaction details in Westpac One to help customers track spending (2025).",
              s=["con"], lc="everyday", st="new", o="P", at="Akahu", neo=[0, "Akahu."],
              mc="Merchant and spend data is a Mastercard strength not used here.",
              src=[["Westpac NZ: card controls, Oct 2025", GAMB]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards", "blurb": "Airpoints and hotpoints.", "div": "partners", "rev": "cbw", "products": [
            P("airnz", "Air New Zealand partnership", "Westpac has been Air New Zealand's bank partner since 2015 and extended the partnership in June 2026 under Air NZ's Koru programme, promising new features ⚠.",
              s=["con", "sme"], lc="grow", st="flux", ay="Jun 2026", o="P", at="Air New Zealand", neo=[1, "Earned on Mastercard cards."],
              mc="Offers and Priceless experiences could feed the promised new features.",
              src=[["Westpac NZ: Air NZ partnership extended, Jun 2026", AIRNZ26], ["Travel Daily: Air NZ picks Westpac, Mar 2015", AIRNZ15]]),
            P("hotpay", "hotpoints Pay", "Use hotpoints like cash on everyday purchases and bills, in Westpac One since April 2024; more than NZ$11 million redeemed in its first six months.",
              s=["con"], lc="grow", ay="Apr 2024", o="B", neo=[1, "Points from Mastercard spend."], src=[["Westpac NZ: FY24 result, Nov 2024", FY24]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: NZ$73 billion of home loans, everyday and savings accounts including a basic account, business and agri lending on a new platform, institutional banking, and KiwiSaver and insurance through BT, Fidelity Life and Tower.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Home lending", "blurb": "NZ$73.3bn.", "div": "wnzl", "rev": "cbw", "products": [
            P("homeloans", "Home loans", "NZ$73.3 billion of home lending (+5%), 3,121 first-home purchases in the half to March 2026, decisions on average within a day, First Home Loans and shared equity, and the NZ$1 billion affordable-housing target passed.",
              s=["home"], lc="borrow", o="B", neo=[0, ""], src=[["Westpac NZ: HY26 result, May 2026", HY26]]),
            P("dosh", "Dosh home loans", "Home loans sold by fintech Dosh and powered by Westpac NZ, applied for online in minutes, with a cashback loyalty reward (March 2025).",
              s=["home"], lc="borrow", st="new", ay="Mar 2025", o="P", at="Dosh", neo=[0, ""], src=[["Dosh: home loans, Mar 2025", DOSH]]),
            P("greener", "Greater Choices top-ups", "More than NZ$300 million lent interest-free since 2020 to help customers cut home energy costs.",
              s=["home"], lc="borrow", o="B", neo=[0, ""], src=[["Westpac NZ: HY26 result, May 2026", HY26]]),
        ]},
        {"id": "4.2", "ic": "wallet", "name": "Everyday & savings", "blurb": "NZ$83.7bn deposits.", "div": "wnzl", "rev": "cbw", "products": [
            P("accounts", "Everyday accounts & savings", "Deposits of NZ$83.7 billion (+3%); nearly 6,000 Notice Saver accounts opened in the half at 3.00%; transaction accounts carry debit Mastercard and EFTPOS.",
              s=["con", "saver"], lc="everyday", o="B", neo=[1, "Debit Mastercard on accounts."], src=[["Westpac NZ: HY26 result, May 2026", HY26]]),
            P("basic", "Basic bank account", "The first bank to pilot a basic account (April 2025): fee-free essential transactions with simplified onboarding and spend limits; Westpac backs a regulator-led industry rollout (March 2026).",
              s=["con"], lc="open", st="new", ay="Apr 2025", o="B", neo=[None, "Card network not stated."], src=[["Westpac NZ: HY25 result, May 2025", HY25], ["Westpac NZ: basic accounts, Mar 2026", BASIC]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "Business & agri", "blurb": "Westpac One for Business.", "div": "wnzl", "rev": "ibb", "products": [
            P("sme", "Small & medium business banking", "SME lending growing faster than the market for two years; business lending NZ$35.0 billion (+6%); about 40% of SME customers on the new Westpac One for Business platform, the rest by late 2026; pre-approved headroom lending.",
              s=["sme"], lc="borrow", st="new", o="B", neo=[1, "Business cards on Mastercard."], src=[["Westpac NZ: HY26 result, May 2026", HY26]]),
            P("startup", "Start-up lending", "A NZ$100 million commitment to lend to start-ups (October 2025), NZ$33 million lent by May 2026.",
              s=["sme"], lc="borrow", st="new", ay="Oct 2025", o="B", neo=[0, ""], src=[["Westpac NZ: start-up lending, Oct 2025", START], ["Westpac NZ: HY26 result, May 2026", HY26]]),
            P("agri", "Agribusiness & Sustainable Farm Loans", "More than NZ$5 billion of discounted Sustainable Business and Sustainable Farm Loans since 2023; NZ$3.6 billion of farm loans in 18 months to September 2024, 43% of agri term lending.",
              s=["agri"], lc="borrow", o="B", neo=[0, ""], src=[["Westpac NZ: HY26 result, May 2026", HY26], ["Westpac NZ: FY24 result, Nov 2024", FY24]]),
        ]},
        {"id": "4.4", "ic": "building", "name": "Institutional", "blurb": "Corporates and the NZ Branch.", "div": "branch", "rev": "ibb", "products": [
            P("institutional", "Institutional & corporate banking", "Corporate lending and capital markets in WNZL, with financial markets, trade finance and international payments from WBC's NZ Branch, whose scope the RBNZ Branch Standard will narrow from 2028.",
              s=["corp"], lc="borrow", st="flux", o="I", neo=[0, ""],
              mc="The parent already runs Mastercard's mobile virtual card for Australian corporates.",
              src=[["Westpac 2025 annual report", AR25]]),
        ]},
        {"id": "4.5", "ic": "coins", "name": "Wealth & insurance", "blurb": "KiwiSaver, Tower, Fidelity.", "div": "bt", "rev": "cbw", "products": [
            P("kiwisaver", "Westpac KiwiSaver Scheme", "Managed by BT Funds Management (NZ); six of eight funds in the top quartile for the year to March 2026; a High Growth Fund launched in September 2024.",
              s=["saver"], lc="grow", o="I", neo=[0, ""], src=[["Westpac NZ: HY26 result, May 2026", HY26], ["Westpac NZ: FY24 result, Nov 2024", FY24]]),
            P("insurance", "Insurance (Tower & Fidelity Life)", "Tower underwrites new house, contents and car cover from 1 July 2026, with property hazard data in the app; Fidelity Life underwrites LifeProtect life and income cover.",
              s=["home", "con"], lc="beyond", st="new", ay="Jul 2026", o="P", at="Tower, Fidelity Life", neo=[0, ""], src=[["Westpac NZ: Tower live, Jul 2026", TOWER26], ["Westpac NZ: Fidelity Life guide, Jun 2025", FIDELITY]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the Westpac One app and online banking, the joint-largest branch network of the big four plus banking vans, NZ-based contact centres, and partners from Air New Zealand to Dosh and POLi.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Digital & contact centres", "blurb": "Westpac One, NZ-based calls.", "div": "wnz", "rev": "cbw", "products": [
            P("app", "Westpac One digital banking", "App and online banking for personal and business customers: card controls, Confirmation of Payee, insurance quotes with hazard data, fee-free international transfers; online home-loan refixing up more than 50% in six months.",
              s=["con", "sme", "home"], lc="everyday", o="B", neo=[0, ""], src=[["Westpac NZ: banking vans, Nov 2025", VANS], ["Westpac NZ: Tower live, Jul 2026", TOWER26]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & vans", "blurb": "Joint-largest network.", "div": "wnz", "rev": "cbw", "products": [
            P("branches", "Branches, vans & community bankers", "The joint-largest branch network of the big four, open 9.30am to 4.30pm; community banking vans in 15 towns across Northland, Southland and Canterbury, and community banker sites in libraries.",
              s=["con", "agri"], lc="open", st="new", o="B", neo=[0, ""], src=[["Westpac NZ: banking vans, Nov 2025", VANS], ["Westpac NZ: HY26 result, May 2026", HY26]]),
            P("contact", "Contact centres & care team", "All contact centres are in New Zealand, now on Microsoft CCaaS; a cards contact centre adds controls for customers who do not bank digitally.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["Westpac NZ: Microsoft CCaaS, Apr 2026", CCAAS], ["Westpac NZ: card controls, Oct 2025", GAMB]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "Air NZ, Dosh, fintechs.", "div": "partners", "rev": "cbw", "products": [
            P("partners", "Partners & fintechs", "Air New Zealand for loyalty, Dosh for home loans, POLi and accredited fintechs on Westpac's APIs, and mortgage advisers.",
              s=["con", "home"], lc="open", o="P", at="Air New Zealand, Dosh, POLi", neo=[0, ""], src=[["Dosh: home loans, Mar 2025", DOSH], ["NZ Adviser: POLi, Jul 2025", POLI]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Westpac NZ", "blurb": "An all-Mastercard issuer since 2014.", "products": [
        P("mcatwestpac", "Mastercard at Westpac NZ", "While its Australian parent went Visa-only in 2013, Westpac NZ signed a five-year Mastercard partnership in 2014 and in July 2026 still issues only Mastercard: debit (with EFTPOS), the Airpoints, hotpoints and Fee Free credit range, and business cards. No renewal announcement or joint Mastercard services were found ⚠.",
          s=["con"], div="wnz", rev="central", mc="The relationship this map is drawn for.",
          src=[["interest.co.nz: Mastercard deal, Apr 2014", MC14], ["Westpac NZ: credit card key information, Jul 2026", CCKEY]]),
    ]},
    {"id": "pillar-market", "name": "NZ payments", "blurb": "Caps, EFTPOS, open banking.", "products": [
        P("market", "The New Zealand market", "Interchange caps cut from 1 December 2025 (credit 0.3% in person) and extended to foreign cards from 1 May 2026; a surcharge ban stalled; fee-free EFTPOS switched by Paymark, now going to Cuscal; open banking regulated by MBIE after the API Centre closed on 30 September 2026.",
          s=["con"], div="wnz", rev="central", src=[["EFTPOS NZ: interchange caps, May 2026", IFEE], ["EFTPOS NZ: surcharge ban, Mar 2026", SURCH], ["API Centre: closure, 2026", APICLOSE]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
