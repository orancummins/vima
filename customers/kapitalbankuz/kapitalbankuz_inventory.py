"""Kapitalbank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

JSCB Kapitalbank of Uzbekistan, not Kapital Bank of Azerbaijan. Figures are the bank's own FY2025 results
(2 March 2026) and Central Bank league tables at 1 July 2026 unless a source says otherwise. kapitalbank.uz and
kapital24.uz were read through archived snapshots, as the live sites block scripted reads. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

FY25 = "https://www.kapitalbank.uz/ru/press_center/news/kapitalbank-podvyel-itogi-2025-goda-rost-aktivov-rekordnye-depozity-i-ukreplenie-roli-v-ekonomike/"
FY23 = "https://www.kapitalbank.uz/ru/press_center/news/chistaya-pribyl-kapitalbanka-v-2023-godu-vyrosla-na-77/"
INFO = "https://www.kapitalbank.uz/en/about/info/"
HISTORY = "https://www.kapitalbank.uz/en/about/history/"
MGMT = "https://kapitalbank.uz/en/about/management/"
COUNCIL = "https://kapitalbank.uz/en/about/council/"
STRATEGY = "https://kapitalbank.uz/en/about/strategy/"
UZUM = "https://kapitalbank.uz/en/press_center/news/jscb-kapitalbank-will-become-a-part-of-uzum-ecosystem-/"
SHAREHOLDERS = "https://kapitalbank.uz/en/press_center/news/changes-in-the-structure-of-shareholders-of-jscb-kapitalbank/"
BOARD25 = "https://www.kapitalbank.uz/en/press_center/news/jscb-kapitalbank-strengthens-its-executive-board-team/"
MOODYS = "https://www.spot.uz/ru/2026/07/02/kapitalbank/"
SP26 = "https://www.spot.uz/ru/2026/07/29/kapitalbank/"
SP25 = "https://www.spot.uz/ru/2025/07/23/kapitalbank/"
FITCH = "https://www.kapitalbank.uz/ru/press_center/news/fitch-podtverdilo-reyting-kapitalbanka-s-prognozom-pozitivnyy/"
TAF = "https://www.spot.uz/ru/2025/10/13/kapitalbank/"
CORE = "https://www.spot.uz/ru/2025/05/26/cs-kapitalbank/"
TOPEMP = "https://www.spot.uz/ru/2026/02/04/kapitalbank/"
BNY = "https://www.spot.uz/ru/2026/09/22/kapitalbank/"
BACEE = "https://www.spot.uz/ru/2026/09/23/kapitalbank-bacee/"
SIBOS = "https://www.kapitalbank.uz/ru/press_center/news/kapitalbank-prinyal-uchastie-v-mezhdunarodnom-bankovskom-forume-sibos-2025/"
LEAGUE = "https://www.uzdaily.uz/en/uzbekistan-banking-assets-exceed-1-quadrillion-soums/"
LEAGUE_JUN = "https://www.uzdaily.uz/en/assets-of-commercial-banks-in-uzbekistan-reach-9844-trillion-soums/"
VISA24 = "https://kapitalbank.uz/en/press_center/news/visa-recognizes-kapitalbank-as-the-best-bank-issuing-visa-cards-in-uzbekistan/"
VISA23 = "https://www.kapitalbank.uz/ru/press_center/news/kapitalbank-vnov-podtverdil-liderstvo-v-platezhnoy-sisteme-visa-sredi-bankov-uzbekistana/"
VISACHINA = "https://www.spot.uz/ru/2025/07/21/kapitalbank/"
VISASUBS = "https://www.kapitalbank.uz/ru/press_center/news/derzhatelyam-visa-kapitalbank-teper-dostupna-funktsiya-upravleniya-platnymi-podpiskami-cherez-mobiln/"
FIFA = "https://www.kapitalbank.uz/ru/press_center/news/est-fan-sbornaya-visa-kapitalbank-podvedeny-itogi-aktsii-k-fifa-world-cup-2026/"
PAYNET = "https://www.kapitalbank.uz/ru/press_center/news/karty-visa-kapitalbank-sum-teper-mozhno-popolnit-vo-vsekh-tochkakh-paynet/"
MCDRAW = "https://www.kapitalbank.uz/ru/press_center/news/karty-mastercard-kapitalbank-vash-shans-vyigrat-puteshestviya-v-yaponiyu-vengriyu-i-na-maldivy/"
MCCASHBACK = "https://kapitalbank.uz/en/press_center/news/travel-profitably-with-mastercard-kapitalbank/"
MCMULTINEWS = "https://kapitalbank.uz/en/press_center/news/mastercard-kapitalbank-multicurrency-cards-for-travel-convenience-and-savings/"
MCOFFERS = "https://anhor.uz/ru/reklama/mastercard-kapitalbank-skidki-yeda-taksi-bilety1"
MCTENDER = "https://kapitalbank.uz/ru/press_center/tenders/last/akb-kapitalbank-obyavlyaet-tender-na-postavku-mezhdunarodnykh-platezhnykh-kart-mastercard-v-koliches/"
CARDS = "https://www.kapital24.uz/en/plastic-cards/list/"
MCBLACK = "https://kapital24.uz/en/plastic-cards/list/premium-cards/mastercard-black-edition/"
MCWE = "https://kapital24.uz/en/plastic-cards/list/premium-cards/mastercard-world-elite-metal-edge/"
MCMULTI = "https://kapital24.uz/en/plastic-cards/list/multi-currency-cards/mastercard-black-edition-multi-currency/"
BRAILLE = "https://kapital24.uz/en/plastic-cards/list/inclusive-cards/mastercard-sum-width-braile-font/"
VISASUM = "https://kapital24.uz/en/plastic-cards/list/uzs/visa-sum/"
HUMO = "https://www.kapital24.uz/en/plastic-cards/list/uzs/humo/"
MONEYSEND = "https://www.kapital24.uz/en/money-transfer/moneysend/"
VISADIRECT = "https://kapital24.uz/en/money-transfer/visa-direct/"
APP = "https://www.kapital24.uz/en/plastic-cards/info/kapitalbank-mobile-app/"
APPUPD = "https://www.kapitalbank.uz/en/press_center/news/mobile-app-update/"
WU = "https://www.kapitalbank.uz/ru/press_center/news/-50-western-union-kapitalbank-online/"
LOANS = "https://www.kapital24.uz/en/crediting/"
UZAUTO = "https://kapital24.uz/ru/crediting/kapitalbankdan-uzauto-nasiya/"
CORPCARDS = "https://www.kapitalbank.uz/en/corporate/plastic-cards/list/"
MCBIZ = "https://www.kapitalbank.uz/en/corporate/plastic-cards/list/mastercard-business/mastercard-business/"
ACQ = "https://kapitalbank.uz/en/corporate/services/merchant-acquiring/"
ECOM = "https://kapitalbank.uz/en/corporate/internet-banking/e-commerce/"
UZBIZ = "https://www.kapitalbank.uz/en/corporate/internet-banking/uzum-business/"
KAPI = "https://www.kapitalbank.uz/en/corporate/services/kapital-api/"
CASHLESS = "https://www.spot.uz/ru/2026/07/02/kapitalbank-online/"
SELFCOLLECT = "https://www.spot.uz/ru/2026/07/22/kapital-cash-collection/"
SAFETY = "https://www.spot.uz/ru/2026/07/29/kapitalbank-safety/"
FACTORING = "https://www.spot.uz/ru/2026/08/26/kapitalbank-growth/"
ACCOUNT = "https://www.spot.uz/ru/2026/06/10/current-account/"
ITPARK = "https://kapitalbank.uz/en/press_center/news/kapitalbank-and-it-park-sign-strategic-cooperation-memorandum/"
UZCARDAWARD = "https://www.kapitalbank.uz/en/press_center/news/kapitalbank-becomes-the-leader-in-corporate-business-development-according-to-uzcard/"
EMBRAS = "https://www.kapitalbank.uz/ru/press_center/news/kapitalbank-stal-pobeditelem-mezhdunarodnoy-premii-embras-2025/"
UZUMVISA = "https://uzum.com/en/press-center/news-and-press-releases/uzum-bank-visa-for-all/"
UZUM5M = "https://www.spot.uz/ru/2026/03/11/uzum-bank/"
UZUMRAISE = "https://www.aap.com.au/aapreleases/cision20250805ae44452"
UZUMBANKCAP = "https://www.spot.uz/ru/2024/10/25/uzum-bank/"
QR = "https://kun.uz/en/news/2026/04/18/central-bank-approves-regulations-for-unified-qr-code-payment-system"
WALLETS = "https://timesca.com/apple-pay-and-google-pay-mobile-wallets-could-launch-in-uzbekistan-within-months/"
CARDS68 = "https://kun.uz/en/news/2026/02/09/cashless-transactions-surge-as-bank-card-usage-rises-across-uzbekistan"
HUMOUP = "https://humocard.uz/en/press_center/news/humo-expands-international-partnership/"
MCOFFICE = "https://m.kun.uz/en/news/2023/05/16/mastercard-to-open-its-representative-office-in-uzbekistan"
XALQ = "https://kun.uz/en/news/2026/05/07/jsc-xalq-bank-strengthens-strategic-partnership-with-mastercard"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · Uzum · core", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: UZS 62.7 trillion of assets and the country's biggest retail deposit book, an ROE of 28.9%, Moody's Ba3, majority ownership by the Uzum group since 2022, a new core system and its own card processing.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & ratings", "blurb": "Largest private bank; Ba3.", "div": "kb", "rev": "treasury", "products": [
            P("balance", "Balance sheet & earnings", "FY2025: assets UZS 57.1 trillion ($4.75 billion, up 21.3%), loans UZS 36.8 trillion, retail deposits UZS 25.7 trillion and corporate deposits UZS 19.5 trillion; net profit UZS 1.94 trillion ($156 million, up 7.2%), ROE 28.9%, ROA 3.7%, cost:income 35.8%, NPLs 4.9%.",
              s=["con"], neo=[0, ""], src=[["Kapitalbank: 2025 results, 2 Mar 2026", FY25]]),
            P("rank", "Market position", "UZS 62.7 trillion of assets at 1 July 2026, the largest bank without a state share and about 6% of the system; third by deposits and first in retail deposits (UZS 28.1 trillion), ahead of every state bank; systemically important for a second year.",
              s=["con", "corp"], neo=[0, ""], src=[["UzDaily: bank assets, Jul 2026", LEAGUE], ["UzDaily: bank assets at 1 June 2026", LEAGUE_JUN]]),
            P("ratings", "Credit ratings", "Moody's Ba3 deposit ratings, stable (upgraded from B1, 2 July 2026); S&P BB-/B, outlook positive (July 2026); Fitch B, positive (July 2025); national uzA+.",
              s=["corp"], st="new", ay="Jul 2026", neo=[0, ""], src=[["Spot: Moody's Ba3, Jul 2026", MOODYS], ["Spot: S&P outlook positive, Jul 2026", SP26], ["Kapitalbank: Fitch, Jul 2025", FITCH]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "Uzum-owned since 2022.", "div": "uzum", "rev": "treasury", "products": [
            P("ownership", "Uzum ownership", "Finance TCI, part of the Uzum group's Djuzum SPV, bought 50% on the exchange in December 2022 for UZS 787 billion, taking 61.54%; Russia's Telecominvest left. Uzum raised about $70 million from Tencent and VR Capital in August 2025 at about $1.5 billion.",
              s=["corp"], o="A", ay="Dec 2022", neo=[0, ""], src=[["Kapitalbank: part of Uzum, Jan 2023", UZUM], ["Kapitalbank: shareholder change, Jan 2023", SHAREHOLDERS], ["Uzum: $70m round, Aug 2025", UZUMRAISE]]),
            P("leadership", "Boards", "Supervisory Board chaired by Maksud Abdusamadov; Management Board chaired by Kirill Maevskiy (since January 2023), with First Deputy Sardor Ismailov, Konstantin Tyan (corporate), Ulugbek Tavakkalov (retail, 2025) and Ekaterina Enikeeva (finance) ⚠ board as at 2025 snapshots.",
              s=["corp"], neo=[0, ""], src=[["Kapitalbank: management", MGMT], ["Kapitalbank: supervisory board", COUNCIL], ["Kapitalbank: board expanded, Feb 2025", BOARD25]]),
            P("heritage", "Heritage & Apelsin", "Licensed in April 2001 as one of the first private banks; merged with Aviabank in 2004. It built the Apelsin app, which became Uzum Bank in November 2022 and is now a separately capitalised sister bank ⚠ separation date.",
              s=["con"], o="I", st="retired", neo=[0, ""], src=[["Kapitalbank: history", HISTORY], ["Spot: Uzum Bank capital, Oct 2024", UZUMBANKCAP]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Core & processing", "blurb": "CS B2 core, own card switch.", "div": "kb", "rev": "treasury", "products": [
            P("core", "Core banking & card processing", "Moved fully to CS's 'B2' core in February 2025, linked to four processing centres: Uzcard domestic and international, HUMO, and the bank's own Tieto-based centre for international cards; about 500,000 issuing and 250,000 acquiring transactions a day.",
              s=["con", "merch"], o="P", at="CS, Tieto", ay="Feb 2025", neo=[0, "Own processing for Visa and Mastercard cards."],
              mc="Kapitalbank switches its own Mastercard transactions, so token and fraud services plug in at the bank.",
              src=[["Spot: CS core migration, May 2025", CORE]]),
            P("people", "People & AI learning", "About 4,000 staff; Top Employer for a third year (2026); Kapital People learning app with AI-built courses won EMBRAS 2025 gold.",
              s=["corp"], neo=[0, ""], src=[["Spot: Top Employer, Feb 2026", TOPEMP], ["Kapitalbank: EMBRAS 2025, Oct 2025", EMBRAS]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & reach", "blurb": "SME growth, global links.", "div": "kb", "rev": "corporate", "products": [
            P("strategy", "Strategy for 2026", "Steady growth, stronger capital, more business and SME lending and less reliance on car loans, digital services and service quality; the last published plan ran to 2023 ⚠.",
              s=["corp", "sme"], neo=[0, ""], src=[["Kapitalbank: 2025 results, Mar 2026", FY25], ["Spot: S&P outlook positive, Jul 2026", SP26], ["Kapitalbank: strategy", STRATEGY]]),
            P("intl", "International links", "A US-dollar correspondent account at BNY (September 2026) among 17 correspondents; BACEE member (August 2026) with Sardor Ismailov on its board; Sibos 2025 exhibitor; ISO 27001 and 27701 certified (2025).",
              s=["corp"], st="new", ay="Sep 2026", neo=[0, ""], src=[["Spot: BNY account, Sep 2026", BNY], ["Spot: BACEE, Sep 2026", BACEE], ["Kapitalbank: Sibos 2025", SIBOS]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Uzcard and HUMO cards at home, a Visa range that wins Visa's best-issuer award every year, a full Mastercard range, premium and multicurrency cards on both, acceptance of every brand plus the new UzQR, cross-border transfers, and corporate cards.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Domestic cards", "blurb": "Uzcard and HUMO.", "div": "kb", "rev": "retail", "products": [
            P("uzcardhumo", "Uzcard & HUMO cards", "Soum debit cards on the two national schemes (UZS 50,000 to issue, free to hold), with HUMO Kids and Uzcard Kids; the bulk of domestic spending ⚠ no bank split published.",
              s=["con", "sme"], lc="everyday", o="P", at="Uzcard, HUMO", neo=[0, "Uzcard and HUMO."], src=[["Kapitalbank: card list", CARDS], ["Kapitalbank: HUMO card", HUMO]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Visa cards", "blurb": "Best Visa issuer 2022–24.", "div": "kb", "rev": "retail", "products": [
            P("visacards", "Visa range", "Classic, Gold, Platinum and Infinite debit cards and Visa Gold Kids; Kapitalbank was named Uzbekistan's best Visa issuer in 2022, 2023 and 2024, with the highest Visa turnover and acceptance rate.",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa's strongest Uzbek issuer: the card book Mastercard is competing for.",
              src=[["Kapitalbank: Visa Awards 2024, Dec 2024", VISA24], ["Kapitalbank: Visa Awards 2023, Dec 2023", VISA23]]),
            P("visasum", "Visa Sum", "A Visa card on a soum account that pays at home and abroad, topped up at about 25,000 Paynet points since September 2024; the bank says it also works with Uzcard and HUMO ⚠ how.",
              s=["con"], lc="everyday", o="P", at="Visa, Paynet", ay="Sep 2024", neo=[0, "Visa."], src=[["Kapitalbank: Visa Sum", VISASUM], ["Kapitalbank: Paynet top-up, Sep 2024", PAYNET]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Mastercard cards", "blurb": "Standard to World.", "div": "kb", "rev": "retail", "products": [
            P("mccards", "Mastercard range", "Mastercard Standard, Gold and World, and Mastercard Sum / Mastercard Euro, billed as the cheapest international card (free to issue); issuing followed a 2022 tender for 300,000 Mastercard cards ⚠ first issue date.",
              short="Mastercard cards", s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["Kapitalbank: card list", CARDS], ["Kapitalbank: Mastercard card tender, Sep 2022", MCTENDER]]),
            P("mcbraille", "Mastercard Gold in Braille", "A soum Mastercard Gold with Braille markings for blind and partially sighted customers, free to issue (page dated December 2025).",
              s=["con"], lc="everyday", st="new", ay="Dec 2025", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Kapitalbank: Braille card", BRAILLE]]),
        ]},
        {"id": "2.4", "ic": "gem", "name": "Premium & multicurrency", "blurb": "Both networks at the top.", "div": "premium", "rev": "retail", "products": [
            P("visainf", "Visa Infinite & Platinum", "Visa Infinite in metal and veneer, and multicurrency Visa Platinum and Infinite; best premium Visa issuer with the highest premium Visa turnover (2024).",
              s=["prem"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Kapitalbank: card list", CARDS], ["Kapitalbank: Visa Awards 2024", VISA24]]),
            P("mcpremium", "Mastercard Black Edition & World Elite", "Black Edition in the Kapital Privilege package ($30,000 balance) and World Elite Metal Edge in Kapital Premium ($200,000): LoungeKey, Fast Track, roaming, travel insurance and Mastercard offers.",
              short="Mastercard premium", s=["prem"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard holds the second premium slot in both of the bank's premium packages.",
              src=[["Kapitalbank: Black Edition", MCBLACK], ["Kapitalbank: World Elite Metal Edge", MCWE]]),
            P("mcmulti", "Multicurrency Mastercard", "Black Edition and World Elite cards holding soum, dollar and euro accounts at once (announced December 2025 ⚠), free spending in each currency.",
              s=["prem", "con"], lc="move", st="new", ay="Dec 2025", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["Kapitalbank: multicurrency Black Edition", MCMULTI], ["Kapitalbank: multicurrency Mastercard, Dec 2025", MCMULTINEWS]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "Five brands and UzQR.", "div": "uzbiz", "rev": "sme", "products": [
            P("acquiring", "Merchant acquiring", "POS terminals that take Uzcard, HUMO, Visa, Mastercard and UnionPay; about 250,000 acquiring transactions a day (2025).",
              s=["merch"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["Kapitalbank: merchant acquiring", ACQ], ["Spot: CS core, May 2025", CORE]]),
            P("ecom", "E-commerce acceptance", "Online payments on websites, apps and Telegram bots at 1% a transaction for Humo, Uzcard, Visa and Mastercard; first Uzbek bank on Visa's CyberSource and Visa's top online acquirer in 2023.",
              s=["merch"], lc="move", o="P", at="Visa CyberSource", neo=[1, "Takes Mastercard; gateway is Visa's CyberSource."],
              src=[["Kapitalbank: e-commerce", ECOM], ["Kapitalbank: Visa Awards 2023", VISA23]]),
            P("qr", "Unified QR", "National UzQR codes issued in the SME app, without a terminal; QR acceptance became mandatory for all merchants on 1 July 2026.",
              s=["merch", "sme"], lc="move", st="new", ay="Jul 2026", neo=[0, "Domestic UzQR."],
              mc="UzQR and the 2027 National Payment Switch move domestic flows off international rails.",
              src=[["Spot: cashless rules, Jul 2026", CASHLESS], ["Kun.uz: unified QR rules, Apr 2026", QR]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Transfers abroad", "blurb": "Visa Direct leader, MoneySend.", "div": "online", "rev": "retail", "products": [
            P("visadirect", "Visa Direct", "Card-to-card transfers in and out of Uzbekistan (1%, minimum $2); Visa's leader for Visa Direct transfers, both person-to-person and business-to-person (2024).",
              s=["con"], lc="move", o="P", at="Visa", neo=[0, "Visa."], src=[["Kapitalbank: Visa Direct", VISADIRECT], ["Kapitalbank: Visa Awards 2024", VISA24]]),
            P("moneysend", "Mastercard MoneySend", "Real-time card transfers to and from Mastercard cards worldwide in the app (1%, minimum $2; up to UZS 100 million a transfer).",
              s=["con"], lc="move", o="P", at="Mastercard", neo=[3, "Mastercard's MoneySend."],
              mc="Mastercard's own rail, but Visa Direct carries the awards.",
              src=[["Kapitalbank: MoneySend", MONEYSEND], ["Kapitalbank: mobile app", APP]]),
            P("swiftwu", "SWIFT, Western Union & others", "SWIFT payments, and Western Union, MoneyGram and Asia Express transfers; Western Union fees halved in the app to January 2026, with inflows from Turkey and the US growing.",
              s=["con", "corp"], lc="move", o="P", at="Western Union", neo=[0, ""], src=[["Kapitalbank: Western Union offer, Dec 2025", WU]]),
        ]},
        {"id": "2.7", "ic": "briefcase-business", "name": "Corporate cards", "blurb": "Visa Business leads.", "div": "uzbiz", "rev": "corporate", "products": [
            P("bizcards", "Visa Business & Platinum Business", "Soum and dollar corporate cards; the first Visa Business Platinum in Uzbekistan (2023) and Visa's best business-card issuer (2024); Uzcard corporate cards too.",
              s=["sme", "corp"], lc="move", o="P", at="Visa", neo=[0, "Visa."], src=[["Kapitalbank: corporate cards", CORPCARDS], ["Kapitalbank: Visa Awards 2024", VISA24]]),
            P("mcbiz", "Mastercard Business", "A free soum corporate Mastercard for companies and sole traders, for travel and spending abroad (page dated July 2024).",
              s=["sme", "corp"], lc="move", ay="Jul 2024", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Kapitalbank: Mastercard Business", MCBIZ]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: security certified to ISO 27001 and a Visa-praised risk system, Visa's subscription controls, offers on both networks, and identity, scoring and accounting links.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "ISO 27001; Visa risk award.", "div": "kb", "rev": "retail", "products": [
            P("fraud", "Card risk & security", "Praised by Visa for its risk-management system (2024); first Uzbek bank with ISO/IEC 27001:2022 and 27701:2019 (2025); new Central Bank cyber rules from August 2025 ⚠ no AI fraud models disclosed.",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa's tools and the bank's own."],
              mc="Generative-AI phishing is named as a 2026 threat; Mastercard's scam and identity tools are untested here.",
              src=[["Kapitalbank: Visa Awards 2024", VISA24], ["Spot: TAF!25, Oct 2025", TAF]]),
            P("bizsecurity", "Business account security", "Role-based access, SMS and secret-code confirmation, device checks and push alerts in Uzum Business Kapitalbank.",
              s=["sme"], lc="everyday", neo=[0, ""], src=[["Spot: account security, Jul 2026", SAFETY]]),
        ]},
        {"id": "3.2", "ic": "refresh-cw", "name": "Card controls", "blurb": "Pause subscriptions.", "div": "online", "rev": "retail", "products": [
            P("subs", "Subscription control", "Visa Kapitalbank holders can see, pause for up to five years and restore recurring card payments in the app (July 2025).",
              s=["con"], lc="everyday", st="new", ay="Jul 2025", o="P", at="Visa", neo=[0, "Visa."], src=[["Kapitalbank: subscription control, Jul 2025", VISASUBS]]),
            P("controls", "Card self-service", "Block and unblock cards, alerts, statements and card ordering with courier delivery, in the app and a Telegram bot (since 2020).",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Kapitalbank: mobile app", APP]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Offers & rewards", "blurb": "Mastercard offers, Visa football.", "div": "kb", "rev": "retail", "products": [
            P("mcoffers", "Mastercard Kapitalbank offers", "Discounts to 31 December 2026: Yandex Eats and Yandex Lavka 10%, My Taxi up to 15% for Black Edition and World Elite, iTicket 10%.",
              s=["con", "prem"], lc="grow", st="new", ay="Aug 2026", o="P", at="Mastercard, Yandex, My Taxi", neo=[2, "Mastercard cards only."],
              src=[["Anhor: Mastercard Kapitalbank offers, Aug 2026", MCOFFERS]]),
            P("mctravel", "Mastercard travel rewards", "'Cashback Abroad' (5% on restaurants, 10% on taxis, late 2024) and a draw for trips to Tokyo, the Maldives and the 2026 Champions League final for Black Edition and World Elite holders (December 2025).",
              s=["prem"], lc="grow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Kapitalbank: Cashback Abroad, Nov 2024", MCCASHBACK], ["Kapitalbank: Mastercard travel draw, Dec 2025", MCDRAW]]),
            P("visapromo", "Visa campaigns", "A Visa FIFA World Cup 2026 campaign sending a fan team to the US, with points for every dollar spent (2025–26), and Visa cards in WeChat Pay and Alipay for China (July 2025).",
              s=["con"], lc="grow", o="P", at="Visa", neo=[0, "Visa."], src=[["Kapitalbank: FIFA 2026 fan team, Apr 2026", FIFA], ["Spot: Visa in China, Jul 2025", VISACHINA]]),
        ]},
        {"id": "3.4", "ic": "fingerprint", "name": "Identity, data & APIs", "blurb": "MyID, scoring, 1C links.", "div": "kb", "rev": "sme", "products": [
            P("identity", "Identity & scoring", "MyID onboarding in the app, biometric checks for online business accounts, and scoring models S&P credits for keeping problem loans below the sector.",
              s=["con", "sme"], lc="open", neo=[0, ""],
              mc="Mastercard signed AI credit scoring with Xalq Bank in May 2026; Kapitalbank has the data to do the same.",
              src=[["Kapitalbank: mobile app", APP], ["Spot: online account, Jun 2026", ACCOUNT], ["Spot: S&P BB-, Jul 2025", SP25]]),
            P("kapi", "Kapital API & DiBank", "Banking from 1C and Didox accounting systems through Venkon Group (since December 2020); no open-banking regime yet ⚠.",
              s=["sme", "corp"], lc="open", o="P", at="Venkon Group", neo=[0, ""], src=[["Kapitalbank: Kapital API", KAPI]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: the country's largest retail deposit book, car loans, mortgages and microloans, Kapital Premium and Privilege, accounts and cash services for about 100,000 entrepreneurs, and trade finance, factoring and FX for corporates.",
    "tiles": [
        {"id": "4.1", "ic": "coins", "name": "Deposits", "blurb": "No. 1 in retail deposits.", "div": "kb", "rev": "retail", "products": [
            P("deposits", "Savings & deposits", "Retail deposits of UZS 28.1 trillion at 1 July 2026, the most of any Uzbek bank (an 18.1% share in June 2025); soum, dollar and euro term deposits opened in the app.",
              s=["con"], lc="grow", neo=[0, ""], src=[["UzDaily: bank assets, Jul 2026", LEAGUE], ["Spot: S&P BB-, Jul 2025", SP25]]),
        ]},
        {"id": "4.2", "ic": "hand-coins", "name": "Retail lending", "blurb": "Cars, homes, microloans.", "div": "kb", "rev": "retail", "products": [
            P("carloans", "Car loans", "Kapital Auto Plus and 0% 'UzAuto Nasiya' loans for Chevrolet Onix and Tracker with UzAuto Motors; car lending is the book S&P says the bank is diversifying away from.",
              s=["borrow"], lc="borrow", o="P", at="UzAuto Motors", neo=[0, ""], src=[["Kapitalbank: UzAuto Nasiya", UZAUTO], ["Spot: S&P outlook positive, Jul 2026", SP26]]),
            P("mortgage", "Mortgages", "'Comfortable House' mortgages at 24–26% for up to ten years and UZS 1 billion.",
              s=["borrow"], lc="borrow", neo=[0, ""], src=[["Kapitalbank: loans", LOANS]]),
            P("microloans", "Microloans", "Kapital Microcredit Universal (23.99%, up to UZS 300 million), Kapital Start and Ecocredit; debt-load rules tightened from July 2024.",
              s=["borrow", "sme"], lc="borrow", neo=[0, ""], src=[["Kapitalbank: loans", LOANS]]),
        ]},
        {"id": "4.3", "ic": "gem", "name": "Premium banking", "blurb": "Kapital Premium & Privilege.", "div": "premium", "rev": "retail", "products": [
            P("kpremium", "Kapital Premium & Kapital Privilege", "Personal managers and dedicated offices; Premium free above $200,000 of balances and Privilege above $30,000, each pairing a Visa Infinite with a Mastercard World Elite or Black Edition.",
              s=["prem"], lc="grow", o="B", neo=[1, "Visa and Mastercard side by side."], src=[["Kapitalbank: World Elite Metal Edge", MCWE], ["Kapitalbank: Black Edition", MCBLACK]]),
        ]},
        {"id": "4.4", "ic": "briefcase", "name": "Small business", "blurb": "About 100,000 entrepreneurs.", "div": "uzbiz", "rev": "sme", "products": [
            P("smeaccount", "Business accounts & loans", "Online account opening with a biometric check, 'Successful Business' loans and IT Park residents' fast track; SME lending doubled in 2024 (Fitch); Uzcard's 'Leader in corporate business development' (2024).",
              s=["sme"], lc="open", neo=[0, ""], src=[["Spot: online account, Jun 2026", ACCOUNT], ["Kapitalbank: Fitch, Jul 2025", FITCH], ["Kapitalbank: IT Park, Jul 2025", ITPARK], ["Kapitalbank: Uzcard award, Oct 2024", UZCARDAWARD]]),
            P("selfcollect", "Cash self-collection", "Businesses pay takings into their accounts at Kapitalbank ATMs without a card, instantly, up to UZS 10 million a day (August 2025).",
              s=["sme", "merch"], lc="everyday", st="new", ay="Aug 2025", neo=[0, ""], src=[["Spot: self-collection, Jul 2026", SELFCOLLECT]]),
        ]},
        {"id": "4.5", "ic": "factory", "name": "Corporate, trade & FX", "blurb": "Factoring, BNY dollars.", "div": "kb", "rev": "corporate", "products": [
            P("tradefin", "Trade finance", "Framework credit lines, guarantees and letters of credit with lines from LBBW, Helaba, ODDO BHF and Commerzbank, and a $22 million syndicated loan for MAKESENSE (2025).",
              s=["corp"], lc="borrow", o="P", at="Commerzbank, LBBW", neo=[0, ""], src=[["Kapitalbank: history", HISTORY], ["Spot: TAF!25, Oct 2025", TAF]]),
            P("factoring", "Factoring", "Classic and reverse factoring up to 90 days; the first Uzbek member of Factors Chain International (2021).",
              s=["corp", "sme"], lc="borrow", neo=[0, ""], src=[["Spot: factoring and leasing, Aug 2026", FACTORING]]),
            P("fx", "Treasury, FX & correspondents", "A major dealer on the Uzbek currency exchange, gold bars, and 17 correspondent banks, adding a BNY dollar account in September 2026.",
              s=["corp"], lc="move", st="new", neo=[0, ""], src=[["Spot: BNY account, Sep 2026", BNY]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the KAPITALBANK.Online app, the Uzum Business Kapitalbank app, more than 90 offices and 1,500 ATMs, and the Uzum ecosystem and partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "KAPITALBANK.Online", "blurb": "Version 3.0, 2025.", "div": "online", "rev": "retail", "products": [
            P("app", "KAPITALBANK.Online app", "The retail app (version 3.0, February 2025): cards, deposits, loans, currency exchange, Visa Direct and MoneySend transfers, payments and MyID sign-up ⚠ no user count.",
              s=["con", "prem"], lc="everyday", st="new", ay="Feb 2025", neo=[1, "MoneySend and Mastercard cards inside."],
              src=[["Kapitalbank: mobile app", APP], ["Kapitalbank: app update, Feb 2025", APPUPD]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Uzum Business Kapitalbank", "blurb": "The SME app.", "div": "uzbiz", "rev": "sme", "products": [
            P("uzbizapp", "Uzum Business Kapitalbank", "The business app and web bank (launched October 2023): payments, payroll, SWIFT, FX, QR codes, cash self-collection and online accounts.",
              s=["sme", "merch"], lc="everyday", ay="Oct 2023", neo=[0, ""], src=[["Kapitalbank: Uzum Business", UZBIZ], ["Spot: cashless rules, Jul 2026", CASHLESS]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & ATMs", "blurb": "90+ offices, 1,500+ ATMs.", "div": "kb", "rev": "retail", "products": [
            P("branches", "Offices & ATMs", "More than 90 branches and banking service offices and more than 1,500 ATMs (2025), which have taken HUMO, Uzcard, Visa, UnionPay and Mastercard since May 2023.",
              s=["con"], lc="everyday", neo=[1, "ATMs take Mastercard among five brands."], src=[["Spot: CS core, May 2025", CORE], ["Kapitalbank: history", HISTORY]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Uzum & partners", "blurb": "Ecosystem cross-sell.", "div": "uzum", "rev": "retail", "products": [
            P("uzumeco", "Uzum ecosystem", "Access to Uzum's customers (more than half the population, says S&P); the sister Uzum Bank has issued more than 5 million Uzum Visa cards with embedded credit (March 2026).",
              s=["con"], lc="beyond", o="P", at="Uzum", neo=[0, "Uzum Bank's cards are Visa."],
              mc="The group's mass-market card went to Visa; Kapitalbank is where Mastercard has a foothold.",
              src=[["Spot: S&P outlook positive, Jul 2026", SP26], ["Spot: 5 million Uzum cards, Mar 2026", UZUM5M], ["Uzum: Visa for all, Oct 2024", UZUMVISA]]),
            P("partners", "Partners", "Paynet's 25,000 cash points, UzAuto Motors dealers, IT Park and Western Union.",
              s=["con", "borrow", "sme"], lc="beyond", o="P", at="Paynet, UzAuto Motors", neo=[0, ""], src=[["Kapitalbank: Paynet top-up, Sep 2024", PAYNET], ["Kapitalbank: UzAuto Nasiya", UZAUTO]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Kapitalbank", "blurb": "Second network, premium slots.", "products": [
        P("mcatkb", "Mastercard at Kapitalbank", "Visa is Kapitalbank's lead international network: best Visa issuer in 2022–24, Visa Direct leader, first on CyberSource, and Visa's World Cup campaign. Mastercard is a full second line: Standard to World Elite, multicurrency premium cards (December 2025 ⚠), Mastercard Business, MoneySend and 2026 partner offers. No network agreement or named executives have been published.",
          s=["con"], div="kb", rev="retail", mc="The relationship this map is drawn for.",
          src=[["Kapitalbank: Visa Awards 2024", VISA24], ["Kapitalbank: card list", CARDS], ["Anhor: Mastercard Kapitalbank offers, Aug 2026", MCOFFERS]]),
    ]},
    {"id": "pillar-market", "name": "Uzbek payments", "blurb": "Uzcard, HUMO, UzQR, wallets.", "products": [
        P("market", "The Uzbek market", "68.3 million cards (January 2026), mostly on Uzcard and HUMO; HUMO owned by Paynet and co-badged with UnionPay (July 2026); UzQR mandatory from July 2026; Apple Pay and Google Pay expected, tokenisation unresolved; a National Payment Switch due in 2027. Mastercard has had an office since May 2023 and signed with Xalq Bank in May 2026.",
          s=["con"], div="kb", rev="retail",
          src=[["Kun.uz: cashless surge, Feb 2026", CARDS68], ["HUMO: UnionPay co-badge, Jul 2026", HUMOUP], ["Times of Central Asia: wallets, Jul 2026", WALLETS], ["Kun.uz: Mastercard office, May 2023", MCOFFICE], ["Kun.uz: Xalq Bank and Mastercard, May 2026", XALQ]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
