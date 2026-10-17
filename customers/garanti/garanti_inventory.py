"""Garanti BBVA's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own (BRSA consolidated) unless a source says otherwise: the 1H 2026 results and
presentation (30 July 2026), the 2025 results presentation and the investor-relations pages. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

IR = "https://www.garantibbvainvestorrelations.com/en/"
H1P = "https://www.garantibbvainvestorrelations.com/en/images/pdf/2Q26_BRSA_Consolidated_Earnings_Presentation.pdf"
FYP = "https://www.garantibbvainvestorrelations.com/en/images/pdf/4Q25_BRSA_Consolidated_Earnings_Presentation.pdf"
H1R = "https://www.bbva.com/en/economy-and-finance/garanti-bbva-continues-to-deliver-consistent-performance-thanks-to-its-strong-capital-structure-and-customer-centric-strategy/"
Q1R = "https://www.garantibbvainvestorrelations.com/en/news/detail/Garanti-BBVA-announces-1Q26-financial-results/113/10624/0"
H125 = "https://www.bbva.com/en/tr/economy-and-finance/garanti-bbva-reports-solid-first-half-results-driven-by-customer-centric-growth-digitization-and-sustainability/"
NUM = "https://www.garantibbvainvestorrelations.com/en/about-garanti/detail/Garanti-BBVA-in-Numbers/8/17/0"
PROF = "https://www.garantibbvainvestorrelations.com/en/about-garanti/detail/Corporate-Profile/3/13/0"
HIST = "https://www.garantibbvainvestorrelations.com/en/about-garanti/detail/History/4/14/0"
SHR = "https://www.garantibbvainvestorrelations.com/en/about-garanti/detail/Shareholding-Structure/7/16/0"
STRAT = "https://www.garantibbvainvestorrelations.com/en/about-garanti/detail/Our-Strategic-Priorities/2152/9540/0"
BOARD = "https://www.garantibbvainvestorrelations.com/en/corporate-governance/Board-of-Directors/Board-of-Directors/77/8078/0"
MGMT = "https://www.garantibbvainvestorrelations.com/en/environment-social-governance/Senior-Management/Senior-Management/79/392/0"
RAT = "https://www.garantibbvainvestorrelations.com/en/about-garanti/detail/Ratings/17/26/0"
ROM = "https://www.bbva.com/en/economy-and-finance/garanti-bbva-reaches-agreement-to-sell-its-romanian-unit/"
CARDS = "https://www.garantibbva.com.tr/kartlar"
BONUS = "https://www.garantibbva.com.tr/kartlar/bonus-card"
BTROY = "https://www.garantibbva.com.tr/kartlar/bonus-troy"
MS = "https://www.garantibbva.com.tr/kartlar/miles-and-smiles"
SF = "https://www.garantibbva.com.tr/kartlar/shop-and-fly"
DEB = "https://www.garantibbva.com.tr/kartlar/banka-kartlari"
AMEX = "https://www.garantibbva.com.tr/kartlar/american-express"
BIO = "https://www.garantibbva.com.tr/kartlar/bonus-platinum-biyometrik"
B25 = "https://www.dha.com.tr/kurumsal/garanti-bbva-ve-mastercard-bonusun-25inci-yilini-kutluyor-2694828"
MP = "https://www.hurriyet.com.tr/advertorial/masterpass-ve-garanti-bbvadan-kayitli-kartlarin-izini-surecek-yenilik-42461901"
TOK = "https://webrazzi.com/2021/07/12/garanti-bbva-ve-mastercard-is-birligi-ile-hangi-kartim-yurt-disinda-nerede-kayitli-derdine-son/"
BIOB = "https://bbva.com/en/innovation/garanti-bbva-goes-biometric-with-its-new-bonus-platinum-card"
EXP = "https://www.dha.com.tr/kurumsal/garanti-bbva-ve-mastercard-is-birligiyle-e-ihracat-paketi-hayata-geciyor-2643364"
COL = "https://www.cnbce.com/haberler/mastercard-ve-garanti-bbvadan-yapay-zeka-destekli-tahsilatta-yeni-donem-h21377"
AGT = "https://www.cnbce.com/fintech/garanti-bbva-mastercard-teknolojisiyle-turkiyede-bankacilik-sektorunde-ilk-uctan-uca-yapay-zeka-asistanli-e-ticaret-islemini-gerceklestirdi-v21912"
VWC = "https://www.cnbce.com/spor-ekonomisi/2026-fifa-dunya-kupasi-resmi-odeme-teknolojileri-partneri-visa-ile-garanti-bbva-is-birligine-imza-atti-h19239"
AX20 = "https://www.haberturk.com/ekonomi/garanti-bbva-ve-american-express-turkiye-deki-20-yillik-is-birliklerini-kart-sahiplerine-ozel-kampanya-ve-deneyimlerle-kutluyor-3896587"
TAMI = "https://www.haberturk.com/garanti-bbvanin-yeni-odeme-ve-elektronik-para-kurulusu-tami-faaliyete-basladi-3739528-ekonomi"
SMART = "https://www.capital.com.tr/sirket-panosu/sirket-panosu-haberleri/garanti-bbvadan-temassiz-odemeye-yenilikci-cozum"
QR = "https://www.garantibbva.com.tr/kurumsal-iletisim/baska-banka-kartlarindan-qr-ile-odeme"
RTP = "https://www.haberturk.com/garanti-bbvadan-odeme-iste-api-ile-tahsilatta-yeni-donem-3886308-ekonomi"
KRP = "https://www.garantibbva.com.tr/kurumsal-iletisim/garanti-bbva-kripto-portfoyu-mobilde"
TROY = "https://www.benguturk.com/ekonomi/troyun-tutarsal-pazar-payi-yuzde-25i-asti-256988h"
FAST = "https://www.teknoblog.com/fast-islem-limiti-26-agustosta-300-bin-tlye-cikiyor/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · BBVA · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: TL 5.2 trillion of assets and a 28% return on equity, BBVA's 86% stake, a bank founded in 1946, an OpenAI-powered assistant and the sale of the Romanian unit.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "TL 64 billion in the half.", "div": "gbbva", "rev": "central", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of TL 5.2 trillion, cash and non-cash loans of TL 3.9 trillion and customer deposits of TL 3.5 trillion at 30 June 2026; net income of TL 64.4 billion in the half (+20%, ROAE 28.1%) and TL 111.3 billion in 2025 (ROAE 29%).",
              s=["con"], neo=[0, ""], src=[["1H26 earnings presentation", H1P], ["2025 earnings presentation", FYP], ["BBVA: 1H26 results, Jul 2026", H1R]]),
            P("capital", "Capital & ratings", "Consolidated capital adequacy 15.9% and CET1 about 12% after BRSA forbearance ended in January 2026; Fitch BB-/Stable (April 2026) and Moody's Ba2/Stable deposits (July 2026).",
              s=["corp"], neo=[0, ""], src=[["1H26 earnings presentation", H1P], ["Garanti BBVA: ratings", RAT]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "BBVA 86%, CEO Mahmut Akten.", "div": "gbbva", "rev": "central", "products": [
            P("owner", "BBVA ownership & listing", "Founded in Ankara in 1946, owned by Doğuş from 1983 with GE and then BBVA as partners; BBVA has held 85.97% since a May 2022 tender. Listed on Borsa Istanbul (GARAN), market value TL 581 billion (about US$12.5 billion) at end-June 2026.",
              s=["corp"], o="I", neo=[0, ""], src=[["Garanti BBVA: shareholding", SHR], ["Garanti BBVA: history", HIST]]),
            P("leadership", "Board & management", "Chairman Süleyman Sözen, vice chairman Jorge Sáenz-Azcúnaga (BBVA), CEO Mahmut Akten; Ceren Acer Kezik runs retail banking and fronts cards, and Kerem Orbay runs Garanti BBVA Payment Systems.",
              s=["corp"], neo=[0, ""], src=[["Garanti BBVA: board", BOARD], ["Garanti BBVA: senior management", MGMT]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology & AI", "blurb": "20 million actions a day.", "div": "gbbva", "rev": "central", "products": [
            P("tech", "Data, AI & engineering", "About 20 million daily customer actions turned into AI-driven decisions, needs of nearly 10 million customers flagged each day, and an in-house engineering and data division; the UGİ assistant's generic content now runs on an OpenAI-powered LLM.",
              s=["con"], neo=[0, ""], src=[["1Q26 results", Q1R], ["1H26 earnings presentation", H1P]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & deals", "blurb": "Radical client focus; Romania sold.", "div": "gbbva", "rev": "central", "products": [
            P("strategy", "Strategic priorities", "BBVA's 2025–2029 plan applied in Turkey: a radical client perspective, sustainability as a growth engine, scale in every enterprise segment, value and capital creation, and data and AI. 2026 guidance: TL loan growth of 30–35% and fee growth of about 30–35%.",
              s=["corp"], neo=[0, ""], src=[["Garanti BBVA: strategic priorities", STRAT], ["1H26 earnings presentation", H1P]]),
            P("romania", "Sale of Garanti BBVA Romania", "Garanti Bank S.A. and Motoractive IFN sold to Raiffeisen Bank Romania for €591 million (agreed 28 March 2026, closing expected in Q4 2026); about €4 billion of assets, under 5% of the group.",
              s=["corp"], div="romania", st="flux", ay="Mar 2026", o="A", neo=[0, ""], src=[["BBVA: Romanian sale, Mar 2026", ROM]]),
            P("sustain", "Sustainable finance", "A TL 3.5 trillion sustainable-finance target for 2025–2029, TL 1.6 trillion reached by June 2026; Equator Principles signatory and COP31 banking partner with BBVA.",
              s=["corp", "sme"], lc="borrow", neo=[0, ""], src=[["Garanti BBVA: corporate profile", PROF], ["Garanti BBVA IR", IR]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Bonus credit cards mostly on Mastercard with Troy versions, travel and team co-brands split across Mastercard, Visa and Amex, Garanti's own American Express range, Visa and Troy debit, Turkey's top private acquirer, FAST instant payments, and the BonusFlaş wallet.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Bonus credit cards", "blurb": "Mastercard-led, Troy alongside.", "div": "gosas", "rev": "pay", "products": [
            P("bonus", "Bonus, Gold, Platinum & Flexi", "Turkey's first multi-brand chip credit card (2000), earning 1 bonus = 1 TL with instalments at partner merchants. The core range and virtual card carry Mastercard; a Trink version carries Visa ⚠. Part of 20.6 million Garanti credit cards and #1 issuing volume among private banks (17.4%, June 2026).", short="Bonus (Mastercard)",
              s=["con", "aff"], lc="everyday", ay="2000", o="B", at="Mastercard", neo=[1, "Mastercard core range; Visa and Troy versions."],
              mc="Mastercard's flagship in Turkey's largest private card book.",
              src=[["Garanti BBVA: Bonus", BONUS], ["Garanti BBVA: cards", CARDS], ["1H26 earnings presentation", H1P]]),
            P("bonustroy", "Bonus Troy cards", "Troy versions of Bonus Classic, Gold, Platinum and Flexi, for domestic use only, on the BKM scheme founded in 2015.",
              s=["con"], lc="everyday", o="P", at="Troy (BKM)", neo=[0, "Troy."], src=[["Garanti BBVA: Bonus Troy", BTROY]]),
            P("biometric", "Bonus Platinum Biometric", "Pay by fingerprint on a sensor in the card, any amount, announced in February 2024 with Mastercard's Turkey general manager ⚠ network inferred.",
              s=["con", "aff"], lc="everyday", ay="Feb 2024", o="P", at="Mastercard", neo=[2, "Mastercard ⚠."], src=[["Garanti BBVA: Bonus Platinum Biometric", BIO], ["BBVA: biometric card, Feb 2024", BIOB]]),
        ]},
        {"id": "2.2", "ic": "plane", "name": "Travel & team cards", "blurb": "Miles&Smiles, Shop&Fly, clubs.", "div": "gosas", "rev": "pay", "products": [
            P("miles", "Miles&Smiles Garanti BBVA", "Turkish Airlines' official credit card since 2000: Platinum on Mastercard, earning extra miles at Mastercard programme-partner merchants; Gold, Platinum and Privé on American Express. Mile earning up to 5.5 times higher by assets held from August 2025.", short="Miles&Smiles (Mastercard, Amex)",
              s=["aff"], lc="everyday", ay="2000", o="P", at="Turkish Airlines", neo=[1, "Mastercard and Amex versions."], src=[["Garanti BBVA: Miles&Smiles", MS]]),
            P("shopfly", "Shop&Fly", "Airline-agnostic miles card: Platinum and Diamond on Visa, Gold and Platinum on American Express; Visa's FIFA World Cup 2026 offers went to Shop&Fly Diamond Visa holders (November 2025).",
              s=["aff"], lc="everyday", o="B", at="Visa, Amex", neo=[0, "Visa and Amex."],
              mc="Visa holds the bank's top travel card and its World Cup tie-in.",
              src=[["Garanti BBVA: Shop&Fly", SF], ["CNBC-e: Visa World Cup deal, Nov 2025", VWC]]),
            P("teams", "Club co-brands", "BJK Bonus and Trabzonspor Bonus on Mastercard; Fenerbahçe Bonus on Visa.",
              s=["con"], lc="everyday", o="P", at="BJK, Trabzonspor, Fenerbahçe", neo=[1, "Two Mastercard, one Visa."], src=[["Garanti BBVA: cards", CARDS]]),
        ]},
        {"id": "2.3", "ic": "gem", "name": "American Express", "blurb": "Amex's licensee for 20 years.", "div": "gosas", "rev": "pay", "products": [
            P("amex", "Garanti BBVA American Express", "Garanti BBVA is American Express's licensed institution in Turkey (20 years in July 2026): the Card, Gold, Platinum and Metal Platinum, Bonus American Express, Selects dining discounts and Membership Rewards.",
              s=["aff"], lc="everyday", o="P", at="American Express", neo=[0, "Amex."], src=[["Garanti BBVA: American Express", AMEX], ["Habertürk: 20 years of Amex, Jul 2026", AX20]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Debit cards", "blurb": "Paracard on Visa and Troy.", "div": "gosas", "rev": "retail", "products": [
            P("paracard", "Paracard Bonus debit", "Paracard Bonus, Platinum, Genç, Cool (ages 12–17) and Business debit cards earning bonus, among 24.2 million Garanti debit cards; the Paracard range carries Visa.", short="Paracard (Visa)",
              s=["con", "sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Garanti BBVA: debit cards", DEB], ["Garanti BBVA in numbers", NUM]]),
            P("paratroy", "Paracard Bonus Troy", "A Troy debit card earning bonus on domestic spending.",
              s=["con"], lc="everyday", o="P", at="Troy (BKM)", neo=[0, "Troy."], src=[["Garanti BBVA: debit cards", DEB]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acquiring", "blurb": "932,000 POS, #1 private.", "div": "gosas", "rev": "pay", "products": [
            P("acquiring", "Merchant acquiring", "932,287 POS terminals (June 2026) and #1 acquiring volume among private banks (15.4%); payment-systems fees are about two-thirds of the bank's TL 90.7 billion of fees, up 36%.",
              s=["mer", "sme"], lc="move", o="B", neo=[1, "Accepts every network."],
              mc="The largest private acquiring book in Turkey.",
              src=[["Garanti BBVA in numbers", NUM], ["1H26 earnings presentation", H1P]]),
            P("tami", "TAMİ", "Garanti's payment and e-money institution, live since November 2024: one multi-bank POS for small merchants, a prepaid card (TL 2,750 limit when anonymous), payment links and e-money wallets.",
              s=["mer", "con"], div="tami", lc="move", ay="Nov 2024", o="B", neo=[None, "Prepaid-card network not stated."], src=[["Habertürk: TAMİ starts, Nov 2024", TAMI]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Instant payments", "blurb": "FAST and request to pay.", "div": "gbbva", "rev": "retail", "products": [
            P("fast", "FAST transfers", "24/7 transfers on the central bank's FAST system (live since January 2021; 5.4 billion transactions and TL 43.2 trillion in 2025), with limits raised to TL 300,000 from 26 August 2026.",
              s=["con", "sme"], lc="move", o="P", at="CBRT", neo=[0, "Central-bank rail."], src=[["Teknoblog: FAST limits, Aug 2026", FAST], ["Garanti BBVA: cards and services", CARDS]]),
            P("odemeiste", "Ödeme İste (request to pay)", "Request-to-pay on FAST, built with BKM, in the app and as an API for billers; first live with Uludağ Elektrik in May 2026.",
              s=["corp", "con"], lc="move", st="new", ay="May 2026", o="P", at="BKM", neo=[0, "FAST."],
              mc="Account-to-account bill collection that bypasses cards.",
              src=[["Habertürk: Ödeme İste API, May 2026", RTP]]),
        ]},
        {"id": "2.7", "ic": "smartphone", "name": "BonusFlaş & wallets", "blurb": "QR, NFC and smart card choice.", "div": "gosas", "rev": "pay", "products": [
            P("bonusflas", "BonusFlaş", "The card app and wallet on more than 5.5 million phones (September 2024): card control, campaigns, QR payments, and GarantiPay.",
              s=["con"], lc="everyday", o="B", neo=[1, "Holds every network's cards."], src=[["Garanti BBVA: QR payments, Sep 2024", QR]]),
            P("smart", "S.M.A.R.T. card selection", "Picks the most rewarding card at checkout for NFC, QR and GarantiPay payments in Garanti BBVA Mobile and BonusFlaş; launched in September 2025 with Miles&Smiles and American Express cards.",
              s=["aff"], lc="everyday", st="new", ay="Sep 2025", o="B", neo=[1, "Chooses among networks."], src=[["Capital: S.M.A.R.T., Sep 2025", SMART]]),
            P("qr", "QR with other banks' cards", "Customers can store other banks' debit cards in BonusFlaş once and pay by QR (September 2024).",
              s=["con"], lc="everyday", ay="Sep 2024", o="B", neo=[None, "Network not stated."], src=[["Garanti BBVA: QR payments, Sep 2024", QR]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card and account: Mastercard tokens and Masterpass controls, the UGİ assistant and an agentic-commerce pilot on Mastercard's Agent Pay principles, AI collections built with Mastercard, the eight-bank Bonus programme, and open banking.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Card security & tokens", "blurb": "Mastercard firsts in Turkey.", "div": "gosas", "rev": "pay", "products": [
            P("token", "Card-on-file control (tokenisation)", "Mastercard's tokenisation (masking) technology, first in Turkey with Garanti in July 2021: BonusFlaş shows which foreign subscription sites hold a Mastercard and lets customers switch them off.",
              s=["con"], lc="everyday", ay="Jul 2021", o="P", at="Mastercard", neo=[3, "Mastercard tokenisation."], src=[["Webrazzi: Mastercard tokenisation, Jul 2021", TOK]]),
            P("masterpass", "Masterpass merchant view", "Customers see in BonusFlaş and Garanti BBVA Mobile which merchants hold a card saved in Masterpass (May 2024), billed as a first in Turkey; Masterpass covers more than 4,000 merchants ⚠ advertorial.",
              s=["con"], lc="everyday", ay="May 2024", o="P", at="Mastercard", neo=[3, "Masterpass."], src=[["Hürriyet: Masterpass and Garanti BBVA, May 2024", MP]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI assistant & agents", "blurb": "UGİ; Agent Pay pilot.", "div": "gbbva", "rev": "retail", "products": [
            P("ugi", "UGİ assistant", "A generative-AI assistant reaching 9.1 million customers with more than 76 million chats, covering about 200 topics on an OpenAI-powered LLM.",
              s=["con"], lc="everyday", o="P", at="OpenAI", neo=[0, ""], src=[["1H26 earnings presentation", H1P]]),
            P("agentpay", "Agentic commerce pilot", "Turkey's first end-to-end AI-assistant e-commerce transaction in banking (December 2025), built on the principles of Mastercard Agent Pay with tokenised, verifiable agent payments; customer launch through Garanti BBVA Mobile and BonusFlaş still pending.",
              s=["con"], lc="everyday", st="new", ay="Dec 2025", o="P", at="Mastercard", neo=[3, "Mastercard Agent Pay principles."],
              mc="A demo waiting to reach 31 million customers.",
              src=[["CNBC-e: agentic transaction, Dec 2025", AGT]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "Collections & risk", "blurb": "AI collections with Mastercard.", "div": "gbbva", "rev": "retail", "products": [
            P("collections", "AI collections optimisation", "Next-best-action models and a stochastic optimisation engine built with Mastercard's consulting team: new NPL inflows down by up to 15% and contact efficiency up more than 30% (December 2025), as the NPL ratio rose to 3.5% by June 2026.",
              s=["con", "sme"], lc="borrow", st="new", ay="Dec 2025", o="P", at="Mastercard", neo=[3, "Mastercard consulting."], src=[["CNBC-e: AI collections, Dec 2025", COL], ["1H26 earnings presentation", H1P]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Bonus loyalty", "blurb": "18 million users, eight banks.", "div": "gosas", "rev": "pay", "products": [
            P("bonusprog", "Bonus programme", "A multi-brand loyalty platform shared with eight banks: about 18 million users, about one in three Turkish credit-card holders and more than 600,000 member merchants (August 2025).",
              s=["con", "mer"], lc="grow", ay="2000", o="B", neo=[1, "Bonus cards are mostly Mastercard."],
              mc="Card-linked offers could run across eight banks' cards.",
              src=[["DHA: Bonus at 25, Aug 2025", B25]]),
        ]},
        {"id": "3.5", "ic": "code-xml", "name": "Open banking & APIs", "blurb": "Other banks' accounts and POS.", "div": "gbbva", "rev": "sme", "products": [
            P("openbank", "Open banking", "Retail, tradesman, SME and commercial customers see their accounts and POS activity at other banks in Garanti BBVA Mobile and Internet.",
              s=["sme", "con"], lc="open", o="B", neo=[0, ""], src=[["Garanti BBVA: services", CARDS]]),
            P("apis", "APIs for companies", "Collection APIs such as Ödeme İste for billers, part of a 'service banking' push; a Garanti BBVA API Store is advertised ⚠ not reviewed.",
              s=["corp"], lc="move", st="new", o="B", neo=[None, ""], src=[["Habertürk: Ödeme İste API, May 2026", RTP]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: Turkey's largest private consumer and card lending book, deposits, pensions and crypto, SME and commercial banking with Mastercard commercial cards, and corporate, investment and international banking.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Retail lending", "blurb": "#1 private lender to consumers.", "div": "gbbva", "rev": "retail", "products": [
            P("retaillend", "Mortgages, auto & personal loans", "Among private banks: 28.7% of mortgages, 41.1% of auto loans and 21.6% of general-purpose loans (June 2026), all #1.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["1H26 earnings presentation", H1P]]),
            P("cardlend", "Credit-card lending", "24.0% of consumer credit-card balances among private banks and 14.0 million card customers; consumer cards are 30.5% of TL performing loans.",
              s=["con"], lc="borrow", neo=[1, "Mostly Mastercard, with Visa, Amex and Troy."], src=[["1H26 earnings presentation", H1P], ["Garanti BBVA in numbers", NUM]]),
        ]},
        {"id": "4.2", "ic": "coins", "name": "Deposits, wealth & crypto", "blurb": "TL 3.5 trillion of deposits.", "div": "subs", "rev": "central", "products": [
            P("deposits", "Deposits", "Customer deposits of TL 3.5 trillion (June 2026), 22.6% of TL deposits among private banks (#1).",
              s=["con", "inv"], lc="grow", div="gbbva", neo=[0, ""], src=[["BBVA: 1H26 results, Jul 2026", H1R], ["1H26 earnings presentation", H1P]]),
            P("wealth", "Pensions, insurance & investments", "Pensions and life insurance, brokerage and portfolio management through subsidiaries; brokerage and asset-management fees up 79% and insurance fees up 65% in 1H26.",
              s=["inv"], lc="grow", neo=[0, ""], src=[["Garanti BBVA: corporate profile", PROF], ["1H26 earnings presentation", H1P]]),
            P("kripto", "Garanti BBVA Kripto", "A bank-owned crypto platform; crypto portfolios shown in Garanti BBVA Mobile next to stocks and funds since August 2025.",
              s=["inv"], div="kripto", lc="grow", ay="Aug 2025", o="B", neo=[0, ""], src=[["Garanti BBVA: crypto in the app, Aug 2025", KRP]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "SME & commercial", "blurb": "26% of small-business loans.", "div": "gbbva", "rev": "sme", "products": [
            P("sme", "SME & commercial banking", "25.9% of micro and small-enterprise loans and 17.9% of TL business loans among private banks; 'My Banker' remote relationship managers for SME and commercial clients.",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["1H26 earnings presentation", H1P], ["BBVA: 1H25 results, Jul 2025", H125]]),
            P("commcard", "Commercial cards & e-export", "Business credit cards (8.2% of TL loans) and an e-export package with Mastercard and MegaMerchant (May 2025), offered only to holders of Mastercard-branded Garanti commercial cards.",
              s=["sme"], lc="move", st="new", ay="May 2025", o="P", at="Mastercard, MegaMerchant", neo=[1, "Some commercial cards are Mastercard."],
              mc="Mastercard-only e-export tools for Turkey's exporters.",
              src=[["DHA: e-export package, May 2025", EXP], ["1H26 earnings presentation", H1P]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Corporate & international", "blurb": "US$21bn of FX loans.", "div": "gbbva", "rev": "cib", "products": [
            P("cib", "Corporate & investment banking", "FX loans of US$20.9 billion, mostly to large corporates, exporters and project finance (64% of project-finance loans with FX revenue), plus global markets.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["1H26 earnings presentation", H1P]]),
            P("intl", "International", "Garanti BBVA International in the Netherlands and branches in Cyprus and Malta; the Romanian bank is being sold.",
              s=["corp"], div="gbi", lc="borrow", neo=[0, ""], src=[["Garanti BBVA: corporate profile", PROF], ["BBVA: Romanian sale, Mar 2026", ROM]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: Garanti BBVA Mobile for 18 million, 796 branches and 6,562 ATMs, remote bankers, and the partner banks and merchants of Bonus.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Garanti BBVA Mobile", "blurb": "1 in 5 Turkish mobile transactions.", "div": "gbbva", "rev": "retail", "products": [
            P("mobile", "Garanti BBVA Mobile", "18.3 million mobile customers and 16.7 million average daily log-ins; one in five mobile-banking transactions in Turkey; 86% of sales digital.",
              s=["con", "sme"], lc="open", neo=[0, ""], src=[["1H26 earnings presentation", H1P], ["2025 earnings presentation", FYP]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & remote", "blurb": "796 branches, 6,562 ATMs.", "div": "gbbva", "rev": "retail", "products": [
            P("branches", "Branches & ATMs", "796 branches (790 in Turkey) and 6,562 ATMs at June 2026.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Garanti BBVA in numbers", NUM]]),
            P("remote", "Remote banking & contact centre", "Remote personal bankers (Benim Bankacım), the 444 0 333 contact centre and WhatsApp banking.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["Garanti BBVA: services", CARDS], ["BBVA: 1H25 results, Jul 2025", H125]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partner banks & merchants", "blurb": "Eight Bonus banks, 600,000 shops.", "div": "gosas", "rev": "pay", "products": [
            P("partners", "Bonus partner banks & merchants", "Bonus is shared with eight banks and more than 600,000 member merchants; Turkish Airlines is the Miles&Smiles partner.",
              s=["mer", "con"], lc="open", o="P", neo=[1, "Partners' Bonus cards span networks."], src=[["DHA: Bonus at 25, Aug 2025", B25], ["Garanti BBVA: Miles&Smiles", MS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Garanti BBVA", "blurb": "Credit cards and 30 years of firsts.", "products": [
        P("mcatgaranti", "Mastercard at Garanti BBVA", "Mastercard carries most Bonus credit cards, Miles&Smiles Platinum and Mastercard commercial cards, in a partnership of more than 30 years with Turkish firsts in tokenisation (2021), Masterpass (2024), AI collections and agentic commerce (2025). Visa carries debit and Shop&Fly, American Express has a Garanti-issued range, and Troy versions sit beside the main cards.",
          s=["con"], div="gosas", rev="pay", mc="The relationship this map is drawn for.",
          src=[["DHA: Bonus at 25, Aug 2025", B25], ["Garanti BBVA: cards", CARDS]]),
    ]},
    {"id": "pillar-market", "name": "Turkish payments", "blurb": "Troy, FAST, high inflation.", "products": [
        P("market", "The Turkish market", "Troy took 25.3% of card spending in 2025 (90 million cards); FAST handled 5.4 billion transactions; inflation is forecast at 30% and the policy funding rate at about 36% at end-2026.",
          s=["con"], div="gbbva", rev="central", src=[["Bengü Türk: Troy share, Jan 2026", TROY], ["Teknoblog: FAST, Aug 2026", FAST], ["1H26 earnings presentation", H1P]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
