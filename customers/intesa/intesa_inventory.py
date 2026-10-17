"""Intesa Sanpaolo's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results (29 July 2026), the 2025 results
and the 2026–2029 Business Plan (both 2 February 2026), and the Italian product pages of intesasanpaolo.com and
isybank.com. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://group.intesasanpaolo.com/content/dam/portalgroup/repository-documenti/investor-relations/comunicati-stampa-en/2026/07/20260729_Ris1H26_uk.pdf"
FY25 = "https://group.intesasanpaolo.com/en/investor-relations/press-releases/2026/02/20260202-ris-fy25-uk"
BP = "https://group.intesasanpaolo.com/en/investor-relations/press-releases/2026/02/20260202-business-plan-uk"
BOD = "https://group.intesasanpaolo.com/en/governance/bod"
ORG = "https://group.intesasanpaolo.com/en/about-us/organisational-structure"
RATINGS = "https://group.intesasanpaolo.com/en/investor-relations/ratings"
PROFILE = "https://group.intesasanpaolo.com/en/about-us/profile"
SHARE = "https://group.intesasanpaolo.com/en/about-us/shareholder-base"
HIST = "https://group.intesasanpaolo.com/en/about-us/history"
BORSA = "https://www.borsaitaliana.it/borsa/azioni/scheda/IT0000072618.html?lang=en"
CARDS = "https://www.intesasanpaolo.com/it/persone-e-famiglie/prodotti/carte.html"
XDEBIT = "https://www.intesasanpaolo.com/it/persone-e-famiglie/prodotti/carte/carte-di-debito/xme-debit-card.html"
XCC = "https://www.intesasanpaolo.com/it/persone-e-famiglie/prodotti/carte/carte-di-credito/xme-credit-card.html"
ICON = "https://www.intesasanpaolo.com/it/persone-e-famiglie/prodotti/carte/carte-di-credito/xme-credit-icon.html"
EXCL = "https://www.intesasanpaolo.com/it/persone-e-famiglie/prodotti/carte/carte-di-credito/carta-di-credito-exclusive.html"
DIGPAY = "https://www.intesasanpaolo.com/it/persone-e-famiglie/prodotti/pagamenti-digitali.html"
BIZCARDS = "https://www.intesasanpaolo.com/it/business/prodotti/carte-di-pagamento-e-carte-di-credito-aziendali.html"
POS = "https://www.intesasanpaolo.com/it/business/prodotti/soluzioni-pos-nexi-gestione-pagamenti.html"
ISY = "https://www.isybank.com/it/"
ISYDEB = "https://www.isybank.com/it/carte/carta-di-debito.html"
ISYCC = "https://www.isybank.com/it/carte/carta-di-credito.html"
ISYPRE = "https://www.isybank.com/it/carte/carta-prepagata.html"
VISA24 = "https://group.intesasanpaolo.com/it/newsroom/comunicati-stampa/2024/11/visa-e-intesa-sanpaolo--rinnovata-partnership-strategica"
MC20 = "https://group.intesasanpaolo.com/it/newsroom/comunicati-stampa/2020/07/intesa-sanpaolo-e-mastercard-annunciano-partnership-per-sostener"
MC14 = "https://www.pagamentidigitali.it/?p=2840"
BIO = "https://www.electronicpaymentsinternational.com/news/intesa-sanpaolo-partnership/"
EXCL21 = "https://www.aziendabanca.it/notizie/banche/carta-exclusive-intesa-sanpaolo"
SETEFI = "https://www.aziendabanca.it/notizie/intesa-sanpaolo-cessione-setefi-intesa-sanpaolo-card-a-mercury"
NEXI19 = "https://group.intesasanpaolo.com/it/investor-relations/comunicati-stampa-price-sensitive/2019/12/20191219_csn_it"
NEXI20 = "https://group.intesasanpaolo.com/it/sala-stampa/news/innovazione-digitale-e-fintech/2020/perfezionato-accordo-strategico-nexi"
ISYAGCM = "https://www.fintechfutures.com/bankingtech/italian-competition-authority-interrupts-migration-of-2-4m-intesa-sanpaolo-accounts-to-isybank"
EURBANK = "https://en.startmag.it/economia-2/atm-all-the-banks-betting-on-eur-bank-the-euro-stablecoin/"
CRYPTO = "https://clear.checksig.com/2026-06-05-intesa-sanpaolo-increases-crypto-exposure/"
BANCOMAT = "https://bancomat.it/en/news-eventi/interview-il-sole-24-ore-fabrizio-burlando-we-want-to-make-bancomat-the-digital-currency-of-italians"
FSI = "https://www.fondofsi.it/en/press-releases/bancomat-and-fsi-to-form-strategic-partnership-for-european-growth-project/"
AI80 = "https://www.fortuneita.com/?p=376900"
ALEX = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2024/march/mastercard-and-alexbank-announce-partnership-to-enhance-the-financial-services-landscape-and-drive-inclusive-growth-in-egypt"
SATIS = "https://app.welcometothejungle.com/jobs/lwajyPar"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · governance · cloud", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Italy's largest bank with €437 billion of loans and a record €9.3 billion profit in 2025, a merger history from Cariplo to UBI, a cloud core called isytech, and a 2026–2029 plan for €11.5 billion of profit.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "€5.6bn net income in H1 2026.", "div": "isp", "rev": "cc", "products": [
            P("balance", "Balance sheet & earnings", "Net income of €5,554 million in H1 2026 (+6.5%) and a record €9,321 million in 2025 (ROTE 22%); loans of €437 billion, banking deposits of €612 billion and customer financial assets of €1,511 billion at 30 June 2026; the 2026 outlook raised to more than €10 billion.",
              s=["con", "corp"], neo=[0, ""], src=[["H1 2026 results", H1], ["2025 results", FY25]]),
            P("capital", "Capital, ratings & shareholders", "CET1 13.1% after distributions; rated A3 (Moody's), BBB+ (S&P), A- (Fitch) and A (DBRS); worth about €107 billion at €6.148 a share on 16 October 2026 ⚠ derived; BlackRock 6.7%, Compagnia di San Paolo 6.7% and Fondazione Cariplo 5.5%.",
              s=["corp"], neo=[0, ""], src=[["Intesa Sanpaolo: ratings", RATINGS], ["Intesa Sanpaolo: shareholder base", SHARE], ["Borsa Italiana: ISP", BORSA]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & heritage", "blurb": "Messina; Intesa and Sanpaolo since 2007.", "div": "isp", "rev": "cc", "products": [
            P("leadership", "Board & top management", "Board appointed 29 April 2025 for 2025–2027: Chair Gian Maria Gros-Pietro, CEO Carlo Messina (the only executive director); division heads S. Barrese (Banca dei Territori), M. Micillo (IMI CIB), P. Papanicolaou (International Banks) and T. Corcos (Wealth Management); M. Proverbio is Chief Data, A.I. and Technology Officer.",
              s=["corp"], neo=[0, ""], src=[["Intesa Sanpaolo: board", BOD], ["Intesa Sanpaolo: top management", ORG]]),
            P("heritage", "Heritage & scale", "Formed on 1 January 2007 from Banca Intesa and Sanpaolo IMI, with UBI Banca bought in 2020 and merged in 2021; about 13.9 million customers in Italy and 7.5 million abroad, 3,567 branches and 89,725 staff at 30 June 2026.",
              s=["con"], o="I", neo=[0, ""], src=[["Intesa Sanpaolo: history", HIST], ["Intesa Sanpaolo: profile", PROFILE], ["H1 2026 results", H1]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "isytech & AI", "blurb": "68% of apps in the cloud.", "div": "isp", "rev": "cc", "products": [
            P("tech", "isytech, cloud & AI", "A cloud-native core first used by Isybank and being extended across the group: €5.6 billion of IT investment in 2022–2025, about 2,430 IT specialists hired, 68% of applications in the cloud at June 2026 (100% targeted by 2029), 153 AI apps in 2025 and 19 AI, GenAI and agentic-AI projects launched in H1 2026.",
              s=["corp"], st="new", neo=[0, ""],
              mc="Agentic AI is in the plan; no network's agent payments are attached to it yet.",
              src=[["2025 results", FY25], ["H1 2026 results", H1], ["2026–2029 Business Plan", BP]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "2026–2029 plan", "blurb": "€11.5bn profit by 2029.", "div": "isp", "rev": "cc", "products": [
            P("strategy", "2026–2029 Business Plan", "Net income above €11.5 billion and ROTE of 27% in 2029, about €50 billion distributed over 2025–2029, cost:income of 36.8%, €4.6 billion for technology and growth, 2.5 million more customers (to about 24 million) and isywealth Europe from 2027; press reports say AI should resolve about 80% of customer requests by 2029 ⚠.",
              s=["corp"], st="new", ay="Feb 2026", neo=[0, ""], src=[["2026–2029 Business Plan", BP], ["Fortune Italia: plan and AI", AI80]]),
            P("deals", "Payments deals", "Setefi and Intesa Sanpaolo Card (processing) sold to Mercury, now Nexi, for €1.035 billion in 2016 with a ten-year service contract ⚠ renewal not found; merchant acquiring (380,000 points of sale) to Nexi for €1 billion with a 9.9% Nexi stake (closed June 2020).",
              s=["sme"], o="P", at="Nexi", neo=[0, ""],
              mc="The 2016 processing contract reaches ten years in 2026, a natural moment to revisit card economics.",
              src=[["AziendaBanca: Setefi sale, May 2016", SETEFI], ["Intesa Sanpaolo: Nexi agreement, Dec 2019", NEXI19], ["Intesa Sanpaolo: Nexi closing, Jun 2020", NEXI20]]),
            P("processing", "Card processing", "Issuing processing outsourced with the sale of Setefi and Intesa Sanpaolo Card in 2016 under a ten-year contract, now with Nexi ⚠ renewal terms not public.",
              s=["corp"], lc="move", o="P", at="Nexi", st="unconf", neo=[0, "Nexi."],
              src=[["AziendaBanca: Setefi sale, May 2016", SETEFI]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: debit co-badged Bancomat with Visa or Mastercard, credit in either network, the Exclusive cards on Mastercard alone, prepaid mostly on Mastercard, Isybank cards on Mastercard, BANCOMAT Pay and wallets, acceptance through Nexi, and instant transfers and stablecoin pilots.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Bancomat plus Visa or Mastercard.", "div": "isp", "rev": "bdt", "products": [
            P("debit", "XME Debit Card & XME Card Plus", "Debit co-badged with BANCOMAT/PagoBANCOMAT for domestic use and the customer's choice of Visa or Mastercard abroad and online; can be digital-only, €1.50 a month, works in wallets, with a virtual card number for online shopping; XME Card Plus for children from eight.", short="Debit (Bancomat + Visa or Mastercard)",
              s=["con"], lc="everyday", o="P", at="Bancomat, Visa, Mastercard", neo=[1, "Bancomat with Visa or Mastercard, per card."],
              mc="Every debit card is a fresh choice between Visa and Mastercard; the domestic leg stays Bancomat.",
              src=[["Intesa Sanpaolo: XME Debit Card", XDEBIT], ["Intesa Sanpaolo: cards", CARDS]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Either network, by choice.", "div": "isp", "rev": "bdt", "products": [
            P("credit", "XME Credit Card & XME Credit Icon", "XME Credit Card (limit up to €3,000, €5 a month) and XME Credit Icon (up to €100,000 a month, €7.50) on Mastercard or Visa; the Visa version of Icon carries my Visa offers under the renewed Visa partnership; SpensieRata spreads purchases of €200 to €5,000.", short="Credit (Mastercard or Visa)",
              s=["con"], lc="borrow", o="P", at="Mastercard, Visa", neo=[1, "Mastercard or Visa, per card."],
              src=[["Intesa Sanpaolo: XME Credit Card", XCC], ["Intesa Sanpaolo: XME Credit Icon", ICON]]),
        ]},
        {"id": "2.3", "ic": "gem", "name": "Exclusive & prepaid", "blurb": "Mastercard-led cards.", "div": "isp", "rev": "bdt", "products": [
            P("exclusive", "Carta di Credito & Debito Exclusive", "The affluent cards: Exclusive credit (May 2021, €58 a month) with a 24/7 concierge, more than 1,200 airport lounges, insurance and Exclusive Club points, and an Exclusive debit card co-badged Bancomat; both on Mastercard, with fee-free euro spending at Mastercard merchants.", short="Exclusive (Mastercard)",
              s=["excl"], lc="everyday", ay="May 2021", o="P", at="Mastercard", neo=[2, "Mastercard only."],
              mc="Mastercard's strongest ground at Intesa: the affluent segment the plan wants to grow abroad.",
              src=[["Intesa Sanpaolo: Exclusive credit card", EXCL], ["AziendaBanca: Exclusive debit, Nov 2021", EXCL21]]),
            P("prepaid", "Superflash, Flash, Pensione & university cards", "Prepaid cards with an IBAN: Superflash (loads up to €10,000), Carta Pensione and university badge cards (La Statale, Siena, NABA, ERDIS and others) on Mastercard; Carta Flash nominativa on Mastercard or Visa.",
              s=["con", "young"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard, bar Flash's Visa option."],
              src=[["Intesa Sanpaolo: cards", CARDS]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Isybank cards", "blurb": "Issued on Mastercard ⚠.", "div": "isybank", "rev": "bdt", "products": [
            P("isycards", "Isybank debit, credit & prepaid", "Digital debit on isyLight and physical debit on isySmart and isyPrime, a €3.90-a-month credit card and a prepaid card, all in Apple Pay, Google Pay and Samsung Pay; a current promotion targets holders of an \"isybank card issued on the Mastercard network\" ⚠ Visa not ruled out.", short="Isybank cards (Mastercard ⚠)",
              s=["young"], lc="everyday", st="new", o="P", at="Mastercard", neo=[2, "Mastercard ⚠ from Isybank's own promotion."],
              mc="The growth engine of the plan appears to issue on Mastercard.",
              src=[["Isybank: debit card", ISYDEB], ["Isybank: credit card", ISYCC], ["Isybank: prepaid card", ISYPRE]]),
            P("receive", "Card-receive service", "Isybank cards can receive money sent over the Mastercard or Visa network the card is enabled for, from other cardholders or from merchants, with some countries excluded.",
              s=["young"], lc="move", o="P", at="Mastercard, Visa", neo=[1, "Mastercard Send or Visa Direct, per card ⚠."],
              src=[["Isybank: debit card", ISYDEB]]),
        ]},
        {"id": "2.5", "ic": "send", "name": "Wallets & BANCOMAT Pay", "blurb": "11m enabled for BANCOMAT Pay.", "div": "isp", "rev": "bdt", "products": [
            P("wallets", "Apple Pay, Google Pay, Samsung Pay & wearables", "Card wallets and wearables for Intesa and Isybank cards, with the card number never shared.",
              s=["con", "young"], lc="move", o="P", at="Apple, Google, Samsung", neo=[1, "Tokens of whichever network the card carries."],
              src=[["Intesa Sanpaolo: digital payments", DIGPAY], ["Isybank: debit card", ISYDEB]]),
            P("bpay", "BANCOMAT Pay", "Phone-number transfers, QR payments in shops and pagoPA bills inside the Intesa and Isybank apps; more than 11 million Italians are enabled and every Intesa POS accepts it.",
              s=["con", "sme"], lc="move", o="P", at="Bancomat", neo=[0, "Domestic scheme."],
              mc="The domestic rail Intesa co-owns competes with cards at the counter and between people.",
              src=[["Intesa Sanpaolo: digital payments", DIGPAY], ["Intesa Sanpaolo: Nexi POS", POS]]),
            P("masterpass", "MasterPass", "In July 2014 Intesa and Mastercard agreed a broad partnership on e-commerce, and Intesa set out to be the first Italian bank on MasterPass, Mastercard's online wallet, from October 2014; Stefano Barrese, now head of Banca dei Territori, led it. MasterPass has since given way to Click to Pay ⚠ no Intesa Click to Pay found.",
              s=["con"], lc="move", st="retired", ay="Oct 2014", o="P", at="Mastercard", neo=[3, "Mastercard's own; retired ⚠."],
              mc="An early Mastercard e-commerce tie; Click to Pay has not followed in public sources.",
              src=[["Pagamenti Digitali: MasterPass, Jul 2014", MC14]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acceptance with Nexi", "blurb": "Exclusive partner since 2020.", "div": "isp", "rev": "bdt", "products": [
            P("accept", "Nexi POS, SoftPOS & XPay", "Nexi is Intesa's exclusive acceptance partner: SoftPOS (Intesa was the first Italian bank to offer it, in 2023), SmartPOS, mobile POS and the XPay e-commerce gateway, taking BANCOMAT, Visa, Maestro, Mastercard, JCB, UnionPay, Diners and Amex.",
              s=["sme"], lc="move", o="P", at="Nexi", neo=[1, "Accepts every network."],
              src=[["Intesa Sanpaolo: Nexi POS", POS], ["2025 results", FY25], ["Intesa Sanpaolo: Nexi agreement, Dec 2019", NEXI19]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Instant & digital money", "blurb": "Eur.Bank and Qivalis.", "div": "isp", "rev": "cc", "products": [
            P("instant", "Instant transfers & Mooney", "Free SEPA and instant transfers on every Isybank plan, and instant banking (bills, top-ups, cash) at Mooney points through the partnership with the Enel group.",
              s=["con", "young"], lc="move", o="P", at="Mooney, Enel", neo=[0, "Account-to-account."],
              src=[["Isybank", ISY], ["H1 2026 results", H1]]),
            P("digitalmoney", "Stablecoins & crypto", "One of nine Italian banks testing Bancomat's euro stablecoin Eur.Bank (from 3 June 2026, no customer use yet), a member of the 37-bank Qivalis consortium, and about $235 million of own-account crypto exposure at March 2026 after buying 11 bitcoin in January 2025.",
              s=["corp"], lc="move", st="new", o="P", at="Bancomat, Qivalis", neo=[0, "Not on Mastercard."],
              mc="Stablecoin settlement is being built with Bancomat and other banks, not with a card network.",
              src=[["Startmag: Eur.Bank, Jun 2026", EURBANK], ["Checksig: Intesa crypto, Jun 2026", CRYPTO]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card and account: in-house security with Geocontrol and virtual numbers, AI and agentic projects, rewards and the Exclusive Club, instalments, and processing bought from Nexi.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security & fraud", "blurb": "Geocontrol, 3-D Secure.", "div": "isp", "rev": "bdt", "products": [
            P("fraud", "Card security & fraud", "A Chief Security Officer on the executive team, 3-D Secure, Geocontrol to choose where a card works, virtual card numbers, biometric confirmation in wallets and AI-led early-warning models; no Mastercard fraud tool was found in public sources ⚠.",
              s=["con", "sme"], lc="everyday", neo=[0, "Intesa's own."],
              mc="Scam and A2A fraud scores would fit as instant payments grow.",
              src=[["Intesa Sanpaolo: XME Debit Card", XDEBIT], ["Intesa Sanpaolo: top management", ORG], ["H1 2026 results", H1]]),
            P("biocard", "Biometric card pilot", "Intesa and Gemalto trialled Italy's first biometric contactless Mastercard, with a fingerprint sensor on the card ⚠ date about 2019, outcome not found.",
              s=["con"], lc="everyday", st="retired", o="P", at="Mastercard, Gemalto", neo=[2, "Mastercard card ⚠."],
              src=[["Electronic Payments International: biometric pilot", BIO]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI for customers", "blurb": "19 agentic and GenAI projects.", "div": "isp", "rev": "cc", "products": [
            P("ai", "AI & agentic projects", "153 AI apps and about 300 specialists in 2025, 19 AI, GenAI and agentic-AI projects launched in H1 2026, and an aim, per the press, for AI to resolve about 80% of customer requests by 2029 ⚠.",
              s=["con", "excl"], lc="everyday", st="new", neo=[0, ""],
              mc="Agent Pay and Mastercard's agentic tokens are untouched ground.",
              src=[["2025 results", FY25], ["H1 2026 results", H1], ["Fortune Italia: plan and AI", AI80]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & offers", "blurb": "Contests, Club points, my Visa.", "div": "isp", "rev": "bdt", "products": [
            P("rewards", "Rewards, Exclusive Club & isyReward", "The \"Intesa Sanpaolo 2027\" prize contest for card sign-up and use, Exclusive Club points on the Exclusive credit card, isyReward and isyToken Collection in Isybank, and Visa's my Visa and Visa Destinations on Visa cards.",
              s=["con", "excl", "young"], lc="grow", o="B", neo=[1, "Visa runs the network offers; Mastercard runs promotions on Isybank cards."],
              mc="Mastercard has no card-linked offer programme here; Visa has my Visa.",
              src=[["Intesa Sanpaolo: XME Credit Icon", ICON], ["Intesa Sanpaolo: Exclusive credit card", EXCL], ["Isybank", ISY]]),
            P("donations", "ATM donations with Mastercard", "A three-year partnership from July 2020 let holders of Mastercard and Maestro debit and prepaid cards donate to Caritas food projects at about 8,000 Intesa ATMs through For Funding; Michele Centemero of Mastercard Italy called it a shared project, and Intesa called Mastercard a \"consolidated partner\". The Exclusive card also gives half its domestic scheme fees to a social project.",
              s=["con", "excl"], lc="beyond", st="retired", ay="Jul 2020", o="P", at="Mastercard, Caritas", neo=[2, "Mastercard and Maestro cards ⚠ ended 2023."],
              mc="The only dated joint Mastercard programme in Italy in recent years.",
              src=[["Intesa Sanpaolo and Mastercard, Jul 2020", MC20], ["Intesa Sanpaolo: Exclusive credit card", EXCL]]),
        ]},
        {"id": "3.4", "ic": "refresh-cw", "name": "Instalments", "blurb": "SpensieRata, €200–€5,000.", "div": "isp", "rev": "bdt", "products": [
            P("spensierata", "SpensieRata", "A credit line that spreads card purchases of €200 to €5,000, offered on XME Credit Card and XME Credit Icon and in Isybank.",
              s=["con", "young"], lc="borrow", o="B", neo=[0, "Intesa's own credit line."],
              mc="A natural home for Mastercard Installments at checkout.",
              src=[["Intesa Sanpaolo: XME Credit Card", XCC], ["Isybank", ISY]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail and Exclusive banking in Italy, Isybank's 1.2 million digital customers, business banking, IMI corporate and investment banking, wealth through Fideuram and Eurizon, insurance, and banks in twelve other countries.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Retail & Exclusive", "blurb": "Banca dei Territori, 43% of income.", "div": "isp", "rev": "bdt", "products": [
            P("accounts", "XME accounts, mortgages & loans", "Banca dei Territori serves retail, Exclusive, enterprise and non-profit clients: €6.2 billion of operating income and €1.7 billion of net income in H1 2026, about 43% of the group, with €220 billion of loans.",
              s=["con", "excl"], lc="everyday", neo=[1, "Cards split between Visa and Mastercard."], src=[["H1 2026 results", H1]]),
        ]},
        {"id": "4.2", "ic": "rocket", "name": "Isybank", "blurb": "1.2 million customers.", "div": "isybank", "rev": "bdt", "products": [
            P("isybank", "Isybank", "The app-only bank on isytech: about 1.2 million customers and 1,050,000 accounts opened by new customers (150,000 in H1 2026), with plans at €0, €3.90 and €9.90 a month; in 2023 the antitrust authority halted the move of 2.4 million existing accounts onto it.",
              s=["young"], lc="open", st="new", ay="2023", o="B", neo=[2, "Cards on Mastercard ⚠."],
              mc="The main source of the 2.5 million new customers planned to 2029.",
              src=[["H1 2026 results", H1], ["Isybank", ISY], ["FinTech Futures: Isybank migration halted, Dec 2023", ISYAGCM]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "Business banking", "blurb": "Cards, POS, factoring.", "div": "isp", "rev": "bdt", "products": [
            P("business", "Business accounts & cards", "Business accounts with Carta Debit Plus (Bancomat with Visa or Mastercard), Carta Credit and Carta Prepaid (up to €60,000) ⚠ networks not stated, Carta Deposit for cash, and Visa Business Solutions reporting on commercial Visa cards since June 2024.",
              s=["sme"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Debit split; commercial credit leans Visa ⚠."],
              mc="Commercial cards and spend controls are where Visa has moved first.",
              src=[["Intesa Sanpaolo: business cards", BIZCARDS], ["Visa and Intesa Sanpaolo, Nov 2024", VISA24]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "IMI CIB", "blurb": "€3.0bn H1 income.", "div": "imi", "rev": "imi", "products": [
            P("cib", "IMI Corporate & Investment Banking", "Global corporates in eight industries, financial institutions, Global Transaction Banking, structured finance and capital markets: €2.96 billion of operating income in H1 2026 (+17.5%) and €134.5 billion of loans.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["H1 2026 results", H1]]),
        ]},
        {"id": "4.5", "ic": "chart-candlestick", "name": "Wealth & insurance", "blurb": "€1.5 trillion of client assets.", "div": "fideuram", "rev": "wm", "products": [
            P("wealth", "Fideuram, Eurizon & Fideuram Direct", "Private banking through Fideuram, Intesa Sanpaolo Private Banking and Reyl; Eurizon in asset management; Fideuram Direct online (81,000 customers at end-2025); H1 2026 net income of €840 million in Private Banking and €297 million in Asset Management; isywealth Europe from 2027.",
              s=["excl"], lc="grow", neo=[0, ""], src=[["H1 2026 results", H1], ["2025 results", FY25], ["2026–2029 Business Plan", BP]]),
            P("insurance", "Insurance", "Intesa Sanpaolo Assicurazioni, Protezione, Fideuram Vita and InSalute Servizi: €531 million net income in H1 2026, with card insurance bundled into credit cards.",
              s=["con", "excl"], lc="grow", neo=[0, ""], src=[["H1 2026 results", H1]]),
        ]},
        {"id": "4.6", "ic": "earth", "name": "International Banks", "blurb": "Twelve countries.", "div": "intl", "rev": "ibd", "products": [
            P("intl", "International subsidiary banks", "PBZ, VUB, CIB Bank, Bank of Alexandria, Banca Intesa Beograd and others in twelve countries: €611 million net income in H1 2026 (down 15%) and €52 billion of loans; Bank of Alexandria signed a Mastercard partnership on credit cards and acquiring in March 2024.",
              s=["intl"], lc="everyday", o="I", neo=[1, "Varies by bank; Mastercard partner in Egypt."],
              src=[["H1 2026 results", H1], ["Mastercard and ALEXBANK, Mar 2024", ALEX]]),
            P("beograd", "Banca Intesa Beograd", "Serbia's largest bank and part of the International Banks Division; its cards (Visa and DinaCard debit, Mastercard and Amex credit) are mapped on its own page.",
              s=["intl"], lc="everyday", o="A", neo=[1, "See the Banca Intesa Beograd page."],
              src=[["H1 2026 results", H1], ["Intesa Sanpaolo: profile", PROFILE]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the Intesa Sanpaolo Mobile app and internet banking, the Isybank app, 2,644 Italian branches and the digital branch, and about 19,100 advisers.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "Intesa Sanpaolo Mobile, Isybank.", "div": "isp", "rev": "bdt", "products": [
            P("app", "Intesa Sanpaolo Mobile & Isybank app", "Omnichannel journeys that start in the app and finish in a branch, cards issued digitally and pushed to wallets, cardless ATM withdrawals and BANCOMAT Pay built in; Isybank is app-only.",
              s=["con", "young"], lc="open", neo=[0, ""], src=[["Intesa Sanpaolo: XME Debit Card", XDEBIT], ["Isybank", ISY]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "2,644 branches in Italy.", "div": "isp", "rev": "bdt", "products": [
            P("branches", "Branches, digital branch & ATMs", "2,644 branches in Italy at June 2026 after 1,502 closures since late 2021, a remote Filiale Digitale open until midnight, and about 8,000 ATMs (2020).",
              s=["con", "excl"], lc="everyday", st="flux", neo=[0, ""], src=[["H1 2026 results", H1], ["2025 results", FY25], ["Intesa Sanpaolo and Mastercard, Jul 2020", MC20]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Advisers & partners", "blurb": "19,100 advisers.", "div": "fideuram", "rev": "wm", "products": [
            P("advisers", "Advisers & partners", "About 19,100 financial advisers, private bankers, Global Advisors and relationship managers, plus partners: Nexi for acceptance, Mooney and Enel for proximity, BlackRock for wealth and Bancomat for the domestic scheme.",
              s=["excl", "sme"], lc="grow", neo=[0, ""], src=[["H1 2026 results", H1], ["2026–2029 Business Plan", BP]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Intesa", "blurb": "Exclusive, Isybank, prepaid; Visa renewed.", "products": [
        P("mcatintesa", "Mastercard at Intesa Sanpaolo", "A dual-network issuer: customers choose Visa or Mastercard on debit and most credit, while the Exclusive cards, most prepaid cards and, it appears, Isybank's cards run on Mastercard alone. Mastercard's dated joint work runs from MasterPass (2014) to Caritas ATM donations (2020); Visa renewed a multi-year strategic partnership in November 2024 and has the offers. Domestic debit is Bancomat, which Intesa co-controls.",
          s=["con"], div="isp", rev="bdt", mc="The relationship this map is drawn for.",
          src=[["Intesa Sanpaolo: cards", CARDS], ["Visa and Intesa Sanpaolo, Nov 2024", VISA24], ["Intesa Sanpaolo and Mastercard, Jul 2020", MC20], ["Pagamenti Digitali: MasterPass, Jul 2014", MC14]]),
    ]},
    {"id": "pillar-market", "name": "Italian payments", "blurb": "Bancomat, Satispay, Nexi.", "products": [
        P("market", "The Italian market", "About 30 million Bancomat cards, with FSI and a pact of Intesa, Iccrea, Banco BPM and BPER controlling 74.7%; Satispay with over 5 million users ⚠; Nexi as the dominant processor and acquirer; Bancomat's Eur.Bank stablecoin pilot; EU interchange caps and instant-payments rules.",
          s=["con"], div="isp", rev="bdt",
          src=[["Bancomat: CEO interview", BANCOMAT], ["FSI and Bancomat", FSI], ["Satispay: job listing", SATIS], ["Startmag: Eur.Bank, Jun 2026", EURBANK]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
