"""Nabil Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the Q4 FY2025/26 interim report and the audited
FY2025/26 extract (year to 16 July 2026), and the 2024/25 annual report. Amounts are Nepalese rupees (NPR).
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q4 = "https://assets.nabilbank.com/uploads/Finance/Interim%20Financial/interim-financial-report-q4-fy-2025-26-nabil-bank-71d27cb6.pdf"
AR26 = "https://assets.nabilbank.com/uploads/Finance/2082-2083/annual-report-2025-26-extract-english-82e1dc1e.pdf"
AR25 = "https://assets.nabilbank.com/uploads/Finance/Annual%20Report%202024-25%20(English).pdf"
MGMT = "https://www.nabilbank.com/management-team"
BOARD = "https://www.nabilbank.com/board-of-directors"
CHAIR = "https://www.sharesansar.com/newsdetail/nabil-bank-approves-1250-cash-dividend-elects-new-chairman-2026-01-13"
AGM42 = "https://www.sharesansar.com/newsdetail/nabil-bank-limited-approves-1580-dividend-at-42nd-agm-2026-10-09"
RANK = "https://www.sharesansar.com/newsdetail/nepals-commercial-banks-net-profit-surges-3233-to-npr-6978-arba-in-q4-208283-nabil-bank-leads-2026-08-17"
UF = "https://www.sharesansar.com/newsdetail/nabil-bank-to-commence-joint-operation-from-ashar-27-after-acquisiton-of-united-finance-2021-07-05"
WIKI = "https://en.wikipedia.org/wiki/Nabil_Bank"
DEBIT = "https://www.nabilbank.com/services-payments/services/debit-card/nabil-smart-debit-card"
VISAINTL = "https://www.nabilbank.com/services-payments/services/debit-card/nabil-visa-international-debit-card"
MCDEBIT = "https://www.sharesansar.com/newsdetail/nabil-bank-launches-new-mastercard-debit-card-with-exclusive-benefits-2025-11-16"
CCMC = "https://www.nabilbank.com/services-payments/services/credit-card/nabil-mastercard--domestic-credit-card"
CCVISA = "https://www.nabilbank.com/services-payments/services/credit-card/nabil-visa--domestic-credit-card"
FDCARD = "https://www.nabilbank.com/services-payments/services/card/nabil-fd-card"
PREPAID = "https://www.nabilbank.com/services-payments/services/prepaid-card-travel-card"
ICARD = "https://www.nabilbank.com/services-payments/services/prepaid-card-travel-card/nabil-icard"
ICARDNEWS = "https://www.sharesansar.com/newsdetail/nabil-bank-launches-us-dollar-nabil-icard-now-customers-can-pay-in-rupees-for-transactions-in-dollars-from-nepal-2021-03-24"
VISAAWARDS = "https://www.sharesansar.com/newsdetail/nabil-bank-wins-three-prestigious-visa-international-awards-2025-11-30"
QR = "https://www.nabilbank.com/services-payments/services/merchant-acquiring/nabil-qr-code"
KOILI = "https://www.nabilbank.com/services-payments/services/merchant-acquiring/instant-voice-notification-device-(ipn-koili)"
ATMS2016 = "https://thehimalayantimes.com/ampArticle/173668"
EPG = "https://www.nabilbank.com/services-payments/services/merchant-acquiring/nabil-electronic-payment-gateway-epg"
BUSDIG = "https://www.nabilbank.com/services-payments/services/business"
NCHL = "https://nchl.com.np/wp-content/uploads/2026/08/Newsletter_NCHL-Connect_-Vol-2_Issue-I_15-August-2026.pdf"
NRB = "https://www.nrb.org.np/psd/payment-systems-oversight-report-2081-82-2024-2025/"
NREMIT = "https://www.nabilbank.com/services-payments/services/other-services/nremit"
HAMRO = "https://www.sharesansar.com/newsdetail/nabil-bank-and-smart-ideas-pvt-ltd-join-forces-for-card-based-remittance-services-2024-10-08"
VISADIRECT = "https://www.sharesansar.com/newsdetail/nabil-launches-visa-direct-service-now-send-easy-remittance-from-180-countries-directly-to-nabil-accounts-linked-to-visa-cards-2022-09-16"
NEPALNOW = "https://www.nabilbank.com/services-payments/services/other-services/nepal-now"
ESECURE = "https://www.nabilbank.com/services-payments/services/card/nabil-e-secure"
VIDEOKYC = "https://www.nabilbank.com/product/video-kyc"
QATAR = "https://thehimalayantimes.com/business/nabil-bank-ties-up-with-qatar-airways"
INSTAL = "https://www.nabilbank.com/services-payments/services/card/nabil-installment"
APPLE = "https://www.nabilbank.com/individual/products/AppleBNPL"
INDIVIDUAL = "https://www.nabilbank.com/individual"
FONELOAN = "https://www.nabilbank.com/services-payments/services/individuals/nabil-foneloan"
NBANK = "https://www.nabilbank.com/services-payments/services/individuals/nbank"
PLAY = "https://play.google.com/store/apps/details?id=com.f1soft.nabilmbank"
KHALTI = "https://www.sharesansar.com/newsdetail/khalti-wallet-users-can-now-withdraw-cash-from-nabil-bank-atms-2026-01-04"
NAMASTE = "https://www.sharesansar.com/newsdetail/nabil-bank-partners-with-namaste-pay-wallet-to-enhance-digital-services-2024-08-07"
FPCC = "https://www.sharesansar.com/newsdetail/fonepay-credit-card-crosses-50000-users-with-support-from-nine-partner-banks-2026-08-12"
FPUPI = "https://www.sharesansar.com/newsdetail/fonepay-integrates-unionpay-international-into-nepals-qr-payment-network-2026-05-29"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: NPR 735 billion of assets and the most profit of any Nepali bank, promoters led by NB International and IFIC Bank, a joint venture from 1984 grown by two mergers, Finacle and early AI, and a trillion-rupee ambition.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "NPR 7.9bn profit, top in Nepal.", "div": "nabil", "rev": "fi", "products": [
            P("balance", "Balance sheet & earnings", "Total assets NPR 734.7 billion, customer loans NPR 460.3 billion and customer deposits NPR 592.1 billion at 16 July 2026; profit NPR 7.91 billion in FY2025/26 (up 33%), the highest of Nepal's commercial banks; capital 12.37% of RWA, gross NPL 4.20%, ROE 11.8%. About 2.5 million customers.",
              s=["con"], neo=[0, ""], src=[["Q4 FY2025/26 report", Q4], ["FY2025/26 audited extract", AR26], ["ShareSansar: sector profits, Aug 2026", RANK], ["ShareSansar: Visa awards, Nov 2025", VISAAWARDS]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Owners & leadership", "blurb": "Chaudhary chair, Gyawali CEO.", "div": "nabil", "rev": "fi", "products": [
            P("owners", "Ownership & listing", "Listed on NEPSE; promoters hold 58.44%: NB (International) Ltd, Ireland 39.44% (linked to the Chaudhary Group ⚠), IFIC Bank, Bangladesh 7.77% and Rastriya Beema 7.63%; foreign ownership 47.65%. Market value about NPR 145 billion ⚠ at the July 2026 close of NPR 534.90; ICRA Nepal issuer rating A@ ⚠, down from AA- in 2022/23.",
              s=["inv"], neo=[0, ""], src=[["Annual report 2024/25", AR25], ["Q4 FY2025/26 report", Q4]]),
            P("leadership", "Board & management", "Chairman Nirvana Kumar Chaudhary (from January 2026), CEO Manoj Kumar Gyawali, deputy CEOs Bhupendra Pandey (lending), Adarsha Bazgain (investment and liabilities) and Ganesh Prasad Awasthi (tech, operations and recovery), and Chief Digital Banking Officer Parmeswor Shrestha.",
              s=["inv"], st="new", ay="Jan 2026", neo=[0, ""], src=[["Nabil: management team", MGMT], ["Nabil: board of directors", BOARD], ["ShareSansar: new chairman, Jan 2026", CHAIR]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & deals", "blurb": "Since 1984; two mergers.", "div": "nabil", "rev": "fi", "products": [
            P("heritage", "Nepal Arab Bank to Nabil", "Founded on 12 July 1984 as Nepal Arab Bank, the country's first joint-venture bank with mainly foreign investors (Dubai Bank held 50%), renamed Nabil around 2001 ⚠; SWIFT, its first ATM and Western Union in the 1990s.",
              s=["con"], o="I", neo=[0, ""], src=[["Annual report 2024/25", AR25], ["Wikipedia: Nabil Bank", WIKI]]),
            P("deals", "Mergers", "United Finance acquired in 2021 (35 Nabil shares per 100) and Nepal Bangladesh Bank in July 2022, which brought IFIC Bank in as a promoter.",
              s=["con", "sme"], o="A", ay="2021–22", neo=[0, ""], src=[["ShareSansar: United Finance, Jul 2021", UF], ["Wikipedia: Nabil Bank", WIKI]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Finacle, RPA, gen-AI.", "div": "nabil", "rev": "cards", "products": [
            P("tech", "Core, automation & AI", "Infosys Finacle core banking; robotic process automation, APIs and process re-engineering; AI/ML anti-money-laundering models, generative-AI virtual assistants and the chatbot Nabina; PCI DSS; a full AI strategy promised within two years.",
              s=["corp"], neo=[0, "Nabil's own."], src=[["Annual report 2024/25", AR25]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & capital", "blurb": "Towards a trillion rupees.", "div": "nabil", "rev": "treasury", "products": [
            P("strategy", "Strategy & capital", "Aims to be 'Nepal's most trusted and future-ready bank' and a trillion-rupee institution; NPR 5 billion of 8% perpetual preference shares, the first such issue approved for a Nepali bank; 15.8% dividend for FY2025/26 (5% bonus, 10.8% cash) approved in October 2026.",
              s=["inv"], st="new", neo=[0, ""], src=[["Annual report 2024/25", AR25], ["Q4 FY2025/26 report", Q4], ["ShareSansar: 42nd AGM, Oct 2026", AGM42]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: debit on Visa and, since 2025, Mastercard; domestic credit on both; Visa prepaid and USD cards; QR on Fonepay and a gateway that takes Visa, Mastercard and UnionPay; connectIPS and NCHL's rails; and remittances, half of them card-funded.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "Visa, and Mastercard since 2025.", "div": "nabil", "rev": "cards", "products": [
            P("debitvisa", "Smart Debit & international debit (Visa)", "Smart Debit cards for Nepal, India and Bhutan, contactless up to NPR 5,000, and a foreign-currency Visa debit card valid everywhere except India. Visa named Nabil a principal client for consumer debit and contactless issuing in November 2025.", short="Debit (Visa)",
              s=["con", "nrn"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Nabil: Smart Debit Card", DEBIT], ["Nabil: Visa international debit", VISAINTL], ["ShareSansar: Visa awards, Nov 2025", VISAAWARDS]]),
            P("debitmc", "Mastercard debit", "Customers can choose Mastercard in the Smart Debit range (valid five years); a Danphe-design Mastercard debit card with dining, spa and gym discounts was launched on 16 November 2025 with Mastercard's Ravi Datla ⚠ and CEO Manoj Kumar Gyawali.", short="Debit (Mastercard)",
              s=["con"], lc="everyday", st="new", ay="Nov 2025", o="P", at="Mastercard", neo=[2, "Mastercard debit."],
              mc="Mastercard's newest foothold: debit choice inside Nepal's most profitable bank.",
              src=[["ShareSansar: Mastercard debit, Nov 2025", MCDEBIT], ["Nabil: Smart Debit Card", DEBIT], ["Annual report 2024/25", AR25]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Visa and Mastercard, NPR 1.5bn.", "div": "nabil", "rev": "cards", "products": [
            P("creditvisa", "Visa Domestic credit card", "Contactless domestic credit card for Nepal, India and Bhutan, repaying 10–100% a month, with instalments; part of a small credit-card book of NPR 1.53 billion (July 2026).", short="Credit (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Nabil: Visa domestic credit card", CCVISA], ["FY2025/26 audited extract", AR26]]),
            P("creditmc", "Mastercard Domestic credit card", "The same contactless domestic credit card on Mastercard, with Nabil Installment and supplementary cards.", short="Credit (Mastercard)",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard credit."],
              mc="Fonepay's QR credit card reached 50,000 users in two years; card credit needs a sharper offer.",
              src=[["Nabil: Mastercard domestic credit card", CCMC], ["ShareSansar: Fonepay Credit Card, Aug 2026", FPCC]]),
            P("fdcard", "Nabil FD Card", "A credit card secured on a fixed deposit, earning deposit interest, 'through Wide VISA Network'.",
              s=["con", "inv"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Nabil: FD Card", FDCARD]]),
        ]},
        {"id": "2.3", "ic": "plane", "name": "Prepaid & USD cards", "blurb": "Travel cards and iCard, Visa.", "div": "nabil", "rev": "cards", "products": [
            P("prepaid", "Prepaid travel cards", "Visa Domestic and Visa International prepaid cards for trips, reloadable into NPR accounts from nBank.",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Nabil: prepaid cards", PREPAID], ["Annual report 2024/25", AR25]]),
            P("icard", "Nabil iCard", "A USD Visa card for international online shopping, up to USD 500 a year under NRB limits, issued over the counter or as a virtual card in nBank (launched March 2021).",
              s=["con"], lc="everyday", ay="Mar 2021", o="P", at="Visa", neo=[0, "Visa."], src=[["Nabil: iCard", ICARD], ["ShareSansar: iCard, Mar 2021", ICARDNEWS]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Merchant acquiring", "blurb": "Fonepay QR, POS, gateway.", "div": "nabil", "rev": "cards", "products": [
            P("qr", "Nabil QR", "Merchant QR on the Fonepay network, with 43,600+ QR terminals (FY2024/25) and Koili voice-alert speakers in five languages; QR is Nepal's most-used retail payment, NPR 958 billion in FY2024/25.",
              s=["sme"], lc="move", o="P", at="Fonepay", neo=[0, "Fonepay QR."], src=[["Nabil: QR", QR], ["Nabil: Koili device", KOILI], ["Annual report 2024/25", AR25], ["NRB: oversight report 2024/25", NRB]]),
            P("pos", "POS terminals & ATMs acceptance", "Card terminals for merchants; Nabil ATMs take Visa, Mastercard, UnionPay and SCT cards (2016) ⚠ current list unconfirmed.",
              s=["sme", "tour"], lc="move", neo=[1, "Accepts every network."], src=[["Himalayan Times: Nabil ATMs, 2016", ATMS2016], ["Annual report 2024/25", AR25]]),
            P("epg", "Electronic Payment Gateway", "E-commerce acquiring for Visa, Mastercard and UnionPay cards with 3-D Secure and rule-based fraud screening; UnionPay 3DS added in FY2024/25. Visa named Nabil a principal client for e-commerce acquiring (November 2025).", short="EPG (all networks)",
              s=["sme", "tour"], lc="move", o="P", at="Visa, Mastercard, UnionPay", neo=[1, "Takes Mastercard with Visa and UnionPay."],
              src=[["Nabil: EPG", EPG], ["Annual report 2024/25", AR25], ["ShareSansar: Visa awards, Nov 2025", VISAAWARDS]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Real-time & national rails", "blurb": "connectIPS, NEPALPAY.", "div": "nabil", "rev": "fi", "products": [
            P("a2a", "connectIPS, IPS & corporatePAY", "Nabil holds shares in Nepal Clearing House and runs its rails: connectIPS, interbank transfers and corporatePAY bulk payments. NCHL handled 238 million transactions worth about NPR 21 trillion in FY2025/26 and NEPALPAY QR 36 million (up 56%).",
              s=["con", "corp"], lc="move", o="P", at="NCHL", neo=[0, "National rails."],
              mc="Account-to-account rails now carry most of Nepal's digital value.",
              src=[["NCHL newsletter, Aug 2026", NCHL], ["Annual report 2024/25", AR25], ["Nabil: business digital", BUSDIG]]),
            P("nepalpay", "NEPALPAY domestic card", "NCHL's domestic card scheme, operational since March 2025 with about 2,000 cards; peers have signed as members, but no public sign Nabil has joined ⚠.",
              s=["con"], lc="everyday", st="unconf", neo=[0, "Domestic scheme."], src=[["NCHL newsletter, Aug 2026", NCHL], ["NRB: oversight report 2024/25", NRB]]),
        ]},
        {"id": "2.6", "ic": "earth", "name": "Remittance & cross-border", "blurb": "Nabil Remit, nRemit, Visa Direct.", "div": "remit", "rev": "fi", "products": [
            P("remit", "Nabil Remit", "Inward remittance since 2006 through Western Union and partners in Qatar, the UAE, India, Korea, Japan, Australia and Hong Kong, paid into accounts and wallets or in cash at 20,000 points; outward through Convera and SWIFT.",
              s=["nrn"], lc="move", o="P", at="Western Union and others", neo=[0, ""], src=[["Annual report 2024/25", AR25]]),
            P("nremit", "nRemit", "Send USD 100–5,000 from abroad with any international Mastercard or Visa card into any Nepali bank account in real time, through Nabil's gateway, in nBank and white-labelled in the Hamro Patro app (October 2024).",
              s=["nrn"], lc="move", ay="Oct 2024", o="P", at="Hamro Patro", neo=[1, "Funded by Mastercard or Visa cards."],
              mc="Account-based remittance is next on Nabil's list; Mastercard Move could carry it.",
              src=[["Nabil: nRemit", NREMIT], ["ShareSansar: Hamro Patro, Oct 2024", HAMRO]]),
            P("visadirect", "Visa Direct", "Remittances pushed from 180+ countries to Nabil Visa cards (September 2022).",
              s=["nrn"], lc="move", ay="Sep 2022", o="P", at="Visa", neo=[0, "Visa."], src=[["ShareSansar: Visa Direct, Sep 2022", VISADIRECT]]),
            P("nepalnow", "Nepal Now", "A wallet for foreign tourists (other than Indians), loaded with foreign-issued cards and spent at Fonepay QR merchants ⚠ launch date not found.",
              s=["tour"], lc="move", st="new", o="P", at="Fonepay", neo=[1, "Loaded by any foreign card ⚠."],
              mc="Tourist spending on foreign cards meets domestic QR here.",
              src=[["Nabil: Nepal Now", NEPALNOW]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: 3-D Secure on Visa and Mastercard and an operations unit for disputes and chargebacks, AI and video KYC, open APIs and a marketplace, and instalments and offers for cardholders.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & disputes", "blurb": "3-D Secure, chargebacks.", "div": "nabil", "rev": "cards", "products": [
            P("esecure", "Nabil e-Secure", "One-time-password protection for online card payments, 'Powered by VerifiedBYVISA (VBV)/ MasterCardSecureCode'.",
              s=["con"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Mastercard SecureCode with Visa's."], src=[["Nabil: e-Secure", ESECURE]]),
            P("fraudops", "Digital Channel Operations", "Reconciles and settles card, QR and gateway transactions, manages disputes and chargebacks and monitors digital-payment risk under NRB, Visa and Mastercard rules; a new reconciliation system; AI/ML anti-money-laundering models. Cyber risk is a named challenge.",
              s=["con", "sme"], lc="everyday", neo=[0, "Nabil's own."],
              mc="NPR 929 million paid in Visa and Mastercard fees in FY2025/26; fraud and dispute tools could earn some of it back.",
              src=[["Annual report 2024/25", AR25], ["FY2025/26 audited extract", AR26], ["Q4 FY2025/26 report", Q4]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "AI, KYC & service", "blurb": "Video KYC, gen-AI.", "div": "nbank", "rev": "fi", "products": [
            P("videokyc", "Video KYC", "Accounts opened online round the clock by video call, with self-captured ID; used by Nepalis abroad; online KYC updates.",
              s=["con", "nrn"], lc="open", neo=[0, ""], src=[["Nabil: Video KYC", VIDEOKYC], ["Annual report 2024/25", AR25]]),
            P("ai", "AI assistants & automation", "Generative-AI virtual assistants, the Nabina chatbot, robotic process automation and appointment banking; Bankers Technology Award 2025.",
              s=["con"], lc="everyday", st="new", neo=[0, "Nabil's own."], src=[["Annual report 2024/25", AR25]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "Open APIs & marketplace", "blurb": "Embedded banking.", "div": "nbank", "rev": "cards", "products": [
            P("openapi", "Open API banking & Marketplace", "Host-to-host APIs into corporate ERP and billing systems, nRemit white-labelled for merchants, and an nBank marketplace (RhinoPass, Nimbuzz, travel bookings) ⚠ partners change.",
              s=["sme", "corp"], lc="beyond", st="new", neo=[0, ""], src=[["Annual report 2024/25", AR25]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Instalments & offers", "blurb": "0% iPhone EMI.", "div": "nabil", "rev": "cards", "products": [
            P("installment", "Nabil Installment & Apple BNPL", "EMI of NPR 20,000–200,000 for domestic Mastercard and Visa credit cardholders; 0% iPhone instalments over 3–12 months with 60% financed; HamroBNPL with HamroBazaar in nBank.",
              s=["con"], lc="borrow", st="new", neo=[1, "On Mastercard and Visa credit cards."], src=[["Nabil: Installment", INSTAL], ["Nabil: Apple BNPL", APPLE], ["Annual report 2024/25", AR25]]),
            P("offers", "Cardholder offers", "Discounts with e-commerce, appliance, hotel and restaurant merchants, and up to 10% off Qatar Airways fares (2022).",
              s=["con"], lc="grow", neo=[None, "Networks not stated."], src=[["Annual report 2024/25", AR25], ["Himalayan Times: Qatar Airways", QATAR]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: savings, remittance and home loans for 2.5 million people, instant digital loans, SME and microfinance credit, corporate, hydropower and trade finance, and treasury and capital-markets services.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Retail deposits & loans", "blurb": "8% of deposits.", "div": "nabil", "rev": "fi", "products": [
            P("deposits", "Savings & deposits", "Savings accounts for youth, women, seniors, workers, remitters and Nepalis abroad (NRN and USD accounts) and fixed deposits; deposit market share 8.15% (FY2024/25).",
              s=["con", "nrn", "inv"], lc="grow", neo=[0, ""], src=[["Nabil: individual products", INDIVIDUAL], ["Annual report 2024/25", AR25]]),
            P("homeloans", "Home, auto & gold loans", "Home loans (including women's Smart Nari Ghar Karja), auto, education and instant gold loans; loan market share 8.72% (FY2024/25).",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Nabil: individual products", INDIVIDUAL], ["Annual report 2024/25", AR25]]),
        ]},
        {"id": "4.2", "ic": "smartphone", "name": "Digital lending", "blurb": "FoneLoan in minutes.", "div": "nbank", "rev": "fi", "products": [
            P("foneloan", "Nabil FoneLoan", "Pre-approved, collateral-free micro-loans up to NPR 200,000 in the nBank app, scored on banking data.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Nabil: FoneLoan", FONELOAN]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "SME & microfinance", "blurb": "Small to mid-market.", "div": "nabil", "rev": "fi", "products": [
            P("sme", "SME & microfinance", "Small (up to NPR 10 million), medium and mid-market lending through an SME hub and every branch, and wholesale loans to microfinance institutions, including the 25%-owned NADEP Laghubitta.",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["Annual report 2024/25", AR25]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "Corporate, infra & trade", "blurb": "Hydropower and LCs.", "div": "nabil", "rev": "trade", "products": [
            P("corporate", "Corporate & infrastructure lending", "Project and infrastructure finance, with NPR 41 billion in energy and NPR 50 billion in agriculture (FY2024/25).",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Annual report 2024/25", AR25]]),
            P("trade", "Trade finance", "Letters of credit and guarantees, earning NPR 1.21 billion of commission in FY2025/26, and 150+ correspondent banks.",
              s=["corp"], lc="move", neo=[0, ""], src=[["FY2025/26 audited extract", AR26], ["Annual report 2024/25", AR25]]),
        ]},
        {"id": "4.5", "ic": "chart-candlestick", "name": "Treasury & capital markets", "blurb": "NPR 128bn invested.", "div": "invest", "rev": "treasury", "products": [
            P("treasury", "Treasury", "Investment securities of NPR 127.5 billion, FX and derivatives; treasury earned NPR 6.1 billion of revenue in FY2025/26.",
              s=["corp", "inv"], lc="grow", neo=[0, ""], src=[["FY2025/26 audited extract", AR26]]),
            P("invest", "Nabil Investment Banking & Stock Dealer", "Merchant banking, share registry and mutual funds (60%-owned Nabil Investment Banking) and broking and dealing (Nabil Stock Dealer).",
              s=["inv"], lc="grow", neo=[0, ""], src=[["Q4 FY2025/26 report", Q4], ["Annual report 2024/25", AR25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the nBank app for 1.8 million users, 268 branches and 323 ATMs, corporate portals, and agents, wallets and apps that carry Nabil's services.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "nBank app", "blurb": "1.8 million users.", "div": "nbank", "rev": "cards", "products": [
            P("app", "nBank", "Launched in December 2022: 1.83 million registered users and 75.8 million transactions worth NPR 499 billion in FY2024/25; accounts, loans, cards, QR, wallet loads and cardless cash; built on F1Soft's platform ⚠.",
              s=["con", "nrn"], lc="everyday", o="P", at="F1Soft ⚠", neo=[0, "Nabil's own."], src=[["Nabil: nBank", NBANK], ["Annual report 2024/25", AR25], ["Google Play: nBank", PLAY]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "268 branches, 323 ATMs.", "div": "nabil", "rev": "fi", "products": [
            P("branches", "Branches, ATMs & digital lounges", "268 branches, 21 extension counters and 321–323 ATMs, digital lounges with cash-deposit machines, appointment banking, and cardless cash for Khalti wallet users (January 2026).",
              s=["con", "tour"], lc="everyday", neo=[1, "ATMs take Mastercard ⚠."], src=[["Annual report 2024/25", AR25], ["ShareSansar: Khalti at Nabil ATMs, Jan 2026", KHALTI]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "Corporate portals", "blurb": "Corporate Net, corporatePAY.", "div": "nabil", "rev": "trade", "products": [
            P("corpdigital", "Corporate Net & corporatePAY", "Corporate internet banking hosted by Nabil, corporatePAY from NCHL for bulk and vendor payments, and a sole-proprietor version.",
              s=["corp", "sme"], lc="move", o="P", at="NCHL", neo=[0, ""],
              mc="No commercial card is offered; corporatePAY handles supplier payments.",
              src=[["Nabil: business digital", BUSDIG]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Agents, wallets & apps", "blurb": "Hamro Patro, Khalti, agents.", "div": "nabil", "rev": "fi", "products": [
            P("partners", "Agents, wallets & partner apps", "Branchless-banking agents in four provinces (eight agents, 337 accounts, mid-July 2025); wallets such as Namaste Pay, IME Pay and Hamro Pay loadable from nBank; nRemit inside Hamro Patro.",
              s=["con", "nrn"], lc="open", o="P", at="Wallets, Hamro Patro", neo=[0, ""], src=[["Annual report 2024/25", AR25], ["ShareSansar: Namaste Pay, Aug 2024", NAMASTE]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Nabil", "blurb": "Second to Visa, growing in debit.", "products": [
        P("mcatnabil", "Mastercard at Nabil", "Nabil has issued Visa and Mastercard since 1999–2004 and holds Mastercard Class B and Visa Class C shares from its days as a principal member of both. Visa leads: prepaid, USD, FD and international debit cards, Visa Direct and three Visa awards in November 2025. Mastercard has a domestic credit card, a debit choice and the Danphe debit launched in November 2025, gateway acceptance, SecureCode and card-funded nRemit. Scheme fees to both reached NPR 929 million in FY2025/26.",
          s=["con"], div="nabil", rev="cards", mc="The relationship this map is drawn for.",
          src=[["ShareSansar: Mastercard debit, Nov 2025", MCDEBIT], ["ShareSansar: Visa awards, Nov 2025", VISAAWARDS], ["Annual report 2024/25", AR25], ["FY2025/26 audited extract", AR26]]),
    ]},
    {"id": "pillar-market", "name": "Nepal payments", "blurb": "QR and NCHL outrun cards.", "products": [
        P("market", "The Nepali market", "13.7 million debit and 318,000 credit cards (mid-July 2025) against 2.9 million QR merchants and 26.8 million wallet users; Fonepay has 2 million+ merchants and a QR credit card; NCHL's connectIPS, NEPALPAY QR and NEPALPAY card are the national rails; UnionPay joined Fonepay QR in May 2026. Commercial-bank NPLs 4.44% (FY2024/25).",
          s=["con"], div="nabil", rev="fi", src=[["NRB: oversight report 2024/25", NRB], ["NCHL newsletter, Aug 2026", NCHL], ["ShareSansar: Fonepay and UnionPay, May 2026", FPUPI], ["ShareSansar: Fonepay Credit Card, Aug 2026", FPCC]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
