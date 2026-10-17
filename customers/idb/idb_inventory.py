"""International Development Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

IDB's own website sits behind bot protection and could not be read directly in October 2026, so figures come from
search extracts of its pages (marked ⚠), a September 2024 archive of its home page, and third parties: the Central
Bank of Iraq, the KRG, Shafaq News, The New Region, Arab News and the Iraq Britain Business Council. No 2025 or 2026
results were found. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

IR = "https://idb.iq/uae/en/investor-relations/overview"
UAESITE = "https://idb.iq/uae/en"
CARDS = "https://idb.iq/iq/en/cards"
VISADEBIT = "https://www.idb.iq/index.php/en/dynamic-pages/page/56/visa-debit-cards"
GOVACH = "https://idb.iq/iq/en/about/governance/achievements"
HOME24 = "https://web.archive.org/web/20240919004500/https://www.idb.iq/en"
IBBC = "https://iraqbritainbusiness.org/member/international-development-bank"
WIKI = "https://en.wikipedia.org/wiki/Zead_Khalaf"
SUMMIT = "https://idb.iq/iq/en/news/1240/international-development-bank-named-official-sponsor-of-the-iraq-business-summit-2025-reinforcing-its-role-in-supporting-the-iraqi-economy"
CBIINIT = "https://www.idb.iq/iq/en/news/1255/dr-ziad-khalaf-abd-karim-presented-initiatives-in-collaboration-with-the-central-bank-of-iraq"
ERBIL = "https://shafaq.com/en/Kurdistan/International-Development-Bank-opens-new-branch-in-Erbil-expanding-reach-in-Iraqi-Kurdistan"
DUBAI = "https://idb.iq/uae/en/news/132/international-development-bank-opens-its-first-branch-in-dubai-the-uae"
CBIDUBAI = "https://cbi.iq/news/view/2123"
IFC = "https://findevgateway.org/news/ifc-international-development-bank-launch-effort-expand-financial-services-iraq"
ATO = "https://www.arabnews.pk/node/2370761"
ATC = 'https://idb.iq/iq/en/news/1262/international-development-bank-launches-the-"arab-tourist-card"-in-cooperation-with-the-official-national-tourism-platform-–-visit-iraq'
MOUS24 = "https://www.iraq-businessnews.com/2024/11/28/iraq-signs-mous-for-tourism-development/"
KRGSAL = "https://www.idb.iq/iq/en/news/207/the-international-development-bank-(idb)-is-opening-its-doors-to-nationalize-the-salaries-of-the-kurdistan-regional-government-(krg)"
KRGJOIN = "https://gov.krd/dmi-en/activities/news-and-press-releases/2024/june/international-development-bank-idb-joins-my-account/"
KRGOUT = "https://gov.krd/mofe-en/activities/news-and-press-releases/2025/september/international-development-bank-idb-removed-from-the-myaccount-programme/"
TNR = "https://thenewregion.com/posts/3003"
CBI2025 = "https://www.iraq-businessnews.com/2025/08/09/iraqs-central-bank-advances-digital-payment-transformation/"
CASH = "https://www.shafaq.com/en/Economy/Cash-dominates-payments-in-Iraq-despite-rise-in-bank-cards"
MC2021 = "https://newsroom.mastercard.com/news/eemea/en/newsroom/press-releases/en/2021/april/mastercard-enters-into-strategic-partnership-with-central-bank-of-iraq-to-advance-digital-payments-in-the-country"
QIABOUT = "https://qi.iq/en/about-us"
QIM2020 = "https://www.zawya.com/en/press-release/companies-news/international-smart-card-strengthens-iraqs-fintech-footprint-at-money20-20-usa-sdrhvcmu"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · licences · founder", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a private bank founded in 2011 with about USD 2.4 billion of assets in 2024, a founder-chairman, card licences from both Mastercard and Visa, a UAE licence, and a US-dollar bar reported in 2025.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & capital", "blurb": "USD 2.4bn of assets, 2024.", "div": "idb", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of about USD 2.38 billion at the end of 2024, up from USD 1.82 billion in 2023; net profit about USD 45.8 million (2023: USD 31.3 million); equity about USD 350.9 million ⚠ from a search extract of the investor-relations page. No 2025 or 2026 results found.",
              s=["corp"], neo=[0, ""], src=[["IDB: investor relations ⚠", IR]]),
            P("capital", "Capital & listing", "Founded with IQD 100 billion of capital, now IQD 250 billion paid up (about USD 171 million); listed on the Iraq Stock Exchange in 2018. Ticker, market value and ratings not found ⚠.",
              s=["corp"], neo=[0, ""], src=[["IBBC: IDB profile", IBBC]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Founder-chairman Ziad Khalaf.", "div": "idb", "rev": "group", "products": [
            P("board", "Chairman & board", "Dr Ziad (Zead) Khalaf Abdul Karim co-founded the bank in 2011 and has chaired it since 2015; he also chairs ZK Holding in Abu Dhabi and sits on the Union of Arab Banks board.",
              s=["corp"], neo=[0, ""], src=[["Wikipedia: Zead Khalaf", WIKI], ["Arab News: ATO agreement, Sep 2023", ATO]]),
            P("exec", "Management", "Fadi Al-Faqih is named as chief executive at the Iraq Business Summit 2025 ⚠; Saad Faik was managing director in May 2024 ⚠ current role. No 2026 executive list found.",
              s=["corp"], st="unconf", neo=[0, ""], src=[["IDB: Iraq Business Summit 2025 ⚠", SUMMIT], ["Shafaq News: Erbil branch, May 2024", ERBIL]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Licences", "blurb": "Mastercard, Visa and the UAE.", "div": "idb", "rev": "group", "products": [
            P("heritage", "Founding & footprint", "A private commercial bank since 2011, describing itself as the largest private bank in Iraq by assets and deposits ⚠, with 27 branches in Iraq (May 2024), a Dubai branch and a Beirut representative office ⚠.",
              s=["con", "corp"], neo=[0, ""], src=[["IDB home page, Sep 2024 (archive)", HOME24], ["IBBC: IDB profile", IBBC], ["IDB: investor relations ⚠", IR]]),
            P("cardlic", "Mastercard & Visa licences", "Says it was the first Iraqi bank to hold both issuing and acquiring licences from Mastercard and Visa, a process begun in 2016 ⚠ from a search extract.",
              s=["con", "merch"], lc="move", ay="2016", o="P", at="Mastercard, Visa", neo=[1, "Licensed by both networks."],
              mc="The licence is in place; the issuing on it is mostly Visa.",
              src=[["IDB: governance achievements ⚠", GOVACH], ["IDB: cards ⚠", CARDS]]),
            P("uaelic", "UAE licence", "The first Iraqi private bank licensed by the UAE Central Bank; its Dubai branch opened on 9 November 2022 with the CBI governor present. Its UAE pages also cite Abu Dhabi Global Market regulation ⚠.",
              s=["corp"], ay="Nov 2022", neo=[0, ""], src=[["CBI: Dubai branch, Nov 2022", CBIDUBAI], ["IDB: Dubai branch", DUBAI], ["IDB UAE ⚠", UAESITE]]),
        ]},
        {"id": "1.4", "ic": "flag", "name": "Dollar restrictions", "blurb": "Barred from US-dollar business.", "div": "idb", "rev": "group", "products": [
            P("usdbar", "US-dollar bar", "Reported in September 2025 as one of the Iraqi banks barred from opening dollar accounts and making international dollar transfers under US pressure; for such banks international card use was restricted. The date of the bar and its status in October 2026 are not public ⚠.",
              s=["con", "corp", "trav"], st="flux", neo=[0, ""],
              mc="Limits what any network can do abroad for IDB cardholders until it is lifted.",
              src=[["The New Region, Sep 2025", TNR], ["KRG: IDB leaves MyAccount, Sep 2025", KRGOUT]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & technology", "blurb": "Corporate links, little on tech.", "div": "idb", "rev": "group", "products": [
            P("strategy", "Strategy", "Tailored commercial banking for every industry with digital banking; a regional bank linking UAE companies to Iraq; and work with the Central Bank of Iraq on national initiatives (2025 ⚠).",
              s=["corp"], neo=[0, ""], src=[["IBBC: IDB profile", IBBC], ["IDB: CBI initiatives ⚠", CBIINIT]]),
            P("deals", "Partnerships", "IFC memorandum on private-sector finance (May 2019); AD Ports Group agreement (2022 ⚠); an Aramex logistics joint venture with about 7,000 service points (2024 ⚠).",
              s=["corp"], o="P", at="IFC, AD Ports, Aramex", neo=[0, ""], src=[["FinDev Gateway: IFC MoU, May 2019", IFC], ["Wikipedia: Zead Khalaf", WIKI]]),
            P("tech", "Technology & AI", "No core-banking, cloud, data or AI programme found in public sources ⚠.",
              s=["corp"], st="unconf", neo=[None, "Nothing public."], src=[["IDB home page, Sep 2024 (archive)", HOME24]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Visa debit cards, a Mastercard Gold credit card, prepaid and the Arab Tourist Card, acquiring on about 5,000 terminals, 400 ATMs and agents, transfers and collections, and the Central Bank of Iraq's new national rails.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Visa Classic and Platinum.", "div": "cards", "rev": "retail", "products": [
            P("visaclassic", "Visa Classic debit", "For any account holder; ATMs worldwide and points of sale in and outside Iraq; valid five years (an older page said three ⚠).",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["IDB: cards ⚠", CARDS], ["IDB: Visa debit ⚠", VISADEBIT]]),
            P("visaplat", "Visa Platinum debit", "Adds selected airport lounges, purchase protection and extended warranty.",
              s=["con", "trav"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["IDB: cards ⚠", CARDS]]),
            P("ratecard", "Debit at the official rate", "IDB debit cards linked to the Central Bank of Iraq's official exchange rate and to every account type (November 2024 ⚠). Network not stated.",
              s=["con"], lc="everyday", neo=[None, "Network not stated."], src=[["IDB: KRG salaries ⚠", KRGSAL]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit", "blurb": "Mastercard Gold.", "div": "cards", "rev": "retail", "products": [
            P("mcgold", "Mastercard Gold credit", "Limits of IQD 6–12 million or USD 4,000–8,000, valid three years; the only credit card named on the cards page.", short="Gold credit (Mastercard)",
              s=["prem", "con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="IDB's only named Mastercard card.",
              src=[["IDB: cards ⚠", CARDS]]),
        ]},
        {"id": "2.3", "ic": "plane", "name": "Prepaid & tourism", "blurb": "The Arab Tourist Card.", "div": "cards", "rev": "retail", "products": [
            P("prepaid", "Prepaid cards", "Prepaid is listed among retail services (2024); the 2023 Arab Tourism Organization deal described a prepaid Visa travel card. Other prepaid networks not stated ⚠.",
              s=["trav", "con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["IDB home page, Sep 2024 (archive)", HOME24], ["Arab News: ATO agreement, Sep 2023", ATO]]),
            P("arabtourist", "Arab Tourist Card", "Launched in May 2025 with Visit Iraq, the national tourism platform; the ATO chose IDB as exclusive issuer of Visa and Mastercard payment cards for Arab tourists, with health insurance and Visa discounts. Sources differ on the networks ⚠.",
              s=["trav"], lc="everyday", st="new", ay="May 2025", o="P", at="ATO, Visit Iraq, Visa", neo=[1, "Visa and Mastercard ⚠."],
              mc="A tourism programme where Mastercard is named but Visa supplies the benefits.",
              src=[["IDB: Arab Tourist Card, May 2025 ⚠", ATC], ["Arab News: ATO agreement, Sep 2023", ATO], ["Iraq Business News: tourism MoUs, Nov 2024", MOUS24]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acquiring", "blurb": "About 5,000 terminals.", "div": "cards", "rev": "corporate", "products": [
            P("acquiring", "Merchant acquiring", "About 5,000 direct POS terminals (May 2024), acquiring for Visa and Mastercard under its own licences ⚠ domestic-switch routing not stated.",
              s=["merch"], lc="move", o="P", at="Mastercard, Visa", neo=[1, "Accepts Mastercard and Visa."],
              mc="Acceptance is growing under the CBI's cashless push.",
              src=[["Shafaq News: Erbil branch, May 2024", ERBIL], ["IDB: governance achievements ⚠", GOVACH]]),
        ]},
        {"id": "2.5", "ic": "network", "name": "ATMs & agents", "blurb": "400 ATMs, 7,000 outlets.", "div": "iraq", "rev": "retail", "products": [
            P("atms", "ATM network", "About 400 ATMs, which it calls the largest in Iraq, with free withdrawals for IDB cardholders (May 2024).",
              s=["con"], lc="everyday", neo=[1, "Takes all cards."], src=[["Shafaq News: Erbil branch, May 2024", ERBIL], ["IDB home page, Sep 2024 (archive)", HOME24]]),
            P("agents", "Agents & service points", "An agent service and about 7,000 'POC' outlets in every province (May 2024), possibly linked to the Aramex venture ⚠.",
              s=["con", "gov"], lc="open", neo=[None, ""], src=[["Shafaq News: Erbil branch, May 2024", ERBIL]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Transfers & collections", "blurb": "Correspondents in 20+ countries.", "div": "iraq", "rev": "retail", "products": [
            P("remit", "Remittances & international transfers", "International transfers through correspondents in more than 20 countries (May 2024); dollar transfers restricted after the bar reported in 2025 ⚠.",
              s=["con", "corp"], lc="move", st="flux", neo=[0, ""], src=[["Shafaq News: Erbil branch, May 2024", ERBIL], ["The New Region, Sep 2025", TNR]]),
            P("billing", "Billing & collection", "Bill collection listed among retail services (2024); no detail found ⚠.",
              s=["gov", "con"], lc="move", neo=[None, ""], src=[["IDB home page, Sep 2024 (archive)", HOME24]]),
        ]},
        {"id": "2.7", "ic": "zap", "name": "National rails", "blurb": "Switch, instant payments, national card.", "div": "idb", "rev": "group", "products": [
            P("switch", "CBI national switch & schemes", "The Central Bank of Iraq is building a national switch, 24/7 instant payments, a unified government gateway and a national card scheme to reduce reliance on foreign systems (August 2025). Go-live dates and IDB's role not found ⚠.",
              s=["con", "merch", "gov"], lc="move", st="new", o="P", at="Central Bank of Iraq", neo=[0, "Domestic rails."],
              mc="A national scheme would compete with international debit for domestic spend.",
              src=[["Iraq Business News: CBI payments, Aug 2025", CBI2025]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: Visa card benefits and sponsorship offers, customer protection with nothing public on fraud or AI, and salary domiciliation for federal and Kurdistan employees.",
    "tiles": [
        {"id": "3.1", "ic": "gift", "name": "Benefits & offers", "blurb": "Lounges and Visa promotions.", "div": "cards", "rev": "retail", "products": [
            P("benefits", "Card benefits", "Platinum debit lounge access, purchase protection and extended warranty; Visa discounts on the Arab Tourist Card.",
              s=["con", "trav"], lc="grow", o="P", at="Visa", neo=[0, "Visa."], src=[["IDB: cards ⚠", CARDS], ["IDB: Arab Tourist Card, May 2025 ⚠", ATC]]),
            P("promos", "Sponsorship promotions", "News items titled 'IDB x Visa – AFC Elite' (April 2025) and 'Olympic Games Paris 2024' (May 2024), apparently Visa campaigns; only titles were readable ⚠.",
              s=["con"], lc="grow", st="unconf", o="P", at="Visa", neo=[0, "Visa ⚠."],
              mc="Visa holds the sponsorship platform; Mastercard has no visible campaign at IDB.",
              src=[["IDB home page, Sep 2024 (archive)", HOME24]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Protection, fraud & data", "blurb": "Little published.", "div": "idb", "rev": "retail", "products": [
            P("protection", "Customer protection & alerts", "A customer-protection section with a tariff guide, claims and clients' rights, and SMS alerts (2024).",
              s=["con"], lc="everyday", neo=[0, ""], src=[["IDB home page, Sep 2024 (archive)", HOME24]]),
            P("fraud", "Fraud, identity & AI", "No fraud, identity, data or AI tools published ⚠; the CBI's 2018 memorandum with Mastercard named fraud management as a priority for Iraq.",
              s=["con", "merch"], lc="everyday", st="unconf", neo=[None, "Nothing public."],
              mc="An open field for fraud scoring and identity tools.",
              src=[["Mastercard: CBI partnership, Apr 2021", MC2021]]),
        ]},
        {"id": "3.3", "ic": "receipt-text", "name": "Salaries", "blurb": "Federal and KRG payroll.", "div": "iraq", "rev": "retail", "products": [
            P("salaries", "Salary domiciliation", "Salary accounts for public and private employers, with free withdrawals at IDB ATMs; opened to Kurdistan Regional Government salaries (2024).",
              s=["gov", "con"], lc="open", neo=[None, "Network of salary cards not stated."], src=[["IDB home page, Sep 2024 (archive)", HOME24], ["IDB: KRG salaries ⚠", KRGSAL]]),
            P("myaccount", "KRG MyAccount", "Joined the KRG's MyAccount salary programme in June 2024; removed on 8 September 2025 because of CBI restrictions on its dollar business, with beneficiaries moved to other banks.",
              s=["gov"], lc="open", st="retired", ay="Jun 2024", o="P", at="KRG", neo=[0, "MyAccount partners with Visa."],
              src=[["KRG: IDB joins MyAccount, Jun 2024", KRGJOIN], ["KRG: IDB leaves MyAccount, Sep 2025", KRGOUT]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail accounts and loans, corporate lending and cash management, trade finance, treasury and custody, a Dubai branch for corporates, and tourism and logistics finance.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Retail banking", "blurb": "Accounts and loans.", "div": "iraq", "rev": "retail", "products": [
            P("accounts", "Accounts", "Current, savings and deposit accounts, with chequebooks, cards and mobile banking (2024).",
              s=["con"], lc="everyday", neo=[0, "Visa debit."], src=[["IDB home page, Sep 2024 (archive)", HOME24]]),
            P("loans", "Personal loans", "Retail loans, with housing, wedding and travel themes on the 2024 site ⚠; book size not published.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["IDB home page, Sep 2024 (archive)", HOME24]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Corporate banking", "blurb": "Lending and liquidity.", "div": "iraq", "rev": "corporate", "products": [
            P("corplending", "Corporate lending", "Short-term financing and medium- and long-term loans, including large projects; lending above USD 70 million in 2021 (later figure not found ⚠).",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["IBBC: IDB profile", IBBC], ["IDB home page, Sep 2024 (archive)", HOME24]]),
            P("cashmgmt", "Cash & liquidity management", "Cash and liquidity management for corporate clients (2024).",
              s=["corp"], lc="move", neo=[0, ""],
              mc="No commercial or purchasing card is published.",
              src=[["IDB home page, Sep 2024 (archive)", HOME24]]),
        ]},
        {"id": "4.3", "ic": "earth", "name": "Trade finance", "blurb": "Correspondents abroad.", "div": "iraq", "rev": "corporate", "products": [
            P("tradefin", "Trade finance", "Letters of credit and guarantees through correspondents in more than 20 countries (May 2024) ⚠ affected by the dollar bar.",
              s=["corp"], lc="move", st="flux", neo=[0, ""], src=[["Shafaq News: Erbil branch, May 2024", ERBIL]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Treasury & investment", "blurb": "Treasury and custody.", "div": "idb", "rev": "invest", "products": [
            P("treasury", "Treasury & advisory", "Treasury services and financial advisory (2024).",
              s=["corp"], lc="grow", neo=[0, ""], src=[["IDB home page, Sep 2024 (archive)", HOME24]]),
            P("custody", "Investment & custody", "Investment and custodian services under investment banking (2024).",
              s=["corp"], lc="grow", neo=[0, ""], src=[["IDB home page, Sep 2024 (archive)", HOME24]]),
        ]},
        {"id": "4.5", "ic": "building", "name": "UAE banking", "blurb": "Dubai since 2022.", "div": "uae", "rev": "corporate", "products": [
            P("dubai", "Dubai branch", "Corporate banking for companies, mostly UAE firms investing and trading in Iraq, since November 2022.",
              s=["corp"], lc="move", ay="Nov 2022", neo=[0, ""], src=[["IDB: Dubai branch", DUBAI], ["CBI: Dubai branch, Nov 2022", CBIDUBAI]]),
            P("escrow", "Escrow & export support", "Authorised Dubai Land Department escrow-account trustee, and an Etihad Credit Insurance agreement on exports ⚠ undated.",
              s=["corp"], lc="beyond", o="P", at="Etihad Credit Insurance", neo=[0, ""], src=[["Wikipedia: Zead Khalaf", WIKI]]),
        ]},
        {"id": "4.6", "ic": "briefcase-business", "name": "Tourism & logistics", "blurb": "ATO, AD Ports, Aramex.", "div": "idb", "rev": "corporate", "products": [
            P("tourismfin", "Tourism finance", "A 2023 agreement with the Arab Tourism Organization to finance tourism projects through its development fund, alongside the tourist card.",
              s=["corp", "trav"], lc="borrow", ay="Sep 2023", o="P", at="Arab Tourism Organization", neo=[0, ""], src=[["Arab News: ATO agreement, Sep 2023", ATO]]),
            P("logistics", "Logistics ventures", "AD Ports Group agreement (2022) and an Aramex joint venture for shipping in Iraq (2024) ⚠ from secondary sources.",
              s=["corp"], lc="beyond", o="P", at="AD Ports, Aramex", neo=[0, ""], src=[["Wikipedia: Zead Khalaf", WIKI]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: 27 branches from Erbil to the south, the e-IDB app and internet banking, and partners from the KRG to Visit Iraq.",
    "tiles": [
        {"id": "5.1", "ic": "building", "name": "Branches", "blurb": "27 in Iraq.", "div": "iraq", "rev": "retail", "products": [
            P("branches", "Branch network", "27 branches across Iraq after Erbil opened in May 2024, plus Dubai.",
              s=["con", "corp"], lc="open", neo=[0, ""], src=[["Shafaq News: Erbil branch, May 2024", ERBIL]]),
        ]},
        {"id": "5.2", "ic": "smartphone", "name": "e-IDB", "blurb": "App and internet banking.", "div": "eidb", "rev": "retail", "products": [
            P("mobile", "Mobile banking app", "The e-IDB mobile app (2024); user numbers and wallet support not published ⚠.",
              s=["con"], lc="everyday", neo=[None, ""],
              mc="No Apple Pay or Google Pay yet; Iraq targeted Apple Pay for 2026 ⚠.",
              src=[["IDB home page, Sep 2024 (archive)", HOME24]]),
            P("internet", "Internet banking", "Online banking for retail and corporate clients (2024).",
              s=["con", "corp"], lc="everyday", neo=[0, ""], src=[["IDB home page, Sep 2024 (archive)", HOME24]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "Government and tourism.", "div": "idb", "rev": "retail", "products": [
            P("partners", "Government & tourism partners", "Salary programmes with federal and Kurdistan employers, the Arab Tourism Organization and Visit Iraq, and sponsorship of the Iraq Business Summit 2025.",
              s=["gov", "trav"], lc="open", o="P", at="KRG, ATO, Visit Iraq", neo=[0, ""], src=[["IDB: Iraq Business Summit 2025 ⚠", SUMMIT], ["IDB: Arab Tourist Card, May 2025 ⚠", ATC]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at IDB", "blurb": "A licence, a Gold card, acceptance.", "products": [
        P("mcatidb", "Mastercard at IDB", "IDB holds Mastercard issuing and acquiring licences, issues a Mastercard Gold credit card, accepts Mastercard on about 5,000 terminals and 400 ATMs, and names Mastercard on the Arab Tourist Card. Its debit range and first prepaid card are Visa, and its visible promotions are Visa's ⚠. Mastercard's Iraqi agreements are with the Central Bank (2018, 2021) and its biggest channel is Qi Card.",
          s=["con"], div="idb", rev="group", mc="The relationship this map is drawn for.",
          src=[["IDB: cards ⚠", CARDS], ["Mastercard: CBI partnership, Apr 2021", MC2021], ["Qi Card: about", QIABOUT]]),
    ]},
    {"id": "pillar-market", "name": "Iraqi payments", "blurb": "Cash, dollar bars, a national switch.", "products": [
        P("market", "The Iraqi market", "Cash is still 90–95% of transactions (March 2026); the CBI is building a national switch, instant payments and a national card scheme; state bodies were to stop taking cash by July 2026 ⚠; Qi Card serves more than 16 million people with Mastercard, Visa and UnionPay; dozens of banks, IDB among them, are barred from dollar business.",
          s=["con"], div="idb", rev="group", src=[["Shafaq News: cash, Mar 2026", CASH], ["Iraq Business News: CBI payments, Aug 2025", CBI2025], ["Zawya: Qi Card at Money20/20, Oct 2025", QIM2020], ["The New Region, Sep 2025", TNR]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
