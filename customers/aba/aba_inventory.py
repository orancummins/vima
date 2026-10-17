"""ABA Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are ABA's own audited 2025 results (released 24 April 2026) and National Bank of Canada's filings for
the quarter to 31 July 2026 (26 August 2026), unless a source says otherwise. ababank.com was not reachable
(bot challenge), so ABA's releases are cited from Cambodia Investment Review, and pages seen only in search
results are marked ⚠. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

NBCQ3 = "https://www.nbc.ca/content/dam/bnc/a-propos-de-nous/relations-investisseurs/resultats-trimestriels/2026/report-shareholder-q3-2026.pdf"
NBCQ3P = "https://www.nbc.ca/content/dam/bnc/a-propos-de-nous/relations-investisseurs/resultats-trimestriels/2026/presentation-q3-2026.pdf"
NBCQ4P = "https://www.nbc.ca/content/dam/bnc/a-propos-de-nous/relations-investisseurs/resultats-trimestriels/2025/presentation-q4-2025.pdf"
STAKE19 = "https://www.newswire.ca/news-releases/national-bank-increases-its-stake-to-100-in-cambodia-based-aba-bank-892785055.html"
STAKE16 = "https://www.retailbankerinternational.com/news/national-bank-of-canada-takes-majority-stake-in-aba-bank-of-cambodia-100516-4888365/"
FY25 = "https://cambodiainvestmentreview.com/2026/04/24/aba-bank-remains-top-cambodian-bank-in-2025-supports-countrys-economic-growth/"
FY24 = "https://cambodiainvestmentreview.com/2025/04/22/aba-bank-strengthens-financial-position-in-2024-with-major-capital-boost-and-robust-deposit-growth/"
AGRI = "https://cambodiainvestmentreview.com/2026/01/29/aba-bank-becomes-key-investor-in-cambodias-first-ever-agriculture-bond/"
RETAIL = "https://cambodiainvestmentreview.com/2026/06/16/aba-bank-named-best-retail-bank-at-the-asian-banker-awards-2026/"
FORBES = "https://cambodiainvestmentreview.com/2026/09/16/aba-bank-named-cambodias-no-1-bank-in-forbes-worlds-top-performing-banks-2026/"
CIB = "https://cambodiainvestmentreview.com/2026/07/27/leader-talks-huot-chanthida-on-building-abas-award-winning-corporate-banking-franchise-and-financing-cambodias-growth/"
ONLINECORP = "https://cambodiainvestmentreview.com/2026/10/13/aba-bank-wins-best-online-corporate-bank-cambodia-2026/"
SECTOR = "https://cambodiainvestmentreview.com/2026/04/21/exclusive-cambodias-banking-sector-faces-a-confidence-test-not-a-crisis-as-sector-loan-to-deposit-ratio-improves-to-95-for-first-time-in-five-years/"
GRAB = "https://cambodiainvestmentreview.com/2024/11/19/aba-bank-and-grab-cambodia-announce-strategic-partnership-to-enhance-payment-facilities/"
TOG = "https://cambodiainvestmentreview.com/2025/09/17/aba-bank-and-t-o-group-strengthen-partnership-to-expand-digital-payment-solutions-in-cambodia/"
TOG26 = "https://cambodiainvestmentreview.com/2026/05/19/aba-bank-and-t-o-group-expand-strategic-partnership-to-advance-digital-payment-solutions/"
SHOPIFY = "https://cambodiainvestmentreview.com/2025/10/21/aba-payway-becomes-cambodias-first-payment-gateway-on-shopify/"
CATA = "https://cambodiainvestmentreview.com/2026/04/08/aba-bank-and-cata-partner-to-launch-hajj-fund-and-interest-free-mode-for-cambodian-muslim-community/"
MOI = "https://cambodiainvestmentreview.com/2026/04/29/aba-and-ministry-of-interior-partner-to-enable-seamless-online-payments/"
CHARGE = "https://cambodiainvestmentreview.com/2025/01/27/aba-bank-and-charge-cambodia-join-forces-to-simplify-ev-payments-and-boost-charging-network-growth/"
ETIQA = "https://cambodiainvestmentreview.com/2026/07/01/aba-bank-partners-with-etiqa-general-insurance-cambodia-to-expand-digital-access-to-general-insurance-nationwide/"
JPM = "https://cambodiainvestmentreview.com/2026/01/12/aba-bank-sets-global-benchmark-with-elite-quality-recognition-award-2025-from-jp-morgan/"
INNOV = "https://cambodiainvestmentreview.com/2025/11/17/aba-bank-wins-financial-innovation-of-the-year-for-digital-banking-excellence/"
VISA24 = "https://cambodiainvestmentreview.com/2025/02/27/aba-bank-garners-eight-awards-from-visa-solidifying-its-market-leadership-in-cambodia/"
VISA25 = "https://cambodiainvestmentreview.com/2026/03/02/aba-triumphs-with-10-visa-leadership-awards-2025-reinforcing-excellence-in-digital-payment/"
EXTAFF = "https://cambodiainvestmentreview.com/2026/08/27/clr-50-khmer-women-voices-2026-romny-theam-executive-vice-president-chief-external-affairs-officer-regional-manager-at-aba-bank/"
PFM = "https://cambodiainvestmentreview.com/2025/08/14/aba-bank-launches-cambodias-first-financial-analytics-tool-in-aba-mobile/"
PAYSOUND = "https://cambodiainvestmentreview.com/2026/06/29/aba-bank-targets-payment-verification-challenges-for-cambodias-busy-fb-vendors-with-new-paysound-feature/"
DOCV = "https://cambodiainvestmentreview.com/2026/09/28/aba-bank-introduces-instant-document-verification-for-a-more-convenient-experience/"
KIOSK = "https://fintech.global/2022/11/25/aba-bank-launches-instant-card-issuance-kiosk/"
FY22 = "https://cambodiainvestmentreview.com/2023/07/13/aba-bank-retains-top-spot-for-second-consecutive-year-in-2022-amidst-challenging-post-pandemic-economy/"
BAKONG = "https://cambodiainvestmentreview.com/2026/10/16/cambodias-bakong-processes-1-33-billion-transactions-as-soramitsu-marks-hyperledger-irohas-10th-anniversary/"
BAKONGSITE = "https://bakong.nbc.gov.kh/en/"
KHQRDATA = "https://cambodiainvestmentreview.com/2026/06/08/exclusive-cambodias-digital-economy-reaches-new-milestone-as-mobile-banking-users-surpass-10-million-and-khqr-payments-exceed-105-billion-annually/"
IMF = "https://cambodiainvestmentreview.com/2026/09/29/imf-sees-cambodia-growth-slowing-to-3-and-inflation-reaching-5-6-in-2026-as-property-and-banking-risks-mount/"
VISASEC = "https://cambodiainvestmentreview.com/2026/06/18/visa-refreshes-cambodias-payment-security-roadmap-to-strengthen-trust-and-resilience-in-digital-payments/"
CANADIA = "https://cambodiainvestmentreview.com/2026/09/28/a-world-of-privilege-is-coming-canadia-bank-previews-its-new-prestigious-world-credit-card-from-mastercard/"
# ababank.com pages, seen in search results only (the site returned a bot challenge) ⚠
MCAWARDS = "https://www.ababank.com/en/aba-news/aba-clinches-three-awards-from-mastercard-for-market-leadership/"
VIRTUAL = "https://www.ababank.com/aba-news/instant-account-holders-can-now-issue-and-order-cards-in-aba-mobile/"
HISTORY = "https://ababank.com/about-us/history"
UPI15 = "https://www.ababank.com/aba-news/unionpay-international-cards-are-now-available-at-aba-bank/"
KHQR22 = "https://ababank.com/aba-news/aba-bank-now-supports-khqr-for-greater-convenience-of-its-qr-paymen"
ATMS = "https://www.ababank.com/aba-online/atm-network/atms/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owner · licence", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Cambodia's largest bank with US$16.2 billion of assets and US$377.5 million of profit in 2025, about a fifth of the country's deposits, wholly owned by National Bank of Canada since 2019, and a plan to become a universal bank.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "US$16.2bn assets, US$377.5m profit.", "div": "aba", "rev": "retail", "products": [
            P("balance", "Balance sheet & earnings", "Total assets US$16.2 billion (+17%), deposits nearly US$13 billion (+17%), gross loans US$9.6 billion (+11%), net profit US$377.5 million (+26%) and equity US$2.7 billion in 2025. In the quarter to 31 July 2026 net income was C$125 million (+5%; about +1% at constant currency), with provisions rising as loans turned bad.",
              s=["con", "corp"], neo=[0, ""], src=[["CIR: ABA 2025 results, Apr 2026", FY25], ["National Bank of Canada: Q3 2026 report", NBCQ3], ["National Bank of Canada: Q3 2026 presentation", NBCQ3P]]),
            P("share", "Market position", "Number one in Cambodia by assets, deposits, loans and profit; about 16% of system assets and about 20% of deposits ⚠ (derived from a US$100.2 billion system). Ranked 31st in Forbes' World's Top Performing Banks 2026 (US$10–20 billion tier), the top Cambodian bank.",
              s=["con"], neo=[0, ""], src=[["CIR: banking sector 2025, Apr 2026", SECTOR], ["CIR: Forbes ranking, Sep 2026", FORBES]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Azhikhanov and team.", "div": "aba", "rev": "retail", "products": [
            P("leadership", "Executive team", "President and CEO Askhat Azhikhanov; Deputy CEO and COO Zhiger Atchabarov; Chief Digital Officer Zokhir Rasulov; Chief Card & E-Payment Officer Sanzhar Abdullayev; Chief Corporate Banking Officer Huot Chanthida; Chief External Affairs Officer Romny Theam. Board chair not found ⚠.",
              s=["corp"], neo=[0, ""], src=[["CIR: ABA and Etiqa, Jul 2026", ETIQA], ["CIR: agriculture bond, Jan 2026", AGRI], ["CIR: Romny Theam, Aug 2026", EXTAFF]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & owner", "blurb": "Founded 1996; Canadian since 2014.", "div": "parent", "rev": "retail", "products": [
            P("heritage", "National Bank of Canada ownership", "Founded in 1996. National Bank of Canada bought 10% in 2014, 42% in 2015, 90% in 2016 (US$103 million) and the rest in October 2019 (99.99% ⚠), US$320 million in all. Clients grew from 60,000 to 600,000 and branches from 12 to 70 over 2014–19. ABA is reported in the parent's U.S. Specialty Finance and International segment.",
              s=["corp"], o="A", neo=[0, ""], src=[["Newswire: stake to 100%, Oct 2019", STAKE19], ["Retail Banker International: 90% stake, May 2016", STAKE16]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & operations", "blurb": "Kiosks, 99.81% STP.", "div": "aba", "rev": "pay", "products": [
            P("tech", "Core operations & payments processing", "Card-issuing kiosks built with Compass Plus (2022), a 99.81% straight-through rate on USD MT103 payments (J.P. Morgan award, six years running), and more than 100 million ABA Mobile transactions a month (2024).",
              s=["con", "corp"], o="P", at="Compass Plus, J.P. Morgan", neo=[0, ""], src=[["CIR: J.P. Morgan STP award, Jan 2026", JPM], ["CIR: ABA 2024 results, Apr 2025", FY24], ["FinTech Global: card kiosks, Nov 2022", KIOSK]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & capital", "blurb": "Toward a universal bank.", "div": "aba", "rev": "corp", "products": [
            P("strategy", "Universal bank & financial ecosystem", "The aim is to combine retail leadership with corporate and investment banking, and to build \"a fully integrated financial ecosystem\" with insurance inside ABA Mobile. No numeric targets are published ⚠.",
              s=["corp", "con"], st="new", neo=[0, ""], src=[["CIR: Leader Talks, Huot Chanthida, Jul 2026", CIB], ["CIR: ABA and Etiqa, Jul 2026", ETIQA]]),
            P("capital", "Capital injection", "A US$220 million injection approved by the central bank in September 2024 lifted registered capital to US$1.32 billion; US$96 million of subordinated debt was repaid in 2024.",
              s=["corp"], ay="Sep 2024", neo=[0, ""], src=[["CIR: ABA 2024 results, Apr 2025", FY24]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Visa debit and credit (18 Visa leadership awards for 2024–25), Mastercard debit, prepaid and virtual cards, instant card machines, ABA PAY on the KHQR and Bakong rails, card-to-card and SWIFT transfers, and the country's biggest acceptance network through POS and PayWay.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit & prepaid", "blurb": "Visa, Mastercard, UnionPay.", "div": "aba", "rev": "pay", "products": [
            P("visadebit", "Visa debit", "Visa debit for mass and affluent customers, including the VannDa Visa Limited Edition debit card. Visa named ABA leader in spend per active Visa debit card in the affluent segment for 2024 and 2025.", short="Visa debit",
              s=["con", "aff"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["CIR: ten Visa awards, Mar 2026", VISA25], ["CIR: eight Visa awards, Feb 2025", VISA24]]),
            P("mcdebit", "Mastercard debit & prepaid", "Mastercard debit cards ordered in ABA Mobile or printed at a Card Machine. ABA won three Mastercard awards for 2023, for prepaid, debit and cross-border volume ⚠, and more at Mastercard's 2024 Cambodia customer event ⚠.", short="Mastercard debit",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard debit and prepaid."],
              mc="Mastercard's main card franchise at Cambodia's largest bank.",
              src=[["ABA: three Mastercard awards ⚠", MCAWARDS], ["ABA: cards in ABA Mobile ⚠", VIRTUAL], ["FinTech Global: card kiosks, Nov 2022", KIOSK]]),
            P("upi", "UnionPay & CSS cards", "UnionPay International cards since May 2015 ⚠, and local Cambodian Shared Switch (CSS) cards issued from the same kiosks.", short="UnionPay & CSS",
              s=["con"], lc="everyday", ay="May 2015", o="P", at="UnionPay, CSS", neo=[0, "UnionPay and the domestic switch."], src=[["ABA: UnionPay cards ⚠", UPI15], ["FinTech Global: card kiosks, Nov 2022", KIOSK]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Affluent credit on Visa.", "div": "aba", "rev": "pay", "products": [
            P("visacredit", "Visa credit", "Credit cards for affluent customers, where Visa named ABA leader in spend per active card for 2025. No ABA Mastercard credit card or rewards programme was found ⚠.", short="Credit (Visa)",
              s=["aff"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="Canadia Bank is launching a Mastercard World credit card (September 2026); ABA's affluent credit is Visa's.",
              src=[["CIR: ten Visa awards, Mar 2026", VISA25], ["CIR: Canadia Mastercard World preview, Sep 2026", CANADIA]]),
        ]},
        {"id": "2.3", "ic": "rocket", "name": "Instant & virtual cards", "blurb": "A card in two minutes.", "div": "mobile", "rev": "pay", "products": [
            P("kiosk", "Card Machines", "Cambodia's first instant card-issuing kiosks (November 2022, Compass Plus): Visa, Mastercard, UnionPay and CSS debit cards in under two minutes; 90 machines in 80+ branches and 191,000 cards issued at launch.",
              s=["con"], lc="open", ay="Nov 2022", o="P", at="Compass Plus", neo=[1, "Issues Visa, Mastercard, UnionPay and CSS."], src=[["FinTech Global: card kiosks, Nov 2022", KIOSK], ["CIR: ABA 2022 results, Jul 2023", FY22]]),
            P("virtual", "Virtual cards in ABA Mobile", "Instant Account holders can issue a free virtual Mastercard or Visa card in the app, linked to a USD account with a daily limit ⚠.",
              s=["con"], lc="everyday", o="B", neo=[1, "Visa or Mastercard, the customer's choice ⚠."], src=[["ABA: cards in ABA Mobile ⚠", VIRTUAL]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "ABA PAY & KHQR", "blurb": "QR on the Bakong rails.", "div": "abapay", "rev": "pay", "products": [
            P("abapay", "ABA PAY", "ABA's QR payment system. KHQR was fully enabled in March 2022, opening 150,000+ ABA merchants to every Bakong-member app ⚠. ABA is number one in Cambodia by KHQR payments and acceptance points.", short="ABA PAY (QR)",
              s=["con", "mer"], lc="move", ay="Mar 2022", o="B", neo=[0, "KHQR."],
              mc="QR, not cards, carries most everyday payments.",
              src=[["ABA: KHQR in ABA PAY ⚠", KHQR22], ["CIR: eight Visa awards, Feb 2025", VISA24]]),
            P("khqr", "KHQR & Bakong", "The central bank's EMV-based \"one QR for all\" and its blockchain payment system (launched 28 October 2020). In 2025 Bakong handled 1.33 billion transactions worth about 4.5 times GDP (58.2% in riel), and KHQR about US$105.6 billion at about 4.5 million merchants.", short="KHQR & Bakong",
              s=["con", "mer"], lc="move", o="P", at="National Bank of Cambodia", neo=[0, "Domestic real-time rail."], src=[["CIR: Bakong 2025, Oct 2026", BAKONG], ["CIR: KHQR US$105bn, Jun 2026", KHQRDATA], ["Bakong", BAKONGSITE]]),
        ]},
        {"id": "2.5", "ic": "send", "name": "Transfers", "blurb": "Card-to-card and SWIFT.", "div": "mobile", "rev": "pay", "products": [
            P("c2c", "Card-to-card transfers", "Instant card-to-card transfers with Mastercard and UnionPay cards in ABA Mobile, up to US$20,000 a month ⚠ (launch date unknown).",
              s=["con"], lc="move", o="P", at="Mastercard, UnionPay", neo=[1, "Mastercard and UnionPay ⚠."], src=[["ABA: history ⚠", HISTORY]]),
            P("swift", "International transfers", "USD clearing and remittances with a 99.81% straight-through rate (J.P. Morgan award for 2024); Bakong's cross-border value rose 235% in 2025.",
              s=["con", "corp"], lc="move", o="P", at="J.P. Morgan", neo=[0, "SWIFT."],
              mc="Nearly a million migrant workers came home in 2026; remittance corridors are open ground.",
              src=[["CIR: J.P. Morgan STP award, Jan 2026", JPM], ["CIR: banking sector 2025, Apr 2026", SECTOR], ["CIR: IMF outlook, Sep 2026", IMF]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acceptance", "blurb": "Most POS and QR points.", "div": "payway", "rev": "pay", "products": [
            P("pos", "POS & card acquiring", "Number one in Cambodia by card payment volume and acceptance points; ABA POS terminals and ATMs take Visa, Mastercard, UnionPay, JCB and CSS ⚠.",
              s=["mer", "sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["CIR: eight Visa awards, Feb 2025", VISA24], ["ABA: ATM network ⚠", ATMS]]),
            P("payway", "ABA PayWay & PayWay Plus", "Online and in-store gateway taking ABA PAY, KHQR, Visa, Mastercard, UPI, JCB, Alipay and WeChat. PayWay Plus is powered by Visa's CyberSource. It was the first Cambodian gateway on Shopify (October 2025).", short="PayWay",
              s=["mer", "sme", "pub"], lc="move", o="P", at="Visa CyberSource, Shopify", neo=[1, "Takes Mastercard; built on Visa CyberSource."],
              mc="Gateway risk and tokenisation sit with Visa's CyberSource today.",
              src=[["CIR: ABA and Grab, Nov 2024", GRAB], ["CIR: PayWay on Shopify, Oct 2025", SHOPIFY]]),
            P("grab", "Grab payments", "Grab users link their ABA account for automatic Account-on-File payments, and PayWay Plus processes all Grab card payments in Cambodia: Visa, Mastercard and UPI (November 2024).",
              s=["con", "mer"], lc="move", ay="Nov 2024", o="P", at="Grab", neo=[1, "Cards include Mastercard."], src=[["CIR: ABA and Grab, Nov 2024", GRAB]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: live face checks and verifiable documents, the Navi AI assistant and the country's first in-app spending analytics, tools for QR merchants, and insurance and faith-aligned banking inside ABA Mobile.",
    "tiles": [
        {"id": "3.1", "ic": "fingerprint", "name": "Security & identity", "blurb": "FacePass, verified documents.", "div": "mobile", "rev": "retail", "products": [
            P("facepass", "FacePass Secure", "Cambodia's first live facial recognition for banking, guarding high-value payments and account changes in ABA Mobile.",
              s=["con", "aff"], lc="everyday", o="B", neo=[0, "ABA's own."],
              mc="Visa refreshed its Cambodia security roadmap (June 2026) to move banks off SMS one-time passwords.",
              src=[["CIR: Financial Innovation of the Year, Nov 2025", INNOV], ["CIR: Visa security roadmap, Jun 2026", VISASEC]]),
            P("docverify", "Document Verification", "Statements and deposit certificates carry a QR code that embassies and auditors can check in the app or at verify.ababank.com (September 2026).",
              s=["con", "pub"], lc="beyond", st="new", ay="Sep 2026", o="B", neo=[0, ""], src=[["CIR: Document Verification, Sep 2026", DOCV]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & insights", "blurb": "Navi and Analytics.", "div": "mobile", "rev": "retail", "products": [
            P("navi", "Navi assistant", "Cambodia's first AI virtual banking assistant, multilingual and inside ABA Mobile.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["CIR: Financial Innovation of the Year, Nov 2025", INNOV]]),
            P("analytics", "Analytics", "The country's first in-app personal finance tool (August 2025): income and spending sorted by category, with trends by week, month or year.",
              s=["con", "sme"], lc="grow", ay="Aug 2025", o="B", neo=[0, ""],
              mc="Merchant-data enrichment could sharpen categories.",
              src=[["CIR: Analytics launch, Aug 2025", PFM]]),
        ]},
        {"id": "3.3", "ic": "receipt-text", "name": "Merchant tools", "blurb": "PaySound, QR API.", "div": "payway", "rev": "pay", "products": [
            P("paysound", "PaySound", "Spoken alerts for each incoming payment, in Khmer, English or Chinese, on ABA Mobile, the ABA Merchant app and ABA POS (June 2026).",
              s=["mer"], lc="move", st="new", ay="Jun 2026", o="B", neo=[0, ""], src=[["CIR: PaySound, Jun 2026", PAYSOUND]]),
            P("qrapi", "QR API & partner integrations", "Dynamic KHQR codes on POS screens, receipts and kiosks through T-O Group (September 2025), extended to its QR Menu ordering (May 2026).",
              s=["mer", "sme"], lc="move", o="P", at="T-O Group", neo=[0, "KHQR."], src=[["CIR: ABA and T-O Group, Sep 2025", TOG], ["CIR: T-O Group QR Menu, May 2026", TOG26]]),
        ]},
        {"id": "3.4", "ic": "hand-coins", "name": "Insurance & inclusion", "blurb": "Etiqa, Interest-Free Mode.", "div": "mobile", "rev": "retail", "products": [
            P("etiqa", "Insurance with Etiqa", "Fire insurance first, then motor and travel cover sold and claimed inside ABA Mobile, with Etiqa General Insurance Cambodia, part of Maybank (July 2026).",
              s=["con", "aff"], lc="beyond", st="new", ay="Jul 2026", o="P", at="Etiqa", neo=[0, ""],
              mc="Travel cover is a natural pairing with premium travel cards.",
              src=[["CIR: ABA and Etiqa, Jul 2026", ETIQA]]),
            P("interestfree", "Interest-Free Mode & Hajj Fund", "An app setting that turns savings interest-free, with the interest going to charity, and ABA as the exclusive gateway for CATA's Hajj Fund via KHQR or card (April 2026).",
              s=["con", "pub"], lc="grow", st="new", ay="Apr 2026", o="P", at="CATA", neo=[0, ""], src=[["CIR: ABA and CATA, Apr 2026", CATA]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: nearly US$13 billion of deposits, US$9.6 billion of retail, SME and corporate loans, corporate and investment banking with Cambodia's first green and agriculture bonds, and ABA Business for companies.",
    "tiles": [
        {"id": "4.1", "ic": "coins", "name": "Deposits & savings", "blurb": "About a fifth of the market.", "div": "aba", "rev": "retail", "products": [
            P("deposits", "Accounts & deposits", "Nearly US$13 billion of customer deposits at end-2025 (+17%); in the quarter to July 2026 average deposits grew 7% at constant currency. Accounts can be opened in the app.",
              s=["con", "aff"], lc="everyday", neo=[0, ""], src=[["CIR: ABA 2025 results, Apr 2026", FY25], ["National Bank of Canada: Q3 2026 presentation", NBCQ3P]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Retail & SME lending", "blurb": "US$9.6bn of loans.", "div": "aba", "rev": "sme", "products": [
            P("loans", "Retail & SME loans", "Gross loans of US$9.6 billion (+11%) and nearly US$1 billion of new lending in 2025, against a system bad-loan ratio of 8.3%; ABA's impaired formations rose in 2026.",
              s=["con", "sme"], lc="borrow", neo=[0, ""], src=[["CIR: ABA 2025 results, Apr 2026", FY25], ["National Bank of Canada: Q3 2026 presentation", NBCQ3P], ["CIR: banking sector 2025, Apr 2026", SECTOR]]),
            P("smeloan", "Targeted SME finance", "Low-rate finance for EV-charger roll-out with Charge+ (January 2025), with charging top-ups through PayWay and KHQR.",
              s=["sme"], lc="borrow", ay="Jan 2025", o="P", at="Charge+", neo=[0, ""], src=[["CIR: ABA and Charge+, Jan 2025", CHARGE]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate & investment", "blurb": "First green and agri bonds.", "div": "aba", "rev": "corp", "products": [
            P("cib", "Corporate & investment banking", "Corporate lending, trade and supply-chain finance, cash management, escrow and project finance (SchneiTec solar); Asian Banking & Finance Corporate & Investment Bank of the Year 2026.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["CIR: Leader Talks, Huot Chanthida, Jul 2026", CIB]]),
            P("bonds", "Bond investments", "The largest investor in Cambodia's first green project bond (a 60MW solar plant) and its first agriculture bond (Daun Penh Agrico, January 2026).",
              s=["corp"], lc="grow", ay="Jan 2026", neo=[0, ""], src=[["CIR: agriculture bond, Jan 2026", AGRI], ["CIR: ABA 2025 results, Apr 2026", FY25]]),
        ]},
        {"id": "4.4", "ic": "briefcase-business", "name": "ABA Business", "blurb": "Volumes up 46%.", "div": "business", "rev": "corp", "products": [
            P("ababusiness", "ABA Business", "Digital banking for companies: payroll, bulk and scheduled payments, tax, virtual accounts, ERP host-to-host links and a mobile approval app (2025). Transactions rose 46% and customers 25% in 2025; named Best Online Corporate Bank – Cambodia 2026.",
              s=["sme", "corp"], lc="move", o="B", neo=[0, ""],
              mc="No commercial-card programme was found; virtual and corporate cards are open ground.",
              src=[["CIR: Best Online Corporate Bank, Oct 2026", ONLINECORP]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach ABA: ABA Mobile for more than 6 million users, 104 branches and 1,900+ self-banking machines, the merchant app and POS, and partner platforms from Grab to government portals.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "ABA Mobile", "blurb": "6m+ users.", "div": "mobile", "rev": "retail", "products": [
            P("app", "ABA Mobile", "The core of the retail strategy: more than 6 million users, account opening, cards, QR payments, insurance and analytics in one app.",
              s=["con", "aff"], lc="everyday", o="B", neo=[0, "ABA's own; its virtual cards sit under Rails."], src=[["CIR: Best Retail Bank, Jun 2026", RETAIL]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & self-banking", "blurb": "104 branches, 1,900+ machines.", "div": "aba", "rev": "retail", "products": [
            P("branches", "Branches", "104 branches at end-2025 (105 by January 2026), up from 35 in 2016, still expanding into the provinces.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["CIR: ABA 2025 results, Apr 2026", FY25], ["CIR: agriculture bond, Jan 2026", AGRI]]),
            P("selfbank", "ABA 24/7 self-banking", "46 self-banking spots and more than 1,900 machines (ATMs, cash-in machines and Card Machines).",
              s=["con"], lc="everyday", neo=[1, "ATMs take Mastercard; kiosks issue it."], src=[["CIR: agriculture bond, Jan 2026", AGRI], ["ABA: ATM network ⚠", ATMS]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "Merchant app & POS", "blurb": "Where sellers see payments.", "div": "payway", "rev": "pay", "products": [
            P("merchantapp", "ABA Merchant app & ABA POS", "Sellers watch incoming QR and card payments, hear them through PaySound, and reconcile in real time.",
              s=["mer"], lc="move", o="B", neo=[0, ""], src=[["CIR: PaySound, Jun 2026", PAYSOUND]]),
        ]},
        {"id": "5.4", "ic": "plug", "name": "Partners & platforms", "blurb": "Grab, Shopify, ministries.", "div": "payway", "rev": "pay", "products": [
            P("partners", "Partner & public platforms", "PayWay sits inside Grab, Shopify, T-O Group's POS, Charge+, the Ministry of Interior's NGO-registration portal (April 2026) and CATA's Hajj Fund.",
              s=["mer", "pub"], lc="open", o="P", at="Grab, Shopify, Ministry of Interior", neo=[0, ""], src=[["CIR: Ministry of Interior, Apr 2026", MOI], ["CIR: PayWay on Shopify, Oct 2025", SHOPIFY]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at ABA", "blurb": "Debit and transfers; Visa leads.", "products": [
        P("mcataba", "Mastercard at ABA", "ABA issues Mastercard debit, prepaid and virtual cards, offers card-to-card transfers with Mastercard and accepts it everywhere, and won Mastercard awards for 2023 and 2024 ⚠. Visa is the more visible partner: 18 leadership awards for 2024–25, affluent debit and credit, and CyberSource behind PayWay Plus. Most everyday payments run on KHQR.",
          s=["con"], div="aba", rev="pay", mc="The relationship this map is drawn for.",
          src=[["ABA: three Mastercard awards ⚠", MCAWARDS], ["CIR: ten Visa awards, Mar 2026", VISA25]]),
    ]},
    {"id": "pillar-market", "name": "Cambodian banking", "blurb": "QR, bad loans, de-dollarisation.", "products": [
        P("market", "The Cambodian market", "A US$100 billion banking system with bad loans at 8.3%, Bakong and KHQR at national scale, cross-border QR with eight economies (India in June 2026, China's Weixin Pay in August 2026), a push for the riel, Chief Bank under administration (September 2026) and growth slowing to about 3%.",
          s=["con"], div="aba", rev="retail", src=[["CIR: banking sector 2025, Apr 2026", SECTOR], ["CIR: Bakong 2025, Oct 2026", BAKONG], ["CIR: IMF outlook, Sep 2026", IMF]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
