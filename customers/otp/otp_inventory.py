"""OTP Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the first-half 2026 report (5 August 2026), the
2Q 2026 investor presentation and the 2025 results (6 March 2026). Hungary (OTP Core) comes first; the
foreign banks are context. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product
runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1R = "https://betb3.bet.hu/newkibdata/129512153/OTP_20262Q_e_final.pdf"
PRES = "https://www.otpgroup.info/static/sw/file/OTP_Bank_Inv_Pres_2Q2026.pdf"
FY25 = "https://www.otpgroup.info/static/sw/file/OTP_20254Q_e_final.pdf"
CEO = "https://www.otpbanka.si/stability-and-renewal-in-the-management-of-otp-bank"
GF = "https://gfmag.com/?p=74326"
EM = "https://www.euromoney.com/article/bbh2sgx8ux44gokkg8o0kc8w4/awards/awards-for-excellence/cees-best-bank-for-consumers-2025-otp-bank/"
MCY = "https://otpbank.hu/portal/hu/hirek/mastercard-ev-bankja-2025"
MCY20 = "https://www.otpbank.hu/portal/hu/hirek/mastercard-ev-bankja-2020-verseny"
DEBIT = "https://www.otpbank.hu/portal/hu/bankkartyak/beteti-kartya"
CREDIT = "https://www.otpbank.hu/portal/hu/hitelkartyak"
CCT = "https://www.otpbank.hu/static/portal/sw/file/Hitelkartya_H_20170717_utani_20260701.pdf"
ACC = "https://www.otpbank.hu/static/portal/sw/file/Tajekoztato-kartyaelfogadashoz-20250701.pdf"
APAY = "https://xpatloop.com/channels/2019/05/apple-pay-arrives-in-hungary.html"
WAL = "https://xpatloop.com/channels/2023/09/largest-commercial-bank-of-hungary-introduces-new-payment-methods.html"
MNB = "https://xpatloop.com/channels/2025/07/analysis-electronic-payments-rise-steeply-in-hungary-is-cash-dying.html"
QVIK = "https://xpatloop.com/channels/2024/07/new-instant-payment-service-qvik-gearing-up-in-hungary.html"
QVIK26 = "https://www.portfolio.hu/cimke/qvik"
SPAY = "https://www.economx.hu/gazdasag/2024/08/27/simplepay-otp-bank-pos-terminal-bankkartya-fizetes-795209/"
SHOP = "https://apps.shopify.com/simplepay"
SZEP = "https://tudastar.money.hu/hir/20251029/otp-szep-kartya-digitalis-virtualis-mobilfizetes/"
OTPAY = "https://www.paymentsdive.com/ex/mpt/news/masterpass-enabled-mobile-wallet-launched-by-cellum-otp-bank-hungary"
NFCW = "https://www.nfcw.com/tag/otp-bank/"
DSKV = "https://dskbank.bg/en/visa"
IPOC = "https://www.ipotekabank.uz/en/plastic-cards"
LUM = "https://www.fintechfutures.com/m-a/otp-bank-to-acquire-luminor"
SRB = "https://n1info.rs/biznis/otp-banka-u-velikoj-globalnoj-akciji-posumljavanja-2/"
MDA = "https://www.otpbank.md/en/publication/news-112"
UKR = "https://dengi.ua/articles/1704832-otp-bank-udostoilsya-nagrady-mastercard-za-effektivnye-ko-brend-programmy-html"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · reach", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: HUF 46.7 trillion of assets and a 21.6% return in 2025, a Budapest listing with no strategic owner, the Csányis at the top, 11 countries and 17.5 million customers, its own AI, and Luminor on the way.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "ROE 21.6% in 2025.", "div": "otpg", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of HUF 46.7 trillion (about €118 billion), gross loans of HUF 27.5 trillion and deposits of HUF 33.7 trillion at 30 June 2026; profit after tax of HUF 482.7 billion in the half (HUF 580.3 billion with special taxes spread evenly) and HUF 1,146 billion in 2025 (ROE 21.6%); CET1 17.6%; market value €36.2 billion; rated BBB (S&P), Baa1 deposits (Moody's) and BBB+ (Scope).",
              s=["corp"], neo=[0, ""], src=[["OTP: first-half 2026 report", H1R], ["OTP: 2025 results", FY25], ["Global Finance: Péter Csányi, May 2026", GF]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & owners", "blurb": "Csányi and Csányi.", "div": "otpg", "rev": "group", "products": [
            P("leadership", "Board, executives & owners", "Dr Sándor Csányi, chairman since 1992 and CEO for 33 years, handed the CEO role to Péter Csányi, former head of the Digital Division, on 1 May 2025. Deputy CEOs include László Wolf, András Becsei (retail), László Bencsik, György Kiss-Haypál and András Sebők. Listed in Budapest since 1995, with no strategic investor; about 48% held by foreign institutions, with MOL, Groupama and staff share plans among the rest ⚠ exact stakes.",
              s=["corp"], neo=[0, ""], src=[["OTP: management renewal, Apr 2025", CEO], ["OTP: first-half 2026 report", H1R], ["OTP: 2Q 2026 presentation", PRES]]),
        ]},
        {"id": "1.3", "ic": "earth", "name": "Group footprint", "blurb": "11 countries, 17.5m customers.", "div": "otpg", "rev": "foreign", "products": [
            P("footprint", "Eleven countries", "About 17.5 million active customers in Hungary, Bulgaria, Slovenia, Croatia, Serbia, Montenegro, Albania, Moldova, Ukraine, Russia and Uzbekistan, with 1,177 branches, 5,619 ATMs and 41,089 staff at 30 June 2026; more than 70% of 2025 profit came from outside Hungary, with Russia still contributing HUF 106 billion in the half.",
              s=["con", "abroad"], neo=[0, ""], src=[["OTP: 2Q 2026 presentation", PRES], ["OTP: first-half 2026 report", H1R], ["Global Finance: Péter Csányi, May 2026", GF]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "Technology & AI", "blurb": "80–90% of loans decided by models.", "div": "otpg", "rev": "group", "products": [
            P("tech", "AI, data & technology", "Machine-learning models decide 80–90% of consumer loans; AI intent recognition in chat and voice; automated document and complaint handling; generative AI and large language models being scaled in 2026; an in-house futurology team and fintech partnerships.",
              s=["con", "corp"], st="new", neo=[0, "OTP's own."], src=[["Global Finance: Péter Csányi, May 2026", GF], ["OTP: first-half 2026 report", H1R]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Luminor signed July 2026.", "div": "otpg", "rev": "group", "products": [
            P("strategy", "Strategy & 2026 guidance", "Stability, growth, innovation and profitability; grow share everywhere organically and by acquisition, and lead retail banking in Uzbekistan. 2026 guidance: loan growth about 15%, margin above 4.34%, ROE below 2025's 21.6%. Deals since 2020: Alpha Bank Albania (2022 ⚠), Nova KBM and Ipoteka Bank (2023), OTP Bank Romania sold (July 2024).",
              s=["corp"], neo=[0, ""], src=[["OTP: first-half 2026 report", H1R], ["OTP: 2025 results", FY25]]),
            P("luminor", "Luminor", "Agreement of 20 July 2026 to buy all of Luminor, number three in the Baltics with about 12% of loans, from Blackstone funds and DNB at below book value; adds about 13% to group assets and takes eurozone loans from 42% to 50%. Awaiting approvals.", short="Luminor (pending)",
              s=["abroad"], lc="open", st="new", ay="Jul 2026", o="A", neo=[None, "Luminor's networks not researched ⚠."],
              mc="A Baltic card portfolio whose network will be reviewed under new owners.",
              src=[["OTP: first-half 2026 report", H1R], ["OTP: 2Q 2026 presentation", PRES], ["FinTech Futures: OTP to buy Luminor, Jul 2026", LUM]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "How money moves: a Hungarian card range that is mostly Mastercard with two Visa debit cards and Visa Infinite, Bonus credit cards, Apple Pay and Google Pay, SZÉP cards, 150,000 POS terminals and SimplePay, qvik instant payments, and foreign banks where Visa has won Bulgaria.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "Mostly Mastercard, two Visa.", "div": "otp", "rev": "core", "products": [
            P("debit", "OTP debit cards", "Mastercard Online, Standard, Standard OKÉ, Gold, Prémium and a EUR card, alongside Visa Online and Visa Classic, for almost 4 million Hungarian customers. No split by network is published ⚠.", short="Debit (mostly Mastercard)",
              s=["con", "young"], lc="everyday", o="B", at="Mastercard, Visa", neo=[1, "Mostly Mastercard; Visa Online and Classic too."],
              mc="Hungary's largest card book, and Mastercard carries most of its range.",
              src=[["OTP: debit cards", DEBIT], ["Euromoney: CEE best bank for consumers, Jul 2025", EM]]),
            P("worldelite", "Private Banking World Elite", "Mastercard World Elite debit cards for private-banking and key private-banking clients.",
              s=["priv"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard World Elite."], src=[["OTP: debit cards", DEBIT]]),
            P("vcard", "Virtual cards", "The Mastercard webKÁRTYA for online shopping, and a virtual card pushed to the phone wallet in under 10 minutes at selfie- and NFC-based account opening.",
              s=["young"], lc="open", o="B", neo=[1, "webKÁRTYA on Mastercard; onboarding card's network not stated ⚠."],
              src=[["OTP: debit cards", DEBIT], ["Euromoney: CEE best bank for consumers, Jul 2025", EM]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Bonus on Mastercard.", "div": "otp", "rev": "core", "products": [
            P("bonus", "OTP Bonus & BonusGold", "Cashback credit cards on Mastercard ⚠ returning up to HUF 30,000 and HUF 50,000 a year, for net incomes from HUF 214,000 and HUF 300,000 a month (terms from 1 July 2026), with instalment purchases; Mastercard Arany and Klasszik and Visa Klasszik are no longer sold.", short="Bonus (Mastercard)",
              s=["con"], lc="borrow", o="B", at="Mastercard", neo=[2, "Bonus Mastercard ⚠."],
              src=[["OTP: credit cards", CREDIT], ["OTP: credit-card terms, Jul 2026", CCT]]),
            P("visainf", "Visa Infinite", "The top credit card for private-banking clients is a Visa.",
              s=["priv"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["OTP: credit cards", CREDIT]]),
            P("cobrand", "Telekom & Otthon credit cards", "A Telekom card with up to HUF 50,000 a year off devices and 24-month interest-free instalments, and an Otthon (home) card for mortgage holders with interest-free instalments on home purchases; network not stated ⚠.",
              s=["con", "home"], lc="borrow", o="P", at="Magyar Telekom", neo=[None, "Network not stated ⚠."], src=[["OTP: credit cards", CREDIT]]),
        ]},
        {"id": "2.3", "ic": "smartphone", "name": "Mobile wallets", "blurb": "First with Apple Pay.", "div": "otp", "rev": "core", "products": [
            P("wallets", "Apple Pay, Google Pay, Garmin Pay & Xiaomi Pay", "OTP was Hungary's only Apple Pay bank at launch in May 2019 (60,000 clients in ten days) and added Google Pay, Garmin Pay and Xiaomi Pay on 5 September 2023, for Mastercard and Visa, debit and credit.",
              s=["con", "young"], lc="everyday", ay="May 2019", o="P", at="Apple, Google", neo=[1, "Tokens for both networks."],
              src=[["XpatLoop: Apple Pay in Hungary, May 2019", APAY], ["XpatLoop: new payment methods, Sep 2023", WAL]]),
            P("otpay", "OTPay with Masterpass", "In March 2014 OTP became the first European bank to build Mastercard's Masterpass into its wallet (built by Cellum), after joining Mastercard's NFC alliance in 2011; it grew into the Simple app ⚠.",
              s=["con"], lc="move", st="retired", ay="Mar 2014", o="P", at="Mastercard, Cellum", neo=[3, "Masterpass, since retired."],
              src=[["Payments Dive: OTPay with Masterpass, Mar 2014", OTPAY], ["NFCW: OTP Bank", NFCW]]),
        ]},
        {"id": "2.4", "ic": "gift", "name": "SZÉP card", "blurb": "HUF 425bn spent in 2025.", "div": "otp", "rev": "core", "products": [
            P("szep", "OTP SZÉP Card", "Hungary's tax-favoured employee leisure card, issued by OTP itself since 1 January 2025; more than HUF 425 billion spent in 2025 ⚠; a digital card in Google Wallet and, from 28 October 2025, Apple Wallet. Network not stated ⚠.",
              s=["con", "sme"], lc="everyday", st="new", ay="Oct 2025", o="B", neo=[None, "Network not stated ⚠."],
              src=[["Money.hu: digital SZÉP card, Oct 2025", SZEP]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "150,000 terminals, SimplePay.", "div": "mobil", "rev": "core", "products": [
            P("pos", "OTP card acceptance", "About 150,000 POS terminals in Hungary (287,000 across the group) accepting Mastercard, Maestro, Visa, V Pay and American Express, with online merchant onboarding since January 2024.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."],
              mc="The largest acceptance network in Hungary.",
              src=[["OTP: first-half 2026 report", H1R], ["OTP: card-acceptance notice, Jul 2025", ACC], ["Euromoney: CEE best bank for consumers, Jul 2025", EM]]),
            P("simplepay", "SimplePay", "OTP Mobil's online payment gateway (1.9–2.6% on Shopify) and phone terminal; merchants on the phone terminal grew about 23% in Q2 2024. A leading Hungarian gateway ⚠ share unverified.",
              s=["sme"], lc="move", o="B", neo=[1, "Takes all cards; qvik too."],
              src=[["Economx: SimplePay and POS data, Aug 2024", SPAY], ["Shopify: SimplePay", SHOP]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Instant payments", "blurb": "qvik and money requests.", "div": "mobil", "rev": "core", "products": [
            P("qvik", "qvik & money requests", "The central bank's qvik QR and NFC payments (from September 2024, with OTP Mobil the first to offer them) on Hungary's instant-payment system; OTP's NFC and QR money requests have carried more than HUF 25 billion, mostly for 16–30-year-olds.",
              s=["young", "sme"], lc="move", st="new", ay="Sep 2024", o="B", neo=[0, "Account-to-account."],
              mc="qvik spares merchants card fees of up to about 1.5%.",
              src=[["Economx: SimplePay and POS data, Aug 2024", SPAY], ["XpatLoop: qvik, Jul 2024", QVIK], ["Portfolio: qvik, Sep 2026", QVIK26]]),
        ]},
        {"id": "2.7", "ic": "globe", "name": "Cards abroad", "blurb": "DSK moves to Visa.", "div": "dsk", "rev": "foreign", "products": [
            P("dskcards", "DSK Bank cards", "Bulgaria's DSK Bank, the group's biggest foreign earner, is replacing all its Mastercards with Visa under a strategic partnership; each Mastercard is switched off a week after the new Visa is activated. Start date not found ⚠.", short="DSK (Mastercard to Visa)",
              s=["abroad"], lc="everyday", st="flux", o="P", at="Visa", neo=[1, "Mastercard until reissued, then Visa."],
              mc="The defining loss in the group.",
              src=[["DSK Bank: Visa partnership", DSKV]]),
            P("ipocards", "Ipoteka Bank cards", "Domestic Humo and Uzcard, co-badged Humo-Visa and Humo-Mastercard, Mastercard Standard and Gold and Visa Gold in Uzbekistan.",
              s=["abroad"], lc="everyday", o="P", at="Humo, Uzcard", neo=[1, "Shared with Visa and domestic schemes."], src=[["Ipoteka Bank: cards", IPOC]]),
            P("cardsabroad", "Ukraine, Moldova & Serbia", "Mastercard co-brand programmes in Ukraine, a Mastercard service-excellence award in Moldova and a joint campaign in Serbia, where card-scheme incentives lifted fees 22% in 2025 ⚠ dates of the awards.",
              s=["abroad"], lc="everyday", o="P", at="Mastercard, Visa", neo=[1, "Both networks ⚠."],
              src=[["Dengi.ua: Mastercard award, OTP Ukraine", UKR], ["OTP Moldova: Mastercard award", MDA], ["N1: OTP Serbia and Mastercard", SRB], ["OTP: 2025 results", FY25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: OTP's own deep-learning fraud model and prize-winning cyber work, AI in service and lending, open-banking duties, and a cashback programme with about 100 merchants.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & cyber", "blurb": "Own deep-learning model.", "div": "otpg", "rev": "group", "products": [
            P("fraud", "Fraud prevention & cybersecurity", "A proprietary deep-learning model for real-time fraud prevention against AI-enabled fraud; first prize for cybersecurity programme of the year at Mastercard's Bank of the Year 2025.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, "OTP's own."],
              mc="Network-level scam and identity scoring could sit beside OTP's model.",
              src=[["Global Finance: Péter Csányi, May 2026", GF], ["OTP: Mastercard Bank of the Year 2025", MCY]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & data", "blurb": "Chat, voice, personal offers.", "div": "otp", "rev": "core", "products": [
            P("ai", "AI service & personalisation", "AI intent recognition in chat and voice, automated loan decisions and data-driven offers; third place for AI innovation at Mastercard's Bank of the Year 2025.",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, "OTP's own."],
              mc="No agentic payments yet; Agent Pay is untouched ground.",
              src=[["Global Finance: Péter Csányi, May 2026", GF], ["OTP: Mastercard Bank of the Year 2025", MCY]]),
            P("openbank", "Open banking & APIs", "PSD2 access duties apply in Hungary and the EU subsidiaries; no OTP open-banking product was found ⚠.",
              s=["sme", "corp"], lc="move", st="unconf", neo=[None, "Nothing public."], src=[["OTP: first-half 2026 report", H1R]]),
        ]},
        {"id": "3.3", "ic": "coins", "name": "Loyalty", "blurb": "Cashback at 100 merchants.", "div": "otp", "rev": "core", "products": [
            P("loyalty", "OTP Kedvezményprogram", "Uncapped cashback at nearly 100 partner merchants on any OTP debit or credit card, paid monthly, plus Bonus card cashback and a 10% welcome offer.",
              s=["con"], lc="grow", o="B", neo=[0, "OTP's own, on both networks."],
              mc="Card-linked offers could widen it beyond 100 merchants.",
              src=[["OTP: credit cards", CREDIT]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: about 40% of Hungarian retail deposits, a third of new mortgages, more than 40% of new cash loans, record corporate share, Merkantil leasing and OTP funds, private banking, and ten foreign banks led by DSK.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Accounts & savings", "blurb": "About 40% of retail deposits.", "div": "otp", "rev": "core", "products": [
            P("accounts", "Current accounts & deposits", "About 40% of Hungarian retail deposits and 30% of banking assets; household deposits grew 9% in the first quarter of 2026.",
              s=["con"], lc="everyday", o="B", neo=[1, "Debit mostly Mastercard."], src=[["OTP: 2Q 2026 presentation", PRES], ["OTP: first-half 2026 report", H1R]]),
            P("piggy", "Virtual Piggy Bank", "Round-up micro-savings with 342,000 accounts (2025).",
              s=["young"], lc="grow", o="B", neo=[0, ""], src=[["Euromoney: CEE best bank for consumers, Jul 2025", EM]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Mortgages & loans", "blurb": "A third of new mortgages.", "div": "otp", "rev": "core", "products": [
            P("mortgage", "Mortgages & Home Start", "About a third of new Hungarian mortgage contracts; mortgages up 17% at OTP Core in the half, driven by the subsidised Home Start Programme (about 21,150 clients this year, average HUF 34 million).",
              s=["home"], lc="borrow", o="B", neo=[0, ""], src=[["OTP: 2Q 2026 presentation", PRES]]),
            P("cashloan", "Cash, baby & workers' loans", "More than 40% of new cash loans and baby loans; cash-loan contracts up 51% year on year in Q2 2026, mostly decided by models and paid out in minutes.",
              s=["con", "home"], lc="borrow", o="B", neo=[0, ""], src=[["OTP: 2Q 2026 presentation", PRES], ["Euromoney: CEE best bank for consumers, Jul 2025", EM]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Business & corporate", "blurb": "Record corporate share.", "div": "otp", "rev": "core", "products": [
            P("msme", "Micro & small business", "Micro and small-business loans up 14% in the first half of 2026, helped by subsidised Széchenyi Card MAX+ loans.",
              s=["sme"], lc="borrow", o="B", neo=[0, ""],
              mc="No commercial or purchasing card programme found ⚠.",
              src=[["OTP: first-half 2026 report", H1R]]),
            P("corporate", "Corporate banking", "About 22% of Hungarian corporate loans, an all-time high, and 21% of corporate deposits.",
              s=["corp"], lc="borrow", o="B", neo=[0, ""], src=[["OTP: 2Q 2026 presentation", PRES]]),
        ]},
        {"id": "4.4", "ic": "gem", "name": "Leasing, funds & private", "blurb": "Merkantil, OTP Funds.", "div": "merkantil", "rev": "husubs", "products": [
            P("merkantil", "Merkantil leasing", "Car and equipment finance and leasing in Hungary, with leasing growing 6% across the group in Q2 2026.",
              s=["sme", "con"], lc="borrow", o="B", neo=[0, ""], src=[["OTP: first-half 2026 report", H1R]]),
            P("funds", "OTP Fund Management", "About 31% of Hungarian asset management.",
              s=["con", "priv"], lc="grow", o="B", neo=[0, ""], src=[["OTP: 2Q 2026 presentation", PRES]]),
            P("privbank", "Private banking", "Private and key private-banking clients, with Mastercard World Elite debit and Visa Infinite credit cards.",
              s=["priv"], lc="grow", o="B", neo=[1, "World Elite debit; Visa Infinite credit."], src=[["OTP: debit cards", DEBIT], ["OTP: credit cards", CREDIT]]),
        ]},
        {"id": "4.5", "ic": "flag", "name": "Banks abroad", "blurb": "Ten foreign banks.", "div": "otpg", "rev": "foreign", "products": [
            P("dsk", "DSK Bank (Bulgaria)", "The group's largest foreign bank: HUF 103 billion profit in the first half of 2026, about 2.7 million clients, a 32% cost/income ratio and euro adoption in 2026.",
              s=["abroad"], lc="everyday", o="A", neo=[1, "Cards moving to Visa."], src=[["OTP: first-half 2026 report", H1R], ["Euromoney: CEE best bank for consumers, Jul 2025", EM]]),
            P("ipoteka", "Ipoteka Bank (Uzbekistan)", "Bought from the state in 2023, with the remaining state stake to follow; profit up 38% to HUF 34.6 billion in the half; OTP aims to be Uzbekistan's leading retail bank.",
              s=["abroad"], lc="everyday", o="A", neo=[1, "Humo and Uzcard plus both networks."], src=[["OTP: first-half 2026 report", H1R]]),
            P("otpbanka", "OTP banka, OBH, OTP Serbia & others", "Slovenia (OTP banka, from Nova KBM and SKB, merged August 2024), Croatia, Serbia (about 1.1 million customers), Montenegro, Albania, Moldova, Ukraine and Russia; networks not researched in detail ⚠.",
              s=["abroad"], lc="everyday", o="A", neo=[None, "Not researched ⚠."], src=[["OTP: first-half 2026 report", H1R], ["OTP: 2025 results", FY25], ["Euromoney: CEE best bank for consumers, Jul 2025", EM]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach OTP: the OTP app and internet bank, the Simple app with 3.5 million users, 299 Hungarian branches and 1,929 ATMs, and agents selling subsidised loans.",
    "tiles": [
        {"id": "5.1", "ic": "monitor", "name": "OTP app & internet bank", "blurb": "Half of customers digital.", "div": "otp", "rev": "core", "products": [
            P("app", "OTP app & internet bank", "More than half of almost 4 million Hungarian customers are digitally active; accounts open by selfie and NFC, overdrafts in one click, and digital sales aim for Europe's top quarter.",
              s=["con", "young"], lc="open", o="B", neo=[0, ""], src=[["Euromoney: CEE best bank for consumers, Jul 2025", EM], ["Global Finance: Péter Csányi, May 2026", GF]]),
        ]},
        {"id": "5.2", "ic": "rocket", "name": "Simple app", "blurb": "3.5m registered users.", "div": "mobil", "rev": "husubs", "products": [
            P("simple", "Simple by OTP", "OTP Mobil's everyday payments app, with more than 3.5 million registered users; contactless phone payments since June 2017.",
              s=["con", "young"], lc="beyond", o="B", neo=[None, "Nothing public on networks ⚠."],
              src=[["Euromoney: CEE best bank for consumers, Jul 2025", EM], ["NFCW: OTP Bank", NFCW]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & ATMs", "blurb": "299 branches in Hungary.", "div": "otp", "rev": "core", "products": [
            P("branches", "Branches & ATMs", "299 branches and 1,929 ATMs in Hungary at 30 June 2026 (1,177 and 5,619 across the group); over-the-counter cash transactions fell 38% with cash-light branches.",
              s=["con", "home"], lc="everyday", o="B", neo=[0, ""], src=[["OTP: first-half 2026 report", H1R], ["Euromoney: CEE best bank for consumers, Jul 2025", EM]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Agents & brokers", "blurb": "Selling subsidised loans.", "div": "otp", "rev": "core", "products": [
            P("agents", "Agents & brokers", "Loan agents and brokers, especially for Home Start; agent commissions rose about HUF 7 billion year on year in the first half of 2026.",
              s=["home"], lc="open", o="P", neo=[0, ""], src=[["OTP: first-half 2026 report", H1R]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at OTP", "blurb": "Hungary's main network; Bulgaria lost.", "products": [
        P("mcatotp", "Mastercard at OTP", "Mastercard carries most of OTP's Hungarian debit range, the Bonus credit cards and World Elite private-banking cards, and OTP won Mastercard's Bank of the Year in Hungary for 2020 and 2025. The ties go back to the 2011 NFC alliance and the 2014 Masterpass wallet. Visa has two entry debit cards and Visa Infinite in Hungary and is taking DSK Bank's whole portfolio in Bulgaria.",
          s=["con"], div="otpg", rev="group", mc="The relationship this map is drawn for.",
          src=[["OTP: debit cards", DEBIT], ["OTP: Mastercard Bank of the Year 2025", MCY], ["OTP: Mastercard Bank of the Year 2020", MCY20], ["DSK Bank: Visa partnership", DSKV]]),
    ]},
    {"id": "pillar-market", "name": "Hungarian banking", "blurb": "Taxes, rate caps, qvik.", "products": [
        P("market", "The Hungarian market", "Close to 10 million cards (7.4 million active), 367 million online card payments and 225 million instant payments in 2024; the central bank targets 67% electronic payments by 2030. Banks pay a windfall tax, a banking tax and a card-transaction levy, and a retail-loan rate cap was made open-ended in 2026.",
          s=["con"], div="otpg", rev="core", src=[["XpatLoop: MNB payments data, Jul 2025", MNB], ["OTP: first-half 2026 report", H1R]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
