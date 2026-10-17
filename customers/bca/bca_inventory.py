"""Bank Central Asia's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are BCA's own unless a source says otherwise: the 1H26 results presentation (28 July 2026) and the
FY25 presentation (February 2026), plus BCA's product pages. ``neo`` is the Mastercard lens: [depth, note],
where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://www.bca.co.id/-/media/Feature/Report/File/Berita-Investor/2026/20260728-1h26-presentasi-perusahaan.pdf"
FY25 = "https://www.bca.co.id/-/media/Feature/Report/File/Berita-Investor/2026/20260210-FY25-Presentasi-Perusahaan-ID.pdf"
MGMT = "https://www.bca.co.id/en/tentang-bca/korporasi/manajemen-bca"
HIST = "https://www.bca.co.id/en/tentang-bca/korporasi/sejarah-bca"
SUBS = "https://www.bca.co.id/en/tentang-bca/korporasi/perusahaan-anak"
CARDS = "https://www.bca.co.id/en/individu/produk/kartu-kredit/pilihan-kartu"
MCW = "https://www.bca.co.id/en/individu/produk/kartu-kredit/mastercard-world"
KKI = "https://www.bca.co.id/en/individu/produk/kartu-kredit/kartu-kredit-indonesia"
CTLS = "https://www.bca.co.id/en/individu/produk/kartu-kredit/contactless"
TAHAPAN = "https://www.bca.co.id/en/Individu/produk/simpanan/Tahapan"
FLAZZ = "https://www.bca.co.id/en/individu/produk/uang-elektronik/flazz"
NFC = "https://www.bca.co.id/en/Individu/layanan/e-banking/mybca/NFC-Pay"
QRJP = "https://www.bca.co.id/en/informasi/news-and-features/2025/08/21/03/13/kini-qris-cross-border-bisa-digunakan-di-jepang"
QRXB = "https://www.bca.co.id/en/informasi/Edukatips/2023/05/11/10/48/ini-dia-negara-yang-bisa-transaksi-qris-lintas-negara-cross-border-lewat-bca-mobile"
PAYL = "https://www.bca.co.id/id/individu/layanan/e-banking/mybca/paylater-bca"
PAYLK = "https://keuangan.kontan.co.id/news/pengguna-paylater-bca-tumbuh-8-per-juni-2026-outstanding-capai-rp-334-miliar"
EDC = "https://www.bca.co.id/en/bisnis/produk/penerimaan-bisnis/EDC-BCA"
QRB = "https://www.bca.co.id/en/bisnis/produk/penerimaan-bisnis/QRIS-bisnis"
BDC = "https://www.bca.co.id/en/bisnis/solusi/business-debit-card"
API = "https://www.bca.co.id/en/bisnis/solusi/api"
WA = "https://bca.co.id/id/informasi/news-and-features/2026/08/28/18/05/notifikasi-layanan-kartu-kredit-bca-kini-hadir-melalui-whatsapp"
HR = "https://www.bca.co.id/en/tentang-bca/sustainability/social/human-capital-management/rekrutmen-and-turnover"
PASPOR17 = "https://www.industry.co.id/read/20037/bekerjasama-dengan-mastercard-bca-luncurkan-kartu-paspor-bca-mastercard"
TIKET21 = "https://finansial.bisnis.com/read/20211025/90/1458032/dukung-pariwisata-bca-gandeng-tiketcom-rilis-mastercard"
BBT26 = "https://investortrust.id/financial/116028/transaksi-capai-rp-3-triliun-bca-integrasikan-kartu-kredit-blibli-dan-tiketcom-jadi-bca-blibli-tiket-mastercard"
BBTP = "https://www.bca.co.id/en/Individu/produk/Kartu-Kredit/bca-blibli-tiket-mastercard"
CC25 = "https://keuangan.kontan.co.id/news/nilai-transaksi-kartu-kredit-bca-capai-rp-63-triliun-tumbuh-9"
CC25B = "https://keuangan.kontan.co.id/news/transaksi-kartu-kredit-bca-tumbuh-14-di-2025"
VFIFA = "https://promo.bca.co.id/en/all/2026/03/13/04/kartu-kredit-bca-visa"
VBTS = "https://mediaasuransinews.co.id/ekonomi-digital/visa-perkuat-posisi-strategis-di-industri-global-lewat-bts-world-tour-arirang"
BLUD = "https://blubybcadigital.id/fitur/kartu/bludebit-card"
BLUV = "https://blubybcadigital.id/fitur/kartu/bluvirtual-card"
BLU5 = "https://selular.id/2026/09/5-tahun-bca-digital-blu-catat-pertumbuhan-dpk-dan-ekosistem-2-0/"
BLUH1 = "https://finansial.bisnis.com/read/20260906/90/2001705/laba-bca-digital-blu-melonjak-5313-jadi-rp12959-miliar-semester-i2026"
AFFIN = "https://www.thestar.com.my/business/business-news/2026/08/19/affin-bca-forge-strategic-partnership-to-boost-cross-border-customer-benefits"
CEO = "https://tirto.id/gantikan-jahja-hendra-lembong-resmi-menjabat-presdir-bca-hcAk"
KKIL = "https://bernama.com/en/news.php?id=2595641"
QRIS7 = "https://katadata.co.id/finansial/keuangan/6a857021225bb/transaksi-qris-juli-2026-tumbuh-82-42-yoy-bi-fast-tembus-546-juta"
ARTA = "https://www.commercialpaymentsinternational.com/?p=4602"
USTR = "https://indonesiabusinesspost.com/4191/policy/govt-remains-open-to-foreign-operators-despite-u-s-criticism-of-qris-system"
ART = "https://www.whitehouse.gov/fact-sheets/2026/02/fact-sheet-trump-administration-finalizes-trade-deal-with-indonesia"
BCAF = "https://keuangan.kontan.co.id/news/perkuat-bisnis-pembiayaan-otomotif-bca-finance-dan-bca-multifinance-resmi-merger"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · AI", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Rp1,661 trillion of assets and 85% CASA funding, the Hartono family's control, a bank rebuilt after 1998, an on-premise AI stack and a transaction-banking strategy.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & returns", "blurb": "Rp29.5tn profit in 1H26.", "div": "bca", "rev": "grp", "products": [
            P("balance", "Balance sheet & earnings, 1H26", "Net profit Rp29.5 trillion in the half to June 2026 (+1.8%); assets Rp1,661 trillion, loans Rp1,036 trillion (+8.0%), CASA Rp1,082 trillion (85.2% of funding); ROE 24.1%, NIM 5.3%, CAR 26.8%, gross NPL 1.9%.",
              s=["con"], neo=[0, ""], src=[["BCA 1H26 results, Jul 2026", H1]]),
            P("fy25", "Full year 2025", "Net profit Rp57.5 trillion (+4.9%), operating income Rp111.1 trillion, loans Rp993 trillion (+7.7%), CASA up 13.1%; 34.3 million customers at FY25 against 32.9 million in the 1H26 deck ⚠ (definitions differ).",
              s=["con"], neo=[0, ""], src=[["BCA FY25 results presentation", FY25], ["BCA 1H26 results, Jul 2026", H1]]),
        ]},
        {"id": "1.2", "ic": "badge-check", "name": "Owners & heritage", "blurb": "Hartono-controlled since 2002.", "div": "bca", "rev": "grp", "products": [
            P("owners", "Ownership & listing", "Listed on the Indonesia Stock Exchange (BBCA), market value Rp769 trillion on 27 July 2026, the largest of any Indonesian bank. PT Dwimuria Investama Andalan owns 54.94%; after Bambang Hartono's death, Robert Budi Hartono is the ultimate shareholder. Fitch BBB, outlook negative ⚠; Pefindo idAAA.",
              s=["corp"], neo=[0, ""], src=[["BCA 1H26 results, Jul 2026", H1]]),
            P("heritage", "Heritage", "Founded 1955, open for business in 1957; taken over and recapitalised by IBRA after the 1998 bank run, listed in 2000, 51% sold to the Hartono group's FarIndo in 2002, state exit in 2005.",
              s=["con"], o="I", neo=[0, ""], src=[["BCA: milestones", HIST]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Leadership", "blurb": "Lembong and Setiaatmadja.", "div": "bca", "rev": "grp", "products": [
            P("leadership", "Boards", "President Director Gregory Hendra Lembong since 1 June 2025; Jahja Setiaatmadja, President Director for about 14 years, now President Commissioner. Deputy Presidents Armand Wahyudi Hartono and John Kosasih; directors include Santoso (cards), Vera Eve Lim and Lianawaty Suwono. About 25,000 staff ⚠ (inferred from turnover).",
              s=["corp"], st="new", ay="Jun 2025", neo=[0, ""], src=[["BCA: management", MGMT], ["Tirto: Lembong takes over, 2025", CEO], ["BCA: recruitment and turnover", HR]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "Technology & AI", "blurb": "On-premise LLM, ISO 42001.", "div": "bca", "rev": "grp", "products": [
            P("tech", "Data centres & on-premise AI", "An on-premise large language model on more than 50 GPUs for data sovereignty; ISO 42001 for AI management and ISO 27701 for personal data; mirrored data centres and a disaster recovery centre in Surabaya.",
              s=["corp"], o="B", neo=[0, ""], src=[["BCA 1H26 results, Jul 2026", H1], ["BCA: milestones", HIST]]),
            P("ai", "AI at work", "AI cuts onboarding to about 4 minutes (from 8), generates merchant and API leads, values collateral, helps score corporate loans, watches debtors through news analytics, and runs the VIRA chatbot.",
              s=["con", "corp"], st="new", o="B", neo=[0, "BCA's own."],
              mc="AI is built in-house; Agent Pay for myBCA is untested ground.",
              src=[["BCA 1H26 results, Jul 2026", H1]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "The supply-chain bank.", "div": "bca", "rev": "txn", "products": [
            P("strategy", "Transaction-banking strategy", "BCA sells itself as the bank for a whole supply chain, from principal to distributor, retailer and end customer, with 99.8% of transaction volume digital and volume up 60% in three years.",
              s=["sme", "corp"], neo=[0, ""], src=[["BCA 1H26 results, Jul 2026", H1]]),
            P("deals", "Deals 2019–2026", "Bank Royal (2019) became BCA Digital; Rabobank Indonesia merged into BCA Syariah (2020); BCA Finance absorbed BCA Multi Finance (2024 ⚠); a cross-border privileges deal with Malaysia's Affin Bank (August 2026).",
              s=["corp"], o="A", neo=[0, ""], src=[["BCA: milestones", HIST], ["Kontan: BCA Finance merger", BCAF], ["The Star: Affin and BCA, Aug 2026", AFFIN]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: Paspor debit on GPN or Mastercard, credit cards on five networks plus BCA's own, co-brands with Blibli Tiket and Singapore Airlines, QRIS, BI-FAST and Flazz, the new KKI and Paylater, cross-border QR, merchant acceptance and business payments.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "GPN or Mastercard.", "div": "bca", "rev": "cons", "products": [
            P("paspor", "Paspor BCA GPN", "The default debit card on Tahapan accounts: Debit BCA and GPN acceptance at home, cash at BCA and PRIMA ATMs; Blue, Gold and Platinum.", short="Paspor GPN",
              s=["con"], lc="everyday", neo=[0, "GPN."], src=[["BCA: Tahapan and Paspor BCA", TAHAPAN]]),
            P("paspormc", "Paspor BCA Mastercard", "The same Paspor card with Mastercard for online and overseas spending and Cirrus ATMs worldwide, launched 21 November 2017 by Jahja Setiaatmadja and Mastercard's Safdar Khan; domestic purchases still run as Debit BCA. No Visa debit found.", short="Paspor Mastercard",
              s=["con", "trav"], lc="everyday", ay="Nov 2017", o="P", at="Mastercard", neo=[1, "Mastercard abroad and online; Debit BCA at home."],
              mc="Mastercard's only debit role at the parent bank; customers choose it over the GPN card.",
              src=[["BCA: Tahapan and Paspor BCA", TAHAPAN], ["Industry.co.id: Paspor BCA Mastercard, Nov 2017", PASPOR17]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Five networks plus BCA Card.", "div": "bca", "rev": "cons", "products": [
            P("bcacard", "BCA Card", "BCA's own domestic credit card network: BCA Everyday Card and BCA Card Platinum.", short="BCA Card (own network)",
              s=["con"], lc="borrow", o="B", neo=[0, "BCA's own network."], src=[["BCA: credit card options", CARDS]]),
            P("mccc", "BCA Mastercard Black, World & Globe", "Mastercard credit cards for affluent and lifestyle customers; World earns 0.2% Reward BCA, 0% instalments abroad and is free for Solitaire clients. Part of about 4.9 million BCA credit cards (June 2025) ⚠.", short="Mastercard credit",
              s=["con", "aff", "trav"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["BCA: credit card options", CARDS], ["BCA: Mastercard World", MCW], ["Kontan: 4.9m BCA cards, Oct 2025", CC25]]),
            P("visacc", "BCA Visa Black & Visa Batman", "Visa credit cards; Visa ran a FIFA World Cup 2026 top-spender campaign for BCA Visa holders (March–April 2026) and a BTS concert ticket draw (August–November 2026 ⚠).", short="Visa credit",
              s=["con", "aff"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["BCA: credit card options", CARDS], ["BCA promo: Visa FIFA top spender, Mar 2026", VFIFA], ["Media Asuransi: Visa and BTS", VBTS]]),
            P("othercc", "BCA JCB Black, UnionPay & American Express", "JCB Black, a BCA UnionPay card and BCA American Express Platinum (no online application offered ⚠); credit card-led consumer loans Rp20.23 trillion at December 2025 (+14%).", short="JCB, UnionPay, Amex",
              s=["con", "aff"], lc="borrow", o="P", at="JCB, UnionPay, Amex", neo=[0, "JCB, UnionPay, Amex."], src=[["BCA: credit card options", CARDS], ["Kontan: card transactions 2025, Jan 2026", CC25B]]),
        ]},
        {"id": "2.3", "ic": "plane", "name": "Co-brand cards", "blurb": "Blibli Tiket and KrisFlyer.", "div": "bca", "rev": "cons", "products": [
            P("bbt", "BCA Blibli Tiket Mastercard", "Launched 12 September 2026 at BCA Expo, folding the BCA Blibli and BCA tiket.com (October 2021) co-brands into one card with Blibli Tiket Points; about 360,000 cards and nearly Rp3 trillion a year of spending across the two.", short="Blibli Tiket (Mastercard)",
              s=["con", "trav"], lc="borrow", st="new", ay="Sep 2026", o="P", at="Blibli, Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's newest BCA card and the clearest co-brand win.",
              src=[["Investortrust: Blibli Tiket Mastercard, Sep 2026", BBT26], ["BCA: Blibli Tiket Mastercard", BBTP], ["Bisnis: tiket.com Mastercard, Oct 2021", TIKET21]]),
            P("krisflyer", "BCA Singapore Airlines KrisFlyer Visa", "KrisFlyer Visa Signature, KrisFlyer Visa Infinite and PPS Club Visa Infinite, earning miles faster.", short="KrisFlyer (Visa)",
              s=["aff", "trav"], lc="borrow", o="P", at="Singapore Airlines, Visa", neo=[0, "Visa."], src=[["BCA: credit card options", CARDS]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "Domestic rails", "blurb": "QRIS, BI-FAST, Flazz.", "div": "bca", "rev": "txn", "products": [
            P("qris", "QRIS & QRIS Tap", "QR payments by scan or customer-presented code, and NFC Pay (QRIS Tap) by Android phone or smartwatch, up to Rp1 million a tap; nationally 65.77 million users and 44.86 million merchants at June 2026.", short="QRIS",
              s=["con", "young"], lc="move", st="new", o="P", at="Bank Indonesia", neo=[0, "QRIS."],
              src=[["BCA: NFC Pay", NFC], ["Bernama: KKI launch and QRIS, Aug 2026", KKIL], ["BCA 1H26 results, Jul 2026", H1]]),
            P("bifast", "Transfers & BI-FAST", "Real-time transfers on Bank Indonesia's BI-FAST rail, which carried 546 million transactions in July 2026 (+31.62%), alongside virtual accounts and host-to-host payments.", short="BI-FAST",
              s=["con", "sme"], lc="move", o="P", at="Bank Indonesia", neo=[0, "BI-FAST."], src=[["Katadata: QRIS and BI-FAST, Jul 2026", QRIS7], ["BCA 1H26 results, Jul 2026", H1]]),
            P("flazz", "Flazz", "A stored-value RFID card since 2007 for toll roads, Transjakarta, MRT, LRT and commuter rail, and more than 57,000 merchant outlets; topped up by NFC in myBCA.",
              s=["con", "young"], lc="everyday", o="B", neo=[0, "BCA closed loop."], src=[["BCA: Flazz", FLAZZ], ["BCA: milestones", HIST]]),
        ]},
        {"id": "2.5", "ic": "hand-coins", "name": "KKI & Paylater", "blurb": "Credit over QRIS.", "div": "bca", "rev": "cons", "products": [
            P("kki", "BCA Kartu Kredit Indonesia", "A virtual domestic credit card that funds QRIS scan, QRIS customer-presented and QRIS Tap in myBCA; BCA was one of eight issuers when Bank Indonesia opened the KKI to individuals on 17 August 2026.", short="KKI (domestic)",
              s=["con"], lc="borrow", st="new", ay="Aug 2026", o="P", at="Bank Indonesia", neo=[0, "GPN and QRIS."],
              mc="A national credit rail that bypasses the international networks at home.",
              src=[["BCA: Kartu Kredit Indonesia", KKI], ["Bernama: KKI launch, Aug 2026", KKIL]]),
            P("paylater", "Paylater BCA", "A revolving limit of Rp1–20 million in myBCA, usable for QRIS; about 196,000 users at June 2026 (+8%) and Rp334 billion outstanding.",
              s=["con", "young"], lc="borrow", st="new", o="B", neo=[0, "QRIS."], src=[["BCA: Paylater BCA", PAYL], ["Kontan: Paylater BCA, Jun 2026", PAYLK]]),
        ]},
        {"id": "2.6", "ic": "earth", "name": "Cross-border", "blurb": "QR in six countries.", "div": "bca", "rev": "txn", "products": [
            P("xbqr", "Cross-border QR", "myBCA customers pay by QR in Singapore, Malaysia, Thailand, Japan (from 17 August 2025), South Korea and China (2026 ⚠) through Bank Indonesia's bilateral links.", short="Cross-border QR",
              s=["trav"], lc="move", st="new", ay="Aug 2025", o="P", at="Bank Indonesia", neo=[0, "Bilateral QR links."],
              mc="Bilateral QR takes the overseas small-ticket spend that cards used to carry.",
              src=[["BCA: QRIS in Japan, Aug 2025", QRJP], ["BCA: cross-border QRIS countries", QRXB]]),
            P("fx", "FX pockets & forex deposits", "Foreign-currency pockets in 18 currencies and USD and SGD e-deposits inside myBCA.",
              s=["trav", "aff"], lc="grow", neo=[None, "Network role not public."], src=[["BCA 1H26 results, Jul 2026", H1]]),
        ]},
        {"id": "2.7", "ic": "store", "name": "Acceptance", "blurb": "EDC BCA and QRIS.", "div": "bca", "rev": "txn", "products": [
            P("edc", "EDC BCA & Merchant BCA app", "Card terminals that accept payments from various issuers, managed in the Merchant BCA app; merchant numbers up 2.2 times and QRIS volume 11 times in three years.", short="EDC BCA",
              s=["mer"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["BCA: EDC BCA", EDC], ["BCA 1H26 results, Jul 2026", H1]]),
            P("qrism", "QRIS for merchants", "Static and dynamic QRIS for small merchants, with real-time reports in the Merchant BCA app and QR Merchant Service.", short="Merchant QRIS",
              s=["mer"], lc="move", o="P", at="Bank Indonesia", neo=[0, "QRIS."], src=[["BCA: QRIS for business", QRB]]),
        ]},
        {"id": "2.8", "ic": "briefcase-business", "name": "Business payments", "blurb": "Cash management on GPN.", "div": "bca", "rev": "comm", "products": [
            P("cashmgmt", "KlikBCA Bisnis & myBCA Bisnis", "Online business banking for transfers, payroll, bulk payments, trade, forex and supply-chain finance, with virtual accounts and host-to-host ERP links.", short="Cash management",
              s=["sme", "corp"], lc="move", o="B", neo=[0, ""], src=[["BCA 1H26 results, Jul 2026", H1]]),
            P("bdc", "Business Debit Card", "Petty-cash, loyalty and deposit cards for companies, on GPN, with limits set through BCA's business channels.", short="Business Debit (GPN)",
              s=["sme", "corp"], lc="move", o="B", neo=[0, "GPN."],
              mc="No commercial credit or virtual card is visible: a gap for a fast-growing corporate book.",
              src=[["BCA: Business Debit Card", BDC]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: AI fraud detection and face biometrics, card controls in the app, API BCA for business, and Reward BCA with instalments across the card range.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Fraud complaints down 47%.", "div": "bca", "rev": "txn", "products": [
            P("fraud", "Fraud detection", "AI detection of anomalous and suspicious transactions; fraud complaints down 47% year on year in 1H26; a 24/7 security monitoring centre and a CISO.",
              s=["con", "mer"], lc="everyday", o="B", neo=[0, "BCA's own."],
              mc="Mastercard's fraud scoring already serves GPN debit through Artajasa ⚠; BCA's link is not public.",
              src=[["BCA 1H26 results, Jul 2026", H1], ["Mastercard and Artajasa (undated ⚠)", ARTA]]),
            P("kyc", "Face biometrics & e-KYC", "Face biometrics for onboarding and new-device registration; online account opening in about 4 minutes and about 57% of accounts opened online in 1H26.", short="Biometric KYC",
              s=["con", "young"], lc="open", st="new", o="B", neo=[0, ""], src=[["BCA 1H26 results, Jul 2026", H1]]),
            P("cardcontrol", "Card controls & alerts", "Contactless on/off and limits for Visa, Mastercard and other BCA cards in BCA mobile and myBCA; card notifications by WhatsApp from 2 September 2026.", short="Card controls",
              s=["con"], lc="everyday", st="new", o="B", neo=[1, "Covers Mastercard cards among others."], src=[["BCA: contactless credit cards", CTLS], ["BCA: WhatsApp notifications, Aug 2026", WA]]),
        ]},
        {"id": "3.2", "ic": "code-xml", "name": "APIs", "blurb": "API BCA.", "div": "bca", "rev": "txn", "products": [
            P("api", "API BCA", "APIs for corporates and individual businesses (balances, statements, transfers), virtual accounts and host-to-host settlement; AI now finds new API clients.",
              s=["mer", "corp"], lc="open", o="B", neo=[0, ""], src=[["BCA: API BCA", API], ["BCA 1H26 results, Jul 2026", H1]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & instalments", "blurb": "Reward BCA, Cicilan BCA.", "div": "bca", "rev": "cons", "products": [
            P("rewards", "Reward BCA & partner points", "Reward BCA on Visa and Mastercard spend, KrisFlyer miles on Singapore Airlines cards, Blibli Tiket Points, and cross-border privileges for BCA cardholders in Malaysia under the Affin deal (August 2026).", short="Reward BCA",
              s=["con", "aff", "trav"], lc="grow", o="B", neo=[1, "Earned on Mastercard and Visa cards."],
              mc="Card-linked offers could feed Reward BCA and the Affin privileges.",
              src=[["BCA: Mastercard World", MCW], ["BCA: Blibli Tiket Mastercard", BBTP], ["The Star: Affin and BCA, Aug 2026", AFFIN]]),
            P("cicilan", "Cicilan BCA", "Instalments on BCA credit cards, including 0% instalments for overseas spending on the Mastercard World card.", short="Instalments",
              s=["con"], lc="borrow", o="B", neo=[1, "Runs on every card network BCA issues."], src=[["BCA: Mastercard World", MCW]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: corporate loans growing 13.6%, commercial and SME lending, mortgages and BCA Finance car loans, and wealth, insurance and sharia banking through the subsidiaries.",
    "tiles": [
        {"id": "4.1", "ic": "building-2", "name": "Corporate lending", "blurb": "Rp513tn, +13.6%.", "div": "bca", "rev": "corp", "products": [
            P("corplend", "Corporate loans", "Rp513.4 trillion at June 2026 (+13.6%), led by investment loans in manufacturing, business services, utilities and mining.",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="Payroll and supply-chain clients with no visible commercial card.",
              src=[["BCA 1H26 results, Jul 2026", H1]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Commercial & SME", "blurb": "Rp289tn of loans.", "div": "bca", "rev": "comm", "products": [
            P("smelend", "Commercial & SME loans", "Commercial loans Rp153.9 trillion and SME loans Rp134.6 trillion (+6.0%) at June 2026; the SME customer base is up 36% in four years.",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["BCA 1H26 results, Jul 2026", H1]]),
        ]},
        {"id": "4.3", "ic": "house", "name": "Homes & cars", "blurb": "Mortgages up, cars down.", "div": "finance", "rev": "cons", "products": [
            P("mortgage", "Mortgages", "Rp144.3 trillion at June 2026 (+4.8%), new bookings up 10.2%; more than half in Jakarta.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["BCA 1H26 results, Jul 2026", H1]]),
            P("auto", "Vehicle loans & BCA Finance", "Vehicle loans Rp51.3 trillion (-21.5%) as car sales fell; BCA Finance absorbed BCA Multi Finance's motorcycle business (2024 ⚠).", short="Vehicle loans",
              s=["con"], lc="borrow", st="flux", o="A", neo=[0, ""], src=[["BCA 1H26 results, Jul 2026", H1], ["Kontan: BCA Finance merger", BCAF]]),
        ]},
        {"id": "4.4", "ic": "gem", "name": "Wealth, insurance & sharia", "blurb": "Rp339tn AUM.", "div": "insure", "rev": "grp", "products": [
            P("wealth", "Prioritas, Solitaire & BCA Sekuritas", "Rp339 trillion of mutual funds and bonds sold (+16%), BCA Prioritas and Solitaire for wealthier clients, brokerage through BCA Sekuritas.", short="Wealth",
              s=["aff"], lc="grow", neo=[0, ""], src=[["BCA 1H26 results, Jul 2026", H1], ["BCA: subsidiaries", SUBS]]),
            P("insure", "BCA Insurance & BCA Life", "General and life insurance sold in myBCA, including travel, property and pet cover.", short="Insurance",
              s=["aff", "con"], lc="beyond", neo=[0, ""], src=[["BCA 1H26 results, Jul 2026", H1], ["BCA: subsidiaries", SUBS]]),
            P("syariah", "BCA Syariah", "Sharia banking, enlarged by Rabobank Indonesia in 2020; sharia financing Rp13.6 trillion and gold financing in its app.",
              s=["con", "sme"], lc="borrow", o="A", neo=[0, ""], src=[["BCA: milestones", HIST], ["BCA 1H26 results, Jul 2026", H1]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach BCA: two mobile apps, blu for the young with Mastercard debit cards, 1,272 branches and 20,300 ATMs with Halo BCA, and partners from Blibli to Affin.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Mobile apps", "blurb": "myBCA and BCA mobile.", "div": "bca", "rev": "txn", "products": [
            P("mybca", "myBCA", "Launched 2021; users up 24 times in four years (+53% YoY), 49% of mobile-banking value; pockets, cards, QRIS Tap, cross-border QR, Paylater and KKI in one app, in Bahasa Indonesia, English and Mandarin.",
              s=["con", "young", "trav"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="The app already holds the cards: the place for tokenised Mastercard credentials.",
              src=[["BCA 1H26 results, Jul 2026", H1]]),
            P("bcamobile", "BCA mobile & KlikBCA", "The classic app since 2011 and KlikBCA internet banking; 99.8% of transaction volume is now digital.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["BCA 1H26 results, Jul 2026", H1], ["BCA: milestones", HIST]]),
        ]},
        {"id": "5.2", "ic": "rocket", "name": "blu by BCA Digital", "blurb": "Mastercard debit for the young.", "div": "blu", "rev": "grp", "products": [
            P("blu", "blu by BCA Digital", "The digital bank (Bank Royal until 2020): about 3.7 million customers at end-2025 ⚠, 91% Gen Z and millennials; H1 2026 profit Rp129.6 billion (+53%), deposits up 20%.",
              s=["young"], lc="open", st="active", o="A", neo=[0, ""], src=[["Bisnis: BCA Digital H1 2026", BLUH1], ["Selular: five years of blu, Sep 2026", BLU5]]),
            P("bludebit", "bluDebit, Garuda x bluDebit & bluVirtual cards", "Physical, Garuda co-brand and virtual debit cards on Mastercard, used at home and abroad, with no FX fee in eight currencies and Mastercard E-Commerce Purchase Protection on the virtual card.", short="blu cards (Mastercard)",
              s=["young", "trav"], lc="everyday", o="P", at="Mastercard, Garuda Indonesia", neo=[2, "Mastercard."],
              mc="Every blu card is a Mastercard.",
              src=[["blu: bluDebit Card", BLUD], ["blu: bluVirtual Card", BLUV], ["Selular: five years of blu, Sep 2026", BLU5]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & Halo BCA", "blurb": "1,272 branches, 20,300 ATMs.", "div": "bca", "rev": "txn", "products": [
            P("branches", "Branches & ATMs", "1,272 branches and 20,300 ATMs in 307 cities, about 75% of them cash recycling machines; about 64% of branch transactions done on machines.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["BCA 1H26 results, Jul 2026", H1]]),
            P("halo", "Halo BCA & VIRA", "A 24/7 contact centre, the VIRA virtual assistant and WhatsApp notifications.", short="Halo BCA",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["BCA 1H26 results, Jul 2026", H1], ["BCA: WhatsApp notifications, Aug 2026", WA]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners", "blurb": "Blibli, Affin.", "div": "bca", "rev": "cons", "products": [
            P("partners", "Ecosystem partners", "Blibli and tiket.com for co-brand cards, Singapore Airlines for miles, Affin Bank for privileges in Malaysia (August 2026), and the yearly BCA Expo.",
              s=["con", "trav"], lc="beyond", st="new", o="P", at="Blibli, Singapore Airlines, Affin", neo=[0, ""],
              src=[["Investortrust: Blibli Tiket Mastercard, Sep 2026", BBT26], ["The Star: Affin and BCA, Aug 2026", AFFIN]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BCA", "blurb": "Abroad and online, not at home.", "products": [
        P("mcatbca", "Mastercard at BCA", "Mastercard carries the Paspor debit card abroad and online (since 2017), four credit cards including the Blibli Tiket co-brand (September 2026), and every blu card. At home BCA runs on GPN, its own BCA Card and Debit BCA, QRIS, BI-FAST and Flazz; Visa holds the Singapore Airlines and premium lines.",
          s=["con"], div="bca", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Industry.co.id: Paspor BCA Mastercard, Nov 2017", PASPOR17], ["Investortrust: Blibli Tiket Mastercard, Sep 2026", BBT26], ["BCA: credit card options", CARDS]]),
    ]},
    {"id": "pillar-market", "name": "Indonesian payments", "blurb": "GPN, QRIS, BI-FAST, KKI.", "products": [
        P("market", "The Indonesian market", "Bank Indonesia's national rails keep growing: QRIS volume up 82% in July 2026, BI-FAST at 546 million transactions a month, and the KKI open to individuals since August 2026. The US named QRIS and GPN as trade barriers in 2025; the February 2026 trade deal promises a level playing field for US payment firms ⚠.",
          s=["con"], div="bca", rev="grp",
          src=[["Katadata: QRIS and BI-FAST, Jul 2026", QRIS7], ["Indonesia Business Post: QRIS and the US, Apr 2025", USTR], ["White House: Indonesia trade deal, Feb 2026", ART]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
