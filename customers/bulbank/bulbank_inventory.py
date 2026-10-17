"""UniCredit Bulbank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the 2025 Annual Report (spring 2026), the 2024
Annual Report and the Bulgarian National Bank's bulletin for 30 June 2026. Bulgaria adopted the euro on
1 January 2026 (BGN 1.95583 = EUR 1); 2025 figures are in BGN as reported. ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

AR25 = "https://www.unicreditbulbank.bg/media/filer_public/00/18/00187e6b-6f5f-45e9-a40f-9e9160680f20/ucb_ar2026_en_all_a4_am_long.pdf"
AR24 = "https://www.unicreditbulbank.bg/media/filer_public/c2/fc/c2fcb6b5-3b3a-4d7c-8ba6-e28a4e943fa6/ucb-annual-report-2025-en.pdf"
BNB = "https://www.bnb.bg/bnbweb/groups/public/documents/bnb_publication/pub_b_in_b_2026_06_en.pdf"
DIVIDEND = "https://www.unicreditbulbank.bg/en/about-us/media/news/ucb-pays-dividends-2025/"
CFO = "https://www.unicreditbulbank.bg/en/about-us/media/news/nevena-nikse-is-the-new-cfo-of-ucb/"
PGGM = "https://www.unicreditbulbank.bg/en/about-us/media/news/UCB-and-pggm-enter-a-21-billion-risk-sharing/"
DOGS = "https://www.unicreditbulbank.bg/en/about-us/media/news/ucb-and-mastercard-donate-for-guide-dogs/"
GF26 = "https://www.unicreditbulbank.bg/en/about-us/media/news/global-finance-ucb-six-awards/"
BLINKDON = "https://www.unicreditbulbank.bg/en/about-us/media/news/unicredit-bulbank-launches-a-blink-donations/"
POSEUR = "https://www.unicreditbulbank.bg/en/about-us/media/news/pos-devices-regarding-the-EUR-conversion/"
DEBIT = "https://www.unicreditbulbank.bg/en/individual-clients/everyday-banking/payments/debit-cards/"
CREDIT = "https://www.unicreditbulbank.bg/en/individual-clients/bank-cards/credit-cards/"
DIGIDEBIT = "https://www.unicreditbulbank.bg/en/individual-clients/everyday-banking/payments/digital-debit-cards/"
WALLETS = "https://www.unicreditbulbank.bg/en/individual-clients/everyday-banking/payments/cards-digitalization/"
PROMO = "https://www.unicreditbulbank.bg/en/individual-clients/bank-cards/promotions/"
TERMINALS = "https://www.unicreditbulbank.bg/en/small-business/banking/terminals/"
SELLAVI = "https://www.unicreditbulbank.bg/en/small-business/banking/pay-by-link-sellavi/"
BLINK = "https://www.unicreditbulbank.bg/en/app/blink/"
UCG2Q26 = "https://www.unicreditgroup.eu/content/dam/unicreditgroup-eu/documents/en/investors/group-results/2026/2Q26/2Q26_Results.pdf"
MCDEAL = "https://insurancenewsnet.com/oarticle/unicredit-and-mastercard-expand-payments-partnership-10"
TOUCH = "https://www.mastercard.com/mt/en/news-and-trends/press/2024/april/unicredit-switches-to-mastercard-touch-card-with-accessibility-features-for-blind-and-partially-sighted-people.html"
C2PIT = "https://www.mastercard.com/news/europe/it-it/redazione/comunicati-stampa/it-it/unicredit-prima-grande-banca-commerciale-in-italia-ad-offrire-l-accesso-diretto-a-mastercard-click-to-pay-tramite-app/"
BCARD = "https://www.bcard.bg/en"
BORICA = "https://tools.prnewswire.com/en-us/live/20823/release/20260326EN18186"
ABB = "https://abanksb.bg/en/banking-system/the-banking-system-in-bulgaria-in-2025-main-highlights/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · ownership · euro", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a million customers, about a quarter of the Bulgarian banking system's profit, a foreign-trade bank from 1964 now 99.45% owned by UniCredit, and the switch to the euro on 1 January 2026.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Third by assets, €20.7bn.", "div": "ucb", "rev": "centre", "products": [
            P("balance", "2025 results", "Net profit of BGN 903 million (about €462 million) in 2025, down 4.7%; total assets BGN 41.0 billion, loans BGN 27.8 billion and deposits BGN 31.1 billion, each up about 18%; ROE 20.3%, cost/income 28.2%, CET1 20.6%; rated A-/F2 Stable by Fitch.",
              s=["con"], neo=[0, ""], src=[["Bulbank 2025 Annual Report", AR25]]),
            P("h1", "H1 2026 and market position", "Profit after tax of €268.7 million in the first half of 2026 and assets of €20.7 billion, about 17% of the system and third behind DSK Bank and UBB; number one in corporate loans with a 27.1% share.", short="H1 2026",
              s=["corp"], st="new", neo=[0, ""], src=[["BNB: Banks in Bulgaria, Q2 2026", BNB], ["Bulbank 2025 Annual Report", AR25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & ownership", "blurb": "Mintcheva; UniCredit 99.45%.", "div": "ucg", "rev": "centre", "products": [
            P("leadership", "Management and supervisory boards", "CEO Tzvetanka Mintcheva, who also sits on the board of BORICA, Bulgaria's card and instant-payments operator; CFO Nevena Nikše (from December 2024); executive directors Ivaylo Glavchovski, Borislav Bangeev and Borislav Genov; supervisory board chaired by Emilia Palibatchiyska.",
              s=["corp"], neo=[0, ""], src=[["Bulbank 2025 Annual Report", AR25], ["Bulbank: new CFO, Dec 2024", CFO], ["BNB: Banks in Bulgaria, Q2 2026", BNB]]),
            P("heritage", "Heritage & ownership", "Founded by decree in 1964 as Bulgaria's foreign-trade bank; merged with HVB Bank Biochim and Hebros Bank in 2007; 99.45% owned by UniCredit S.p.A., which took direct control from Bank Austria in 2016; paid a €277 million dividend for 2025.",
              s=["corp"], o="I", neo=[0, ""], src=[["BNB: Banks in Bulgaria, Q2 2026", BNB], ["Bulbank: dividend for 2025", DIVIDEND]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology & the euro", "blurb": "Euro switch, no outage.", "div": "ucb", "rev": "centre", "products": [
            P("tech", "Core systems & operations", "New core-banking servers, a private test cloud, Microsoft 365, a new BI tool and data-warehouse migration, and DORA, AnaCredit and AML programmes; domestic payments up 12.7% and international up 13.2% in 2025 without more staff.",
              s=["corp"], neo=[0, ""], src=[["Bulbank 2024 Annual Report", AR24], ["Bulbank 2025 Annual Report", AR25]]),
            P("euro", "Euro changeover", "The bank's top programme in 2024–25: accounts and loans redenominated, dual-currency display, unified SEPA payments and SEPA Instant, and every ATM and POS terminal switched to euro on 1 January 2026.",
              s=["con", "sme"], lc="move", st="new", ay="Jan 2026", neo=[0, ""], src=[["Bulbank 2025 Annual Report", AR25], ["Bulbank: POS devices to EUR, Dec 2025", POSEUR]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & capital", "blurb": "Organic growth, Unlimited.", "div": "ucg", "rev": "centre", "products": [
            P("strategy", "UniCredit Unlimited in Bulgaria", "The group's Unlimited plan (February 2026) replaces Unlocked; locally, organic growth, capital-light fee products and digital service, as the only big Bulgarian bank that has not grown by acquisition in a decade.",
              s=["corp"], st="new", neo=[0, ""], src=[["Bulbank 2025 Annual Report", AR25]]),
            P("srt", "Risk-sharing deals", "ARTS Morava (2024) and ARTS Silver-2 (July 2025) with PGGM: Silver-2 covers a €2.1 billion portfolio of Bulgarian corporate and SME loans, the largest such deal in the country.",
              s=["corp"], o="P", at="PGGM", ay="Jul 2025", neo=[0, ""], src=[["Bulbank: PGGM deal, Jul 2025", PGGM]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Mastercard debit and credit cards after a 2024 switch from Visa, phone wallets, card acceptance for a growing merchant base, BORICA's Blink and SEPA Instant for instant transfers, and corporate payments.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "Mastercard since 2024.", "div": "ucb", "rev": "retail", "products": [
            P("debit", "Debit Mastercard & Gold", "Contactless Debit Mastercard and Debit Mastercard Gold (Lounge Key), reissued from 2024 as Mastercard Touch Cards in recycled PVC; debit card transactions up 15% in 2025.", short="Debit (Mastercard)",
              s=["con"], lc="everyday", ay="2024", o="P", at="Mastercard", neo=[2, "Mastercard since the 2024 migration."],
              mc="The core of the switch: the debit book moved from a mixed estate to Mastercard.",
              src=[["Bulbank: debit cards", DEBIT], ["Bulbank 2025 Annual Report", AR25], ["Bulbank and Mastercard: guide dogs, Aug 2024", DOGS]]),
            P("digitaldebit", "Digital debit card", "Issued instantly in Bulbank Mobile with no plastic (launched 2024), added to Apple Pay, Google Pay or Huawei, and usable at ATMs; issuance up 33% in 2025.",
              s=["con"], lc="open", st="new", ay="2024", neo=[2, "Mastercard ⚠ inferred from the migration."], src=[["Bulbank: digital debit card", DIGIDEBIT], ["Bulbank 2025 Annual Report", AR25]]),
            P("kids", "Debit Mastercard Kids & Teens", "Free cards for ages 6–14 and 14–18 with parental spending controls; a raffle for new cards ran to 30 September 2026.",
              s=["fam"], lc="everyday", neo=[2, "Mastercard."], src=[["Bulbank: debit cards", DEBIT], ["Bulbank: card promotions", PROMO]]),
            P("visatail", "Visa Gold debit", "One Visa Gold debit card is still listed with Visa Luxury Hotel Collection benefits; the bank ended Visa issuing in 2024 at a cost of BGN 4.4 million, so this is likely a legacy card ⚠.", short="Visa Gold debit (legacy)",
              s=["aff"], lc="everyday", st="flux", o="I", at="Visa", neo=[0, "Visa."], src=[["Bulbank: debit cards", DEBIT], ["Bulbank 2024 Annual Report", AR24]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Shopping, Gold, Platinum.", "div": "ucb", "rev": "retail", "products": [
            P("credit", "UniCredit Shopping Card, Gold & Platinum Smart Credit", "Three Mastercard credit cards: Shopping Card (€500–2,499, first year free), Gold Smart Credit (to €15,000, lounges) and Platinum Smart Credit (to €50,000, Priority Pass); credit cards in circulation up 2.5% and transactions up 19% in 2025.", short="Credit (Mastercard)",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Bulbank: credit cards", CREDIT], ["Bulbank: card promotions", PROMO], ["Bulbank 2025 Annual Report", AR25]]),
            P("instal", "Card instalments", "Purchases over €25 split into up to 36 monthly instalments in Bulbank Mobile or Online, with a 0% fee for three instalments; instalments on debit cards since 2024.",
              s=["con"], lc="borrow", neo=[1, "The bank's own plan on Mastercard cards."],
              mc="Mastercard Installments could take the same plans to online checkout.",
              src=[["Bulbank: credit cards", CREDIT], ["Bulbank 2024 Annual Report", AR24]]),
        ]},
        {"id": "2.3", "ic": "smartphone", "name": "Wallets & tokens", "blurb": "Digitised payments +84%.", "div": "ucb", "rev": "retail", "products": [
            P("wallets", "Apple Pay, Google Pay, Huawei & Garmin Pay", "Bulbank cards in every major phone and watch wallet, plus a digital wallet in Bulbank Mobile for Android; payments with digitised cards rose 84% in 2024.",
              s=["con"], lc="everyday", o="P", at="Apple, Google, Huawei, Garmin", neo=[2, "Tokens on Mastercard cards ⚠."],
              mc="Click to Pay runs at UniCredit in Italy and Romania but is not seen in Bulgaria ⚠.",
              src=[["Bulbank: card digitalisation", WALLETS], ["Bulbank 2024 Annual Report", AR24], ["Mastercard: UniCredit Click to Pay, Italy", C2PIT]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acquiring", "blurb": "Merchants +13.6%.", "div": "ucb", "rev": "corporate", "products": [
            P("pos", "POS, mPOS & ePOS terminals", "Countertop, mobile and software terminals on phones and tablets; in 2025 the fleet grew 6%, merchants 13.6% and acquiring volume 13.5%, after 5,519 terminals were replaced in 2024.",
              s=["sme"], lc="move", neo=[1, "Accepts every scheme."],
              mc="Acquiring is the bank's own; gateway, risk and Tap on Phone services are open ground.",
              src=[["Bulbank: terminals", TERMINALS], ["Bulbank 2025 Annual Report", AR25]]),
            P("ecom", "E-commerce & Pay by Link", "Virtual POS with Apple Pay and Google Pay added in 2025, Pay by Link and QR payments with Sellavi (€4.60 a month), and CloudCart and Sellavi online shops.",
              s=["sme"], lc="move", st="new", o="P", at="Sellavi, CloudCart", neo=[1, "Accepts every scheme."], src=[["Bulbank: Pay by Link with Sellavi", SELLAVI], ["Bulbank 2025 Annual Report", AR25]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Instant payments", "blurb": "Blink and SEPA Instant.", "div": "ucb", "rev": "retail", "products": [
            P("blink", "Blink transfers & phone-number payments", "BORICA's Blink instant transfers, 24/7, up to BGN 30,000 in the app, and Blink P2P by mobile number (joined 2024), free up to €150; Blink donations from December 2025.",
              s=["con", "sme"], lc="move", o="P", at="BORICA", neo=[0, "BORICA's Blink."],
              mc="The A2A rail that competes with cards for person-to-person and bill payments.",
              src=[["Bulbank: Blink", BLINK], ["Bulbank: Blink donations", BLINKDON], ["Bulbank 2024 Annual Report", AR24]]),
            P("sepainst", "SEPA Instant", "Incoming cross-border SEPA Instant payments delivered with the euro in 2025, through BORICA's link to the ECB's TIPS.",
              s=["con", "corp"], lc="move", st="new", ay="2025", neo=[0, "SEPA Instant."], src=[["Bulbank 2025 Annual Report", AR25], ["BORICA: euro cutover, Mar 2026", BORICA]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Payments & cash management", "blurb": "PSP clearing, ISO 20022.", "div": "ucb", "rev": "corporate", "products": [
            P("cashmgmt", "Corporate payments & PSP clearing", "Bulk payments in ISO 20022, SWIFT and SEPA, and a settlement and clearing service, the first of its kind in Bulgaria, giving payment service providers access to the national BISERA6 system.",
              s=["corp"], lc="move", neo=[0, ""],
              mc="Mastercard Move could serve the growing international flows (+13.2% in 2025).",
              src=[["Bulbank 2024 Annual Report", AR24], ["Bulbank 2025 Annual Report", AR25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud controls that saved €3.5 million in 2025, app-based identity, AI assistants for customers and staff, merchant analytics from card data, and Mastercard-branded cashback.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "€3.5m of losses prevented.", "div": "ucb", "rev": "retail", "products": [
            P("fraud", "Fraud prevention", "Monitoring that prevented €3.5 million of losses in 2025, anti-fraud campaigns through the euro switch, dynamic passwords for online card payments and SMS alerts.",
              s=["con", "sme"], lc="everyday", neo=[0, "The bank's own."],
              mc="Scam scoring for Blink and SEPA Instant transfers is a gap.",
              src=[["Bulbank 2025 Annual Report", AR25]]),
            P("identity", "Digital identity", "Biometric self-reactivation of Bulbank Mobile, automatic caller identification through the app, and automatic KYC review.",
              s=["con"], lc="open", st="new", neo=[0, ""], src=[["Bulbank 2025 Annual Report", AR25], ["Bulbank 2024 Annual Report", AR24]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI", "blurb": "Niki, DigiMate, app assistant.", "div": "ucb", "rev": "retail", "products": [
            P("ai", "Niki, DigiMate & AI in the app", "The Niki voice bot in the contact centre (pilot, end of 2025), DigiMate, the first AI assistant for bank staff in Bulgaria, and real-time AI assistance in the mobile app, listed in UniCredit's 1H 2026 results.",
              s=["con"], lc="everyday", st="new", neo=[0, ""],
              mc="Agent Pay is untouched ground for the new assistant.",
              src=[["Bulbank 2025 Annual Report", AR25], ["UniCredit 2Q26 results", UCG2Q26]]),
        ]},
        {"id": "3.3", "ic": "chart-column", "name": "Merchant data & APIs", "blurb": "Peer-to-peer analytics.", "div": "ucb", "rev": "corporate", "products": [
            P("p2p", "Peer-to-Peer Comparative Analysis", "A Bulbank Online tool that benchmarks shopper behaviour at a merchant's locations against peers from anonymised POS data, with dashboards (second phase in 2025).",
              s=["sme", "corp"], lc="grow", st="new", neo=[0, "Built on the bank's own acquiring data."],
              mc="Mastercard's merchant data could widen it beyond the bank's terminals.",
              src=[["Bulbank 2025 Annual Report", AR25]]),
            P("psd2", "Open banking", "PSD2 compliance work; no public API product or open-finance offer found ⚠.",
              s=["sme"], lc="open", st="unconf", neo=[None, "Nothing public."], src=[["Bulbank 2024 Annual Report", AR24]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards & offers", "blurb": "Your Mastercard Day.", "div": "ucb", "rev": "retail", "products": [
            P("offers", "Mastercard cashback & campaigns", "\"Your Mastercard Day\" 10% cashback on food and drink every Tuesday in 2026, cashback abroad for Premium Mastercard, merchant prize draws and up to €20 for issuing a credit card in the app; a Mastercard Consumer Card Award for innovation in 2025.",
              s=["con"], lc="grow", st="new", o="P", at="Mastercard", neo=[2, "Mastercard-branded campaigns."], src=[["Bulbank: card promotions", PROMO], ["Bulbank 2025 Annual Report", AR25]]),
            P("vouchers", "Kaufland vouchers & beyond banking", "Kaufland voucher cards stored and managed in Bulbank Mobile (2025), alongside vignettes and fines.",
              s=["con"], lc="beyond", st="new", o="P", at="Kaufland", neo=[0, ""], src=[["Bulbank 2025 Annual Report", AR25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: Bulgaria's largest corporate loan book, trade finance and custody, mortgages and consumer loans, daily-banking plans and onemarkets funds, private banking on Mastercard World Elite, small-business packages, and leasing.",
    "tiles": [
        {"id": "4.1", "ic": "building-2", "name": "Corporate banking", "blurb": "Number one, 27.1%.", "div": "ucb", "rev": "corporate", "products": [
            P("corp", "Corporate lending", "Number one in corporate loans with a 27.1% share and 21.6% of system lending to companies; EU, EIF and EBRD guarantee schemes, project finance and green loans.",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="Commercial and virtual cards for Bulgaria's biggest corporate franchise are not public.",
              src=[["Bulbank 2025 Annual Report", AR25]]),
            P("trade", "Trade finance, custody & factoring", "Euromoney's best trade-finance bank in Bulgaria, Global Finance's best sub-custodian, and eFactoring.bg for domestic, export and reverse factoring.",
              s=["corp"], lc="move", neo=[0, ""], src=[["Bulbank 2025 Annual Report", AR25]]),
            P("markets", "Treasury, FX & capital markets", "Corporate FX and hedging, the most active primary dealer in government bonds, and debt, equity and M&A advisory.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["Bulbank 2024 Annual Report", AR24]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Retail lending", "blurb": "17.9% of retail loans.", "div": "ucb", "rev": "retail", "products": [
            P("mortgages", "Mortgages", "A 19.6% share of mortgages in 2024 and a Virtual Mortgage Center (Q4 2025) for a fully remote process by video, aimed also at Bulgarians abroad.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["Bulbank 2024 Annual Report", AR24], ["Bulbank 2025 Annual Report", AR25]]),
            P("ucfin", "Consumer loans & UniCredit Consumer Financing", "With UCFin, 17.9% of Bulgarian retail loans at end-2025 after 48 months of share gains; UCFin sells through branches, retail POS partners and campaigns and earned BGN 79 million in 2025.",
              s=["con"], lc="borrow", div="ucfin", neo=[0, ""], src=[["Bulbank 2025 Annual Report", AR25]]),
        ]},
        {"id": "4.3", "ic": "coins", "name": "Daily banking & savings", "blurb": "Plans, funds, pensions.", "div": "ucb", "rev": "retail", "products": [
            P("plans", "Daily banking plans & deposits", "Daily-banking plans with a Mastercard debit card, a digital savings account (12,000 sold in six months) and about 16% of household deposits.",
              s=["con", "fam"], lc="everyday", neo=[1, "Comes with a Mastercard debit card."], src=[["Bulbank 2024 Annual Report", AR24]]),
            P("invest", "onemarkets funds, pensions & insurance", "onemarkets funds with Amundi, BlackRock, PIMCO and J.P. Morgan bought in the app, the group's first fully digital voluntary pension sale (2025), and Allianz-linked insurance and certificates.",
              s=["con", "aff"], lc="grow", st="new", o="P", at="Allianz, onemarkets", neo=[0, ""], src=[["Bulbank 2025 Annual Report", AR25]]),
        ]},
        {"id": "4.4", "ic": "gem", "name": "Private banking", "blurb": "World Elite.", "div": "ucb", "rev": "private", "products": [
            P("private", "Private banking", "Best private bank in Bulgaria (Euromoney, The Banker 2025); a daily-banking plan with a Debit Mastercard World Elite and Mastercard Platinum credit, funds, certificates and brokerage.",
              s=["aff"], lc="grow", o="P", at="Mastercard", neo=[2, "Mastercard World Elite."], src=[["Bulbank 2024 Annual Report", AR24], ["Bulbank 2025 Annual Report", AR25]]),
        ]},
        {"id": "4.5", "ic": "briefcase", "name": "Small business", "blurb": "Packages and terminals.", "div": "ucb", "rev": "corporate", "products": [
            P("smebiz", "Small-business banking", "Packages, loans backed by EU and national guarantee schemes, business cards, terminals and online shops through Sellavi and CloudCart.",
              s=["sme"], lc="everyday", neo=[None, "Business-card network not stated ⚠."], src=[["Bulbank 2025 Annual Report", AR25]]),
        ]},
        {"id": "4.6", "ic": "factory", "name": "Leasing & fleet", "blurb": "Leasing, fleet, insurance.", "div": "leasing", "rev": "subs", "products": [
            P("leasing", "UniCredit Leasing, Fleet Management & Insurance Broker", "Equipment and vehicle leasing with international vendors and a lead in green financing, full-service operating leases from UniCredit Fleet Management, and an insurance broker.",
              s=["sme", "corp"], lc="borrow", neo=[0, ""],
              mc="Fleet and fuel cards for the leasing book are untested ground.",
              src=[["Bulbank 2025 Annual Report", AR25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: Bulbank Mobile for more than 800,000 active users, Bulbank Online for companies, 121 branches and the leading ATM deposit network, and remote bankers, agents and partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Bulbank Mobile", "blurb": "800k+ active users.", "div": "ucb", "rev": "retail", "products": [
            P("app", "Bulbank Mobile", "More than 800,000 active users and 1.5 million transfers a month, more than 20 fully digital journeys, a redesign in 2025, and Global Finance's best mobile app 2025 and six digital awards in 2026.",
              s=["con", "fam"], lc="everyday", neo=[0, ""], src=[["Bulbank 2025 Annual Report", AR25], ["Bulbank: Global Finance awards, Aug 2026", GF26]]),
            P("beyond", "MyCar & beyond banking", "MyCar (March 2024) tracks licences, fines and vehicle documents; vignettes, municipal taxes and fines are paid in the app.",
              s=["con"], lc="beyond", ay="Mar 2024", neo=[0, ""], src=[["Bulbank 2024 Annual Report", AR24]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Bulbank Online", "blurb": "Corporate NPS +60.", "div": "ucb", "rev": "corporate", "products": [
            P("online", "Bulbank Online & document exchange", "Corporate online banking rated NPS +60, 15 points ahead of rivals; Master Control self-service user management (2025) and the Digital Document Exchange platform, both on mobile.",
              s=["sme", "corp"], lc="everyday", neo=[0, ""], src=[["Bulbank 2025 Annual Report", AR25]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & ATMs", "blurb": "121 branches.", "div": "ucb", "rev": "retail", "products": [
            P("branches", "Branches", "121 branches and 161 points of presence at end-2025, moving from operations to advice, with cashless branches in large cities.",
              s=["con", "home"], lc="everyday", neo=[0, ""], src=[["Bulbank 2025 Annual Report", AR25]]),
            P("atm", "ATM network", "First in Bulgaria for ATM deposits; ATM deposit volumes up about 20% in 2025 as customers banked their leva before the euro.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Bulbank 2025 Annual Report", AR25]]),
        ]},
        {"id": "5.4", "ic": "headset", "name": "Remote & partners", "blurb": "Comfort, agents, partners.", "div": "ucb", "rev": "retail", "products": [
            P("comfort", "Comfort by UniCredit & contact centre", "Personal remote bankers (Comfort by UniCredit, renamed in 2025) and a contact centre with an NPS of 66 and sales up 12%.",
              s=["con", "sme"], lc="everyday", st="new", neo=[0, ""], src=[["Bulbank 2025 Annual Report", AR25]]),
            P("partners", "Agents & partners", "UniCredit Point agents in smaller towns (7 in 2024), UCFin's retail POS partners, and Sellavi and CloudCart for merchants.",
              s=["sme"], lc="open", o="P", at="Sellavi, CloudCart", neo=[0, ""], src=[["Bulbank 2024 Annual Report", AR24], ["Bulbank: Pay by Link with Sellavi", SELLAVI]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Bulbank", "blurb": "A whole card book moved in 2024.", "products": [
        P("mcatbulbank", "Mastercard at UniCredit Bulbank", "Under UniCredit's May 2023 group deal (13 banks, about 20 million cards), Bulbank moved its card book to Mastercard in 2024: Mastercard paid BGN 28 million of migration support and the bank spent BGN 4.4 million ending Visa issuing. Cards are Touch Cards in recycled PVC; Mastercard-branded cashback runs in 2026. Instant payments stay on BORICA's Blink.",
          s=["con"], div="ucg", rev="retail", mc="The relationship this map is drawn for.",
          src=[["Bulbank 2024 Annual Report", AR24], ["UniCredit and Mastercard, May 2023", MCDEAL], ["Mastercard: UniCredit Touch Card, Apr 2024", TOUCH]]),
    ]},
    {"id": "pillar-market", "name": "Bulgarian banking", "blurb": "Euro, Blink, consolidation.", "products": [
        P("market", "The Bulgarian market", "Euro adoption on 1 January 2026; 23 banks with €116 billion of assets at end-2025 (up 18.5%); DSK, UBB and Bulbank about level at the top; BORICA runs bcard, Blink and the euro cutover; Revolut and SEPA Instant compete for payments.",
          s=["con"], div="ucb", rev="centre", src=[["ABB: banking system in 2025", ABB], ["BNB: Banks in Bulgaria, Q2 2026", BNB], ["bcard", BCARD], ["BORICA: euro cutover, Mar 2026", BORICA]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
