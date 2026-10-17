"""Bank Muscat's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the audited 2025 financial statements, the March 2026
investor presentation and the H1 2026 results (August 2026). ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

AFS25 = "https://www.bankmuscat.om/en/investorrelations/AnnualReports/BM_AFS_2025_Audited_BM_Website_EN.pdf"
RES25 = "https://www.bankmuscat.om/en/investorrelations/AnnualReports/Annual_Results_2025_EN.pdf"
IP26 = "https://bankmuscat.com/en/investorrelations/FinancialPresentation/BM%20Investor%20Presentation%20Mar%202026.pdf"
H1Q = "https://quartr.com/events/bank-muscat-saog-bkmb-h1-2026_FtETXa9s"
H1G = "https://www.gurufocus.com/news/9014726/bank-muscat-saog-musbkmb-h1-2026-earnings-call-highlights-profit-up-93-amid-strategic-repositioning"
FY25MD = "https://www.muscatdaily.com/2026/01/18/bank-muscat-net-profit-rises-13-to-ro255mn-in-2025/"
MGMT = "https://www.bankmuscat.com/en/about/pages/management.aspx"
BOD = "https://www.bankmuscat.com/en/about/pages/bod.aspx"
INTL = "https://www.bankmuscat.com/en/about/pages/intloperations.aspx"
HOME = "https://www.bankmuscat.com/en/"
LULU = "https://www.bankmuscat.com/en/bm-cards/Pages/Bank-Muscat-Lulu-Titanium-Mastercard-Credit-Card.aspx"
LULU15 = "https://www.electronicpaymentsinternational.com/news/bank-muscat-teams-up-with-lulu-to-launch-new-co-branded-card-in-oman-160315-4532404/"
LULUAWD = "https://timesofoman.com/article/140844-bank-muscat-lulu-titanium-mastercard-credit-card-gains-esteemed-recognition"
VISA21 = "https://blackandwhiteoman.com/bank-muscat-and-visa-renew-partnership/"
OMANAIR = "https://www.bankmuscat.com/en/bm-cards/Pages/Oman-Air-Visa-Credit-Card.aspx"
CASHBACK = "https://blackandwhiteoman.com/bank-muscat-visa-credit-cards-5-percent-cashback-offer/"
SHUKRAN = "https://timesofoman.com/article/138920-bank-muscat-launches-shukran-co-branded-visa-prepaid-card-in-collaboration-with-landmark-group-and-visa"
FLOOSI = "https://www.bankmuscat.com/en/bm-cards/Pages/Floosi-Visa-Classic.aspx"
CORP = "https://www.bankmuscat.com/en/Business/Everydaybanking/Pages/Visa_Corporate_Cards.aspx"
MAAL = "https://www.bankmuscat.com/en/bm-cards/Pages/maal.aspx"
MAALCBO = "https://www.muscatdaily.com/2025/09/15/central-bank-of-oman-launches-national-payment-card-maal/"
MPCSS = "https://www.omanobserver.om/article/1196181/business/instant-payments-widen-value-lead-over-omannet"
INSTANT = "https://www.omanobserver.om/article/1196476/business/banking/instant-credit-cards-with-bank-muscat-mobile-banking"
APPLEPAY = "https://www.bankmuscat.com/en/bm-cards/Pages/ApplePay.aspx"
APPLEOM = "https://meatechwatch.com/2024/09/25/apple-pay-launches-in-oman-enhancing-digital-payment-options/"
EPP = "https://www.bankmuscat.com/en/bm-cards/Pages/epp.aspx"
REWARDS = "https://www.bankmuscat.com/en/Pages/Rewards.aspx"
HISABY = "https://www.bankmuscat.com/en/accounts/Pages/Hisaby.aspx"
AWARDS = "https://www.bankmuscat.com/en/about/pages/ratingawards.aspx"
MEETHAQ = "https://www.meethaq.om/"
DIGI = "https://www.zawya.com/en/economy/gcc/bank-muscat-leverages-innovation-to-enhance-customer-experience-and-drive-digital-excellence-rtgzmg1i"
TAPNGO = "https://ibsintelligence.com/?p=569184"
SOHARSEND = "https://www.gccbusinessnews.com/tag/mastercard-send-platform/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · ownership · licences", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: about a third of Oman's banking assets, RO 255.5 million of profit in 2025, the Royal Court as largest shareholder, investment-grade ratings regained, and a strategy that will not chase share at the cost of credit quality.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "RO 15.1bn assets, ROE 13.6%.", "div": "bm", "rev": "corporate", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of RO 15.13 billion, net loans of RO 10.73 billion and deposits of RO 10.43 billion at end-2025; net profit RO 255.5 million in 2025 (up 13.3%) and RO 137.5 million in H1 2026 (up 9.3%); ROE 13.6% and cost:income 38.0% in 2025; total capital ratio 19.66%.",
              s=["corp"], neo=[0, ""], src=[["Audited 2025 financial statements", AFS25], ["2025 results", RES25], ["H1 2026 results summary", H1Q]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "Royal Court 27%; Al Hashar CEO.", "div": "bm", "rev": "corporate", "products": [
            P("owners", "Ownership, ratings & listing", "Listed on the Muscat Stock Exchange since 1993, and in London and Bahrain; the Royal Court Affairs holds 27.31% and Omani pension funds are long-term holders; market value about RO 3.65 billion in March 2026 ⚠; rated Baa3 by Moody's, BBB- by S&P and Fitch; a domestic systemically important bank.",
              s=["corp"], neo=[0, ""], src=[["Investor presentation, Mar 2026", IP26]]),
            P("leadership", "Board & management", "Chairman Sheikh Khalid bin Mustahail Al Mashani (since 2011); CEO Sheikh Waleed Khamis Al Hashar; deputy CEOs Ahmed Al Bulushi (Banking), Sheikha Yousuf Al Farsi (Operations) and T. Ganesh (Finance and Investment Banking); Abdulnasir Al Raisi runs Personal Banking and Abdullah Al Maashani Products.",
              s=["corp"], neo=[0, ""], src=[["Bank Muscat: management", MGMT], ["Bank Muscat: board", BOD]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & licences", "blurb": "Since 1982; Meethaq since 2013.", "div": "bm", "rev": "corporate", "products": [
            P("heritage", "Heritage & licences", "Founded in 1982 and built by mergers with Commercial Bank of Oman and Bank Al Ahli Al Omani; licensed by the Central Bank of Oman, with a separate Islamic banking licence for Meethaq from January 2013; 4,462 employees at end-2025.",
              s=["con"], o="I", neo=[0, ""], src=[["Investor presentation, Mar 2026", IP26], ["Audited 2025 financial statements", AFS25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology", "blurb": "200+ app features, RPA.", "div": "bm", "rev": "personal", "products": [
            P("tech", "Digital platform & automation", "A mobile platform with more than 200 features, tokenised cards, QR and soft POS; AI and robotic process automation used inside the bank, with generative AI and predictive analytics being explored ⚠ undated report.",
              s=["con", "sme"], neo=[0, ""], src=[["Zawya: Bank Muscat digital excellence ⚠", DIGI], ["Bank Muscat: awards", AWARDS]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy", "blurb": "Disciplined growth, Islamic spin-off.", "div": "bm", "rev": "corporate", "products": [
            P("strategy", "Strategy & 2026 guidance", "Customer centricity, efficiency, innovation and market leadership; loan growth of about 6–7% guided for 2026 with fee income about 30% of income; the bank says it will not cut credit quality or pricing to chase share.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 call highlights", H1G], ["Investor presentation, Mar 2026", IP26]]),
            P("spinoff", "Islamic window spin-off", "The Central Bank of Oman requires Islamic windows to be separated; Bank Muscat expects banks to merge, buy or close windows and calls the timelines workable ⚠ no CBO document seen.",
              s=["isl"], st="flux", neo=[0, ""], src=[["H1 2026 call highlights", H1G]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Visa debit and prepaid for about 4 million customers, the new Maal national card, a Visa credit range with one LuLu Mastercard, instant digital cards and wallets, Oman's largest merchant-acquiring book, transfers over the central bank's instant rails, and Visa corporate cards.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit & prepaid", "blurb": "Visa throughout.", "div": "bm", "rev": "personal", "products": [
            P("debit", "Visa debit cards", "Visa Classic debit for every account, with Al Jawhar, Asalah Visa Platinum, Private Banking Visa Platinum, Shababi (youth) and Zeinah (women) variants; contactless and in Apple Pay and Samsung Pay.", short="Debit (Visa)",
              s=["con", "prem", "expat"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Bank Muscat: cards menu", HOME]]),
            P("floosi", "Floosi Visa debit for children", "A personalised Visa Classic debit card for 7–17-year-olds, Omani or expatriate, with daily limits of OMR 50 and monthly limits of OMR 200.",
              s=["con"], lc="open", o="P", at="Visa", neo=[0, "Visa."], src=[["Bank Muscat: Floosi", FLOOSI]]),
            P("prepaid", "Visa prepaid & Shukran", "A reloadable Visa prepaid card and the Shukran co-branded Visa prepaid card with Landmark Group (November 2023), earning Shukran points at Landmark stores, with balances up to OMR 2,000.", short="Prepaid (Visa)",
              s=["con", "expat"], lc="everyday", ay="Nov 2023", o="P", at="Visa, Landmark Group", neo=[0, "Visa."], src=[["Times of Oman: Shukran Visa prepaid, Nov 2023", SHUKRAN]]),
        ]},
        {"id": "2.2", "ic": "flag", "name": "Maal national card", "blurb": "Oman's own scheme.", "div": "bm", "rev": "personal", "products": [
            P("maal", "Maal national debit card", "The Central Bank of Oman's national card, announced September 2025, issued free to all Bank Muscat customers as an extra card for domestic ATMs, POS (rolling out), local e-commerce and government payments over OmanNet; it cannot be used abroad and is not yet in mobile wallets.", short="Maal (domestic)",
              s=["con", "expat"], lc="everyday", st="new", ay="Sep 2025", o="P", at="Central Bank of Oman, OmanNet", neo=[0, "Domestic scheme."],
              mc="Takes domestic volume from every international network; cross-border spend still needs one.",
              src=[["Bank Muscat: Maal", MAAL], ["Muscat Daily: CBO launches Maal, Sep 2025", MAALCBO]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Credit cards", "blurb": "Visa, plus one LuLu Mastercard.", "div": "bm", "rev": "personal", "products": [
            P("visacredit", "Visa credit range", "Visa Classic, Gold, Al Jawhar Platinum, Asalah Signature and Private Banking Infinite credit cards; a 5% international cashback offer ran on Visa credit cards in July–August 2026.", short="Credit (Visa)",
              s=["con", "prem"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Bank Muscat: cards menu", HOME], ["Black & White Oman: Visa cashback, 2026", CASHBACK]]),
            P("omanair", "Oman Air Visa Platinum", "A co-branded credit card with the national airline earning Oman Air miles, for customers earning at least OMR 500 a month.",
              s=["prem"], lc="borrow", o="P", at="Visa, Oman Air", neo=[0, "Visa."], src=[["Bank Muscat: Oman Air Visa", OMANAIR]]),
            P("lulu", "LuLu Titanium Mastercard", "Co-branded with LuLu Hypermarket since March 2015: 2% back at LuLu and 0.5% elsewhere, Mastercard Flight Delay lounge access through Travel Pass; Mastercard named it Oman's largest co-branded credit card in January 2024.", short="LuLu (Mastercard)",
              s=["con", "expat"], lc="borrow", ay="Mar 2015", o="P", at="Mastercard, LuLu", neo=[2, "Issued on Mastercard."],
              mc="The bank's only Mastercard card, and Oman's only exclusive Mastercard co-brand credit card.",
              src=[["Bank Muscat: LuLu Mastercard", LULU], ["EPI: LuLu card launch, Mar 2015", LULU15], ["Times of Oman: Mastercard award, Jan 2024", LULUAWD]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Digital cards & wallets", "blurb": "Instant cards in the app.", "div": "bm", "rev": "personal", "products": [
            P("instantcard", "Instant digital debit & credit cards", "Oman's first fully digital credit-card issuance in the app (September 2026), after an instant digital debit card: approved cards are issued at once, usable online, and added to Apple Pay and Samsung Pay; international use can be switched on and off.",
              s=["con", "prem"], lc="open", st="new", ay="Sep 2026", neo=[1, "Mostly Visa; the LuLu card is Mastercard."],
              mc="Instant issuance needs tokens and Click to Pay on whichever network issues.",
              src=[["Oman Observer: instant credit cards, Sep 2026", INSTANT]]),
            P("wallets", "Apple Pay & Samsung Pay", "Bank Muscat cards in Apple Pay, live in Oman since September 2024 ⚠, and Samsung Pay.",
              s=["con"], lc="everyday", ay="Sep 2024", o="P", at="Apple, Samsung", neo=[1, "Visa tokens and the LuLu Mastercard."], src=[["Bank Muscat: Apple Pay", APPLEPAY], ["MEA Tech Watch: Apple Pay in Oman, Sep 2024", APPLEOM]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Merchant acquiring", "blurb": "46% of Oman's volume.", "div": "bm", "rev": "personal", "products": [
            P("acquiring", "Merchant acquiring & e-commerce", "More than 46% of Oman's merchant-acquiring volume (March 2026) and the leading e-commerce gateway; more than 24,000 POS devices and 61 million POS transactions in 2021; merchant onboarding went digital in H1 2026.",
              s=["sme", "corp"], lc="move", o="B", neo=[1, "Accepts Mastercard, Visa and OmanNet."],
              mc="Oman's biggest acceptance book: acquirer risk, tokenised checkout and merchant data.",
              src=[["Investor presentation, Mar 2026", IP26], ["Black & White Oman: Visa renewal, Nov 2021", VISA21], ["H1 2026 results summary", H1Q]]),
            P("tapngo", "Tap'N'Go soft POS", "Turns an Android phone into a card terminal for any NFC card, without extra hardware; expanded in July 2025 ⚠.",
              s=["sme"], lc="move", ay="Jul 2025", neo=[1, "Accepts all NFC cards ⚠."], src=[["IBSi: Tap'N'Go ⚠", TAPNGO]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Transfers & instant payments", "blurb": "MPCSS passes OmanNet.", "div": "bm", "rev": "personal", "products": [
            P("mpcss", "Instant payments: MPCSS & OmanNet", "Bank Muscat customers pay over the central bank's rails: MPCSS (live since 2017) carried 224.2 million payments worth RO 8.2 billion in H1 2026, up 72% by value and now ahead of OmanNet's RO 4.7 billion; local digital transfers became free for individuals and SMEs on 1 July 2026 ⚠ bank's own participation inferred.",
              s=["con", "sme"], lc="move", o="P", at="Central Bank of Oman", neo=[0, "Central bank rails."],
              mc="Account-to-account payments are growing fastest; scam risk grows with them.",
              src=[["Oman Observer: instant payments, Sep 2026", MPCSS]]),
            P("remit", "Remittances & international transfers", "SWIFT and IBAN transfers for about 4 million customers, many of them expatriates; the bank calls itself market leader in remittances. No card-rail transfer product found.",
              s=["expat", "con"], lc="move", neo=[None, "No Mastercard Move or Visa Direct product found."],
              mc="Sohar International already sends abroad with Mastercard Send ⚠.",
              src=[["Investor presentation, Mar 2026", IP26], ["GCC Business News: Mastercard Send in Oman ⚠", SOHARSEND]]),
        ]},
        {"id": "2.7", "ic": "briefcase-business", "name": "Commercial cards", "blurb": "Visa Commercial Pay.", "div": "bm", "rev": "corporate", "products": [
            P("corpcard", "Visa corporate & virtual cards", "Visa corporate credit cards, with virtual cards for paying suppliers at home and abroad powered by Visa Commercial Pay.", short="Corporate cards (Visa)",
              s=["corp", "sme"], lc="move", o="P", at="Visa", neo=[0, "Visa."], src=[["Bank Muscat: Visa corporate cards", CORP]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: OTP and in-app card controls, Bank Muscat Rewards and co-brand points, 0% instalments, internal AI and automation, and no public open-banking offer yet.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "OTPs and card controls.", "div": "bm", "rev": "personal", "products": [
            P("security", "Card security & controls", "One-time passcodes for online card payments, e-PIN, in-app blocking and switching international use on and off; a 2025 award for cybersecurity. No fraud-scoring vendor is named.",
              s=["con", "sme"], lc="everyday", neo=[None, "No vendor named."],
              mc="Fast-growing instant payments and app-only issuance call for scam and identity scoring.",
              src=[["Oman Observer: instant credit cards, Sep 2026", INSTANT], ["Bank Muscat: awards", AWARDS]]),
        ]},
        {"id": "3.2", "ic": "gift", "name": "Rewards & instalments", "blurb": "BM Rewards, 0% EPP.", "div": "bm", "rev": "personal", "products": [
            P("rewards", "Bank Muscat Rewards", "A points programme for all customers, earned on credit-card spend, salary transfers and digital banking and spent on flights, hotels, shopping and e-vouchers; points last 24 months.",
              s=["con", "prem"], lc="grow", o="B", neo=[0, "The bank's own programme."],
              mc="Card-linked offers could feed the programme.",
              src=[["Bank Muscat: Rewards", REWARDS]]),
            P("epp", "Easy Payment Plan", "0% instalments over 12 months on credit-card purchases at partner merchants across Oman, for all personal credit cardholders.",
              s=["con"], lc="borrow", o="B", neo=[1, "On every credit card, the LuLu Mastercard included."], src=[["Bank Muscat: Easy Payment Plan", EPP]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "Data & AI", "blurb": "Automation inside.", "div": "bm", "rev": "corporate", "products": [
            P("ai", "AI & automation", "AI and robotic process automation in several functions; generative AI, predictive analytics and omnichannel service being explored ⚠ undated report. No customer-facing AI assistant found.",
              s=["corp"], lc="everyday", neo=[0, ""], src=[["Zawya: Bank Muscat digital excellence ⚠", DIGI]]),
        ]},
        {"id": "3.4", "ic": "code-xml", "name": "Open banking", "blurb": "Nothing public yet.", "div": "bm", "rev": "corporate", "products": [
            P("openbanking", "Open banking & APIs", "No Bank Muscat open-banking or API product was found, and the status of an Omani open-banking framework could not be confirmed ⚠.",
              s=["sme", "corp"], lc="open", st="unconf", neo=[None, "Nothing public."], src=[["Investor presentation, Mar 2026", IP26]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: personal banking for about 4 million people, premier and private banking, corporate and SME banking, treasury and Oman's largest fund manager, Meethaq Islamic banking and a Saudi branch.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Personal banking", "blurb": "About 4 million customers.", "div": "bm", "rev": "personal", "products": [
            P("personal", "Personal Banking", "About 4 million retail customers, personal loans (21.8% of loans) and housing loans (17.4%), cards, bancassurance and remittances; RO 80.8 million of profit in 2025.",
              s=["con", "expat"], lc="everyday", neo=[0, "Visa debit."], src=[["Investor presentation, Mar 2026", IP26], ["Audited 2025 financial statements", AFS25]]),
        ]},
        {"id": "4.2", "ic": "gem", "name": "Premier & private", "blurb": "Al Jawhar, Asalah, Private.", "div": "premier", "rev": "personal", "products": [
            P("premier", "Al Jawhar, Asalah & Private Banking", "Three premier tiers with their own Visa Platinum, Signature and Infinite cards; named Best Private Bank in Oman by The Banker/PWM and MEED in 2025.",
              s=["prem"], lc="grow", neo=[0, "Visa premium cards."],
              mc="Premium credit is Visa's; World and World Elite are untried here.",
              src=[["Bank Muscat: cards menu", HOME], ["Bank Muscat: awards", AWARDS]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate & SME", "blurb": "Lead bank to Omani corporates.", "div": "bm", "rev": "corporate", "products": [
            P("corporate", "Corporate Banking", "Lead bank to top-tier Omani corporates, with project finance, trade finance and cash management; RO 78.5 million of profit and RO 4.9 billion of assets in 2025.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Audited 2025 financial statements", AFS25], ["Investor presentation, Mar 2026", IP26]]),
            P("sme", "SME banking", "Accounts, loans and acceptance for small businesses; Best SME Bank in Oman (MEED, 2025).",
              s=["sme"], lc="everyday", neo=[0, ""], src=[["Bank Muscat: awards", AWARDS]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Wholesale & asset management", "blurb": "Oman's largest fund manager.", "div": "bm", "rev": "wholesale", "products": [
            P("wholesale", "Wholesale Banking", "Treasury, financial institutions, corporate finance and Oman's largest mutual-fund manager; RO 58.4 million of profit in 2025.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["Audited 2025 financial statements", AFS25], ["Investor presentation, Mar 2026", IP26]]),
        ]},
        {"id": "4.5", "ic": "landmark", "name": "Meethaq Islamic banking", "blurb": "32 branches, RO 2.1bn.", "div": "meethaq", "rev": "islamic", "products": [
            P("meethaq", "Meethaq Islamic Banking", "Oman's largest Islamic window by market share, launched January 2013, with 32 branches, RO 2.09 billion of assets and RO 11.8 million of profit in 2025.",
              s=["isl"], lc="everyday", neo=[0, ""], src=[["Audited 2025 financial statements", AFS25], ["H1 2026 call highlights", H1G]]),
            P("meethaqcards", "Meethaq Visa cards", "Hafawa Visa Signature, Visa Platinum and Gold credit cards on Qard Hassan and Ujra terms, and Neswa and standard Visa debit cards.", short="Meethaq cards (Visa)",
              s=["isl"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Meethaq website", MEETHAQ], ["Audited 2025 financial statements", AFS25]]),
        ]},
        {"id": "4.6", "ic": "earth", "name": "International", "blurb": "A Saudi branch; Kuwait closed.", "div": "intl", "rev": "intl", "products": [
            P("intl", "Saudi branch & representative offices", "A commercial branch in Saudi Arabia since April 2007 for corporate, trade and treasury business; representative offices in Dubai, Singapore and Iran; the Kuwait branch closed in 2025; about 7% of profit.",
              s=["corp"], lc="beyond", st="flux", neo=[0, ""], src=[["Bank Muscat: international operations", INTL], ["Audited 2025 financial statements", AFS25], ["H1 2026 call highlights", H1G]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: an award-winning app where cards can be opened without a branch, Oman's largest branch network with Hisaby centres for expatriate workers, and co-brand partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Mobile & internet banking", "blurb": "Cards opened in the app.", "div": "bm", "rev": "personal", "products": [
            P("app", "Mobile Banking app & internet banking", "More than 200 features, app-only card and loan applications, and rewards inside the app; Best Consumer Digital Bank in Oman (Global Finance, 2025).",
              s=["con", "prem", "sme"], lc="everyday", neo=[0, ""], src=[["Bank Muscat: awards", AWARDS], ["Oman Observer: instant credit cards, Sep 2026", INSTANT]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & Hisaby", "blurb": "200 sites; expat centres.", "div": "hisaby", "rev": "personal", "products": [
            P("branches", "Branch network", "200 branches and service centres across Oman in March 2026, the largest network in the country.",
              s=["con", "isl"], lc="everyday", neo=[0, ""], src=[["Investor presentation, Mar 2026", IP26]]),
            P("hisaby", "Hisaby centres", "Basic banking and transfer centres for expatriate workers, open evenings and Fridays at some sites.",
              s=["expat"], lc="open", neo=[0, ""],
              mc="Expatriate wage and remittance flows meet here.",
              src=[["Bank Muscat: Hisaby", HISABY]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Co-brand partners", "blurb": "LuLu, Landmark, Oman Air.", "div": "bm", "rev": "personal", "products": [
            P("partners", "Co-brand partners", "LuLu Hypermarket (Mastercard credit), Landmark Group's Shukran (Visa prepaid) and Oman Air (Visa credit) bring customers to Bank Muscat cards.",
              s=["con", "expat"], lc="grow", o="P", at="LuLu, Landmark Group, Oman Air", neo=[1, "LuLu on Mastercard; Shukran and Oman Air on Visa."],
              src=[["Bank Muscat: LuLu Mastercard", LULU], ["Times of Oman: Shukran Visa prepaid, Nov 2023", SHUKRAN], ["Bank Muscat: Oman Air Visa", OMANAIR]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Bank Muscat", "blurb": "One co-brand, and acceptance.", "products": [
        P("mcatbm", "Mastercard at Bank Muscat", "Visa carries Bank Muscat's debit, prepaid, credit, Islamic and corporate cards under a partnership renewed in November 2021. Mastercard has one card, the LuLu Titanium co-brand (2015), which it named Oman's largest co-branded credit card in 2024, and is accepted across the bank's 46% share of Omani card acquiring.",
          s=["con"], div="bm", rev="personal", mc="The relationship this map is drawn for.",
          src=[["Black & White Oman: Visa renewal, Nov 2021", VISA21], ["Times of Oman: Mastercard award, Jan 2024", LULUAWD]]),
    ]},
    {"id": "pillar-market", "name": "Omani payments", "blurb": "Maal, MPCSS, investment grade.", "products": [
        P("market", "The Omani market", "21 banks with Bank Muscat at about 32% of assets; the central bank's Maal national card (2025) and MPCSS instant payments, now larger than OmanNet by value and free for retail transfers from July 2026; Oman back at investment grade in 2025.",
          s=["con"], div="bm", rev="personal", src=[["Investor presentation, Mar 2026", IP26], ["Oman Observer: instant payments, Sep 2026", MPCSS], ["Muscat Daily: CBO launches Maal, Sep 2025", MAALCBO]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
