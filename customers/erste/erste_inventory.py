"""Erste Group's and Erste Bank Oesterreich's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 half-year report, results release and
presentation (30 July 2026), the 2025 results (26 February 2026) and the Erste Bank und Sparkassen 2026 factsheet.
Product and network facts come from Erste Bank's own pages on sparkasse.at, read 17 October 2026. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

HYR = "https://www.bvb.ro/infocont/infocont26/2026_HY_financial_report_Erste_Group_EN_final.pdf"
H1PR = "https://www.erstegroup.com/en/news-media/press-releases/2026/07/30/erstegroup-h1-2026-results"
IRN = "https://www.erstegroup.com/en/investors/news/investorinformation/2026/07/30/irnews-q22026-results"
PRES = "https://cdn.erstegroup.com/content/dam/at/eh/www_erstegroup_com/en/Investor_Relations/2026/presentations/IR_Pres_CC_260730_H126.pdf"
POL = "https://www.erstegroup.com/en/news-media/press-releases/2026/01/09/erste-group-completes-acquisition-of-controlling-stake-in-santander-bank-polska"
EBPW = "https://en.wikipedia.org/wiki/Erste_Bank_Polska"
FY25 = "https://www.leadersnet.at/news/97688,erste-group-staerkt-kapitalbasis-und-baut-kundengeschaeft-aus.html"
SHARE = "https://www.erstegroup.com/en/investors/share/shareholder-structure"
WIKI = "https://en.wikipedia.org/wiki/Erste_Group"
FACT = "https://cdn0.erstegroup.com/content/dam/at/sparkassenverband/www_sparkassenverband_de/EBSPK_Factsheet_2026.pdf"
EURO = "https://www.euromoney.com/article/78slla2659gkkc4k0gkscoksg/cees-best-bank-2026-erste-group/"
MAESTRO = "https://futurezone.at/produkte/erste-bank-maestro-karte-ist-bis-mitte-2020-geschichte/400679150"
DEBIT = "https://www.sparkasse.at/erstebank/privatkunden/konto-karten/karten/debit-mastercard"
BANKOMAT = "https://www.sparkasse.at/erstebank/privatkunden/konto-karten/karten/bankomatkarten"
CREDIT = "https://www.sparkasse.at/erstebank/privatkunden/konto-karten/s-kreditkarten"
CCOMP = "https://www.sparkasse.at/erstebank/privatkunden/konto-karten/s-kreditkarten/kreditkartenvergleich"
SMV = "https://www.sparkasse.at/erstebank/privatkunden/konto-karten/s-kreditkarten/s-visa-card/smartcard-visa"
SMM = "https://www.sparkasse.at/erstebank/privatkunden/konto-karten/s-kreditkarten/s-mastercard/smartcard-mastercard"
GOED = "https://www.sparkasse.at/erstebank/privatkunden/konto-karten/s-kreditkarten/s-visa-card/s-visacard-goed"
MM = "https://www.sparkasse.at/erstebank/privatkunden/konto-karten/s-kreditkarten/s-mastercard/miles-more-kreditkarten"
MMNEWS = "https://www.leadersnet.at/news/91910,aua-und-miles-more-wechseln-ihren-kreditkarten-partner.html"
BIZCARDS = "https://www.sparkasse.at/erstebank/unternehmen/produkte-firmenkunden/konto-karten/business-karten"
BIZSMART = "https://www.sparkasse.at/erstebank/unternehmen/produkte-firmenkunden/konto-karten/business-karten/business-smartcard"
VIRTUAL = "https://www.sparkasse.at/erstebank/unternehmen/produkte-firmenkunden/konto-karten/business-karten/business-virtualcards"
YOKOY = "https://www.sparkasse.at/erstebank/unternehmen/produkte-firmenkunden/konto-karten/business-karten/yokoy"
POS = "https://www.sparkasse.at/erstebank/unternehmen/produkte-firmenkunden/cash-management/zv-services/bankomatkasse"
GBIZ = "https://www.sparkasse.at/erstebank/unternehmen/produkte-firmenkunden/digitales-banking/george-business"
GEORGE = "https://www.sparkasse.at/erstebank/privatkunden/digitales-banking/george-kennenlernen"
GFIT = "https://www.sparkasse.at/erstebank/privatkunden/digitales-banking/george-fit"
GINV = "https://www.sparkasse.at/erstebank/privatkunden/digitales-banking/george-invest"
MONEYBACK = "https://www.sparkasse.at/erstebank/privatkunden/digitales-banking/george-erweitern/moneyback"
MOVE = "https://www.sparkasse.at/erstebank/privatkunden/digitales-banking/move-and-save"
GEO = "https://www.sparkasse.at/erstebank/privatkunden/konto-karten/konto-leistungen/geo-control"
APPLEPAY = "https://www.sparkasse.at/erstebank/privatkunden/konto-karten/apple-pay"
OPENB = "https://www.sparkasse.at/erstebank/open-banking/public"
KK = "https://www.sparkasse.at/erstebank/privatkunden/konto-karten"
WERO = "https://www.trendingtopics.eu/oesterreichische-banken-steigen-bei-europaeischer-zahlungsloesung-wero-ein/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · foundation · savings banks", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: 23.2 million customers in eight markets, €283 billion of loans, a foundation holding 26.65%, a savings bank dating from 1819 with 48 Sparkassen behind it, the George platform, and a 2030 plan built on Poland.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "€2.0bn profit in H1 2026.", "div": "group", "rev": "oat", "products": [
            P("balance", "Group balance sheet & earnings", "Net profit of €1,975 million in H1 2026 (up 18.6%; 7.6% like for like), ROTE 19.6%, cost/income 44.4% and CET1 15.2%; loans of €282.7 billion and deposits of €323.7 billion at 30 June 2026, Poland included. 2025 net profit was €3.5 billion. Rated Aa3 by Moody's, A+ by S&P and A by Fitch.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 half-year report", HYR], ["H1 2026 results release", H1PR], ["2025 results, Feb 2026", FY25]]),
            P("austria", "Erste Bank und Sparkassen in Austria", "4.3 million customers, 732 branches and 16,844 staff at end-2025; loans of €105.6 billion and deposits of €119.1 billion; 263,673 new customers in 2025. Erste Bank Oesterreich's own net result rose 27.2% to €333 million in H1 2026, helped by higher payment fees.",
              s=["con", "sme"], neo=[0, ""], src=[["Erste Bank und Sparkassen factsheet 2026", FACT], ["H1 2026 half-year report", HYR]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "Foundation-anchored, Bosek leads.", "div": "group", "rev": "oat", "products": [
            P("owners", "Ownership & listing", "Listed in Vienna, Prague and Bucharest, with a market value of €48.1 billion at 30 June 2026. The ERSTE Foundation controls 26.65% with its partners; 73.35% is free float.",
              s=["corp"], neo=[0, ""], src=[["Erste Group: shareholder structure", SHARE], ["H1 2026 half-year report", HYR]]),
            P("leadership", "Management board", "Peter Bosek (CEO), Stefan Dörfler (CFO), Alexandra Habeler-Drabek and Maurizio Poletto ⚠ portfolios not confirmed; Gerda Holzinger-Burgstaller runs Erste Bank Oesterreich.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 half-year report", HYR], ["Trending Topics: Wero, Jun 2026", WERO]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & savings banks", "blurb": "Since 1819; 48 Sparkassen.", "div": "spk", "rev": "spk", "products": [
            P("heritage", "Erste oesterreichische Spar-Casse", "Founded in Vienna in October 1819, listed in 1997, split into a holding and Erste Bank Oesterreich in 2008; bought Česká spořitelna, Slovenská sporiteľňa and BCR in 2000–06.",
              s=["con"], o="I", neo=[0, ""], src=[["Wikipedia: Erste Group", WIKI]]),
            P("haftung", "Savings-bank cross-guarantee system", "Erste Bank and 48 Austrian savings banks work as one group through a cross-guarantee system (Haftungsverbund); Salzburger Sparkasse merged into Erste Bank Oesterreich on 1 August 2025.",
              s=["con", "sme"], o="I", neo=[0, ""], src=[["Erste Bank und Sparkassen factsheet 2026", FACT], ["H1 2026 half-year report", HYR]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "George, built in-house.", "div": "george", "rev": "ebo", "products": [
            P("tech", "George platform & IT", "George, Erste's own digital platform, launched in Austria in January 2015 and now runs in seven markets with more than 11.8 million users; group IT spending was €485 million in H1 2026, €129 million of it in Poland.",
              s=["con", "corp"], o="B", neo=[0, ""], src=[["H1 2026 results presentation", PRES], ["Investor information, Q2 2026", IRN], ["Wikipedia: Erste Group", WIKI]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy 2030 & deals", "blurb": "Double EPS by 2030.", "div": "group", "rev": "oat", "products": [
            P("strategy", "2030 ambition", "Double earnings per share to more than €15 by 2030 (about 15% a year) with ROTE above 20% throughout; 2026 net profit guided above €4 billion.",
              s=["corp"], st="new", neo=[0, ""], src=[["H1 2026 half-year report", HYR]]),
            P("polanddeal", "Santander Bank Polska purchase", "A 49% controlling stake and 50% of Santander TFI for about €7.0 billion, completed 9 January 2026 and renamed Erste Bank Polska on 24 April 2026; Santander keeps 9.7% and a corporate-banking alliance.",
              s=["corp"], st="new", ay="Jan 2026", o="A", at="Banco Santander", neo=[0, ""], src=[["Erste: Polish deal completed, Jan 2026", POL], ["Wikipedia: Erste Bank Polska", EBPW]]),
            P("cardclub", "Erste Card Club (Croatia)", "The Croatian card company was sold in H1 2026 for a €116 million gain; buyer not confirmed ⚠.",
              s=["con"], st="retired", o="I", neo=[None, "Network not researched."], src=[["H1 2026 half-year report", HYR]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves in Austria: Debit Mastercard on every account, credit cards on both Mastercard and Visa, the Austrian Miles & More card on Mastercard, phone wallets, card acceptance through Global Payments, and Wero coming.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Debit Mastercard since 2019.", "div": "ebo", "rev": "ebo", "products": [
            P("debit", "Debitkarte (Debit Mastercard)", "Erste Bank and the Sparkassen replaced Maestro with Debit Mastercard from April 2019; about 1.7 million had been issued by November 2019 and the rest by mid-2020. It now comes as card, micro card or wristband and works in Apple Pay, Google Pay, Garmin Pay and Swatch Pay.", short="Debit (Mastercard)",
              s=["con", "inv"], lc="everyday", ay="Apr 2019", o="P", at="Mastercard", neo=[2, "Debit Mastercard."],
              mc="Mastercard's anchor at Erste in Austria: every personal account card.",
              src=[["futurezone: Maestro gone by mid-2020, Nov 2019", MAESTRO], ["Erste Bank: Debitkarte", DEBIT]]),
            P("bizdebit", "Business Debit Mastercard", "Debit Mastercard for business accounts, managed in George Business.",
              s=["sme"], lc="everyday", o="P", at="Mastercard", neo=[2, "Debit Mastercard."], src=[["Erste Bank: business cards", BIZCARDS]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Mastercard or Visa, customer's choice.", "div": "ebo", "rev": "ebo", "products": [
            P("credit", "Smartcard & Premiumcard", "Erste's own credit cards, each sold on both Mastercard and Visa: Split Now spreads purchases of €50 to €4,800 over up to four bills, Umsatzbonus pays back up to 0.3%, and Premiumcard adds travel insurance and airport services. First year free until 31 December 2026.", short="Credit (Mastercard and Visa)",
              s=["con", "trav"], lc="borrow", o="B", at="Mastercard, Visa", neo=[1, "Split between Mastercard and Visa."],
              mc="Every new credit customer picks a network; the split is not public.",
              src=[["Erste Bank: s Kreditkarten", CREDIT], ["Erste Bank: card comparison", CCOMP], ["Smartcard Mastercard", SMM]]),
            P("goed", "GÖD Visa cards", "Smartcard and Premiumcard for members of the public-service union GÖD, doubling as the membership card.",
              s=["con"], lc="borrow", o="P", at="GÖD, Visa", neo=[0, "Visa."], src=[["Erste Bank: GÖD Visa cards", GOED]]),
        ]},
        {"id": "2.3", "ic": "plane", "name": "Miles & More", "blurb": "Won from card complete.", "div": "ebo", "rev": "ebo", "products": [
            P("miles", "Austrian Miles & More credit cards", "Erste Bank und Sparkasse won Austrian Airlines' and Miles & More's tender (August 2025) and took the cards from card complete in early 2026. Mastercard stayed as the network; cards are issued instantly in George, with FX-fee refunds, business versions and Priority Pass on premium cards.", short="Miles & More (Mastercard)",
              s=["trav", "sme"], lc="borrow", st="new", ay="Early 2026", o="P", at="Austrian Airlines, Miles & More, Mastercard", neo=[2, "Mastercard co-brand."],
              mc="A co-brand Mastercard kept on its network through a change of issuer.",
              src=[["Leadersnet: AUA and Miles & More, Aug 2025", MMNEWS], ["Erste Bank: Miles & More cards", MM]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Wallets & tokens", "blurb": "Apple, Google, Garmin, Swatch.", "div": "ebo", "rev": "ebo", "products": [
            P("wallets", "Phone and watch wallets", "Debit and credit cards, including all business credit cards, work in Apple Pay, Google Pay, Garmin Pay and Swatch Pay, added from the George app.",
              s=["con", "sme"], lc="everyday", o="P", at="Apple, Google, Garmin, Swatch", neo=[1, "Tokens on both networks ⚠."], src=[["Erste Bank: Apple Pay", APPLEPAY], ["Erste Bank: Debitkarte", DEBIT]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "Global Payments joint venture.", "div": "group", "rev": "ebo", "products": [
            P("accept", "Bankomatkasse with Global Payments", "POS terminals and online gateways from Global Payments, Erste's joint-venture partner since 2016, accepting Maestro, Mastercard, Visa, JCB, UnionPay and Diners, with next-day settlement.",
              s=["sme"], lc="move", ay="2016", o="P", at="Global Payments", neo=[1, "Accepts every network."], src=[["Erste Bank: Bankomatkasse", POS]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Account-to-account", "blurb": "Wero shareholder.", "div": "ebo", "rev": "ebo", "products": [
            P("wero", "Wero (European Payments Initiative)", "Erste Bank Oesterreich became an EPI shareholder on 22 June 2026, alongside Raiffeisen, to bring Wero's phone-number and merchant payments to Austria; no launch date yet. Wero has more than 55 million users.",
              s=["con", "sme"], lc="move", st="new", ay="Jun 2026", o="P", at="EPI", neo=[0, "Wero, an account-to-account scheme."],
              mc="The European alternative to card rails, with Erste as an owner.",
              src=[["Trending Topics: Wero, Jun 2026", WERO]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: Mastercard Identity Check and Geo-Control on cards, George ID and open-banking APIs, Hey George built with OpenAI, and cashback, savings nudges and financial-health tools.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Card security", "blurb": "Identity Check, Geo-Control.", "div": "ebo", "rev": "ebo", "products": [
            P("idcheck", "Mastercard Identity Check", "Online debit payments are authenticated through Mastercard Identity Check and approved with George ID, s Identity or cardTAN.",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[3, "Mastercard's own."], src=[["Erste Bank: debit card FAQ", BANKOMAT]]),
            P("geo", "Geo-Control & Karten-Airbag", "Debit cards cannot withdraw cash outside Europe unless the customer lifts the block in George for up to three months; customers are not liable for misuse except for gross negligence.",
              s=["con"], lc="everyday", o="B", neo=[0, "Erste's own."], src=[["Erste Bank: Geo-Control", GEO]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Identity & open banking", "blurb": "George ID, PSD2 APIs.", "div": "george", "rev": "ebo", "products": [
            P("georgeid", "George ID & s Identity", "App-based approval for banking, card payments and contracts, replacing older TAN methods.",
              s=["con", "sme"], lc="open", o="B", neo=[0, ""], src=[["Erste Bank: George app", GEORGE], ["Erste Bank: debit card FAQ", BANKOMAT]]),
            P("psd2", "Open-banking APIs", "PSD2 interfaces that let licensed third parties see accounts and start payments with the customer's consent.",
              s=["sme"], lc="open", o="B", neo=[0, ""], src=[["Erste Bank: PSD2 and open banking", OPENB]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "AI", "blurb": "Hey George with OpenAI.", "div": "george", "rev": "cee", "products": [
            P("heygeorge", "Hey George", "An AI chatbot rolling out in the Czech Republic and Romania, built with OpenAI, as Erste moves to AI-supported advice for all retail customers ⚠ Austrian launch not confirmed.",
              s=["con", "inv"], lc="everyday", st="new", o="P", at="OpenAI", neo=[0, ""],
              mc="Agentic payments would need tokenised card credentials; Agent Pay is open ground.",
              src=[["Euromoney: CEE's best bank 2026", EURO]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards & financial health", "blurb": "Moneyback, George FIT.", "div": "ebo", "rev": "ebo", "products": [
            P("moneyback", "Moneyback", "Card-linked cashback in the George app, run with Dateio, paid straight to the account for activated offers in shops and online.",
              s=["con"], lc="grow", o="P", at="Dateio", neo=[0, "Dateio."],
              mc="Mastercard's card-linked offers could compete with or feed it.",
              src=[["Erste Bank: Moneyback", MONEYBACK]]),
            P("movesave", "Move & Save", "Turns Apple Watch activity goals into transfers to savings, a securities plan or gold.",
              s=["inv"], lc="grow", o="B", neo=[0, ""], src=[["Erste Bank: Move & Save", MOVE]]),
            P("georgefit", "George FIT", "A free budgeting and financial-health companion in the George app for everyone from 14.",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["Erste Bank: George FIT", GFIT]]),
            P("zweite", "Zweite Sparkasse", "A bank for people in financial difficulty, run by volunteers; more than 27,200 accounts since 2006.",
              s=["con"], lc="open", o="B", neo=[0, ""], src=[["Erste Bank und Sparkassen factsheet 2026", FACT]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: accounts and home loans from Erste Bank and the Sparkassen, investing through George Invest and Erste Asset Management, business cards and virtual cards, corporate and markets banking, Erste Bank Polska and six more CEE banks.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Accounts & home loans", "blurb": "22,550 homes in 2025.", "div": "ebo", "rev": "ebo", "products": [
            P("accounts", "Current accounts", "s Kompakt, Plus and online accounts, free youth (spark7) and student accounts and a basic payment account, opened online in George, with a free switching service.",
              s=["con"], lc="open", neo=[1, "Every account card is a Debit Mastercard."], src=[["Erste Bank: accounts and cards", KK]]),
            P("housing", "Home loans & s Bausparkasse", "22,550 home loans in 2025 across Erste Bank and the Sparkassen, with s Bausparkasse building-society savings and loans.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["Erste Bank und Sparkassen factsheet 2026", FACT], ["H1 2026 half-year report", HYR]]),
        ]},
        {"id": "4.2", "ic": "chart-candlestick", "name": "Investing", "blurb": "€112bn under management.", "div": "eam", "rev": "oat", "products": [
            P("invest", "George Invest & Erste Asset Management", "George Invest in Austria, the Czech Republic and Slovakia (customers' average age 35), 2.2 million securities savings plans (up 21.4%) and €112 billion managed by Erste Asset Management at June 2026.",
              s=["inv"], lc="grow", o="B", neo=[0, ""], src=[["H1 2026 results presentation", PRES], ["Erste Bank: George Invest", GINV]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "Business banking", "blurb": "232,000 commercial clients.", "div": "ebo", "rev": "ebo", "products": [
            P("bizcards", "Business credit cards", "Business Smartcard (from €1 a month, 0.5% cashback, on Visa), Business Premiumcard and Premiumcard Plus with travel cover ⚠ premium networks not stated; blocked merchant categories and receipt upload in George.",
              s=["sme"], lc="everyday", o="B", at="Visa", neo=[0, "Visa (Smartcard); others not stated ⚠."], src=[["Erste Bank: business cards", BIZCARDS], ["Erste Bank: Business Smartcard", BIZSMART]]),
            P("virtual", "Business Virtualcards", "Up to 120 virtual credit cards for €12 a month (free if signed by 31 December 2026), created in George Business with limits, budgets and expiry per card.",
              s=["sme"], lc="everyday", st="new", o="B", neo=[None, "Network not stated."],
              mc="Virtual commercial cards with spend controls are Mastercard's ground.",
              src=[["Erste Bank: Business Virtualcards", VIRTUAL]]),
            P("yokoy", "Expense management with Yokoy", "AI expense software linked to George Business: card transactions flow in automatically, are matched to receipts and posted to the ledger.",
              s=["sme", "corp"], lc="everyday", o="P", at="Yokoy", neo=[0, ""], src=[["Erste Bank: Yokoy", YOKOY]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Corporates & markets", "blurb": "193 capital-markets deals in H1.", "div": "group", "rev": "oat", "products": [
            P("corp", "Group Corporates & Markets", "Corporate lending up 7.0% a year to June 2026, 193 equity and debt mandates in H1 2026, and a cross-border alliance with Santander for corporate, cash-management and trade business.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["H1 2026 results presentation", PRES], ["Erste: Polish deal completed, Jan 2026", POL]]),
        ]},
        {"id": "4.5", "ic": "flag", "name": "Erste Bank Polska", "blurb": "6.2 million customers.", "div": "ebp", "rev": "pl", "products": [
            P("ebp", "Erste Bank Polska", "Poland's third-largest bank by assets: about 6.2 million customers, 10,222 staff, loans of €41.4 billion and €183 million of net result for the group in H1 2026; more than 300,000 new customers in the half.",
              s=["con", "corp"], lc="everyday", st="new", ay="Jan 2026", o="A", neo=[None, "Card networks not researched ⚠."],
              mc="The group's largest new card book, and its network split is not public here.",
              src=[["H1 2026 half-year report", HYR], ["H1 2026 results presentation", PRES], ["H1 2026 results release", H1PR]]),
        ]},
        {"id": "4.6", "ic": "earth", "name": "CEE banks", "blurb": "Six more markets.", "div": "cee", "rev": "cee", "products": [
            P("ceebanks", "Česká spořitelna, Slovenská sporiteľňa & others", "Banks in the Czech Republic (4.6 million customers), Slovakia (1.9 million), Romania (3.0 million), Hungary (1.2 million), Croatia (1.4 million) and Serbia; about two-thirds of group profit comes from outside Austria.",
              s=["con", "corp"], lc="everyday", o="A", neo=[None, "Covered separately ⚠."], src=[["H1 2026 results presentation", PRES], ["2025 results, Feb 2026", FY25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Erste: George for 2.6 million Austrians and 11.8 million across the group, 714 Austrian branches, and George Business.",
    "tiles": [
        {"id": "5.1", "ic": "monitor", "name": "George", "blurb": "11.8 million users.", "div": "george", "rev": "ebo", "products": [
            P("george", "George & the George app", "2.6 million users in Austria and more than 11.8 million across seven markets; card blocking, PIN display, limits and wallet set-up all in the app; 73% of group sales are digital.",
              s=["con", "inv", "trav"], lc="everyday", o="B", neo=[0, ""], src=[["Erste Bank und Sparkassen factsheet 2026", FACT], ["H1 2026 results presentation", PRES]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "714 in Austria.", "div": "spk", "rev": "spk", "products": [
            P("branches", "Branches & advisers", "714 branches in Austria in mid-2026 (732 at end-2025) across Erste Bank and the Sparkassen, plus video and phone advice.",
              s=["con", "home"], lc="open", neo=[0, ""], src=[["H1 2026 results presentation", PRES], ["Erste Bank und Sparkassen factsheet 2026", FACT]]),
        ]},
        {"id": "5.3", "ic": "briefcase-business", "name": "George Business", "blurb": "85,000 clients.", "div": "george", "rev": "ebo", "products": [
            P("gbiz", "George Business", "Business banking for sole traders up to large companies, with roles, multibanking and card controls; about 85,000 clients onboarded across the group, up 12% in 2026.",
              s=["sme", "corp"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["Erste Bank: George Business", GBIZ], ["H1 2026 results presentation", PRES]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Erste", "blurb": "Debit, Miles & More, half of credit.", "products": [
        P("mcaterste", "Mastercard at Erste", "Mastercard carries every Erste Bank and Sparkasse debit card in Austria (since 2019), the Austrian Miles & More cards Erste won in 2025, half of the Smartcard and Premiumcard range and Identity Check. Visa holds the other half of credit, the GÖD cards and the Business Smartcard; no group-wide network deal is public ⚠.",
          s=["con"], div="ebo", rev="ebo", mc="The relationship this map is drawn for.",
          src=[["futurezone: Maestro gone by mid-2020, Nov 2019", MAESTRO], ["Leadersnet: AUA and Miles & More, Aug 2025", MMNEWS], ["Erste Bank: card comparison", CCOMP]]),
    ]},
    {"id": "pillar-market", "name": "Austria & CEE", "blurb": "Wero, levies, growth.", "products": [
        P("market", "The market", "Wero entering Austria with Erste and Raiffeisen as EPI shareholders (June 2026), €392 million of bank levies across the group in H1 2026, and Central Europe as the growth region behind the 2030 plan.",
          s=["con"], div="group", rev="oat", src=[["Trending Topics: Wero, Jun 2026", WERO], ["H1 2026 half-year report", HYR]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
