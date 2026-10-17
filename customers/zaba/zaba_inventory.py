"""Zagrebačka banka's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the H1 2026 unaudited financial statements (22 July 2026)
and the 2025 audited group statements, both filed on the Zagreb Stock Exchange, Hina's report of the H1 2026 group
result, and the profile page on zaba.hr (data at 31 March 2026). Product and network facts come from Zaba's own pages on
zaba.hr, read 17 October 2026 and translated from Croatian. UniCredit, the parent, is mapped separately. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1R = "https://eho.zse.hr/fileadmin/issuers/ZABA/FI-ZABA-5b0e7f28db2e778291ddefae5c6ad309.pdf"
FY25 = "https://eho.zse.hr/fileadmin/issuers/ZABA/FI-ZABA-245d6d7dc87d19b9b1393a95c24b4eeb.pdf"
NOVI = "https://www.novilist.hr/?p=1725090"
PROFILE = "https://www.zaba.hr/home/o-nama/o-nama/pregled"
HISTORY = "https://www.zaba.hr/home/o-nama/o-nama/povijest"
STRUCT = "https://www.zaba.hr/home/o-nama/o-nama/struktura"
BOARD = "https://www.zaba.hr/home/o-nama/uprava"
OWN = "https://www.companywall.hr/tvrtka/zagrebacka-banka-dd-92963223473unicredit-spa-99448991218/MM3eGxED"
CREDIT = "https://www.zaba.hr/home/kreditne-kartice-zagrebacke-banke"
DIGICARD = "https://www.zaba.hr/home/moja-m-zaba/digitalno-ugovaranje-kartica"
SPLIT = "https://www.zaba.hr/home/moja-m-zaba/naknadna-podjela-na-rate-uz-naknadu"
VIRT = "https://www.zaba.hr/home/gradjani/jednokratna-virtualna-kartica"
VIRTPR = "https://www.zaba.hr/home/o-nama/zagrebacka-banka-predstavila-jednokratnu-virtualnu-karticu-za-jednostavnu-i-sigurnu-online-kupnju"
MPC = "https://www.zaba.hr/home/gradjani/multipluscard-program-lojalnosti"
PERKS = "https://www.zaba.hr/home/placanje/pogodnosti"
PRICELESS = "https://www.zaba.hr/home/gradjani/priceless-cities12"
LOUNGE = "https://www.zaba.hr/home/gradjani/program-zaba-airport-lounge-u-suradnji-s-loungekeyjem"
BIZCARDS = "https://www.zaba.hr/home/mali-poduzetnici/kartice/kreditne-kartice-za-poslovne-korisnike-sb"
BMCPLUS = "https://www.zaba.hr/home/mali-poduzetnici/business-mastercard-plus-sb"
ACCEPT = "https://www.zaba.hr/home/mali-poduzetnici/kartice/prihvat-kartica-na-prodajnom-mjestu-ili-internetu-sb"
SOFTPOS = "https://www.zaba.hr/home/mali-poduzetnici/softpos-zaba-sb"
FISKAL = "https://www.zaba.hr/home/mali-poduzetnici/jedan-uredaj-za-sve-zaba-fiskal-pos"
ECOM = "https://www.zaba.hr/home/mali-poduzetnici/e-commerce"
PORTAL = "https://www.zaba.hr/home/mali-poduzetnici/web-portal-za-trgovce-sb"
IZIPAY = "https://www.zaba.hr/home/gradjani/mzaba-izipay"
MZABA = "https://www.zaba.hr/home/m-zaba-mobilno-bankarstvo"
MSTUDENT = "https://www.zaba.hr/home/m-student"
MPARK = "https://www.zaba.hr/home/moja-m-zaba/m-parking"
PSD2 = "https://www.zaba.hr/home/footer/psd2-open-banking"
SECURITY = "https://www.zaba.hr/home/placanje/digitalna-sigurnost"
FRAUDPR = "https://www.zaba.hr/home/o-nama/vise-od-55-posto-gradana-nije-prepoznalo-financijsku-prijevaru-ni-u-simulaciji"
FRAUD2 = "https://www.zaba.hr/home/o-nama/hrvati-izgubili-20-milijuna-eura-u-financijskim-prijevarama-mladi-su-zbog-usamljenosti-vise-podlozni-manipulaciji"
PRIME = "https://www.zaba.hr/home/o-nama/prime-bankarstvo-zagrebacke-banke-nova-dimenzija-personaliziranog-bankarstva"
BTC = "https://www.zaba.hr/home/o-nama/zaba-uvela-bitcoin-etf-certifikat-most-izmedu-kriptotrzista-i-reguliranog-ulaganja"
UCINV = "https://www.zaba.hr/home/o-nama/novo-ime-ista-predanost-zb-invest-postaje-unicredit-invest"
DEALSYNC = "https://www.zaba.hr/home/o-nama/dealsync-rjesenje-koje-malim-i-srednjim-poduzecima-otvara-put-do-europskih-investicija-ulagaca-i-strateskih-partnera"
MINIBOND = "https://www.zaba.hr/home/o-nama/zagrebacka-banka-u-svega-nekoliko-mjeseci-uspjesno-aranzirala-gotovo-60-milijuna-eura-mini-obveznica"
EUROMONEY = "https://www.zaba.hr/home/o-nama/zagrebacka-banka-osvojila-prestiznu-nagradu-euromoneyja-za-najbolju-banku-u-hrvatskoj-za-2026"
CORRESP = "https://www.zaba.hr/home/banke/placanja"
EPOSL = "https://www.zaba.hr/home/e-poslovnica"
MIGR = "https://www.index.hr/vijesti/clanak/kartice-sve-popularnije-u-hrvatskoj-prosjecan-gradjanin-ima-barem-dvije/2613927.aspx"
HRT = "https://en.hrturizam.hr/tag/mastercard"
LIDER = "https://en.lider.media/?p=20085"
MWALLET = "https://www.tportal.hr/biznis/clanak/korisnici-kartica-zagrebacke-banke-odsad-mogu-placati-mobitelom-20190215"
GARMIN = "https://en.lider.media/?p=41445"
MCDEAL = "https://insurancenewsnet.com/oarticle/unicredit-and-mastercard-expand-payments-partnership-10"
INSTANT = "https://www.croatiaweek.com/croatia-to-introduce-10-second-bank-transfers-under-new-rules/"
HNB22 = "https://www.hnb.hr/documents/20182/4686884/h-pkkt-2022.pdf/58d25789-540c-94a1-2e34-4a61df02c17b"
SECTOR = "https://www.intellinews.com/croatia-s-bank-profits-fall-5-5-as-a-strong-first-quarter-unwinds-465513/"
MKT = "https://en.lider.media/?p=23476"
NEWS = "https://www.zaba.hr/home/o-nama/press/novosti"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · UniCredit · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a quarter of Croatia's banking assets, €23.6 billion on the balance sheet, UniCredit owning about 96%, a city savings bank dating from 1914, its own m-token and signing platform, and the group's UniCredit Unlimited plan.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "€251m profit in H1 2026.", "div": "zaba", "rev": "retail", "products": [
            P("balance", "Bank balance sheet & earnings", "Net profit of €251 million in H1 2026 (down 2.7%), operating income €417 million, net fees up 16.0% to €109 million and a cost/income ratio of 28.3%; assets €23.6 billion, customer loans €13.7 billion (up 6.6% in six months) and deposits €19.1 billion at 30 June 2026.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 financial statements, Jul 2026", H1R], ["Novi list: H1 2026 result, Jul 2026", NOVI]]),
            P("group", "Zaba Group results", "Group net profit of €572 million in 2025 (up 2.9%) on €1,042 million of operating income, with assets of €28.4 billion; €301 million in H1 2026. Zaba, UniCredit Bank Mostar and UniCredit Leasing Croatia contribute most. About €448 million of dividends paid in 2025.",
              s=["corp"], neo=[0, ""], src=[["2025 audited group statements", FY25], ["Novi list: H1 2026 result, Jul 2026", NOVI]]),
            P("share", "Croatia's largest bank", "25.8% of banking-sector assets, 26.2% of resident deposits and 29.0% of income at 31 March 2026, on HNB statistics; capital adequacy 22.6%.",
              s=["con", "corp"], neo=[0, ""], src=[["Zaba: profile", PROFILE]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "UniCredit ~96%; Ćubela leads.", "div": "uc", "rev": "subs", "products": [
            P("owners", "UniCredit ownership & listing", "Part of UniCredit since March 2002; UniCredit S.p.A. holds about 96.2% ⚠ (registry data). Shares listed in Zagreb (ZABA) since 1995. Rated A- by Fitch (stable), with shareholder support a-.",
              s=["corp"], o="A", at="UniCredit", neo=[0, ""], src=[["CompanyWall: shareholders ⚠", OWN], ["Zaba: history", HISTORY], ["Zaba: profile", PROFILE]]),
            P("leadership", "Management board", "Dalibor Ćubela (CEO since July 2024), Slaven Rukavina (Retail), Aleksandra Rašić (Corporate), Jasna Mandac (Finance), Ivana Lonjak Dam (Risk) and Stefano Gison (Banking support), the last two since September 2025. Jana Novina Cukrov runs Payments.",
              s=["corp"], neo=[0, ""], src=[["Zaba: management board", BOARD], ["Zaba: virtual card, Jan 2026", VIRTPR]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "Gradska štedionica, 1914.", "div": "zaba", "rev": "retail", "products": [
            P("heritage", "From city savings bank to Zaba", "Founded in 1914 as Gradska štedionica; the first joint-stock bank in former Yugoslavia (1989); listed in Zagreb (1995) and London (1996); the world's first euro-denominated GDRs (1998). Financed Zagreb's trams, airport and Lisinski concert hall. 3,145 staff at June 2026.",
              s=["con"], o="I", neo=[0, ""], src=[["Zaba: history", HISTORY], ["H1 2026 financial statements, Jul 2026", H1R]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & signing", "blurb": "m-token, QPKI, UniCredit IT.", "div": "digital", "rev": "retail", "products": [
            P("tech", "m-token & Zaba QPKI", "A software token installed with m-zaba confirms logins, payments and online card purchases, and also opens the state e-Građani portal; Zaba's own QPKI certificates give qualified e-signatures for contracts signed remotely.",
              s=["con", "sme"], lc="open", o="B", neo=[0, ""], src=[["Zaba: m-zaba", MZABA], ["Zaba: digital security", SECURITY]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & awards", "blurb": "UniCredit Unlimited; best bank 2026.", "div": "uc", "rev": "corp", "products": [
            P("strategy", "Growth under UniCredit Unlimited", "No separate Zaba targets are published ⚠. The H1 2026 report names fee growth from new products, a home-loan sales network for refinancing, Prime banking and cost discipline. Euromoney's best bank in Croatia for 2026, the second year running.",
              s=["corp"], st="new", neo=[0, ""], src=[["H1 2026 financial statements, Jul 2026", H1R], ["Zaba: Euromoney award, Jul 2026", EUROMONEY]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: a Debit Mastercard on every account after the 2024–25 switch from Visa, Mastercard credit cards, Zaba's own instalments, phone and watch wallets, network-neutral acceptance, and IziPay and SEPA Instant between accounts.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Two million cards moved from Visa.", "div": "cards", "rev": "retail", "products": [
            P("debit", "Debit Mastercard", "Zaba and Mastercard began moving about two million debit cards from Visa to Mastercard in May 2024; private customers through early 2025, business cards from June ⚠. PINs and benefits stayed; Mastercard was to be the only brand on Zaba's cards during 2025. Contactless, daily limits in m-zaba.", short="Debit (Mastercard)",
              s=["con", "young"], lc="everyday", st="new", ay="May 2024", o="P", at="Mastercard", neo=[2, "Debit Mastercard."],
              mc="A whole debit book won from Visa, under UniCredit's 2023 group deal.",
              src=[["HRturizam: Zaba switches from Visa to Mastercard, May 2024", HRT], ["Lider: two million debit cards ⚠", LIDER], ["Index.hr with Zaba, Nov 2024", MIGR]]),
            P("virtual", "Single-use virtual card", "Created in seconds in m-zaba from the Mastercard debit card, free; one online purchase of up to €1,300, then void. Not for subscriptions, pre-authorisations or wallets. Launched 27 January 2026.", short="Virtual card (Mastercard)",
              s=["con"], lc="everyday", st="new", ay="Jan 2026", o="B", neo=[2, "Mastercard debit credentials."],
              mc="Zaba's own answer to card-not-present fraud; Click to Pay tokens do the same job.",
              src=[["Zaba: single-use virtual card", VIRT], ["Zaba: virtual card, Jan 2026", VIRTPR]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "All Mastercard.", "div": "cards", "rev": "retail", "products": [
            P("credit", "Standard, Platinum & Student Mastercard", "Charge cards paid in full each month: Standard (€19.91 a year, first year free), Platinum (€66.36, airport lounges) and Student (limits for students without income); Gold still in use. Contracted fully in m-zaba.", short="Credit (Mastercard)",
              s=["con", "prime", "young"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["Zaba: Mastercard credit cards", CREDIT], ["Zaba: digital card contracting", DIGICARD]]),
            P("gocard", "go!card revolving Mastercard", "A revolving card with no joining or annual fee; the balance is repaid over 36 instalments at a fixed 6.79% (APR 7.02% on €700), or in full without interest.",
              s=["con"], lc="borrow", o="B", neo=[2, "Mastercard."], src=[["Zaba: Mastercard credit cards", CREDIT], ["Zaba: digital card contracting", DIGICARD]]),
        ]},
        {"id": "2.3", "ic": "receipt-text", "name": "Instalments", "blurb": "Up to 36, at 25,000 merchants.", "div": "cards", "rev": "retail", "products": [
            P("instal", "Interest-free instalments at the till", "Zaba debit and credit cards split purchases into 2 to 36 instalments without interest or fees at more than 25,000 partner merchants, in shops, online and on SoftPOS; debit up to 24, credit up to 36.",
              s=["con", "sme"], lc="borrow", o="B", neo=[1, "Zaba's own scheme, on Mastercard cards."],
              mc="Zaba runs its own instalments; Mastercard Installments could take them to merchants outside its network.",
              src=[["Zaba: card acceptance", ACCEPT], ["Zaba: Mastercard credit cards", CREDIT]]),
            P("postsplit", "Split it later in m-zaba", "Marked purchases of €26 to €535 on a credit card or current account can be split into 2–3 instalments in m-zaba after the fact, at €1.32 an instalment and no interest.",
              s=["con"], lc="borrow", o="B", neo=[1, "On Mastercard cards."], src=[["Zaba: post-purchase instalments", SPLIT], ["Zaba: Mastercard credit cards", CREDIT]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Wallets", "blurb": "Apple, Google, Garmin Pay.", "div": "cards", "rev": "retail", "products": [
            P("wallets", "Apple Pay, Google Pay & Garmin Pay", "Debit, credit and business cards work in Apple Pay, Google Pay and Garmin Pay; Zaba says it was the first Croatian bank with Garmin Pay ⚠ date.",
              s=["con", "young", "sme"], lc="everyday", o="P", at="Apple, Google, Garmin", neo=[2, "All tokens are Mastercard."],
              src=[["Zaba: Mastercard credit cards", CREDIT], ["Zaba: Business Mastercard Plus", BMCPLUS], ["Lider: Garmin Pay ⚠", GARMIN]]),
            P("mwallet", "m-novčanik", "Zaba's own Android phone wallet inside m-zaba, launched 15 February 2019 for contactless Mastercard and Maestro cards; whether it still runs alongside Google Pay is not stated ⚠.",
              s=["con"], lc="everyday", st="unconf", ay="Feb 2019", o="B", neo=[2, "Mastercard and Maestro."], src=[["tportal: Zaba phone payments, Feb 2019", MWALLET]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "POS, SoftPOS, Fiskal POS, online.", "div": "cards", "rev": "sme", "products": [
            P("accept", "POS acquiring", "Zaba acquires Mastercard and Visa cards from any issuer plus Apple, Google and Garmin Pay; free POS terminal, next-day payout, instalments on Zaba cards and DCC for foreign cards; a merchant web portal shows transactions in real time.", short="Acquiring (all networks)",
              s=["sme", "corp"], lc="move", o="B", neo=[1, "Accepts Mastercard and Visa."],
              mc="A tourism-heavy acquiring book where gateway and risk tools fit.",
              src=[["Zaba: card acceptance", ACCEPT], ["Zaba: merchant web portal", PORTAL]]),
            P("softpos", "ZABA SoftPOS", "An Android app that turns a phone, tablet or NFC device into a contactless terminal for Mastercard and Visa, with instalments, tips, order IDs and digital receipts by e-mail, SMS, WhatsApp or Viber; no Zaba account needed.",
              s=["sme"], lc="move", o="B", neo=[1, "Mastercard and Visa."], src=[["Zaba: SoftPOS", SOFTPOS]]),
            P("fiskal", "Zaba Fiskal POS", "A fiscal till and card terminal in one Android device for €25 a month plus VAT, accepting Mastercard, Visa, Maestro and Diners, with e-invoices and instalments; no Zaba account needed.",
              s=["sme"], lc="move", st="new", o="B", neo=[1, "Mastercard, Visa, Maestro, Diners."], src=[["Zaba: Fiskal POS", FISKAL]]),
            P("ecom", "E-commerce acquiring", "Online card acceptance built to Mastercard and Visa rules with 3-D Secure, instalments and pre-authorisation, through gateways including Corvus Pay, Monri, HT PayWay and mstart.",
              s=["sme"], lc="move", o="P", at="Corvus Pay, Monri, HT, mstart", neo=[1, "Mastercard and Visa."], src=[["Zaba: e-commerce", ECOM]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Transfers & cross-border", "blurb": "IziPay, SEPA Instant, correspondents.", "div": "zaba", "rev": "retail", "products": [
            P("izipay", "IziPay", "Send money free by picking a phone contact; the recipient can bank anywhere in Croatia and registers a phone number against an IBAN, or takes a one-off SMS link. Non-customers can download m-zaba just for IziPay.",
              s=["con", "young"], lc="move", o="B", neo=[0, "Account-to-account."],
              mc="Mastercard's account-to-account and scam tools sit next to it.",
              src=[["Zaba: IziPay", IZIPAY]]),
            P("instant", "SEPA Instant transfers", "Croatian banks must offer euro instant transfers, with payee-name checks, from 9 October 2025 under the EU Instant Payments Regulation. No Croatian bank was found in Wero ⚠.",
              s=["con", "sme"], lc="move", st="new", ay="Oct 2025", neo=[0, "Account-to-account."], src=[["Croatia Week: 10-second transfers", INSTANT]]),
            P("corresp", "Correspondent banking & cross-border", "Euro and major-currency accounts for banks, euro settlement across Croatia, international payments and market leadership in paying pensions from abroad, on UniCredit's network.",
              s=["corp"], lc="move", o="B", at="UniCredit", neo=[0, ""], src=[["Zaba: payments for banks", CORRESP]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: 3-D Secure with m-token and a public anti-fraud campaign, PSD2 APIs through UniCredit, MultiPlusCard points and Mastercard offers, Priceless and LoungeKey, and AI and property data.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Card & scam security", "blurb": "3-D Secure, ZABAci oko.", "div": "cards", "rev": "retail", "products": [
            P("cardsec", "3-D Secure & card controls", "Every Zaba Mastercard is enrolled in 3-D Secure, approved with the m-token; customers block cards, see PINs and set online and daily limits in m-zaba.",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "3-D Secure on Mastercard cards; Identity Check brand not stated ⚠."],
              src=[["Index.hr with Zaba, Nov 2024", MIGR], ["Zaba: virtual card, Jan 2026", VIRTPR]]),
            P("fraudcamp", "ZABAci oko na prijevare", "An anti-fraud campaign and site; at a quiz kiosk in Zagreb 55.32% failed to spot every scam (May 2026). Croatian police logged more than 2,100 cyber crimes and €20 million of losses in 2025, up 22%.",
              s=["con", "young", "sme"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="Evidence of need for scam scoring on instant transfers.",
              src=[["Zaba: fraud quiz, May 2026", FRAUDPR], ["Zaba: €20m lost to fraud, Mar 2026", FRAUD2], ["Zaba: digital security", SECURITY]]),
        ]},
        {"id": "3.2", "ic": "key-round", "name": "Open banking", "blurb": "Berlin Group APIs since 2019.", "div": "uc", "rev": "retail", "products": [
            P("psd2", "PSD2 APIs", "Berlin Group account and payment APIs through UniCredit's developer portal since 14 March 2019, exempt from the fallback interface since September 2019.",
              s=["sme"], lc="open", o="P", at="UniCredit", neo=[0, ""], src=[["Zaba: PSD2 open banking", PSD2]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & benefits", "blurb": "MultiPlusCard, Priceless, lounges.", "div": "cards", "rev": "retail", "products": [
            P("mpc", "MultiPlusCard points", "One point per €5 on Mastercard credit cards and per €9 on debit, 100 points to one BONUS euro, spent at Konzum, Tisak and other MultiPlusCard partners; double points at partners.",
              s=["con"], lc="grow", o="P", at="MultiPlusCard", neo=[1, "Earned on Mastercard cards; partner-run."],
              src=[["Zaba: MultiPlusCard", MPC]]),
            P("perks", "Zaba Mastercard pogodnosti", "Monthly merchant offers for Zaba Mastercard holders, for example 10% off the Konzum webshop and eKupi, up to 50% at Big Bang (15–18 October 2026) and 15% at Terme Sveti Martin.",
              s=["con"], lc="grow", o="P", at="Mastercard, merchants", neo=[1, "Zaba offers on Mastercard cards."],
              mc="Card-linked offers would automate what Zaba now runs by campaign.",
              src=[["Zaba: Mastercard benefits", PERKS]]),
            P("priceless", "Priceless", "Experiences and discounts for Zaba Mastercard holders on priceless.com, branded in Croatia as \"Mastercard. Vrijedi više.\", such as backstage at Ultra Europe.",
              s=["con", "prime"], lc="grow", o="P", at="Mastercard", neo=[3, "Mastercard's own programme."], src=[["Zaba: Priceless", PRICELESS]]),
            P("lounge", "ZABA Airport Lounge with LoungeKey", "Free entry to about 1,500 airport lounges on Platinum and Business Mastercard credit cards; Gold Mastercard lost lounge access on 1 September 2026.",
              s=["prime", "sme"], lc="grow", o="P", at="LoungeKey, Mastercard", neo=[2, "Mastercard card benefit."], src=[["Zaba: Airport Lounge", LOUNGE]]),
        ]},
        {"id": "3.4", "ic": "brain", "name": "Data & AI", "blurb": "Property index, AI deal matching.", "div": "zaba", "rev": "corp", "products": [
            P("npuls", "Nekretninski puls", "A quarterly property-market analysis with Arhivanalitika, from July 2026, with regional indices and an affordability calculator from October 2026.",
              s=["home"], lc="beyond", st="new", ay="Jul 2026", o="P", at="Arhivanalitika", neo=[0, ""], src=[["Zaba: newsroom, Jul and Oct 2026", NEWS]]),
            P("dealsync", "DealSync", "UniCredit's AI-based platform matching buyers and sellers of small and mid-sized companies across its markets, open to Zaba clients from April 2026. No customer-facing AI assistant at Zaba was found ⚠.",
              s=["corp", "sme"], lc="beyond", st="new", ay="Apr 2026", o="P", at="UniCredit", neo=[0, ""],
              mc="Agent Pay is open ground once Zaba builds an assistant.",
              src=[["Zaba: DealSync, Apr 2026", DEALSYNC]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: accounts and loans for 1.3 million account holders, Prime and private banking, UniCredit Invest funds and pensions, business Mastercard cards, SME and corporate finance, leasing and a bank in Bosnia.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Accounts & loans", "blurb": "1.3 million account holders.", "div": "zaba", "rev": "retail", "products": [
            P("accounts", "Current accounts & packages", "Euro current accounts, Lepeza mogućnosti packages, youth and student packages and a basic account, with a switching service; more than 1.3 million Croatians held an account at Zaba in November 2024.",
              s=["con", "young"], lc="open", neo=[1, "Every account card is a Debit Mastercard."], src=[["Index.hr with Zaba, Nov 2024", MIGR], ["Zaba: m-zaba", MZABA]]),
            P("loans", "Cash loans & m-kredit", "Cash loans up to €50,000, overdrafts and pensioner loans, with pre-approved m-kredit and \"my credit options\" in the app.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["Zaba: m-zaba", MZABA]]),
            P("homeloans", "Home loans", "A specialist home-loan sales network drives refinancing and switching (H1 2026); example: €100,000 over 20 years at a fixed 3.70%, APR 4.02%.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["H1 2026 financial statements, Jul 2026", H1R], ["Zaba: m-zaba", MZABA]]),
        ]},
        {"id": "4.2", "ic": "gem", "name": "Prime & private banking", "blurb": "Prime since May 2026.", "div": "zaba", "rev": "retail", "products": [
            P("prime", "Prime banking", "Launched 11 May 2026: a dedicated Prime banker, Prime zones in branches and a Prime section in m-zaba for clients with more complex finances, at no charge.",
              s=["prime"], lc="grow", st="new", ay="May 2026", o="B", neo=[0, ""],
              mc="Premium card benefits are the obvious companion.",
              src=[["Zaba: Prime, May 2026", PRIME]]),
        ]},
        {"id": "4.3", "ic": "chart-candlestick", "name": "Investing & pensions", "blurb": "UniCredit Invest, AZ fund.", "div": "ucinv", "rev": "subs", "products": [
            P("ucinv", "UniCredit Invest funds", "ZB Invest, founded 2000 and about 32% of the Croatian fund market, became UniCredit Invest on 30 April 2026 and the group's regional fund centre.",
              s=["prime"], lc="grow", st="new", ay="Apr 2026", o="B", neo=[0, ""], src=[["Zaba: UniCredit Invest, Apr 2026", UCINV], ["Zaba: profile", PROFILE]]),
            P("pensions", "AZ pension funds (Allianz ZB)", "Mandatory and voluntary pension funds run by Allianz ZB, an associate; the AZ mandatory fund holds about 38% of its market.",
              s=["con", "prime"], lc="grow", o="P", at="Allianz", neo=[0, ""], src=[["Zaba: profile", PROFILE], ["Zaba: structure", STRUCT]]),
            P("btc", "Bitcoin ETF certificate", "From 15 June 2026: a capital-protected certificate linked to a Bitcoin ETF, five years two months, return capped at 50%, sold in branches after advice.",
              s=["prime"], lc="grow", st="new", ay="Jun 2026", o="P", neo=[0, ""], src=[["Zaba: Bitcoin ETF certificate, Jun 2026", BTC]]),
        ]},
        {"id": "4.4", "ic": "briefcase", "name": "Business cards", "blurb": "Three business Mastercards.", "div": "cards", "rev": "sme", "products": [
            P("bizcards", "Business Mastercard, go! business & Business Mastercard Plus", "Business credit cards with spend limits per user, deferred settlement, wallets and lounge access, managed in m-zaba PS. No virtual commercial card or expense platform was found ⚠.", short="Business cards (Mastercard)",
              s=["sme", "corp"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Virtual cards and Business Payment Controls would extend the range.",
              src=[["Zaba: business credit cards", BIZCARDS], ["Zaba: Business Mastercard Plus", BMCPLUS]]),
        ]},
        {"id": "4.5", "ic": "building-2", "name": "SME & corporate finance", "blurb": "Mini bonds, trade finance.", "div": "zaba", "rev": "corp", "products": [
            P("corp", "Corporate & investment banking", "Lending, trade finance, treasury, capital markets and custody; Euromoney's best bank for corporates and best investment bank in Croatia in 2026.",
              s=["corp"], lc="borrow", o="B", neo=[0, ""], src=[["Zaba: Euromoney award, Jul 2026", EUROMONEY], ["H1 2026 financial statements, Jul 2026", H1R]]),
            P("minibond", "Mini bonds", "A new financing route for SMEs and utilities from February 2026: nine issues worth almost €60 million by mid-July, far ahead of other arrangers.",
              s=["sme", "corp"], lc="borrow", st="new", ay="Feb 2026", o="B", neo=[0, ""], src=[["Zaba: mini bonds, Jul 2026", MINIBOND]]),
        ]},
        {"id": "4.6", "ic": "flag", "name": "Leasing & Bosnia", "blurb": "UniCredit Leasing, Mostar.", "div": "mostar", "rev": "subs", "products": [
            P("leasing", "UniCredit Leasing Croatia", "Vehicle and equipment leasing, one of the three main contributors to group profit.",
              s=["sme", "con"], lc="borrow", o="B", neo=[0, ""], src=[["Zaba: structure", STRUCT], ["Novi list: H1 2026 result, Jul 2026", NOVI]]),
            P("mostar", "UniCredit Bank d.d. Mostar", "Zaba's bank in Bosnia and Herzegovina, a main contributor to group profit. Its card networks were not researched ⚠.",
              s=["con", "corp"], lc="everyday", o="A", neo=[None, "Not researched ⚠."], src=[["Zaba: structure", STRUCT], ["2025 audited group statements", FY25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Zaba: m-zaba for 680,000 users, e-zaba and the e-poslovnica remote branch, more than 100 locations with 700 ATMs, and business portals.",
    "tiles": [
        {"id": "5.1", "ic": "monitor", "name": "m-zaba", "blurb": "680,000+ users.", "div": "digital", "rev": "retail", "products": [
            P("mzaba", "m-zaba app", "More than 680,000 users: cards opened and managed in the app, instalments, the virtual card, IziPay, m-kredit, m-redomat queueing and a Prime section.",
              s=["con", "young", "prime"], lc="everyday", o="B", neo=[0, ""], src=[["Zaba: profile", PROFILE], ["Zaba: m-zaba", MZABA]]),
            P("mstudent", "m-student", "QR payments in University of Zagreb canteens, subsidy balance and partner discounts; free Thursday lunch refunded up to €5 until June 2026.",
              s=["young"], lc="everyday", o="B", neo=[0, "QR, not card."], src=[["Zaba: m-student", MSTUDENT]]),
            P("mparking", "m-parking", "Pay for street parking in about 80 Croatian cities from m-zaba, with Bmove.",
              s=["con"], lc="everyday", o="P", at="Bmove", neo=[0, ""], src=[["Zaba: m-parking", MPARK]]),
        ]},
        {"id": "5.2", "ic": "log-in", "name": "e-zaba & remote", "blurb": "690,000+ users.", "div": "digital", "rev": "retail", "products": [
            P("ezaba", "e-zaba & e-poslovnica", "Internet banking for more than 690,000 users, and e-poslovnica, a remote branch by chat and e-mail on weekdays from 8 to 20 for card, limit and product changes.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, ""], src=[["Zaba: profile", PROFILE], ["Zaba: e-poslovnica", EPOSL]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & ATMs", "blurb": "100+ locations, 700+ ATMs.", "div": "zaba", "rev": "retail", "products": [
            P("branches", "Branches & ATMs", "More than 100 locations and 700 ATMs, Prime zones and business centres; cards can be activated at Zaba ATMs.",
              s=["con", "home", "prime"], lc="open", neo=[0, ""], src=[["Zaba: profile", PROFILE], ["Zaba: Prime, May 2026", PRIME]]),
        ]},
        {"id": "5.4", "ic": "briefcase-business", "name": "Business channels", "blurb": "m-zaba PS, merchant portal.", "div": "digital", "rev": "sme", "products": [
            P("bizdigital", "Business banking & merchant portal", "e-zaba and m-zaba for businesses with business-card management, cash management, and a web portal for merchants with real-time transactions and reports.",
              s=["sme", "corp"], lc="everyday", o="B", neo=[0, ""], src=[["Zaba: business credit cards", BIZCARDS], ["Zaba: merchant web portal", PORTAL]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Zaba", "blurb": "Every card Zaba issues.", "products": [
        P("mcatzaba", "Mastercard at Zaba", "Since the 2024–25 migration of about two million debit cards from Visa, every card Zaba issues is a Mastercard: debit, consumer and business credit, the virtual card and every wallet token, with Priceless and LoungeKey on top. It follows UniCredit's May 2023 multi-market deal with Mastercard ⚠ Zaba not named. Acquiring stays network-neutral.",
          s=["con"], div="cards", rev="retail", mc="The relationship this map is drawn for.",
          src=[["HRturizam: Zaba switches from Visa to Mastercard, May 2024", HRT], ["Index.hr with Zaba, Nov 2024", MIGR], ["UniCredit and Mastercard, May 2023", MCDEAL]]),
    ]},
    {"id": "pillar-market", "name": "Croatia", "blurb": "Largest bank; instant payments.", "products": [
        P("market", "The market", "Zaba holds a quarter of Croatian banking assets, ahead of PBZ (about a fifth) and Erste (18%) at end-2024 ⚠. SEPA Instant became mandatory in October 2025; sector profit fell 5.5% in H1 2026. Croatia had 6.9 million debit and 1.7 million credit cards in 2022, on Mastercard, Visa and Diners.",
          s=["con"], div="zaba", rev="retail", src=[["Zaba: profile", PROFILE], ["Lider: market shares ⚠", MKT], ["Croatia Week: 10-second transfers", INSTANT], ["IntelliNews: H1 2026 bank profits", SECTOR], ["HNB: payment cards 2022", HNB22]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
