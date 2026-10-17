"""Golomt Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the 2025 annual report (May 2026), the 2025 MD&A
(April 2026) and the Q2 2026 statement (21 July 2026). Mongolian payments context comes from the Bank of Mongolia,
Mastercard and QPay. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

AR25 = "https://www.golomtbank.com/wp-content/uploads/2026/05/Golomt-Bank-Annual-Report-2025-EN.pdf"
MDA25 = "https://www.golomtbank.com/wp-content/uploads/2026/04/MDA-2025.pdf"
Q2 = "https://golomtbank.com/en/news/55715/"
CEO = "https://golomtbank.com/en/news/52989/"
HIST = "https://www.golomtbank.com/en/about-bank/history-and-highlights"
CARDS = "https://www.golomtbank.com/en/retail/cards"
WORLD = "https://www.golomtbank.com/en/cards/48584/"
MCDEBIT = "https://www.golomtbank.com/en/cards/9649/"
GOLDMC = "https://www.golomtbank.com/en/cards/9639/"
AMEX = "https://www.golomtbank.com/en/cards/9634/"
SKATE = "https://www.golomtbank.com/en/cards/54329/"
TCARD = "https://www.golomtbank.com/en/cards/21795/"
UPDEBIT = "https://www.golomtbank.com/en/cards/9654/"
VISAPAY = "https://www.golomtbank.com/en/news/53719"
SAMSUNG = "https://www.golomtbank.com/en/news/55861/"
BOC = "https://www.golomtbank.com/en/news/57152/"
ABC = "https://www.golomtbank.com/en/news/57126/"
MASHREQ = "https://www.golomtbank.com/en/news/56194/"
NUCC = "https://golomtbank.com/en/news/43017"
SOCIALPAY = "https://www.golomtbank.com/en/digital-bank/socialpay"
IKONPAY = "https://ikon.mn/n/3i1q"
UNIVERSE = "https://ikon.mn/n/3nlv"
GPAY = "https://www.mongolbank.mn/en/r/11003"
TCARDHK = "https://www.mongolbank.mn/en/r/9147"
NPS = "https://mongolbank.mn/en/p/1301"
MCHIP = "https://newsroom.mastercard.com/news/europe/en/newsroom/news-briefs/en/2020/december/mastercard-partners-with-bank-of-mongolia-for-emv-chip-conversion"
QPAY = "https://qpay.mn/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · funding", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Mongolia's second-largest bank with 22% of sector assets and ROE of 24% in 2025, founded in 1995 and listed since 2022, funded by Eurobonds, a Samurai bond and development lenders, and heading for an 'AI bank'.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "MNT 19.9tn, 1.3m customers.", "div": "golomt", "rev": "treasury", "products": [
            P("balance", "Balance sheet & earnings 2025", "Total assets MNT 19.2 trillion (about USD 5.4 billion, 22.3% of the sector), loans MNT 8.3 trillion, customer funds MNT 10.8 trillion; net profit MNT 330.4 billion, ROE 23.8%, cost:income 47.2%, NPL 2.5%; more than 1.3 million customers, about 36% of Mongolians.",
              s=["con", "corp"], neo=[0, ""], src=[["Golomt: 2025 annual report", AR25], ["Golomt: 2025 MD&A", MDA25]]),
            P("h1", "First half 2026", "Assets MNT 19.9 trillion (up 32.9% on a year earlier), loans MNT 8.9 trillion (55% corporate), deposits MNT 11.0 trillion; half-year profit MNT 134.2 billion, annualised ROE 16.5%, NPL 2.5%.",
              s=["corp"], st="new", neo=[0, ""], src=[["Golomt: Q2 2026 statement, Jul 2026", Q2]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Owners, board & heritage", "blurb": "Since 1995; listed 2022.", "div": "gfg", "rev": "treasury", "products": [
            P("owners", "Ownership & listing", "Golomt Financial Group holds 79.77%, the public 11.6% since the 2022 IPO on the Mongolian Stock Exchange, Swiss-Mo Investment 5.21% and Bodi International 3.42%; market value MNT 1.08 trillion at end-2025; dividend MNT 80 a share from 2025 profit.",
              s=["corp"], neo=[0, ""], src=[["Golomt: 2025 annual report", AR25]]),
            P("leadership", "Board & management", "Chair Munkhtsetseg Ch. with five independent directors; CEO Odonbaatar A., President Ganbold Galsan, CRO Otgon T., CIO Sainbileg M.; about 2,800 staff.",
              s=["corp"], neo=[0, ""], src=[["Golomt: 2025 annual report", AR25]]),
            P("heritage", "Heritage", "Opened in 1995 with four staff and MNT 436 million of capital as Mongolia's first private bank with national investment; Mastercard issuer from 1999, Visa from 2000; a domestic systemically important bank.",
              s=["con"], o="I", neo=[0, ""], src=[["Golomt: history", HIST], ["Golomt: 2025 MD&A", MDA25]]),
        ]},
        {"id": "1.3", "ic": "coins", "name": "Funding & ratings", "blurb": "Samurai and green bonds.", "div": "intl", "rev": "treasury", "products": [
            P("funding", "International funding", "A USD 300 million Eurobond (2024), a USD 50 million green and social bond listed in Luxembourg (January 2025, 8%), Mongolia's first private Samurai bond (JPY 15 billion, 1.85%, November 2025) and a USD 160 million IFC 'blue' package; USD 1.2 billion raised abroad in 2025.",
              s=["corp"], st="new", o="P", at="SMBC, IFC, EBRD, ADB", neo=[0, ""], src=[["Golomt: 2025 annual report", AR25]]),
            P("ratings", "Credit ratings", "Moody's B1 stable (upgraded in 2025), S&P B+ positive and Fitch B+ stable.",
              s=["corp"], neo=[0, ""], src=[["Golomt: 2025 annual report", AR25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Towards an AI bank.", "div": "golomt", "rev": "retail", "products": [
            P("tech", "Core, cloud & AI", "Kubernetes across two data centres, AWS Direct Connect, microservices with CI/CD, a data lakehouse with 679 new models, AI for car and house pricing, eKYC and OCR, and PCI DSS 4.0 and PCI 3DS certification; 2025 is called the start of its move to an 'AI bank'.",
              s=["corp"], st="new", neo=[0, ""], src=[["Golomt: 2025 annual report", AR25]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy 2026", "blurb": "SMEs, markets, AI.", "div": "golomt", "rev": "treasury", "products": [
            P("strategy", "Seven priorities for 2026", "International capital markets, SMEs and non-mining growth, VIP and wealth services, asset quality, governance, the green transition and an 'AI-enabled virtual banking model'; no numeric targets published.",
              s=["corp"], st="new", neo=[0, ""],
              mc="The AI-bank plan is an opening for agentic payments.",
              src=[["Golomt: CEO letter, Mar 2026", CEO]]),
            P("green", "Green & blue finance", "Green loans of MNT 406 billion (4.9% of loans) with a 10% target by 2030, an internal carbon price, PCAF reporting since 2023 and a 30% emissions cut targeted by 2030.",
              s=["corp", "sme"], lc="borrow", neo=[0, ""], src=[["Golomt: 2025 annual report", AR25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: debit on Visa, Mastercard, UnionPay and the national ₮ Card; credit split between Visa, Mastercard and Amex; a World Mastercard at the top; Apple, Google and Samsung Pay; SocialPay QR; the China corridor; and card and QR acceptance.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "Four schemes side by side.", "div": "universe", "rev": "retail", "products": [
            P("debit", "Classic & premium debit", "Classic debit on Visa, Mastercard or UnionPay, Gold debit on Mastercard, and Si and Premier VIP debit on Visa; no split of cards by network is published.", short="Debit (Visa, Mastercard, UnionPay)",
              s=["con", "vip"], lc="everyday", o="P", at="Visa, Mastercard, UnionPay", neo=[1, "Shared with Visa and UnionPay."],
              src=[["Golomt: cards", CARDS], ["Golomt: Classic Mastercard debit", MCDEBIT]]),
            P("tcard", "₮ chip card", "The Bank of Mongolia's national ₮ Card, issued by Golomt: more than 2 million cards in Mongolia, over 45% of payment cards and 40% of transactions (April 2025), built on Mastercard's M/Chip specification and switched domestically.", short="₮ Card (national, M/Chip)",
              s=["con"], lc="everyday", o="P", at="Bank of Mongolia", neo=[1, "Domestic scheme on Mastercard's M/Chip specification."],
              mc="Mastercard's chip standard sits under the national card, but the switching is the central bank's.",
              src=[["Golomt: ₮ chip card", TCARD], ["Bank of Mongolia: ₮ Card in Hong Kong, Apr 2025", TCARDHK], ["Mastercard: M/Chip for the ₮ Card, Dec 2020", MCHIP]]),
            P("youth", "Color & Skate cards", "Contactless cards for ages 7–22: the Color card and Skate, Mongolia's first wearable payment device (2025, UnionPay).",
              s=["young"], lc="everyday", st="new", ay="2025", o="P", at="UnionPay, Mastercard ⚠", neo=[1, "Color card on Mastercard and UnionPay ⚠; Skate on UnionPay."],
              src=[["Golomt: Skate card", SKATE], ["Golomt: 2025 annual report", AR25]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "39% of card lending.", "div": "universe", "rev": "retail", "products": [
            P("visacredit", "Copper, Si & Platinum credit", "Visa credit cards from the Copper card to the metal Platinum card with limits up to MNT 50 million; Golomt holds 39.2% of Mongolia's credit-card loans.", short="Credit (Visa)",
              s=["con", "vip"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Golomt: cards", CARDS], ["Golomt: 2025 MD&A", MDA25]]),
            P("goldmc", "Gold Mastercard", "Gold credit and debit cards on Mastercard with Mastercard Travel Rewards, Priceless offers and Apple Pay; refreshed in 2017.", short="Gold (Mastercard)",
              s=["con", "vip"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Golomt: Gold card", GOLDMC], ["Golomt: history", HIST]]),
            P("amex", "American Express", "Golomt is Amex's partner in Mongolia (agreement 2013): Green and Gold credit cards with SELECTS discounts at 10,000+ merchants in 75+ countries, and a virtual Amex card.", short="American Express",
              s=["con", "vip"], lc="borrow", o="P", at="American Express", neo=[0, "American Express."], src=[["Golomt: Amex Green", AMEX], ["Golomt: history", HIST]]),
        ]},
        {"id": "2.3", "ic": "gem", "name": "World Mastercard & Universe", "blurb": "Metal at the top.", "div": "universe", "rev": "retail", "products": [
            P("worldmc", "World Mastercard", "A 22-gram metal credit card launched in 2025 with 26 concierge services and limits up to MNT 100 million, called the highest-tier card in Mongolia; Golomt credits it with 17% card-sales growth and 25% growth in international transactions.", short="World Mastercard",
              s=["vip"], lc="borrow", st="new", ay="2025", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard holds the top of Golomt's range.",
              src=[["Golomt: 2025 annual report", AR25], ["Golomt: World card", WORLD]]),
            P("universe", "Universe card range", "The whole card range redesigned for the 30th anniversary (2025), with limits, renewals and transfers managed in SocialPay; a first-anniversary offer ran in May 2026.", short="Universe cards",
              s=["con", "vip"], lc="everyday", st="new", ay="2025", neo=[1, "Spans Visa and Mastercard ⚠ no split published."],
              src=[["Golomt: 2025 annual report", AR25], ["Ikon: Universe anniversary, May 2026", UNIVERSE]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Phone wallets", "blurb": "Apple, Google, Samsung Pay.", "div": "socialpay", "rev": "retail", "products": [
            P("applepay", "Apple Pay", "First in Mongolia with TDB in December 2024, for Mastercard and ₮ cards; Visa added about April 2026 ⚠; a Mastercard cashback campaign ran September–November 2025.", short="Apple Pay (Mastercard first)",
              s=["con", "young"], lc="everyday", ay="Dec 2024", o="P", at="Apple, Mastercard", neo=[1, "Mastercard first, Visa since 2026."],
              src=[["Bank of Mongolia: Google Pay launch, Nov 2025", GPAY], ["Golomt: Visa on Apple Pay", VISAPAY], ["Ikon: Mastercard Apple Pay offer, Sep 2025", IKONPAY]]),
            P("googlepay", "Google Pay", "Launched in Mongolia on 18 November 2025; Golomt links Mastercard and ₮ cards and calls itself the first bank to offer it.", short="Google Pay",
              s=["con", "young"], lc="everyday", st="new", ay="Nov 2025", o="P", at="Google", neo=[1, "Mastercard and ₮ cards."],
              src=[["Bank of Mongolia: Google Pay launch, Nov 2025", GPAY], ["Golomt: 2025 annual report", AR25]]),
            P("samsungpay", "Samsung Pay", "First in Mongolia (July 2026) for about 800,000 Samsung phone users, with Visa and UnionPay cards only, linked through SocialPay.", short="Samsung Pay (no Mastercard)",
              s=["con"], lc="everyday", st="new", ay="Jul 2026", o="P", at="Samsung, Visa, UnionPay", neo=[0, "Visa and UnionPay only."],
              mc="The newest wallet launched without Mastercard.",
              src=[["Golomt: Samsung Pay, Jul 2026", SAMSUNG]]),
        ]},
        {"id": "2.5", "ic": "wallet", "name": "SocialPay", "blurb": "78% of digital users.", "div": "socialpay", "rev": "retail", "products": [
            P("socialpay", "SocialPay wallet", "Golomt's wallet since 2017 (version 3.0 in 2023): transfers by phone number or social handle, QR payments in shops, online account opening and card controls; 78% of the bank's 1 million digital users; connected to QPay, which links all Mongolian banks.", short="SocialPay QR",
              s=["con", "young", "sme"], lc="everyday", o="B", neo=[0, "Domestic QR and transfers."],
              src=[["Golomt: SocialPay", SOCIALPAY], ["Golomt: 2025 annual report", AR25], ["QPay", QPAY]]),
            P("virtual", "Virtual cards", "206,196 virtual cards issued in 2025, created in SocialPay on Visa, Mastercard, UnionPay or Amex, saving MNT 3.4 billion of plastic.",
              s=["con", "young"], lc="open", st="new", neo=[1, "Shared across schemes."],
              src=[["Golomt: 2025 annual report", AR25], ["Golomt: cards", CARDS]]),
        ]},
        {"id": "2.6", "ic": "globe", "name": "China & cross-border", "blurb": "29% of foreign payments.", "div": "intl", "rev": "treasury", "products": [
            P("unionpay", "UnionPay & WeChat QR", "UnionPay cards since 2010, with QR and barcode payments; since 2025 SocialPay scans WeChat QR codes in China with UnionPay cards at no extra fee; a 2024 MoU with CCB and NetsUnion on cross-border wallets.", short="UnionPay & WeChat",
              s=["con", "trader"], lc="move", o="P", at="UnionPay, WeChat Pay, CCB, NetsUnion", neo=[0, "UnionPay."],
              src=[["Golomt: UnionPay debit", UPDEBIT], ["Golomt: 2025 annual report", AR25], ["Golomt: CCB and NetsUnion MoU, Jul 2024", NUCC]]),
            P("cips", "RMB via CIPS", "A direct participant in China's CIPS (approved 2024), sending RMB with Agricultural Bank of China since September 2025; a trade and payments MoU with Bank of China and Xiamen C&D in September 2026.",
              s=["trader", "corp"], lc="move", st="new", ay="Sep 2025", o="P", at="ABC, Bank of China", neo=[0, ""],
              src=[["Golomt: ABC RMB anniversary, Sep 2026", ABC], ["Golomt: Bank of China MoU, Sep 2026", BOC]]),
            P("swift", "International transfers", "49 correspondent accounts in 15 currencies, SWIFT gpi and ISO 20022, Visa B2B, Western Union, fintech transfers by card or phone number and an AED account with Mashreq (August 2026); 29% of Mongolia's foreign payments by number and 32% by value.",
              s=["trader", "con"], lc="move", o="P", at="SWIFT, Visa B2B, Western Union, Mashreq", neo=[0, "SWIFT and Visa B2B."],
              mc="Cross-border card and phone transfers are open ground for Mastercard Move.",
              src=[["Golomt: 2025 annual report", AR25], ["Golomt: Mashreq, Aug 2026", MASHREQ]]),
        ]},
        {"id": "2.7", "ic": "store", "name": "Acceptance", "blurb": "POS, gateways, QR.", "div": "golomt", "rev": "sme", "products": [
            P("acquiring", "POS & e-commerce acceptance", "POS terminals, four payment gateways (2020) and e-commerce used by 16% of corporate clients; card commissions of MNT 81.8 billion in 2025 almost matched by MNT 75.0 billion of card costs; better 'issuance and acceptance' is a 2026 goal ⚠ no acquiring volumes published.", short="Acceptance (all networks)",
              s=["sme", "corp"], lc="move", o="B", neo=[1, "Accepts every network and the ₮ Card."],
              mc="Thin card margins and a 2026 acceptance push.",
              src=[["Golomt: 2025 annual report", AR25], ["Golomt: 2025 MD&A", MDA25], ["Golomt: history", HIST]]),
            P("easypay", "EasyPay instalments", "An instalment service built with a fintech in 2025 ⚠ network not stated.",
              s=["con", "sme"], lc="borrow", st="new", ay="2025", o="P", neo=[None, "Network not stated."],
              src=[["Golomt: 2025 annual report", AR25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: Golomt's own real-time fraud models, AI assistants in SocialPay and the contact centre, Wide Loyalty with a million members, and eKYC, open banking and agents.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Real-time AI models.", "div": "golomt", "rev": "retail", "products": [
            P("fraud", "Fraud & cyber defence", "Real-time AI fraud detection with behavioural analytics, multi-factor and risk-based authentication against account takeover, phishing and SMS scams; a 24/7 security operations centre with an international firm; PCI 3DS certified.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, "Golomt's own."],
              mc="Scam and fraud scoring is untested ground.",
              src=[["Golomt: 2025 annual report", AR25]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI assistants", "blurb": "In SocialPay and on the phone.", "div": "socialpay", "rev": "retail", "products": [
            P("aiassist", "AI personal assistant", "An AI assistant rolling out in mobile banking and SocialPay for budgets, bill reminders, payments and financial literacy.",
              s=["con"], lc="everyday", st="new", neo=[0, ""],
              mc="An assistant that pays is where Agent Pay could fit.",
              src=[["Golomt: CEO letter, Mar 2026", CEO], ["Golomt: 2025 annual report", AR25]]),
            P("contact", "AI contact centre", "An AI bot handling more than 30 services and resolving 67% of online chats; 1.95 million customer contacts in 2025 and WeChat, WhatsApp and KakaoTalk channels.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Golomt: 2025 annual report", AR25]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty & offers", "blurb": "A million members.", "div": "golomt", "rev": "retail", "products": [
            P("loyalty", "Wide Loyalty & coupons", "Points earned across partner merchants (the only bank scheme of its kind, says Golomt), Big Loyalty with 1,015,378 participants, Gen Z loyalty for 270,000 under-23s, and a Coupon Marketplace with 100+ coupon stores (2025).",
              s=["con", "young", "sme"], lc="grow", st="new", o="B", neo=[0, ""],
              mc="Card-linked offers could feed the coupon marketplace.",
              src=[["Golomt: 2025 annual report", AR25]]),
            P("offers", "Scheme offers", "Mastercard Travel Rewards and Priceless on Mastercard cards, Visa Offers and Perks on Visa cards, Amex SELECTS on Amex cards, and Priority Pass on the World card ⚠.",
              s=["vip", "con"], lc="grow", o="P", at="Mastercard, Visa, American Express", neo=[1, "Mastercard offers on Mastercard cards."],
              src=[["Golomt: Gold card", GOLDMC], ["Golomt: cards", CARDS]]),
        ]},
        {"id": "3.4", "ic": "fingerprint", "name": "Identity, open & agent banking", "blurb": "eKYC and agents.", "div": "golomt", "rev": "retail", "products": [
            P("ekyc", "eKYC & online onboarding", "Remote identification with eKYC and OCR, account opening in SocialPay and online branch registration.",
              s=["con", "young"], lc="open", st="new", neo=[0, ""], src=[["Golomt: 2025 annual report", AR25]]),
            P("openbank", "Open & agent banking", "Digital, open, service and agent banking are the bank's four business models; an agent platform sells products in places without branches ⚠ no API catalogue published.",
              s=["sme", "con"], lc="open", neo=[None, ""], src=[["Golomt: 2025 annual report", AR25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: corporate banking for 95% of Mongolia's top 100 companies, SME and women-entrepreneur lending, mortgages and savings, 61% of the country's letters of credit, and gold, wealth and leasing.",
    "tiles": [
        {"id": "4.1", "ic": "factory", "name": "Corporate banking", "blurb": "95% of the top 100.", "div": "golomt", "rev": "corp", "products": [
            P("corporate", "Corporate lending", "21.8% of corporate loans and 25.8% of corporate funding; lending to mining suppliers, energy, cashmere and food, and guarantees for 27 national projects.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Golomt: 2025 MD&A", MDA25], ["Golomt: 2025 annual report", AR25]]),
            P("gateway", "Corporate Gateway, payroll & fuel payments", "99% of corporate clients bank online, 21% through Corporate Gateway and 20% with payroll; Golomt handles 80–85% of Mongolia's fuel-payment transactions.",
              s=["corp"], lc="move", neo=[0, ""],
              mc="Corporate and fuel cards are untried for Mongolia's main corporate bank.",
              src=[["Golomt: 2025 annual report", AR25]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "SMEs & women entrepreneurs", "blurb": "Loans up 27%.", "div": "golomt", "rev": "sme", "products": [
            P("sme", "SME banking", "Micro and small loans up 27% and women-led lending up 28.4% in 2025, two SME centres, the Golomt Business Academy and Euromoney's Best Bank for SMEs 2025.",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["Golomt: 2025 annual report", AR25]]),
        ]},
        {"id": "4.3", "ic": "house", "name": "Retail lending & savings", "blurb": "24% of mortgages.", "div": "golomt", "rev": "retail", "products": [
            P("mortgages", "Mortgages", "23.6% of Mongolia's mortgages; MNT 267 billion of 6% state-programme mortgages to 2,118 families and MNT 351 billion securitised in 2025.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Golomt: 2025 MD&A", MDA25], ["Golomt: 2025 annual report", AR25]]),
            P("retaillending", "Salary, digital & herder loans", "Salary, pension, digital, car and herder loans, 16.7% of individual lending, with an internal 45% debt-to-income cap.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Golomt: 2025 MD&A", MDA25], ["Golomt: 2025 annual report", AR25]]),
            P("savings", "Savings & children's accounts", "16.6% of individual deposits, Altantulkhuur children's savings and savings lotteries such as 'Travel with Savings' (145,442 entrants).",
              s=["con", "young"], lc="grow", neo=[0, ""], src=[["Golomt: 2025 MD&A", MDA25], ["Golomt: 2025 annual report", AR25]]),
        ]},
        {"id": "4.4", "ic": "earth", "name": "Trade finance", "blurb": "61% of letters of credit.", "div": "intl", "rev": "treasury", "products": [
            P("tradefin", "Trade finance", "MNT 2.03 trillion of trade finance in 2025 and 60.6% of letters of credit and foreign guarantees, with ADB, IFC and EBRD programmes and 300+ partner banks.",
              s=["trader", "corp"], lc="move", o="P", at="ADB, IFC, EBRD", neo=[0, ""], src=[["Golomt: 2025 annual report", AR25], ["Golomt: 2025 MD&A", MDA25]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Gold, wealth & leasing", "blurb": "48% of gold.", "div": "premiere", "rev": "treasury", "products": [
            P("gold", "Gold trading", "48% of Mongolia's deposited physical gold and Digital Gold Trading in customers' names (2025).",
              s=["vip", "corp"], lc="grow", st="new", neo=[0, ""], src=[["Golomt: 2025 annual report", AR25]]),
            P("wealth", "Premiere, wealth, leasing & insurance", "Premiere VIP service with concierge, private wealth management since 2023, leasing of MNT 257.3 billion and 28% of insurance brokerage.",
              s=["vip"], lc="grow", neo=[0, ""], src=[["Golomt: 2025 annual report", AR25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: internet bank, Smart bank and SocialPay for a million users, 108 branches and 403 ATMs, and agents and direct sales.",
    "tiles": [
        {"id": "5.1", "ic": "monitor", "name": "Internet & Smart bank", "blurb": "A million users.", "div": "golomt", "rev": "retail", "products": [
            P("digital", "Internet bank & Smart bank", "About 1 million digital users (993,000 on internet and Smart bank) and 99% of transfers and payments made online or by card.",
              s=["con", "sme", "corp"], lc="everyday", neo=[0, ""], src=[["Golomt: 2025 annual report", AR25]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "108 branches.", "div": "golomt", "rev": "retail", "products": [
            P("branches", "Branches & ATMs", "108 branches (73 in Ulaanbaatar, 35 rural), 403 ATMs and cash machines, self-service kiosks in 66 branches and five new branches in 2025.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Golomt: 2025 MD&A", MDA25], ["Golomt: 2025 annual report", AR25]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Agents & direct sales", "blurb": "628 partner organisations.", "div": "golomt", "rev": "retail", "products": [
            P("agents", "Agents, direct sales & cards.mn", "Agent banking in branchless places, a direct-sales team working with 628 organisations, and card ordering at cards.mn.",
              s=["con", "sme"], lc="open", neo=[0, ""], src=[["Golomt: 2025 annual report", AR25], ["Golomt: Samsung Pay, Jul 2026", SAMSUNG]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Golomt", "blurb": "Metal cards and phone wallets.", "products": [
        P("mcatgolomt", "Mastercard at Golomt", "A Mastercard issuer since 1999, Golomt puts Mastercard at the top of its range (World and Gold) and first on Apple Pay (December 2024) and Google Pay (November 2025), and issues the national ₮ Card built on Mastercard's M/Chip. Visa carries more credit programmes and, with UnionPay, Samsung Pay; Amex and UnionPay hold their own niches.",
          s=["con"], div="golomt", rev="retail", mc="The relationship this map is drawn for.",
          src=[["Golomt: history", HIST], ["Golomt: 2025 annual report", AR25], ["Mastercard: M/Chip for the ₮ Card, Dec 2020", MCHIP]]),
    ]},
    {"id": "pillar-market", "name": "Mongolian payments", "blurb": "₮ Card, QPay, ACH+.", "products": [
        P("market", "The Mongolian market", "Twelve banks led by Khan Bank and Golomt; the Bank of Mongolia runs RTGS, a 24/7 ACH+ and the interbank card switch through its National Electronic Transaction Center; the ₮ Card and QPay's interbank QR carry much of domestic spending; policy rate 12% and a 45% debt-to-income cap from January 2026.",
          s=["con"], div="golomt", rev="retail", src=[["Bank of Mongolia: national payment system", NPS], ["QPay", QPAY], ["Golomt: 2025 MD&A", MDA25]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
