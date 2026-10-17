"""FirstRand's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the results for the year to 30 June 2026
(10 September 2026) and the pre-close update (23 June 2026). FNB's product pages could not be read (bot wall),
so card networks for FNB's own cards are inferred from its Visa relationship and marked ⚠. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

FY26MR = "https://www.firstrand.co.za/media/investors/reports/fsr-results-media-release-June-2026.pdf"
FY26P = "https://www.firstrand.co.za/media/investors/reports/fsr-results-presentation-june-2026.pdf"
FY26B = "https://www.firstrand.co.za/media/investors/reports/fsr-analysis-of-financial-results-booklet-june-2026.pdf"
PRECLOSE = "https://www.firstrand.co.za/media/investors/presentations/pre-close-investor-update-23-June-2026.pdf"
MGMT = "https://www.firstrand.co.za/the-group/management-and-board/"
OWN = "https://www.firstrand.co.za/the-group/ownership-and-legal-structure/"
FNBCEO = "https://www.businessday.co.za/companies/2026-03-30-breaking-news-fnb-names-lytania-johnson-ceo-in-major-shake-up"
VISA25 = "https://it-online.co.za/?p=306980"
VISAWC = "https://www.itnewsafrica.com/gadgets/fnb-and-visa-kick-off-fifa-world-cup-2026-sponsorship/"
GLOBBA = "https://businessreport.co.za/companies/2025-11-11-fnb-mastercard-unite-to-advance-africas-cross-border-payments-with-launch-of-globba/"
QR19 = "https://www.electronicpaymentsinternational.com/news/fnb-qr-code-payment-service"
PNP = "https://businessreport.co.za/companies/2026-05-01-fnb-and-pick-n-pay-partner-to-deliver-r600-million-in-rewards-to-south-africans/"
NAVI = "https://www.itnewsafrica.com/2026/04/fnb-upgrades-navi-virtual-assistant-to-strengthen-advisor-led-services/"
OPTASIA = "https://www.timeslive.co.za/news/business/2026-03-26-firstrand-increases-stake-in-optasia-to-261/"
HSBC = "https://www.ecofinagency.com/news-finances/1106-47217-firstrand-to-acquire-hsbcs-clients-and-assets-in-south-africa"
ALDSALE = "https://www.mpamag.com/uk/news/general/nationwide-and-investec-among-bidders-circling-aldermore-sale/589814"
APPLE = "https://www.imore.com/south-african-bank-fnb-adds-support-apple-pay"
GWALLET = "https://www.itweb.co.za/article/sa-banks-embrace-google-wallet-in-contactless-payment-drive/rxP3jMBEmpY7A2ye"
WALLETS = "https://fnb.co.za/ways-to-bank/digital/partner-wallets.html"
SPEEDEE = "https://fnb.co.za/business-banking/merchant-services/speedeeapp.html"
SPEEDPT = "https://www.engineeringnews.co.za/article/fnb-launches-upgraded-payments-business-support-system-2026-03-04"
NAMCARD = "https://www.fnbnamibia.com.na/downloads/namibia/carddisclosures.pdf"
JUSTMONEY = "https://www.justmoney.co.za/products/fnb-private-clients-credit-card"
STITCH = "https://stitch.money/blog/real-time-payments-in-south-africa-the-state-of-payshap-in-2026"
PASA = "https://thecondia.com/south-africa-dissolves-pasa-payinc-sarb/"
NPS = "https://www.resbank.co.za/content/dam/sarb/publications/media-releases/2026/nps-transition.pdf"
DCS = "https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/regulation-oversight-and-supervision/document-for-comments/Domestic%20scheme%20feasibility%20paper%20-%20version%20sent%20to%20stakeholders%20-%201%20March%202021.pdf"
SABRIC = "https://www.sabric.co.za/?p=4450"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · ownership · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a R546 billion listed group earning R44.5 billion from South Africa and broader Africa at a 24.9% ROE, a UK business being sold after a £518 million motor-finance provision, new leaders at FNB, and a stake in Optasia.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "R44.5bn continuing, ROE 24.9%.", "div": "frg", "rev": "centre", "products": [
            P("balance", "Balance sheet & earnings", "Year to 30 June 2026: continuing normalised earnings of R44.5 billion (up 13%) at an ROE of 24.9%; R39.7 billion (down 5%, ROE 18.3%) including the UK motor provision. Core lending advances R1,374 billion, CET1 13.9%, a record dividend of 539 cents, and 51,712 employees. ROE target raised to 21–26%.",
              s=["corp"], neo=[0, ""], src=[["FY2026 media release", FY26MR], ["FY2026 results presentation", FY26P]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & ownership", "blurb": "Vilakazi; PIC holds 15.7%.", "div": "frg", "rev": "centre", "products": [
            P("leadership", "Board & executive", "Chair Johan Burger, CEO Mary Vilakazi and CFO Markos Davias (both since April 2024); Lytania Johnson became FNB CEO on 1 April 2026 ⚠, Emrie Brown runs RMB, Muneer Ismail commercial and corporate banking, Sizwe Nxedlana private banking and wealth, Gert Kruger is COO and Kevin Mitchell Chief Digital Officer.",
              s=["corp"], st="flux", neo=[0, ""], src=[["FirstRand: management and board", MGMT], ["BusinessDay: FNB CEO, Mar 2026", FNBCEO]]),
            P("owners", "Ownership & listing", "Listed on the JSE (FSR); market value R545.6 billion at 30 June 2026, up 28%. No controlling shareholder: the Public Investment Corporation held 15.7%, BEE partners 4.9%, BlackRock 3.0% and Old Mutual 2.7% at June 2025; 53% of shares held in South Africa. FNB's roots go back to 1838 ⚠.",
              s=["corp"], o="I", neo=[0, ""], src=[["FY2026 results booklet", FY26B], ["FirstRand: ownership", OWN]]),
        ]},
        {"id": "1.3", "ic": "target", "name": "Strategy, tech & deals", "blurb": "Africa focus, AI, Optasia.", "div": "frg", "rev": "centre", "products": [
            P("strategy", "Africa focus & new targets", "Capture the largest share of economic profit in South Africa and grow in eight broader-Africa markets; ROE target 21–26% and high-single to low-double-digit earnings growth guided for the year to June 2027.",
              s=["corp", "afr"], st="new", ay="Sep 2026", neo=[0, ""], src=[["FY2026 media release", FY26MR], ["FY2026 results booklet", FY26B]]),
            P("tech", "Platform, data & AI", "FNB invests in technology platforms, data, digitisation and AI to improve service and decisions; renewed large foreign-currency technology contracts in the year; platform modernisation under way in Ghana.",
              s=["corp"], neo=[0, ""], src=[["FY2026 results booklet", FY26B]]),
            P("optasia", "Optasia stake", "20.1% bought at Optasia's 2025 listing and raised to 26.1% on 25 March 2026 (about R1.48 billion ⚠); Optasia's credit decisioning powers an FNB airtime advance about to launch.",
              s=["con"], o="P", at="Optasia", st="new", ay="Mar 2026", neo=[0, ""], src=[["TimesLIVE: Optasia stake, Mar 2026", OPTASIA], ["FY2026 results presentation", FY26P]]),
            P("hsbc", "HSBC South Africa", "HSBC's South African corporate and investment clients moved to RMB: approved June 2025 ⚠, integration completed in the year with 444 entities transferred.",
              s=["corp"], o="A", at="HSBC", ay="Jun 2025", neo=[0, ""], src=[["Ecofin: HSBC clients, Jun 2025", HSBC], ["FY2026 results presentation", FY26P]]),
        ]},
        {"id": "1.4", "ic": "flag", "name": "UK exit", "blurb": "Aldermore for sale.", "div": "aldermore", "rev": "uk", "products": [
            P("ukexit", "Aldermore & MotoNovo", "Owned since 2018; exit announced April 2026 and shown as discontinued. Normalised earnings £156 million (down 11%) before a further £518 million FCA motor-redress provision. Binding offers due by end-December 2026; press names Nationwide, Investec and CVC with JC Flowers among bidders ⚠.",
              s=["corp"], o="A", st="flux", ay="Apr 2026", neo=[0, ""], src=[["FY2026 results booklet", FY26B], ["Pre-close update, Jun 2026", PRECLOSE], ["MPA: Aldermore bidders", ALDSALE]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: 1.4 billion card purchases on FNB cards (Visa ⚠) including 6.3 million virtual cards and fleet cards, partner wallets, a 1.2-billion-transaction acquiring estate, PayShap as the default instant payment, eWallet Send Money, and Globba on Mastercard Move.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Cards", "blurb": "1.39bn card transactions; Visa ⚠.", "div": "fnb", "rev": "fnb", "products": [
            P("cards", "FNB debit & credit cards", "Debit and credit cards from Aspire to Premier, Private Clients and the metal Private Wealth card: 1.39 billion card-issuing transactions in the year (up 7%), card fees of R4.0 billion and card-issuing income up 15%, partly offset by higher association charges. Issued on Visa ⚠ (a relationship since 1966).", short="Cards (Visa ⚠)",
              s=["con", "priv"], lc="everyday", o="P", at="Visa", neo=[0, "Visa ⚠."],
              mc="Scheme costs are rising for FNB; any issuing conversation starts against a 60-year Visa tie.",
              src=[["FY2026 results booklet", FY26B], ["IT-Online: FNB and Visa renew, Oct 2025", VISA25], ["JustMoney: Private Clients card, Jan 2026", JUSTMONEY]]),
            P("virtual", "Virtual cards", "6.3 million activated virtual cards (up 7%) with transaction values up 47% to R101 billion, used for safer e-commerce and to cut fraud. Network as for FNB's cards ⚠.",
              s=["con", "priv"], lc="everyday", o="B", neo=[0, "Visa ⚠."], src=[["FY2026 results booklet", FY26B]]),
            P("fleet", "Petro card & Fleet Services", "Fuel and fleet cards for businesses; FNB Namibia's linked Petro Card carries Visa's assistance service ⚠ SA network not read.",
              s=["sme", "driver"], lc="move", o="P", at="Visa", neo=[0, "Visa ⚠."], src=[["FNB Namibia: card disclosures", NAMCARD]]),
        ]},
        {"id": "2.2", "ic": "smartphone", "name": "Wallets & tokens", "blurb": "60%+ contactless.", "div": "fnb", "rev": "fnb", "products": [
            P("wallets", "Apple Pay, Google Pay, Samsung Pay & wearables", "Garmin Pay and Fitbit Pay with Visa (2018), Samsung Pay (2019 ⚠), Apple Pay (March 2021) and Google Pay (2022; replaced Fitbit Pay in July 2024 ⚠). More than 60% of card-present transactions are contactless; digital-wallet values rose 36% in the year.",
              s=["con", "priv"], lc="everyday", o="P", at="Apple, Google, Samsung, Visa", neo=[0, "Visa-issued tokens ⚠."],
              src=[["IT-Online: FNB and Visa renew, Oct 2025", VISA25], ["iMore: Apple Pay at FNB", APPLE], ["ITWeb: Google Wallet in SA", GWALLET], ["FNB: partner wallets", WALLETS], ["FY2026 results presentation", FY26P]]),
        ]},
        {"id": "2.3", "ic": "store", "name": "Merchant acquiring", "blurb": "1.16bn transactions.", "div": "fnb", "rev": "fnb", "products": [
            P("acquiring", "SpeedPoint & merchant services", "1.16 billion card-acquiring transactions (up 5%) and billable devices up 9%, but commission and rental income fell 7% as FNB repriced to defend clients. An upgraded SpeedPoint platform (March 2026 ⚠) takes cards, wallets and PayShap.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."],
              mc="A big acquiring estate under margin pressure: room for acquirer risk and data services.",
              src=[["FY2026 results booklet", FY26B], ["Engineering News: SpeedPoint, Mar 2026", SPEEDPT]]),
            P("speedee", "SpeedeeApp", "Turns an Android phone into a card terminal through the FNB App, with no hardware or rental.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network ⚠."], src=[["FNB: SpeedeeApp", SPEEDEE]]),
            P("scantopay", "Scan to Pay QR", "QR payments for consumers and merchants inside the FNB App, launched January 2019 on Mastercard's Masterpass: FNB was the first SA bank to do this ⚠ current status.",
              s=["con", "sme"], lc="move", ay="Jan 2019", o="P", at="Mastercard", neo=[3, "Masterpass ⚠ status."], src=[["EPI: FNB and Mastercard QR, Jan 2019", QR19]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "Instant payments", "blurb": "PayShap by default.", "div": "fnb", "rev": "fnb", "products": [
            P("payshap", "PayShap", "FNB made PayShap, the PayInc real-time rail, its default instant payment; FNB's PayShap volumes rose more than eight times in a year. Industry-wide about 45 million PayShap payments a month by late 2025, 80% under R500.",
              s=["con", "sme"], lc="move", st="new", o="P", at="PayInc", neo=[0, "Domestic account-to-account rail."],
              mc="Low-value domestic payments are moving off cards onto PayShap.",
              src=[["FY2026 results booklet", FY26B], ["Stitch: PayShap in 2026", STITCH]]),
            P("instantpay", "FNB Instant Pay", "South Africa's first peer-to-peer instant payment (2022), built on Visa Direct; more than a million transactions in its first year.",
              s=["con"], lc="move", ay="2022", o="P", at="Visa", neo=[0, "Visa Direct."], src=[["IT-Online: FNB and Visa renew, Oct 2025", VISA25]]),
        ]},
        {"id": "2.5", "ic": "send", "name": "eWallet & Send Money", "blurb": "68m sends a year.", "div": "fnb", "rev": "fnb", "products": [
            P("ewallet", "eWallet", "Money sent to any phone number and drawn at ATMs without a card: about 68 million transactions in the year, the market leader in send-money; 7.77 million eWallets, 6.23 million of them held by people with no other FNB product.",
              s=["con"], lc="move", o="B", neo=[0, "FNB's own."], src=[["FY2026 results booklet", FY26B]]),
        ]},
        {"id": "2.6", "ic": "earth", "name": "Cross-border", "blurb": "Globba on Mastercard Move.", "div": "fnb", "rev": "fnb", "products": [
            P("globba", "Globba", "Person-to-person transfers from the FNB and RMB Private Banking apps to 120+ countries (45 in Africa), to bank accounts, wallets and cash pick-up, launched 11 November 2025 on Mastercard Move; roll-out across FNB's African network planned.", short="Globba (Mastercard Move)",
              s=["con", "priv", "afr"], lc="move", st="new", ay="Nov 2025", o="P", at="Mastercard", neo=[3, "Mastercard Move."],
              mc="Mastercard's newest and clearest foothold at FNB.",
              src=[["Business Report: Globba, Nov 2025", GLOBBA]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: virtual cards against card-not-present fraud, the NAVi AI assistant, eBucks rewards with Pick n Pay, prepaid airtime and electricity, and Optasia's credit scoring.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Virtual cards, monitoring.", "div": "fnb", "rev": "fnb", "products": [
            P("fraud", "Fraud prevention", "Virtual cards for online spending (R101 billion) to reduce fraud outcomes, in a market where card-not-present fraud leads card losses ⚠. No public Mastercard fraud tool at FNB.",
              s=["con", "sme"], lc="everyday", o="B", neo=[None, "Nothing public."],
              mc="Scam and identity scoring would meet a known card-not-present problem.",
              src=[["FY2026 results booklet", FY26B], ["SABRIC: 2025 crime statistics", SABRIC]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI assistant", "blurb": "NAVi.", "div": "fnb", "rev": "fnb", "products": [
            P("navi", "NAVi", "A virtual assistant in the FNB App from late 2025, upgraded in April 2026 to support advisors during customer conversations, with guided next-best actions planned.",
              s=["con", "priv"], lc="everyday", st="new", ay="Apr 2026", o="B", neo=[0, ""],
              mc="Agentic payments are untouched ground; Agent Pay could sit behind NAVi.",
              src=[["ITNewsAfrica: NAVi, Apr 2026", NAVI]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "eBucks rewards", "blurb": "R600m with Pick n Pay.", "div": "ebucks", "rev": "fnb", "products": [
            P("ebucks", "eBucks", "Rewards for using FNB's banking, insurance and investment products, spent on travel, Lotto, electricity and offers; Pick n Pay became the primary retail partner in April 2025, with more than R600 million of rewards in a year and up to 30% back on Pick n Pay asap!.",
              s=["con", "priv", "sme"], lc="grow", o="B", at="Pick n Pay", neo=[0, ""],
              mc="Card-linked offers and merchant data could extend eBucks.",
              src=[["FY2026 results booklet", FY26B], ["Business Report: FNB and Pick n Pay, May 2026", PNP]]),
        ]},
        {"id": "3.4", "ic": "coins", "name": "Value-added services", "blurb": "R3.1bn VAS income.", "div": "fnb", "rev": "fnb", "products": [
            P("vas", "Airtime, data & electricity", "Prepaid airtime, data, electricity and vouchers in the app; value-added services income up 14% to R3.1 billion. An airtime advance using Optasia's credit decisioning is about to launch.",
              s=["con"], lc="beyond", o="B", neo=[0, ""], src=[["FY2026 results booklet", FY26B], ["FY2026 results presentation", FY26P]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: FNB accounts for 12.8 million, home loans and nav»Home, personal loans, the largest SME lending book, FNB Connect mobile, insurance and investments, WesBank vehicle finance, RMB's corporate and investment bank, and FNB in eight African markets.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Accounts & private", "blurb": "12.8m active customers.", "div": "fnb", "rev": "fnb", "products": [
            P("accounts", "FNB retail accounts", "8.89 million South African retail customers (7.09 million personal, 1.80 million private, up 8%); retail deposits about R447 billion; stokvel deposits up 31% to R5.7 billion.",
              s=["con"], lc="everyday", neo=[0, "Visa cards ⚠."], src=[["FY2026 results booklet", FY26B], ["FY2026 results presentation", FY26P]]),
            P("private", "FNB Private & Private Wealth", "Private banking for 1.80 million customers, with NIR per customer up 8% and PBT up 12%; private-wealth credit card in metal ⚠.",
              s=["priv"], lc="everyday", neo=[0, "Visa ⚠."], src=[["FY2026 results presentation", FY26P]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Home & personal lending", "blurb": "R296bn mortgages.", "div": "fnb", "rev": "fnb", "products": [
            P("homeloans", "Home loans & nav»Home", "Residential mortgages of R296 billion (up 5%), production up 20%; nav»Home has placed about 65,000 homes and R81 billion of lending since launch, 14% of new home-loan origination.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["FY2026 results presentation", FY26P], ["FY2026 results booklet", FY26B]]),
            P("loans", "Personal loans & card credit", "Retail unsecured lending of R112 billion (up 7%), personal-loan production up 21%, card advances up 4%.",
              s=["con"], lc="borrow", neo=[0, "Visa cards ⚠."], src=[["FY2026 results presentation", FY26P], ["FY2026 results booklet", FY26B]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "Business & commercial", "blurb": "Largest SME lender.", "div": "fnb", "rev": "fnb", "products": [
            P("commercial", "FNB Business & Commercial", "1.38 million commercial customers; commercial deposits R563 billion (up 13%); the largest SME lender with a R49 billion business-banking book; NIR squeezed by card scheme fees and acquiring margins.",
              s=["sme"], lc="everyday", neo=[0, ""],
              mc="Business cards and payment controls for a large SME base.",
              src=[["FY2026 results presentation", FY26P], ["FY2026 results booklet", FY26B]]),
        ]},
        {"id": "4.4", "ic": "hand-coins", "name": "Insurance, investments & Connect", "blurb": "APE +22%; R3bn mobile.", "div": "fnb", "rev": "fnb", "products": [
            P("insure", "Insurance & investments", "Life and short-term insurance on FirstRand's own licences (new business APE R4.2 billion, up 22%; short-term profitable for the first time), and Ashburton and wealth assets under management up about a quarter ⚠.",
              s=["con", "priv"], lc="grow", neo=[0, ""], src=[["FY2026 results presentation", FY26P]]),
            P("connect", "FNB Connect", "FNB's mobile virtual network operator: more than a million MVNO customers, about three million using Connect services, R26 billion of transactions and revenue up 14% to more than R3 billion.",
              s=["con"], lc="beyond", o="B", neo=[0, ""], src=[["FY2026 results booklet", FY26B], ["FY2026 media release", FY26MR]]),
        ]},
        {"id": "4.5", "ic": "target", "name": "WesBank", "blurb": "Record R59.4bn production.", "div": "wesbank", "rev": "wesbank", "products": [
            P("wesbank", "Vehicle & asset finance", "Record production of R59.4 billion (up 18%), vehicle finance advances of R143 billion (up 15%), new Chinese manufacturer partners; PBT broadly flat at R3.1 billion.",
              s=["driver"], lc="borrow", neo=[0, ""],
              mc="Fleet and fuel cards for a large vehicle-finance book are open ground.",
              src=[["FY2026 results presentation", FY26P], ["FY2026 media release", FY26MR]]),
        ]},
        {"id": "4.6", "ic": "factory", "name": "RMB", "blurb": "PBT R17.6bn, ROE 23%.", "div": "rmb", "rev": "rmb", "products": [
            P("rmb", "RMB corporate & investment banking", "Investment banking, Global Markets (revenue up 42%), transactional banking and private equity; PBT up 15% to R17.6 billion at a 23.0% ROE; HSBC's South African clients absorbed.",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="Commercial and virtual cards for HSBC's former multinational clients.",
              src=[["FY2026 media release", FY26MR], ["FY2026 results presentation", FY26P]]),
        ]},
        {"id": "4.7", "ic": "globe", "name": "FNB broader Africa", "blurb": "Eight markets.", "div": "africa", "rev": "fnb", "products": [
            P("africa", "FNB in broader Africa", "Subsidiaries in eight African countries, 2.50 million customers (up 6%) and PBT of R3.8 billion (up 3%): Namibia, Botswana and Eswatini are systemic banks; Zambia (PBT up 50%) and Ghana are scaling. Namibia cards on Visa; other markets not checked ⚠.",
              s=["afr"], lc="everyday", neo=[0, "Visa in Namibia; others ⚠."],
              mc="Globba's planned roll-out runs through these markets.",
              src=[["FY2026 results booklet", FY26B], ["FY2026 results presentation", FY26P], ["FNB Namibia: card disclosures", NAMCARD]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach FirstRand: the FNB App for 8.2 million digitally active customers, branches, ATMs and agencies, shelves in Pick n Pay and Boxer, and advisors, dealers and nav» platforms.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "FNB App & online", "blurb": "782m app transactions.", "div": "fnb", "rev": "fnb", "products": [
            P("app", "FNB App, online & USSD", "8.16 million digitally active customers; 782 million app transactions (up 10%) and 951 million digital transactions in all; nav»Money used by more than 6.5 million.",
              s=["con", "priv", "sme"], lc="everyday", neo=[0, ""], src=[["FY2026 results booklet", FY26B]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches, ATMs & agencies", "blurb": "+125 agencies in SA.", "div": "fnb", "rev": "fnb", "products": [
            P("branches", "Branches, ATMs & AgencyPlus", "13 new branches in South Africa and 5 in broader Africa; AgencyPlus points up 125 in South Africa and 840 in broader Africa; ATM transactions down 5% to 265 million.",
              s=["con", "afr"], lc="everyday", neo=[0, ""], src=[["FY2026 results booklet", FY26B]]),
            P("retailpartners", "Pick n Pay & Boxer", "Banking points inside Pick n Pay and Boxer stores, strengthened in the year, alongside eBucks offers.",
              s=["con"], lc="open", o="P", at="Pick n Pay", st="new", neo=[0, ""], src=[["FY2026 results presentation", FY26P], ["Business Report: FNB and Pick n Pay, May 2026", PNP]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Advisors & dealers", "blurb": "Advisors, dealers, nav».", "div": "frg", "rev": "fnb", "products": [
            P("advisors", "Advisors, relationship managers & dealers", "Advisor-led insurance and investment sales (advisor APE up 44%), relationship managers for business clients, and WesBank's motor dealers and manufacturers.",
              s=["priv", "driver", "sme"], lc="open", neo=[0, ""], src=[["FY2026 results presentation", FY26P], ["FY2026 results booklet", FY26B]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at FirstRand", "blurb": "Globba, QR, acceptance.", "products": [
        P("mcatfnb", "Mastercard at FirstRand", "FNB has been a Visa bank since 1966 and renewed with Visa in October 2025; its cards are Visa ⚠ and Instant Pay runs on Visa Direct. Mastercard runs Globba, FNB's cross-border transfers on Mastercard Move (November 2025), and the Masterpass rail behind Scan to Pay QR (2019), and its cards are accepted across FNB's acquiring estate.",
          s=["con"], div="frg", rev="fnb", mc="The relationship this map is drawn for.",
          src=[["IT-Online: FNB and Visa renew, Oct 2025", VISA25], ["Business Report: Globba, Nov 2025", GLOBBA], ["EPI: FNB and Mastercard QR, Jan 2019", QR19]]),
    ]},
    {"id": "pillar-market", "name": "South African payments", "blurb": "PayShap, PayInc, SARB.", "products": [
        P("market", "The South African market", "PASA is being wound down; the SARB took over card interoperability from 11 August 2026 ⚠ and is taking 50% of PayInc (formerly BankservAfrica), which runs PayShap, EFT and DebiCheck. PayShap has passed R100 billion across 136 million payments. There is no domestic card scheme; the SARB studied one in 2021.",
          s=["con"], div="frg", rev="fnb",
          src=[["The Condia: PASA and PayInc, Jun 2026", PASA], ["SARB: NPS transition, Aug 2026", NPS], ["Stitch: PayShap in 2026", STITCH], ["SARB: domestic card scheme paper, 2021", DCS]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
