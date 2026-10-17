"""ING Groep's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 2Q2026 results (30 July 2026), the 4Q/FY2025
results (29 January 2026) and the 2025 Form 20-F (26 February 2026). ``neo`` is the Mastercard lens: [depth, note],
where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://www.ing.com/binaries/content/assets/documents/results/2q2026/2q2026-ing-press-release.pdf"
FY25 = "https://ing.com/news/press-releases/4qfy2025-ing-press-release.html"
F20 = "https://www.sec.gov/Archives/edgar/data/1039765/000162828026011979/ing-20251231.htm"
GIROTEL = "https://ing.com/news/2026/girotel-at-40-the-retro-tech-that-started-it-all.html"
ITALY = "https://ing.com/news/2026/ing-in-italy-marks-25-years-of-digital-banking-launches-private-banking.html"
SPAIN = "https://ing.com/news/2026/more-than-a-branch.html"
BUYBACK = "https://ing.com/news/press-releases/progress-on-share-buyback-programme-13oct26.html"
RUSSIA = "https://ing.com/news/press-releases/ing-has-terminated-sale-agreement-for-its-russian-business.html"
TFI = "https://ing.com/news/press-releases/ing-bank-slaski-completes-acquisition-of-goldman-sachs-tfi.html"
SINGULAR = "https://ing.com/news/press-releases/ing-accelerates-growth-in-private-banking-with-strategic-investment-in-leading-spanish-wealth-manager-singular-bank-6-july-2026.html"
TTB = "https://ing.com/news/press-releases/ing-reduces-its-stake-in-tmbthanachart-bank-18aug26.html"
EGM = "https://ing.com/news/press-releases/results-of-ings-extraordinary-general-meeting.html"
MGMT = "https://ing.com/news/press-releases/update-on-management-changes.html"
BANKEN = "https://www.banken.nl/nieuws/26615/pin-novatie-ing-markeert-40-jaar-pinnen-met-kaart-update"
ICULTURE = "https://www.iculture.nl/nieuws/apple-pay-kaart-vervangen/"
RADAR = "https://radar.avrotros.nl/artikel/ook-ing-klanten-krijgen-betaalkaarten-van-visa-25100"
TESTAANKOOP = "https://www.test-aankoop.be/geld/kredietkaarten/nieuws/afschaffing-maestro"
INGDE = "https://www.ing.de/girokonto/"
TONLINE = "https://www.t-online.de/finanzen/aktuelles/verbraucher/id_101374816/ing-bringt-erstmals-kreditkarte-heraus-wann-die-karte-erscheinen-soll.html"
PLDEBIT = "https://www.ing.pl/indywidualni/karty/karty-do-konta"
PLCREDIT = "https://www.ing.pl/indywidualni/karty/karty-kredytowe"
PLCARDS = "https://www.ing.pl/indywidualni/karty"
AUCARDS = "https://www.ing.com.au/credit-cards.html"
RO = "https://www.ing.ro/persoane-fizice"
SUBS = "https://ing.com/news/press-releases/ing-rolls-out-global-subscription-banking-model.html"
WERO = "https://ing.com/news/2026/wero-europes-new-way-to-pay.html"
WERODE = "https://ing.com/news/2026/wero-expands-to-online-shopping-in-germany.html"
EPI = "https://www.epicompany.eu/"
QIVALIS = "https://qivalis.eu/"
QIVALISING = "https://ing.com/news/2026/european-banks-rally-behind-a-euro-stablecoin.html"
AGENTIC = "https://ing.com/news/2026/ai-can-now-shop-for-you-if-you-let-it.html"
PRINCIPLES = "https://ing.com/news/2026/as-ai-starts-shopping-who-stays-in-control.html"
MORTGAGEAI = "https://ing.com/news/2026/how-ing-uses-agentic-ai-to-speed-up-mortgage-decisions.html"
BELGA = "https://www.belganewsagency.eu/maestro-debit-cards-to-disappear-in-belgium"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · heritage · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: more than 41 million customers and RoTE of 17% in 2Q26, a group formed in 1991 with Postbank's Girotel behind it, one data and AI environment, and an outlook raised in July 2026.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "41m customers, RoTE 17%.", "div": "group", "rev": "grp", "products": [
            P("balance", "Balance sheet & earnings", "Net result of €1,947 million in 2Q26 (RoTE 17.0%, CET1 13.1%) and €6,327 million in 2025 on income of €23.0 billion; more than 41 million customers, nearly 16 million of them mobile primary; ING Bank rated A+/A1/AA-; market value about €79 billion at 30 June 2026 ⚠ derived from the share count; 62,770 staff.",
              s=["con", "corp"], neo=[0, ""], src=[["2Q2026 results", Q2], ["FY2025 results", FY25], ["2025 Form 20-F", F20]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Van Rijswijk and Lerner.", "div": "group", "rev": "grp", "products": [
            P("leadership", "Boards & management", "CEO Steven van Rijswijk (since July 2020), CFO Ida Lerner (from April 2026), CRO Andrea Cesaroni (Executive Board from July 2026); Ljiljana Čortan runs Wholesale Banking and Pinar Abay Retail Banking, and sits on EPI's board; Hans Overeem leads payments ⚠ title varies; Karl Guha chairs the Supervisory Board.",
              s=["corp"], neo=[0, ""], src=[["ING: EGM results, Jul 2026", EGM], ["ING: management changes, Feb 2026", MGMT], ["2025 Form 20-F", F20]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "Formed in 1991.", "div": "group", "rev": "grp", "products": [
            P("heritage", "Heritage", "ING Groep incorporated on 4 March 1991 ⚠ from Nationale-Nederlanden and NMB Postbank; Postbank's Girotel home banking turned 40 in February 2026; in Italy since 1979, Conto Arancio since 2001, and digital-first in Spain for more than 25 years.",
              s=["con"], o="I", neo=[0, ""], src=[["2025 Form 20-F", F20], ["ING: Girotel at 40, Feb 2026", GIROTEL], ["ING: Italy at 25, May 2026", ITALY]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Data & AI", "blurb": "One agentic environment.", "div": "group", "rev": "grp", "products": [
            P("ai", "Data, AI & capability hubs", "A single data, analytics, AI and agentic environment with a central AI Risk Committee; five AI priorities (contact centres, KYC, hyper-personalisation, wholesale lending and software engineering); hubs in six countries and Madrid from November 2025; inbound contacts down 43% in 2025.",
              s=["corp"], st="new", neo=[0, ""], src=[["2025 Form 20-F", F20]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Outlook raised, July 2026.", "div": "group", "rev": "grp", "products": [
            P("strategy", "Growing the difference", "Aiming to be 'the best European bank': for 2026 income above €24.5 billion and RoTE above 15%, for 2027 income above €26 billion and RoTE above 16%; a 50% payout and a €1 billion buyback 93% done by 9 October 2026.",
              s=["corp"], neo=[0, ""], src=[["2Q2026 results", Q2], ["ING: buyback progress, Oct 2026", BUYBACK]]),
            P("deals", "Deals", "The rest of Goldman Sachs TFI bought by ING Bank Śląski (April 2026), about 40% of Singular Bank agreed (July 2026), the TMBThanachart stake cut to 11.6% (August 2026), and the Russian sale terminated (April 2026).",
              s=["aff", "corp"], o="A", st="flux", neo=[0, ""], src=[["ING: Goldman Sachs TFI, Apr 2026", TFI], ["ING: Singular Bank, Jul 2026", SINGULAR], ["ING: TTB stake, Aug 2026", TTB], ["ING: Russia, Apr 2026", RUSSIA]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Dutch debit reissued on Visa and Mastercard, Belgian debit on Bancontact and Mastercard, German debit on Visa with a first credit card coming, Polish cards on both, cards and acquiring elsewhere, Wero and iDEAL, and the Qivalis stablecoin and cash management.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Netherlands debit", "blurb": "10 million cards, two networks.", "div": "ingnl", "rev": "nl", "products": [
            P("nldebit", "New ING debit cards", "New Visa and Mastercard debit cards for private and business customers, nearly 10 million in all, announced in November 2025: new customers first, existing cards replaced soon; contactless ATM use via Apple Pay, Google Pay and Garmin Pay ⚠ split between networks not disclosed.", short="NL debit (Visa and Mastercard)",
              s=["con", "sme"], lc="everyday", st="flux", ay="Nov 2025", o="P", at="Visa, Mastercard", neo=[1, "Split between Visa and Mastercard ⚠ shares not disclosed."],
              mc="The biggest card decision in ING's home market, shared with Visa.",
              src=[["Banken.nl: new ING cards, Nov 2025", BANKEN], ["iCulture: Apple Pay card swap, Feb 2026", ICULTURE]]),
            P("maestro", "Maestro & V PAY", "Since 2018 new Dutch debit cards were assigned at random to Maestro or V PAY to avoid relying on one provider; Maestro cards stay usable until 2027 at the latest.", short="Maestro and V PAY (being replaced)",
              s=["con"], lc="everyday", st="retired", ay="Apr 2018", o="P", at="Mastercard, Visa", neo=[1, "Maestro and V PAY, split at random."], src=[["Radar: ING adds Visa, Apr 2018", RADAR]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Belgium debit", "blurb": "Bancontact and Mastercard.", "div": "ingbe", "rev": "be", "products": [
            P("bedebit", "Bancontact/Debit Mastercard", "ING Belgium's debit card, co-badged Bancontact for domestic use and Debit Mastercard in place of Maestro from 2023.", short="Belgium debit (Mastercard)",
              s=["con"], lc="everyday", ay="May 2023", o="P", at="Mastercard, Bancontact", neo=[1, "Debit Mastercard; Bancontact at home."],
              src=[["Test-Aankoop: Maestro ends, May 2023", TESTAANKOOP], ["Belga: Maestro to disappear", BELGA]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Germany cards", "blurb": "Visa debit, credit to come.", "div": "ingde", "rev": "de", "products": [
            P("dedebit", "ING VISA Card (debit)", "A Visa debit card free with the Girokonto.", short="Germany debit (Visa)",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["ING Germany: Girokonto", INGDE]]),
            P("girocard", "girocard", "An optional girocard at €1.49 a month ⚠ co-badge not known.",
              s=["con"], lc="everyday", neo=[0, "girocard ⚠ co-badge not known."], src=[["ING Germany: Girokonto", INGDE]]),
            P("decredit", "ING Germany credit card", "ING's first German credit card, 'highly prioritised' by CEO Lars Stoy and aimed at the Christmas season; fees and network not decided or disclosed.", short="Germany credit (network open)",
              s=["con"], lc="borrow", st="new", neo=[None, "Network not chosen."],
              mc="A greenfield network decision in a Visa-debit franchise.",
              src=[["t-online: ING credit card, Aug 2026", TONLINE]]),
        ]},
        {"id": "2.4", "ic": "earth", "name": "Poland cards", "blurb": "Visa debit, Mastercard Platinum.", "div": "slaski", "rev": "other", "products": [
            P("pldebit", "ING Bank Śląski debit & prepaid", "Moja Karta ING and multi-currency debit on Visa, a Visa virtual prepaid card, a Mastercard for the euro account and a Mastercard prepaid card from age 13.", short="Poland debit (mostly Visa)",
              s=["con"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Visa main debit; Mastercard for euro and prepaid."], src=[["ING Poland: debit cards", PLDEBIT]]),
            P("plcredit", "ING Bank Śląski credit cards", "A standard credit card in Visa or Mastercard (limits PLN 500–20,000) and a Platinum Mastercard with concierge and Priority Pass.", short="Poland credit (Visa and Mastercard)",
              s=["con", "aff"], lc="borrow", o="P", at="Mastercard, Visa", neo=[1, "Both; Platinum is Mastercard."], src=[["ING Poland: credit cards", PLCREDIT]]),
            P("plpay", "BLIK, Click to Pay & wallets", "BLIK, Apple Pay, Google Pay and Garmin Pay; online card payments support Click to Pay, and subscription payments can be blocked in Moje ING.",
              s=["con"], lc="move", o="P", at="BLIK", neo=[1, "Click to Pay alongside BLIK."], src=[["ING Poland: cards", PLCARDS]]),
        ]},
        {"id": "2.5", "ic": "globe", "name": "Other markets", "blurb": "Australia, Romania.", "div": "ingau", "rev": "other", "products": [
            P("aucards", "Orange One", "Low Rate ($48 a year) and Rewards Platinum ($149, 1% cashback up to $30 a month), with no ING FX fee and instalment plans ⚠ network not stated.",
              s=["con"], lc="borrow", neo=[None, "Network not stated."], src=[["ING Australia: credit cards", AUCARDS]]),
            P("rocards", "ING Romania cards & RoPay", "A virtual card, a credit card, ING Young for ages 10 to 18 and cards in Go, More and Extra plans ⚠ network not stated; RoPay instant payments with no commission.", div="group",
              s=["con"], lc="everyday", neo=[None, "Network not stated."], src=[["ING Romania", RO]]),
            P("roacquiring", "Merchant acquiring in Romania", "POS terminals, e-commerce and SoftPOS for businesses.", div="group",
              s=["sme"], lc="move", neo=[None, "Schemes not stated."], src=[["ING Romania", RO]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Wero & iDEAL", "blurb": "ING co-owns EPI.", "div": "group", "rev": "grp", "products": [
            P("wero", "Wero in Belgium & Germany", "Person-to-person in Belgium since November 2024 (more than 1 million ING users) with e-commerce from January 2026; in Germany since August 2025 (about 600,000 activations) with online shopping from June 2026 and shops next.",
              s=["con", "sme"], lc="move", st="new", ay="Jun 2026", o="P", at="EPI", neo=[0, "EPI's own."],
              mc="The main threat to card volume in ING's three biggest retail markets.",
              src=[["ING: Wero, Feb 2026", WERO], ["ING: Wero online in Germany, Jun 2026", WERODE]]),
            P("ideal", "iDEAL to Wero", "iDEAL and Wero co-branded from 2026, with purchase protection on iDEAL by end-2026, Wero at ING Netherlands in Q4 2026 and full migration by end-2027.", div="ingnl",
              s=["con", "sme"], lc="move", st="flux", o="P", at="EPI", neo=[0, "EPI's own."], src=[["ING: Wero, Feb 2026", WERO], ["ING: Wero online in Germany, Jun 2026", WERODE]]),
            P("epi", "EPI", "ING is a shareholder in EPI, whose Wero has about 48 million users and plans links with Bancomat, Bizum, SIBS MB WAY and Vipps MobilePay by 2027.",
              s=["con"], lc="move", o="P", at="EPI", neo=[0, ""], src=[["EPI Company", EPI], ["ING: Wero, Feb 2026", WERO]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Stablecoins & cash management", "blurb": "Qivalis, licensed.", "div": "ingwb", "rev": "wb", "products": [
            P("qivalis", "Qivalis", "A euro stablecoin issuer ING co-founded with 11 banks, now 37 banks in 15 countries; licensed as an e-money institution by DNB on 14 October 2026 and due to launch later in 2026.",
              s=["corp"], lc="move", st="new", ay="Oct 2026", o="P", at="Qivalis", neo=[0, "Mastercard's role unknown."],
              mc="Multi-token settlement could connect Qivalis to cards.",
              src=[["Qivalis", QIVALIS], ["ING: euro stablecoin, May 2026", QIVALISING]]),
            P("pcm", "Payments & cash management", "Inside Daily Banking & Trade Finance (€503 million of income in 2Q26), with growing mandates and cash pooling; electronic bills of lading cutting transfer times from weeks to minutes.",
              s=["corp"], lc="move", neo=[0, ""], src=[["2Q2026 results", Q2], ["FY2025 results", FY25]]),
            P("cryptoetp", "Crypto ETPs", "Exchange-traded crypto products in self-managed investment accounts in five markets from January 2026.", div="group",
              s=["aff"], lc="grow", st="new", neo=[0, ""], src=[["FY2025 results", FY25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: an agentic payment with Mastercard and Worldline and principles for agentic commerce, AI monitoring and due diligence, chatbots and an agentic mortgage assistant, and subscription plans for 3 million customers.",
    "tiles": [
        {"id": "3.1", "ic": "bot", "name": "Agentic commerce", "blurb": "A pilot with Mastercard.", "div": "ingnl", "rev": "nl", "products": [
            P("agentpilot", "Agentic payment pilot", "A customer bought Concertgebouw Orchestra tickets through an AI assistant, with Mastercard and Worldline on infrastructure based entirely in Europe (Money20/20 Amsterdam, 2 June 2026) ⚠ Agent Pay not named.", short="Agentic pilot (Mastercard)",
              s=["con"], lc="everyday", st="new", ay="Jun 2026", o="P", at="Mastercard, Worldline", neo=[2, "With Mastercard and Worldline ⚠ product not named."],
              mc="Mastercard's clearest new opening at ING.",
              src=[["ING: AI can now shop for you, Jun 2026", AGENTIC]]),
            P("principles", "Agentic commerce principles", "Five principles (transparency, safety, privacy and data, choice and interoperability) with NatWest, ASB, Bank of America, Capital One and CBA (22 September 2026); the networks are not signatories, and ING names work with Worldline, Mastercard and Visa.", div="group",
              s=["con"], lc="everyday", st="new", ay="Sep 2026", neo=[0, "Banks only; Visa also named."], src=[["ING: who stays in control, Sep 2026", PRINCIPLES]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud & KYC", "blurb": "AI monitoring in four markets.", "div": "group", "rev": "grp", "products": [
            P("monitoring", "Transaction monitoring & due diligence", "AI transaction monitoring in Belgium, the Netherlands, Romania and Australia, and AI-driven customer due diligence (STP 2.0 and a risk assessment model).",
              s=["con", "corp"], lc="everyday", neo=[0, "ING's own."],
              mc="Wero needs purchase protection; fraud tools could cover A2A as well as cards.",
              src=[["2025 Form 20-F", F20]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "AI for customers", "blurb": "Chatbots, agentic mortgages.", "div": "group", "rev": "grp", "products": [
            P("chatbots", "GenAI chatbots & personalisation", "Generative-AI chatbots in seven markets (Australia from 4Q25), AI marketing in five, and financial-wellbeing scoring in the Netherlands.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["2025 Form 20-F", F20], ["FY2025 results", FY25]]),
            P("mortgageai", "Agentic mortgage assistant", "An agentic AI assistant for Dutch mortgage decisions, piloted from March 2026 and scaling, with a person making the final call; in Germany a fully digital mortgage decided in under 30 minutes.", div="ingnl",
              s=["home"], lc="borrow", st="new", neo=[0, ""], src=[["ING: agentic AI mortgages, Jun 2026", MORTGAGEAI], ["2Q2026 results", Q2]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Subscriptions & perks", "blurb": "3 million on plans.", "div": "group", "rev": "grp", "products": [
            P("subs", "ING Go, More, Extra & Max", "Subscription plans in nine markets (the Netherlands from 10 June 2026) for 3 million customers, bundling streaming, travel, loyalty, cashback, insurance and an enhanced debit-and-credit card option.",
              s=["con", "aff"], lc="everyday", st="new", ay="Jun 2026", neo=[None, "Card network in plans not stated."],
              mc="Card benefits and premium tiers could fill the plans.",
              src=[["ING: subscription banking, Jun 2026", SUBS]]),
            P("perks", "Pocket Perks", "Cashback offers on ING Australia cards.", div="ingau",
              s=["con"], lc="grow", neo=[None, "Network not stated."], src=[["ING Australia: credit cards", AUCARDS]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: everyday banking and mortgages in ten retail markets, Business Banking spreading to Italy and Spain, €322 billion of private banking and wealth assets, and Wholesale Banking.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Private individuals", "blurb": "41 million in ten markets.", "div": "group", "rev": "nl", "products": [
            P("retail", "Retail banking & mortgages", "About 41 million customers in the Netherlands, Belgium, Luxembourg, Germany, Spain, Italy, Türkiye, Poland, Romania and Australia; mortgages up €7.1 billion in 2Q26; first for NPS in five of nine markets; Luxembourg retail being phased out.",
              s=["con", "home"], lc="everyday", neo=[1, "Mastercard in Belgium and part of NL; Visa in Germany."], src=[["2025 Form 20-F", F20], ["2Q2026 results", Q2]]),
            P("upgrader", "ING Upgrader", "A Dutch home-retrofit platform run with partners.", div="ingnl",
              s=["home"], lc="beyond", o="P", neo=[0, ""], src=[["2Q2026 results", Q2]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Business Banking", "blurb": "Into Italy and Spain.", "div": "group", "rev": "other", "products": [
            P("business", "Business Banking", "Nine markets, Italy from January 2026 and Spain planned for 2027, digital onboarding and instant lending in six; business lending up €4.2 billion in 2Q26.",
              s=["sme"], lc="borrow", st="new", neo=[None, "Commercial-card data not public ⚠."],
              mc="Commercial and virtual cards for the Italy and Spain launches.",
              src=[["2025 Form 20-F", F20], ["2Q2026 results", Q2], ["ING: Spain flagship, Oct 2026", SPAIN]]),
        ]},
        {"id": "4.3", "ic": "gem", "name": "Private banking & wealth", "blurb": "€322bn under management.", "div": "group", "rev": "other", "products": [
            P("wealth", "Private Banking & Wealth Management", "€322 billion under management (up 27%); private banking in the Netherlands, Belgium, Luxembourg and Poland, Italy from Q3 2026 and Spain later in 2026, with Goldman Sachs TFI and the Singular Bank stake.",
              s=["aff"], lc="grow", st="new", neo=[0, ""], src=[["2Q2026 results", Q2], ["ING: Italy at 25, May 2026", ITALY]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "Wholesale Banking", "blurb": "€1.9bn a quarter.", "div": "ingwb", "rev": "wb", "products": [
            P("wholesale", "Wholesale Banking", "Lending (€860 million in 2Q26), Daily Banking & Trade Finance (€503 million) and Financial Markets (€418 million); a private-markets unit and a capital-markets build-out; client NPS of 77.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["2Q2026 results", Q2], ["2025 Form 20-F", F20]]),
            P("sustainable", "Sustainable finance", "€166 billion mobilised in 2025 and €86.5 billion in the first half of 2026.",
              s=["corp"], lc="beyond", neo=[0, ""], src=[["FY2025 results", FY25], ["2Q2026 results", Q2]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: mobile first for 87% of customers, InsideBusiness for companies, a new Madrid flagship, and contact centres led by generative AI.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps & portals", "blurb": "87% mobile-first.", "div": "group", "rev": "grp", "products": [
            P("apps", "ING apps", "87% of customers chose mobile as their main channel in 2025 and digital platforms had 8.8 billion visits; OneApp in Australia, Moje ING in Poland, Home'Bank and Business OneApp in Romania.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["2025 Form 20-F", F20], ["FY2025 results", FY25]]),
            P("insidebusiness", "InsideBusiness", "The Wholesale Banking self-service portal, with more journeys added in 2025.", div="ingwb",
              s=["corp"], lc="open", neo=[0, ""], src=[["2025 Form 20-F", F20]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & contact centres", "blurb": "A Madrid flagship.", "div": "group", "rev": "other", "products": [
            P("branches", "Branches", "A new Madrid flagship at Plaza de Colón for retail and private banking, about 800 visitors a day, serving about 5 million customers in Spain.",
              s=["con", "aff"], lc="open", st="new", ay="Oct 2026", neo=[0, ""], src=[["ING: Spain flagship, Oct 2026", SPAIN]]),
            P("contact", "Contact centres", "Led by generative AI, with inbound contacts down 43% in 2025.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["2025 Form 20-F", F20]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at ING", "blurb": "Belgium, half of NL, an agent.", "products": [
        P("mcating", "Mastercard at ING", "Mastercard carries ING Belgium's debit alongside Bancontact, shares the reissue of about 10 million Dutch debit cards with Visa, holds Platinum credit, euro and prepaid cards in Poland, and ran ING's first agentic payment with Worldline in June 2026. Visa holds German debit and Polish main debit; ING's first German credit card has no network yet. ING has dual-sourced Dutch debit since 2018 and co-owns Wero.",
          s=["con"], div="group", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Banken.nl: new ING cards, Nov 2025", BANKEN], ["ING: AI can now shop for you, Jun 2026", AGENTIC], ["Radar: ING adds Visa, Apr 2018", RADAR]]),
    ]},
    {"id": "pillar-market", "name": "European banking", "blurb": "Wero, iDEAL, stablecoins.", "products": [
        P("market", "The market", "iDEAL becoming Wero by end-2027, Wero links to Bizum, Bancomat, MB WAY and Vipps MobilePay, domestic schemes (Bancontact, girocard, BLIK, RoPay), the EU AI Act and PSD3, Poland's higher bank tax, and Qivalis under MiCA ⚠.",
          s=["con"], div="group", rev="grp", src=[["ING: Wero, Feb 2026", WERO], ["2025 Form 20-F", F20], ["Qivalis", QIVALIS]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
