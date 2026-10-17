"""Grupo Financiero Banorte's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 2T26 report (July 2026), the 2Q26 corporate
presentation, the 4T25 report (29 January 2026) and the 2025 Integrated Annual Report. Amounts are pesos (Ps).
banorte.com and Mastercard's newsroom could not be read on 17 October 2026, so card networks rest on Banorte's
reports and press. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://www.latibex.com/docs/Documentos/esp/resulta/2026/2T26.pdf"
Q4 = "https://www.latibex.com/docs/Documentos/esp/resulta/2026/20260129%204T25.pdf"
AR25 = "https://investors.banorte.com/~/media/Files/B/Banorte-IR/financial-information/annual-reports/en/2026/AnnualReport2025_ENG.pdf"
CP = "https://investors.banorte.com/~/media/Files/B/Banorte-IR/presentation/en/2026/2Q26/GFNortes%20Corporate%20Presentation%202Q26_public_fv1.pdf"
CUE24 = "https://investors.banorte.com/~/media/Files/B/Banorte-IR/financial-information/annual-reports/en/2025/GFNORTE-%20Annual%20Report%202024_CUE_CorrectionArrendadora.pdf"
AR24 = "https://investors.banorte.com/~/media/Files/B/Banorte-IR/financial-information/annual-reports/en/2025/Integrated%20Annual%20Report%202024_-_-_.pdf"
CFO = "https://investors.banorte.com/~/media/Files/B/Banorte-IR/press-release/en/2026/_MatEv%20_%20Changes%20in%20Organizational%20Structure_21072_final__.pdf"
TDFAPR = "https://investors.banorte.com/~/media/Files/B/Banorte-IR/press-release/en/2025/Material%20Event%20-%2015abr.pdf"
TDF = "https://investors.banorte.com/~/media/Files/B/Banorte-IR/press-release/en/2025/MatEv_%20Acq%20TDF_%20Dec25_.pdf"
BINEO = "https://investors.banorte.com/~/media/Files/B/Banorte-IR/press-release/en/2025/MatEv_Bineo.pdf"
TU = "https://investors.banorte.com/~/media/Files/B/Banorte-IR/press-release/en/2026/MatEv_TransU_Mar2.pdf"
AMEX08 = "https://banorte-ir.prod-use1.investis.com/~/media/Files/B/Banorte-IR/press-release/es/2008/30jul08.pdf"
AMAZON = "https://www.milenio.com/negocios/banorte-amazon-trabajaran-juntos-carlos-hank-gonzalez"
SOCIO7 = "https://www.banorte.com/cms/NOTICIASBANORTE/2018/Noticias/4-feb_26_BANORTE-Y-7-ELEVEN-LANZAN-SOCIO-7.pdf"
MARRIOTT = "https://www.mdzol.com/dinero/2021/4/22/las-nuevas-tarjetas-de-credito-de-banorte-marriott-mastercard-154007.html"
RAPPI21 = "https://expansion.mx/economia/2021/01/25/banorte-se-alia-con-rappi-para-dar-creditos-a-negocios-y-clientes"
BLRAPPI = "https://www.bloomberglinea.com/latinoamerica/mexico/banorte-compra-todo-el-negocio-de-rappicard-por-us50-millones/"
RANKIA = "https://www.rankia.mx/blog/tarjetas-bancarias-credito-debito-prepago-virtuales/4332028-tarjeta-credito-banorte-clasica-vs-oro"
UNIVERSE = "https://www.banorte.com/universe"
PAYPAL = "https://www.xataka.com.mx/aplicaciones/banorte-es-el-primer-banco-en-mexico-que-firma-una-alianza-con-paypal-pero-no-sabemos-que-beneficios-traera"
WIKI = "https://es.wikipedia.org/wiki/Banco_Mercantil_del_Norte"
WIKIEN = "https://en.wikipedia.org/wiki/Banorte"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · ownership · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Ps 1.27 trillion of performing loans and a 25.7% ROE, Mexico's only large bank in Mexican hands, roots in 1899 Monterrey, a cloud-and-AI technology base, and the 4,5,6 Plan that bought all of RappiCard and is selling Bineo.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Ps 15.6bn a quarter, ROE 25.7%.", "div": "gfn", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Net income of Ps 15,550 million in 2Q26 (+6%) and Ps 58,788 million in 2025; performing loans of Ps 1,273 billion (+8%), deposits of Ps 1,199 billion, ROE 25.7%, efficiency 36.2%, NPL ratio 1.50% and CET1 12.55% at 30 June 2026. Guidance for 2026 is Ps 62–64 billion of net income.",
              s=["corp"], neo=[0, ""], src=[["GFNorte 2T26 report", Q2], ["Corporate presentation 2Q26", CP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "Hank González and Ramírez.", "div": "gfn", "rev": "group", "products": [
            P("govern", "Listing, ratings & board", "Listed on the BMV (GFNORTEO), OTCQX and Latibex, with a market value of US$29.7 billion and a float of about 87% at 30 June 2026; the only large Mexican bank not controlled by a foreign group. Rated BBB by S&P (negative outlook, May 2026), Baa2 by Moody's and BBB- by Fitch (positive). A 13-member board, about 64% independent.",
              s=["corp"], neo=[0, ""], src=[["Corporate presentation 2Q26", CP], ["GFNorte 2T26 report", Q2], ["Wikipedia: Banorte", WIKIEN]]),
            P("leadership", "Executive team", "Chairman Carlos Hank González; CEO Marcos Ramírez Miguel; COO Rafael Arana, who leads transformation, technology and AI; CFO Tomás Lozano (from 21 July 2026); José Francisco Martha runs digital businesses, Mario Barraza retail and Armando Rodal wholesale banking.",
              s=["corp"], st="new", neo=[0, ""], src=[["Banorte: organisational change, Jul 2026", CFO], ["2025 annual report", AR25]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "Monterrey, 1899.", "div": "bank", "rev": "banking", "products": [
            P("heritage", "Heritage & brands", "Banco Mercantil de Monterrey (licensed 1899) and Banco Regional del Norte (1947) merged in 1986 and were privatised in 1992; Bancrecer, Ixe (2011) and Interacciones (2018) followed. Estadio Azteca became Estadio Banorte in March 2025.",
              s=["con"], o="I", neo=[0, ""], src=[["Wikipedia: Banco Mercantil del Norte", WIKI], ["Wikipedia: Banorte", WIKIEN]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Google Cloud, Azure, Red Hat.", "div": "gfn", "rev": "group", "products": [
            P("tech", "Cloud, AI & payment engine", "An AI and cloud alliance with Google Cloud (renewed 2025), Red Hat OpenShift AI as the base for generative-AI assistants (May 2026), Copilot Chat for more than 18,000 employees, a corporate platform on Microsoft Azure and its own acquiring engine, which cleared more than 167 million transactions in one month of 2025.",
              s=["corp"], o="B", neo=[0, ""], src=[["2025 annual report", AR25], ["GFNorte 2T26 report", Q2]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "All of Rappi, Bineo sold.", "div": "gfn", "rev": "group", "products": [
            P("strategy", "4,5,6 Plan", "Hyper-personalisation across the best experience, the best personalised offer and the best business operation; 2026 adds a virtual-assistant launch, the sale of Bineo and full ownership of RappiCard. Guidance: loans +8–11%, ROE 22–24%.",
              s=["corp"], st="new", neo=[0, ""], src=[["Corporate presentation 2Q26", CP]]),
            P("deals", "Deals", "Bought Rappi's 44.28% of Tarjetas del Futuro for US$50 million (closed 17 December 2025) with an exclusive 15-year agreement; sold its Trans Union de México stake (March 2026); holds 19.73% of Controladora Prosa, the card processor in which Visa agreed to take 51% (December 2023).",
              s=["corp"], o="A", neo=[0, "Prosa is now Visa-controlled ⚠."], src=[["Banorte: TDF acquisition, Apr 2025", TDFAPR], ["Banorte: TDF closing, Dec 2025", TDF], ["Banorte: Trans Union sale, Mar 2026", TU], ["2024 annual report (CNBV)", CUE24]]),
            P("bineo", "Bineo", "Mexico's first fully digital bank with its own licence (launched January 2024), being sold to Clearscope, a Klar subsidiary (agreed September 2025, antitrust cleared December 2025, closing pending at 2Q26).",
              s=["young"], div="bineo", st="flux", ay="Sep 2025", o="B", neo=[None, "Network not public."], src=[["Banorte: Bineo sale, Sep 2025", BINEO], ["GFNorte 4T25 report", Q4]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: own-brand credit cards led by Visa, a Mastercard Marriott co-brand, 1.3 million RappiCards on Visa, 14.6 million debit cards split across both networks, wallets, an acquiring business with 269,000 terminals, and SPEI transfers and US remittances.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Own-brand credit cards", "blurb": "Ps 80.6bn, third in Mexico.", "div": "bank", "rev": "banking", "products": [
            P("credit", "Clásica & Oro", "The core range, both on Visa (2024); the card book reached Ps 80.6 billion in 2Q26 (+12%), an 11.5% share and third place; cards with billing rose 12% in 2025 and 192,520 cards were issued digitally.", short="Clásica & Oro (Visa)",
              s=["con"], lc="borrow", o="B", at="Visa", neo=[0, "Visa."], src=[["Rankia: Clásica vs Oro, Apr 2024", RANKIA], ["GFNorte 2T26 report", Q2], ["2025 annual report", AR25]]),
            P("premium", "Platinum & Infinite", "Premium cards with lounge access; Infinite is a Visa Infinite card ⚠ and Platinum's network is not confirmed.",
              s=["aff"], lc="borrow", o="P", at="Visa", neo=[0, "Visa Infinite ⚠; Platinum unconfirmed."], src=[["Banorte: United Universe and premium cards", UNIVERSE]]),
            P("conmigo", "Banorte Conmigo & OneUp", "Launched in 2024: Conmigo, a low-cost card for payroll customers building a credit history, and OneUp, a digital card that Banorte calls its most successful launch.",
              s=["young", "con"], lc="borrow", st="new", ay="2024", o="B", neo=[None, "Network not confirmed."], src=[["2025 annual report", AR25]]),
        ]},
        {"id": "2.2", "ic": "plane", "name": "Co-brand cards", "blurb": "Marriott on Mastercard.", "div": "bank", "rev": "banking", "products": [
            P("marriott", "Marriott Bonvoy & Bonvoy Inspire", "Co-brand credit cards with Marriott, launched in April 2021 on Mastercard with Priceless access ⚠.", short="Marriott Bonvoy (Mastercard)",
              s=["aff"], lc="borrow", ay="Apr 2021", o="P", at="Marriott, Mastercard", neo=[2, "Mastercard ⚠."],
              mc="Mastercard's main credit foothold at Banorte.",
              src=[["MDZ: Banorte Marriott Mastercard cards, Apr 2021", MARRIOTT], ["2025 annual report", AR25]]),
            P("united", "United cards", "Co-brand cards with United Airlines, including United Universe, earning MileagePlus miles; the network is not confirmed ⚠.",
              s=["aff"], lc="borrow", o="P", at="United Airlines", neo=[None, "Network not confirmed."], src=[["Banorte: United Universe", UNIVERSE], ["2025 annual report", AR25]]),
        ]},
        {"id": "2.3", "ic": "smartphone", "name": "RappiCard", "blurb": "1.3 million cards on Visa.", "div": "rappi", "rev": "banking", "products": [
            P("rappicard", "RappiCard", "A no-fee cash-back credit card sold inside the Rappi app since 2021, on Visa; about 1.3 million cards, most holders under 36. Banorte bought Rappi's stake (closed December 2025), moved the book onto the bank and has a 15-year exclusive agreement reaching about 7.4 million active Rappi users.", short="RappiCard (Visa)",
              s=["young"], lc="borrow", st="flux", ay="Dec 2025", o="A", at="Rappi, Visa", neo=[0, "Visa."],
              mc="1.3 million young cardholders being rebuilt into a multiproduct offer.",
              src=[["Expansión: RappiCard with Visa, Jan 2021", RAPPI21], ["Banorte: TDF closing, Dec 2025", TDF], ["Corporate presentation 2Q26", CP], ["Bloomberg Línea: RappiCard, Apr 2025", BLRAPPI]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Debit", "blurb": "14.6m cards, both networks.", "div": "bank", "rev": "banking", "products": [
            P("debit", "Debit cards", "A portfolio of 14.6 million debit cards ⚠ (the report also gives 14.0 million), more than 90% without printed data; 7.5 million payroll cards in the national-team design in 2025; debit billing +13.4%. Visa Platinum debit sits alongside Mastercard programmes.",
              s=["con"], lc="everyday", o="B", neo=[1, "Split: Visa and Mastercard programmes."], src=[["2025 annual report", AR25]]),
            P("mujer", "Mujer Banorte", "An account for women with insurance, savings buckets and a debit card with Mastercard Priceless experiences: 600,513 accounts in 2025.", short="Mujer Banorte (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard, with Priceless."], src=[["2025 annual report", AR25]]),
            P("worldelite", "World Elite debit", "A premium debit card on Mastercard World Elite, issued on recycled plastic in 2025.",
              s=["aff"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard World Elite."], src=[["2025 annual report", AR25]]),
            P("partnerdebit", "Amazon Recargable & Socio 7", "Reloadable debit cards on Mastercard: Amazon Recargable with Amazon (March 2018) and Socio 7, sold in 7-Eleven stores (2018 ⚠).", short="Partner debit (Mastercard)",
              s=["young"], lc="open", ay="Mar 2018", o="P", at="Amazon, 7-Eleven, Mastercard", neo=[2, "Mastercard ⚠ current status."], src=[["Milenio: Amazon Recargable, Mar 2018", AMAZON], ["Banorte: Socio 7, 2018", SOCIO7]]),
        ]},
        {"id": "2.5", "ic": "wallet", "name": "Wallets", "blurb": "Wallet billing up 158%.", "div": "bank", "rev": "banking", "products": [
            P("wallets", "Digital cards & wallets", "Digital cards, Apple Pay, Google Pay and Garmin Pay; in 2025 wallet billing rose 158% on credit and 212% on debit, and digital cards made up 24% and 31% of card-not-present billing. PayPal linking since October 2017.",
              s=["con", "young"], lc="move", st="new", o="P", at="Apple, Google, Garmin, PayPal", neo=[1, "Tokens on both networks."], src=[["2025 annual report", AR25], ["Xataka: Banorte and PayPal, Oct 2017", PAYPAL]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acquiring", "blurb": "268,877 terminals.", "div": "bank", "rev": "banking", "products": [
            P("acquiring", "Merchant acquiring", "268,877 POS terminals (2Q26) and more than 178,000 affiliations, Tap to Phone on Android and A920 Pro smart terminals; third by affiliated merchants (10.78% share), ninth-largest acquirer in Latin America (Nilson, 2024); American Express accepted through OptBlue.",
              s=["sme"], lc="move", o="B", at="American Express (OptBlue)", neo=[1, "Accepts every network."], src=[["Corporate presentation 2Q26", CP], ["2025 annual report", AR25], ["2024 integrated report", AR24]]),
            P("prosa", "Prosa stake", "Banorte holds 19.73% of Controladora Prosa; Visa agreed to buy 51% of Prosa, a main Mexican card processor, in December 2023 ⚠ completion not confirmed.",
              s=["corp"], div="gfn", rev="group", o="P", at="Visa", neo=[0, "Visa-controlled processor ⚠."],
              mc="A structural tie between Banorte and Visa.",
              src=[["2024 annual report (CNBV)", CUE24]]),
        ]},
        {"id": "2.7", "ic": "send", "name": "Transfers & remittances", "blurb": "SPEI and UniTeller.", "div": "bank", "rev": "banking", "products": [
            P("spei", "SPEI transfers", "Real-time transfers on Banxico's SPEI from Banorte Móvil, with saved recipients and cardless cash codes; mobile monetary transactions grew 29% in the year to 2Q26.",
              s=["con", "sme"], lc="move", o="B", neo=[0, "Banxico's SPEI."], src=[["Corporate presentation 2Q26", CP], ["2025 annual report", AR25]]),
            P("uniteller", "UniTeller & remittances", "UniTeller, Banorte's US remittance company, bought MORE Payment Evolution (Uruguay) in 2023–24; 'Solicitar una Remesa' in Banorte Móvil lets customers request money from the US (January 2026).",
              s=["con"], div="uniteller", lc="move", st="new", ay="Jan 2026", o="A", neo=[0, "Own network."],
              mc="Remittance inflows are untouched ground for Mastercard Move.",
              src=[["2024 annual report (CNBV)", CUE24], ["GFNorte 4T25 report", Q4]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: SIM-based identity checks and fraud tools, the Maya assistant and hyper-personalisation, APIs into dealers and accounting software, and loyalty programmes with Priceless on the Mastercard cards.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "True ID, Cleafy.", "div": "bank", "rev": "banking", "products": [
            P("fraud", "Fraud & identity", "True ID checks the SIM behind each phone (successful log-ins +93.5%), Cleafy protects digital identity in Banorte Móvil, biometric authentication for companies, and PCI-DSS certification.",
              s=["con", "sme"], lc="everyday", o="P", at="Cleafy", neo=[0, "Banorte's own and Cleafy."],
              mc="Scam scoring on SPEI transfers would add network intelligence.",
              src=[["2025 annual report", AR25]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "Data, AI & APIs", "blurb": "Maya, 2m messages a month.", "div": "bank", "rev": "banking", "products": [
            P("maya", "Maya", "A virtual assistant in the app and portal handling more than 2 million messages a month, with a 'Maya Virtual Supervisor' and Maya services in branches.",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="Agent Pay is untouched ground.",
              src=[["2025 annual report", AR25], ["Corporate presentation 2Q26", CP]]),
            P("hyper", "Hyper-personalisation", "A central database and analytics behind next-best offers; digital sales reached 32% of the total in 2025 and digital card activation rose from 27% to 87%.",
              s=["con", "young"], lc="open", o="B", neo=[0, ""], src=[["2025 annual report", AR25]]),
            P("apis", "APIs & integrations", "The only bank with a car-loan quoting API inside partners' portals, a CONTPAQi bank feed for SMEs (June 2026) and a data platform for 211,000 corporate users.",
              s=["sme", "home"], lc="beyond", st="new", o="P", at="CONTPAQi", neo=[0, ""], src=[["2025 annual report", AR25], ["GFNorte 2T26 report", Q2]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty", "blurb": "Recompensa Total.", "div": "bank", "rev": "banking", "products": [
            P("rewards", "Recompensa Total & Mi Tarjeta Favorita", "Points redeemable for travel, goods or purchases, usage rewards with 2.3 million customers in Mi Tarjeta Favorita, and Priceless experiences on Mastercard programmes.",
              s=["con", "aff"], lc="everyday", o="B", neo=[1, "Priceless on Mastercard programmes."], src=[["2025 annual report", AR25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: second place in mortgages, car loans, payroll loans, commercial and government lending, SME loans, and insurance, annuities, the Afore and funds through Banorte Ahorro y Previsión.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Mortgages", "blurb": "19.9%, second.", "div": "bank", "rev": "banking", "products": [
            P("mortgages", "Mortgages", "Ps 297.7 billion at 2Q26 (+5%), a 19.9% share and second place; approval cut to 18 days.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["GFNorte 2T26 report", Q2], ["2025 annual report", AR25]]),
        ]},
        {"id": "4.2", "ic": "gauge", "name": "Auto loans", "blurb": "+26%, Hyundai's partner.", "div": "bank", "rev": "banking", "products": [
            P("auto", "Auto loans", "Ps 76.9 billion (+26%), a 20.6% share and second place; principal finance partner of Hyundai Motor de México from December 2025.",
              s=["home"], lc="borrow", st="new", o="P", at="Hyundai", neo=[0, ""], src=[["GFNorte 2T26 report", Q2], ["GFNorte 4T25 report", Q4]]),
        ]},
        {"id": "4.3", "ic": "hand-coins", "name": "Payroll loans", "blurb": "22.0%, second.", "div": "bank", "rev": "banking", "products": [
            P("payroll", "Payroll accounts & loans", "Payroll loans of Ps 98.8 billion (+14%), a 22.0% share; payroll accounts are a main source of card customers.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["GFNorte 2T26 report", Q2]]),
        ]},
        {"id": "4.4", "ic": "briefcase", "name": "SMEs", "blurb": "Ps 64bn, Mujer PyME.", "div": "bank", "rev": "banking", "products": [
            P("sme", "SME banking", "SME loans of Ps 64.1 billion (+7%); Mujer PyME has made more than 1,500 loans worth over Ps 3 billion since May 2024; BePYME CRM for account executives.",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["GFNorte 2T26 report", Q2], ["2025 annual report", AR25]]),
        ]},
        {"id": "4.5", "ic": "factory", "name": "Corporate & government", "blurb": "27.4% of government loans.", "div": "bank", "rev": "banking", "products": [
            P("corporate", "Commercial & corporate banking", "Commercial loans of Ps 325.7 billion and corporate Ps 230.0 billion (12.4% share, second); trade finance named best in Mexico by Global Finance (2026).",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["GFNorte 2T26 report", Q2]]),
            P("government", "Government banking", "Loans to federal, state and municipal governments of Ps 163.5 billion, a 27.4% share and second place.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["GFNorte 2T26 report", Q2]]),
            P("corpcards", "Corporate cards", "American Express became the issuer of Banorte's corporate cards in July 2008 ⚠ current status.",
              s=["corp"], lc="move", ay="Jul 2008", o="P", at="American Express", neo=[0, "American Express."],
              mc="Commercial and virtual cards are open ground.",
              src=[["Banorte and American Express, Jul 2008", AMEX08]]),
        ]},
        {"id": "4.6", "ic": "coins", "name": "Insurance, pensions & funds", "blurb": "8 million Afore clients.", "div": "seguros", "rev": "bap", "products": [
            P("seguros", "Seguros & Pensiones Banorte", "Insurance (Ps 1,196 million net income in 2Q26) sold largely through the bank, and annuities through Pensiones Banorte (Ps 735 million).",
              s=["saver"], lc="grow", neo=[0, ""], src=[["GFNorte 2T26 report", Q2]]),
            P("afore", "Afore XXI Banorte", "A retirement-savings manager, 50% owned, with about 8.0 million clients.",
              s=["saver"], div="afore", lc="grow", neo=[0, ""], src=[["Corporate presentation 2Q26", CP]]),
            P("funds", "Casa de Bolsa & Operadora de Fondos", "Brokerage and mutual funds, with assets under management for the group of Ps 5.52 trillion.",
              s=["saver", "corp"], div="casa", rev="broker", lc="grow", neo=[0, ""], src=[["GFNorte 2T26 report", Q2]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: Banorte Móvil for 7.4 million users, 1,229 branches, 12,318 ATMs and 46,191 correspondents including OXXO, and partners from Rappi to car dealers.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Banorte Móvil", "blurb": "7.4 million users.", "div": "bank", "rev": "banking", "products": [
            P("app", "Banorte Móvil & digital banking", "7.38 million app users and 6,080 million transactions in 2025; 8.37 million active internet-banking customers; app NPS 82.7; named best banking app in Mexico by World Finance (2025).",
              s=["con", "young"], lc="everyday", neo=[0, ""], src=[["2025 annual report", AR25], ["Corporate presentation 2Q26", CP]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches, ATMs & correspondents", "blurb": "46,191 correspondents.", "div": "bank", "rev": "banking", "products": [
            P("branches", "Branches & ATMs", "1,229 branches and 12,318 ATMs, the second-largest ATM network, at 2Q26; ATMs historically on the Visa and Plus network.",
              s=["con"], lc="everyday", neo=[0, "ATMs on Visa/Plus."], src=[["Corporate presentation 2Q26", CP], ["2024 annual report (CNBV)", CUE24]]),
            P("correspondents", "Correspondents", "46,191 correspondent points, after more than 24,000 OXXO stores joined in December 2025, alongside Walmart, 7-Eleven and Farmacias Guadalajara.",
              s=["con"], lc="open", st="new", ay="Dec 2025", o="P", at="OXXO, Walmart, 7-Eleven", neo=[0, ""], src=[["GFNorte 4T25 report", Q4], ["Corporate presentation 2Q26", CP]]),
        ]},
        {"id": "5.3", "ic": "network", "name": "Partners", "blurb": "Rappi, dealers, Estadio.", "div": "gfn", "rev": "banking", "products": [
            P("partners", "Partners & ecosystems", "Rappi's app under a 15-year exclusive agreement, car dealers and Hyundai, CONTPAQi for SMEs, and Estadio Banorte, home of the 2026 World Cup opening.",
              s=["young", "home", "sme"], lc="open", o="P", at="Rappi, Hyundai, CONTPAQi", neo=[0, ""], src=[["Corporate presentation 2Q26", CP], ["GFNorte 4T25 report", Q4], ["Wikipedia: Banorte", WIKIEN]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Banorte", "blurb": "Marriott and debit, Visa elsewhere.", "products": [
        P("mcatbanorte", "Mastercard at Banorte", "Banorte's core Clásica and Oro credit cards and RappiCard are on Visa, Visa controls Prosa, in which Banorte holds 19.73%, and American Express issues its corporate cards. Mastercard carries the Marriott Bonvoy co-brand (2021 ⚠), the Mujer Banorte and World Elite debit cards with Priceless, and Amazon Recargable (2018). No network agreement or volume split is public.",
          s=["con"], div="gfn", rev="group", mc="The relationship this map is drawn for.",
          src=[["Rankia: Clásica vs Oro, Apr 2024", RANKIA], ["Expansión: RappiCard with Visa, Jan 2021", RAPPI21], ["2025 annual report", AR25], ["2024 annual report (CNBV)", CUE24]]),
    ]},
    {"id": "pillar-market", "name": "Mexican banking", "blurb": "BBVA first, Banorte second.", "products": [
        P("market", "The Mexican market", "Banorte is second in loans (15.1%) and deposits (14.1%) behind BBVA México and third in cards (11.5%) behind BBVA (32.4%) and Banamex (23.7%) at May 2026. Banxico cut its rate to 6.50%; Moody's cut Mexico to Baa3 in May 2026; a new antitrust commission replaced COFECE.",
          s=["corp"], div="gfn", rev="group", src=[["Corporate presentation 2Q26", CP], ["GFNorte 2T26 report", Q2]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
