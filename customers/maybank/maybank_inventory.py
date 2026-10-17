"""Maybank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 2Q FY26 results (27 August 2026), the FY2025
results (26 February 2026) and the ROAR30 strategy (21 January 2026). Maybank's Malaysian and Singapore retail
sites could not be read, so card networks there come from comparison sites and press. ``neo`` is the Mastercard
lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://www.theasianbanker.com/press-releases/maybank-s-2q-fy26-net-profit-rises-2-4-to-668-million-1h-profit-reaches-1-28-billion"
STAR2Q = "https://www.thestar.com.my/business/business-news/2026/08/27/maybank039s-2q-net-profit-rises-to-rm269bil-declares-31c-divshare"
FY25 = "https://www.theasianbanker.com/press-releases/maybank-fy25-roe-rises-to-11-7-as-net-profit-reaches-2-3b-and-casa-ratio-strengthens-to-40-5"
ROAR = "https://www.theasianbanker.com/press-releases/maybank-launches-roar30-targets-roe-of-13-14-by-2030"
LEAD = "https://www.maybank.com/en/about-us/leadership.page"
HIST = "https://www.maybank.com/en/about-us/history.page"
HOME = "https://www.maybank.com/en/index.page"
WIKI = "https://en.wikipedia.org/wiki/Maybank"
CARDS = "https://ringgitplus.com/en/credit-card/Maybank/"
GRAB20 = "https://www.marketing-interactive.com/maybank-goes-platinum-in-credit-card-partnership-with-grab"
GRABEND = "https://ringgitplus.com/en/blog/credit-card-news/maybank-discontinues-grab-mastercard-platinum-credit-card-from-7-september-2026.html"
WEMC = "https://ringgitplus.com/en/blog/personal-finance-news/maybank-revises-world-elite-mastercard-perks-for-2026.html"
NADI = "https://www.bharian.com.my/amp/bisnes/korporat/2026/07/1584153/maybank-islamic-perkenal-kad-kredit-mudah-digunakan-inklusif-untuk"
DEBIT = "https://www.maybank2u.com.my/maybank2u/malaysia/en/personal/cards/debit/maybank_visa_debit.page"
KAWANKU = "https://ringgitplus.com/en/debit-card/Maybank-MyDebit-Kawanku.html"
QRPAY = "https://www.maybank2u.com.my/maybank2u/malaysia/en/personal/services/digital_banking/maybank_qrpay_consumer.page"
QRBIZ = "https://apps.apple.com/app/id1320603823"
SAMSUNG = "https://ringgitplus.com/en/blog/bank-news/maybank-adds-qr-payments-to-samsung-wallet.html"
CHINA = "https://thesun.my/news/malaysia-news/maybank-expands-cross-border-qr-pay-service-to-china-af11726134/"
APPLEPAY = "https://ringgitplus.com/en/blog/bank-news/maybank-apple-pay-in-malaysia-full-list-of-cards-supported-amex-coming-soon.html"
SHARE18 = "https://malaymail.com/news/money/2018/05/03/maybank-eyes-rm50b-credit-card-billing-this-year/1626981"
AMEX06 = "https://www.malaysiakini.com/news/54793"
PAYNET = "https://paynet.my/about-us/media-centre/press-release/8-44-billion-transactions-processed-in-2025-as-digital-payments-become-malaysians-preferred-way-to-pay.html"
BNM = "https://www.nst.com.my/amp/business/corporate/2026/03/1407140/bank-negara-malaysias-e-payment-transactions-jump-25pct-184bil"
VISACHK = "https://www.visa.com.my/about-visa/newsroom/press-releases/visa-and-maybank-to-simplify-online-shopping-with-visa-checkout-in-malaysia.html"
FCB = "https://www.businesstoday.com.my/2024/08/13/fc-barcelona-maybank-extend-partnership-until-2027/"
SGCARDS = "https://www.singsaver.com.sg/credit-card/maybank"
XL = "https://milelion.com/2025/07/29/maybank-xl-rewards-card-4-mpd-on-all-fcy-spend-dining-shopping-travel-and-entertainment/"
IDCC = "https://www.maybank.co.id/id/creditcard"
IDDEBIT = "https://www.maybank.co.id/id/savings/Maybank-Kartu-ATM-Debit"
IDTP = "https://www.maybank.co.id/id/premier/Mastercard-Travel-Pass"
IDHOME = "https://www.maybank.co.id/"
IDRUN = "https://investortrust.id/lifestyle/90779/gandeng-visa-maybank-indonesia-siap-gelar-maybank-marathon-2026-di-bali"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · footprint · ROAR30", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: RM696 billion of loans and a 12% return on equity, a bank that opened in a Kuala Lumpur shop lot in 1960 and now spans ASEAN, and ROAR30, a five-year plan with RM10 billion for technology.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "RM696bn of loans, ROE 12%.", "div": "group", "rev": "ho", "products": [
            P("balance", "Balance sheet & earnings", "Group loans of RM695.9 billion at 30 June 2026 (up 2.7%), CASA ratio 41.5% and CET1 14.92%; net profit of RM2.69 billion in 2Q FY26 (ROE 12.0%, cost-to-income 49.1%) and RM10.51 billion in 2025 (ROE 11.7%). Total assets about RM1.05 trillion ⚠; market cap and ratings not confirmed ⚠.",
              s=["con"], neo=[0, ""], src=[["Asian Banker: 2Q FY26 results, Aug 2026", Q2], ["Asian Banker: FY25 results, Feb 2026", FY25], ["Wikipedia: Maybank", WIKI]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Khairussaleh and Zamzamzairani.", "div": "group", "rev": "ho", "products": [
            P("leadership", "Board & group management", "Chairman Tan Sri Zamzamzairani Mohd Isa, President & Group CEO Dato' Sri Khairussaleh Ramli, CFO Shafiq Abdul Jabbar; Syed Ahmad Taufik Albar runs Community Financial Services, John Chong Global Banking, Mohamad Yasin Abdullah Islamic banking and Giorgio Migliarina technology and digital; Alvin Lee leads Singapore and Steffano Ridwan Indonesia.",
              s=["corp"], neo=[0, ""], src=[["Maybank: our leadership", LEAD]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & footprint", "blurb": "The coffee-shop bank, 1960.", "div": "group", "rev": "ho", "products": [
            P("heritage", "Heritage", "Opened on 12 September 1960 in a Kuala Lumpur shop lot, the first home-grown Malaysian bank; bought Amex's Malaysian charge-card business in 2006 (RM80 million), Bank Internasional Indonesia in 2008 and Kim Eng in 2011. Head office now in the Merdeka 118 tower ⚠.",
              s=["con"], o="I", neo=[0, ""], src=[["Maybank: our history", HIST], ["Malaysiakini: Amex deal, 2006", AMEX06], ["Maybank: home", HOME]]),
            P("footprint", "Footprint", "Three home markets (Malaysia, Singapore, Indonesia), a presence in all ten ASEAN countries and beyond, about 2,600 branches and over 43,000 staff ⚠.",
              s=["reg"], neo=[0, ""], src=[["Wikipedia: Maybank", WIKI]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "ROAR30 & technology", "blurb": "ROE 13–14% by 2030.", "div": "group", "rev": "ho", "products": [
            P("roar30", "ROAR30", "Five-year plan launched in January 2026: ROE of 13–14%, NIM above 2.05% and cost-to-income at or below 47% by 2030, with four businesses to lead in — Islamic finance, regional wealth, regional transactions and payments, and corporate and investment banking.",
              s=["corp"], st="new", ay="Jan 2026", neo=[0, ""],
              mc="Payments is one of the four businesses ROAR30 says Maybank will lead in.",
              src=[["Asian Banker: ROAR30, Jan 2026", ROAR]]),
            P("tech", "Technology, data & AI", "RM10 billion over five years for AI, cloud and core banking modernisation (RM1.5 billion in FY26), and a next-generation regional app to grow out of MAE.",
              s=["corp"], st="new", neo=[0, ""], src=[["Asian Banker: ROAR30, Jan 2026", ROAR], ["Asian Banker: 2Q FY26 results, Aug 2026", Q2]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Malaysia's largest card book on Visa, Mastercard and Amex, Islamic cards, Visa and Mastercard debit on top of MyDebit, DuitNow QR in the MAE app, merchant acquiring, RM465 billion of cross-border flows in half a year, and tokenised wallets.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "Three networks, the largest issuer.", "div": "my", "rev": "cfs", "products": [
            P("ccvisa", "Visa cards: Petronas, Shopee & football", "The biggest co-brands sit on Visa: Petronas Maybank Visa Gold and Platinum, Maybank Shopee Visa Platinum, Manchester United Visa and Visa Infinite, FC Barcelona Visa Signature, plus Maybank Visa Signature and Visa Infinite.",
              s=["con", "aff"], lc="borrow", o="P", at="Visa, Petronas, Shopee", neo=[0, "Visa."],
              src=[["RinggitPlus: Maybank credit cards", CARDS], ["Business Today: FC Barcelona to 2027", FCB]]),
            P("ccmc", "Mastercard cards: World Elite & Cash Back", "Maybank World Elite Mastercard (RM800 fee; Malaysia Airlines business-class two-for-one at RM150,000 a year and 25% off Agoda from January 2026) and Maybank Cash Back Mastercard Platinum.", short="World Elite & Cash Back (Mastercard)",
              s=["con", "aff"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard holds Maybank's top premium card in Malaysia.",
              src=[["RinggitPlus: Maybank credit cards", CARDS], ["RinggitPlus: World Elite perks 2026, Dec 2025", WEMC]]),
            P("grab", "Maybank Grab Mastercard Platinum", "Launched in August 2020 with Grab and Mastercard, with same-day digital issuance; discontinued on 7 September 2026 after the Grab partnership ended.", short="Grab card (Mastercard, ended)",
              s=["con"], lc="borrow", st="retired", ay="Aug 2020", o="P", at="Grab, Mastercard", neo=[2, "Mastercard; ended Sep 2026."],
              src=[["Marketing-Interactive: Grab card launch, Aug 2020", GRAB20], ["RinggitPlus: Grab card ends, Aug 2026", GRABEND]]),
            P("grabnext", "Grab replacement cashback card", "Grab cardholders moved automatically to a no-fee cashback card from 12 September 2026 (8% in three categories above RM1,500 a month), keeping the same 16-digit card number ⚠ network not stated.",
              s=["con"], lc="borrow", st="flux", ay="Sep 2026", neo=[None, "Number kept, so likely still Mastercard ⚠."],
              mc="A Mastercard base without a co-brand partner: one to keep.",
              src=[["RinggitPlus: Grab card ends, Aug 2026", GRABEND]]),
            P("ccamex", "American Express & Maybank 2 Cards", "Maybank is Amex's issuer in Malaysia since 2006: Maybank 2 Cards pair an Amex with a Visa or Mastercard under one application, alongside Amex Platinum, Amex Cash Back Gold and Singapore Airlines KrisFlyer Amex cards. Credit-card share was over 20% in 2018 ⚠ dated.",
              s=["con", "aff"], lc="borrow", o="A", at="American Express", neo=[1, "Amex, paired with Visa or Mastercard."],
              src=[["RinggitPlus: Maybank credit cards", CARDS], ["Malaysiakini: Amex deal, 2006", AMEX06], ["Malay Mail: card share, May 2018", SHARE18]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Islamic cards", "blurb": "Ikhwan range and the new Nadi.", "div": "islamic", "rev": "cfs", "products": [
            P("ikhwan", "Ikhwan Card-i range", "Shariah-compliant cards on all three networks: World Elite Mastercard Ikhwan (upgraded from World Mastercard in October 2024), Ikhwan Mastercard Gold and Platinum, myimpact Ikhwan Mastercard, Petronas Ikhwan Visa, Ikhwan Visa Infinite and Ikhwan Amex Platinum.",
              s=["isl"], lc="borrow", o="P", at="Mastercard, Visa, American Express", neo=[1, "Mostly Mastercard; Visa and Amex too."],
              src=[["RinggitPlus: Maybank credit cards", CARDS], ["RinggitPlus: World Elite perks 2026, Dec 2025", WEMC]]),
            P("nadi", "Nadi Mastercard Credit Card-i", "Launched by Maybank Islamic in July 2026 ⚠: no annual fee, non-compounding charges and a fixed 14% profit rate, aimed at first-time cardholders ⚠.", short="Nadi (Mastercard)",
              s=["isl"], lc="borrow", st="new", ay="Jul 2026", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="A new inclusion card on Mastercard from a global top-five Islamic bank.",
              src=[["Berita Harian: Nadi card, Jul 2026", NADI], ["RinggitPlus: Maybank credit cards", CARDS]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Debit & MyDebit", "blurb": "Visa and Mastercard over MyDebit.", "div": "my", "rev": "cfs", "products": [
            P("debit", "Visa & Mastercard debit", "Maybank Visa Debit, Visa Platinum Debit and Mastercard Platinum Debit, each also working as MyDebit at home; terms define a debit transaction as \"MyDebit, Visa or MasterCard\". Split by volume not public ⚠; the MAE card is Visa ⚠.",
              s=["con"], lc="everyday", o="P", at="Visa, Mastercard, PayNet", neo=[1, "Visa and Mastercard."],
              src=[["Maybank: Visa Debit", DEBIT], ["Bank Negara: e-payments 2025", BNM]]),
            P("mydebit", "MyDebit Kawanku", "A MyDebit-only card for ATM and in-store payments within Malaysia, for customers who do not need a scheme card.",
              s=["con"], lc="everyday", o="P", at="PayNet", neo=[0, "MyDebit (PayNet)."],
              src=[["RinggitPlus: MyDebit Kawanku", KAWANKU]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "DuitNow & QR", "blurb": "Scan & Pay in MAE.", "div": "my", "rev": "cfs", "products": [
            P("maeqr", "MAE Scan & Pay", "QR payments straight from the account on DuitNow QR (formerly Maybank QRPay), now also inside Samsung Wallet (July 2026). Malaysia's DuitNow QR doubled to 3 billion transactions in 2025.",
              s=["con"], lc="everyday", st="new", o="P", at="PayNet, Samsung", neo=[0, "DuitNow QR."],
              mc="The fastest-growing way Maybank customers pay does not use a card.",
              src=[["Maybank: QRPay moves to MAE", QRPAY], ["RinggitPlus: Samsung Wallet QR, Jul 2026", SAMSUNG], ["Bank Negara: e-payments 2025", BNM]]),
            P("duitnow", "DuitNow transfers & FPX", "Real-time account-to-account transfers on PayNet's rails, which handled 8.44 billion transactions in 2025.",
              s=["con", "sme"], lc="move", o="P", at="PayNet", neo=[0, "PayNet."],
              src=[["PayNet: 2025 volumes, Apr 2026", PAYNET]]),
            P("xqr", "Cross-border QR", "MAE QR payments at merchants in Singapore, Thailand, Indonesia, Cambodia and China ⚠ date; Malaysia's cross-border QR volume rose 2.5 times to 29.7 million in 2025.",
              s=["con"], lc="move", o="P", at="PayNet", neo=[0, "QR links."],
              src=[["The Sun: QR to China", CHINA], ["PayNet: 2025 volumes, Apr 2026", PAYNET]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acquiring", "blurb": "40% of merchants (2018).", "div": "my", "rev": "cfs", "products": [
            P("acquiring", "Card acquiring", "Maybank said it had about 40% of card-accepting merchants in Malaysia in 2018 ⚠ dated, self-reported; terminals take Visa, Mastercard, Amex and MyDebit ⚠.",
              s=["sme"], lc="move", neo=[1, "Accepts every network."],
              mc="Merchant risk and Tap on Phone tools could fit Malaysia's largest acquiring base ⚠.",
              src=[["Malay Mail: card share, May 2018", SHARE18]]),
            P("qrpaybiz", "Maybank QRPayBiz", "A merchant app to take DuitNow QR payments without a terminal, with a soundbox that announces each payment; more than 700,000 QRPay merchants ⚠ date.",
              s=["sme"], lc="move", o="B", neo=[0, "DuitNow QR."],
              src=[["App Store: Maybank QRPayBiz", QRBIZ], ["The Sun: QR to China", CHINA]]),
        ]},
        {"id": "2.6", "ic": "earth", "name": "Cross-border payments", "blurb": "RM465bn in a half.", "div": "group", "rev": "gb", "products": [
            P("xborder", "Regional transactions & payments", "Cross-border payments volume of RM465.2 billion in 1H FY26, up 15.8%; ROAR30 plans a single regional platform for money movement and a payments-provider partnership for cross-border trade (provider not named ⚠).",
              s=["corp", "sme"], lc="move", st="new", neo=[None, "No public network role."],
              mc="Mastercard Move could serve remittances (RM31.6 billion of e-remittances in Malaysia in 2025).",
              src=[["Asian Banker: 2Q FY26 results, Aug 2026", Q2], ["Asian Banker: ROAR30, Jan 2026", ROAR], ["Bank Negara: e-payments 2025", BNM]]),
        ]},
        {"id": "2.7", "ic": "key-round", "name": "Wallets & tokens", "blurb": "Apple Pay, Samsung Wallet.", "div": "my", "rev": "cfs", "products": [
            P("applepay", "Apple Pay & phone wallets", "Maybank Visa and Mastercard cards in Apple Pay, with Amex following ⚠ date; tokens run on each network's service ⚠.",
              s=["con"], lc="everyday", o="P", at="Apple", neo=[1, "Visa and Mastercard tokens ⚠."],
              src=[["RinggitPlus: Maybank Apple Pay", APPLEPAY]]),
            P("samsungqr", "Samsung Wallet QR", "MAE Scan & Pay inside Samsung Wallet from July 2026, with a RM500,000 reward pool to 30 October 2026.",
              s=["con"], lc="everyday", st="new", ay="Jul 2026", o="P", at="Samsung", neo=[0, "DuitNow QR."],
              src=[["RinggitPlus: Samsung Wallet QR, Jul 2026", SAMSUNG]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: Maybank's own and PayNet's scam defences, RM10 billion for AI and data with banking-as-a-service in Indonesia, and TREATS Points, World Elite perks and football sponsorships.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & scams", "blurb": "PayNet's fraud portal.", "div": "my", "rev": "cfs", "products": [
            P("fraud", "Fraud & scam defences", "Maybank's own controls in MAE and Maybank2u ⚠ detail, inside a national effort: PayNet's fraud portal traced about 57,700 victim accounts in 2025 and is returning about RM46 million. No public Mastercard fraud tool ⚠.",
              s=["con"], lc="everyday", neo=[0, "Maybank's and PayNet's own."],
              mc="Scam scores and identity checks could fit Malaysia's anti-scam push.",
              src=[["PayNet: 2025 volumes, Apr 2026", PAYNET]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "AI, data & APIs", "blurb": "RM10bn to 2030.", "div": "group", "rev": "ho", "products": [
            P("ai", "AI & data", "AI and machine learning across the bank under ROAR30, behavioural segmentation for wealth clients, and regional AI in the app that will follow MAE.",
              s=["aff"], lc="grow", st="new", neo=[0, ""],
              mc="An AI-led app is where Agent Pay could sit.",
              src=[["Asian Banker: ROAR30, Jan 2026", ROAR]]),
            P("ibaas", "Islamic banking-as-a-service & APIs", "iBaaS to win individual and small-business customers in Indonesia through partners, and API services listed by Maybank Indonesia.",
              s=["isl", "reg"], lc="open", st="new", o="P", neo=[0, ""],
              src=[["Asian Banker: ROAR30, Jan 2026", ROAR], ["Maybank Indonesia: home", IDHOME]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & perks", "blurb": "TREATS Points, World Elite.", "div": "my", "rev": "cfs", "products": [
            P("treats", "TREATS Points", "Points across Maybank's cards in Malaysia, Singapore and Indonesia, convertible to KrisFlyer, Asia Miles, Enrich and AirAsia.",
              s=["con", "aff"], lc="grow", neo=[1, "Earned on all three networks."],
              src=[["MileLion: XL cards, Jul 2025", XL], ["RinggitPlus: Maybank credit cards", CARDS]]),
            P("wemc", "World Elite privileges", "From January 2026: Malaysia Airlines two-for-one business class at RM150,000 a year, 25% off Agoda hotels, and an annual-fee waiver at RM120,000 spend.",
              s=["aff"], lc="grow", st="new", ay="Jan 2026", o="P", at="Mastercard, Malaysia Airlines, Agoda", neo=[2, "World Elite Mastercard."],
              mc="Priceless experiences fit ROAR30's wealth push.",
              src=[["RinggitPlus: World Elite perks 2026, Dec 2025", WEMC]]),
            P("sports", "Football partnerships", "Manchester United and FC Barcelona (to 2027) partnerships, with their co-brand cards on Visa.",
              s=["con"], lc="beyond", o="P", at="Visa", neo=[0, "Visa."],
              src=[["Business Today: FC Barcelona to 2027", FCB], ["RinggitPlus: Maybank credit cards", CARDS]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: consumer and small-business banking, Malaysia's largest Islamic bank, wealth, Global Banking, Etiqa insurance and takaful, and the banks in Singapore and Indonesia, each with its own card mix.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Consumer & SME", "blurb": "Malaysia loans up 5.5%.", "div": "my", "rev": "cfs", "products": [
            P("consumer", "Consumer banking", "Mortgages, car and personal loans, and deposits; Malaysia consumer loans up 5.7% and Malaysia CASA ratio 44.0% (2Q FY26).",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Asian Banker: 2Q FY26 results, Aug 2026", Q2]]),
            P("sme", "SME & business banking", "SME lending up 2.7% in Malaysia (2Q FY26), with RM100 billion of SME financing targeted under ROAR30.",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["Asian Banker: 2Q FY26 results, Aug 2026", Q2], ["Asian Banker: ROAR30, Jan 2026", ROAR]]),
        ]},
        {"id": "4.2", "ic": "flag", "name": "Islamic banking", "blurb": "Global top five.", "div": "islamic", "rev": "cfs", "products": [
            P("islamicbank", "Maybank Islamic", "Malaysia's largest Islamic bank and in the global top five by assets; Islamic CIB income RM896.8 million in 1H FY26, and Islamic wealth assets RM18.22 billion at end-2025.",
              s=["isl"], lc="everyday", neo=[0, ""], src=[["Asian Banker: ROAR30, Jan 2026", ROAR], ["Asian Banker: 2Q FY26 results, Aug 2026", Q2], ["Asian Banker: FY25 results, Feb 2026", FY25]]),
        ]},
        {"id": "4.3", "ic": "gem", "name": "Wealth", "blurb": "Fees up 48%.", "div": "my", "rev": "cfs", "products": [
            P("wealth", "Premier, Privilege & Private", "Wealth fees up 48.4% in 1H FY26 after RM1.50 billion in 2025; ROAR30 aims for one ASEAN wealth brand and the top spot in Malaysia.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["Asian Banker: 2Q FY26 results, Aug 2026", Q2], ["Asian Banker: ROAR30, Jan 2026", ROAR]]),
        ]},
        {"id": "4.4", "ic": "briefcase-business", "name": "Global Banking", "blurb": "CIB fees RM1.5bn.", "div": "ib", "rev": "gb", "products": [
            P("gb", "Corporate & investment banking", "Corporate lending, markets and Maybank Investment Bank; CIB fees RM1.51 billion in 1H FY26, up 15.6%; investment-banking fees up 58.4% in the quarter.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Asian Banker: 2Q FY26 results, Aug 2026", Q2]]),
            P("txn", "Transaction banking", "Cash management and trade for corporates across ASEAN, to become one regional platform under ROAR30; corporate card network not public ⚠.",
              s=["corp"], lc="move", neo=[None, "Not public."], src=[["Asian Banker: ROAR30, Jan 2026", ROAR]]),
        ]},
        {"id": "4.5", "ic": "badge-check", "name": "Insurance & takaful", "blurb": "Etiqa, 16.6% share.", "div": "etiqa", "rev": "ins", "products": [
            P("etiqa", "Etiqa", "16.6% of Malaysian general insurance and takaful and fourth in life and family new business (2025); takaful contributions RM1.72 billion in 1H FY26, up 10.2%.",
              s=["con"], lc="grow", neo=[0, ""], src=[["Asian Banker: FY25 results, Feb 2026", FY25], ["Asian Banker: 2Q FY26 results, Aug 2026", Q2]]),
        ]},
        {"id": "4.6", "ic": "globe", "name": "Maybank Singapore", "blurb": "Mixed Visa and Mastercard.", "div": "sg", "rev": "cfs", "products": [
            P("sgbank", "Maybank Singapore", "A locally incorporated retail and SME bank plus a wholesale branch; profit before tax S$711.3 million in 2025, loans up 3.4% (2Q FY26).",
              s=["reg"], lc="everyday", neo=[0, ""], src=[["Asian Banker: FY25 results, Feb 2026", FY25], ["Asian Banker: 2Q FY26 results, Aug 2026", Q2]]),
            P("sgcards", "Singapore cards", "Mastercard: World Mastercard, Family & Friends and the XL Rewards and XL Cashback cards for under-40s (July 2025) ⚠ networks from card names and reader reports; Visa: Horizon Visa Signature, Platinum Visa and Visa Infinite.",
              s=["reg"], lc="borrow", st="new", o="P", at="Mastercard, Visa", neo=[1, "Split between Mastercard and Visa ⚠."],
              src=[["SingSaver: Maybank cards", SGCARDS], ["MileLion: XL cards, Jul 2025", XL]]),
        ]},
        {"id": "4.7", "ic": "earth", "name": "Maybank Indonesia", "blurb": "Mastercard debit, Visa credit.", "div": "id", "rev": "cfs", "products": [
            P("idbank", "PT Bank Maybank Indonesia", "The former BII, bought in 2008; profit after tax up 48.5% in 2025, loans up 4.3% and CASA ratio 63.5% (2Q FY26).",
              s=["reg"], lc="everyday", o="A", neo=[0, ""], src=[["Asian Banker: FY25 results, Feb 2026", FY25], ["Asian Banker: 2Q FY26 results, Aug 2026", Q2]]),
            P("idcards", "Indonesia credit cards", "Visa Infinite, Visa Platinum, Manchester United, BMW and MINI on Visa, alongside Mastercard Platinum, JCB, White Card and corporate cards; the 2026 Maybank Marathon is run with Visa.",
              s=["reg"], lc="borrow", o="P", at="Visa, Mastercard, JCB", neo=[1, "Mostly Visa; one Mastercard Platinum."],
              src=[["Maybank Indonesia: credit cards", IDCC], ["Investor Trust: Marathon with Visa, Jan 2026", IDRUN]]),
            P("iddebit", "Indonesia debit", "Maybank Debit Mastercard and Maybank Debit GPN, the domestic network; QRIS for QR payments.",
              s=["reg"], lc="everyday", o="P", at="Mastercard, GPN", neo=[1, "Mastercard and GPN."],
              src=[["Maybank Indonesia: ATM and debit", IDDEBIT]]),
            P("travelpass", "Mastercard Travel Pass", "Premier customers with the World Premier debit card use Mastercard's Travel Pass app for 1,330+ airport lounges and transfers.", short="Travel Pass (Mastercard)",
              s=["reg", "aff"], lc="grow", o="P", at="Mastercard", neo=[3, "Mastercard's own app."],
              src=[["Maybank Indonesia: Mastercard Travel Pass", IDTP]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the MAE app and Maybank2u for 10.7 million active digital users, M2U ID and branches across ASEAN, and partners from Samsung to Petronas.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "MAE app", "blurb": "10.7m digital users.", "div": "my", "rev": "cfs", "products": [
            P("mae", "MAE", "The everyday app for payments, QR and cards: 10.68 million active MAE and Maybank2u users (September 2025) and over 8 million on MAE ⚠ date; a regional next-generation app is planned.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Asian Banker: ROAR30, Jan 2026", ROAR], ["The Sun: QR to China", CHINA]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Online & branches", "blurb": "M2U, M2E, 2,600 branches.", "div": "group", "rev": "cfs", "products": [
            P("m2u", "Maybank2u, Maybank2E & M2U ID", "Internet banking for retail (Maybank2u) and business (Maybank2E) in Malaysia and Singapore, and the M2U ID app in Indonesia; 88.5% of sales are digital.",
              s=["con", "sme", "reg"], lc="open", neo=[0, ""], src=[["Asian Banker: ROAR30, Jan 2026", ROAR], ["Maybank Indonesia: home", IDHOME]]),
            P("branches", "Branches", "About 2,600 branches worldwide ⚠, from Malaysia's first local bank branches in 1960.",
              s=["con"], lc="open", neo=[0, ""], src=[["Wikipedia: Maybank", WIKI]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "Samsung, Petronas, Shopee.", "div": "my", "rev": "cfs", "products": [
            P("partners", "Partners", "Samsung Wallet for QR, Petronas and Shopee co-brand cards on Visa, Malaysia Airlines and Agoda for World Elite, and Grab until September 2026.",
              s=["con"], lc="beyond", o="P", at="Samsung, Petronas, Shopee", neo=[0, ""],
              src=[["RinggitPlus: Samsung Wallet QR, Jul 2026", SAMSUNG], ["RinggitPlus: Maybank credit cards", CARDS], ["RinggitPlus: Grab card ends, Aug 2026", GRABEND]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Maybank", "blurb": "One of three networks.", "products": [
        P("mcatmaybank", "Mastercard at Maybank", "Mastercard is one of three networks at Malaysia's largest card issuer. It carries the World Elite card, most of the Islamic Ikhwan range and the new Nadi card, Mastercard and Visa debit, and in Indonesia the debit card and Travel Pass. Visa holds the biggest co-brands and Amex sits in every Maybank 2 Cards pair; the Grab Mastercard ended in September 2026, and DuitNow QR in MAE carries the fastest growth.",
          s=["con"], div="group", rev="ho", mc="The relationship this map is drawn for.",
          src=[["RinggitPlus: Maybank credit cards", CARDS], ["RinggitPlus: Grab card ends, Aug 2026", GRABEND], ["Maybank Indonesia: ATM and debit", IDDEBIT]]),
    ]},
    {"id": "pillar-market", "name": "Malaysian payments", "blurb": "QR doubles, cards grow.", "products": [
        P("market", "The Malaysian market", "18.4 billion e-payments in 2025 (538 a head), DuitNow QR doubling to 3 billion, contactless 2 billion, debit-card transactions up 20.5% and credit up 10.9%; MyDebit and DuitNow are run by PayNet, and Visa was Maybank's first partner for online checkout (2015).",
          s=["con"], div="group", rev="ho",
          src=[["Bank Negara: e-payments 2025", BNM], ["PayNet: 2025 volumes, Apr 2026", PAYNET], ["Visa: Visa Checkout with Maybank", VISACHK]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
