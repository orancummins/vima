"""MCB Group's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the FY 2025/26 results (year to 30 June 2026, announced
28 September 2026) and the 2025 annual report (year to 30 June 2025). ``neo`` is the Mastercard lens: [depth, note],
where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

GMS = "https://mcbgroup.com/docs/default-source/investor-centre/group-management-statement/mcbg-gms-q4-2025-26.pdf"
ECP = "https://mcbgroup.com/docs/default-source/investor-centre/earnings-call-presentation/q4-earnings-call-presentation-2025-26.pdf"
RES = "https://mcbgroup.com/news/article/profits-of-rs-20.1-billion-for-fy-2025-2026"
AR25 = "https://mcbgroup.com/docs/default-source/investor-centre/annual-report-2025/annual-report-2025.pdf"
BOARD = "https://mcbgroup.com/board"
GLANCE = "https://mcb.mu/personal/about-us/at-a-glance"
CARDS = "https://mcb.mu/personal/cards"
DEBIT = "https://mcb.mu/personal/cards/mcb-debit-card"
CLASSIC = "https://mcb.mu/personal/cards/classic-credit-card"
PRIMO = "https://mcb.mu/personal/cards/mastercard-primo-credit-card"
SIG = "https://mcb.mu/personal/cards/visa-signature"
AMEX = "https://mcb.mu/personal/cards/american-express/american-express-gold"
AMEXMU = "https://www.americanexpress.com/en-mu/network/business/"
CORP = "https://mcb.mu/corporate/payment-cash/pay/mastercard-corporate-credit-card"
FLEET = "https://mcb.mu/sme/pay/cards/fleetman-card"
JUICE = "https://mcb.mu/personal/ways-to-bank/juice"
APPLE = "https://mcbgroup.com/news/article/mcb-brings-apple-pay-to-customers"
ECO = "https://mcbgroup.com/news/article/mcb-expands-its-payments-ecosystem-to-offer-greater-choice--convenience-and-seamless-experiences-for-customers"
TECHISH = "https://tech-ish.com/2026/05/21/apple-pay-mauritius-launch-kenya-still-waiting/"
JTAP = "https://fr.allafrica.com/stories/202412060500.html"
QR67 = "https://fr.allafrica.com/stories/202601200361.html"
UPI18 = "https://mcbgroup.com/news/article/mcb-first-acquiring-bank-of-unionpay-cards-in-mauritius"
UPI23 = "https://mcb.mu/private-wealth/news/mcb-and-upi-celebrate-15-years-of-successful-collaboration"
MC16 = "https://www.electronicpaymentsinternational.com/?p=39526"
MC15 = "https://www.electronicpaymentsinternational.com/?p=40505"
CASHP = "https://cashpassport.mastercard.com/media/228209/mcb-privacy-policy_20220613.pdf"
MAUCAS = "https://www.bom.mu/sites/default/files/maucas_-_english_leaflet.pdf"
BOM19 = "https://www.bis.org/review/r190816g.htm"
FINTECH = "https://www.capmad.com/post/mauritius-unveils-its-national-fintech-strategy-20262030-to-modernise-public-and-private-payments"
MV = "https://www.mcb.mv/notices"
SC = "https://www.mcb.sc/"
MG = "https://www.mcb.mg/"
ETG = "https://mcbgroup.com/news/article/mcb-and-etg-turn-digital-trade-into-reality"
TRADE1B = "https://mcbgroup.com/news/article/mcb-announces-a--1-billion-envelope-"
SUST25 = "https://mcbgroup.com/news/article/mcb-strengthens-its-commitment-and-increases-its-sustainable-finance-facility-to-rs-25-billion"
MBA = "https://mcbgroup.com/news/article/thierry-hebraud-elected-as-chairperson-of-the-mba"
MICRO = "https://mcbgroup.com/news/article/mcb-microfinance--10-years-of-empowering-entrepreneurship"
NEWS = "https://mcbgroup.com/news"
PEACH = "https://www.peachpayments.com/mcb-juice"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · heritage · Vision 2030", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Rs 20.1 billion of profit in FY26, about half of Mauritius' rupee deposits, a bank dating from 1838, a footprint in 11 countries, cloud and AI investment, and Vision 2030.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Rs 20.1bn profit, ROE 16%.", "div": "group", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Profit to shareholders of Rs 20.1 billion in the year to 30 June 2026 (+11.3%), operating income Rs 47.1 billion, ROE 16.0%, cost-to-income 38.1%; total assets Rs 1,283 billion, loans Rs 500 billion, customer deposits Rs 881 billion, CAR 20.3%. About 56% of MCB Ltd's profit is earned abroad.",
              s=["corp"], neo=[0, ""], src=[["FY26 group management statement", GMS], ["FY26 results release, Sep 2026", RES]]),
            P("ratings", "Listing, ownership & ratings", "The largest company on the Stock Exchange of Mauritius, about Rs 112 billion and 36% of the SEMDEX at June 2025 ⚠ not updated; about 24,000 shareholders with no controlling owner; Moody's Baa3 deposits and a domestic AAA from CARE Ratings.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025", AR25], ["MCB: at a glance", GLANCE]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Ng Tseung and Hebraud.", "div": "group", "rev": "group", "products": [
            P("leadership", "Board & executives", "Chairperson Jayananda Nirsimloo (from November 2024), Group Chief Executive Jean Michel Ng Tseung (since March 2023), Group CFO Dipak Chummun; Thierry Hebraud runs MCB Ltd and chairs the Mauritius Bankers Association (June 2026); Stephanie Ng Tseung is Head of Payments.",
              s=["corp"], neo=[0, ""], src=[["MCB Group: board", BOARD], ["Hebraud elected MBA chair, Jun 2026", MBA], ["L'Express: payment trends, Jan 2026", QR67]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & reach", "blurb": "Since 1838, 11 countries.", "div": "group", "rev": "group", "products": [
            P("heritage", "Heritage & market share", "Open since 1 September 1838 in Port Louis; about 39% of domestic credit and about 50% of rupee deposits; about 1.29 million group customers and 4,900 staff at June 2025; The Banker's African Bank of the Year 2024.",
              s=["con"], o="I", neo=[0, ""], src=[["MCB: at a glance", GLANCE], ["Annual report 2025", AR25]]),
            P("footprint", "Footprint", "Banks in Madagascar (80%), Seychelles and Maldives, 49.99% of BFCOI in Réunion and Mayotte, hubs in Johannesburg, Nairobi, Lagos, Paris and Dubai, and about 100 correspondent banks in Africa.",
              s=["afr", "isl"], neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Cloud, Calypso, AI.", "div": "group", "rev": "group", "products": [
            P("tech", "Cloud, platforms & AI", "A cloudification strategy, Calypso moved to Nasdaq's CapCloud, the MCB Wave FX trading platform, an AI strategy and machine-learning tools for staff; IT costs rose 19.2% in FY26 for cloud, cybersecurity and AI. No customer-facing AI product found ⚠.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025", AR25], ["FY26 group management statement", GMS]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Vision 2030", "blurb": "Home markets and Africa.", "div": "group", "rev": "group", "products": [
            P("strategy", "Vision 2030", "Launched June 2025: lead in the home markets, become a top-tier African corporate, investment and private bank, and win in the workplace. Home Markets earned Rs 22.1 billion (+15.8%) and African CIBPB Rs 24.9 billion (+10.8%) in FY26.",
              s=["corp", "afr"], st="new", ay="Jun 2025", neo=[0, ""], src=[["Annual report 2025", AR25], ["FY26 earnings call", ECP]]),
            P("deals", "Funding & deals", "A USD 400 million bond in London and a USD 450 million syndicated loan in FY26, a USD 1 billion African trade envelope (May 2026), and MCB Real Assets' majority of the Club Med resort at Pointe aux Canonniers.",
              s=["corp", "afr"], o="A", neo=[0, ""], src=[["FY26 group management statement", GMS], ["USD 1bn trade envelope, May 2026", TRADE1B], ["Annual report 2025", AR25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: a Mastercard debit card for the mass market, credit cards on Mastercard, Visa and Amex, prepaid on three networks, Visa SME debit and a Mastercard corporate card, acquiring for every network, MauCAS QR and instant transfers, and Juice Tap and Apple Pay.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Mastercard since at least 2015.", "div": "mcb", "rev": "retail", "products": [
            P("debit", "MCB Mastercard debit card", "The personal debit card in Mauritius is an MCB Mastercard Debit Card: contactless, with on/off controls for contactless, online and foreign use, and in Juice Tap and Apple Pay. About 675,000 were made contactless from October 2016, the first in Mauritius.", short="Debit (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard debit."],
              mc="Mastercard's anchor at MCB: the everyday card of Mauritius' largest bank.",
              src=[["MCB: debit card", DEBIT], ["EPI: contactless with Mastercard, Sep 2016", MC16], ["EPI: online debit, Nov 2015", MC15]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Mastercard, Visa and Amex.", "div": "mcb", "rev": "retail", "products": [
            P("credit", "Classic & Gold credit cards", "The Classic card comes as an MCB Mastercard or an MCB Visa, with up to 45 days interest-free and Sweet deals offers; the Gold card's network is not stated ⚠.", short="Credit (Mastercard or Visa)",
              s=["con"], lc="borrow", o="P", at="Mastercard, Visa", neo=[1, "Mastercard or Visa, customer's choice."], src=[["MCB: Classic credit card", CLASSIC], ["MCB: cards", CARDS]]),
            P("primo", "Mastercard Primo", "An entry credit card with a lower limit, Touch & Pay, Juice Tap, Apple Pay and MCB Secure for online shopping.", short="Primo (Mastercard)",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["MCB: Mastercard Primo", PRIMO]]),
            P("premium", "Visa Platinum & Visa Signature", "The premium tier is Visa: Signature brings LoungeKey with six visits a year, USD 750,000 travel cover, concierge and the Visa Luxury Hotel Collection.", short="Premium (Visa)",
              s=["aff"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="No World or World Elite card at MCB; SBM launched World Elite in Mauritius in 2019.",
              src=[["MCB: Visa Signature", SIG]]),
            P("amex", "American Express Green & Gold", "Amex cards issued by MCB, with Membership Rewards and Priority Pass through MCB Travel; MCB is also Amex's named merchant acquirer in Mauritius ⚠ exclusivity not stated.", short="Amex",
              s=["aff"], lc="borrow", o="P", at="American Express", neo=[0, "Amex."], src=[["MCB: American Express Gold", AMEX], ["Amex Mauritius: merchants", AMEXMU]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Prepaid", "blurb": "Visa, UnionPay, Cash Passport.", "div": "mcb", "rev": "retail", "products": [
            P("prepaid", "Visa prepaid card", "A reloadable Visa prepaid card for personal customers.", short="Prepaid (Visa)",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["MCB: cards", CARDS]]),
            P("upiprepaid", "UnionPay prepaid card", "In renminbi and US dollars since 2013, the first UnionPay prepaid card in Africa, part of a UnionPay partnership dating from 2010.", short="Prepaid (UnionPay)",
              s=["con"], lc="move", ay="2013", o="P", at="UnionPay", neo=[0, "UnionPay."], src=[["MCB: first UnionPay acquirer, Apr 2018", UPI18]]),
            P("cashpassport", "Cash Passport", "Prepaid cards issued by MCB as a Mastercard member, with Mastercard Prepaid Management Services as programme manager (policy dated June 2022) ⚠ current scope not public.",
              s=["con"], lc="move", st="unconf", o="P", at="Mastercard", neo=[3, "Mastercard's own prepaid programme ⚠."], src=[["MCB Cash Passport privacy policy, Jun 2022", CASHP]]),
        ]},
        {"id": "2.4", "ic": "briefcase-business", "name": "Business cards", "blurb": "Visa SME, Mastercard corporate.", "div": "mcb", "rev": "corporate", "products": [
            P("smedebit", "Visa Business Debit", "Business debit cards as a digital alternative to cheques: more than 21,000 SME debit cards issued by June 2025.", short="SME debit (Visa)",
              s=["sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Annual report 2025", AR25], ["MCB: cards", CARDS]]),
            P("corpcard", "Mastercard Corporate FCY credit card", "Corporate credit cards in USD, EUR, GBP and ZAR (launched FY 2024/25) with no conversion fees, Mastercard Flight Delay Pass, Priceless hotel offers and a USD 25,000 liability waiver.", short="Corporate FCY (Mastercard)",
              s=["corp", "afr"], lc="move", st="new", ay="FY 2024/25", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="A Mastercard foothold in the international corporate base MCB is building.",
              src=[["MCB: Mastercard corporate FCY card", CORP], ["Annual report 2025", AR25]]),
            P("fleetman", "Fleetman card", "A vehicle-tied fuel and maintenance card with spending limits, no PIN and a Vehicle Technical Report for each car; network not stated ⚠.",
              s=["sme", "corp"], lc="everyday", neo=[None, "Network not stated."], src=[["MCB: Fleetman card", FLEET]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acquiring", "blurb": "About 18,000 merchants.", "div": "mcb", "rev": "retail", "products": [
            P("acquiring", "Merchant acquiring", "The island's leading acquirer: about 18,000 merchants accepting card or MauCAS QR at end-2025, first UnionPay acquirer in Mauritius (2010), Amex acquiring, and Visa and Mastercard.",
              s=["sme", "corp"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["MCB and UnionPay: 15 years, Dec 2023", UPI23], ["L'Express: payment trends, Jan 2026", QR67]]),
            P("pos", "Android POS", "About 3,400 new Android terminals across Mauritius, Seychelles and Maldives to modernise acceptance and add Tap to Pay for SMEs.",
              s=["sme"], lc="move", st="new", o="B", neo=[1, "Accepts every network."], src=[["Annual report 2025", AR25], ["MCB payments ecosystem, May 2026", ECO]]),
            P("ecom", "Online payment gateway", "E-commerce acquiring with website checks at onboarding; MCB's e-commerce volumes rose 43% in FY 2024/25.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "QR & instant transfers", "blurb": "MauCAS QR up 67%.", "div": "juice", "rev": "retail", "products": [
            P("maucasqr", "MauCAS QR", "MCB has deployed the Bank of Mauritius' interoperable QR: QR payments rose 67% in 2025 against 4% for contactless cards.", short="MauCAS QR (domestic)",
              s=["con", "sme"], lc="move", o="P", at="Bank of Mauritius", neo=[0, "Domestic rail."],
              mc="The fastest-growing way to pay at MCB, and not a card.",
              src=[["L'Express: payment trends, Jan 2026", QR67], ["MCB payments ecosystem, May 2026", ECO]]),
            P("transfers", "Instant transfers on MauCAS", "Send money from Juice to any account, card or mobile number; MauCAS, the central bank's 24x7 switch, launched the Instant Payment System on 14 August 2019.",
              s=["con"], lc="move", o="P", at="Bank of Mauritius", neo=[0, "Domestic rail."], src=[["MCB Juice", JUICE], ["BoM: MauCAS launch, Aug 2019", BOM19], ["BoM: MauCAS leaflet", MAUCAS]]),
            P("remit", "International transfers", "Cross-currency transfers and remittances, SWIFT gpi tracking, and PayPal linking in Juice. No Mastercard Move or Visa Direct use found ⚠.",
              s=["con", "corp"], lc="move", o="B", neo=[0, "SWIFT and PayPal."],
              mc="Cross-border payouts are an open gap.",
              src=[["Annual report 2025", AR25], ["MCB Juice", JUICE]]),
        ]},
        {"id": "2.7", "ic": "smartphone", "name": "Wallets & tokens", "blurb": "Juice Tap, Apple Pay.", "div": "juice", "rev": "retail", "products": [
            P("juicetap", "Juice Tap", "NFC payments from Juice on Android and Huawei, launched with Visa in December 2024 with Mastercard to follow; Juice now holds Mastercard and Visa cards. About 13% of Visa cards were tokenised by June 2025, and Tap to Pay was 1.4% of transactions in 2025.",
              s=["con"], lc="everyday", st="new", ay="Dec 2024", o="P", at="Visa, Mastercard", neo=[1, "Visa first, then Mastercard."],
              mc="Visa got the launch; token growth is still ahead.",
              src=[["L'Express: Juice Tap with Visa, Dec 2024", JTAP], ["MCB Juice", JUICE], ["Annual report 2025", AR25]]),
            P("applepay", "Apple Pay", "Live from 19 May 2026 on MCB Visa and Mastercard credit and debit cards; MCB is the first Mauritian bank on Apple's list and Visa announced the launch.",
              s=["con", "aff"], lc="everyday", st="new", ay="May 2026", o="P", at="Apple, Visa, Mastercard", neo=[1, "Visa and Mastercard."],
              src=[["MCB brings Apple Pay, May 2026", APPLE], ["Tech-ish: Apple Pay in Mauritius, May 2026", TECHISH]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: selfie checks, card controls and 3-D Secure, host-to-host and SWIFT links for corporates, Juice as a checkout button, and MCB's own merchant offers.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security & identity", "blurb": "Selfie checks, card controls.", "div": "mcb", "rev": "retail", "products": [
            P("security", "Fraud & card security", "Juice registration with ID capture and a selfie plus two-factor authentication, on/off card controls, and MCB Secure for online card payments. No named fraud-scoring vendor found ⚠.",
              s=["con"], lc="everyday", o="B", neo=[1, "3-D Secure runs on the card networks ⚠."],
              mc="93% of online purchases go to foreign sites; fraud and identity tools have room.",
              src=[["Annual report 2025", AR25], ["MCB: debit card", DEBIT], ["L'Express: payment trends, Jan 2026", QR67]]),
            P("onboard", "Digital onboarding", "Self-onboarding on the website and MoKloud, finished in branch; SME accounts opened in about three days, 76% digitally.",
              s=["con", "sme"], lc="open", st="new", o="B", neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "3.2", "ic": "plug", "name": "APIs & connectivity", "blurb": "Host-to-host, Juice checkout.", "div": "mcb", "rev": "corporate", "products": [
            P("h2h", "Host-to-host & SWIFT", "Host-to-host and SWIFT connectivity, a SWIFT service bureau, bulk payments and the Global Trade Portal for corporates. No public open-banking API programme found ⚠.",
              s=["corp", "afr"], lc="move", o="B", neo=[0, ""], src=[["Annual report 2025", AR25]]),
            P("peach", "Juice at checkout", "Juice as a payment method at online checkouts through Peach Payments, at 1.5% plus MUR 3.50 for SMEs ⚠ undated page.",
              s=["sme"], lc="move", o="P", at="Peach Payments", neo=[0, "Account-to-account."], src=[["Peach Payments: MCB Juice", PEACH]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Offers & rewards", "blurb": "Sweet deals, lucky draws.", "div": "mcb", "rev": "retail", "products": [
            P("offers", "Offers, rewards & cashback", "Sweet deals merchant offers, privileges and lucky draws on MCB cards, Amex Membership Rewards, 10 cents to biodiversity for each card payment, and Visa cashback campaigns in Madagascar (1% then 2.6%, 2024–25).",
              s=["con", "isl"], lc="grow", o="B", neo=[0, "MCB's own; Visa in Madagascar."],
              mc="Card-linked offers could replace home-grown deals.",
              src=[["MCB: Classic credit card", CLASSIC], ["MCB: debit card", DEBIT], ["Annual report 2025", AR25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail and SME banking in Mauritius, corporate lending with a Rs 25 billion green line, an African corporate and investment bank built on commodity trade finance, three overseas banks, and wealth, markets and leasing.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Retail banking", "blurb": "Half of rupee deposits.", "div": "mcb", "rev": "retail", "products": [
            P("retail", "Accounts & loans", "Current, savings and multi-currency accounts, home loans (FY26 growth led by housing), personal, education and green loans; about half of Mauritius' rupee deposits.",
              s=["con"], lc="everyday", o="I", neo=[1, "Accounts come with a Mastercard debit card."], src=[["Annual report 2025", AR25], ["FY26 group management statement", GMS]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "SME banking", "blurb": "Overdrafts in three days.", "div": "mcb", "rev": "retail", "products": [
            P("sme", "Business Banking", "Express overdrafts in about three days, Lokal is Beautiful financing, payroll and leasing for micro, small and mid-sized firms.",
              s=["sme"], lc="borrow", o="B", neo=[0, "Visa business debit."], src=[["Annual report 2025", AR25]]),
            P("micro", "MCB Microfinance", "Ten years of microcredit for entrepreneurs in 2026.",
              s=["sme"], lc="borrow", o="B", neo=[0, ""], src=[["MCB Microfinance: 10 years, Jul 2026", MICRO]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate banking", "blurb": "Rs 25bn green line.", "div": "mcb", "rev": "corporate", "products": [
            P("corporate", "Corporate & institutional", "Lending, cash management and trade for Mauritian and regional corporates (loans up 5.7% in FY26) and a sustainable finance facility raised to Rs 25 billion (July 2026).",
              s=["corp"], lc="borrow", o="B", neo=[1, "Mastercard corporate card."], src=[["FY26 earnings call", ECP], ["Sustainable finance to Rs 25bn, Jul 2026", SUST25]]),
        ]},
        {"id": "4.4", "ic": "earth", "name": "African CIB", "blurb": "Over half of income.", "div": "mcb", "rev": "cibpb", "products": [
            P("cib", "African corporate & investment banking", "Commodity trade finance (about Rs 101 billion), natural resources, power and infrastructure and global corporates: loans up 37.4% in FY26, with deals for AXIAN Energy (USD 60 million) and Tolaram (USD 51 million).",
              s=["afr"], lc="borrow", o="B", neo=[0, ""],
              mc="Commercial and virtual cards could follow the trade flows.",
              src=[["FY26 earnings call", ECP], ["FY26 group management statement", GMS], ["MCB newsroom", NEWS]]),
            P("trade1b", "USD 1bn trade envelope & e-Bills", "A USD 1 billion envelope for African trade over four years (May 2026) and Africa's first electronic Bill of Exchange under Mauritian law, with ETG (September 2026).",
              s=["afr"], lc="move", st="new", ay="May 2026", o="P", at="ETG, Enigio", neo=[0, ""], src=[["USD 1bn trade envelope, May 2026", TRADE1B], ["MCB and ETG e-Bill, Sep 2026", ETG]]),
        ]},
        {"id": "4.5", "ic": "globe", "name": "Overseas banks", "blurb": "Visa in the islands.", "div": "mg", "rev": "overseas", "products": [
            P("madagascar", "MCB Madagascar", "80%-owned; Visa cards with nationwide cashback campaigns, Juice Madagascar (8,072 users, June 2025) and the first SUNREF green credit line.",
              s=["isl"], lc="everyday", o="B", neo=[0, "Visa."], src=[["Annual report 2025", AR25], ["MCB Madagascar", MG]]),
            P("seychelles", "MCB Seychelles", "Visa debit, Classic and Gold credit cards and Juice Seychelles (21,410 users); card revenue lifted non-interest income 28% in FY 2024/25.",
              s=["isl"], lc="everyday", o="B", div="sc", neo=[0, "Visa."], src=[["MCB Seychelles", SC], ["Annual report 2025", AR25]]),
            P("maldives", "MCB Maldives", "A corporate-focused bank that ended all card services, including merchant acceptance, deactivating its Visa debit cards on 30 September 2026.",
              s=["isl"], lc="everyday", st="retired", ay="Sep 2026", o="B", div="mv", neo=[0, "Visa; cards ended."], src=[["MCB Maldives notices, Aug 2026", MV]]),
        ]},
        {"id": "4.6", "ic": "gem", "name": "Wealth, markets & leasing", "blurb": "Private loans up 76%.", "div": "capm", "rev": "cibpb", "products": [
            P("wealth", "Private Wealth Management", "Investment, advisory and Lombard lending for resident and non-resident wealthy clients; private wealth loans up 76.5% in FY26; Juice Wealth in the app.",
              s=["aff"], lc="grow", o="B", div="mcb", neo=[0, ""], src=[["FY26 earnings call", ECP], ["Annual report 2025", AR25]]),
            P("capmkts", "MCB Capital Markets", "Investment banking, asset management, brokerage and private equity through MCB Equity Fund (USD 100 million evergreen).",
              s=["corp", "afr"], lc="grow", o="B", neo=[0, ""], src=[["Annual report 2025", AR25]]),
            P("leasing", "Leasing, factoring & real assets", "MCB Leasing, MCB Factors and MCB Real Assets, which owns most of the Club Med resort at Pointe aux Canonniers.",
              s=["sme", "corp"], lc="borrow", o="B", div="nbf", neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: MCB Juice, the most used banking app in Mauritius, JuicePro and Internet Banking Pro for business, 63 branches and kiosks, and hubs from Johannesburg to Dubai.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "MCB Juice", "blurb": "708,671 subscribers.", "div": "juice", "rev": "retail", "products": [
            P("juice", "MCB Juice", "Launched in 2013 and the most used banking app in Mauritius: 708,671 subscribers across three countries at June 2025, Juice 5.0 from September 2025, about 35 million log-ins in December 2025; transfers, QR, bills, Juice Tap and Juice Wealth.",
              s=["con", "isl"], lc="everyday", o="B", neo=[1, "Holds Mastercard and Visa tokens."], src=[["MCB payments ecosystem, May 2026", ECO], ["Annual report 2025", AR25], ["L'Express: payment trends, Jan 2026", QR67]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Business channels", "blurb": "JuicePro and IB Pro.", "div": "mcb", "rev": "corporate", "products": [
            P("juicepro", "JuicePro & Internet Banking Pro", "JuicePro 2.0 for SMEs (35,033 subscribers, June 2025) with a real-time payment dashboard and scan to pay for government bills; Internet Banking Pro and SmartApprove for corporates.",
              s=["sme", "corp"], lc="everyday", o="B", neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & hubs", "blurb": "63 branches, 5 hubs.", "div": "group", "rev": "group", "products": [
            P("branches", "Branches, ATMs & kiosks", "63 branches and kiosks and 217 ATMs across the group at June 2025, with InstaBank self-service kiosks in key Mauritian branches.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["Annual report 2025", AR25]]),
            P("hubs", "Commercial hubs", "Representative and advisory offices in Johannesburg, Nairobi, Lagos, Paris and Dubai for African and cross-border clients.",
              s=["afr"], lc="open", o="B", neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at MCB", "blurb": "Debit and corporate on Mastercard.", "products": [
        P("mcatmcb", "Mastercard at MCB", "Mastercard carries MCB's mass-market debit card in Mauritius (contactless since 2016), the Primo and half the Classic credit cards, the foreign-currency corporate card and ⚠ a Cash Passport prepaid programme. Visa holds the premium tier, SME debit, prepaid and every overseas subsidiary, and led Juice Tap (2024) and Apple Pay (2026).",
          s=["con"], div="group", rev="group", mc="The relationship this map is drawn for.",
          src=[["MCB: debit card", DEBIT], ["L'Express: Juice Tap with Visa, Dec 2024", JTAP], ["Tech-ish: Apple Pay in Mauritius, May 2026", TECHISH]]),
    ]},
    {"id": "pillar-market", "name": "Mauritian banking", "blurb": "MauCAS, QR, new taxes.", "products": [
        P("market", "The Mauritian market", "The central bank's MauCAS switch with instant payments and interoperable QR, a National Fintech Strategy 2026–2030 opening payments to non-banks ⚠, new taxes lifting MCB's tax rate to 26.4%, and rivals SBM, Absa and MauBank with telco wallets.",
          s=["con"], div="group", rev="group", src=[["BoM: MauCAS leaflet", MAUCAS], ["Capmad: National Fintech Strategy, Jun 2026", FINTECH], ["FY26 group management statement", GMS]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
