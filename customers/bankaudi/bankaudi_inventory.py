"""Bank Audi's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 2025 Annual Report (published 8 June 2026)
and the unaudited Q1 2026 figures released the same day. ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public. (The neo digital bank is a Bank Audi brand, written in lower case.)
"""
# ruff: noqa: E501

AR25 = "https://pwstg02.blob.core.windows.net/pwfiles/ContentFiles/16382PublicationFile.pdf"
BLOM = "https://blog.blominvestbank.com/bank-audi-publishes-its-audited-financial-results-for-2025-and-its-non-audited-financial-results-for-q1-2026/"
GROUP = "https://www.bankaudigroup.com/"
HOME = "https://www.bankaudi.com.lb/"
CARDS = "https://www.bankaudi.com.lb/personal-banking/cards"
CEDAR = "https://www.bankaudi.com.lb/personal-banking/cards/cards-listing/mea-cedar-miles-world-elite"
TOTERS = "https://www.bankaudi.com.lb/common/ip/ba-x-mc-x-toters"
MC10K = "https://www.bankaudi.com.lb/english/newsroom/press-releases/mastercard-empower-10000-lebanese-entrepreneurs"
CHAIR = "https://www.bankaudi.com.lb/english/newsroom/press-releases/new-chair-of-the-board"
DIGI = "https://www.bankaudi.com.lb/lebanon/digital-banking-solutions"
NEO = "https://www.neo.com.lb/"
NEOLAUNCH = "https://www.fintechfutures.com/digital-banking/bank-audi-launches-new-digital-bank-neo-in-lebanon-powered-by-codebase-technologies"
GPAY = "https://v7cdn.lbcgroup.tv/news/lebanon-news/863598/bank-audi-and-neo-digital-bank-introduce-google-pay-services-in-lebano/en"
VISAGPAY = "https://km.visamiddleeast.com/en_KM/about-visa/newsroom/press-releases/prl-24062025.html"
MCBDL = "https://techafricanews.com/?p=87055"
ICE = "https://www.ice.it/it/news/notizie-dal-mondo/308884"
LBCI24 = "https://lbcgroup.tv/news/economy/767035/bdl-initiates-measures-to-promote-electronic-payments-and-reduce-cash/en"
BDL980 = "https://bdl.gov.lb/CB%20Com/Laws%20And%20Regulations/Announcements/980_04-06-2026_Ar%C2%A711794_1.pdf"
BDL976 = "https://bdl.gov.lb/CB%20Com/Laws%20And%20Regulations/Announcements/976_18-02-2026_Ar%C2%A711532_1.pdf"
ABLCEDAR = "https://www.abl.org.lb/english/abl-and-banking-sector-news/abl-news/bank-audi-unveils-the-exclusive---the-ultimate-cedar-miles-world-elite--mastercard-credit-card-in-lebanon"
ABLMB = "https://www.abl.org.lb/english/abl-and-banking-sector-news/abl-news/bank-audi-launches-the-mercedes-benz-visa-card-in-collaboration-with-t--gargour-and-fils"
WIKI = "https://en.wikipedia.org/wiki/Bank_Audi"
ACAP = "https://www.audicapital.com/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · governance · restructuring", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $15.1 billion of assets and a return to profit in 2025, a bank founded in Sidon in 1830, a new chair in January 2026, a slimmed-down footprint after selling Egypt and Turkey, and a strategy built around Lebanon's pending bank restructuring.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & results", "blurb": "$83m profit in 2025.", "div": "group", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Assets of $15.12 billion, customer deposits of $12.89 billion, loans of $1.14 billion and equity of $1.16 billion at the end of 2025; net profit of $83 million (2024: nil), about half from Lebanon, after putting all non-fresh profit into provisions. Q1 2026: profit $19.4 million, deposits $12.62 billion.",
              s=["con"], neo=[0, ""], src=[["2025 Annual Report", AR25], ["BLOMInvest: 2025 and Q1 2026 results", BLOM]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & owners", "blurb": "Sherine Audi chairs.", "div": "group", "rev": "group", "products": [
            P("leadership", "Board & management", "Sherine R. Audi became chair on 13 January 2026 after Samir Hanna stepped down; Khalil El Debs is group CEO, Hassan Saleh deputy CEO and head of neo, Elias Abousleiman CFO.",
              s=["corp"], st="new", ay="Jan 2026", neo=[0, ""], src=[["Bank Audi: new chair, Jan 2026", CHAIR], ["2025 Annual Report", AR25]]),
            P("owners", "Shareholders & listing", "More than 1,500 holders of shares and GDRs, including the Audi family, FRH Investment Holding, Gulf and Kuwaiti families, IFC and EBRD; 588.5 million shares listed in Beirut, at $1.71 on 9 October 2026, about $1.0 billion in all ⚠ thin trading.",
              s=["corp"], neo=[0, ""], src=[["Bank Audi Group", GROUP], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "1.3", "ic": "earth", "name": "Heritage & footprint", "blurb": "Since 1830; Egypt and Turkey sold.", "div": "group", "rev": "intl", "products": [
            P("footprint", "Heritage, footprint & deals", "Founded in Sidon in 1830 and incorporated in 1962; now Lebanon, Switzerland, France, Qatar, Saudi Arabia and an Abu Dhabi office. Egypt went to First Abu Dhabi Bank (2021) and Odea Bank in Turkey to ADQ (completed March 2025); 1,612 staff and 43 branches at the end of 2025.",
              s=["corp"], o="I", st="flux", neo=[0, ""], src=[["2025 Annual Report", AR25], ["Bank Audi Group", GROUP], ["Wikipedia: Bank Audi", WIKI]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology", "blurb": "New mobile and online platform.", "div": "audi", "rev": "group", "products": [
            P("tech", "Infostructure & core systems", "In-house IT has moved workloads to the cloud, upgraded the ATM fleet and onboarding, and in 2025 chose vendors to replace internet and mobile banking; neo runs on its own stack, Codebase Technologies' Digibanc ⚠.",
              s=["corp"], o="B", neo=[0, ""], src=[["2025 Annual Report", AR25], ["FinTech Futures: neo launch", NEOLAUNCH]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & restructuring", "blurb": "Ready for the Gap law.", "div": "group", "rev": "group", "products": [
            P("strategy", "Strategy", "Readiness for sector restructuring, selective lending in fresh dollars, leadership in digital banking through neo and partnerships, international entities and cost discipline.",
              s=["corp"], neo=[0, ""], src=[["2025 Annual Report", AR25]]),
            P("resolution", "Bank restructuring & the Gap law", "Law 23/2025 set up bank restructuring; the Financial Regularisation and Deposit-Recovery draft, approved by Cabinet on 27 December 2025 and before Parliament, would repay deposits up to $100,000 in phases. War resumed in March 2026; a partial ceasefire held from 16 April.",
              s=["con", "corp"], st="flux", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Mastercard credit and the MEA Cedar Miles co-brand, Mastercard debit in fresh dollars and lira, neo's multi-currency cards, Google Pay, card acceptance for merchants, and transfers and cash over BDL's rails, wallets and agents.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "World Elite and Cedar Miles.", "div": "audi", "rev": "retail", "products": [
            P("credit", "Bank Audi credit cards", "World, World Elite (in dollars, euros and pounds) and Platinum credit cards, marketed to affluent clients as premium lifestyle products; no Visa card appears on the bank's card pages in October 2026.", short="Credit (Mastercard)",
              s=["con", "aff"], lc="borrow", o="B", neo=[2, "Mastercard."], src=[["Bank Audi: cards", CARDS], ["Bank Audi home page", HOME], ["2025 Annual Report", AR25]]),
            P("cedar", "MEA Cedar Miles World Elite", "Co-brand with Middle East Airlines: 1.5 Cedar Miles per dollar, SkyTeam redemptions, unlimited access to more than 1,300 lounges and travel cover up to $500,000; first launched as 'The Ultimate' World Elite card in late 2013 ⚠.", short="Cedar Miles (Mastercard)",
              s=["aff"], lc="everyday", o="P", at="Middle East Airlines", neo=[2, "World Elite Mastercard."],
              src=[["Bank Audi: MEA Cedar Miles World Elite", CEDAR], ["ABL: Ultimate Cedar Miles World Elite", ABLCEDAR]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Debit & currency cards", "blurb": "Fresh dollars and lira.", "div": "audi", "rev": "retail", "products": [
            P("debit", "Debit & currency cards", "Platinum Debit in fresh dollars, Debit and Platinum Debit in lira, Loubnani Platinum, and euro and sterling cards for children abroad; the catalogue is split into foreign-currency and local-currency cards. A 2015 Mercedes-Benz Visa co-brand is the only Visa card found ⚠ status.", short="Debit (Mastercard ⚠)",
              s=["con", "teen"], lc="everyday", o="B", neo=[2, "Mastercard tiers ⚠ per product."], src=[["Bank Audi: cards", CARDS], ["Bank Audi home page", HOME], ["ABL: Mercedes-Benz Visa card", ABLMB]]),
            P("fresh", "Fresh-dollar & lira card rules", "BDL Circular 150 (April 2020) keeps fresh dollars free for international card use; Circular 158 pays part of monthly deposit withdrawals onto cards; Announcement 980 (4 June 2026) made dollar cards issued locally payable in lira at POS at LBP 89,500 from 15 June 2026.",
              s=["con"], lc="everyday", st="flux", ay="Jun 2026", neo=[1, "Applies to every card; Bank Audi's are Mastercard."],
              mc="Two kinds of dollar in one wallet: the card is where fresh money gets spent.",
              src=[["2025 Annual Report", AR25], ["BDL Announcement 980, Jun 2026", BDL980]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "neo cards", "blurb": "Six currencies on one card.", "div": "neo", "rev": "retail", "products": [
            P("neocard", "neo multi-currency debit card", "A physical and digital debit card across six currencies, the first multi-currency digital account and card in Lebanon (2025), with FX savings of up to 3.3% claimed ⚠.", short="neo debit (Mastercard ⚠)",
              s=["dig", "teen"], lc="everyday", st="new", ay="2025", o="B", neo=[2, "Mastercard ⚠ inferred from Google Pay launch."],
              src=[["neo by Bank Audi", NEO], ["2025 Annual Report", AR25], ["LBCI: Google Pay, Jun 2025", GPAY]]),
            P("neocredit", "neo Cedar Miles credit card", "One Cedar Mile per dollar, SkyTeam redemptions and lounge access; 1.9% monthly interest and up to 45 days' grace.", short="neo credit (Mastercard)",
              s=["dig"], lc="borrow", o="P", at="Middle East Airlines", neo=[2, "Mastercard."], src=[["neo by Bank Audi", NEO]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Google Pay", "blurb": "First on Mastercard in Lebanon.", "div": "audi", "rev": "retail", "products": [
            P("gpay", "Google Pay", "On 24 June 2025 Bank Audi and neo added Google Pay for their Mastercard holders, in shops, online and abroad, the day Google Pay reached Lebanon; Visa launched it the same day with BLOM and BLF. Apple Pay is not live in Lebanon ⚠.",
              s=["con", "dig"], lc="everyday", st="new", ay="Jun 2025", o="P", at="Google", neo=[2, "Mastercard tokens only."],
              mc="Tokenised Mastercard credentials are already in the wallet; Click to Pay is the next step.",
              src=[["LBCI: Google Pay, Jun 2025", GPAY], ["Visa: Google Pay in Lebanon, Jun 2025", VISAGPAY], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "POS for merchants.", "div": "audi", "rev": "corporate", "products": [
            P("pos", "POS & merchant acceptance", "POS terminals for business clients, offered through neo Business ⚠ acquirer and processor not disclosed; BDL capped merchant fees at 1.25% on Visa and Mastercard cards in essential sectors in 2026, and card transactions rose about 130% in January–August 2026.",
              s=["sme"], lc="move", neo=[1, "Accepts every network."],
              mc="Acceptance is where Lebanon's cash economy is won or lost.",
              src=[["neo by Bank Audi", NEO], ["ICE Beirut: card payments, Sep 2026", ICE]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Transfers & cash", "blurb": "QR, BDL-RTGS, agents.", "div": "neo", "rev": "retail", "products": [
            P("transfers", "neo transfers & QR", "Send money by mobile number, IBAN or QR code, pay merchants by QR, split bills, and receive transfers from any bank in Lebanon or abroad.",
              s=["dig", "sme"], lc="move", o="B", neo=[0, "Bank Audi's own rails."], src=[["neo by Bank Audi", NEO]]),
            P("rtgs", "BDL-RTGS & BDL-CLEAR", "Interbank payments settle on BDL-RTGS (2012) and BDL-CLEAR; BDL reset their fees on 18 February 2026, including for fresh-money transfers and cheques. No national retail instant-payment scheme was found; instant transfers reach people through bank apps and licensed wallets ⚠.",
              s=["corp"], lc="move", st="flux", neo=[0, "BDL's rails."],
              src=[["BDL Announcement 976, Feb 2026", BDL976], ["LBCI: BDL e-payments, Apr 2024", LBCI24]]),
            P("cashout", "ATMs, agents & cross-border", "Cardless cash-out at more than 200 Bank Audi ATMs and through OMT, BOB Finance and Cash United agents; correspondent banking for cross-border flows.",
              s=["con", "dig"], lc="move", o="P", at="OMT, BOB Finance, Cash United", neo=[0, ""],
              mc="Diaspora money arrives through agents and correspondents, not on cards.",
              src=[["neo by Bank Audi", NEO], ["2025 Annual Report", AR25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: 3-D Secure and cyber defences, anti-money-laundering controls, experiences and offers for card spenders, digital loans, and AI only at the edges.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security & compliance", "blurb": "3-D Secure, AML.", "div": "group", "rev": "group", "products": [
            P("secure", "3-D Secure & cyber security", "3-D Secure for online card payments and a dedicated cyber-security budget since 2022.",
              s=["con", "dig"], lc="everyday", neo=[1, "3-D Secure on Mastercard cards ⚠ vendor not public."], src=[["Bank Audi home page", HOME], ["2025 Annual Report", AR25]]),
            P("aml", "Compliance & AML", "A board compliance and AML committee; the Swiss unit, censured by FINMA in 2024, made progress in 2025 towards leaving its enforcement regime.",
              s=["corp"], st="flux", neo=[0, ""], src=[["2025 Annual Report", AR25], ["Wikipedia: Bank Audi", WIKI]]),
        ]},
        {"id": "3.2", "ic": "gift", "name": "Experiences & offers", "blurb": "Champions League, Toters.", "div": "audi", "rev": "retail", "products": [
            P("experiences", "Experiences for top spenders", "In 2025 the cards team took top spenders to the Cannes Film Festival and the UEFA Champions League Final, offering access rather than points.",
              s=["aff"], lc="grow", neo=[1, "Champions League is a Mastercard property ⚠."], src=[["2025 Annual Report", AR25]]),
            P("offers", "Card offers", "20% off Toters food delivery with Mastercard cards issued in Lebanon in October 2026 (code MASTERCARD2026), up to 15% off trip.com and IHG hotels, up to 35% off Avis, lounges and concierge.",
              s=["con", "aff"], lc="grow", st="new", ay="Oct 2026", o="P", at="Toters, Mastercard", neo=[1, "Toters offer is Mastercard's."],
              src=[["Bank Audi: Toters offer", TOTERS], ["Bank Audi: cards", CARDS]]),
        ]},
        {"id": "3.3", "ic": "hand-coins", "name": "Digital lending", "blurb": "A loan without a branch.", "div": "neo", "rev": "retail", "products": [
            P("dlend", "neo digital loans", "Lebanon's first end-to-end digital loan (2025) and a 50% salary advance for clients paid through neo; Lebanese loans reached $163 million at the end of 2025, $146 million in fresh dollars.",
              s=["dig"], lc="borrow", st="new", ay="2025", o="B", neo=[0, ""], src=[["2025 Annual Report", AR25], ["neo by Bank Audi", NEO]]),
        ]},
        {"id": "3.4", "ic": "brain", "name": "Data & AI", "blurb": "Research, not yet customers.", "div": "acap", "rev": "private", "products": [
            P("ai", "AI & data", "AI tools for research and advisory reports at Audi Capital and a new CRM; no customer-facing AI found ⚠.",
              s=["aff"], neo=[None, "Nothing public."], src=[["2025 Annual Report", AR25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail and payroll accounts holding 91% of deposits, the neo digital bank and neo teens, neo Business for 10,000 entrepreneurs, corporate and commercial banking, private banking in Geneva and Saudi Arabia, and Bank Audi France.",
    "tiles": [
        {"id": "4.1", "ic": "users-round", "name": "Retail & payroll", "blurb": "$11.7bn of deposits.", "div": "audi", "rev": "retail", "products": [
            P("retail", "Retail, personal & payroll banking", "Retail, personal and public-sector deposits of $11.7 billion (91% of the total) at the end of 2025; fresh deposits in Bank Audi Lebanon rose $297 million to $973 million, against $9.4 billion of restricted 'lollar' deposits.",
              s=["con"], lc="everyday", neo=[1, "Cards on Mastercard."], src=[["2025 Annual Report", AR25]]),
            P("teens", "neo teens", "A card and app for 11- to 17-year-olds, with pocket money, freezes and live spending for parents.",
              s=["teen"], lc="open", st="new", o="B", neo=[None, "Network not stated."], src=[["neo by Bank Audi", NEO], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "4.2", "ic": "rocket", "name": "neo digital bank", "blurb": "Profitable in its second year.", "div": "neo", "rev": "retail", "products": [
            P("neobank", "neo by Bank Audi", "Lebanon's first digital bank (2024): fresh dollar and lira accounts at onboarding, up to seven currencies, a $1.99 monthly package, payroll partnerships; profitable in 2025, ahead of plan; customer numbers not disclosed ⚠.",
              s=["dig"], lc="open", st="new", ay="2024", o="B", neo=[1, "Cards on Mastercard."],
              mc="The bank's growth engine and the natural home for Mastercard's digital tools.",
              src=[["neo by Bank Audi", NEO], ["2025 Annual Report", AR25], ["FinTech Futures: neo launch", NEOLAUNCH]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "SMEs & entrepreneurs", "blurb": "10,000 with Mastercard.", "div": "neo", "rev": "corporate", "products": [
            P("neobiz", "neo Business", "With Mastercard (9 September 2026): free accounts and Mastercard business debit cards for 10,000 entrepreneurs, including micro and women-led firms, with digital collections and supply-chain finance; Mastercard adds acceptance tools and merchant training.",
              s=["sme"], lc="open", st="new", ay="Sep 2026", o="P", at="Mastercard", neo=[2, "Mastercard business debit and acceptance."],
              mc="The newest joint programme, run by neo's Hassan Saleh and Mastercard's Mohamed Assem.",
              src=[["Bank Audi and Mastercard: 10,000 entrepreneurs", MC10K]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Corporate & commercial", "blurb": "Lending restarts in fresh dollars.", "div": "audi", "rev": "corporate", "products": [
            P("corporate", "Corporate & commercial banking", "Large corporates and specialised lending, corporate and commercial banking and SME banking; corporate and SME deposits of $1.18 billion at the end of 2025.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["2025 Annual Report", AR25], ["Bank Audi home page", HOME]]),
            P("treasury", "Treasury & capital markets", "Treasury and capital-markets desks, with placements at the central bank and banks worth 105% of deposits.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Private banking & wealth", "blurb": "$6.2bn of client assets.", "div": "suisse", "rev": "private", "products": [
            P("private", "Bank Audi Private Bank", "Banque Audi (Suisse) in Geneva and Lebanon Invest: client assets of $6.2 billion at the end of 2025, up 6%.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
            P("acap", "Audi Capital (KSA)", "The group's wealth arm in the Gulf, focused on Saudi Arabia: $635 million under management, more than 30 new clients in 2025, Audi Tadawul online trading and a retail platform with Amana ⚠.",
              s=["aff"], lc="grow", st="new", neo=[0, ""], src=[["2025 Annual Report", AR25], ["Audi Capital", ACAP]]),
        ]},
        {"id": "4.6", "ic": "globe", "name": "International", "blurb": "France and Qatar.", "div": "france", "rev": "intl", "products": [
            P("france", "Bank Audi France", "Corporate, personal, private and treasury banking in France, with 'solid growth' in 2025.",
              s=["corp", "aff"], lc="everyday", neo=[None, "Card network not found."], src=[["2025 Annual Report", AR25]]),
            P("qatar", "Bank Audi LLC (Qatar) & Abu Dhabi", "Corporate and commercial banking at the Qatar Financial Centre and a representative office in Abu Dhabi.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Bank Audi Group", GROUP]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the Bank Audi and neo apps, 43 group branches refocused on complex needs, and ATMs, agents and a 1570 contact centre.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps & online", "blurb": "Bank Audi app, neo app.", "div": "audi", "rev": "retail", "products": [
            P("app", "Bank Audi app & Audi Online", "Mobile and browser banking with transfers and bill payments (Touch top-ups, cinema tickets); a new internet and mobile platform is being procured.",
              s=["con", "corp"], lc="everyday", neo=[0, ""], src=[["Bank Audi: digital banking", DIGI], ["2025 Annual Report", AR25]]),
            P("neoapp", "neo app", "Fully digital onboarding and day-to-day banking, payroll-led.",
              s=["dig", "teen", "sme"], lc="open", st="new", o="B", neo=[0, ""], src=[["neo by Bank Audi", NEO]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "43, for complex needs.", "div": "audi", "rev": "retail", "products": [
            P("branches", "Branches", "43 group branches at the end of 2025, focused on higher-value and complex needs while routine work moves to digital channels.",
              s=["aff", "corp"], lc="everyday", st="flux", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
        ]},
        {"id": "5.3", "ic": "headset", "name": "ATMs, agents & 1570", "blurb": "200+ ATMs, cash agents.", "div": "audi", "rev": "retail", "products": [
            P("atms", "Smart ATMs & agents", "Smart ATMs open around the clock, more than 200 of them used for cardless cash-out, and agent partnerships for reach across Lebanon.",
              s=["con", "dig"], lc="everyday", o="P", at="OMT, BOB Finance, Cash United", neo=[0, ""], src=[["Bank Audi: digital banking", DIGI], ["neo by Bank Audi", NEO]]),
            P("contact", "Contact Center 1570", "Support around the clock by phone.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Bank Audi: digital banking", DIGI]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Bank Audi", "blurb": "A Mastercard issuer, now in SMEs.", "products": [
        P("mcataudi", "Mastercard at Bank Audi", "Every Bank Audi and neo card on its October 2026 pages is a Mastercard: World and World Elite credit, the MEA Cedar Miles co-brand, debit in fresh dollars and lira, neo's cards and neo Business debit. Google Pay launched for these Mastercard holders in June 2025, and on 9 September 2026 neo Business and Mastercard set out to bring 10,000 entrepreneurs into digital payments. Visa appears only in a 2015 co-brand ⚠.",
          s=["con"], div="group", rev="group", mc="The relationship this map is drawn for.",
          src=[["Bank Audi: cards", CARDS], ["Bank Audi and Mastercard: 10,000 entrepreneurs", MC10K], ["LBCI: Google Pay, Jun 2025", GPAY]]),
    ]},
    {"id": "pillar-market", "name": "Lebanese banking", "blurb": "Crisis, fresh dollars, cards back.", "products": [
        P("market", "The Lebanese market", "Since 2019: default, capital controls, 'lollars' against fresh dollars and a single rate of LBP 89,500. BDL now pushes cards over cash: merchant fees capped at 1.25%, dollar cards usable in lira at POS, card transactions up about 130% in January–August 2026, and a Mastercard–BDL acceptance programme (September 2026). Licensed wallets carry instant transfers; no national instant-payment scheme ⚠.",
          s=["con"], div="group", rev="group",
          src=[["ICE Beirut: card payments, Sep 2026", ICE], ["Mastercard and BDL, Sep 2026", MCBDL], ["BDL Announcement 980, Jun 2026", BDL980], ["2025 Annual Report", AR25]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
