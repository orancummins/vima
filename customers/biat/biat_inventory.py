"""BIAT's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the 2025 annual report (published August 2026), the
Q1 2026 activity indicators (May 2026) and shareholder letter no. 76 with the H1 2026 figures (September 2026).
Amounts are in Tunisian dinars (TND). Most sources are French and are translated here. Card networks come from
BIAT's product pages on biat.tn; where a page does not name the network it is marked ⚠. ``neo`` is the Mastercard
lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

RA25 = "https://www.biat.com.tn/sites/default/files/2026-08/20260805-Rapport-annuel-2025-vdef.pdf"
RA24 = "https://www.biat.com.tn/sites/default/files/2025-12/20251202-RA-2024-ENG.pdf"
Q1 = "https://www.biat.com.tn/sites/default/files/2026-05/BIAT-indicateurs-d-activite-trimestriels-31-03-2026.pdf"
L76 = "https://www.biat.com.tn/sites/default/files/2026-09/lettre-a%CC%80-lactionnaire-BIAT-76.pdf"
AGM = "https://managers.tn/2026/04/24/la-biat-tient-son-assemblee-generale-ordinaire-au-titre-de-lexercice-2025/"
PRES = "https://www.biat.com.tn/la-biat/presentation-generale"
HIST = "https://www.biat.com.tn/la-biat/histoire"
DG = "https://www.biat.com.tn/la-direction-generale"
FIL = "https://www.biat.com.tn/la-biat/les-filiales"
YOUTH = "https://www.biat.com.tn/jeunes-entrepreneurs"
PRIV = "https://www.biat.com.tn/biat-la-une/press-media/la-biat-lance-lapplication-biat-privileges-une-marketplace-bancaire-dediee"
MYAWARD = "https://www.biat.com.tn/biat-la-une/actualites/mybiat-elue-produit-de-lannee-2026"
OVERT = "https://www.biat.com.tn/biat-la-une/press-media/la-biat-lance-biat-overt-et-renforce-son-engagement-en-faveur-de-la-finance"
BAD = "https://www.biat.com.tn/biat-la-une/press-media/la-biat-et-la-bad-scellent-un-partenariat-strategique-au-service-du"
PHISH = "https://www.biat.com.tn/biat-la-une/actualites/securite-bancaire-adoptez-les-bons-reflexes"
VISA22 = "https://managers.tn/2022/09/24/la-biat-signe-un-nouveau-partenariat-avec-visa/"
VINF14 = "https://www.leconomistemaghrebin.com/2014/11/12/tunisie-biat-lance-premiere-carte-visa-infinite/"
BUS16 = "https://africanmanager.com/?p=259205"
TRAVEL18 = "https://africanmanager.com/la-carte-allocation-touristique-biatravel-monte-en-gamme/"
PREPAID16 = "https://www.leconomistemaghrebin.com/2016/09/21/biat-lance-cartes-prepayees-internationales-tounessna-univers/"
FLEXY = "https://www.webmanagercenter.com/2025/10/01/552733/la-biat-lance-sa-nouvelle-carte-de-paiement-fractionne-biatflexy/"
# biat.tn product pages (read 17 October 2026)
T = "https://www.biat.tn/biat/Fr/"
CLASSIC = T + "carte-visa-ou-mastercard-classique_63_31"
FIRST = T + "pack-first_63_80"
EXPRESS = T + "pack-express_63_362"
VEXPRESS = T + "carte-visa-express_63_189"
PLAT = T + "carte-mastercard-platinum_63_33"
INF = T + "carte-visa-infinite_63_347"
PREMIER = T + "carte-visa-premier_63_32"
CPLAT = T + "classe-platinum_63_350"
ELITE = T + "classe-elite_63_349"
FLEXYPAGE = T + "carte-biat-flexy_63_410"
TRAVEL = T + "carte-travel_63_35"
CASH = T + "carte-cash_63_359"
FLY = T + "carte-fly_63_358"
HEDYA = T + "carte-hedya_63_360"
TECHNO = T + "carte-technologique-entreprise_63_393"
BUSINESS = T + "carte-business_63_371"
AFFAIRES = T + "cartes-affaires_63_95"
TPE = T + "terminal-de-paiement-electronique-tpe_63_96"
ECOM = T + "biat-e-commerce_63_364"
MYBIAT = T + "mybiat_63_37"
STARTUP = T + "pack-start-up_63_392"
RETAIL = T + "particuliers_58_4"
# market
BCTH1 = "https://businessnews.com.tn/2026/08/15/paiements-le-cheque-decroche-le-virement-domine-et-la-lettre-de-change-simpose/1414294/"
TUNPAY = "https://businessnews.com.tn/2026/05/06/la-bct-lance-le-label-unifie-tunpay-pour-le-paiement-mobile/1400181/"
SMT25 = "https://www.lapresse.tn/?p=3949015"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Tunisia's largest bank by deposits and income, TND 22.3 billion of deposits and TND 385 million of profit in 2025, about 40% owned by Groupe Mabrouk, fifty years of history, and a new IT subsidiary.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "First in deposits, ROE 16%.", "div": "biat", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings, 2025", "PNB of TND 1,594.8 million (+7.8%), net profit TND 385.3 million (+7.7%), ROE 16.3%, cost/income 44.6%; deposits TND 22,291 million (21.4% share, first) and net loans TND 13,045 million (second); solvency 15.81%, NPLs 6.7%. Group net profit TND 467.1 million.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025", RA25], ["Managers: AGM, Apr 2026", AGM]]),
            P("h1", "H1 2026", "At 30 June 2026: PNB TND 803 million (+1.9%, first in Tunisia), deposits TND 23,022 million (+9.9%, first), net loans TND 13,209 million (+1.4%, second). Q1 commissions were TND 69.2 million. Q3 figures are due in October 2026.",
              s=["corp"], st="new", neo=[0, ""], src=[["Shareholder letter 76, Sep 2026", L76], ["Q1 2026 indicators", Q1]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Owners & governance", "blurb": "Mabrouk 40%, Jebir CEO.", "div": "biat", "rev": "group", "products": [
            P("owners", "Ownership & listing", "Listed in Tunis since 1990 and the exchange's largest company: TND 6.9 billion at 30 June 2026 (14.2% of the market). Groupe Mabrouk has held about 40% since 2007; 99.8% of capital is Tunisian. Moody's rates deposits Caa1, outlook stable (March 2025).",
              s=["corp"], neo=[0, ""], src=[["Shareholder letter 76, Sep 2026", L76], ["BIAT: presentation", PRES], ["Annual report 2025", RA25]]),
            P("leadership", "Board & management", "Chairman Ismaïl Mabrouk (since 2009) and chief executive Elyes Jebir (since March 2024); 12 directors, two independent; COMEX and CODIR run the bank.",
              s=["corp"], neo=[0, ""], src=[["BIAT: management", DG], ["Annual report 2025", RA25]]),
            P("heritage", "Heritage & Fondation BIAT", "Founded in 1976 from the Tunisian branches of Société Marseillaise de Crédit and the British Bank of the Middle East; 50 years old in 2026. Fondation BIAT (2014) and the B@Labs incubator (2017) back young entrepreneurs.",
              s=["young"], o="I", neo=[0, ""], src=[["BIAT: history", HIST], ["BIAT: young entrepreneurs", YOUTH]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology & data", "blurb": "A new IT subsidiary.", "div": "tech", "rev": "group", "products": [
            P("tech", "BIAT Innovation & Technology", "IT moved into a new subsidiary (capital TND 2 million) to run digital and data development and security, with a central IT strategy unit, a data-governance organisation and a T24 core banking system ⚠; the card payment infrastructure was upgraded in 2024.",
              s=["corp"], st="new", neo=[0, ""], src=[["Annual report 2025", RA25], ["Annual report 2024 (English)", RA24]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy", "blurb": "Digital, green, trade.", "div": "biat", "rev": "group", "products": [
            P("strategy", "Strategy for 2026", "Faster digital journeys using the technology subsidiaries and AI, 70+ branches in the new format, green finance (TND 114 million of solar lending in 2025), trade support and non-banking offers. A plan after 2023–25 is not published ⚠.",
              s=["corp"], st="new", neo=[0, ""], src=[["Annual report 2025", RA25]]),
            P("groupmoves", "Group moves, 2020–26", "Tunisie Valeurs joined the group (2020), MyBIAT (2022), a six-year Visa deal (2022), MyBIAT Corporate (2024), BIAT France moved to IYU Europe (December 2024), Flexy (2025), and an AfDB US$50 million trade guarantee (February 2026). No bank or payments acquisitions.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025", RA25], ["BIAT: AfDB guarantee, Feb 2026", BAD]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: about 636,000 cards split between Visa and Mastercard, Visa at the top (Infinite, Premier, TEMPO credit, prepaid) and Mastercard in travel, Platinum and business cards, Flexy split payments, card acceptance through SMT, and transfers into and out of Tunisia.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "Visa or Mastercard.", "div": "retail", "rev": "retail", "products": [
            P("classic", "Visa or Mastercard classic", "The everyday debit card, on Visa or Mastercard at the customer's choice, in a domestic version or an international one for customers with transfer rights; contactless, with limits raised in 2025. BIAT had 635,633 cards in circulation at end-2024.", short="Classic (Visa or Mastercard)",
              s=["con", "pro"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Visa or Mastercard; split not published."],
              src=[["BIAT: classic card", CLASSIC], ["Annual report 2024 (English)", RA24]]),
            P("mcnational", "Mastercard national debit (Pack FIRST, Pack Express)", "The entry packs for young graduates and everyday customers carry a domestic 'MasterCard électronique' card, free in Pack FIRST.", short="Entry packs (Mastercard)",
              s=["young", "con"], lc="open", o="P", at="Mastercard", neo=[1, "Mastercard brand; domestic use switched by SMT ⚠."],
              src=[["BIAT: Pack FIRST", FIRST], ["BIAT: Pack Express", EXPRESS]]),
            P("visaexpress", "Visa Express", "An account-access card for ATM withdrawals up to TND 1,000 a day, payments and Tunisian online shopping; also the card for the savings pack.",
              s=["con", "pro"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["BIAT: Visa Express", VEXPRESS]]),
        ]},
        {"id": "2.2", "ic": "gem", "name": "Premium cards", "blurb": "Infinite on Visa, Platinum on Mastercard.", "div": "retail", "rev": "retail", "products": [
            P("infinite", "Visa Infinite", "The top card, in Classe ELITE, with Visa's concierge and lounge access; launched in November 2014 as the first Visa Infinite in Tunisia, in personal and business versions.",
              s=["aff"], lc="everyday", ay="Nov 2014", o="P", at="Visa", neo=[0, "Visa."], src=[["BIAT: Visa Infinite", INF], ["L'Economiste Maghrébin, Nov 2014", VINF14], ["BIAT: Classe ELITE", ELITE]]),
            P("platinum", "Mastercard Platinum", "'The must by BIAT': the card in Classe Platinum, with Mastercard partner offers and priceless.com, travel insurance, purchase protection and SecureCode online.", short="Platinum (Mastercard)",
              s=["aff"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's place in BIAT's affluent range, one step below Visa Infinite.",
              src=[["BIAT: Mastercard Platinum", PLAT], ["BIAT: Classe Platinum", CPLAT]]),
            P("premier", "Visa Premier", "A higher-limit card for privileged customers, domestic or international, with Mawdy travel insurance.",
              s=["aff"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["BIAT: Visa Premier", PREMIER]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Credit & split payment", "blurb": "TEMPO and Flexy.", "div": "retail", "rev": "retail", "products": [
            P("tempo", "TEMPO revolving credit card", "A Visa credit card on a revolving line repaid at 5% a month; its limit was raised in 2025 and it now sits in the Platinum pack.",
              s=["con", "aff"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["BIAT: Classe Platinum", CPLAT], ["Annual report 2025", RA25]]),
            P("flexy", "BIAT Flexy & Flexy+", "A split-payment card (October 2025): purchases at terminals and online repaid in six monthly instalments, with a reserve of TND 500–2,000 (Flexy+ up to TND 20,000), built as an alternative to post-dated cheques after the cheque law.",
              s=["con", "pro"], lc="borrow", st="new", ay="Oct 2025", o="B", neo=[None, "Network not stated ⚠."],
              mc="An instalment product looking for a network partner.",
              src=[["BIAT: Flexy", FLEXYPAGE], ["WMC: Flexy launch, Oct 2025", FLEXY]]),
        ]},
        {"id": "2.4", "ic": "plane", "name": "Travel & prepaid", "blurb": "Allowance card on Mastercard.", "div": "retail", "rev": "retail", "products": [
            P("travel", "BIATRAVEL allowance card", "An international Mastercard that carries the customer's annual tourist allowance (up to TND 6,000), loaded in branch on sight of a passport; upgraded in 2018 with medical cover up to US$50,000, Priceless and Mastercard Buy 1 Get 1.", short="Travel (Mastercard)",
              s=["con", "aff"], lc="move", ay="Jan 2018", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Under exchange controls this is how most BIAT customers pay abroad.",
              src=[["BIAT: Travel card", TRAVEL], ["African Manager: BIATRAVEL, Jan 2018", TRAVEL18]]),
            P("prepaid", "CASH, FLY & H'DYA prepaid", "Reloadable Visa prepaid cards: CASH (also for paying unbanked staff), CASH Anonyme without an account, FLY for young people and H'DYA as a gift card; reloaded in branch, at ATMs or in MyBIAT.",
              s=["young", "con", "pro"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["BIAT: CASH", CASH], ["BIAT: FLY", FLY], ["BIAT: H'DYA", HEDYA]]),
            P("fxprepaid", "Tounessna & Univers foreign-currency prepaid", "International prepaid cards on foreign-currency or convertible-dinar accounts, for the diaspora (Tounessna) and foreigners (Univers); the first in Tunisia (September 2016).",
              s=["tre"], lc="move", ay="Sep 2016", o="B", neo=[None, "Network not stated ⚠."], src=[["L'Economiste Maghrébin, Sep 2016", PREPAID16]]),
            P("techno", "Carte Technologique", "An internet-only international prepaid card for paying foreign websites in currency: TND 10,000 a year, or TND 100,000 for labelled start-ups.",
              s=["pro"], lc="move", o="B", neo=[None, "Network not stated ⚠."], src=[["BIAT: Carte Technologique", TECHNO]]),
        ]},
        {"id": "2.5", "ic": "briefcase-business", "name": "Commercial cards", "blurb": "Mastercard Business range.", "div": "cib", "rev": "corp", "products": [
            P("business", "Business, Business Gold & Business Premium", "Mastercard Business cards for staff, managers and executives (June 2016), domestic or international, with SMS alerts on foreign and online use and fraud cover; a Business card comes in the Start-up pack.", short="Business (Mastercard)",
              s=["pro", "corp"], lc="everyday", ay="Jun 2016", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's strongest single programme at BIAT.",
              src=[["African Manager: Business cards, Jun 2016", BUS16], ["BIAT: Carte Business", BUSINESS], ["BIAT: Pack Start-up", STARTUP]]),
            P("affaires", "Cartes Affaires", "Older domestic and international expense cards for named staff, alongside Visa Infinite Affaires for top executives.",
              s=["corp"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Mixed ⚠."], src=[["BIAT: Cartes Affaires", AFFAIRES]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acceptance", "blurb": "Terminals and e-commerce.", "div": "retail", "rev": "retail", "products": [
            P("tpe", "Payment terminals (TPE)", "Terminals for merchants accepting Visa, Mastercard and domestic cards, with daily telecollection and e-mailed statements; Tunisia had 45,600 terminals at end-June 2026 (+5.7%).",
              s=["pro"], lc="move", o="P", at="SMT ⚠", neo=[1, "Accepts every network."],
              src=[["BIAT: TPE", TPE], ["Business News: BCT H1 2026", BCTH1]]),
            P("ecom", "BIAT E-Commerce", "Online acquiring for merchant websites, taking national and foreign cards (Visa, Mastercard); Tunisian e-payments rose 22.1% to 10.3 million in H1 2026.",
              s=["pro", "corp"], lc="move", o="P", at="SMT ⚠", neo=[1, "Accepts every network."],
              mc="Click to Pay and authentication have a growing e-commerce market to serve.",
              src=[["BIAT: E-Commerce", ECOM], ["Business News: BCT H1 2026", BCTH1]]),
        ]},
        {"id": "2.7", "ic": "send", "name": "Transfers & remittances", "blurb": "Clearing and BIAT France.", "div": "france", "rev": "retail", "products": [
            P("transfers", "Transfers & clearing", "Domestic transfers, direct debits and bills of exchange through the BCT's clearing and Elyssa-RTGS, scheduled transfers in MyBIAT, and about 1,500 correspondent banks. No instant-payment product was found ⚠.",
              s=["con", "pro", "corp"], lc="move", neo=[0, ""], src=[["Annual report 2025", RA25], ["Business News: BCT H1 2026", BCTH1]]),
            P("biatfrance", "BIAT France remittances", "A Paris payment agent (since 2015) for transfers from Europe into BIAT accounts; agent of IYU Europe since December 2024, with a European passport and a mobile transfer app from late 2025; 3,510 direct transfers in 2025.",
              s=["tre"], lc="move", st="flux", o="P", at="IYU Europe", neo=[0, "IYU Europe."],
              mc="Card- and account-funded transfers from Europe are where Mastercard Move could fit.",
              src=[["Annual report 2025", RA25], ["BIAT: subsidiaries", FIL]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: card security and Visa's fraud monitoring, an internal rating system, BIAT Privilèges offers at 1,300 shops, Visa card campaigns, data and AI plans, and Assurances BIAT.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & risk", "blurb": "Alerts, blocking, Visa monitoring.", "div": "biat", "rev": "retail", "products": [
            P("fraud", "Card security & fraud monitoring", "SMS alerts on foreign and online card use, secure codes online, instant blocking in MyBIAT and anti-phishing warnings (August 2025); the 2022 Visa partnership brought fraud monitoring, transaction security and analytics.",
              s=["con", "pro"], lc="everyday", o="P", at="Visa", neo=[0, "BIAT's own and Visa's."],
              mc="Visa holds the fraud work; Mastercard's scoring tools are not in.",
              src=[["BIAT: security advice, Aug 2025", PHISH], ["Managers: Visa partnership, Sep 2022", VISA22]]),
            P("risk", "Internal rating & overdraft limits", "An internal rating system with ten performing grades, and a global overdraft-limit tool that now covers split-payment cards.",
              s=["con", "corp"], lc="borrow", o="B", neo=[0, ""], src=[["Annual report 2025", RA25]]),
        ]},
        {"id": "3.2", "ic": "gift", "name": "Loyalty & offers", "blurb": "BIAT Privilèges.", "div": "retail", "rev": "retail", "products": [
            P("privileges", "BIAT Privilèges", "A non-banking app (14 August 2026), built with FreeOui, giving customers discounts at more than 450 brands and 1,300 shops across Tunisia, by theme and location; part of the diaspora offer too.",
              s=["con", "aff", "tre"], lc="beyond", st="new", ay="Aug 2026", o="P", at="FreeOui", neo=[0, "FreeOui."],
              mc="A merchant marketplace without card-linked offers.",
              src=[["BIAT: BIAT Privilèges, Aug 2026", PRIV]]),
            P("campaigns", "Card usage campaigns", "Visa cashback on international purchases and 'Smart Delay' lounge access (2024), the BIAT–Visa CAN 2025 contest and a Visa 'Win the world' 2026 contest ⚠.",
              s=["con", "aff"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              src=[["Annual report 2025", RA25], ["Annual report 2024 (English)", RA24], ["BIAT: retail site", RETAIL]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "Data & AI", "blurb": "Planned for 2026.", "div": "tech", "rev": "group", "products": [
            P("aidata", "Data & AI", "AI and data analysis named as levers to personalise offers and anticipate needs; no live AI product was found ⚠.",
              s=["con", "corp"], lc="everyday", st="new", neo=[None, "Nothing public."], src=[["Annual report 2025", RA25]]),
        ]},
        {"id": "3.4", "ic": "badge-check", "name": "Insurance", "blurb": "TND 188m bancassurance.", "div": "assur", "rev": "retail", "products": [
            P("assur", "Assurances BIAT & card cover", "A group insurer since 2002: 2025 turnover TND 318 million, TND 188 million of it through the bank; travel cover (Mawdy) on premium and business cards, and loss and theft cover on all cards.",
              s=["con", "pro"], lc="grow", neo=[0, ""], src=[["BIAT: subsidiaries", FIL], ["Annual report 2025", RA25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: accounts and packs for 950,000 customers and the diaspora, consumer, home and green loans, corporate and trade banking (62% of commitments), syndicated project finance, and FX, brokerage and private equity.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Accounts & packs", "blurb": "950,000 customers.", "div": "retail", "rev": "retail", "products": [
            P("packs", "Accounts & packs", "Current and savings accounts and packs from Pack FIRST and University to Classe Platinum and Classe ELITE, for about 950,000 customers.",
              s=["con", "young", "aff"], lc="open", neo=[1, "Mastercard in entry packs; Visa in savings and ELITE."],
              src=[["Annual report 2025", RA25], ["BIAT: Pack FIRST", FIRST], ["BIAT: Classe ELITE", ELITE]]),
            P("tounessna", "Pack Tounessna (diaspora)", "The offer for Tunisians resident abroad, split into standard and Premium variants in 2025, with foreign-currency and convertible-dinar accounts, Tunizen car assistance and BIAT Privilèges.",
              s=["tre"], lc="open", neo=[0, ""], src=[["Annual report 2025", RA25], ["Shareholder letter 76, Sep 2026", L76]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Consumer, home & green loans", "blurb": "42,500 personal loans.", "div": "retail", "rev": "retail", "products": [
            P("loans", "Consumer & home loans", "Crediauto, Credifoyer, Avan'Salaire, BIATIMMO, Crédit Awal Sakan and Fleximmo: about 42,500 personal loans in 2025.",
              s=["con", "young"], lc="borrow", neo=[0, ""], src=[["Managers: AGM, Apr 2026", AGM]]),
            P("overt", "BIAT O'VERT", "Green loans (1 April 2026): O'VERT Rénov for energy and water savings at home, O'VERT Auto for cleaner vehicles, and an SME version.",
              s=["con", "pro"], lc="borrow", st="new", ay="Apr 2026", o="B", neo=[0, ""], src=[["BIAT: BIAT O'VERT, Apr 2026", OVERT]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate & trade", "blurb": "62% of commitments.", "div": "cib", "rev": "corp", "products": [
            P("corporate", "Corporate & trade banking", "Working capital, documentary credits, guarantees, cash pooling and Dutycash; an AfDB US$50 million transaction guarantee (6 February 2026) backs clients' imports.",
              s=["corp", "pro"], lc="borrow", st="new", o="P", at="AfDB", neo=[0, ""], src=[["BIAT: AfDB guarantee, Feb 2026", BAD], ["Annual report 2025", RA25]]),
            P("community", "Community-company financing", "A platform for financing 'sociétés communautaires' under a partnership with the employment ministry (TND 4 million of a TND 40 million state envelope).",
              s=["pro"], lc="borrow", st="new", o="P", neo=[0, ""], src=[["Annual report 2025", RA25]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "Project & syndicated finance", "blurb": "Solar, microfinance.", "div": "cib", "rev": "bfi", "products": [
            P("bfi", "Financing & investment banking", "Agent and arranger of TND 140 million for the 100 MWac GFR solar plant in Kairouan; arranger of TND 90 million for Advans Tunisie (July 2026); part of TND 160 million for Enda Tamweel.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Annual report 2025", RA25], ["Shareholder letter 76, Sep 2026", L76]]),
        ]},
        {"id": "4.5", "ic": "chart-candlestick", "name": "Markets, wealth & capital", "blurb": "Top FX bank, top broker.", "div": "tv", "rev": "bfi", "products": [
            P("fx", "FX & markets", "Global Finance's best FX bank in Tunisia for the sixth year (2026).",
              s=["corp"], lc="move", neo=[0, ""], src=[["Shareholder letter 76, Sep 2026", L76]]),
            P("tunisievaleurs", "Tunisie Valeurs & asset management", "First Tunisian broker in 2025 (29.3% share, TND 3,156 million traded), with BIAT Asset Management funds.",
              s=["aff"], lc="grow", o="A", neo=[0, ""], src=[["BIAT: subsidiaries", FIL]]),
            P("capitalrisque", "BIAT Capital Risque", "Private equity with TND 905 million of group funds (2025), including stakes in solar plants.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["BIAT: subsidiaries", FIL]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach BIAT: MyBIAT for 415,000 people, MyBIAT Corporate for 19,000 companies, 206 branches and a call centre, and BIAT France for the diaspora.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "MyBIAT", "blurb": "415,000 users.", "div": "retail", "rev": "retail", "products": [
            P("mybiat", "MyBIAT", "The app and web bank for individuals and professionals (March 2022): more than 415,000 users, over half of those eligible, at end-2025; card limits, blocking and scheduled transfers; 'Produit de l'Année 2026'.",
              s=["con", "young", "pro"], lc="everyday", neo=[0, ""], src=[["Annual report 2025", RA25], ["BIAT: MyBIAT award, Feb 2026", MYAWARD], ["BIAT: MyBIAT", MYBIAT]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "MyBIAT Corporate", "blurb": "19,000 companies.", "div": "cib", "rev": "corp", "products": [
            P("mybiatcorp", "MyBIAT Corporate", "Online banking for companies (2024), used by about 19,000: trade and card-activity tracking, Tunichèque cheque reservations and securities; Multivir and BIATNET Business close in 2026.",
              s=["corp", "pro"], lc="everyday", st="new", neo=[0, ""], src=[["Annual report 2025", RA25]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & call centre", "blurb": "206 branches.", "div": "retail", "rev": "retail", "products": [
            P("branches", "Branches", "206 branches across Tunisia, more than 70 rebuilt in the new format by end-2025, and a representative office in Tripoli, Libya.",
              s=["con", "pro"], lc="open", st="flux", neo=[0, ""], src=[["Annual report 2025", RA25]]),
            P("crc", "Customer relations centre", "About 420,000 calls and 250,000 requests handled in 2025; 'Élu Service Client de l'Année 2026'.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Annual report 2025", RA25]]),
        ]},
        {"id": "5.4", "ic": "earth", "name": "Diaspora channels", "blurb": "Paris and events.", "div": "france", "rev": "retail", "products": [
            P("trechannels", "BIAT France & diaspora desks", "A Paris agency, dedicated Tounessna advisers in Tunis and events in Paris, Lyon and Dubai; a second French agency was considered for 2026 ⚠.",
              s=["tre"], lc="open", neo=[0, ""], src=[["Annual report 2025", RA25], ["BIAT: subsidiaries", FIL]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BIAT", "blurb": "Travel and business cards; Visa first.", "products": [
        P("mcatbiat", "Mastercard at BIAT", "Visa has backed BIAT's cards for more than 30 years, signed a six-year partnership in September 2022 and carries Infinite, Premier, TEMPO credit and all prepaid cards. Mastercard carries the travel-allowance card, the Business range (2016), Platinum and the entry-pack debit, and is one of two choices for classic debit. No BIAT–Mastercard agreement or digital programme is public ⚠.",
          s=["con"], div="biat", rev="group", mc="The relationship this map is drawn for.",
          src=[["Managers: Visa partnership, Sep 2022", VISA22], ["BIAT: Travel card", TRAVEL], ["African Manager: Business cards, Jun 2016", BUS16]]),
    ]},
    {"id": "pillar-market", "name": "Tunisian payments", "blurb": "SMT, TUNPAY, cheque reform.", "products": [
        P("market", "The Tunisian market", "SMT switches domestic cards and plans a tokenised national scheme for cards and wallets at the end of 2026 ⚠; the BCT and SMT launched the TUNPAY mobile-payment label in May 2026. At end-June 2026 Tunisia had 6.15 million cards, 512,000 wallets and 45,600 terminals; cheques fell 10.7% in H1 2026 after the 2025 reform.",
          s=["con"], div="biat", rev="group",
          src=[["La Presse: SMT, Dec 2025", SMT25], ["Business News: TUNPAY, May 2026", TUNPAY], ["Business News: BCT H1 2026", BCTH1]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
