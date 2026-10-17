"""NLB Group's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results (6 August 2026), the 2025
annual report and results (12 February 2026), and the 2026 Investor Day update to Strategy 2030. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1KH = "https://www.nlbgroup.com/content/dam/nlb/nlb-group/documents/investor-relations/financial-reports/2026/h1/NLB-Group-in-Q2andH1-Key-Highlights.pdf"
H1P = "https://www.nlbgroup.com/content/dam/nlb/nlb-group/documents/investor-relations/financial-reports/2026/h1/NLB-Group-Presentation-1H-2026.pdf"
Q2 = "https://www.nlbgroup.com/int-en/investor-relations/investor-news/2026/investor-news-06-08-2026"
AR25 = "https://www.nlbgroup.com/content/dam/nlb/nlb-group/documents/investor-relations/financial-reports/2025/ye2025/NLB-Group-Annual-Report-2025_ENG.pdf"
FY25 = "https://www.nlbgroup.com/int-en/media-center/press-releases/2026/press-release-12-02-2026"
IR = "https://www.nlbgroup.com/int-en/investor-relations"
DBS = "https://www.nlbgroup.com/int-en/investor-relations/investor-news/2026/investor-news-18-09-2026"
ADDIKO = "https://www.nlbgroup.com/int-en/investor-relations/investor-news/2026/investor-news-03-08-2026"
ADDIKOBID = "https://www.intellinews.com/slovenia-s-nlb-announces-29-per-share-takeover-bid-for-addiko-bank-436804/"
RBI = "https://www.intellinews.com/rbi-reaches-takeover-threshold-in-addiko-bid-as-battle-with-nlb-enters-final-week-456508/"
STRAT26 = "https://inter.capital/nlbs-2030-bet-can-the-see-growth-engine-deliver/"
CARDS = "https://www.nlb.si/kartice"
BIZCARD = "https://www.nlb.si/podjetja/pomoc-in-orodja/kartice/kako-narocim-novo-kartico"
TARIFF25 = "https://nlb.si/content/dam/nlb/pdf-files/osebne-finance/napovednik-za-objavo-sprememb-v-nlb-tarifi-za-prebivalstvo-z-veljavnostjo-1-4-2025.pdf"
KBCARDS = "https://www.nlbkb.rs/content/dam/nlb/nlbkb-rs-serbia/documents/opsti-uslovi-poslovanja/op%C5%A1ti-uslovi/01-07-2025/Pregled%20tarifa%20naknada%20koje%20se%20primenjuju%20u%20poslovima%20Banke%20sa%20platnim%20karticama_25.12.2025..pdf"
KOSVISA = "https://nlb-kos.com/en/news/17/visa-classic-debit"
APPLEPAY24 = "https://www.nlb.si/press-release-27-2-2024"
FLIK = "https://www.bankart.si/en/flik-pay/"
PAYSCHED = "https://nlb.si/urnik-placilnega-prometa_ang"
NLBPAY = "https://apps.apple.com/mx/app/nlb-pay/id1509897528"
KB2020 = "https://seenews.com/news/slovenias-nlb-completes-purchase-of-serbias-komercijalna-banka-726388"
WIKI = "https://en.wikipedia.org/wiki/NLB_Group"
WERO = "https://banking.vision/en/development-wero-2025-2026/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · seven banks · Strategy 2030", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: EUR 31.9 billion of assets and 2.9 million active clients across seven banks, a third of Slovenian banking, a state stake of 25% plus one share, and Strategy 2030 with a lost Addiko bid and a new deal for DBS.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & ratings", "blurb": "EUR 31.9bn, A2 from Moody's.", "div": "group", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Total assets EUR 31.85 billion, gross loans EUR 20.06 billion (up 12% a year) and deposits EUR 25.08 billion at 30 June 2026; H1 2026 profit after tax EUR 252.4 million (Q2 EUR 133.1 million), CET1 14.8%, ROTE 14.5%, CIR 46.5%; 2025 profit EUR 503.1 million.",
              s=["con"], neo=[0, ""], src=[["H1 2026 key highlights", H1KH], ["2025 results, Feb 2026", FY25]]),
            P("owners", "Listing, ownership & ratings", "Listed in Ljubljana with London GDRs since November 2018; the Republic of Slovenia holds 25% plus one share; market value about EUR 3.65 billion at end-2025; Moody's A2 (March 2026) and S&P BBB+ (positive outlook).",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025", AR25], ["Wikipedia: NLB Group", WIKI], ["H1 2026 presentation", H1P]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Brodnjak and Karpe.", "div": "group", "rev": "other", "products": [
            P("leadership", "Management & supervisory boards", "CEO Blaž Brodnjak, CFO Archibald Kremser, CRO Andreas Burkhardt, Chief Transformation Officer Reinhard Höll, Hedvika Usenik (retail), Andrej Lasič (CIB) and Antonio Argir; Primož Karpe chairs the Supervisory Board. No named head of cards or payments ⚠.",
              s=["corp"], neo=[0, ""], src=[["Q2 2026 results release", Q2], ["Annual report 2025", AR25]]),
        ]},
        {"id": "1.3", "ic": "earth", "name": "Heritage & footprint", "blurb": "Seven banks, six countries.", "div": "group", "rev": "sfm", "products": [
            P("heritage", "Heritage & footprint", "Ljubljanska banka (1955) became Nova Ljubljanska banka in 1994; today seven banks with 371 branches in Slovenia, Serbia, North Macedonia, Bosnia and Herzegovina, Kosovo and Montenegro, plus leasing in Croatia; SEE banks gave 57% of the H1 2026 result.",
              s=["con", "see"], o="I", neo=[0, ""], src=[["Wikipedia: NLB Group", WIKI], ["H1 2026 presentation", H1P]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "A quarter of staff on AI tools.", "div": "group", "rev": "other", "products": [
            P("tech", "Operating model, IT & AI", "A new technology operating model, core-banking migrations and NLB DigIT in Belgrade; about 25% of employees use AI tools (Copilot for Microsoft 365, ChatGPT Enterprise) and more than 60% have had AI training; higher IT spending pushed H1 2026 costs up 3.6%.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025", AR25], ["H1 2026 key highlights", H1KH]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy 2030 & deals", "blurb": "EUR 45bn organic, DBS next.", "div": "group", "rev": "other", "products": [
            P("strategy", "Strategy 2030", "Set in May 2024 and updated at the 2026 Investor Day in Sarajevo: EUR 45 billion of assets organically (EUR 50 billion+ with M&A), recurring revenue above EUR 1.8 billion, net income above EUR 0.85 billion, CIR in the low 40s, payout towards 60%, digital penetration above 80% and payments revenue above EUR 320 million.",
              s=["corp"], st="new", neo=[0, ""], src=[["InterCapital: NLB's 2030 bet, May 2026", STRAT26], ["Q2 2026 results release", Q2]]),
            P("deals", "Acquisitions 2020–25", "Komercijalna banka Beograd (December 2020, EUR 394.7 million), Sberbank Slovenia as N Banka (March 2022, merged September 2023) and Summit Leasing with Mobil Leasing in Croatia (September 2024, merged into NLB Lease&Go in July 2025).",
              s=["see"], o="A", neo=[0, ""], src=[["SeeNews: Komercijalna completed, Dec 2020", KB2020], ["Wikipedia: NLB Group", WIKI], ["Annual report 2025", AR25]]),
            P("addiko", "Addiko Bank bid (failed)", "An all-cash bid for Addiko Bank AG from 13 May 2026 at EUR 29 a share, later raised; only 31.22% of shares were tendered and the offer lapsed on 3 August 2026, while Raiffeisen Bank International took control.",
              s=["see"], st="retired", ay="May 2026", o="A", neo=[0, ""],
              src=[["NLB: Addiko offer results, Aug 2026", ADDIKO], ["Intellinews: EUR 29 bid, May 2026", ADDIKOBID], ["Intellinews: RBI reaches threshold, Jul 2026", RBI]]),
            P("dbs", "Deželna banka Slovenije", "Agreement on 18 September 2026 to buy more than 55% of DBS: 65 branches, EUR 1.6 billion of assets (2.8% share) and a focus on farming and rural clients; closing expected in the second half of 2027.",
              s=["con", "sme"], st="new", ay="Sep 2026", o="A", neo=[None, "DBS's card networks not checked."],
              mc="65 branches of rural customers whose cards could move onto NLB's programmes after 2027.",
              src=[["NLB: DBS agreement, Sep 2026", DBS]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Debit Mastercard for every Slovenian personal account since Maestro went, mostly Mastercard credit with some Visa, Visa for business debit, Visa, Mastercard and DinaCard in Serbia, NLB Pay and the big wallets, Flik and SEPA Instant, and Smart POS acquiring with Bankart behind it.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "Debit Mastercard replaced Maestro.", "div": "nlb", "rev": "retail", "products": [
            P("debit", "NLB Mastercard debit", "Every Slovenian personal debit card is now a Debit Mastercard (standard in all packages, World in Premium, World Elite for private clients), with purchase insurance and airport perks; Maestro was discontinued from April 2025.", short="Debit (Mastercard)",
              s=["con", "priv"], lc="everyday", st="new", ay="Apr 2025", o="P", at="Mastercard", neo=[2, "Debit Mastercard."],
              mc="The core of the relationship: about 738,000 active Slovenian clients bank with a Mastercard debit card.",
              src=[["NLB: cards", CARDS], ["NLB tariff notice, Apr 2025", TARIFF25], ["Annual report 2025", AR25]]),
            P("digitalcard", "Digital-first debit card", "A debit card issued instantly into the NLB Pay wallet on ordering, usable online, in shops and at ATMs before the plastic arrives (late 2025); real-time card delivery is a 2026 priority across the group.",
              s=["con"], lc="open", st="new", ay="Dec 2025", o="B", neo=[2, "Issued on Debit Mastercard."],
              src=[["Annual report 2025", AR25], ["H1 2026 presentation", H1P]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit & premium cards", "blurb": "Mostly Mastercard, some Visa.", "div": "nlb", "rev": "retail", "products": [
            P("credit", "NLB credit cards", "Revolving 3v1 cards (Mastercard, World and World Elite) and charge-style NLB Zlati Mastercard, NLB Mastercard, NLB Visa and NLB Premium Visa, with SMS instalments and family cards; balances not disclosed.", short="Credit (Mastercard and Visa)",
              s=["con", "priv"], lc="borrow", o="P", at="Mastercard, Visa", neo=[1, "Mostly Mastercard; Visa and Premium Visa too."],
              src=[["NLB: cards", CARDS]]),
            P("premium", "World & World Elite benefits", "Mastercard Concierge, Priority Pass and fast-track at Ljubljana airport on World and World Elite cards; LoungeKey added to World Elite debit for private-banking clients in 2025.",
              s=["priv"], lc="everyday", st="new", ay="2025", o="P", at="Mastercard", neo=[2, "World and World Elite Mastercard benefits."],
              src=[["NLB: cards", CARDS], ["Annual report 2025", AR25]]),
        ]},
        {"id": "2.3", "ic": "briefcase", "name": "Business & prepaid cards", "blurb": "Business debit moved to Visa.", "div": "nlb", "rev": "cib", "products": [
            P("bizcards", "Business cards", "Business debit cards migrated into the Visa scheme in June 2025 and the Visa Business migration was completed, though NLB's help pages still name a business debit Mastercard and a Mastercard business credit card ⚠.", short="Business cards (Visa, Mastercard ⚠)",
              s=["sme"], lc="move", st="flux", ay="Jun 2025", o="P", at="Visa, Mastercard", neo=[1, "Business debit on Visa; Mastercard credit ⚠."],
              mc="Mastercard lost the business debit book in 2025; commercial and virtual cards are the way back.",
              src=[["Annual report 2025", AR25], ["NLB: business cards", BIZCARD]]),
            P("prepaid", "CeKR prepaid card", "A prepaid card issued with the Municipality of Kranj.",
              s=["con"], lc="everyday", o="P", at="Municipality of Kranj, Visa", neo=[0, "Visa."], src=[["NLB: cards", CARDS]]),
        ]},
        {"id": "2.4", "ic": "globe", "name": "Cards in SEE", "blurb": "Visa, Mastercard and DinaCard.", "div": "kb", "rev": "sfm", "products": [
            P("kbcards", "NLB Komercijalna banka cards", "Serbia's bank for 1 million active clients issues DinaCard (domestic, including a DIS co-brand), Visa (Debit PayWave, Prepaid, Platinum, Revolving, Business) and Mastercard (Debit Standard and Gold, Standard and Installment credit, Business).", short="Serbia (DinaCard, Visa, Mastercard)",
              s=["see"], lc="everyday", o="I", at="DinaCard, Visa, Mastercard", neo=[1, "Shared with Visa and DinaCard."],
              src=[["NLB Komercijalna banka: card tariff, Dec 2025", KBCARDS], ["H1 2026 presentation", H1P]]),
            P("seecards", "Cards in Skopje, Bosnia, Prishtina & Podgorica", "NLB Banka Prishtina issues Visa Classic Debit and Visa Personal Banking alongside a debit Mastercard ⚠; networks in North Macedonia, Bosnia and Montenegro were not confirmed from primary pages ⚠.",
              s=["see"], lc="everyday", o="I", at="Visa, Mastercard", neo=[1, "Visa and Mastercard in Kosovo ⚠; others not confirmed."],
              src=[["NLB Banka Prishtina: Visa Classic Debit", KOSVISA]]),
        ]},
        {"id": "2.5", "ic": "smartphone", "name": "Wallets & tokens", "blurb": "28.9% tokenised.", "div": "nlb", "rev": "retail", "products": [
            P("nlbpay", "NLB Pay", "The group's own wallet for Mastercard and Visa cards plus Flik transfers and QR payments; 25.9% of mobile-wallet payments in 2025 (target above 40% by 2030), with tokenised payments rising from 2.9% of card transactions in 2023 to 28.9% in H1 2026.",
              s=["con"], lc="move", o="B", neo=[1, "Tokenises Mastercard and Visa; Flik too."],
              mc="Fast-rising tokenisation and a 40% wallet target are where Mastercard's token services earn their place.",
              src=[["H1 2026 presentation", H1P], ["InterCapital: NLB's 2030 bet, May 2026", STRAT26], ["App Store: NLB Pay", NLBPAY]]),
            P("xpay", "Apple Pay, Google Pay & Garmin Pay", "Apple Pay in Slovenia from February 2024 and in every NLB bank by July 2025, the first bank in the region to do so; Google Pay and Garmin Pay in Banja Luka and Prishtina.",
              s=["con", "see"], lc="move", st="new", ay="Feb 2024", o="P", at="Apple, Google, Garmin", neo=[1, "Carries Mastercard and Visa cards."],
              src=[["NLB: Apple Pay, Feb 2024", APPLEPAY24], ["Annual report 2025", AR25]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Instant payments", "blurb": "Flik and SEPA Instant.", "div": "nlb", "rev": "retail", "products": [
            P("flik", "Flik", "Slovenia's bank-owned instant-payment scheme, run by Bankart: NLB offers Flik person-to-person, Flik at every point of sale, Split Bill and recurring payments (2025), up to EUR 15,000 into NLB accounts.",
              s=["con", "sme"], lc="move", o="P", at="Bankart", neo=[0, "Domestic account-to-account."],
              mc="Flik at the till competes with cards for the same purchases.",
              src=[["Bankart: Flik Pay", FLIK], ["Annual report 2025", AR25], ["NLB: payment schedule", PAYSCHED]]),
            P("sepa", "SEPA & instant transfers", "Instant euro payments 24/7 through BIPS IP and TIPS; regional SEPA extended to Montenegro and North Macedonia in 2025, with SEPA Instant rolling out across the group.",
              s=["con", "corp", "see"], lc="move", st="new", o="B", neo=[0, ""],
              src=[["NLB: payment schedule", PAYSCHED], ["Annual report 2025", AR25], ["H1 2026 presentation", H1P]]),
        ]},
        {"id": "2.7", "ic": "store", "name": "Acceptance & processing", "blurb": "Smart POS, Bankart.", "div": "nlb", "rev": "cib", "products": [
            P("acquiring", "Merchant acquiring & NLB Smart POS", "Acquiring aimed at small merchants: Smart POS on a phone with instalments and tips, Android terminals, digital onboarding from end-2025, and partnerships with fiscal-register and POS vendors.", short="Acquiring & Smart POS",
              s=["sme"], lc="move", o="P", neo=[1, "Accepts every network ⚠."],
              mc="An acquirer rebuilding its small-merchant model needs acceptance, onboarding and risk tools.",
              src=[["Annual report 2025", AR25]]),
            P("atm", "ATMs & cash machines", "One of Slovenia's largest ATM networks and the first cash-deposit machine for businesses (2025); retail branch cash transactions to fall from 15.1% to below 10% by 2030.",
              s=["con", "sme"], lc="everyday", o="B", neo=[1, "Accepts cards of every network ⚠."],
              src=[["Annual report 2025", AR25], ["InterCapital: NLB's 2030 bet, May 2026", STRAT26]]),
            P("bankart", "Bankart", "NLB owns 46% of Bankart, Slovenia's shared payment processor and the operator of Flik; its role in NLB's card processing is not set out in public ⚠.",
              s=["corp"], lc="move", o="P", at="Bankart", neo=[None, "Processing role not public."],
              src=[["H1 2026 presentation", H1P], ["Bankart: Flik Pay", FLIK]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: wallet anti-fraud and biometric onboarding, an AI assistant and a 24/7 contact centre, and a loyalty model still on the drawing board.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Biometric onboarding.", "div": "nlb", "rev": "retail", "products": [
            P("fraud", "Fraud & security", "An anti-fraud solution and a one-device rule in NLB Pay (2025), and external security scoring above the 80% target; which card-fraud tools NLB uses is not public ⚠.",
              s=["con"], lc="everyday", o="B", neo=[None, "Card-fraud tools not public."],
              mc="Network fraud scoring and identity checks have nothing public against them.",
              src=[["Annual report 2025", AR25], ["H1 2026 presentation", H1P]]),
            P("onboarding", "Digital onboarding & login", "Mobile-first, biometric onboarding in Slovenia (early 2026), simplified login and reactivation, and digital client acquisition to rise from 0.4% to above 30% by 2030.",
              s=["con"], lc="open", st="new", o="B", neo=[0, ""],
              src=[["H1 2026 presentation", H1P], ["InterCapital: NLB's 2030 bet, May 2026", STRAT26]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & service", "blurb": "Assistant and 24/7 centre.", "div": "nlb", "rev": "retail", "products": [
            P("ai", "AI assistant", "An AI virtual assistant on nlb.si, an AI chatbot and text-to-speech in the contact centre, being rolled out across the group with internal AI assistants planned for 2026.",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["Annual report 2025", AR25], ["H1 2026 presentation", H1P]]),
            P("contact", "Contact centre & video", "A 24/7 contact centre on one number, and video calls that made 11% of key retail sales in 2025.",
              s=["con", "priv"], lc="everyday", o="B", neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty", "blurb": "A model still being designed.", "div": "group", "rev": "retail", "products": [
            P("loyalty", "Customer loyalty model", "A target loyalty model being defined in 2025, with data collection and choice of a pilot country; no group-wide programme is live ⚠.",
              s=["con", "see"], lc="grow", st="unconf", o="B", neo=[None, "Not built yet."],
              mc="Card-linked offers could form the loyalty model before it is built.",
              src=[["Annual report 2025", AR25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: a third of Slovenian retail banking in four packages, private banking and Slovenia's biggest fund manager, leasing, corporate and SME banking, and six banks across the Western Balkans.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Retail Slovenia", "blurb": "A third of the market.", "div": "nlb", "rev": "retail", "products": [
            P("packages", "Accounts & packages", "Osnovni, Aktivni, Premium and Privatno packages for about 738,000 active clients, each with a Debit Mastercard; 37% of individuals' sight deposits.",
              s=["con"], lc="everyday", o="B", neo=[1, "Debit Mastercard in every package."],
              src=[["NLB: cards", CARDS], ["H1 2026 presentation", H1P]]),
            P("housing", "Housing & consumer loans", "About 33% of Slovenian housing loans and 30% of consumer loans at 30 June 2026, with the NLB Dom home platform and estate-agent referrals.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["H1 2026 presentation", H1P], ["Annual report 2025", AR25]]),
        ]},
        {"id": "4.2", "ic": "gem", "name": "Private banking & wealth", "blurb": "EUR 3.7bn private, EUR 4.4bn funds.", "div": "ancillary", "rev": "retail", "products": [
            P("private", "NLB Private Banking", "More than 3,000 clients and EUR 3.7 billion under management, with World Elite Mastercard cards and the NLB Private app.",
              s=["priv"], lc="grow", o="B", neo=[1, "World Elite Mastercard cards."],
              src=[["H1 2026 presentation", H1P], ["Annual report 2025", AR25]]),
            P("skladi", "NLB Skladi & funds", "Slovenia's leading fund manager with 43.3% of mutual-fund assets (EUR 4.4 billion), plus NLB Fondovi in Skopje and Belgrade; net inflows of EUR 151.1 million in H1 2026.",
              s=["saver"], lc="grow", o="B", neo=[0, ""], src=[["H1 2026 presentation", H1P]]),
            P("bancassurance", "Bancassurance", "Insurance sold through the banks, growing double digits, with insurance acquisitions under review.",
              s=["saver"], lc="grow", o="P", neo=[0, ""], src=[["H1 2026 key highlights", H1KH], ["Q2 2026 results release", Q2]]),
        ]},
        {"id": "4.3", "ic": "briefcase-business", "name": "Leasing", "blurb": "37% of Slovenian leasing.", "div": "ancillary", "rev": "cib", "products": [
            P("lease", "NLB Lease&Go", "Vehicle and equipment leasing in Slovenia (37% share after the Summit Leasing merger), Serbia, North Macedonia and Croatia (Mobil Leasing); profit above EUR 35 million in 2025.",
              s=["sme", "con"], lc="borrow", o="A", neo=[0, ""], src=[["H1 2026 presentation", H1P], ["2025 results, Feb 2026", FY25]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Corporate & SME", "blurb": "Slovenia's top arranger.", "div": "nlb", "rev": "cib", "products": [
            P("cib", "Corporate & investment banking", "Key, SME and cross-border corporates, Slovenia's leading syndicated-loan arranger, EUR 1.17 billion of bonds arranged in 2025, custody and FX hedging.",
              s=["corp"], lc="borrow", o="B", neo=[0, ""], src=[["Annual report 2025", AR25], ["H1 2026 presentation", H1P]]),
            P("trade", "Trade finance & factoring", "Guarantees, factoring and reverse factoring, receivables finance for foreign buyers, and digital factoring with faster payouts.",
              s=["corp", "sme"], lc="borrow", st="new", o="B", neo=[0, ""], src=[["Annual report 2025", AR25], ["H1 2026 presentation", H1P]]),
            P("sme", "Micro & SME banking", "Advisory teams and simplified digital products for micro businesses; a revamped SME service model in Slovenia and Serbia.",
              s=["sme"], lc="everyday", o="B", neo=[0, "Business debit on Visa ⚠."], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "4.5", "ic": "flag", "name": "Banks in SEE", "blurb": "Six banks, 2.2m clients.", "div": "kb", "rev": "sfm", "products": [
            P("seebanks", "Six banks in the Western Balkans", "NLB Komercijalna banka (Serbia, 10.6%), Skopje (16.3%), Banja Luka (21.8%), Sarajevo (6.3%), Prishtina (17.6%) and Podgorica (14.3%): EUR 10.1 billion of loans, up 15% a year, and EUR 150.9 million pre-tax in H1 2026.",
              s=["see"], lc="everyday", o="A", neo=[1, "Cards on Visa, Mastercard and DinaCard."],
              src=[["H1 2026 presentation", H1P]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach NLB: NLB Klik and the specialist apps for 1.9 million digital users, Klikpro for businesses, 371 branches, and partners from estate agents to POS vendors.",
    "tiles": [
        {"id": "5.1", "ic": "monitor", "name": "NLB Klik & apps", "blurb": "1.9 million digital users.", "div": "nlb", "rev": "retail", "products": [
            P("klik", "NLB Klik", "Online and mobile banking, rated Slovenia's best digital bank; 70.8% digital penetration at NLB and more than 1.9 million digital users across the group, about 70% of them active.",
              s=["con", "see"], lc="everyday", o="B", neo=[0, ""], src=[["H1 2026 presentation", H1P], ["Annual report 2025", AR25]]),
            P("privateapp", "NLB Private & NLB Trading apps", "A private-banking app (August 2025) and a trading app (September 2025), with individual investment accounts in Slovenia.",
              s=["priv", "saver"], lc="grow", st="new", ay="Aug 2025", o="B", neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "5.2", "ic": "log-in", "name": "Klikpro", "blurb": "Business e-banking.", "div": "nlb", "rev": "cib", "products": [
            P("klikpro", "Klikpro", "Corporate e-banking, upgraded in Slovenia and rolling out across the group.",
              s=["sme", "corp"], lc="everyday", o="B", neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches", "blurb": "371 branches, 70 in Slovenia.", "div": "group", "rev": "retail", "products": [
            P("branches", "Branches", "371 branches: 70 in Slovenia, 129 in Serbia and the rest across the region, turning into advisory hubs; DBS would add 65 in rural Slovenia.",
              s=["con", "see"], lc="everyday", o="B", neo=[0, ""], src=[["H1 2026 presentation", H1P], ["NLB: DBS agreement, Sep 2026", DBS]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners", "blurb": "Agents, vendors, towns.", "div": "group", "rev": "retail", "products": [
            P("partners", "Partners", "Estate agents for NLB Dom, fiscal-register and POS vendors for merchants, the Municipality of Kranj for prepaid cards, and Apple, Google and Garmin for wallets.",
              s=["con", "sme"], lc="open", o="P", neo=[0, ""], src=[["Annual report 2025", AR25], ["NLB: cards", CARDS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at NLB", "blurb": "Consumer cards, not business debit.", "products": [
        P("mcatnlb", "Mastercard at NLB", "Mastercard carries every Slovenian personal debit card since Maestro was retired in 2025, most credit cards and the World and World Elite tiers. Visa took business debit in June 2025 and shares Serbia and Kosovo, where DinaCard also competes. No joint initiative with Mastercard is public.",
          s=["con"], div="group", rev="retail", mc="The relationship this map is drawn for.",
          src=[["NLB: cards", CARDS], ["Annual report 2025", AR25], ["NLB Komercijalna banka: card tariff, Dec 2025", KBCARDS]]),
    ]},
    {"id": "pillar-market", "name": "Slovenia & the Western Balkans", "blurb": "Flik, SEPA, consolidation.", "products": [
        P("market", "The market", "NLB holds 33.5% of Slovenian banking assets against OTP's 26.6%; Addiko went to Raiffeisen; Flik and SEPA Instant compete at the till, Wero and the European alliance aim at shops by 2027 ⚠, and SEPA is reaching Montenegro, North Macedonia and Kosovo.",
          s=["con"], div="group", rev="other", src=[["H1 2026 presentation", H1P], ["Wero 2025/2026", WERO]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
