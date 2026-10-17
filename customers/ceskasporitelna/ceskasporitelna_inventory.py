"""Česká spořitelna's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the Half-Year Report 2026 (to 30 June 2026,
authorised 1 September 2026), the Q1 2026 results (30 April 2026) and the Q1 2026 one-pager. Erste Group,
the parent, is a separate customer. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's
own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

HY26 = "https://www.csas.cz/banka/content/inet/internet/cs/half-year-report-2026.pdf"
Q1 = "https://cdn0.erstegroup.com/content/dam/cz/csas/www_csas_cz/dokumenty/Press_Release_Q1-2026.pdf"
ONE = "https://cdn0.erstegroup.com/content/dam/cz/csas/www_csas_cz/dokumenty/CS_onepager_Q1-2026_CZE.pdf"
ANNIV = "https://www.csas.cz/en/news/2025/05/09/ceska-sporitelna-continues-strong-performance-200th-anniversary-year"
PEOPLE = "https://www.csas.cz/en/about-us/our-people"
ABOUT = "https://www.csas.cz/en/about-us"
VISA23 = "https://www.finance.cz/aktuality/ceska-sporitelna-karty-visa/"
VAWARDS = "https://www.newstream.cz/money/visa-rozdala-ceny-visa-awards-partnery-ocenila-za-rozvoj-platebnich-technologii"
GPJV15 = "https://www.erstegroup.com/en/news-media/press-releases/2015/07/27"
GPNEWS = "https://cdn-gxx.dataweavers.io/-/media/global-payments/files/central-europe/news/cz-merchant-newssummer16enfinal.pdf"
HEYG = "https://www.svetandroida.cz/ceska-sporitelna-hey-george-chatbot"
EMONEY = "https://wporigin.euromoney.com/article/auh8zba20nsc4400s8okwc88w/awards/awards-for-excellence/awards-for-excellence-national-winners-2025-czech-republic/"
CRYPTO = "https://www.e15.cz/byznys/finance-a-bankovnictvi/velky-obrat-ceskych-bank-po-partners-se-k-bitcoinu-chysta-i-ceska-sporitelna-i-raiffeisenbank-1434775"
CCIT = "https://cc.cz/jsme-korporace-kde-se-ujala-umela-inteligence-i-startupy-ceska-sporitelna-vyrostla-v-it-firmu/"
BROKU = "https://www.seznamzpravy.cz/clanek/ekonomika-finance-cesko-zna-banku-roku-hlavni-oceneni-ziskala-ceska-sporitelna-292633"
SALOMON = "https://www.seznamzpravy.cz/clanek/ekonomika-byznys-rozhovory-domacnosti-si-prilepsi-rika-sef-ceske-sporitelny-294875"
LOGO = "https://www.ceskenoviny.cz/zpravy/cs-meni-logo-a-v-kampani-se-zavazuje-zlepsit-financni-situaci-svych-klientu/2307419"
CREDIT = "https://www.csas.cz/cs/osobni-finance/ucty-karty/kreditni-karta"
MOBILE = "https://www.csas.cz/cs/osobni-finance/ucty-karty/karty-platby-mobilem"
PLUS = "https://www.csas.cz/cs/osobni-finance/ucty-karty/ucet-plus"
MONEYBACK = "https://www.csas.cz/cs/osobni-finance/ucty-karty/moneyback"
BANKID = "https://www.csas.cz/cs/o-nas/bezpecnost-ochrana-dat/bankovni-identita"
MCCZ = "https://www.mastercard.com/news/europe/cs-cz/tiskove-centrum/tiskove-zpravy"
CEIC = "https://www.dr.ceicdata.com/en/czech-republic/payment-cards-statistics-by-type"
WERO = "https://banking.vision/en/development-wero-2025-2026/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · parent · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: 4.6 million clients, CZK 1,259 billion of loans and ROE of 19% in the first half of 2026, Erste Group as owner since 2000, two hundred years of savings banking, and a mission built around clients' financial health.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "CZK 14.3bn profit in H1.", "div": "cs", "rev": "alm", "products": [
            P("balance", "Balance sheet & earnings", "Net profit of CZK 14.3 billion in the first half of 2026 (CZK 12.8 billion a year earlier), ROE 19.4%, cost/income 41.5%; loans of CZK 1,259 billion (+9.5%), deposits of CZK 1,655 billion, total capital ratio 19.5% and NPLs of 1.6% at 30 June 2026. Full-year 2025 figures were not retrieved ⚠.",
              s=["con"], neo=[0, ""], src=[["ČS Half-Year Report 2026", HY26], ["ČS Q1 2026 results", Q1]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & parent", "blurb": "Salomon; Erste since 2000.", "div": "cs", "rev": "alm", "products": [
            P("leadership", "Board of directors", "CEO Tomáš Salomon (since 2016), Karel Mourek (risk), Daniela Pešková (retail), Martin Kobza (operations and IT), CFO Attila Sánta and Norbert Hovančák (both joined in 2025); 9,175 staff at 30 June 2026.",
              s=["corp"], neo=[0, ""], src=[["ČS: our people", PEOPLE], ["ČS Half-Year Report 2026", HY26]]),
            P("erste", "Erste Group", "Controlled by Erste Group Bank AG since 2000; the supervisory board is chaired by Erste CEO Peter Bosek. Not listed itself; Erste's exact stake is not stated in the sources read ⚠. A CZK 23.3 billion dividend went up to the group in the first half of 2026.",
              s=["corp"], o="A", neo=[0, "Erste Austria is Mastercard-heavy; ČS is not."], src=[["ČS: about us", ABOUT], ["ČS Half-Year Report 2026", HY26]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brand", "blurb": "200 years; bank of the year.", "div": "cs", "rev": "retail", "products": [
            P("heritage", "Heritage & brand", "Savings banking since 1825 (200th anniversary in 2025); the joint-stock company was founded on 30 December 1991 as successor to the Czech State Savings Bank. A new logo with the Erste 'S' on bright blue came with a pledge to improve clients' financial health ⚠ 2023.",
              s=["con"], o="I", neo=[0, ""], src=[["ČS: 200th anniversary year", ANNIV], ["ČS Half-Year Report 2026", HY26], ["ČTK: new logo", LOGO]]),
            P("awards", "Awards", "Mastercard Banka roku (Mastercard Bank of the Year) in 2024 and 2025, with Private Bank and Responsible Bank of the Year 2025; Euromoney Best Bank 2025 and Best Retail Bank 2026 in the Czech Republic.",
              s=["con"], neo=[0, "A Mastercard-named award, not a programme."],
              mc="Mastercard's brand is on ČS's trophy shelf but not in its wallet.",
              src=[["Seznam Zprávy: Banka roku 2025, Nov 2025", BROKU], ["Euromoney: Czech awards 2025", EMONEY], ["ČS Half-Year Report 2026", HY26]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology", "blurb": "1,500 IT staff, George.", "div": "george", "rev": "alm", "products": [
            P("tech", "George platform, IT & startups", "George is shared with Erste's other markets; about 1,500 IT specialists in more than 100 product teams, about 40 software robots, and the Seed Starter fund, which had put more than CZK 130 million into startups by 2023.",
              s=["corp"], o="B", neo=[0, ""], src=[["CzechCrunch: ČS as an IT firm, Jun 2023", CCIT]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Financial health first.", "div": "cs", "rev": "alm", "products": [
            P("strategy", "Mission & strategy", "Improve clients' financial health and support Czech prosperity; a shadow board set up in 2025 reviewed the mission and named AI as a key challenge. No ČS-level numeric targets were found ⚠; Erste Group's targets apply.",
              s=["corp"], neo=[0, ""], src=[["Seznam Zprávy: Salomon interview", SALOMON]]),
            P("deals", "Deals & disposals", "Merchant acquiring carved out into a Global Payments joint venture in 2016; affordable-housing companies set up or bought in 2025–26; property holdings sold in April and May 2026; gains on Kooperativa shares in H1 2026.",
              s=["corp"], o="A", neo=[0, ""], src=[["ČS Half-Year Report 2026", HY26], ["Erste: Global Payments JV, Jul 2015", GPJV15]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: 4.3 million Visa debit cards, 240,000 Visa credit cards, the 2023 switch that ended Mastercard and Maestro, Apple Pay, Google Pay and virtual cards, acceptance through Global Payments, and transfers in George.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "4.3m on Visa.", "div": "cs", "rev": "retail", "products": [
            P("debit", "Debit cards", "About 4.3 million active debit cards (4.53 million cards in all, up 7% in a year), included with Účet Plus and Standard; all on Visa since 2023.", short="Debit (Visa)",
              s=["con", "young"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["ČS Half-Year Report 2026", HY26], ["finance.cz: Visa only, Apr 2023", VISA23]]),
            P("multicurrency", "Multi-currency card", "One account and card for up to 10 currencies; George picks the currency so clients pay and withdraw abroad without conversion fees.",
              s=["con"], lc="move", neo=[0, "Visa."], src=[["ČS: Účet Plus", PLUS]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit & business cards", "blurb": "240,000 credit cards.", "div": "cs", "rev": "retail", "products": [
            P("credit", "Kreditní karta", "239,760 active credit cards at 30 June 2026; CZK 50 a month, up to 55 days interest-free, 1% back on online and foreign payments up to CZK 350 a month, discounted airport lounges. Network not named on the page; Visa under the 2023 policy ⚠.", short="Credit (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa ⚠."], src=[["ČS: credit card", CREDIT], ["ČS Half-Year Report 2026", HY26]]),
            P("premier", "Erste Premier & Private Banking cards", "Cards for the Premier and Private Banking segments, moved from Mastercard to Visa by 30 November 2023; card tier names not confirmed ⚠.",
              s=["saver"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["finance.cz: Visa only, Apr 2023", VISA23]]),
            P("corpcards", "Business & corporate cards", "All corporate cards moved to Visa by 30 November 2023.",
              s=["sme", "corp"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["finance.cz: Visa only, Apr 2023", VISA23]]),
        ]},
        {"id": "2.3", "ic": "refresh-cw", "name": "The 2023 switch", "blurb": "Mastercard out.", "div": "cs", "rev": "retail", "products": [
            P("switch", "Mastercard & Maestro retired", "Announced 6 April 2023: about 15% of card clients held Mastercard or Maestro. Personal cards stopped on 31 August 2023; Premier, Private Banking and corporate cards on 30 November 2023. One network, the bank said, makes innovation, loyalty and discounts simpler. Visa then named ČS its number-one Czech issuer.", short="Mastercard retired",
              s=["con", "corp"], lc="everyday", st="retired", ay="Apr 2023", o="P", at="Visa", neo=[0, "Moved to Visa in 2023."],
              mc="The defining loss: Mastercard's 15% of ČS cards went to Visa.",
              src=[["finance.cz: Visa only, Apr 2023", VISA23], ["Newstream: Visa Awards, Apr 2023", VAWARDS]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Wallets & virtual cards", "blurb": "Apple, Google, Garmin.", "div": "george", "rev": "retail", "products": [
            P("wallets", "Apple Pay, Google Pay & Garmin Pay", "Phone and watch payments on ČS cards.",
              s=["con", "young"], lc="everyday", o="P", at="Apple, Google, Garmin", neo=[0, "Visa tokens ⚠."], src=[["ČS: mobile payments", MOBILE]]),
            P("virtual", "Virtual cards", "One-time and permanent virtual cards created in George; Visa's 2023 award for the best digital proposition in Czechia.",
              s=["con"], lc="everyday", o="B", neo=[0, "Visa."], src=[["ČS: mobile payments", MOBILE], ["Newstream: Visa Awards, Apr 2023", VAWARDS]]),
            P("clicktopay", "Click to Pay", "Saved-card checkout online, offered on ČS cards.",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa Click to Pay ⚠."], src=[["ČS: mobile payments", MOBILE]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance & ATMs", "blurb": "Global Payments; 1,501 ATMs.", "div": "gp", "rev": "corp", "products": [
            P("acquiring", "Merchant acquiring (Global Payments)", "ČS's acquiring business moved in June 2016 into Global Payments s.r.o., Prague, with the same staff: Global Payments and CaixaBank 51%, Erste 49% ⚠ current stake. It accepts every scheme.",
              s=["sme"], lc="move", o="P", at="Global Payments", neo=[1, "Accepts every network."],
              mc="Mastercard's main remaining touchpoint with ČS clients.",
              src=[["Erste: Global Payments JV, Jul 2015", GPJV15], ["Global Payments: Czech newsletter, 2016", GPNEWS]]),
            P("atms", "ATMs & payment machines", "1,501 ATMs and payment machines at 30 June 2026, the widest network in the country.",
              s=["con"], lc="everyday", neo=[1, "Accepts every network."], src=[["ČS Half-Year Report 2026", HY26], ["ČS one-pager Q1 2026", ONE]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Transfers", "blurb": "Payments in George.", "div": "george", "rev": "retail", "products": [
            P("transfers", "Domestic & instant transfers", "Koruna and foreign transfers in George and George Business. Instant-payment and QR volumes were not found ⚠; Wero is spreading in Western Europe but no Czech bank was found among its members ⚠.",
              s=["con", "sme"], lc="move", neo=[0, "Account-to-account."], src=[["ČS: Účet Plus", PLUS], ["banking.vision: Wero 2025–26", WERO]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: George security and card controls, Bank iD for the state and private firms, the Hey George assistant on GPT-4o, and Moneyback cashback and Level Up points.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security", "blurb": "George approves payments.", "div": "george", "rev": "retail", "products": [
            P("security", "Security & card controls", "The George app approves logins and online card payments; clients block cards and switch online payments on or off in George. Fraud figures were not found ⚠.",
              s=["con"], lc="everyday", o="B", neo=[0, ""],
              mc="Instant transfers and digital logins carry scam risk that network-agnostic tools address.",
              src=[["ČS: Bank iD", BANKID], ["Svět Androida: Hey George, Dec 2024", HEYG]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Bank iD", "blurb": "A digital ID card.", "div": "george", "rev": "retail", "products": [
            P("bankid", "Bankovní identita", "Free digital identity for every George user: logs into Portál občana, eRecepty, Moje daně, the trade register, e-shops, energy firms, insurers and telcos; managed in George.",
              s=["con", "sme"], lc="open", o="P", at="Czech Bank iD", neo=[0, ""], src=[["ČS: Bank iD", BANKID]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "Hey George", "blurb": "GPT-4o assistant.", "div": "george", "rev": "retail", "products": [
            P("heygeorge", "Hey George", "Launched 3 December 2024 as the first virtual assistant at a Czech bank, built on OpenAI's GPT-4o after more than a year of work; answers questions about a client's own transactions, with a financial-adviser role planned.",
              s=["con"], lc="everyday", st="new", ay="Dec 2024", o="P", at="OpenAI", neo=[0, ""],
              mc="Merchant data and agentic payments are open ground; ČSOB tested an AI purchase with Mastercard in 2026 ⚠.",
              src=[["Svět Androida: Hey George, Dec 2024", HEYG], ["Euromoney: Czech awards 2025", EMONEY]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards & financial health", "blurb": "Moneyback, Level Up.", "div": "cs", "rev": "retail", "products": [
            P("moneyback", "Moneyback", "Card-linked cashback at dozens of merchants, switched on in George; ČS estimates average savings of CZK 4,917 a year. The operator is not named ⚠.",
              s=["con"], lc="grow", o="P", neo=[0, "On Visa cards."],
              mc="Merchant offers content could widen a programme that runs on Visa cards.",
              src=[["ČS: Moneyback", MONEYBACK]]),
            P("levelup", "Level Up", "Points for holding ČS products that unlock further benefits.",
              s=["con"], lc="grow", o="B", neo=[0, ""], src=[["ČS: credit card", CREDIT]]),
            P("fithealth", "Financial health tools", "Round-up saving ('Platím a spořím') from every card payment, and Skoala financial education reaching 3,685 schools.",
              s=["con", "young"], lc="grow", o="B", neo=[0, ""], src=[["ČS: Účet Plus", PLUS], ["ČS one-pager Q1 2026", ONE]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What clients buy: 28% of new Czech mortgages and affordable rental flats, current accounts and CZK 100 billion of consumer loans, pensions, building savings and insurance, CZK 424 billion of funds, and lending to firms and the public sector.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Mortgages & housing", "blurb": "28% of new mortgages.", "div": "cs", "rev": "retail", "products": [
            P("mortgages", "Mortgages", "Mortgage book up 11.2% in a year; 28% of newly originated Czech mortgages in the first half of 2026.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["ČS Half-Year Report 2026", HY26]]),
            P("housing", "Dostupné bydlení ČS", "Affordable rental housing: 695 flats completed, with new project companies in Barrandov, Strašnice and Harfa in 2026.",
              s=["home"], lc="beyond", st="new", o="B", neo=[0, ""], src=[["ČS one-pager Q1 2026", ONE], ["ČS Half-Year Report 2026", HY26]]),
        ]},
        {"id": "4.2", "ic": "wallet", "name": "Accounts & loans", "blurb": "4.6m clients.", "div": "cs", "rev": "retail", "products": [
            P("accounts", "Current accounts", "Účet Plus (free with four card payments a month), Standard, and accounts for children, students and seniors; 4.58 million clients at 30 June 2026.",
              s=["con", "young"], lc="open", neo=[0, "Visa debit."], src=[["ČS: Účet Plus", PLUS], ["ČS Half-Year Report 2026", HY26]]),
            P("consumer", "Consumer loans", "Consumer lending above CZK 100 billion, up 9.3% in a year after a lending campaign; instant loans in George.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["ČS Q1 2026 results", Q1], ["ČS Half-Year Report 2026", HY26]]),
        ]},
        {"id": "4.3", "ic": "hand-coins", "name": "Pensions, savings & insurance", "blurb": "912,000 pension savers.", "div": "pension", "rev": "retail", "products": [
            P("pensions", "ČS penzijní společnost", "912,000 clients save for retirement with ČS; the pension company earned CZK 680 million in the first half of 2026.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["ČS one-pager Q1 2026", ONE], ["ČS Half-Year Report 2026", HY26]]),
            P("buildsav", "Stavební spořitelna ČS", "Building savings and housing loans; building-society loans up 6.3%, profit CZK 551 million in H1 2026.",
              s=["saver", "home"], lc="grow", neo=[0, ""], src=[["ČS Half-Year Report 2026", HY26]]),
            P("insurance", "Insurance", "Life and non-life insurance sold through the bank: CZK 1.2 billion of fee income in H1 2026; partner not confirmed ⚠ (Kooperativa).",
              s=["con", "home"], lc="grow", o="P", neo=[0, ""], src=[["ČS Half-Year Report 2026", HY26]]),
        ]},
        {"id": "4.4", "ic": "trending-up", "name": "Investments & private banking", "blurb": "780,000 investors.", "div": "cs", "rev": "retail", "products": [
            P("invest", "Funds & George Invest", "780,000 investing clients; retail mutual funds of CZK 423.5 billion, up 21% in a year.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["ČS one-pager Q1 2026", ONE], ["ČS Half-Year Report 2026", HY26]]),
            P("private", "Erste Premier & Private Banking", "Wealth segments, Private Bank of the Year 2025.",
              s=["saver"], lc="grow", neo=[0, "Visa cards."], src=[["Seznam Zprávy: Banka roku 2025, Nov 2025", BROKU]]),
            P("crypto", "Crypto ETFs & bitcoin", "Bitcoin, ether and solana ETFs in George; direct crypto purchase is being prepared with no date ⚠.",
              s=["saver"], lc="grow", st="flux", neo=[0, ""], src=[["e15: banks and bitcoin, 2026", CRYPTO]]),
        ]},
        {"id": "4.5", "ic": "building-2", "name": "Business & corporate", "blurb": "CZK 466bn of loans.", "div": "cs", "rev": "corp", "products": [
            P("sme", "Small business banking", "Accounts, cards and loans for micro and small firms; SME loans up 5.2%.",
              s=["sme"], lc="everyday", neo=[0, "Visa business cards."], src=[["ČS Half-Year Report 2026", HY26]]),
            P("corporate", "Corporate & public sector", "Corporate loans of CZK 466.3 billion, up 9.1%: large corporates +14.2%, public sector +19.2%; markets and financial-institutions business in Group Markets.",
              s=["corp"], lc="borrow", neo=[0, "Visa corporate cards."], src=[["ČS Half-Year Report 2026", HY26]]),
            P("leasing", "Leasing & factoring", "Leasing České spořitelny (CZK 200 million H1 profit) and Factoring České spořitelny (CZK 67 million).",
              s=["sme", "corp"], lc="borrow", neo=[0, ""], src=[["ČS Half-Year Report 2026", HY26]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How clients reach the bank: George for almost 2.7 million digital users, George Business for every firm by the end of 2026, and 332 branches with the country's largest ATM network.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "George", "blurb": "2.7m digital users.", "div": "george", "rev": "retail", "products": [
            P("george", "George app & web", "Almost 2.7 million digital users and 2.45 million on mobile; second in Mobile App of the Year 2025 behind Air Bank.",
              s=["con", "young", "saver"], lc="everyday", o="B", neo=[0, ""], src=[["ČS Half-Year Report 2026", HY26], ["ČS one-pager Q1 2026", ONE], ["Seznam Zprávy: Banka roku 2025, Nov 2025", BROKU]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "George Business", "blurb": "All firms by end-2026.", "div": "george", "rev": "corp", "products": [
            P("georgebiz", "George Business", "More than 10,000 business clients migrated by April 2026, with all of them due by the end of 2026.",
              s=["sme", "corp"], lc="everyday", st="flux", o="B", neo=[0, ""],
              mc="A migration under way: the moment to add open-finance and spend tools.",
              src=[["ČS Q1 2026 results", Q1]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & partners", "blurb": "332 branches.", "div": "cs", "rev": "retail", "products": [
            P("branches", "Branches", "332 physical branches at 30 June 2026 (336 a year earlier), the most in the country.",
              s=["con", "home"], lc="open", neo=[0, ""], src=[["ČS Half-Year Report 2026", HY26], ["ČS one-pager Q1 2026", ONE]]),
            P("partners", "Partners", "Visa for cards, Global Payments for acceptance, OpenAI for Hey George, Apple, Google and Garmin for wallets, and Seed Starter startups such as wflow inside George.",
              s=["corp"], lc="beyond", o="P", at="Visa, Global Payments, OpenAI", neo=[0, ""], src=[["CzechCrunch: ČS as an IT firm, Jun 2023", CCIT], ["ČS: mobile payments", MOBILE]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at ČS", "blurb": "Gone from the cards since 2023.", "products": [
        P("mcatcs", "Mastercard at Česká spořitelna", "ČS has issued only Visa cards since the end of 2023, after moving about 15% of its card clients off Mastercard and Maestro; Visa named it its top Czech issuer. Mastercard still reaches ČS's merchants through Global Payments, and its name is on the Banka roku award ČS won in 2024 and 2025. Erste's Austrian bank, by contrast, is Mastercard-heavy.",
          s=["con"], div="cs", rev="alm", mc="The relationship this map is drawn for.",
          src=[["finance.cz: Visa only, Apr 2023", VISA23], ["Seznam Zprávy: Banka roku 2025, Nov 2025", BROKU]]),
    ]},
    {"id": "pillar-market", "name": "Czech banking", "blurb": "Visa-led, A2A rising.", "products": [
        P("market", "The Czech market", "About 8.2 million Mastercard cards in Czechia (September 2025), carried by other issuers such as Air Bank (renewed to 2028) and ČSOB; Moneta and UniCredit went Visa-only like ČS. Bank iD and instant transfers are shared bank rails; Wero has not reached Czechia ⚠.",
          s=["con"], div="cs", rev="alm", src=[["CEIC: Czech card statistics", CEIC], ["Mastercard Czech press releases ⚠", MCCZ], ["finance.cz: Visa only, Apr 2023", VISA23]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
