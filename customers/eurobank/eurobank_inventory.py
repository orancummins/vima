"""Eurobank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own as reported in the press: the H1 2026 results (30–31 July 2026), Q1 2026 (8 May
2026) and FY2025 (March 2026). Eurobank's own websites refused automated reads, so several items rest on
coverage of its releases. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product
runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://cyprus-mail.com/2026/07/31/eurobank-posts-e738m-profit-in-first-half-of-2026-cyprus-contributes-e231m"
H1CY = "https://cyprus-mail.com/2026/08/05/eurobank-highlights-cyprus-role-in-regional-growth-plans"
Q1 = "https://cyprus-mail.com/2026/05/08/eurobank-posts-e351m-profit-cyprus-remains-key-contributor"
FY25 = "https://cyprus-mail.com/2026/03/10/eurobank-annual-profit-hits-e1-36bn-driven-by-cyprus-expansion"
EUROLIFE = "https://cyprus-mail.com/2026/05/07/eurobank-agrees-e813-million-eurolife-acquisition"
AWARDS = "https://cyprus-mail.com/2026/07/17/eurobank-named-cyprus-best-bank-praised-for-corporate-banking-services"
SUMMER = "https://cyprus-mail.com/2026/07/22/eurobank-offers-5-per-cent-cashback-on-summer-spending-in-greece"
MC = "https://www.euro2day.gr/en/article/2358425/eurobank-and-mastercard-expand-their-strategic-par"
MCPR = "https://www.eurobank.gr/-/media/eurobank/omilos/grafeio-tupou/deltia-tupou/2026/deltio-tupou-01-07-2026/deltio-tupou-01-07-2026.pdf"
FORWARD = "https://www.parapolitika.gr/business/article/1753738/eurobank-ependusi-1-dis-euro-stin-psifiaki-trapeziki-me-aihmi-tin-tehniti-noimosuni/"
GIANNAKLIS = "https://www.powergame.gr/trapezes/537885/eurobank-epistrefei-o-giannaklis-meta-tin-paraitisi-athanasopoulou/"
GPAY = "https://www.powergame.gr/trapezes/136820/eurobank-pliromes-mono-me-kinito-meso-tou-google-pay/"
CYCARDS = "https://fastforward.com.cy/business/eurobank-brings-its-cards-new-era"
WL21 = "https://www.in.gr/2021/12/07/english-edition/eurobank-sells-80-merchant-acquiring-activities-worldline-b-v/"
WL26 = "https://worldline.com/en-gr/home/top-navigation/media-relations/press-release/pr-2026_05_19_01"
SOFTPOS = "https://tapxphone.com/news/eurobank-launches-smartphone-payments-in-greece/"
FAIRFAX = "https://ered.gr/en/real-estate-news-fairfax-s-stake-in-eurobank-at-32-67/"
LISTING = "https://athens.euronext.com/en/more-options/announcements/listing-approval-and-start-trading-eurobank-sa"
WIKI = "https://en.wikipedia.org/wiki/Eurobank_Ergasias"
INBANK = "https://www.alantra.com/ib-transaction/inbank-as-ma-joint-venture-merger-eurobank-ergasias-sa/"
POSTBANK = "https://www.postbank.bg/en"
BGEURO = "https://content.postbank.bg/en/Bulgaria_Euro"
VISADEBIT = "https://eurobank.gr/en/retail/personal-banking/i-kathimerinotita-sas/personal-banking-debit-visa-card"
EMCREDIT = "https://www.euromonitor.com/credit-cards-in-greece/report"
EMCARDS = "https://www.euromonitor.com/financial-cards-and-payments-in-greece/report"
GLOBALDATA = "https://www.globaldata.com/store/report/greece-cards-and-payments-market-analysis/"
ALPHAVISA = "https://www.alpha.gr/-/media/AlphaGr/Files/Group/Press-Releases/2025/20250522-deltio-typou-en.pdf"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · ownership · plan", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: €113 billion of assets across Greece, Cyprus and Bulgaria, RoTBV near 17%, Fairfax as the largest shareholder, a bank built from Euromerchant and Ergasias, and a €1 billion technology plan.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "€113bn assets, RoTBV 16.6%.", "div": "group", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings, H1 2026", "Net profit of €738 million in the first half of 2026 (adjusted €776 million, RoTBV 16.6%); assets of €112.9 billion, loans of €58.1 billion, deposits of €86.4 billion, CET1 15.4%, NPE ratio 2.5% and cost-to-income 36.6% at 30 June 2026.",
              s=["con"], neo=[0, ""], src=[["Cyprus Mail: H1 2026 results", H1], ["Cyprus Mail: Q1 2026 results", Q1]]),
            P("fy25", "Full year 2025", "Net profit of €1.36 billion (adjusted €1.41 billion, of which €741 million international), NII €2.54 billion, fees €770 million (+15.7%), assets €108 billion, CET1 15.2%, RoTBV 16%.",
              s=["con"], neo=[0, ""], src=[["Cyprus Mail: FY2025 results", FY25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "Fairfax 32.67%; Karavias.", "div": "group", "rev": "group", "products": [
            P("listing", "Eurobank S.A. listing", "Eurobank S.A. absorbed its listed holding company on 12 December 2025; 3.63 billion new shares began trading in Athens on 15 December 2025. Market capitalisation and ratings were not confirmed ⚠.",
              s=["corp"], st="new", ay="Dec 2025", neo=[0, ""], src=[["Euronext Athens: listing of Eurobank S.A.", LISTING], ["Wikipedia: Eurobank Ergasias", WIKI]]),
            P("fairfax", "Fairfax", "Fairfax Financial Holdings holds 32.67% of shares and votes, the largest stake; it is also the seller of Eurolife Life.",
              s=["corp"], neo=[0, ""], src=[["ERED: Fairfax at 32.67%", FAIRFAX]]),
            P("leadership", "Board & management", "Chair Georgios Zanias, CEO Fokion Karavias (since 2015), Deputy CEOs Konstantinos Vasileiou, Iakovos Giannaklis (retail and digital) and Stavros Ioannou; Kostis Paikos is Group Chief Digital Officer. CFO not confirmed ⚠.",
              s=["corp"], neo=[0, ""], src=[["Parapolitika: Banking Forward, Jun 2026", FORWARD], ["PowerGame: Giannaklis returns, Oct 2023", GIANNAKLIS]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "Euromerchant, 1990.", "div": "group", "rev": "greece", "products": [
            P("heritage", "Heritage", "Euromerchant Bank (1990) became EFG Eurobank, merged with Bank of Athens (1999) and Ergasias Bank (2000), left the EFG group in 2012 and bought New TT Hellenic Postbank and New Proton Bank in 2013; 12,408 staff in 2025.",
              s=["con"], o="I", neo=[0, ""], src=[["Wikipedia: Eurobank Ergasias", WIKI]]),
            P("serbia", "Eurobank Serbia", "Sold to AIK Banka for €280 million in March 2023.",
              s=["con"], st="retired", ay="Mar 2023", neo=[None, ""], src=[["Wikipedia: Eurobank Ergasias", WIKI]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Banking Forward", "blurb": "€1bn on technology.", "div": "gr", "rev": "greece", "products": [
            P("forward", "Banking Forward technology plan", "About €1 billion over 2025–2028, the largest technology spend in Eurobank's history: cloud (about 50% of applications already), data, cybersecurity and AI, with more than 1,600 people in its Digital & Technology Hub and 100 new features in six months.",
              s=["corp"], st="new", ay="Jun 2026", o="B", neo=[0, ""], src=[["Parapolitika: Banking Forward, Jun 2026", FORWARD]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Plan & deals", "blurb": "RoTBV 17% by 2028.", "div": "group", "rev": "group", "products": [
            P("targets", "Business plan 2026–2028", "RoTBV of at least 16%, rising to 17% by 2028, and payouts above 50%; 2026 guidance raised in July to RoTBV close to 17%, core profit about €2 billion and about €4.5 billion of organic loan growth.",
              s=["corp"], neo=[0, ""], src=[["Cyprus Mail: FY2025 results", FY25], ["Cyprus Mail: Cyprus role and targets", H1CY]]),
            P("hellenic", "Hellenic Bank acquisition", "Stake raised from 29% to 55.9% (September 2024) and 100% (June 2025) after a mandatory bid at €4.843 a share; Hellenic Bank was merged into Eurobank Cyprus in 2025 ⚠ exact date.",
              s=["intl"], o="A", ay="Jun 2025", neo=[0, ""], src=[["Cyprus Mail: FY2025 results", FY25], ["Wikipedia: Eurobank Ergasias", WIKI]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Greek cards all moving to Mastercard, dual-network ranges in Cyprus and Bulgaria, tokenised wallets, card acceptance through Worldline and a phone terminal, IRIS and a UPI corridor to India, and buy-now-pay-later with Inbank.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Cards in Greece", "blurb": "All moving to Mastercard.", "div": "gr", "rev": "greece", "products": [
            P("grcards", "Eurobank debit & credit cards", "Consumer and business cards issued on both Visa and Mastercard until 2026; under the expanded partnership of 1 July 2026 Eurobank issues all its payment cards, for individuals and businesses, under the Mastercard brand. The reissue timetable is not public ⚠.", short="Greek cards (to Mastercard)",
              s=["con", "sme"], lc="everyday", st="flux", ay="Jul 2026", o="P", at="Mastercard", neo=[1, "Moving to Mastercard; Visa until reissued ⚠."],
              mc="The defining win: Greece's fastest-growing credit issuer goes all-Mastercard.",
              src=[["euro2day: Eurobank and Mastercard, Jul 2026", MC], ["Eurobank press release, 1 Jul 2026 ⚠", MCPR]]),
            P("visadebit", "Personal Banking Debit Visa", "A debit card for Personal Banking clients with higher cashback for those with an active payment account; still listed in 2026 ⚠, expected to move with the rest.",
              s=["con"], lc="everyday", st="flux", o="P", at="Visa", neo=[0, "Visa."], src=[["Eurobank: Personal Banking Debit Visa ⚠", VISADEBIT]]),
            P("bizcards", "Business cards", "Business debit and credit cards, covered by the July 2026 move to Mastercard ⚠ product names not public.",
              s=["sme", "corp"], lc="move", st="flux", ay="Jul 2026", o="P", at="Mastercard", neo=[2, "Mastercard ⚠ timing."],
              mc="Commercial-card tools could follow €36 billion of business lending.",
              src=[["euro2day: Eurobank and Mastercard, Jul 2026", MC]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Cards in Cyprus", "blurb": "Visa and Mastercard, May 2026.", "div": "cy", "rev": "cyprus", "products": [
            P("cycards", "Eurobank Cyprus card range", "New range from May 2026: Visa debit, credit, Gold, Teens, Youth and Prepaid; Mastercard debit, credit, Platinum and Business debit, credit and lite; biodegradable cards with a side notch for card type.", short="Cyprus cards (Visa & Mastercard)",
              s=["intl"], lc="everyday", st="new", ay="May 2026", o="P", at="Visa, Mastercard", neo=[1, "Split between Visa and Mastercard."],
              src=[["FastForward: Eurobank Cyprus cards, May 2026", CYCARDS]]),
            P("worldelite", "World Elite Mastercard", "The top card in the Cyprus range, on Mastercard.",
              s=["intl", "wealth"], lc="everyday", st="new", ay="May 2026", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["FastForward: Eurobank Cyprus cards, May 2026", CYCARDS]]),
        ]},
        {"id": "2.3", "ic": "coins", "name": "Cards in Bulgaria", "blurb": "Postbank, in euros.", "div": "postbank", "rev": "bulgaria", "products": [
            P("bgcards", "Postbank credit cards", "Mastercard Standard, Premium, Cash and World and Visa Classic, Gold and Premium, with limits up to €50,000 and cashback; switched to euros on 1 January 2026 without reissue.", short="Postbank cards (Visa & Mastercard)",
              s=["intl"], lc="borrow", o="P", at="Visa, Mastercard", neo=[1, "Split between Visa and Mastercard."],
              src=[["Postbank Bulgaria", POSTBANK], ["Postbank: the euro", BGEURO]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Wallets", "blurb": "Apple, Google, Garmin.", "div": "group", "rev": "greece", "products": [
            P("wallets", "Apple Pay, Google Pay & Garmin Pay", "Google Pay for Visa and Mastercard cards from October 2021, using tokens; Apple Pay and Garmin Pay also offered in Greece and Cyprus ⚠ launch dates.",
              s=["con", "intl"], lc="everyday", ay="Oct 2021", o="P", at="Google, Apple, Garmin", neo=[1, "Tokens on both networks."],
              src=[["PowerGame: Google Pay, Oct 2021 ⚠", GPAY], ["FastForward: Eurobank Cyprus cards, May 2026", CYCARDS]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "Worldline Greece.", "div": "gr", "rev": "greece", "products": [
            P("worldline", "Worldline Greece", "Eurobank's acquiring business, about 20% of the Greek market in 2021, was 80% sold to Worldline in 2021–22; Worldline bought the last 20% for €72 million on 19 May 2026. Eurobank remains a key distribution channel.",
              s=["sme"], lc="move", st="flux", ay="May 2026", o="P", at="Worldline", neo=[1, "Accepts every network."],
              src=[["Worldline: remaining 20%, May 2026", WL26], ["in.gr: Worldline deal, Dec 2021", WL21]]),
            P("smartpos", "Eurobank Smart POS", "A SoftPOS app that turns an Android phone into a contactless terminal, built on IBA Group technology and launched with Visa in November 2021; accepts Visa and Mastercard.",
              s=["sme"], lc="move", ay="Nov 2021", o="P", at="IBA Group, Visa", neo=[1, "Launched with Visa; accepts both."],
              src=[["tapxphone: Smart POS, Nov 2021", SOFTPOS]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Instant & cross-border", "blurb": "IRIS, UPI to India.", "div": "gr", "rev": "greece", "products": [
            P("iris", "IRIS instant payments", "Greece's account-to-account system, with QR-code online payments since January 2023; Eurobank's own IRIS volumes are not public ⚠.",
              s=["con", "sme"], lc="move", o="P", at="IRIS", neo=[0, "Domestic A2A."], src=[["GlobalData: Greece cards and payments", GLOBALDATA]]),
            P("upi", "Remittances to India", "Greece–India remittances on India's UPI, to be extended to Cyprus later ⚠ partner not named.",
              s=["con"], lc="move", st="new", o="P", at="UPI", neo=[0, "UPI."],
              mc="A corridor Mastercard Move could serve.",
              src=[["Cyprus Mail: Cyprus role and targets", H1CY]]),
        ]},
        {"id": "2.7", "ic": "hand-coins", "name": "Pay later", "blurb": "Inbank JV, 2027.", "div": "gr", "rev": "greece", "products": [
            P("inbank", "Inbank embedded-finance JV", "A 50/50 joint venture with Inbank (July 2026) for buy-now-pay-later, sales finance and consumer lending at Greek merchants; a Bank of Greece licence is pending and launch is targeted for Q1 2027.",
              s=["con", "sme"], lc="borrow", st="new", ay="Jul 2026", o="P", at="Inbank", neo=[None, "Not card-based on what is public."],
              mc="Installments on Mastercard cards could sit alongside it.",
              src=[["Alantra: Inbank JV, Jul 2026", INBANK]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: card controls and virtual cards, the EVA assistants and a GenAI factory, €pistrofi cashback at 8,500 Greek shops and Mastercard's Priceless, and fully digital account opening for 29 countries.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Card controls & security", "blurb": "Freeze, virtual cards.", "div": "cy", "rev": "cyprus", "products": [
            P("controls", "Card controls & virtual cards", "Freeze and unfreeze, notifications, cancellation and biometric viewing of card details and PIN in online banking and the app, and a virtual card in minutes for online shopping (Eurobank Cyprus).",
              s=["con", "intl"], lc="everyday", st="new", neo=[0, "Eurobank's own."], src=[["FastForward: Eurobank Cyprus cards, May 2026", CYCARDS]]),
            P("fraud", "Fraud prevention", "No public detail on Eurobank's fraud tools or partners ⚠; cybersecurity is one of the Banking Forward spending areas.",
              s=["con"], lc="everyday", neo=[None, "Nothing public."],
              mc="More than a million digital transactions a day and no named fraud partner.",
              src=[["Parapolitika: Banking Forward, Jun 2026", FORWARD]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI", "blurb": "EVA and a GenAI factory.", "div": "group", "rev": "greece", "products": [
            P("eva", "EVA & myEVA", "Virtual assistants for customers (also 'Ask EVA' at Postbank) and a GenAI Factory and Digital Brain for service, mortgage assessment, document processing and staff; more than 1,500 staff trained in machine learning and GenAI.",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="Agent Pay could give EVA tokenised Mastercard credentials.",
              src=[["Parapolitika: Banking Forward, Jun 2026", FORWARD], ["Postbank Bulgaria", POSTBANK]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards", "blurb": "€pistrofi and Priceless.", "div": "gr", "rev": "greece", "products": [
            P("epistrofi", "€pistrofi", "Cashback in euros at more than 8,500 points of sale in Greece and 850 in Cyprus; 5% back on summer spending in Greece to 20 August 2026.",
              s=["con", "sme"], lc="grow", o="B", neo=[0, "Eurobank's own; any card."],
              mc="Card-linked offers could widen the merchant base.",
              src=[["FastForward: Eurobank Cyprus cards, May 2026", CYCARDS], ["Cyprus Mail: summer cashback, Jul 2026", SUMMER]]),
            P("priceless", "Priceless", "From July 2026 Eurobank Mastercard holders get Priceless experiences in music, cinema and sport in more than 35 destinations, including presales; a first for a Greek bank.",
              s=["con", "wealth"], lc="grow", st="new", ay="Jul 2026", o="P", at="Mastercard", neo=[3, "Mastercard's own."],
              src=[["euro2day: Eurobank and Mastercard, Jul 2026", MC]]),
        ]},
        {"id": "3.4", "ic": "fingerprint", "name": "Digital onboarding", "blurb": "29 countries, all in the app.", "div": "gr", "rev": "greece", "products": [
            P("onboard", "Digital account opening", "The only Greek bank opening accounts fully in its app for residents of Greece and 28 other European countries; one in three products bought fully digitally in H1 2026, up more than 160%.",
              s=["con"], lc="open", st="new", o="B", neo=[0, ""],
              mc="Identity and open-finance checks could support onboarding across borders.",
              src=[["Parapolitika: Banking Forward, Jun 2026", FORWARD]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: €18 billion of household loans and €36 billion of business loans, private banking and funds, Eurolife insurance, and the banks in Cyprus and Bulgaria that earn nearly half the profit.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Households", "blurb": "€13bn of mortgages.", "div": "gr", "rev": "greece", "products": [
            P("mortgages", "Mortgages", "€13 billion of mortgages at 30 June 2026, with AI used in mortgage assessment.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["Cyprus Mail: H1 2026 results", H1], ["Parapolitika: Banking Forward, Jun 2026", FORWARD]]),
            P("consumer", "Consumer loans", "€5.1 billion of consumer loans at 30 June 2026; point-of-sale lending to move into the Inbank JV ⚠.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Cyprus Mail: H1 2026 results", H1]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Business & corporate", "blurb": "€36bn of loans.", "div": "group", "rev": "greece", "products": [
            P("business", "Business & corporate banking", "€36.3 billion of business loans, 61% of the book, and €2.7 billion of organic loan growth in the half; Euromoney named the Cyprus bank best for corporate banking in 2026.",
              s=["sme", "corp"], lc="borrow", neo=[1, "Business cards moving to Mastercard."],
              src=[["Cyprus Mail: H1 2026 results", H1], ["Cyprus Mail: Euromoney awards, Jul 2026", AWARDS]]),
        ]},
        {"id": "4.3", "ic": "gem", "name": "Wealth", "blurb": "€14.9bn private banking.", "div": "lux", "rev": "group", "products": [
            P("wealth", "Private banking & asset management", "Private-banking client assets and liabilities of €14.9 billion and managed funds of €11 billion (+29%) at 30 June 2026, including Eurobank Private Bank Luxembourg.",
              s=["wealth"], lc="grow", neo=[0, ""], src=[["Cyprus Mail: H1 2026 results", H1], ["Wikipedia: Eurobank Ergasias", WIKI]]),
        ]},
        {"id": "4.4", "ic": "shield-check", "name": "Insurance", "blurb": "Eurolife, €813m.", "div": "eurolife", "rev": "group", "products": [
            P("eurolife", "Eurolife Life", "Agreement of 7 May 2026 to buy the 80% it did not own from Fairfax for about €813 million; about 21% of Greek life premiums (FY24) and 1,200 intermediary agreements. Completion expected in Q3 2026 ⚠.",
              s=["wealth"], lc="grow", st="flux", ay="May 2026", o="A", neo=[0, ""], src=[["Cyprus Mail: Eurolife deal, May 2026", EUROLIFE]]),
            P("cyins", "ERB Cyprus insurance", "CNP Cyprus Insurance, bought for €182 million and merged into the Cypriot insurers in 2025; 45% of ERB Asfalistiki to be sold to Fairfax affiliates for about €55 million.",
              s=["intl"], lc="grow", o="A", neo=[0, ""], src=[["Cyprus Mail: FY2025 results", FY25], ["Cyprus Mail: Cyprus role and targets", H1CY]]),
        ]},
        {"id": "4.5", "ic": "earth", "name": "Cyprus & Bulgaria", "blurb": "46.5% of profit.", "div": "cy", "rev": "cyprus", "products": [
            P("cyprus", "Eurobank Cyprus", "The former Hellenic Bank and Eurobank Cyprus: €29.3 billion of assets, €24.1 billion of deposits and €231 million of adjusted profit in H1 2026; operational integration under way.",
              s=["intl"], lc="everyday", st="flux", o="A", neo=[1, "Visa and Mastercard cards."], src=[["Cyprus Mail: H1 2026 results", H1], ["Cyprus Mail: Cyprus role and targets", H1CY]]),
            P("bulgaria", "Postbank (Eurobank Bulgaria)", "€14.6 billion of assets, €9.8 billion of loans and €119 million of adjusted profit in H1 2026 (+7.8%), in the eurozone since January 2026.",
              s=["intl"], lc="everyday", o="I", neo=[1, "Visa and Mastercard cards."], src=[["Cyprus Mail: H1 2026 results", H1], ["Postbank: the euro", BGEURO]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the Eurobank Mobile App, where 61% of transactions happen, 562 branches, and partners from Worldline to Eurolife's intermediaries.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Mobile app", "blurb": "61% of transactions.", "div": "gr", "rev": "greece", "products": [
            P("app", "Eurobank Mobile App & e-banking", "96% of transactions are digital and 61% go through the app; about 574 million log-ins a year and more than a million digital transactions a day; 94% of under-35s use mobile.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, ""], src=[["Parapolitika: Banking Forward, Jun 2026", FORWARD]]),
            P("intlapps", "Eurobank Cyprus & Postbank apps", "Card controls and virtual cards in the Cyprus app; the Postbank App in Bulgaria.",
              s=["intl"], lc="everyday", neo=[0, ""], src=[["FastForward: Eurobank Cyprus cards, May 2026", CYCARDS], ["Postbank Bulgaria", POSTBANK]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "562 branches.", "div": "group", "rev": "group", "products": [
            P("branches", "Branches", "562 branches in Greece and abroad (December 2025), 67 of them branches and business centres in Cyprus.",
              s=["con", "home"], lc="everyday", neo=[0, ""], src=[["Wikipedia: Eurobank Ergasias", WIKI], ["Cyprus Mail: Cyprus role and targets", H1CY]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "Worldline, intermediaries.", "div": "group", "rev": "greece", "products": [
            P("partners", "Partners & intermediaries", "Worldline sells acceptance through Eurobank's network, Eurolife has 1,200 intermediary agreements, and the Inbank JV will reach shoppers at merchants from 2027.",
              s=["sme", "wealth"], lc="open", o="P", at="Worldline, Inbank", neo=[0, ""],
              src=[["Worldline: remaining 20%, May 2026", WL26], ["Cyprus Mail: Eurolife deal, May 2026", EUROLIFE], ["Alantra: Inbank JV, Jul 2026", INBANK]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Eurobank", "blurb": "Every Greek card to Mastercard.", "products": [
        P("mcateurobank", "Mastercard at Eurobank", "On 1 July 2026 Eurobank and Mastercard expanded a multi-year partnership: Eurobank will issue all of its payment cards, for individuals and businesses, under the Mastercard brand, and its Mastercard holders get Priceless, a first in Greece. Visa stays on cards not yet reissued and on half of the Cyprus and Bulgarian ranges; acceptance is Worldline's.",
          s=["con"], div="group", rev="group", mc="The relationship this map is drawn for.",
          src=[["euro2day: Eurobank and Mastercard, Jul 2026", MC], ["FastForward: Eurobank Cyprus cards, May 2026", CYCARDS]]),
    ]},
    {"id": "pillar-market", "name": "Greek payments", "blurb": "Visa credit, Mastercard debit, IRIS.", "products": [
        P("market", "The Greek market", "Mastercard leads Greek debit, with Piraeus the largest issuer; Visa leads credit through exclusive bank deals, Alpha Bank among them (renewed May 2025 ⚠); Eurobank was the credit issuer gaining most. IRIS gives account-to-account payments, including QR online since 2023.",
          s=["con"], div="group", rev="greece",
          src=[["Euromonitor: credit cards in Greece", EMCREDIT], ["Euromonitor: cards and payments in Greece", EMCARDS], ["Alpha Bank: Visa agreement, May 2025 ⚠", ALPHAVISA]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
