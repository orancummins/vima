"""Swisscard AECS's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Swisscard publishes no accounts, so figures come from its own website and press releases, the
brand sites of its card ranges, Swiss press and the Swiss Payment Monitor. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

HOME = "https://www.swisscard.ch/en"
FIG = "https://www.swisscard.ch/en/company/facts-and-figures"
MGMT = "https://www.swisscard.ch/en/company/management"
NET = "https://www.swisscard.ch/en/company/network"
PROD = "https://www.swisscard.ch/en/private-customers/products"
BIZ = "https://www.swisscard.ch/en/business-customers/business-cards/card-overview"
BANKS = "https://www.swisscard.ch/en/business-customers/banks"
WMC = "https://www.swisscard.ch/en/business-customers/banks/world-mastercard"
MERCH = "https://www.swisscard.ch/en/business-customers/merchants"
BONUS = "https://www.swisscard.ch/en/private-customers/credit-card-services/bonus-programs"
C2P = "https://www.swisscard.ch/en/private-customers/credit-card-services/digital-services/click-to-pay"
MOBILE = "https://www.swisscard.ch/en/private-customers/credit-card-services/digital-services/mobile-payment"
APP = "https://www.swisscard.ch/en/private-customers/credit-card-services/digital-services/swisscard-app"
WEB = "https://www.swisscard.ch/en/private-customers/credit-card-services/digital-services/web-services"
PICTURE = "https://www.swisscard.ch/en/business-customers/business-cards/card-services/mastercard-picture-card"
MCGOLD = "https://www.swisscard.ch/en/business-customers/business-cards/card-overview/mastercard-business-gold"
LOYB = "https://www.swisscard.ch/en/business-customers/business-cards/card-services/loyaltyprograms"
CAMINADA = "https://www.swisscard.ch/en/company/media/2026/partnership-andreas-caminada"
GLOBUS = "https://www.swisscard.ch/en/company/media/2022/globus-partnership"
CGO = "https://www.swisscard.ch/en/company/media/2023/member-to-the-executive-board-chief-growth-officer"
GETSC = "https://www.getswisscard.ch/en"
CASHBACK = "https://www.cashback-cards.ch/en/cards"
MM = "https://www.miles-and-more-cards.ch/en/private-customers/credit-cards/gold"
POINZ = "https://www.poinz.ch/en/home/poinz-swiss-loyalty-cards"
BK26 = "https://www.baerkarrer.ch/fr/news/baer-und-karrer-advises-ubs-on-the-completion-of-the-sale-of-its-stake-in-swisscard-and-the-transition-of-the-credit-suisse-branded-card-portfolios"
SWI24 = "https://www.swissinfo.ch/eng/archive-banking-fintech/american-express-to-take-over-ubss-stake-in-swisscard/87766827"
FINEWS24 = "https://www.finews.ch/news/banken/64860-swisscard-ubs-american-express"
MONEYCAB24 = "https://www.moneycab.com/finanz/swisscard-wird-ganz-von-amex-uebernommen-ubs-steigt-aus/amp/"
JV24 = "https://allnews.ch/content/corporate/credit-suisse-et-american-express-ne-renouvellent-pas-leur-accord-avec-swisscard"
FITCH24 = "https://allnews.ch/node/125515"
CBI = "https://www.cbinsights.com/company/swisscard"
SUPERCARD = "https://allnews.ch/node/9218"
PREISPIRAT = "https://www.preispirat.ch/die-swisscard-kreditkarte/"
SPM26 = "https://www.zhaw.ch/storage/hochschule/medien/news/2026/Press_Release_Swiss_Payment_Monitor_2026_EN.pdf"
SWATCH = "https://www.mobilepaymentstoday.com/news/swatch-rolls-out-contactless-payment-watches-in-switzerland/"
VISECA = "https://www.viseca.ch/en"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "owner · ratings · platform", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: American Express as sole owner since January 2026, Fitch ratings tied to Amex, a 1998 platform built for three card networks, and a business that publishes no accounts.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Ownership & ratings", "blurb": "Amex's alone since Jan 2026.", "div": "amex", "rev": "company", "products": [
            P("owner", "American Express ownership", "A 50:50 joint venture of American Express and Credit Suisse from 1998. UBS inherited Credit Suisse's half, agreed to sell it to American Express Swiss Holdings in October 2024, and the sale was completed on 21 January 2026.",
              s=["con"], o="A", st="new", ay="Jan 2026", at="American Express", neo=[0, "Owned by American Express."],
              mc="The owner is a rival network; every consumer offer leads with an Amex card.",
              src=[["Bär & Karrer: sale completed, Jan 2026", BK26], ["Swissinfo: Amex to take UBS stake, Oct 2024", SWI24], ["Swisscard: our network", NET]]),
            P("ratings", "Ratings & funding", "Fitch Long-Term IDR A- (stable) and F1 short-term; the support rating of a- is now anchored one notch below Amex ⚠. Card receivables are funded partly through Swiss-franc ABS (Swiss Credit Card Issuance 2022-1 and 2023-1) ⚠ current status.",
              s=["corp"], neo=[0, ""], src=[["allnews: Fitch, Jul 2024", FITCH24], ["CB Insights: Fitch, Jan 2026 ⚠", CBI], ["finews: UBS sells stake, Oct 2024", FINEWS24]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "A former Mastercard country head.", "div": "swisscard", "rev": "company", "products": [
            P("leadership", "Executive Board", "CEO Guido Müller since January 2021, who ran Mastercard Switzerland from 2012 to 2017 and Mastercard Data & Services in South East Asia from 2018 to 2020; CIO Linda de Winter, CFO Roman Binder, CCO Sabine Mantoiu (May 2026), COO Alex Friedli.",
              s=["corp"], neo=[0, ""], mc="The CEO knows Mastercard from the inside.",
              src=[["Swisscard: Executive Board", MGMT]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & scale", "blurb": "650 staff, no published accounts.", "div": "swisscard", "rev": "company", "products": [
            P("heritage", "Heritage & scale", "Founded in 1998 in Zurich, in Horgen since 2001; took over Credit Suisse's card issuing in 2015. More than 650 staff (about 600 in a June 2026 release ⚠), more than 400,000 app users and over 1.5 million cards managed before the Credit Suisse cards left ⚠. No revenue, card or volume figures are published.",
              s=["con"], o="I", neo=[0, ""], src=[["Swisscard: facts and figures", FIG], ["Swisscard: CGO appointment, 2023", CGO], ["Moneycab: Amex takes over, Oct 2024", MONEYCAB24]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "One platform, three networks.", "div": "swisscard", "rev": "company", "products": [
            P("tech", "Card platform, service tools & AI", "An integrated platform for American Express, Mastercard and Visa cards since 1998, the Transakt 3-D Secure app (2014, first in Europe), speech recognition (2018) and a Customer Service Agent portal (2024); the CIO owns the IT and AI strategy ⚠.",
              s=["corp"], o="B", neo=[0, ""],
              mc="No public agentic-payments plan; Agent Pay is open ground.",
              src=[["Swisscard: facts and figures", FIG], ["CB Insights: Top CIO 2026 ⚠", CBI]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Credit Suisse cards gone to UBS.", "div": "swisscard", "rev": "company", "products": [
            P("strategy", "Strategy", "No published targets. In practice: premium American Express cards and lifestyle partnerships, free cards with instant digital issuing, and growing Amex acceptance in Switzerland.",
              s=["con"], neo=[0, ""], src=[["Swisscard: Caminada partnership, Jun 2026", CAMINADA], ["swisscard credit card", GETSC]]),
            P("csexit", "Credit Suisse card portfolios", "Credit Suisse-branded American Express, Mastercard and Visa cards (Bonviva from 2008) moved to UBS, which began issuing its own cards in the first half of 2025; the transition was completed before January 2026. A Credit Suisse business-card page is still online ⚠.",
              short="Credit Suisse cards (to UBS)", s=["con", "sme"], lc="everyday", st="retired", ay="2025", o="I", at="UBS", neo=[1, "All three networks; now UBS's."],
              src=[["Bär & Karrer: sale completed, Jan 2026", BK26], ["allnews: JV not renewed, Jun 2024", JV24], ["Swissinfo: Amex to take UBS stake, Oct 2024", SWI24]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: proprietary American Express cards, SWISS Miles & More and Cashback duos with a Mastercard or Visa second card, Visa-only free cards, Mastercard and Amex business cards, Amex supplier payments, Amex acceptance, and wallets and Click to Pay.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "American Express cards", "blurb": "Platinum, Gold, Centurion.", "div": "amex", "rev": "private", "products": [
            P("amexcards", "American Express Platinum, Gold, Card & Centurion", "Swisscard is the only Swiss issuer of American Express: the metal Platinum (about 1,700 lounges), Gold (Rose Gold design in 2024, first in Europe), the American Express Card and the Centurion Card (2002).",
              short="Amex cards", s=["prem", "con"], lc="everyday", o="P", at="American Express", neo=[0, "American Express."],
              src=[["Swisscard: credit cards", PROD], ["Swisscard: facts and figures", FIG]]),
        ]},
        {"id": "2.2", "ic": "plane", "name": "SWISS Miles & More", "blurb": "Amex plus Mastercard or Visa.", "div": "swiss", "rev": "private", "products": [
            P("mm", "SWISS Miles & More credit cards", "Classic, Gold and Platinum card duos, issued exclusively by Swisscard for more than 20 years: an American Express plus a World Mastercard or a Visa. Gold earns 2 miles per CHF 2 on the Amex and 0.8 on the Mastercard or Visa.",
              short="Miles & More (Amex + MC or Visa)", s=["trav"], lc="everyday", o="P", at="SWISS, Lufthansa Miles & More", neo=[1, "Second card is Mastercard or Visa."],
              mc="Mastercard competes with Visa for the second card in each duo.",
              src=[["Miles & More Gold cards", MM], ["Swisscard: our network", NET]]),
        ]},
        {"id": "2.3", "ic": "coins", "name": "Free & cashback cards", "blurb": "New launches chose Visa.", "div": "cashback", "rev": "private", "products": [
            P("cashback", "Cashback Cards", "A free duo since November 2018: American Express Cashback (1%, 5% for three months up to CHF 100) plus a World Mastercard or a Visa (0.25%); it replaced the Coop SUPERCARDplus.",
              short="Cashback (Amex + MC or Visa)", s=["con"], lc="everyday", ay="Nov 2018", neo=[1, "Second card is Mastercard or Visa."],
              src=[["Cashback Cards", CASHBACK], ["allnews: Cashback replaces SUPERCARDplus", SUPERCARD]]),
            P("poinz", "poinz Cards", "A free duo with the Zurich loyalty start-up poinz since 2022: poinz American Express (1%) and poinz Visa (0.25%), cashback paid in francs into the poinz app.",
              short="poinz (Amex + Visa)", s=["con"], lc="everyday", ay="2022", o="P", at="poinz", div="poinz", neo=[0, "Amex and Visa."],
              src=[["poinz Cards", POINZ], ["Swisscard: our network", NET]]),
            P("sccard", "swisscard Visa Credit Card", "A free card with no foreign-currency fees, a virtual card in the app on approval, QR-bill and eBill repayment and an optional instalment facility; launched in 2025 ⚠.",
              short="swisscard (Visa)", s=["con"], lc="open", st="new", ay="2025", div="free", neo=[0, "Visa."],
              mc="The newest own-brand card went to Visa.",
              src=[["swisscard credit card", GETSC], ["Preispirat: launch ⚠", PREISPIRAT]]),
        ]},
        {"id": "2.4", "ic": "briefcase-business", "name": "Business & corporate cards", "blurb": "Mastercard and Amex side by side.", "div": "swisscard", "rev": "business", "products": [
            P("mcbiz", "Mastercard business & corporate cards", "Mastercard Business Standard, Business Gold (free in year one, then CHF 150), Business Euro and Corporate Dollar, with Mastercard's spending bonus that cuts the next year's fee.",
              short="Mastercard business cards", s=["sme", "corp"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's firmest ground at Swisscard.",
              src=[["Swisscard: business cards", BIZ], ["Swisscard: Mastercard Business Gold", MCGOLD]]),
            P("amexcorp", "American Express corporate & business cards", "Corporate Platinum, Corporate Gold, Corporate Card and Meeting Card, plus the Business and Gold Business Cards with Membership Rewards.",
              short="Amex corporate cards", s=["corp", "sme"], lc="everyday", div="amex", at="American Express", neo=[0, "American Express."],
              src=[["Swisscard: business cards", BIZ]]),
            P("smepkg", "SWISS SME card packages", "Silver, Gold and Platinum packages pairing an American Express and a Mastercard: miles for staff and PartnerPlusBenefit for the firm.",
              short="SWISS SME (Amex + MC)", s=["sme"], lc="everyday", div="swiss", at="SWISS", neo=[1, "Amex and Mastercard."],
              src=[["Swisscard: business loyalty programmes", LOYB], ["Swisscard: business cards", BIZ]]),
        ]},
        {"id": "2.5", "ic": "receipt-text", "name": "Supplier payments", "blurb": "Amex vPayment and BTA.", "div": "amex", "rev": "business", "products": [
            P("supplier", "Purchasing, vPayment & Business Travel Account", "American Express Corporate Purchasing Card, vPayment virtual accounts and the Business Travel Account, including one for SBB rail travel.",
              s=["corp"], lc="move", at="American Express", neo=[0, "American Express."],
              mc="Virtual and purchasing cards run on Amex; Mastercard has no product here.",
              src=[["Swisscard: business cards", BIZ]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acceptance", "blurb": "149,000 Amex points.", "div": "amex", "rev": "merchants", "products": [
            P("acceptance", "American Express acceptance", "Swisscard signs and serves Swiss merchants for American Express: more than 149,000 acceptance points, a merchant portal and Shop Small. It does not acquire Mastercard or Visa.",
              short="Amex acquiring", s=["merch"], lc="move", o="P", at="American Express", neo=[0, "American Express only."],
              src=[["Swisscard: merchants", MERCH], ["Swisscard: facts and figures", FIG]]),
        ]},
        {"id": "2.7", "ic": "wallet", "name": "Wallets & Click to Pay", "blurb": "Every network tokenised.", "div": "swisscard", "rev": "private", "products": [
            P("wallets", "Apple Pay, Google Pay, Samsung Pay & Swatch Pay", "Apple Pay and Samsung Pay in 2016 (the first major Swiss provider), Swatch Pay in 2018 (certified by Mastercard and Visa) and Google Pay in July 2020, using device tokens on all three networks.",
              short="Mobile wallets", s=["con", "trav"], lc="everyday", ay="2016", o="P", at="Apple, Google, Samsung, Swatch", neo=[1, "Mastercard tokens for its Mastercards."],
              src=[["Swisscard: mobile payment", MOBILE], ["Swisscard: facts and figures", FIG], ["Mobile Payments Today: Swatch Pay ⚠", SWATCH]]),
            P("c2p", "Click to Pay", "Enabled card by card in the Swisscard app for American Express, Visa and Mastercard cards; Amex business, corporate and supplier cards are excluded. Launch date not published ⚠.",
              s=["con"], lc="move", o="P", at="Amex, Mastercard, Visa", neo=[1, "Mastercard Click to Pay for its Mastercards."],
              src=[["Swisscard: Click to Pay", C2P]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card: 3-D Secure and phishing warnings, Membership Rewards, miles and Priceless, Mastercard data feeds for companies, insurance, and 24/7 service in four languages.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security & fraud", "blurb": "3-D Secure in the app.", "div": "swisscard", "rev": "private", "products": [
            P("threeds", "3-D Secure & card controls", "Online payments approved in the app with 3-D Secure (piloted for Mastercard and Visa in 2010), biometric login, limits, card blocking and push notifications.",
              s=["con"], lc="everyday", ay="2010", neo=[1, "Each network's 3-D Secure."],
              src=[["Swisscard: app", APP], ["Swisscard: facts and figures", FIG]]),
            P("phishing", "Scam & phishing protection", "Phishing warnings on the home page and the LINDA anti-phishing contest (2026). Fewer than half of Swiss know a credit card payment can be disputed.",
              s=["con"], lc="everyday", st="new", neo=[None, "No public fraud partner."],
              mc="Scam scoring and identity tools are an open need.",
              src=[["Swisscard: home page", HOME], ["Swiss Payment Monitor, Feb 2026", SPM26]]),
        ]},
        {"id": "3.2", "ic": "gift", "name": "Loyalty & lifestyle", "blurb": "Membership Rewards, Priceless.", "div": "amex", "rev": "private", "products": [
            P("mr", "Membership Rewards, miles & Pay with Points", "Membership Rewards, Miles & More, cashback and pointup, with Pay with Points and MilesPay in the app since 2021.",
              s=["prem", "trav"], lc="grow", ay="2021", neo=[0, ""], src=[["Swisscard: bonus programmes", BONUS], ["Swisscard: facts and figures", FIG]]),
            P("selects", "Amex Selects & partnerships", "Amex Selects with Switzerland Tourism, Globus credit for Platinum members (2022), GaultMillau and Andreas Caminada as brand ambassador (June 2026).",
              s=["prem"], lc="beyond", st="new", at="Globus, GaultMillau, Caminada", neo=[0, "American Express."],
              src=[["Swisscard: Caminada, Jun 2026", CAMINADA], ["Swisscard: Globus, 2022", GLOBUS], ["Swisscard: our network", NET]]),
            P("priceless", "Mastercard Priceless Cities", "Promoted to holders of the Mastercard in the Cashback and SWISS Miles & More duos.",
              s=["con", "trav"], lc="beyond", o="P", at="Mastercard", neo=[3, "Mastercard's own programme."],
              src=[["Cashback Cards", CASHBACK], ["Miles & More Gold cards", MM]]),
        ]},
        {"id": "3.3", "ic": "chart-column", "name": "Data for companies", "blurb": "Mastercard SDG2 feeds.", "div": "swisscard", "rev": "business", "products": [
            P("sdg2", "Mastercard Smart Data (SDG2)", "Daily, weekly or monthly Mastercard card data files for expense and accounting systems, for companies using Mastercard business cards across countries.",
              short="SDG2 data", s=["corp"], lc="move", o="P", at="Mastercard", neo=[3, "Mastercard's own data service."],
              src=[["Swisscard: Mastercard Business Gold", MCGOLD]]),
            P("picture", "Mastercard Picture Card", "Company logos or own designs on Business Standard, Gold and Euro Mastercards: logo free, own design CHF 150 once, CHF 5 a card a year.",
              s=["sme"], lc="open", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["Swisscard: Picture Card", PICTURE]]),
        ]},
        {"id": "3.4", "ic": "badge-check", "name": "Insurance", "blurb": "Travel, purchase, returns.", "div": "swisscard", "rev": "private", "products": [
            P("insurance", "Card insurance", "Travel accident cover up to CHF 700,000 on Miles & More Gold, purchase and return protection (up to CHF 1,000) on the free cards, and paid add-ons.",
              s=["trav", "con"], lc="grow", neo=[0, ""], src=[["Miles & More Gold cards", MM], ["Cashback Cards", CASHBACK]]),
        ]},
        {"id": "3.5", "ic": "headset", "name": "Customer service", "blurb": "24/7 in four languages.", "div": "swisscard", "rev": "company", "products": [
            P("service", "Customer service", "Around-the-clock service in German (including dialect), French, Italian and English, with a Customer Service Agent portal since 2024.",
              s=["con", "prem"], lc="everyday", o="B", neo=[0, ""], src=[["swisscard credit card", GETSC], ["Swisscard: facts and figures", FIG]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What Swisscard sells: credit cards to private customers, business and corporate cards, cards for private-bank clients, and American Express acceptance to merchants.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Private customers", "blurb": "Amex first, a second card optional.", "div": "swisscard", "rev": "private", "products": [
            P("privatecards", "Private-customer card range", "About 31 private cards in October 2024, from free cards to Centurion. Amex leads every range; Mastercard is an option in two duos.",
              s=["con", "prem", "trav"], lc="everyday", neo=[1, "Amex first; Mastercard or Visa second."],
              src=[["Moneycab: Amex takes over, Oct 2024", MONEYCAB24], ["Swisscard: credit cards", PROD]]),
            P("instalment", "Instalment credit", "Statements can be paid in instalments with interest on the free and duo cards, within Swiss consumer-credit rules.",
              s=["con"], lc="borrow", neo=[1, "On whichever network the card runs."],
              src=[["swisscard credit card", GETSC], ["Cashback Cards", CASHBACK]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Business customers", "blurb": "23 business products.", "div": "swisscard", "rev": "business", "products": [
            P("bizline", "Business card range", "About 23 corporate products in October 2024: Amex corporate and supplier payments, Mastercard business cards and SWISS SME packages, with online applications and video identification.",
              s=["sme", "corp"], lc="open", neo=[1, "Amex and Mastercard."],
              src=[["Moneycab: Amex takes over, Oct 2024", MONEYCAB24], ["Swisscard: business cards", BIZ]]),
        ]},
        {"id": "4.3", "ic": "gem", "name": "Private banks", "blurb": "World Mastercard for wealth clients.", "div": "swisscard", "rev": "banks", "products": [
            P("wmc", "World Mastercard for private banks", "World Mastercard Standard, Gold and Platinum in a neutral design, distributed through private banks.",
              short="World Mastercard", s=["pb"], lc="everyday", o="P", at="Private banks", neo=[2, "Mastercard."],
              src=[["Swisscard: World Mastercard", WMC], ["Swisscard: private banks", BANKS]]),
            P("wmcfx", "World Mastercard Gold EUR/USD", "Cards billed in euros or dollars, so spending in those currencies carries no exchange loss.",
              s=["pb"], lc="move", o="P", at="Private banks", neo=[2, "Mastercard."],
              src=[["Swisscard: private banks", BANKS]]),
            P("pbamex", "American Express & Miles & More for private banks", "Amex Platinum (CHF, EUR or USD), Gold and Card, and SWISS Miles & More cards for private-bank clients.",
              s=["pb"], lc="everyday", div="amex", neo=[0, "American Express."],
              src=[["Swisscard: private banks", BANKS]]),
        ]},
        {"id": "4.4", "ic": "store", "name": "Merchants", "blurb": "Amex acceptance and marketing.", "div": "amex", "rev": "merchants", "products": [
            P("merchline", "Merchant services", "Acceptance contracts, free marketing support, listing on Amex websites and Shop Small for Swiss merchants.",
              s=["merch"], lc="grow", neo=[0, "American Express."],
              src=[["Swisscard: merchants", MERCH]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Swisscard: the Swisscard app for 400,000 users, partners such as SWISS, poinz and private banks, and portals for companies and merchants.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Swisscard app", "blurb": "400,000 users.", "div": "swisscard", "rev": "private", "products": [
            P("app", "Swisscard app", "More than 400,000 users: balances, 3-D Secure approvals, PIN, limits, Click to Pay, spending categories and instant applications for the free cards (2023).",
              s=["con", "trav", "prem"], lc="open", ay="2020", o="B", neo=[0, ""],
              src=[["Swisscard: app", APP], ["Swisscard: facts and figures", FIG]]),
            P("webservices", "Web Services", "Statements as PDF and transactions as CSV in a browser, unlocked through the app.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Swisscard: Web Services", WEB]]),
        ]},
        {"id": "5.2", "ic": "users-round", "name": "Partners", "blurb": "SWISS, poinz, private banks.", "div": "swiss", "rev": "private", "products": [
            P("partners", "Distribution partners", "SWISS (exclusive issuer of its Miles & More cards for more than 20 years), poinz (1,600 local businesses, a million users) and private banks.",
              s=["trav", "pb"], lc="open", o="P", at="SWISS, poinz", neo=[0, ""],
              src=[["Swisscard: our network", NET], ["Swisscard: private banks", BANKS]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "Portals", "blurb": "Company and merchant online.", "div": "swisscard", "rev": "business", "products": [
            P("portals", "Company and merchant portals", "Company-online for business card administrators and the American Express merchant and reconciliation portals.",
              s=["corp", "merch"], lc="everyday", neo=[0, ""], src=[["Swisscard: home page", HOME]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Swisscard", "blurb": "Business cards and the second card.", "products": [
        P("mcatswisscard", "Mastercard at Swisscard", "Mastercard carries Swisscard's business and corporate range, its World Mastercards for private banks and one option in the Miles & More and Cashback duos, with SDG2 data and Priceless. American Express owns Swisscard outright since January 2026, leads every consumer offer and is the only network Swisscard acquires; the newest own-brand launches chose Visa. The CEO ran Mastercard Switzerland from 2012 to 2017.",
          s=["con"], div="swisscard", rev="company", mc="The relationship this map is drawn for.",
          src=[["Swisscard: our network", NET], ["Swisscard: Executive Board", MGMT], ["swisscard credit card", GETSC]]),
    ]},
    {"id": "pillar-market", "name": "Swiss payments", "blurb": "Mobile first, credit growing.", "products": [
        P("market", "The Swiss market", "Mobile payments lead at 31.4% of transactions, debit 23.8%, cash 23.0% and credit cards 17.2% (autumn 2025); TWINT took 10.6% of in-store payments. Viseca issues on Mastercard and Visa; UBS now issues the former Credit Suisse cards itself.",
          s=["con"], div="swisscard", rev="company", src=[["Swiss Payment Monitor, Feb 2026", SPM26], ["Viseca", VISECA]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
