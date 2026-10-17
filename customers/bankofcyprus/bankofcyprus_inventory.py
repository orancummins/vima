"""Bank of Cyprus's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results presentation (4 August 2026),
the FY2025 preliminary results (18 February 2026) and the Investor Update (3 March 2026). ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1PRES = "https://www.bankofcyprus.com/globalassets/group/investor-relations/presentations/eng/20260804-1h2026-financial-results-presentation-_final.pdf"
H1NEWS = "https://cyprus-mail.com/2026/08/04/bank-of-cyprus-posts-e252-million-first-half-profit-raises-dividend"
FY25 = "https://www.athexgroup.gr/sites/default/files/hermes_3/2026-02/en/9f3afaf7-5944-4511-bafa-f75944b5115e/1391_883_2026_English_2.pdf"
IU = "https://www.athexgroup.gr/sites/default/files/hermes_3/2026-03/en/870008c7-42af-44bf-8008-c742af84bfec/1391_1103_2026_English_2.pdf"
CDB = "https://www.athexgroup.gr/sites/default/files/hermes_3/2026-03/en/9e3348ee-1ea2-4bba-b348-ee1ea20bba2c/1391_1620_2026_English_2.pdf"
Q1 = "https://athens.euronext.com/sites/default/files/hermes_3/2026-05/en/5666561a-f0ed-428d-a656-1af0ed728dd7/1391_3062_2026_English_2.pdf"
BOARD = "https://www.bankofcyprus.com/globalassets/group/investor-relations/press-releases/eng/20260515-bod-and-committee-composition_en_final.pdf"
HOLDERS = "https://www.bankofcyprus.com/en-gb/group/investor-relations/shareholder-information/major-holders-of-shares-and-financial-instruments/"
ATHEX = "https://bankofcyprus.com/globalassets/group/investor-relations/listing-on-athex/en/20240819-listing-and-delisting-announcement-_eng.pdf"
WIKI = "https://en.wikipedia.org/wiki/Bank_of_Cyprus"
CARDS = "https://www.bankofcyprus.com/en-gb/Personal/cards/"
DEBIT = "https://www.bankofcyprus.com/en-gb/Personal/cards/Personal/debit/"
CREDIT = "https://www.bankofcyprus.com/en-gb/Personal/cards/Personal/Credit/"
ELITE = "https://www.bankofcyprus.com/en-gb/Personal/cards/Personal/Credit/elite-mastercard/"
AEGEAN = "https://www.bankofcyprus.com/en-gb/group/news-archive/aegean-boc-mastercard/"
AEGEAN26 = "https://en.aegeanair.com/milesandbonus/news/2026/boc_coupons_update/"
BIZCREDIT = "https://www.bankofcyprus.com/en-gb/Personal/cards/business/business-credit/"
BIZDEBIT = "https://www.bankofcyprus.com/en-gb/Personal/cards/business/Business-Debit/"
SPECIAL = "https://www.bankofcyprus.com/en-gb/Personal/cards/business/special-cards"
PREPAID = "https://www.bankofcyprus.com/en-gb/Personal/cards/Personal/Prepaid/"
VIRTUAL = "https://www.bankofcyprus.com/en-gb/Personal/cards/Personal/virtual-card/"
VISAPLUS = "https://www.bankofcyprus.com/en-gb/Personal/cards/Personal/visa-plus/"
C2P = "https://www.bankofcyprus.com/en-gb/Personal/cards/Personal/click-to-pay/"
APPLEPAY = "https://bankofcyprus.com/en-gb/Personal/cards/digital-products/apple-pay"
GPAY = "https://www.bankofcyprus.com/en-gb/Personal/cards/digital-products/googlepay/"
FLEKSY = "https://bankofcyprus.com/en-gb/Personal/loans/Consumer/fleksy"
JCC = "https://www.jcc.com.cy/"
JCCDE = "https://www.jcc.com.cy/news-announcements/jcc-selected-to-participate-in-the-digital-euro-pilot/"
JCCMC = "https://www.jcc.com.cy/news-announcements/be-a-master-of-your-bills/"
JCCVISA = "https://www.jcc.com.cy/news-announcements/30-days-30-winners-30-smartphones/"
AVENGA = "https://www.cyprus-mail.com/2025/12/17/bank-of-cyprus-partners-with-avenga-for-new-ai-digital-platform"
EUROMONEY = "https://cyprus-mail.com/2026/07/30/bank-of-cyprus-named-cyprus-best-digital-bank"
CBCCARDS = "https://cyprus-mail.com/2026/07/22/cyprus-leads-euro-area-in-card-payments-as-digital-transactions-surge"
WEALTHY = "https://www.powergame.gr/trapezes/1313886/trapezas-kyprou-stratigiki-eisodos-sto-metochiko-kefalaio-tis-wealthyhood/"
EUROBANK = "https://www.cyprus-mail.com/2024/09/16/competition-watchdog-approves-eurobanks-acquisition-of-hellenic-bank-stake"
HELLENIC = "https://en.wikipedia.org/wiki/Hellenic_Bank"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · listing · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Cyprus' largest financial group with €29 billion of assets, ROTE near 19% and CET1 near 21%, a bank founded in 1899 that came through the 2013 bail-in, and a 2026–28 plan to pay out up to all of its profit.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "€252m in H1, ROTE 18.8%.", "div": "boc", "rev": "jccrev", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of €29.1 billion, gross performing loans of €11.4 billion and mainly retail deposits of €22.8 billion at 30 June 2026; profit after tax of €252 million in the half (ROTE 18.8%) and €481 million in 2025; CET1 20.9%, NPE ratio 1.0%, cost:income 36%. Rated A3 (Moody's deposits), BBB- (S&P) and BBB (Fitch).",
              s=["con"], neo=[0, ""], src=[["H1 2026 results presentation", H1PRES], ["FY2025 results", FY25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Governance & heritage", "blurb": "Arapoglou and Nicolaou.", "div": "boc", "rev": "jccrev", "products": [
            P("leadership", "Board, management & listing", "Chair Takis Arapoglou, Vice-Chair Georgios Syrichas, CEO Panicos Nicolaou (since 2019), Executive Director Finance Eliza Livadiotou. An Irish holding company listed on Euronext Athens and the Cyprus Stock Exchange since leaving London in September 2024; 436 million shares, Senvest (9.7%) and Lamesa (9.5%) the largest holders.",
              s=["corp"], neo=[0, ""], src=[["Board composition, May 2026", BOARD], ["Athens listing and London delisting, Aug 2024", ATHEX], ["Major holders", HOLDERS]]),
            P("heritage", "Heritage", "Founded in 1899 as the Nicosia Savings Bank; absorbed Laiki under the March 2013 bail-in; sold or closed its Greek, Russian, Romanian and UK businesses between 2013 and 2024 to become a Cyprus-focused group.",
              s=["con"], o="I", neo=[0, ""], src=[["Wikipedia: Bank of Cyprus", WIKI]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology & AI", "blurb": "Agentic AI on Azure.", "div": "bank", "rev": "jccrev", "products": [
            P("tech", "Cloud, AI & transformation", "A multi-year cloud strategy with Microsoft and a partnership with Avenga (December 2025) to build conversational banking on agentic AI and Azure AI services; internal AI assistants for call-centre staff. Led by George Kousis (Technology & Operations) and Dimitris Chouchoulis (Transformation).",
              s=["corp"], st="new", ay="Dec 2025", o="P", at="Avenga, Microsoft", neo=[0, ""], src=[["Cyprus Mail: Avenga partnership, Dec 2025", AVENGA]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy 2026–28", "blurb": "Mid-teens ROTE, up to 100% payout.", "div": "boc", "rev": "jccrev", "products": [
            P("strategy", "2026–28 targets", "Mid-teens ROTE (above 20% on 15% CET1), organic capital generation of 350–400 bps a year, cost:income about 40%, loan growth about 4% a year with international lending to about €2 billion by 2028, and payouts of up to 90% for 2026 and up to 100% for 2027–28.",
              s=["corp"], st="new", ay="Mar 2026", neo=[0, ""], src=[["Investor Update, Mar 2026", IU], ["H1 2026 results presentation", H1PRES]]),
            P("deals", "Bolt-on deals", "Ethniki Insurance Cyprus bought in July 2025 and merged into EuroLife and Genikes in December 2025; a 26% stake in Wealthyhood agreed in Q1 2026.",
              s=["aff"], o="A", neo=[0, ""], src=[["FY2025 results", FY25], ["Q1 2026 results", Q1]]),
            P("cdb", "CDB loans & deposits", "Agreement (26 March 2026) to take about €150 million of performing loans and about €500 million of deposits from The Cyprus Development Bank at near par, for about 35 bps of capital; completion expected in H2 2026.",
              s=["sme", "corp"], st="flux", ay="Mar 2026", o="A", neo=[0, ""], src=[["CDB agreement, Mar 2026", CDB]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: debit and credit cards issued on both Visa and Mastercard, the Aegean and Elite cards on Mastercard alone, Visa prepaid and Visa-only Click to Pay, wallets, QuickPay on Visa+ and instant payments, and JCC, the 75%-owned acquirer that takes every network.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "Visa and Mastercard.", "div": "bank", "rev": "consumer", "products": [
            P("debitvisa", "Visa Debit", "Ocean, Classic, Gold and Platinum Visa debit cards, with antamivi rewards, contactless, wallets and Priority Pass. The split of debit cards between networks is not published ⚠.", short="Debit (Visa)",
              s=["con", "young"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Bank of Cyprus: debit cards", DEBIT]]),
            P("debitmc", "Mastercard Debit", "Classic, Gold and Platinum Mastercard debit cards, with antamivi rewards, contactless, wallets and Mastercard Airport Security Fast Track.", short="Debit (Mastercard)",
              s=["con", "young"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard debit."], src=[["Bank of Cyprus: debit cards", DEBIT]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Both networks; Aegean on Mastercard.", "div": "bank", "rev": "consumer", "products": [
            P("creditvisa", "Visa Credit", "Classic, Gold and Platinum Visa credit cards with an interest-free period, travel insurance and antamivi.", short="Credit (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Bank of Cyprus: credit cards", CREDIT]]),
            P("creditmc", "Mastercard Credit", "Classic, Gold and Platinum Mastercard credit cards with travel insurance, antamivi and Fast Track on Platinum; Mastercard Blue closed to new customers on 1 February 2019.", short="Credit (Mastercard)",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard credit."], src=[["Bank of Cyprus: credit cards", CREDIT]]),
            P("elite", "Elite Mastercard", "The bank's top card: concierge, LoungeKey access to more than 1,200 lounges, free worldwide cash withdrawals and emergency cash; offered through personal banking advisers. Mastercard tier not stated ⚠.",
              s=["aff"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard only."], src=[["Bank of Cyprus: Elite Mastercard", ELITE]]),
            P("aegean", "Aegean Mastercard", "Co-brand with Aegean Airlines' Miles+Bonus, personal and business (about 2021 ⚠): 3,000 or 4,000 welcome miles, miles on all spending; from 8 May 2026 one €40 flight voucher a year instead of two €20 vouchers.", short="Aegean (Mastercard)",
              s=["con", "sme"], lc="borrow", st="flux", ay="2021", o="P", at="Aegean Airlines, Mastercard", neo=[2, "Mastercard co-brand."],
              mc="The bank's only co-brand, and it is Mastercard's; its benefits were trimmed in 2026.",
              src=[["Bank of Cyprus: Aegean Mastercard", AEGEAN], ["Aegean: coupon update, May 2026", AEGEAN26]]),
        ]},
        {"id": "2.3", "ic": "briefcase", "name": "Business cards", "blurb": "Debit, credit, prepaid.", "div": "bank", "rev": "business", "products": [
            P("bizcards", "Business debit & credit", "Business Debit Visa and Mastercard Business Debit; Business Credit Visa, Mastercard Business Credit and Aegean Mastercard Business, with Priority Pass and Fast Track; ordered with digital business-account opening since 2026.",
              s=["sme"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard versions."], src=[["Bank of Cyprus: business debit", BIZDEBIT], ["Bank of Cyprus: business credit", BIZCREDIT]]),
            P("topup", "Mastercard Business Top Up", "A prepaid business card with no credit limit, loaded as needed, with SMS or push alerts.",
              s=["sme"], lc="move", o="P", at="Mastercard", neo=[2, "Mastercard prepaid."],
              mc="A base for virtual and expense cards for business clients.",
              src=[["Bank of Cyprus: special cards", SPECIAL]]),
        ]},
        {"id": "2.4", "ic": "gift", "name": "Prepaid & virtual", "blurb": "Prepaid Visa, a virtual card.", "div": "bank", "rev": "consumer", "products": [
            P("prepaid", "Prepaid Visa", "A reloadable prepaid card for anyone aged 16 or over, with antamivi and wallets.",
              s=["young"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Bank of Cyprus: prepaid", PREPAID]]),
            P("virtual", "Virtual card", "A no-fee digital card for online shopping, with no plastic and antamivi rewards; network not stated ⚠.",
              s=["con", "young"], lc="everyday", st="new", neo=[None, "Network not stated."], src=[["Bank of Cyprus: virtual card", VIRTUAL]]),
            P("youthcard", "Youth Culture Card", "A prepaid card for 18–21-year-olds with a €220 offer for concerts and theatre; network not stated ⚠.",
              s=["young"], lc="beyond", neo=[None, "Network not stated."], src=[["Bank of Cyprus: cards", CARDS]]),
        ]},
        {"id": "2.5", "ic": "smartphone", "name": "Wallets & Click to Pay", "blurb": "Click to Pay on Visa only.", "div": "bank", "rev": "consumer", "products": [
            P("wallets", "Apple Pay, Google Pay & Garmin Pay", "All BoC Visa and Mastercard cards, personal and business, can be tokenised into Google Wallet (terms from 2022–23), Apple Pay (authenticated in the BoC app) and Garmin Pay.",
              s=["con"], lc="everyday", o="P", at="Apple, Google, Garmin", neo=[1, "Tokens on both networks."], src=[["Bank of Cyprus: Google Pay", GPAY], ["Bank of Cyprus: Apple Pay", APPLEPAY]]),
            P("c2p", "Click to Pay", "Online checkout without card details for Visa debit, credit and prepaid cards, enrolled in the app and approved by push or one-time code; Mastercard cards are not offered.", short="Click to Pay (Visa only)",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa only."],
              mc="Every card family is also issued on Mastercard, yet only Visa cards get Click to Pay.",
              src=[["Bank of Cyprus: Click to Pay", C2P]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "P2P & instant", "blurb": "QuickPay on Visa+.", "div": "bank", "rev": "consumer", "products": [
            P("quickpay", "QuickPay & Visa+", "Send money by mobile number in the BoC app (259,000 active users, June 2026); receiving runs on Visa+, which pays into any linked personal Visa or Mastercard card or account, usually instantly.", short="QuickPay (Visa+)",
              s=["con"], lc="move", o="P", at="Visa", neo=[0, "Visa+."],
              mc="Visa owns the P2P rail; Mastercard Move has no foothold.",
              src=[["Bank of Cyprus: Visa+", VISAPLUS], ["H1 2026 results presentation", H1PRES]]),
            P("instant", "SEPA instant transfers", "Instant credit transfers under the EU Instant Payments Regulation reached about 32% of Cyprus' SEPA transfer volume in the second half of 2025; the bank's own volumes are not published ⚠.",
              s=["con", "sme"], lc="move", neo=[0, "SEPA Instant."], src=[["Cyprus Mail: CBC payments report, Jul 2026", CBCCARDS]]),
            P("digitaleuro", "Digital euro pilot", "JCC was selected by the ECB as a participating payment service provider in the digital euro pilot (July 2026).",
              s=["con"], lc="move", st="new", ay="Jul 2026", o="P", at="ECB", neo=[0, ""], src=[["JCC: digital euro pilot, Jul 2026", JCCDE]]),
        ]},
        {"id": "2.7", "ic": "store", "name": "JCC acquiring", "blurb": "€9.2bn in H1, every network.", "div": "jcc", "rev": "jccrev", "products": [
            P("jcc", "JCC Payment Systems", "Card processing and acquiring in Cyprus since 1989, 75% owned: €9.2 billion of transactions in H1 2026 (+11%), €15 million of net fees; JCC Gateway, pay-by-link, QR Pay, SoftPOS, DCC and instalments; accepts Visa, Mastercard, Amex, Diners, UnionPay and JCB.", short="JCC (all networks)",
              s=["merch"], lc="move", o="B", neo=[1, "Acquires every network."],
              mc="Cyprus' main acquirer sits inside the group.",
              src=[["H1 2026 results presentation", H1PRES], ["JCC", JCC]]),
            P("jccsmart", "JCCsmart", "Bill and subscription payments without a merchant website, relaunched in June 2024; a Mastercard bill-pay campaign ran from September to December 2025 and a Visa smartphone promotion in September 2026.",
              s=["con", "merch"], lc="move", o="B", neo=[1, "Campaigns with both networks."], src=[["JCC: Be a master of your bills, Sep 2025", JCCMC], ["JCC: Visa promotion, Sep 2026", JCCVISA]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: antamivi rewards on cards of both networks, Fleksy, the first buy-now-pay-later in Cyprus, alerts and JCC's fraud and trust services, conversational AI on the way, and Jinius, the group's e-invoicing and marketplace platform.",
    "tiles": [
        {"id": "3.1", "ic": "gift", "name": "Rewards", "blurb": "antamivi on both networks.", "div": "bank", "rev": "consumer", "products": [
            P("antamivi", "antamivi", "The card rewards scheme on BoC Visa and Mastercard cards, with cashback at participating merchants (1.2% under the Aegean terms) and embedded in Jinius.",
              s=["con", "merch"], lc="grow", o="B", neo=[1, "Visa and Mastercard cards."],
              mc="Card-linked offers could feed antamivi and Jinius.",
              src=[["Bank of Cyprus: Aegean Mastercard", AEGEAN], ["H1 2026 results presentation", H1PRES]]),
        ]},
        {"id": "3.2", "ic": "coins", "name": "Buy now, pay later", "blurb": "Fleksy, €8m since launch.", "div": "bank", "rev": "consumer", "products": [
            P("fleksy", "Fleksy", "An overdraft-backed account with a digital debit card: limits of €500–3,000 over 3, 6 or 9 months; about €8.0 million used since launch, €4.5 million in H1 2026; four merchants pay the fee for customers. Card network not stated ⚠.",
              s=["con"], lc="borrow", st="new", o="B", neo=[None, "Network not stated."],
              mc="Mastercard Installments could carry Fleksy beyond the bank's merchants.",
              src=[["Bank of Cyprus: Fleksy", FLEKSY], ["H1 2026 results presentation", H1PRES]]),
        ]},
        {"id": "3.3", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Alerts, 3-D Secure, eIDAS.", "div": "jcc", "rev": "jccrev", "products": [
            P("security", "Card security & fraud monitoring", "SMS or push alerts on every card, 3-D Secure 2.0 under PSD2, and JCC's transaction monitoring, run for more than 35 years. No Visa or Mastercard fraud product is named ⚠.",
              s=["con", "merch"], lc="everyday", neo=[0, "Own and JCC's."], src=[["JCC", JCC], ["Bank of Cyprus: cards", CARDS]]),
            P("trust", "JCC trust services", "eIDAS-certified e-signatures, e-seals and eIDentity, with a signing portal and APIs.",
              s=["sme", "corp"], lc="open", o="B", neo=[0, ""], src=[["JCC", JCC]]),
        ]},
        {"id": "3.4", "ic": "bot", "name": "Conversational AI", "blurb": "Banking in plain language.", "div": "bank", "rev": "consumer", "products": [
            P("assistant", "Conversational banking", "Customers will use natural language in the BoC app to transact, get guidance and support, built with Avenga on agentic AI and Azure (announced December 2025); launch timing not confirmed ⚠.",
              s=["con"], lc="everyday", st="new", ay="Dec 2025", o="P", at="Avenga, Microsoft", neo=[0, ""],
              mc="Agentic banking in the app is open ground for Agent Pay.",
              src=[["Cyprus Mail: Avenga partnership, Dec 2025", AVENGA]]),
        ]},
        {"id": "3.5", "ic": "network", "name": "Jinius", "blurb": "€1.7bn exchanged in H1.", "div": "jinius", "rev": "business", "products": [
            P("jiniusb2b", "Jinius for business", "E-invoicing, remittances, tenders and a Car Dealers' Portal for about 1,930 companies; €1.7 billion exchanged in H1 2026 and €2.6 billion in 2025.",
              s=["sme", "corp"], lc="move", o="B", neo=[0, ""], src=[["H1 2026 results presentation", H1PRES], ["FY2025 results", FY25]]),
            P("marketplace", "Jinius Marketplace", "A consumer marketplace launched in February 2024 with 16 categories, gross merchandise value up 160% in a year, and Fleksy, QuickLoans and insurance at checkout; a cars marketplace and developer portals are planned.",
              s=["con", "merch"], lc="beyond", ay="Feb 2024", o="B", neo=[0, ""], src=[["H1 2026 results presentation", H1PRES], ["FY2025 results", FY25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: consumer accounts and loans, much of it now digital; SME and corporate lending; a growing international book; EuroLife and Genikes, first and second in Cypriot insurance; and private banking and investing.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Consumer banking", "blurb": "€204m income in H1.", "div": "bank", "rev": "consumer", "products": [
            P("accounts", "Accounts & QuickAccounts", "Current and savings accounts for about three quarters of Cypriots, 63,576 QuickAccounts opened digitally by June 2026, in euros, sterling and dollars.",
              s=["con"], lc="open", neo=[1, "Debit on Visa or Mastercard."], src=[["H1 2026 results presentation", H1PRES], ["FY2025 results", FY25]]),
            P("housing", "Housing loans", "Mortgages including a digital housing loan with an instant decision (€33 million by June 2026), the first in the market.",
              s=["con"], lc="borrow", st="new", neo=[0, ""], src=[["H1 2026 results presentation", H1PRES], ["Cyprus Mail: Euromoney award, Jul 2026", EUROMONEY]]),
            P("quickloans", "QuickLoans", "Digital consumer loans, €192 million outstanding at 30 June 2026.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["H1 2026 results presentation", H1PRES]]),
            P("joey", "Joey", "Banking for children aged 6 to 17 without needing a phone, with savings goals and transfers; about 12,900 users by June 2026. Card network not stated ⚠.",
              s=["young"], lc="open", st="new", neo=[None, "Network not stated."], src=[["H1 2026 results presentation", H1PRES]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "SME & corporate", "blurb": "€1.6bn new lending in H1.", "div": "bank", "rev": "business", "products": [
            P("business", "SME & corporate banking", "Lending, accounts and cash management for Cypriot businesses; digital business-account opening with a debit card launched in 2026.",
              s=["sme", "corp"], lc="borrow", neo=[1, "Business cards on both networks."], src=[["H1 2026 results presentation", H1PRES]]),
            P("dealers", "Car Dealers' Portal", "Instant digital car-loan quotes and financing through the dealer.",
              s=["con", "merch"], lc="borrow", st="new", neo=[0, ""], src=[["H1 2026 results presentation", H1PRES]]),
        ]},
        {"id": "4.3", "ic": "earth", "name": "International", "blurb": "€1.4bn, aiming for €2bn.", "div": "bank", "rev": "intl", "products": [
            P("intl", "International lending & IBU", "International corporate lending, shipping and syndicated loans (about €1.4 billion at end-2025, up 42%, targeted at about €2 billion by 2028) and the IBU serving international companies.",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="Commercial and virtual cards for international clients are untested.",
              src=[["FY2025 results", FY25], ["Investor Update, Mar 2026", IU]]),
        ]},
        {"id": "4.4", "ic": "shield-check", "name": "Insurance", "blurb": "#1 life, #2 non-life.", "div": "eurolife", "rev": "ins", "products": [
            P("lifeins", "EuroLife", "Life insurance, first in Cyprus with about a 33% share; solvency ratio 245%.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["H1 2026 results presentation", H1PRES]]),
            P("genins", "Genikes Insurance", "General insurance, second in Cyprus with about a 16% share, €44 million of premiums in H1 2026 and motor and home cover sold in the app.",
              s=["con", "aff"], lc="grow", neo=[0, ""], src=[["H1 2026 results presentation", H1PRES], ["FY2025 results", FY25]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Wealth & investing", "blurb": "Wealthyhood, 26%.", "div": "bank", "rev": "consumer", "products": [
            P("privatebank", "Private banking", "Euromoney's best private bank in Cyprus for the second year, with assets under management up 36% in 2025.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["Cyprus Mail: Euromoney award, Jul 2026", EUROMONEY]]),
            P("wealthyhood", "Digital investing & Wealthyhood", "A digital investing platform launched in 2026 and a 26% stake in Wealthyhood (about €6 million ⚠), giving retail customers stocks and ETFs.",
              s=["aff"], lc="grow", st="new", ay="2026", o="A", at="Wealthyhood", neo=[0, ""], src=[["Q1 2026 results", Q1], ["Powergame: Wealthyhood stake", WEALTHY]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the BoC Mobile App and 1bank for 517,000 digital users, 56 branches, and Jinius and partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "BoC Mobile App", "blurb": "488,000 active users.", "div": "bank", "rev": "consumer", "products": [
            P("app", "BoC Mobile App & 1bank", "488,000 active app users and 517,000 active digital users at 30 June 2026, a third of them logging in every day; Euromoney's best digital bank in Cyprus for 2025.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["H1 2026 results presentation", H1PRES], ["Cyprus Mail: Euromoney award, Jul 2026", EUROMONEY]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "56 in Cyprus.", "div": "bank", "rev": "consumer", "products": [
            P("branches", "Branches", "56 branches in Cyprus, two of them cash offices, and 2,850 staff at the end of 2025.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["FY2025 results", FY25]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Jinius & partners", "blurb": "Marketplace, dealers, Aegean.", "div": "jinius", "rev": "business", "products": [
            P("partners", "Jinius app & partners", "The Jinius apps for iOS and Android, car dealers, Fleksy merchant partners and the Aegean co-brand.",
              s=["con", "merch"], lc="open", o="P", neo=[0, ""], src=[["H1 2026 results presentation", H1PRES]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Bank of Cyprus", "blurb": "Both networks; Visa has the extras.", "products": [
        P("mcatboc", "Mastercard at Bank of Cyprus", "Bank of Cyprus issues debit, credit and business cards on both Visa and Mastercard and does not publish the split ⚠. Mastercard alone carries the Aegean co-brand, the Elite card and the business prepaid card; JCC, 75% owned, acquires every network and ran a Mastercard bill-pay campaign in 2025. Visa has the extras: Click to Pay, Visa+ behind QuickPay and the only personal prepaid card.",
          s=["con"], div="boc", rev="jccrev", mc="The relationship this map is drawn for.",
          src=[["Bank of Cyprus: debit cards", DEBIT], ["Bank of Cyprus: Click to Pay", C2P], ["Bank of Cyprus: Visa+", VISAPLUS]]),
    ]},
    {"id": "pillar-market", "name": "Cyprus banking", "blurb": "Two big banks, card-heavy.", "products": [
        P("market", "The Cypriot market", "A consolidated market led by Bank of Cyprus and Eurobank, which absorbed Hellenic Bank in 2025 ⚠. Cyprus has the euro area's highest card share of non-cash payments (75% by volume in H2 2025), instant transfers at about 32% of SEPA volume, and a digital euro pilot under way.",
          s=["con"], div="boc", rev="jccrev", src=[["Cyprus Mail: CBC payments report, Jul 2026", CBCCARDS], ["Wikipedia: Hellenic Bank", HELLENIC], ["Cyprus Mail: Eurobank and Hellenic, Sep 2024", EUROBANK]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
