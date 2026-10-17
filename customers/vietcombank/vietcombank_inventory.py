"""Vietcombank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the H1 2026 results (reported 31 July 2026), the
2025 results given to the AGM (24 April 2026), the 2024 annual report and the bank's card pages. Vietcombank
publishes little in English, so several sources are Vietnamese press, translated. ``neo`` is the Mastercard
lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

ABOUT = "https://www.vietcombank.com.vn/en/Ve-Vietcombank"
IR = "https://www.vietcombank.com.vn/en/Nha-dau-tu"
AR24 = "https://static2.vietstock.vn/vietstock/2025/4/21/20250421_vcb_250421_annual_report_2024.pdf"
AGM26 = "https://nguoiquansat.vn/dhdcd-vietcombank-du-kien-chi-20-332-ty-dong-de-tra-co-tuc-thanh-lap-ngan-hang-con-tai-vifc-288118.html"
H126 = "https://mekongasean.vn/lai-ban-nien-vietcombank-vuot-29000-ty-dong-thu-nhap-nhan-vien-tang-manh-57943.html"
CEO25 = "https://thitruongtaichinhtiente.vn/ong-le-quang-vinh-duoc-bo-nhiem-lam-tong-giam-doc-vietcombank-66142.html"
LEGAL24 = "https://vnba.org.vn/vi/vietcombank-bo-nhiem-nguoi-dai-dien-theo-phap-luat-thay-ong-pham-quang-dung-12896.htm"
VCBNEO = "https://vtcnews.vn/sau-chuyen-giao-bat-buoc-ve-vietcombank-ngan-hang-xay-dung-co-ten-moi-ar921982.html"
VIRTUSA = "https://www.intelligentcio.com/apac/2026/08/18/vietcombank-partners-with-virtusa-to-launch-next-gen-corporate-banking-platform/"
CARDS = "https://www.vietcombank.com.vn/en/Personal/SPDV/The"
CARD = "https://www.vietcombank.com.vn/en/Personal/SPDV/The/"
CTP26 = "https://thitruongtaichinhtiente.vn/vietcombank-chinh-thuc-trien-khai-tinh-nang-click-to-pay-cho-chu-the-visa-80892.html"
VISAAW25 = "https://nhandan.vn/vietcombank-duoc-to-chuc-the-quoc-te-visa-vinh-danh-voi-8-giai-thuong-quan-trong-nam-2025-post916943.html"
MCAW25 = "https://tapchikinhtetaichinh.vn/vietcombank-duoc-vinh-danh-voi-ba-giai-thuong-danh-gia-tai-su-kien-thuong-nien-mastercard-customer-forum-2025-131929.html"
AW15 = "https://thanhtra.com.vn/tai-chinh-701717FFD/vietcombank-nhan-8-giai-thuong-cua-to-chuc-the-quoc-te-visa-va-mastercard-11729BB9.html"
AW21 = "https://thitruongtaichinhtiente.vn/print/39056.html"
APPLE23 = "https://theinvestor.vn/news/six-lenders-join-apple-pay-launch-in-vietnam-d6146.amp"
GW22 = "https://tapchicongthuong.vn/vietcombank-chinh-thuc-trien-khai-dich-vu-thanh-toan-qua-ung-dung-google-wallet-cho-the-visa-100600.htm"
APC24 = "https://daibieunhandan.vn/vietcombank-gioi-thieu-apple-pay-den-chu-the-noi-dia-vietcombank-connect24-post410510.html"
AMEX = "https://daibieunhandan.vn/vietcombank-amex-va-nhung-quyen-nang-chua-tung-co-10285910.html"
SBV25 = "https://mekongasean.vn/den-cuoi-nam-2025-ca-nuoc-co-tren-232-trieu-tai-khoan-thanh-toan-51536.html"
NAPAS25 = "https://en.napas.com.vn/napas-2025-member-organization-conference-184260317124736875.htm"
XQR26 = "https://vietnamnet.vn/en/vietnam-sees-eightfold-rise-in-qr-payments-by-tourists-from-three-neighbors-2559837.html"
IDEMIA = "https://fintechnews.sg/110299/payments/idemia-napas-vietnam/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · state · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Vietnam's most profitable bank, VND 2.66 quadrillion of assets, 74.8% owned by the state and 15% by Mizuho, a foreign-trade bank since 1963, a failed bank taken over as VCBNeo, and a 2030 plan to join the world's top 200 financial institutions.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "VND 29.2tn pre-tax in H1.", "div": "vcb", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Pre-tax profit of VND 29,222 billion in H1 2026, up 33.5%, with a record VND 17,420 billion in Q2; total assets about VND 2.66 quadrillion, loans over VND 1.76 quadrillion and deposits nearly VND 1.73 quadrillion at 30 June 2026; NPL ratio 0.61%. Q2 net fee income was flat at VND 860 billion.",
              s=["corp"], neo=[0, ""], src=[["Mekong ASEAN: H1 2026 results, Jul 2026", H126]]),
            P("fy25", "2025 results", "Consolidated pre-tax profit of VND 44,020 billion in 2025, up just over 4% and still the system's highest; assets over VND 2.4 quadrillion (+17%), credit about VND 1.7 quadrillion (+15%). The 2026 plan is credit growth of about 10% within a 13% cap and profit up about 5% ⚠.",
              s=["corp"], neo=[0, ""], src=[["Người Quan Sát: 2026 AGM, Apr 2026", AGM26]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & heritage", "blurb": "State 74.8%, Mizuho 15%.", "div": "vcb", "rev": "group", "products": [
            P("owners", "Ownership, listing & ratings", "The State Bank of Vietnam holds 74.8% for the state and Mizuho Bank 15.0% (end-2024); listed on HOSE as VCB since 30 June 2009; market value about USD 18 billion at end-2025; rated BB+, Ba2 (positive) and BB, the highest of any Vietnamese commercial bank ⚠ agencies not labelled.",
              s=["corp"], o="I", neo=[0, ""], src=[["Vietcombank annual report 2024", AR24], ["Vietcombank: investors", IR], ["Người Quan Sát: 2026 AGM, Apr 2026", AGM26]]),
            P("heritage", "Heritage & network", "Founded on 1 April 1963 from the central bank's foreign-exchange bureau, the first state bank to be equitised (2008); 131 branches, 536 transaction offices, about 24,000 staff and 1,194 correspondent banks in 87 countries.",
              s=["con"], o="I", neo=[0, ""], src=[["Vietcombank: about us", ABOUT]]),
            P("capital", "Capital raising", "A 49.5% share dividend took charter capital to VND 83,557 billion in 2025; the April 2026 AGM approved a bonus issue of about 1 billion shares and a private placement of up to 6.5%, towards about VND 99,000 billion ⚠ timing 2026–27.",
              s=["corp"], st="new", neo=[0, ""], src=[["Người Quan Sát: 2026 AGM, Apr 2026", AGM26]]),
        ]},
        {"id": "1.3", "ic": "users-round", "name": "Leadership", "blurb": "Tùng chairs, Vinh runs it.", "div": "vcb", "rev": "group", "products": [
            P("leadership", "Board & executive", "Chairman Nguyễn Thanh Tùng (CEO from 2023, legal representative from January 2024); CEO Lê Quang Vinh from 7 March 2025; Deputy CEO Shojiro Mizoguchi for Mizuho; Đoàn Hồng Nhung, board member and Retail Director, leads retail and cards.",
              s=["corp"], neo=[0, ""], src=[["Thị trường Tài chính Tiền tệ: new CEO, Mar 2025", CEO25], ["VNBA: legal representative, Jan 2024", LEGAL24], ["Nhân Dân: Visa awards, Oct 2025", VISAAW25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & data", "blurb": "Core 2020, AI-native 2026.", "div": "vcb", "rev": "group", "products": [
            P("tech", "Core, data & cloud", "Core banking replaced in early 2020, a data platform for big data in the 2025 plan, cloud training on AWS, and VCB Corporate DigiBank: a cloud-native, AI-native corporate platform built with Virtusa, billed as the largest technology project in the bank's history (August 2026).",
              s=["corp"], st="new", ay="Aug 2026", o="P", at="Virtusa", neo=[0, ""], src=[["Intelligent CIO: Virtusa, Aug 2026", VIRTUSA], ["Vietcombank annual report 2024", AR24]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Top 200 by 2030.", "div": "vcb", "rev": "group", "products": [
            P("strategy", "Strategy to 2030", "Stay Vietnam's number one bank, enter the world's top 200 financial institutions and top 700 listed companies, lead in digital transformation, raise fee income and seek an international listing; a wholly owned bank in the Vietnam International Financial Centre with VND 3,000 billion of capital was approved in April 2026.",
              s=["corp"], st="new", neo=[0, ""], src=[["Vietcombank: about us", ABOUT], ["Người Quan Sát: 2026 AGM, Apr 2026", AGM26]]),
            P("vcbneo", "VCBNeo", "Construction Bank, a failed state-owned bank, was transferred to Vietcombank by order of the central bank on 17 October 2024 and renamed Vietcombank Neo (VCBNeo) on 17 January 2025; wholly owned and not consolidated.",
              s=["con"], st="new", ay="Jan 2025", o="A", neo=[0, ""], src=[["VTC News: VCBNeo, Jan 2025", VCBNEO], ["Vietcombank annual report 2024", AR24]]),
            P("laos", "Vietcombank Laos", "A wholly owned bank in Laos, licensed on 30 August 2024 with VND 1,820 billion of capital, alongside a Vietnam–Laos QR payment service launched in 2024.",
              s=["corp"], st="new", ay="Aug 2024", o="B", neo=[0, ""], src=[["Vietcombank annual report 2024", AR24]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: credit cards on five international brands, debit on NAPAS and Visa, wallets and Click to Pay that came to Visa first, 121,000 acceptance points, NAPAS transfers and VietQR, and the foreign-trade bank's FX and remittance rails.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "Visa, Amex, Mastercard, JCB.", "div": "cards", "rev": "retail", "products": [
            P("mccredit", "Vietcombank Mastercard & World Mastercard", "Two live Mastercard credit cards: the standard card (up to 45 days interest-free, VCB Rewards, limits to VND 300 million) and World Mastercard (5% cashback on dining and travel abroad, travel cover to VND 11.65 billion, golf).", short="Mastercard credit",
              s=["con", "aff"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's main programmes at the bank, two of about nine live credit cards.",
              src=[["Vietcombank: Mastercard credit card", CARD + "Credit_VCB-Mastercard"], ["Vietcombank: World Mastercard", CARD + "Credit_VCB-Mastercard-World"]]),
            P("visacredit", "Visa Platinum, Vibe, Snack & Takashimaya", "The mass and youth credit cards are Visa: Visa Platinum (0.5% cashback), Vibe and Vibe Platinum ⚠ (points on Shopee, Grab and travel), Visa Snack (fully online, MoMo cashback) and the Saigon Centre–Takashimaya Visa.", short="Visa credit",
              s=["con", "young"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Vietcombank: Vibe", CARD + "Credit_VCB-Vibe"], ["Vietcombank: Visa Snack", CARD + "Credit_VCB-Snack"], ["Vietcombank: Visa Platinum", CARD + "Credit_VCB-Visa-Platinum"]]),
            P("amex", "American Express range", "Vietcombank Amex, Vietnam Airlines Amex and Platinum Amex (Lotusmiles), and Cashplus Platinum Amex (1.5% overseas cashback, travel cover to VND 23.3 billion); described as Amex's only issuer in Vietnam ⚠.", short="Amex credit",
              s=["aff"], lc="borrow", o="P", at="American Express, Vietnam Airlines", neo=[0, "Amex."], src=[["Vietcombank: Cashplus Platinum Amex", CARD + "Credit_VCB-Cashplus-Platinum-Amex"], ["Đại biểu Nhân dân: Vietcombank Amex", AMEX]]),
            P("jcb", "JCB & JCB Platinum", "JCB credit cards with 5% restaurant and supermarket cashback and Japan campaigns; Apple Pay for JCB from June 2025. UnionPay credit cards are no longer issued.", short="JCB credit",
              s=["con", "aff"], lc="borrow", o="P", at="JCB", neo=[0, "JCB."], src=[["Vietcombank: JCB Platinum", CARD + "Credit_VCB-JCB-Platinum"], ["Vietcombank: discontinued credit cards", CARD + "Credit_The-ngung-phat-hanh"]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Debit cards", "blurb": "NAPAS at home, Visa abroad.", "div": "cards", "rev": "retail", "products": [
            P("connect24", "Vietcombank Connect24", "The domestic debit card on every account, on NAPAS: contactless, cards for children aged 6 to 15, Samsung Pay and, from April 2025 ⚠, Apple Pay; co-branded versions for hospitals.", short="Connect24 (NAPAS)",
              s=["con", "young"], lc="everyday", o="P", at="NAPAS", neo=[0, "NAPAS."],
              mc="The default card is domestic; international brands are the add-on.",
              src=[["Vietcombank: Connect24", CARD + "Debit_VCB-Connect24"], ["Đại biểu Nhân dân: Apple Pay for Connect24", APC24]]),
            P("visadebit", "eVer-link, DigiCard, MeGO & other Visa debit", "The international debit cards are Visa: eVer-link (Connect24 Visa), VCB DigiCard issued in about a minute in the app, Visa MeGO (carbon footprint, Hanoi Metro cashback, September 2026), Haha Collection, DigiAds and Visa Platinum debit.", short="Visa debit",
              s=["con", "young"], lc="everyday", st="new", o="P", at="Visa", neo=[0, "Visa."], src=[["Vietcombank: eVer-link", CARD + "Debit_VCB-Everlink"], ["Vietcombank: VCB DigiCard", CARD + "Debit_VCB-DigiCard"], ["Vietcombank: Visa MeGO", CARD + "Debit_VCB-MeGO"]]),
            P("mcdebit", "Vietcombank Mastercard Debit", "A contactless Mastercard debit card, physical or virtual, with VCB Rewards; Mastercard named Vietcombank its 'Debit Growth Trailblazer' in December 2025. Its page shows no apply button ⚠.", short="Mastercard debit",
              s=["con"], lc="everyday", st="unconf", o="P", at="Mastercard", neo=[2, "Mastercard ⚠ de-emphasised."], src=[["Vietcombank: Mastercard debit", CARD + "Debit_VCB-Mastercard"], ["Tạp chí Kinh tế Tài chính: Mastercard awards, Dec 2025", MCAW25]]),
        ]},
        {"id": "2.3", "ic": "smartphone", "name": "Wallets & tokens", "blurb": "Visa first, every time.", "div": "digi", "rev": "retail", "products": [
            P("wallets", "Apple Pay, Google Wallet & Samsung Pay", "Google Wallet for Visa cards from 15 November 2022; Apple Pay from 8 August 2023 with Visa; then NAPAS Connect24 (April 2025 ⚠) and JCB (June 2025); Samsung Pay and Garmin Pay also offered. No Mastercard wallet launch is public ⚠.",
              s=["con", "young"], lc="everyday", o="P", at="Apple, Google, Samsung", neo=[1, "Visa first; Mastercard ⚠ not announced."],
              mc="Wallets came to Visa, NAPAS and JCB in public; Mastercard tokens are the gap.",
              src=[["The Investor: Apple Pay launch, Aug 2023", APPLE23], ["Tạp chí Công Thương: Google Wallet, Nov 2022", GW22], ["Vietcombank: cards and offers", CARDS]]),
            P("ctp", "Click to Pay", "Click to Pay for all personal Visa debit and credit cards from 31 March 2026, on Visa Token Service, switched on by default for new Visa cards in VCB Digibank; Visa-backed promotions from May 2026.",
              s=["con", "young"], lc="move", st="new", ay="Mar 2026", o="P", at="Visa", neo=[0, "Visa Token Service."],
              mc="Mastercard Click to Pay is not live at Vietcombank.",
              src=[["Thị trường Tài chính Tiền tệ: Click to Pay, Apr 2026", CTP26]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acquiring", "blurb": "121,000 acceptance points.", "div": "vcb", "rev": "retail", "products": [
            P("acquiring", "Merchant acquiring", "121,035 card acceptance points taking seven card brands; Mastercard ranked Vietcombank first for merchant acceptance volume and as leading acquirer for global travellers (December 2025), and Visa first for merchant sales volume (October 2025).",
              s=["sme", "corp"], lc="move", o="B", neo=[1, "Accepts every brand."],
              mc="Mastercard's strongest public tie: acquiring for visitors.",
              src=[["Vietcombank: about us", ABOUT], ["Tạp chí Kinh tế Tài chính: Mastercard awards, Dec 2025", MCAW25], ["Nhân Dân: Visa awards, Oct 2025", VISAAW25]]),
            P("ecom", "E-commerce & instalments at merchants", "Online card acceptance and 0% instalment offers at merchants, such as the Apple Store online through OnePAY; the OnePAY tie dates from Mastercard's early gateway work ⚠.",
              s=["sme"], lc="move", o="P", at="OnePAY", neo=[1, "All brands ⚠."], src=[["Vietcombank: cards and offers", CARDS]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "NAPAS & VietQR", "blurb": "32 million transfers a day.", "div": "digi", "rev": "retail", "products": [
            P("napas247", "NAPAS 24/7 transfers & VietQR", "Instant interbank transfers and VietQR in VCB Digibank and at ATMs; NAPAS handled more than 32 million transactions a day in 2025 and VietQR value rose 85% in ten months. Vietcombank owns 1.83% of NAPAS.", short="NAPAS & VietQR",
              s=["con", "sme"], lc="move", o="P", at="NAPAS", neo=[0, "NAPAS."],
              mc="The domestic rail that takes everyday payments away from cards.",
              src=[["NAPAS: 2025 conference, Nov 2025", NAPAS25], ["Vietcombank annual report 2024", AR24]]),
            P("xqr", "Cross-border QR", "A Vietnam–Laos QR service (2024) and NAPAS's VietQR links to Thailand, Cambodia, Laos, Singapore, Korea, UnionPay (December 2025) and Alipay (April 2026); inbound volumes from three neighbours rose eightfold in the first eight months of 2026.",
              s=["con", "travel"], lc="move", st="new", o="P", at="NAPAS", neo=[0, "NAPAS VietQR."], src=[["VietNamNet: cross-border QR, Sep 2026", XQR26], ["Vietcombank annual report 2024", AR24]]),
        ]},
        {"id": "2.6", "ic": "earth", "name": "FX, trade & remittances", "blurb": "The foreign-trade bank.", "div": "remit", "rev": "wholesale", "products": [
            P("trade", "Trade finance & FX", "The bank's heritage business: trade finance, foreign exchange and derivatives through 1,194 correspondent banks; Visa also ranks it first for cross-border payment volume (2025).",
              s=["corp", "sme"], lc="move", o="I", neo=[0, ""], src=[["Vietcombank: about us", ABOUT], ["Nhân Dân: Visa awards, Oct 2025", VISAAW25]]),
            P("remit", "VCB Money, VCBR & Vinafico", "Remittances into Vietnam through Vietcombank Money Transfer (VCBR), VCB Money in the US (87.5%) and Vinafico Hong Kong.",
              s=["travel", "con"], lc="move", o="B", neo=[None, "Nothing public."],
              mc="An opening for Mastercard Move.",
              src=[["Vietcombank annual report 2024", AR24]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: chip, 3-D Secure, tokens and biometric checks under central-bank rules, a data platform and an AI-native corporate build, VCB Rewards and network offers, card instalments, and green credit.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security & identity", "blurb": "Biometrics by law.", "div": "vcb", "rev": "retail", "products": [
            P("security", "Card security & biometric checks", "EMV chip, 3-D Secure 2.0, tokenisation and PCI DSS on cards; biometric checks against chip ID cards and VNeID under central-bank rules from 1 July 2024 (146.1 million individual records verified across the system by January 2026). No network fraud tool is public ⚠.",
              s=["con", "sme"], lc="everyday", o="B", neo=[None, "Nothing public."], src=[["Nhân Dân: Visa awards, Oct 2025", VISAAW25], ["Vietcombank annual report 2024", AR24], ["Mekong ASEAN: payments data, Feb 2026", SBV25]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data & AI", "blurb": "A data platform.", "div": "vcb", "rev": "group", "products": [
            P("data", "Data platform & AI", "A group data platform for 'big data' is a 2025 priority, and the new corporate platform is designed as AI-native; no retail AI assistant is public ⚠.",
              s=["corp"], st="new", neo=[0, ""], src=[["Vietcombank annual report 2024", AR24], ["Intelligent CIO: Virtusa, Aug 2026", VIRTUSA]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & offers", "blurb": "VCB Rewards, network deals.", "div": "cards", "rev": "retail", "products": [
            P("rewards", "VCB Rewards & VCB Loyalty", "Points on cards (2 per VND 1,000, more online and abroad) redeemed in VCB Digibank, and a VCB Loyalty refer-a-friend scheme.",
              s=["con", "young"], lc="grow", o="B", neo=[0, ""], src=[["Vietcombank: cards and offers", CARDS]]),
            P("offers", "Network offers", "Card-brand campaigns: 'Offers of Vietcombank Mastercard abroad' (June 2025), Traveloka x Mastercard, Mastercard deals at Jollibee and California Fitness; alongside Visa travel privileges, Amex dining and JCB Japan draws.",
              s=["con", "aff", "travel"], lc="grow", o="P", at="Mastercard, Visa, Amex, JCB", neo=[1, "Mastercard among four brands."], src=[["Vietcombank: cards and offers", CARDS]]),
        ]},
        {"id": "3.4", "ic": "receipt-text", "name": "Instalments", "blurb": "0% on cards.", "div": "cards", "rev": "retail", "products": [
            P("install", "Card instalments", "0% instalment plans on credit cards and flexible instalments for larger purchases, offered on every brand and promoted with Mastercard, Visa and merchants.",
              s=["con"], lc="borrow", o="B", neo=[1, "All brands."], src=[["Vietcombank: Mastercard credit card", CARD + "Credit_VCB-Mastercard"], ["Vietcombank: cards and offers", CARDS]]),
        ]},
        {"id": "3.5", "ic": "sparkles", "name": "Green banking", "blurb": "Green credit, MeGO.", "div": "vcb", "rev": "wholesale", "products": [
            P("green", "Green credit & carbon footprint", "A green-credit portfolio for firms and households, and a carbon-footprint view on the Visa MeGO debit card ⚠ provider not named.",
              s=["con", "corp"], lc="beyond", st="new", neo=[0, "Visa card."],
              mc="Room for Mastercard's Carbon Calculator on its own cards.",
              src=[["Vietcombank annual report 2024", AR24], ["Vietcombank: Visa MeGO", CARD + "Debit_VCB-MeGO"]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail deposits and loans, priority banking and FWD insurance, SME and corporate banking for FDI and mid-market firms, capital markets, and the securities, leasing and fund subsidiaries.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Retail banking", "blurb": "Deposits, homes, cars.", "div": "vcb", "rev": "retail", "products": [
            P("deposits", "Accounts & savings", "Current accounts, savings and term deposits in VND and foreign currency; customer deposits of nearly VND 1.73 quadrillion at 30 June 2026.",
              s=["con"], lc="everyday", neo=[0, "NAPAS and Visa debit."], src=[["Mekong ASEAN: H1 2026 results, Jul 2026", H126]]),
            P("retailloans", "Home, auto & consumer loans", "Home, car, consumer and business loans for individuals, inside loans of over VND 1.76 quadrillion; retail credit growth is a stated priority.",
              s=["con", "home"], lc="borrow", neo=[0, ""], src=[["Vietcombank annual report 2024", AR24]]),
        ]},
        {"id": "4.2", "ic": "gem", "name": "Priority & insurance", "blurb": "FWD since 2019.", "div": "vcb", "rev": "retail", "products": [
            P("priority", "Priority banking", "A separate priority-banking service with its own privileges and conditions, paired with Amex and World Mastercard premium cards.",
              s=["aff"], lc="grow", neo=[1, "Premium cards split."], src=[["Vietcombank: about us", ABOUT]]),
            P("banca", "Bancassurance with FWD", "Life insurance sold through the branch network under a distribution agreement with FWD signed on 12 November 2019, still promoted in 2025–26.",
              s=["aff", "con"], lc="grow", o="P", at="FWD", neo=[0, ""], src=[["Vietcombank annual report 2024", AR24], ["Vietcombank: cards and offers", CARDS]]),
        ]},
        {"id": "4.3", "ic": "briefcase-business", "name": "SME & corporate", "blurb": "FDI and mid-market.", "div": "vcb", "rev": "wholesale", "products": [
            P("sme", "SME banking", "Loans, accounts, overdrafts and payments for small firms, run in VCB DigiBiz.",
              s=["sme"], lc="everyday", neo=[0, ""], src=[["Vietcombank annual report 2024", AR24]]),
            P("corporate", "Corporate, FDI & mid-market", "Wholesale banking for large corporates, FDI firms and the mid-market, with cash management and commercial cards; Visa ranked the bank first for commercial payment volume in 2025.",
              s=["corp"], lc="borrow", neo=[0, "Commercial cards mostly Visa ⚠."],
              mc="Commercial and virtual cards are open ground.",
              src=[["Vietcombank annual report 2024", AR24], ["Nhân Dân: Visa awards, Oct 2025", VISAAW25]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Capital & markets", "blurb": "FX, bonds, derivatives.", "div": "vcb", "rev": "markets", "products": [
            P("markets", "Treasury & markets", "Foreign exchange, bonds and derivatives for clients and the bank's own book, run by the Capital and Markets division.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["Vietcombank: about us", ABOUT]]),
        ]},
        {"id": "4.5", "ic": "building-2", "name": "Subsidiaries", "blurb": "Securities, leasing, funds.", "div": "vcbs", "rev": "group", "products": [
            P("vcbs", "VCBS & VCBF", "Vietcombank Securities (wholly owned, pre-tax profit about VND 634 billion in 2024) and the Vietcombank Fund Management joint venture.",
              s=["aff", "corp"], lc="grow", neo=[0, ""], src=[["Vietcombank annual report 2024", AR24]]),
            P("leasing", "Vietcombank Leasing", "Financial leasing through Vietcombank Financial Leasing (VCBL), wholly owned.",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["Vietcombank annual report 2024", AR24]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: VCB Digibank, which carries 99% of retail transactions, DigiBiz, CashUp and the corporate platform in build, 667 branches and offices with 3,090 ATMs, and co-brand partners from Vietnam Airlines to Hanoi Metro.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "VCB Digibank", "blurb": "99% of retail transactions.", "div": "digi", "rev": "retail", "products": [
            P("digibank", "VCB Digibank", "The retail app: card issuance and control, transfers, QR, savings and gold-bar booking; 99% of retail transactions were digital by end-2024; a new version in 2024 and an 'An vui' version for older customers. User numbers are not published ⚠.",
              s=["con", "young"], lc="everyday", neo=[0, ""], src=[["Nhân Dân: Visa awards, Oct 2025", VISAAW25], ["Vietcombank annual report 2024", AR24]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Business channels", "blurb": "DigiBiz, CashUp.", "div": "digi", "rev": "wholesale", "products": [
            P("digibiz", "VCB DigiBiz", "Digital banking for SMEs and household businesses, with overdraft disbursement added in 2024.",
              s=["sme"], lc="everyday", neo=[0, ""], src=[["Vietcombank annual report 2024", AR24]]),
            P("cashup", "VCB CashUp, iB@nking & Corporate DigiBank", "Cash management and internet banking for corporates, to be replaced by VCB Corporate DigiBank, the multi-year build with Virtusa announced in August 2026.",
              s=["corp"], lc="everyday", st="new", o="P", at="Virtusa", neo=[0, ""], src=[["Intelligent CIO: Virtusa, Aug 2026", VIRTUSA], ["Vietcombank: about us", ABOUT]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & ATMs", "blurb": "131 branches, 3,090 ATMs.", "div": "vcb", "rev": "retail", "products": [
            P("branches", "Branches, offices & ATMs", "131 branches, 536 transaction offices and 3,090 ATMs, with QR cash withdrawal; representative offices in Singapore and the US.",
              s=["con", "sme"], lc="open", neo=[0, ""], src=[["Vietcombank: about us", ABOUT]]),
        ]},
        {"id": "5.4", "ic": "plane", "name": "Co-brand partners", "blurb": "Airlines to metro.", "div": "cards", "rev": "retail", "products": [
            P("partners", "Co-brands & partners", "Vietnam Airlines (Amex), Saigon Centre–Takashimaya (Visa), Tekmedi and Chợ Rẫy hospitals (Connect24), Vietnam National University HCMC (Visa), Hanoi Metro (Visa MeGO) and MoMo (Visa Snack).",
              s=["con", "travel"], lc="open", o="P", at="Vietnam Airlines, Takashimaya, MoMo", neo=[0, "Visa, Amex and NAPAS co-brands."],
              mc="No public Mastercard co-brand.",
              src=[["Vietcombank: cards and offers", CARDS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Vietcombank", "blurb": "One of five brands.", "products": [
        P("mcatvcb", "Mastercard at Vietcombank", "Vietcombank issues five international brands. Visa is the default for new debit and credit, wallets and Click to Pay; NAPAS carries the domestic Connect24 card and VietQR. Mastercard has two credit cards and a debit card, and rates Vietcombank its leading acquirer for merchant volume and travellers (December 2025). No network agreement is public ⚠.",
          s=["con"], div="cards", rev="retail", mc="The relationship this map is drawn for.",
          src=[["Tạp chí Kinh tế Tài chính: Mastercard awards, Dec 2025", MCAW25], ["Vietcombank: cards and offers", CARDS], ["Thanh Tra: 2015 awards", AW15]]),
    ]},
    {"id": "pillar-market", "name": "Vietnamese payments", "blurb": "QR, NAPAS, 164m cards.", "products": [
        P("market", "The Vietnamese market", "164 million bank cards and 232 million payment accounts at end-2025; QR payments up 124% by value in 2025; NAPAS tokenising domestic cards with IDEMIA; central-bank caps on credit growth and biometric checks on transfers.",
          s=["con"], div="vcb", rev="group", src=[["Mekong ASEAN: payments data, Feb 2026", SBV25], ["Fintech News SG: NAPAS and IDEMIA, Apr 2025", IDEMIA], ["NAPAS: 2025 conference, Nov 2025", NAPAS25]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
