"""Banca Intesa Beograd's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the 2024 annual report (the latest on its site),
its card tariff applying from 4 May 2026 and its product pages, with 2025 results from the Serbian press and
the parent's H1 2026 release (29 July 2026). ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

BIB = "https://www.bancaintesa.rs"
ABOUT = "https://www.bancaintesa.rs/en/stanovnistvo/o-nama.html"
HIST = "https://www.bancaintesa.rs/en/stanovnistvo/o-nama/istorijat.html"
ORG = "https://www.bancaintesa.rs/document/documents/BIB/2026-01-22-BIB-O-struktura-EN.pdf"
CEO = "https://www.bancaintesa.rs/en/stanovnistvo/mi-smo-banca-intesa/darko-popovic.html"
UBS = "https://biznis.rs/vesti/darko-popovic-novi-predsednik-upravnog-odbora-udruzenja-banaka-srbije/"
AR24 = "https://www.bancaintesa.rs/document/publications/BIB/Godi%C5%A1nji-izve%C5%A1taji/Godisnji_izvestaj_2024/Godisnji%20izvestaj%202024%20SRB.pdf"
TOP6 = "https://biznis.rs/vesti/srbija/zarada-sest-najvecih-banaka-u-srbiji-iznosila-12-milijarde-evra-u-2025/"
N1 = "https://n1info.rs/biznis/banke-po-zaradama-u-prvih-100-kompanija-u-srbiji/"
EMONEY = "https://www.euromoney.com/article/bluk16wes000csk08wo0sos8c/banking/awards-for-excellence-national-winners-2026-serbia/"
KURIR = "https://biznis.kurir.rs/info-biz/10051369/banca-intesa-i-ove-godine-najbolja-banka-u-srbiji"
BANKER = "https://group.intesasanpaolo.com/it/newsroom/tutte-le-news/news/2025/banca-intesa-beograd-bank-of-the-year-2025"
ISP1H = "https://group.intesasanpaolo.com/content/dam/portalgroup/repository-documenti/investor-relations/comunicati-stampa-en/2026/07/20260729_Ris1H26_uk.pdf"
DEBIT = "https://www.bancaintesa.rs/stanovnistvo/platne-kartice/debitne-kartice.html"
CREDIT = "https://www.bancaintesa.rs/stanovnistvo/platne-kartice/kreditne-kartice.html"
TARIFF = "https://www.bancaintesa.rs/document/documents/BIB/Retail/Kartice/Kreditne-kartice/Extract-from-the-Tariff-of-fees.pdf"
APPLE = "https://www.bancaintesa.rs/stanovnistvo/digitalno-bankarstvo/apple-pay.html"
GPAY = "https://www.bancaintesa.rs/stanovnistvo/digitalno-bankarstvo/google-pay.html"
N1644 = "https://www.bancaintesa.rs/en/stanovnistvo/medija-centar/vesti/news1644.html"
N1667 = "https://www.bancaintesa.rs/en/stanovnistvo/medija-centar/vesti/news1667.html"
MCPLAT = "https://www.bancaintesa.rs/en/stanovnistvo/medija-centar/vesti/MC-simbol_prvoklasnog_servisa.html"
MCPLAT2 = "https://biznis.rs/novac/nova-platna-kartica-na-srpskom-trzistu/"
N102 = "https://www.bancaintesa.rs/en/stanovnistvo/medija-centar/vesti/news102.html"
N87 = "https://www.bancaintesa.rs/en/stanovnistvo/medija-centar/vesti/news87.html"
N569 = "https://www.bancaintesa.rs/en/stanovnistvo/medija-centar/vesti/news569.html"
N1466 = "https://www.bancaintesa.rs/en/stanovnistvo/medija-centar/vesti/news1466.html"
SBDEBIT = "https://www.bancaintesa.rs/mali-biznis/platne-kartice/debitne-kartice.html"
SBCREDIT = "https://www.bancaintesa.rs/mali-biznis/platne-kartice/kreditne-kartice.html"
SHESNEXT = "https://www.bancaintesa.rs/mali-biznis/platne-kartice/debitne-kartice/she-s-next.html"
ACQ = "https://www.bancaintesa.rs/mali-biznis/prihvatanje-platnih-kartica.html"
ECOM = "https://www.bancaintesa.rs/mali-biznis/digitalno-bankarstvo/E-commerce.html"
IPSACC = "https://www.bancaintesa.rs/mali-biznis/digitalno-bankarstvo/prihvatanje-ips.html"
GARSON = "https://www.bancaintesa.rs/mali-biznis/digitalno-bankarstvo/banca-intesa-garson-ordering.html"
BIZPORTAL = "https://www.bancaintesa.rs/mali-biznis/digitalno-bankarstvo/intesa-biz-portal.html"
FARMER = "https://www.bancaintesa.rs/mali-biznis/intesa-farmer.html"
MAGNIFICA = "https://www.bancaintesa.rs/magnifica"
PRIVREDA = "https://www.bancaintesa.rs/privreda"
SEPA = "https://www.bancaintesa.rs/stanovnistvo/obavestenje-o-primeni-SEPA-placanja.html"
NEWAPP = "https://www.bancaintesa.rs/stanovnistvo/digitalno-bankarstvo/unapredjena-digitalna-aplikacija.html"
MOBI = "https://www.bancaintesa.rs/stanovnistvo/digitalno-bankarstvo/mobilno-bankarstvo.html"
EGOV = "https://www.bancaintesa.rs/stanovnistvo/digitalno-bankarstvo/e-gradjanin-consent-id-kes.html"
RATE = "https://www.bancaintesa.rs/stanovnistvo/platne-kartice/debitne-kartice/kupovina-na-rate-debitnom-karticom.html"
GALERIJA = "https://www.bancaintesa.rs/stanovnistvo/digitalno-bankarstvo/galerija-popusta.html"
AIRSERBIA = "https://www.airserbia.com/sr_cyril/novosti/Er-Srbija-i-Banca-Intesa-pretvaraju-svaku-kupovinu-u-novo-putovanje-stratesko-partnerstvo-i-nova-co-brand-kartica~1956179"
DINA = "https://biznis.rs/vesti/srbija/kako-je-dina-kartica-ustedela-srpskim-bankarima-vise-od-200-miliona-evra/"
IPS = "https://biznis.rs/novac/nbs-u-sistemu-za-instant-placanja-u-septembru-realizovano-931-milion-transakcija/"
IFLAW = "https://dinacard.nbs.rs/en/trgovci_akceptanti"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · parent · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Serbia's largest bank by assets and deposits, wholly owned by Intesa Sanpaolo, the country's first Mastercard issuer in 2002, a new executive line-up and a Data & AI unit.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & returns", "blurb": "Number one, €265m profit.", "div": "bib", "rev": "central", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of RSD 1,029 billion (about €8.8 billion) and profit after tax of RSD 26.8 billion in 2024, with a capital adequacy ratio of 19.9%; 2025 net profit of about €265 million (RSD 31 billion), the largest in Serbia; 15.3% of net assets and 15.6% of client deposits at the end of 2025; 1.34 million clients, 134 branches and 3,044 staff.",
              s=["con", "corp"], neo=[0, ""], src=[["2024 annual report", AR24], ["Biznis.rs: top six banks 2025, Mar 2026", TOP6], ["Kurir: Euromoney award, Jul 2026", KURIR]]),
        ]},
        {"id": "1.2", "ic": "building-2", "name": "Parent & heritage", "blurb": "Intesa Sanpaolo since 2005.", "div": "isp", "rev": "central", "products": [
            P("isp", "Intesa Sanpaolo", "100% owned by Intesa Sanpaolo and part of its International Banks Division (12 countries), which earned €611 million in the first half of 2026; the group earned €5.6 billion and expects more than €10 billion for 2026.",
              s=["corp"], o="A", neo=[0, ""], src=[["Banca Intesa: about us", ABOUT], ["Intesa Sanpaolo H1 2026 results", ISP1H]]),
            P("heritage", "Heritage", "Founded in Belgrade in 1991; part of Banca Intesa (now Intesa Sanpaolo) since 2005; brought Mastercard to Serbia in 2002 and American Express back in 2006; bought Panonska banka in 2007; an Intesa Sanpaolo Card office for card development opened in Belgrade in 2010.",
              s=["con"], o="I", neo=[0, "Serbia's first Mastercard issuer, 2002."], src=[["Banca Intesa: history", HIST], ["Banca Intesa: Mastercard three years on, Jul 2005", N102]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Leadership", "blurb": "Popović and Đurić.", "div": "bib", "rev": "central", "products": [
            P("leadership", "Board & executive board", "Draginja Đurić chairs the board; Darko Popović has led the executive board since 2022 and on 1 October 2026 became chair of the Association of Serbian Banks; Dragica Mihajlović is CFO, with heads for risk, operations and transformation, governance, retail and corporate (January 2026 chart).",
              s=["corp"], neo=[0, ""], src=[["Banca Intesa: organisation chart, Jan 2026", ORG], ["Banca Intesa: Darko Popović", CEO], ["Biznis.rs: Popović heads bank association, Oct 2026", UBS]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "A Data & AI unit.", "div": "bib", "rev": "central", "products": [
            P("tech", "Technology, data & AI", "A Data & AI unit under the Chief Governance Officer, machine-learning models that picked digital non-users for Viber and in-app campaigns (about 23% response in 2024), and the parent's isytech 2.0 platform and 19 AI projects.",
              s=["corp"], neo=[0, ""], src=[["Banca Intesa: organisation chart, Jan 2026", ORG], ["2024 annual report", AR24], ["Intesa Sanpaolo H1 2026 results", ISP1H]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & standing", "blurb": "Organic growth, many awards.", "div": "bib", "rev": "central", "products": [
            P("strategy", "Strategy", "The 2022–2025 plan had six initiatives: revenue and fees, digitalisation, value in lending, the credit machine, reskilling and ESG; growth in 2024 was described as wholly organic. No local plan for 2026 onward has been published ⚠; the parent's 2026–2029 plan leads on technology and wealth.",
              s=["corp"], neo=[0, ""], src=[["2024 annual report", AR24], ["Intesa Sanpaolo H1 2026 results", ISP1H]]),
            P("awards", "Awards", "The Banker's Bank of the Year in Serbia for the 12th time (December 2025) and Euromoney's Best Bank in Serbia 2026, citing a loan book up 14.4% and cash loans above €980 million in 2025.",
              s=["con"], st="new", neo=[0, ""], src=[["Intesa Sanpaolo: Bank of the Year, Dec 2025", BANKER], ["Euromoney: Serbia 2026", EMONEY]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Visa and DinaCard debit, credit split across Mastercard, Visa and American Express, business cards, Apple Pay and Google Pay, the country's largest acquiring network, NBS instant payments and SEPA, and card instalments.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Visa and DinaCard.", "div": "bib", "rev": "retail", "products": [
            P("visadebit", "Visa debit cards", "Visa Inspire (the packaged card since September 2012), Visa Classic Debit, Visa Platinum and the Banca Intesa Internet card; the May 2026 tariff lists no Mastercard or Maestro debit.", short="Visa debit",
              s=["con", "young"], lc="everyday", ay="Sep 2012", o="P", at="Visa", neo=[0, "Visa."],
              mc="Debit, once Maestro, is now wholly Visa's.",
              src=[["Banca Intesa: debit cards", DEBIT], ["Card tariff, May 2026", TARIFF], ["Visa Inspire launch, Sep 2012", N569]]),
            P("visainfinite", "Visa Infinite debit", "Serbia's first Visa Infinite debit card (November 2017), with concierge, lounge access and travel insurance, at RSD 6,000 a month.",
              s=["aff"], lc="everyday", ay="Nov 2017", o="P", at="Visa", neo=[0, "Visa."], src=[["Visa Infinite launch, Nov 2017", N1466], ["Card tariff, May 2026", TARIFF]]),
            P("dinadebit", "DinaCard debit", "The domestic NBS scheme's debit card, free and included in every account package, for cash and payments in Serbia.",
              s=["con", "sb"], lc="everyday", o="P", at="DinaCard (NBS)", neo=[0, "DinaCard."], src=[["Banca Intesa: debit cards", DEBIT], ["Biznis.rs: DinaCard savings, Jan 2026", DINA]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Mastercard, Visa and Amex.", "div": "bib", "rev": "retail", "products": [
            P("mccredit", "Mastercard credit cards", "Mastercard Standard (free inside the Hit and Hit Plus packages), Mastercard Standard, Gold (free with Magnifica) and Platinum; the bank holds about 28% of Serbian credit cards and 31.7% of retail card lending (2024).", short="Mastercard credit",
              s=["con", "aff"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's main foothold at the bank.",
              src=[["Banca Intesa: credit cards", CREDIT], ["Card tariff, May 2026", TARIFF], ["2024 annual report", AR24]]),
            P("mcplatinum", "Mastercard Platinum", "Launched in 2021 with 'long-term partner Mastercard': 24/7 concierge, flight-delay lounge pass, internet abroad, up to 24 interest-free instalments and a choice of FitPass, Kopaonik ski pass or Arena Cloud; RSD 1,400 a month.",
              s=["aff"], lc="borrow", ay="2021", o="P", at="Mastercard", neo=[2, "Mastercard Platinum benefits."], src=[["Banca Intesa: Mastercard Platinum, 2021", MCPLAT], ["Biznis.rs: new card, 2021", MCPLAT2]]),
            P("visacredit", "Visa credit cards", "Visa Classic, Visa Gold and the Visa Classic Affinity Paralympic charity card.",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Card tariff, May 2026", TARIFF]]),
            P("amex", "American Express", "The exclusive Serbian issuer since 2006: Blue (free in the Hit, Hit Plus and Magnifica packages), Green, Green for the medical chamber, Gold and a deposit-backed Green.",
              s=["con", "aff"], lc="borrow", ay="2006", o="P", at="American Express", neo=[0, "American Express."], src=[["Banca Intesa: history", HIST], ["Card tariff, May 2026", TARIFF]]),
        ]},
        {"id": "2.3", "ic": "briefcase", "name": "Business cards", "blurb": "Visa debit, Mastercard credit.", "div": "bib", "rev": "smallbiz", "products": [
            P("bizdebit", "Business debit cards", "Dina Business debit, Visa Business Debit, Visa Platinum Business and Visa Platinum Business She's Next for women entrepreneurs (RSD 750 a month for six months if taken by 31 December 2026).",
              s=["sb"], lc="everyday", st="new", o="P", at="Visa, DinaCard", neo=[0, "Visa and DinaCard."], src=[["Banca Intesa: business debit cards", SBDEBIT], ["Banca Intesa: She's Next", SHESNEXT]]),
            P("mcbusiness", "Mastercard Business credit card", "The bank's business credit card: limits from €500, up to 40 days interest-free, use at home and abroad.",
              s=["sb", "corp"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="The only business credit card on the menu, and a base for commercial cards.",
              src=[["Banca Intesa: business credit cards", SBCREDIT]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Wallets", "blurb": "Apple Pay and Google Pay.", "div": "mobi", "rev": "retail", "products": [
            P("applepay", "Apple Pay & Google Pay", "Apple Pay for Visa cards from December 2020 and for Mastercard from April 2021, with cards added from Intesa Mobi; 12.8 million Apple Pay and 6.2 million Google Pay transactions in 2024. DinaCard and Amex are not listed ⚠.",
              s=["con"], lc="everyday", ay="Dec 2020", o="P", at="Apple, Google", neo=[1, "Visa and Mastercard tokens."], src=[["Banca Intesa: Apple Pay", APPLE], ["Banca Intesa: Google Pay", GPAY], ["Apple Pay for Mastercard, Apr 2021", N1667], ["2024 annual report", AR24]]),
            P("virtual", "Virtual card", "A virtual copy of the debit card, made in Intesa Mobi for safer online shopping.",
              s=["con"], lc="everyday", neo=[None, "Network not stated."], src=[["Banca Intesa: Intesa Mobi", MOBI]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "71% of online card spend.", "div": "bib", "rev": "smallbiz", "products": [
            P("acquiring", "Card acquiring", "20,000 POS terminals taking every card; 21% of Serbia's POS terminals, 26% of POS turnover and more than 71% of internet acquiring turnover (2024).",
              s=["merch"], lc="move", o="B", neo=[1, "Accepts every network."],
              mc="The main route to Serbian merchants for any network.",
              src=[["Banca Intesa: card acceptance", ACQ], ["2024 annual report", AR24]]),
            P("softpos", "Soft POS & Android POS", "Banca Intesa Soft POS takes cards and IPS on any Android phone (328 merchants and 2,278 terminals at the end of 2024), and runs on the Garson ordering device for restaurants.",
              s=["merch", "sb"], lc="move", st="new", o="P", at="Garson", neo=[1, "Takes Mastercard, Visa and IPS."], src=[["Banca Intesa: instant payment acceptance", IPSACC], ["Banca Intesa: Garson", GARSON], ["2024 annual report", AR24]]),
            P("ecom", "E-commerce gateway", "Online acceptance with instalments, recurring payments, pay-by-link, card-on-file and phone orders, secured by 3-D Secure (Mastercard and Visa).",
              s=["merch"], lc="move", o="B", neo=[1, "Mastercard and Visa 3-D Secure."], src=[["Banca Intesa: e-commerce", ECOM]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Instant & cross-border", "blurb": "IPS and SEPA.", "div": "bib", "rev": "retail", "products": [
            P("ips", "IPS instant payments", "NBS instant payments in the app by scanning or showing a QR code, at merchant POS and online; the national system handled 9.31 million payments in September 2025.",
              s=["con", "merch"], lc="move", o="P", at="National Bank of Serbia", neo=[0, "NBS IPS."], src=[["Banca Intesa: Intesa Mobi", MOBI], ["Banca Intesa: instant payment acceptance", IPSACC], ["Biznis.rs: IPS September 2025", IPS]]),
            P("sepa", "SEPA transfers", "SEPA credit transfers in euro, sent and received from 5 May 2026, same or next day, alongside SWIFT and the NBS FX clearing.",
              s=["con", "corp"], lc="move", st="new", ay="May 2026", neo=[0, ""], src=[["Banca Intesa: SEPA notice", SEPA]]),
            P("withcash", "#withCASH", "Cash from the bank's ATMs without a card, now up to RSD 80,000.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Banca Intesa: new app", NEWAPP]]),
        ]},
        {"id": "2.7", "ic": "refresh-cw", "name": "Instalments", "blurb": "10% of POS spend.", "div": "bib", "rev": "retail", "products": [
            P("cardinst", "Credit-card instalments", "Banca Intesa credit cards split purchases into instalments at more than 12,000 merchants, about 10% of turnover on the bank's POS (2024).",
              s=["con"], lc="borrow", neo=[1, "Mastercard, Visa and Amex credit."], src=[["2024 annual report", AR24]]),
            P("debitinst", "Debit-card instalments", "Up to 12 instalments on DinaCard debit, limit one month's pay up to RSD 300,000, granted automatically to salary clients.",
              s=["con"], lc="borrow", neo=[0, "DinaCard."], src=[["Banca Intesa: debit instalments", RATE], ["Banca Intesa: debit cards", DEBIT]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: 3-D Secure and an antifraud unit, state digital identity and e-signatures in the app, data and AI models, and card offers, with an Air Serbia co-brand card in preparation.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security & identity", "blurb": "3-D Secure, ConsentID.", "div": "bib", "rev": "central", "products": [
            P("tds", "3-D Secure", "One-time SMS passwords for online card payments, under Mastercard and Visa 3-D Secure.",
              s=["con"], lc="everyday", o="P", neo=[1, "Mastercard and Visa authentication."], src=[["Banca Intesa: debit cards", DEBIT], ["Banca Intesa: e-commerce", ECOM]]),
            P("fraud", "Antifraud", "A Cybersecurity, Antifraud, BCM & Corporate Security unit and internal fraud rules; no Mastercard fraud tool found ⚠.",
              s=["con", "corp"], lc="everyday", o="B", neo=[0, "In-house."], src=[["Banca Intesa: organisation chart, Jan 2026", ORG], ["2024 annual report", AR24]]),
            P("consentid", "ConsentID & e-signature", "eGrađanin, ConsentID and a cloud qualified e-signature activated in the app with the government's IT and eGovernment office; used to sign cash loans up to RSD 1.2 million remotely.",
              s=["con", "sb"], lc="open", o="P", at="Office for IT and eGovernment", neo=[0, ""], src=[["Banca Intesa: eGrađanin and ConsentID", EGOV]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data & AI", "blurb": "Models for engagement.", "div": "bib", "rev": "central", "products": [
            P("dataai", "Data & AI", "Machine-learning models to target digital non-users, personalised offers in the app and the Data & AI unit's work; digital channels gave 23% of cash-loan sales in 2024.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["2024 annual report", AR24], ["Banca Intesa: organisation chart, Jan 2026", ORG]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Offers & loyalty", "blurb": "Galerija popusta, Air Serbia.", "div": "mobi", "rev": "retail", "products": [
            P("galerija", "Galerija popusta", "Personalised merchant coupons for Banca Intesa cardholders inside Intesa Mobi, launched in 2024 as a discount platform.",
              s=["con", "merch"], lc="grow", o="B", neo=[0, ""],
              mc="A ready home for card-linked offers.",
              src=[["Banca Intesa: Galerija popusta", GALERIJA], ["2024 annual report", AR24]]),
            P("airserbia", "Air Serbia co-brand card", "A letter of intent signed on 21 May 2026 for a co-brand card tied to Air Serbia's future loyalty programme; network and launch date not announced ⚠.",
              s=["con", "aff"], lc="grow", st="new", ay="May 2026", o="P", at="Air Serbia", neo=[None, "Network not announced."],
              mc="The most visible card decision still open at the bank.",
              src=[["Air Serbia: co-brand card, May 2026", AIRSERBIA]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: account packages from the youth IN account to Magnifica, cash loans and mortgages, savings, Intesa Invest funds and Generali insurance, small-business and farmer banking, and corporate lending.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Accounts & packages", "blurb": "IN, Hit, Magnifica.", "div": "bib", "rev": "retail", "products": [
            P("packages", "Account packages", "Basic, IN (ages 16–26, launched 2024 with a Visa Inspire card on eco-plastic), Intesa Hit and Hit Plus; packages bundle Visa and Dina debit with a Mastercard Standard or Amex Blue credit card.",
              s=["con", "young"], lc="open", neo=[1, "Visa and Dina debit; Mastercard or Amex credit."], src=[["Banca Intesa: home page", BIB], ["Card tariff, May 2026", TARIFF], ["2024 annual report", AR24]]),
            P("magnifica", "Intesa Magnifica", "Premium banking with the highest savings rates, COMBI savings-plus-funds, Visa Infinite debit and a free Mastercard Gold.",
              s=["aff"], lc="grow", neo=[1, "Visa Infinite debit; Mastercard Gold credit."], div="magnifica", src=[["Banca Intesa: Magnifica", MAGNIFICA], ["Card tariff, May 2026", TARIFF]]),
        ]},
        {"id": "4.2", "ic": "hand-coins", "name": "Loans & mortgages", "blurb": "Cash loans +63%.", "div": "bib", "rev": "retail", "products": [
            P("cashloan", "Cash loans", "An online cash loan up to RSD 1.2 million signed digitally, plus Intermezzo, refinancing, senior and auto loans; cash-loan disbursements topped €980 million in 2025, up 63%.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Banca Intesa: eGrađanin and ConsentID", EGOV], ["Euromoney: Serbia 2026", EMONEY]]),
            P("mortgage", "Mortgages", "Approval in as little as seven days, subsidised loans for the young and the Intesa Casa green loan.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Banca Intesa: home page", BIB]]),
        ]},
        {"id": "4.3", "ic": "trending-up", "name": "Savings & investments", "blurb": "#withSAVE, Intesa Invest.", "div": "invest", "rev": "retail", "products": [
            P("savings", "Savings & #withSAVE", "Online savings and term deposits up to RSD 2.4 million or €20,000, and #withSAVE goals fed by transfers and card round-ups.",
              s=["con", "young"], lc="grow", st="new", neo=[0, ""], div="mobi", src=[["Banca Intesa: new app", NEWAPP]]),
            P("funds", "Intesa Invest funds", "Five funds with assets above €600 million (2024), bought and sold in the app, plus the Gold&Silver Alternative fund.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["2024 annual report", AR24], ["Banca Intesa: Magnifica", MAGNIFICA]]),
            P("bancassurance", "Insurance", "Life, credit-protection and health cover from Generali, sold in branches.",
              s=["con", "aff"], lc="grow", o="P", at="Generali", neo=[0, ""], div="bib", src=[["Banca Intesa: Magnifica", MAGNIFICA]]),
        ]},
        {"id": "4.4", "ic": "briefcase-business", "name": "Small business & farmers", "blurb": "Biz packages, Intesa Farmer.", "div": "bib", "rev": "smallbiz", "products": [
            P("smallbiz", "Small business", "BizCOMFORT and BizPRO packages, Biz Invest and working-capital loans, loans for women in business and young entrepreneurs (EBRD), and online BizMobi loans; small-business lending hit a record in 2024.",
              s=["sb"], lc="borrow", neo=[1, "Visa and Dina debit; Mastercard Business credit."], src=[["Banca Intesa: She's Next", SHESNEXT], ["2024 annual report", AR24]]),
            P("farmer", "Intesa Farmer", "A farmer's account with Dina debit (Visa on request) and loans with interest subsidised by the agriculture ministry.",
              s=["sb"], lc="borrow", neo=[0, "Dina and Visa debit."], src=[["Banca Intesa: Intesa Farmer", FARMER]]),
        ]},
        {"id": "4.5", "ic": "factory", "name": "Corporate & SME", "blurb": "16.8% of corporate loans.", "div": "bib", "rev": "corp", "products": [
            P("corporate", "Corporate & SME banking", "Corporate loans up 6.6% in 2024 to a 16.8% share and a portfolio above RSD 360 billion, €1.9 billion of new lending, a 15.9% deposit share and €104 million of green lending; an Italian Desk, trade finance, factoring and project finance.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["2024 annual report", AR24], ["Banca Intesa: corporate", PRIVREDA]]),
            P("leasing", "Intesa Leasing", "The group's leasing company, set up in 2006 ⚠ current status not checked.",
              s=["corp", "sb"], lc="borrow", neo=[0, ""], div="leasing", src=[["Banca Intesa: history", HIST]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: Intesa Mobi for 700,000 digital clients, online banking and the Intesa Biz portal, 134 branches and ATMs, and partners from merchants to the national cashless campaign.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Intesa Mobi", "blurb": "700,000 digital clients.", "div": "mobi", "rev": "retail", "products": [
            P("mobi", "Intesa Mobi", "About 700,000 digital clients, 573,000 active and 28.2 million transactions in 2024; a new version in 2026 adds shortcuts, QR payments before log-in and #withKEY ⚠ release date not stated.",
              s=["con", "young"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["2024 annual report", AR24], ["Banca Intesa: new app", NEWAPP]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Online & business portals", "blurb": "BizMobi, Intesa Biz portal.", "div": "bib", "rev": "smallbiz", "products": [
            P("online", "Banca Intesa Online & BizMobi", "Web banking for individuals and BizMobi for firms, integrated with the bank's CRM in 2024.",
              s=["con", "sb"], lc="everyday", o="B", neo=[0, ""], src=[["2024 annual report", AR24]]),
            P("bizportal", "Intesa Biz portal", "A portal for companies to manage users, statements, certificates and their banker, with ConsentID log-in.",
              s=["sb", "corp"], lc="open", st="new", o="B", neo=[0, ""], src=[["Banca Intesa: Intesa Biz portal", BIZPORTAL]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & ATMs", "blurb": "134 branches.", "div": "bib", "rev": "retail", "products": [
            P("branches", "Branches, ATMs & contact centre", "134 branches being turned into advice-led outlets, cash-in ATMs in dinars and euros, contactless ATM withdrawals, a contact centre, chat and video meetings for mortgages.",
              s=["con", "aff"], lc="everyday", neo=[0, ""], src=[["2024 annual report", AR24], ["Banca Intesa: home page", BIB]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners", "blurb": "Merchants and 'Bolji način'.", "div": "bib", "rev": "smallbiz", "products": [
            P("partners", "Partners & cashless campaign", "12,000-plus instalment merchants, Garson and City Express, and the 'Bolji način' national cashless initiative launched by GIZ, Mastercard, Visa, the finance ministry and NALED, under which new merchants get a free POS, Soft POS or web shop for a year.",
              s=["merch"], lc="move", o="P", at="GIZ, Mastercard, Visa, NALED", neo=[1, "Co-founded by Mastercard and Visa."], src=[["Banca Intesa: card acceptance", ACQ], ["Banca Intesa: Garson", GARSON]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Banca Intesa", "blurb": "First issuer, now credit only.", "products": [
        P("mcatbib", "Mastercard at Banca Intesa", "Banca Intesa brought Mastercard to Serbia in 2002 and in 2005 handled more than 90% of the country's Mastercard turnover. It joined Visa in 2003 and built debit on it: Visa was 78.7% of its cards by 2017, and the May 2026 tariff lists only Visa and DinaCard debit. Mastercard keeps credit (Standard, Gold, Platinum, Business), wallets and acceptance; American Express is exclusive to the bank.",
          s=["con"], div="bib", rev="central", mc="The relationship this map is drawn for.",
          src=[["Banca Intesa: Mastercard three years on, Jul 2005", N102], ["Visa Infinite launch, Nov 2017", N1466], ["Card tariff, May 2026", TARIFF]]),
    ]},
    {"id": "pillar-market", "name": "Serbian payments", "blurb": "DinaCard, IPS, SEPA, caps.", "products": [
        P("market", "The Serbian market", "Interchange is capped at 0.2% on debit and 0.3% on credit ⚠; DinaCard is mandatory in every account package and the NBS says it saved banks €223 million in 2020–2024 against €142 million paid to international schemes in 2024; NBS instant payments run 9 million-plus a month; SEPA opened in May 2026.",
          s=["con"], div="bib", rev="central", src=[["Biznis.rs: DinaCard savings, Jan 2026", DINA], ["NBS DinaCard: merchants", IFLAW], ["Biznis.rs: IPS September 2025", IPS], ["Banca Intesa: SEPA notice", SEPA]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
