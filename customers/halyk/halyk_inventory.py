"""Halyk Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 1H 2026 results, presentation and call
(18 August 2026), the 2025 annual report, and the bank's product and tariff pages. ``neo`` is the Mastercard
lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1PR = "https://halykbank.com/storage/830/Press-Release.pdf"
H1P = "https://halykbank.com/storage/831/Presentation.pdf"
H1T = "https://halykbank.com/storage/844/Call-Transcript.pdf"
AR25 = "https://halykbank.com/storage/789/2025.pdf"
IR = "https://halykbank.com/"
ABOUT = "https://halykbank.com/about-us"
BOARD = "https://halykbank.com/news/on-election-of-the-new-board-of-directors"
MB1 = "https://halykbank.com/news/changes-to-the-management-board-2026"
MB2 = "https://halykbank.com/news/changes-to-the-management-board-2026-04-02"
SP = "https://halykbank.com/news/sp-global-ratings-revises-outlook-on-halyk-bank-to-positive"
CLICK = "https://halykbank.com/news/halyk-bank-and-click-sign-agreement-on-strategic-partnership"
EURO = "https://halykbank.com/news/euromoney-ranks-halyk-as-kazakhstans-best-transaction-bank"
TARIFF = "https://halykbank.kz/storage/app/media/Tarify/2026/8/ENG_Pril_2_TarifyFL_01.08.2026.pdf"
MCWE = "https://halykbank.kz/en/card/mastercard-worldelite-new"
MCIMP = "https://halykbank.kz/en/card/mastercard-worldelite-imperial"
VIP = "https://halykbank.kz/en/card/diamond"
VSIG = "https://halykbank.kz/en/card/visa-signature-new"
VULTRA = "https://halykbank.kz/en/card/visa-infinite-ultra"
UPD = "https://halykbank.kz/en/card/black"
INFC = "https://halykbank.kz/en/card/infinite"
MYCARD = "https://halykbank.kz/en/card/mycard"
BONUS = "https://halykbank.kz/en/card/digital"
APPLE = "https://halykbank.kz/en/card/apple-pay"
VDIRECT = "https://halykbank.kz/en/transfer/alipay-i-wechat"
TRANSFERS = "https://halykbank.kz/en/transfers"
ACQ = "https://halykbank.kz/en/business/payments"
BIZCARDS = "https://halykbank.kz/en/business/cards"
HID = "https://halykbank.kz/en/other/halyk-id"
VOICE = "https://halykbank.kz/en/other/golosovaya-biometriya"
CLUB = "https://halykbank.kz/en/halykclub/page/halyk-club"
OIY = "https://halykbank.kz/en/other/halyk-oiy-tech-2026"
NBKCARDS = "https://nationalbank.kz/en/news/elektronnye-bankovskie-uslugi/19843"
IMTPS = "https://www.kt.kz/eng/society/interbank_qr_payments_to_become_available_across_1377995187.html"
UQR = "https://astanatimes.com/2025/11/kazakhstan-launches-unified-interbank-qr-payment-system/"
KASPI = "https://ir.kaspi.kz/media/2Q_2026_Results.pdf"
MCHUB = "https://forbes.kz/news/newsid_309262"
DTCARD = "https://forklog.com/en/kazakhstan-issues-payment-card-linked-to-the-digital-tenge/"
HUMO = "https://tengebank.uz/en/about/press_center/pressrelease/50"
REKASSA = "https://kapital.kz/business/148881/halyk-bank-kupil-servis-rekassa.html"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · ownership · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Central Asia's largest bank with KZT 22 trillion of assets and about 30% of Kazakh loans and deposits, ALMEX's majority since 2004, a history back to 1923, and a 2025–2027 strategy built on ecosystems, Uzbekistan and AI.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "KZT 22trn, RoAE 24.8%.", "div": "group", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Total assets KZT 22,036 billion, gross loans KZT 13,958 billion and deposits KZT 14,871 billion at 30 June 2026. Net income KZT 447.6 billion in 1H 2026, down 15.3% on higher reserve requirements and lending curbs (RoAE 24.8%); KZT 1,058 billion in 2025 (RoAE 32.6%). Capital adequacy 19.0%.",
              s=["con"], neo=[0, ""], src=[["1H 2026 results", H1PR], ["Annual report 2025", AR25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "ALMEX 61.9%; Shayakhmetova CEO.", "div": "group", "rev": "other", "products": [
            P("owners", "Ownership, listings & ratings", "ALMEX Holding Group owns 61.9%, GDR holders 35% (30 June 2026); listed on KASE (1998), London (2006) and AIX (2019); market cap about US$6.8 billion in July 2025 ⚠. Rated Baa1 (Moody's), BBB- (Fitch) and BBB- with a positive outlook from S&P (September 2026).",
              s=["corp"], neo=[0, ""], src=[["Halyk: about us", ABOUT], ["S&P outlook positive, Sep 2026", SP], ["Halyk and Click, Jul 2025", CLICK]]),
            P("leadership", "Board & management", "Chairman Arman Dunayev; CEO Umut Shayakhmetova, at Halyk since 2004 and on Mastercard's Europe (since 2019) and EEMEA (since 2022) advisory boards ⚠; First Deputy CEO Dauren Sartayev (B2B, acquiring); CFO Murat Koshenov; new deputy CEOs Mikhail Khasin (IT, January 2026) and Kiril Bachvarov (B2C, April 2026).",
              s=["corp"], st="new", neo=[0, "CEO sits on Mastercard advisory boards."],
              mc="The CEO's seat on Mastercard's advisory boards is the most senior tie between the two.",
              src=[["Board elected, Apr 2026", BOARD], ["Khasin appointed, Jan 2026", MB1], ["Bachvarov appointed, Apr 2026", MB2], ["Annual report 2025", AR25]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology & AI", "blurb": "AI agents, own data centres.", "div": "group", "rev": "other", "products": [
            P("tech", "Core, cloud & AI", "AI built into service, onboarding, lending and lead generation under the 2025–2027 strategy; Kazteleport runs the group's data centres and GPU cloud; an AI agent platform and bank-scale LLM service are on the agenda of Halyk OIY Tech on 29 October 2026, with Visa, AWS and Microsoft speakers.",
              s=["corp"], st="new", neo=[0, ""], src=[["Annual report 2025", AR25], ["Halyk OIY Tech 2026", OIY]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & deals", "blurb": "Ecosystems, Uzbekistan, AI.", "div": "group", "rev": "other", "products": [
            P("strategy", "Strategy 2025–2027 & 2026 targets", "Grow the B2C and B2B ecosystems, scale in Uzbekistan and lead on AI. For 2026: net income about KZT 1.0 trillion, RoAE about 29%, loans +9–12%; net fee guidance cut in August 2026 to about −10% after BNPL curbs and VAT on banking services.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025", AR25], ["1H 2026 call", H1T]]),
            P("deals", "Deals", "re:Kassa cash-register service (Comrun) bought, completed June 2026; a 49% stake in Uzbekistan's Click agreed for US$176.4 million in July 2025 lapsed without completion ⚠ talks continue; Halyk Bank Kyrgyzstan sold in 2024; SPO in 2025.",
              s=["merch"], o="A", st="flux", neo=[0, ""], src=[["Halyk and Click, Jul 2025", CLICK], ["Annual report 2025", AR25], ["Kapital.kz: re:Kassa, Jun 2026", REKASSA]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: debit cards on Visa, Mastercard, UnionPay and Amex; premium cards with Mastercard World Elite at the top; credit and BNPL; wallets and Halyk QR; phone-number and cross-border transfers on Visa Direct; acquiring for every network; and the first digital-tenge card, on Visa.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "Visa, Mastercard, UnionPay, Amex.", "div": "bank", "rev": "retail", "products": [
            P("debit", "Debit cards & Halyk Bonus Digital", "Salary cards reach 39.3% of Kazakhstan's employed. The in-app Halyk Bonus Digital card is opened in a minute; the digital card is tariffed as Visa Gold ⚠, the basic pack as Visa Gold or MasterCard World, allowance and pension cards as UnionPay Gold or Visa Gold, with a Visa gift card and an American Express Rewards virtual card.", short="Debit (Visa-led, Mastercard option)",
              s=["con", "saver"], lc="everyday", o="B", at="Visa, Mastercard, UnionPay, Amex", neo=[1, "Mastercard World in the basic pack; the digital card is Visa ⚠."],
              mc="Mastercard is an option in the basic pack, but the mass digital card leans Visa.",
              src=[["Halyk retail card tariffs, Aug 2026", TARIFF], ["Halyk Bonus Digital card", BONUS], ["1H 2026 presentation", H1P]]),
        ]},
        {"id": "2.2", "ic": "gem", "name": "Premium cards", "blurb": "World Elite against Infinite.", "div": "bank", "rev": "retail", "products": [
            P("mcpremium", "Mastercard World Elite & World Elite Imperial", "Debit cards with 3% and 5% bonuses, Lounge Key, Fast Track through Mastercard Travel Experiences, Mastercard concierge and 'Cashback without borders' (330+ partners in 25 countries); Imperial adds insurance up to EUR 7.5 million. Also one of three choices for the VIP card.", short="World Elite (Mastercard)",
              s=["prem"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard World Elite."],
              mc="Mastercard's strongest product at Halyk: the top premium tier, with Mastercard's own benefits.",
              src=[["Halyk: Mastercard World Elite", MCWE], ["Halyk: World Elite Imperial", MCIMP], ["Halyk: VIP card", VIP]]),
            P("visapremium", "Visa Signature, Infinite Ultra & UnionPay Diamond", "Visa Signature and Visa Infinite Ultra (Dragon Pass, Visa concierge, up to 5% bonus), Visa Infinite or UnionPay Asia Prestige Diamond in the VIP card, and a UnionPay Diamond card in KZT, USD and CNY.", short="Visa & UnionPay premium",
              s=["prem"], lc="everyday", o="P", at="Visa, UnionPay", neo=[0, "Visa and UnionPay."],
              src=[["Halyk: Visa Signature", VSIG], ["Halyk: Visa Infinite Ultra", VULTRA], ["Halyk: UnionPay Diamond", UPD]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Credit & BNPL", "blurb": "0.6% of retail loans.", "div": "bank", "rev": "retail", "products": [
            P("credit", "Credit cards", "My!Card and DARA (limits up to KZT 7.5 million, digital issue in the app; networks not stated ⚠), Infinite Credit on Visa and a Black Premium credit card labelled MasterCard ⚠. Credit cards are only 0.6% of the retail book.",
              s=["con", "prem"], lc="borrow", st="new", o="B", at="Visa, Mastercard", neo=[1, "Black Premium on Mastercard ⚠; Infinite Credit on Visa."],
              src=[["Halyk: My!Card", MYCARD], ["Halyk: Infinite Credit", INFC], ["Annual report 2025", AR25]]),
            P("bnpl", "BNPL & instalments", "Buy-now-pay-later and 0-0-24 instalments at Halyk Market and partner retailers; BNPL fell to 2.2% of retail loans at 1 July 2026 as Halyk tightened underwriting under new rules, cutting fee income.",
              s=["con"], lc="borrow", st="flux", o="B", neo=[0, "Halyk's own."],
              src=[["1H 2026 presentation", H1P], ["1H 2026 call", H1T]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Wallets & QR", "blurb": "Halyk QR and the national QR.", "div": "bank", "rev": "retail", "products": [
            P("wallets", "Apple Pay, Google Pay, Samsung Pay & Face Pay", "Apple Pay for Halyk's Visa, Mastercard and American Express cards, plus Google Pay, Samsung Pay, Garmin Pay and Face Pay at Halyk POS.",
              s=["con", "prem"], lc="everyday", o="P", at="Apple, Google, Samsung", neo=[1, "Mastercard tokens among others."],
              src=[["Halyk: Apple Pay", APPLE], ["1H 2026 presentation", H1P]]),
            P("halykqr", "Halyk QR & Unified QR", "Halyk's own QR payments at its POS and in the Super-App, with bonuses, plus the National Bank's unified interbank QR (launched November 2025, nationwide from 19 July 2026), which bypasses card networks.", short="Halyk QR (account-to-account)",
              s=["con", "merch"], lc="move", st="new", o="B", neo=[0, "Account-to-account."],
              mc="QR and instant payments are where Kazakh spending is moving, outside any card network.",
              src=[["1H 2026 presentation", H1P], ["Astana Times: unified QR, Nov 2025", UQR], ["Kazinform: interbank QR, Jul 2026", IMTPS]]),
        ]},
        {"id": "2.5", "ic": "send", "name": "Transfers & cross-border", "blurb": "234.7m app payments in 1H.", "div": "bank", "rev": "retail", "products": [
            P("p2p", "Phone-number & instant transfers", "234.7 million app payments and transfers worth KZT 10.5 trillion in 1H 2026; free between Halyk clients, from KZT 200 to other banks by phone number over the national instant-payment system.",
              s=["con"], lc="move", o="B", neo=[0, "Account-to-account."], src=[["1H 2026 presentation", H1P], ["Halyk: transfers", TRANSFERS]]),
            P("xborder", "International transfers", "To accounts and Alipay or WeChat wallets in China and about 30 other countries via Visa Direct (0.1% fee), free transfers to Uzbekistan, Western Union and MoneyGram.", short="Cross-border (Visa Direct)",
              s=["con", "prem"], lc="move", o="P", at="Visa, Western Union, MoneyGram", neo=[0, "Visa Direct, Western Union, MoneyGram."],
              mc="Visa Direct carries Halyk's outbound card-based transfers; Mastercard Move is absent.",
              src=[["Halyk: Alipay and WeChat via Visa Direct", VDIRECT], ["Halyk: transfers", TRANSFERS]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acquiring", "blurb": "744m transactions in 2025.", "div": "bank", "rev": "sme", "products": [
            P("acquiring", "Merchant & internet acquiring", "744.2 million acquiring transactions in 2025 on Halyk POS, the Halyk Pos phone app and internet acquiring; WeChat Pay accepted on Halyk's own terminals and Uzbek HUMO cards since March 2026.",
              s=["merch"], lc="move", o="B", at="WeChat Pay, HUMO", neo=[1, "Accepts every network."],
              src=[["Annual report 2025", AR25], ["Halyk: acquiring", ACQ], ["Tenge Bank: HUMO at Halyk, Mar 2026", HUMO]]),
            P("rekassa", "re:Kassa", "Online cash register for fiscal receipts and tax, run by Comrun, which Halyk has owned since 3 June 2026 after an integrated POS-and-cash-register product in 2025.",
              s=["merch"], lc="everyday", st="new", ay="Jun 2026", o="A", neo=[0, ""], src=[["Kapital.kz: re:Kassa, Jun 2026", REKASSA]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Digital tenge", "blurb": "First card, with Visa.", "div": "bank", "rev": "corporate", "products": [
            P("dtenge", "Digital tenge", "Halyk and Visa issued the first card linked to the digital tenge (first payment November 2023); digital-tenge services in Onlinebank for businesses. Over KZT 340 billion of digital tenge had been issued by July 2026.",
              s=["con", "corp"], lc="move", st="new", ay="Nov 2023", o="P", at="Visa", neo=[0, "Visa."],
              src=[["ForkLog: digital-tenge card, Nov 2023", DTCARD], ["Annual report 2025", AR25], ["Kazinform: interbank QR, Jul 2026", IMTPS]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: an AI-assisted fraud hub tied to the National Bank's anti-fraud centre, Halyk ID and voice biometrics, an AI agent platform in the making, and Halyk Club and Halyk+ bonuses for 2 million users.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud", "blurb": "AI agents watch transactions.", "div": "bank", "rev": "retail", "products": [
            P("fraud", "Anti-fraud hub", "A single anti-fraud platform across the ecosystem, with RPA and AI agents monitoring applications and transactions, money-mule detection, and data-sharing with other banks and the National Bank's Anti-Fraud Centre.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, "Halyk's own."],
              mc="Most Kazakh payments are account-to-account, where card-network fraud tools do not reach yet.",
              src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Identity & APIs", "blurb": "Halyk ID, voice, BaaS.", "div": "bank", "rev": "retail", "products": [
            P("halykid", "Halyk ID & biometrics", "Halyk ID single sign-on across Kino.kz, Halyk Life and Halyk Market (the first such scheme in Kazakhstan, Halyk says), voice biometrics in the call centre, and Face ID and Touch ID in the app.",
              s=["con"], lc="open", o="B", neo=[0, ""], src=[["Halyk ID", HID], ["Halyk: voice biometrics", VOICE]]),
            P("baas", "BaaS & APIs", "Banking-as-a-service for partners, Onlinebank API links to accounting systems, and open-banking onboarding through other banks' APIs at Halyk Bank Georgia.",
              s=["sme", "corp"], lc="open", o="B", neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "Data & AI", "blurb": "An AI agent platform.", "div": "group", "rev": "other", "products": [
            P("ai", "AI agents & LLMs", "AI tax recommendations for small firms, an AI chatbot at Halyk Life, AI agents in fraud monitoring, and an AI agent platform and bank-scale LLM service presented at OIY Tech in October 2026. Kaspi launched its Kasper AI shopping assistant in July 2026.",
              s=["con", "sme"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="Agent Pay is untouched ground as Halyk builds agents and Kaspi launches Kasper.",
              src=[["Halyk OIY Tech 2026", OIY], ["Annual report 2025", AR25], ["Kaspi.kz 2Q 2026 results", KASPI]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Loyalty", "blurb": "Halyk+ for 2 million.", "div": "bank", "rev": "retail", "products": [
            P("loyalty", "Halyk Club & Halyk+", "Halyk Club bonuses of up to 30% with partners such as Sulpak, Magnum and Air Astana's Nomad, and Halyk+, a tiered, gamified programme launched in 2025 (1% base, up to 10%) that grew from 196,000 to 2.05 million users between August and December 2025.",
              s=["con", "prem"], lc="grow", st="new", o="B", neo=[0, "Halyk's own."],
              mc="Card-linked offers and Mastercard benefits could plug into Halyk+.",
              src=[["Halyk Club", CLUB], ["Annual report 2025", AR25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: KZT 4.8 trillion of retail loans and 27% of retail deposits, nearly half of corporate lending, a fast-growing SME book with OnlineDuken, the leading life insurer, a lifestyle ecosystem, and banks in Uzbekistan and Georgia.",
    "tiles": [
        {"id": "4.1", "ic": "hand-coins", "name": "Retail lending & deposits", "blurb": "KZT 4.8trn loans, 26.9% of deposits.", "div": "bank", "rev": "retail", "products": [
            P("retaillending", "Retail loans", "KZT 4.8 trillion at 1 July 2026 (73.7% unsecured, 12.7% mortgages, 10.7% car loans), 1.83 million borrowers, a 17.8% market share and 88% issued digitally.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["1H 2026 presentation", H1P]]),
            P("deposits", "Retail deposits", "KZT 8.3 trillion, a 26.9% market share, 75% in tenge, with 95% of new deposits opened digitally in 1H 2026.",
              s=["saver"], lc="grow", o="B", neo=[0, ""], src=[["1H 2026 presentation", H1P]]),
        ]},
        {"id": "4.2", "ic": "factory", "name": "Corporate banking", "blurb": "47.6% of real-economy lending.", "div": "bank", "rev": "corporate", "products": [
            P("corporate", "Corporate banking", "KZT 6.8 trillion of loans, 47.6% of commercial-bank lending to the real economy, 31% of corporate deposits and 86% of the country's largest taxpayers; Euromoney's best transaction bank in Kazakhstan for 2025.",
              s=["corp"], lc="borrow", o="B", neo=[0, ""], src=[["1H 2026 presentation", H1P], ["Euromoney award, Dec 2025", EURO]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "SME & OnlineDuken", "blurb": "SME loans +24.7%.", "div": "bank", "rev": "sme", "products": [
            P("sme", "SME banking", "KZT 2.4 trillion of loans (+24.7% year on year), 93% issued digitally, digital bid and performance bonds, and lending to merchants on their acquiring data.",
              s=["sme", "merch"], lc="borrow", o="B", neo=[0, ""], src=[["1H 2026 presentation", H1P], ["Annual report 2025", AR25]]),
            P("bizcards", "Business, fuel & customs cards", "Business, digital, self-cash-in, sole-proprietor, customs and fuel cards ordered in Onlinebank, sold as 'the widest choice of payment systems in one bank'; networks not itemised ⚠.",
              s=["sme"], lc="everyday", o="B", neo=[None, "Networks not stated."],
              mc="Commercial and fuel cards for 514,000 business clients are open ground.",
              src=[["Halyk: business cards", BIZCARDS]]),
            P("onlineduken", "OnlineDuken", "A B2B platform linking corner shops to distributors for ordering, delivery and payment: 2Q 2026 GMV KZT 68.9 billion (+35.6%) and 18,800 stores, nudging merchants to Halyk payments.",
              s=["merch"], lc="beyond", st="new", o="B", neo=[0, ""], src=[["1H 2026 presentation", H1P], ["1H 2026 call", H1T]]),
        ]},
        {"id": "4.4", "ic": "shield-check", "name": "Insurance & investments", "blurb": "Life insurer number one.", "div": "ins", "rev": "other", "products": [
            P("insurance", "Halyk Life & Halyk Insurance", "Halyk Life leads life insurance with a 42.8% share; Halyk Insurance sells general and car insurance, largely through the Super-App.",
              s=["saver"], lc="grow", o="B", neo=[0, ""], src=[["Annual report 2025", AR25]]),
            P("invest", "Halyk Invest, Halyk Finance & Halyk Leasing", "Retail brokerage with direct access to KASE and AIX, investment banking at Halyk Finance, and Halyk Leasing (portfolio +69% in 2025).",
              s=["saver", "corp"], lc="grow", o="B", neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "4.5", "ic": "sparkles", "name": "Lifestyle ecosystem", "blurb": "Market, Travel, GovTech.", "div": "life", "rev": "retail", "products": [
            P("lifestyle", "Halyk Market, Travel & lifestyle", "Halyk Market (since December 2020), Halyk Travel, Kino.kz, Airba Fresh e-grocery (November 2025), Kundelik education, e-pharmacy and government services inside the Super-App.",
              s=["con"], lc="beyond", o="B", neo=[0, ""], src=[["Annual report 2025", AR25], ["1H 2026 presentation", H1P]]),
        ]},
        {"id": "4.6", "ic": "earth", "name": "International", "blurb": "Uzbekistan and Georgia.", "div": "tenge", "rev": "other", "products": [
            P("tenge", "Tenge Bank (Uzbekistan)", "Founded 2019 as Uzbekistan's first foreign-owned bank after reforms; the base for a digital and payments ecosystem there and for Kazakhstan–Uzbekistan flows; the Click partnership lapsed ⚠.",
              s=["con", "sme"], lc="move", st="flux", o="B", at="HUMO", neo=[None, "Card networks not checked."], src=[["Annual report 2025", AR25], ["Halyk and Click, Jul 2025", CLICK]]),
            P("georgia", "Halyk Bank Georgia", "An SME-focused bank with net income of GEL 22 million in 2025, ISO 20022 payments and open-banking onboarding.",
              s=["sme"], lc="everyday", o="B", neo=[None, ""], src=[["Annual report 2025", AR25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the Halyk Super-App for 8.6 million monthly users, Onlinebank for businesses, and 530 branches with partner retailers.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Halyk Super-App", "blurb": "8.6 million monthly users.", "div": "bank", "rev": "retail", "products": [
            P("superapp", "Halyk Super-App", "8.6 million monthly and 2.8 million daily users, 6.1 million transacting monthly and 11.5 million active clients (1 July 2026), with banking, Halyk QR, marketplace, travel and government services in one app.",
              s=["con", "prem", "saver"], lc="everyday", o="B", neo=[0, ""], src=[["1H 2026 presentation", H1P], ["Halyk investor site", IR]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Onlinebank", "blurb": "KZT 89.6trn in 1H.", "div": "bank", "rev": "sme", "products": [
            P("onlinebank", "Onlinebank", "317,400 monthly users and 29.4 million tenge payments worth KZT 89.6 trillion in 1H 2026 (+25.1%), with 150+ services from registration and tax to FX, payroll and acquiring.",
              s=["sme", "corp", "merch"], lc="everyday", o="B", neo=[0, ""], src=[["1H 2026 presentation", H1P], ["Annual report 2025", AR25]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & partners", "blurb": "530 outlets.", "div": "bank", "rev": "retail", "products": [
            P("branches", "Branches & ATMs", "530 branches and outlets in Kazakhstan, 17 in Uzbekistan and 9 in Georgia, with ATMs, card-issuing kiosks and QR queue tickets.",
              s=["con"], lc="open", o="B", neo=[0, ""], src=[["Halyk: about us", ABOUT], ["Annual report 2025", AR25]]),
            P("partners", "Retail partners & payroll", "Instalment partners such as Sulpak, Alser, Evrika and Mechta, and payroll projects that bring 39.3% of the employed population onto Halyk salary cards.",
              s=["con", "corp"], lc="open", o="P", neo=[0, ""], src=[["Halyk Club", CLUB], ["1H 2026 presentation", H1P]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Halyk", "blurb": "Top tier, CEO ties, Visa ahead.", "products": [
        P("mcathalyk", "Mastercard at Halyk", "Halyk issues Visa, Mastercard, UnionPay and Amex. Mastercard holds the premium top (World Elite and Imperial), an option in the basic debit pack, wallet tokens and acceptance, and the CEO sits on its Europe and EEMEA advisory boards. Visa is ahead: the digital mass card ⚠, Infinite credit, the digital-tenge card and Visa Direct transfers. Nationally Visa has 40.6 million cards to Mastercard's 14.1 million (1 June 2026).",
          s=["con"], div="group", rev="other", mc="The relationship this map is drawn for.",
          src=[["Halyk retail card tariffs, Aug 2026", TARIFF], ["NBK card statistics, Jun 2026", NBKCARDS], ["Annual report 2025", AR25]]),
    ]},
    {"id": "pillar-market", "name": "Kazakh payments", "blurb": "Kaspi, QR and instant payments.", "products": [
        P("market", "The Kazakh market", "Kaspi.kz (Payments TPV KZT 12.7 trillion in 2Q 2026, its own domestic card system and QR, pay-by-palm) is Halyk's main rival; the national instant-payment and unified QR system went nationwide on 19 July 2026; 80% of non-cash transactions already run through mobile and internet banking. Mastercard set up an Almaty hub and a Digital Country Partnership in 2023.",
          s=["con"], div="group", rev="other",
          src=[["Kaspi.kz 2Q 2026 results", KASPI], ["Kazinform: interbank QR, Jul 2026", IMTPS], ["NBK card statistics, Jun 2026", NBKCARDS], ["Forbes.kz: Mastercard hub, Sep 2023", MCHUB]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
