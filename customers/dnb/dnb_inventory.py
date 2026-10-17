"""DNB's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the Q2 2026 report (14 July 2026), the
August 2026 debt-investor presentation and the 2025 annual report (March 2026). Q3 2026 results are
due on 21 October 2026. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own
product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://ir.dnb.no/sites/default/files/pr/202607138455-2.pdf"
Q2PR = "https://mfn.se/all/a/dnb-bank/dnb-bank-asa-solide-resultater-drevet-av-utlansvekst-og-hoy-kundeaktivitet-c61deb2e"
DEBT = "https://www.ir.dnb.no/sites/default/files/260805%20DNBBank%20-%20DNB%20Boligkreditt.pdf"
AR25 = "https://www.ir.dnb.no/sites/default/files/arsrapport_2025_DNB_konsernet.pdf"
IR = "https://www.ir.dnb.no/"
OMOSS = "https://www.dnb.no/om-oss"
TS = "https://www.ir.dnb.no/press-and-reports/press-releases/dnb-making-organisational-changes-technology-services-2485833"
CARNEGIE = "https://www.ir.dnb.no/press-and-reports/press-releases/dnb-bank-asa-acquires-carnegie-accelerates-nordic-strategy-and"
CARNEGIE_DONE = "https://www.carnegie.se/en/news/carnegie-holding-ab-announces-completion-of-acquisition-by-dnb-bank-asa/"
PLUSS = "https://www.dnb.no/en/card/pluss"
SAGA = "https://www.dnb.no/en/card/saga"
DNBMC = "https://www.dnb.no/en/card/dnb-mastercard"
PB = "https://www.dnb.no/en/card/private-banking"
CIRCLEK = "https://www.dnb.no/en/card/creditcard/circle-k"
PRICELESS = "https://www.dnb.no/kort/kredittkort/mastercard/priceless"
BIZCARDS = "https://www.dnb.no/en/business/daily-banking/cards"
CORPMC = "https://www.dnb.no/en/business/daily-banking/cards/corporate-mastercard"
CORPTERMS = "https://content.dnb.no/docs/7832669/kontovilkr-dnb-corporate-mastercard-firmaansvar.pdf"
VISAPARTNER = "https://www.dnb.no/dnbnyheter/no/bedrift/kortendringer-for-partner-visa"
DEBITTERMS = "https://content.dnb.no/docs/8611244/vilk-r-debet-bankkort.pdf"
APPLEPAY = "https://www.dnb.no/dnbnyheter/no/samfunn/dnb-vil-tilby-applepay-til-norske-kunder"
GOOGLEPAY = "https://www.dnb.no/dagligbank/betaling/kontaktlos/google-pay"
VIPPSTERM = "https://www.dnb.no/dnbnyheter/no/din-okonomi/sjekk-ut--vipps-i-terminal----mobilbetaling-med-qr-kode"
NB25 = "https://www.norges-bank.no/en/news-events/publications/retail-payment-services/retail-payment-services-2025/web-report-retail-payment-services-2025/"
BITS = "https://thepaypers.com/payments-general/mastercard-extends-partnership-with-bits--1273492"
NETS = "https://www.nets.eu/Media-and-press/news/Pages/DNB-extends-partnership-with-Nets.aspx"
TWO = "https://www.two.inc/resources/two-cents-blog/two-partners-with-dnb-to-launch-ai-powered-b2b-payments-across-the-nordics"
DEV = "https://developer.dnb.no/"
OECD = "https://konkurransetilsynet.no/wp-content/uploads/2025/09/oecd-bidrag-om-mobile-betalingslosninger-2025.pdf"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · state stake · brands", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: about a quarter of Norwegian banking, NOK 2.3 trillion of loans and ROE near 15%, a 34% state shareholder and AA ratings, roots going back to 1822, cloud payments and agentic AI, and targets to 2027.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "ROE 14.6%, CET1 17.4%.", "div": "group", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Loans to customers of NOK 2,332 billion and deposits of NOK 1,605 billion at 30 June 2026; profit of NOK 9.8 billion in Q2 2026 (ROE 14.6%, cost/income 40.3%) and NOK 43.6 billion in 2025 (ROE 15.9%); CET1 17.4%. About 25% of the Norwegian market.",
              s=["con", "corp"], neo=[0, ""], src=[["DNB: Q2 2026 report", Q2], ["DNB: 2025 annual report", AR25], ["DNB: debt-investor presentation, Aug 2026", DEBT]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "34% state-owned; Braathen.", "div": "group", "rev": "other", "products": [
            P("owners", "Ownership & ratings", "Listed on Oslo Børs and about 34% owned by the Norwegian state; rated Aa2 by Moody's and AA- by S&P, both stable; 1.44 billion shares after the June 2026 cancellation. Market value not checked ⚠.",
              s=["corp"], neo=[0, ""], src=[["DNB: debt-investor presentation, Aug 2026", DEBT], ["DNB: Q2 2026 report", Q2]]),
            P("leadership", "Board & group management", "Chair Olaug Svarva; CEO Kjerstin R. Braathen (since 2019, also chair of Vipps MobilePay); CFO Rasmus T. Figenschou; Maria Ervik Løvold (personal), Marianne Wik Sætre (SME), Harald Serck-Hanssen (large corporates), Alexander Opstad (DNB Carnegie), Per Kristian Næss-Fladset (products, data and innovation).",
              s=["corp"], neo=[0, ""], src=[["DNB: 2025 annual report", AR25]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brands", "blurb": "Since 1822; DNB and Sbanken.", "div": "group", "rev": "pm", "products": [
            P("brands", "Heritage & brands", "Roots going back to 1822, the DnB and Gjensidige NOR merger, and Nordlandsbanken and Sbanken bought since; today DNB and Sbanken for personal customers, DNB Carnegie, DNB Eiendom, DNB Finans and DNB Livsforsikring. About 10,800 full-time equivalents.",
              s=["con"], o="I", neo=[0, ""], src=[["DNB: about us", OMOSS], ["DNB: 2025 annual report", AR25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Cloud payments, agentic AI.", "div": "group", "rev": "other", "products": [
            P("tech", "Core, cloud & data", "Critical payment systems moved to cloud-based platforms in 2025; more than 400 million payment transactions a day pass through DNB's systems; AI tools in standard software for every employee.",
              s=["corp"], neo=[0, ""], src=[["DNB: 2025 annual report", AR25]]),
            P("agentic", "Agentic AI & restructuring", "Agentic AI in customer-data control, KYC and coding; Technology & Services to cut about 400 full-time equivalents, with costs in Q4 2026 (announced 6 October 2026).",
              s=["corp"], st="new", ay="Oct 2026", neo=[0, ""],
              mc="DNB is putting AI agents to work; Agent Pay is untested ground.",
              src=[["DNB: Technology & Services changes, Oct 2026", TS]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "ROE above 14% to 2027.", "div": "group", "rev": "other", "products": [
            P("strategy", "Targets 2025–2027", "ROE above 14%, cost/income below 40%, CET1 above 16.4% and a payout above 50%, set at the November 2024 Capital Markets Day; Sweden is the second home market. A new Capital Markets Day is set for 10 November 2026.",
              s=["corp"], neo=[0, ""], src=[["DNB: debt-investor presentation, Aug 2026", DEBT], ["DNB investor relations", IR]]),
            P("deals", "Deals", "Carnegie bought for about SEK 12 billion (agreed October 2024, completed March 2025), Sbanken (2022), and the 19.95% stake in Luminor agreed for sale to OTP Bank (July 2026, about NOK 1 billion loss in Q3).",
              s=["corp", "inv"], o="A", st="flux", neo=[0, ""], src=[["DNB: Carnegie acquisition, Oct 2024", CARNEGIE], ["Carnegie: completion, Mar 2025", CARNEGIE_DONE], ["DNB: debt-investor presentation, Aug 2026", DEBT]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: BankAxept and Visa debit, a credit range that is all Mastercard, Visa Business and a Corporate Mastercard issued by SEB Kort, Apple Pay, Google Pay and Vipps MobilePay, instant payments cleared by Mastercard for Bits, and B2B checkout credit with Two.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "BankAxept and Visa.", "div": "dnb", "rev": "pm", "products": [
            P("debit", "DNB & Sbanken debit card", "The bank card in every personal package carries BankAxept, Norway's domestic scheme, and Visa; Pluss and SAGA cost NOK 295 a year. DNB's 2025 terms say the schemes offer Click to Pay and that DNB sends card updates to Visa.", short="Debit (BankAxept + Visa)",
              s=["con"], lc="everyday", o="P", at="BankAxept, Visa", neo=[0, "BankAxept and Visa."],
              mc="The largest card franchise in Norway sits with Visa and BankAxept.",
              src=[["DNB: Pluss", PLUSS], ["DNB: debit card terms, Apr 2025", DEBITTERMS]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "All Mastercard.", "div": "dnb", "rev": "pm", "products": [
            P("mccredit", "DNB, Pluss, Ung & SAGA Mastercard", "Every DNB consumer credit card is a Mastercard: up to 45 days interest-free, travel insurance, fuel and EV-charging discounts, limits up to NOK 150,000 on SAGA, and a paid Mastercard Upgrade with SAS EuroBonus points and lounges.", short="Credit (Mastercard)",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's core at DNB: the whole consumer credit book.",
              src=[["DNB: DNB Mastercard", DNBMC], ["DNB: SAGA", SAGA], ["DNB: Pluss", PLUSS]]),
            P("pbcard", "Private Banking World Elite Mastercard", "For customers with at least NOK 6 million to invest: World Elite Mastercard with 2% fuel and 10% EV-charging discounts, Priceless, Mastercard Security Fast Track, concierge and lounges, in a package at NOK 250 a month.", short="World Elite Mastercard",
              s=["aff"], lc="grow", o="P", at="Mastercard", neo=[2, "Mastercard World Elite."],
              src=[["DNB: Private Banking cards", PB]]),
        ]},
        {"id": "2.3", "ic": "briefcase-business", "name": "Business cards", "blurb": "Visa debit, Mastercard credit.", "div": "dnb", "rev": "bmn", "products": [
            P("visabiz", "Visa Business", "The business debit card, Visa-only since October 2022 when it replaced BankAxept-and-Visa Partner cards; a separate BankAxept business card handles cash deposits.", short="Visa Business",
              s=["sme"], lc="everyday", ay="Oct 2022", o="P", at="Visa", neo=[0, "Visa."],
              src=[["DNB Nyheter: Visa Partner replaced, Oct 2022", VISAPARTNER], ["DNB: business cards", BIZCARDS]]),
            P("corpmc", "DNB Corporate Mastercard", "A company-liability credit card for firms with up to 250 employees, from NOK 350 a year, with the Corporate Card app, travel insurance and Avis discounts; issued by SEB Kort in cooperation with DNB. Larger groups are offered other Mastercard solutions.", short="Corporate Mastercard",
              s=["sme", "corp"], lc="move", o="P", at="SEB Kort, Mastercard", neo=[2, "Mastercard, issued by SEB Kort."],
              mc="Mastercard commercial cards, but the issuing sits with SEB Kort.",
              src=[["DNB: Corporate Mastercard", CORPMC], ["DNB Corporate Mastercard terms, Apr 2020", CORPTERMS]]),
            P("virtual", "Purchase account (virtual card)", "A virtual credit card for online purchases with all spending on one invoice. Network and issuer not stated ⚠.",
              s=["sme"], lc="move", st="unconf", neo=[None, "Network not stated ⚠."], src=[["DNB: business cards", BIZCARDS]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Wallets & Vipps", "blurb": "Apple Pay, Vipps MobilePay.", "div": "vipps", "rev": "pm", "products": [
            P("wallets", "Apple Pay, Google Pay & wearables", "Google Pay since May 2019 and Apple Pay for all DNB and Sbanken customers since 10 December 2024, for Visa and Mastercard cards; Garmin Pay, Fitbit Pay, Swatch Pay and Fidesmo on Corporate Mastercard.", short="Apple & Google Pay",
              s=["con", "sme"], lc="everyday", ay="Dec 2024", o="P", at="Apple, Google", neo=[1, "Tokens for Visa debit and Mastercard credit."],
              src=[["DNB Nyheter: Apple Pay, Dec 2024", APPLEPAY], ["DNB: Google Pay", GOOGLEPAY], ["DNB: Corporate Mastercard", CORPMC]]),
            P("vipps", "Vipps MobilePay", "The Nordic wallet that dominates Norwegian person-to-person payments; DNB owns 47.3% of Vipps Holding and its CEO chairs Vipps MobilePay. Vipps NFC launched in December 2024 and international cards work in Vipps from autumn 2025.", short="Vipps MobilePay",
              s=["con", "sme"], lc="move", o="P", at="Vipps MobilePay", neo=[1, "Carries BankAxept and international cards."],
              mc="DNB's own stake in the wallet that competes with card-scheme wallets at the till.",
              src=[["DNB: 2025 annual report", AR25], ["Norges Bank: retail payment services 2025", NB25], ["DNB Nyheter: Vipps i terminal, Jul 2020", VIPPSTERM]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Instant payments & processing", "blurb": "NICS cleared by Mastercard.", "div": "group", "rev": "other", "products": [
            P("instant", "Instant & interbank payments", "Norwegian instant payments (210 million in 2025, NOK 135 billion) run over NICS Real; Bits, chaired by DNB's Per Kristian Næss-Fladset, renewed Mastercard as NICS clearing provider in May 2025.", short="Instant payments (NICS)",
              s=["con", "sme", "corp"], lc="move", o="P", at="Bits, Mastercard", neo=[1, "Mastercard clears NICS for Bits."],
              src=[["Norges Bank: retail payment services 2025", NB25], ["The Paypers: Mastercard and Bits, May 2025", BITS], ["DNB: 2025 annual report", AR25]]),
            P("nets", "Card processing with Nets", "A framework agreement with Nets (now Nexi), extended in February 2019, covers card processing, payment services and value-added card services.",
              s=["con"], lc="move", ay="Feb 2019", o="P", at="Nets", neo=[0, "Nets (Nexi)."], src=[["Nets: DNB extends partnership, Feb 2019", NETS]]),
        ]},
        {"id": "2.6", "ic": "hand-coins", "name": "B2B checkout & FX", "blurb": "BNPL with Two.", "div": "dnb", "rev": "bmn", "products": [
            P("two", "B2B Buy Now, Pay Later with Two", "Net 30, 60 or 90-day terms at checkout for Nordic webshops and marketplaces, with AI credit checks and same-day settlement; credit risk shared by DNB and Two (announced 23 March 2026).", short="B2B BNPL (Two)",
              s=["sme"], lc="borrow", st="new", ay="Mar 2026", o="P", at="Two", neo=[0, "Invoice credit, not cards."],
              mc="B2B credit at checkout where virtual cards could also play.",
              src=[["Two: partnership with DNB, Mar 2026", TWO]]),
            P("fx", "Currency & cross-border", "A leading currency bank, trading more than 170 currency pairs, with offices in 17 countries; cards abroad carry a 1.75% currency fee.",
              s=["corp", "sme"], lc="move", neo=[0, ""], src=[["DNB: about us", OMOSS], ["DNB: business cards", BIZCARDS]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud teams that stopped NOK 3 billion of NOK 3.3 billion attempted in 2025, the Aino AI chatbot, open-banking APIs and BankID, and customer programmes with fuel discounts and Priceless tickets on Mastercard.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & financial crime", "blurb": "NOK 3bn stopped in 2025.", "div": "group", "rev": "pm", "products": [
            P("fraud", "Fraud prevention & AML", "Criminals tried to take NOK 3.3 billion from DNB customers in 2025, up 30%; DNB stopped NOK 3.0 billion, nine kroner in ten. 5,032 customers were hit and 4,572 cases were reported to Økokrim. Vendors not public ⚠.",
              s=["con", "sme"], lc="everyday", neo=[None, "Vendors not public ⚠."],
              mc="Scam losses up 30% a year with no Mastercard fraud tool in public view.",
              src=[["DNB: 2025 annual report", AR25]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI for customers", "blurb": "Aino answers 1.5m.", "div": "dnb", "rev": "pm", "products": [
            P("aino", "Aino chatbot", "A generative-AI chatbot that answered more than 1.5 million personal-customer enquiries in 2025, alongside 3.5 million calls and chats.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["DNB: 2025 annual report", AR25]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "Open banking & identity", "blurb": "APIs and BankID.", "div": "group", "rev": "other", "products": [
            P("apis", "DNB Developer & open banking", "PSD2 and other APIs on the DNB Developer portal; open banking sits in the Products, Data & Innovation area. Contents not reviewed ⚠.",
              s=["sme", "corp"], lc="open", st="unconf", neo=[None, ""], src=[["DNB Developer", DEV], ["DNB: 2025 annual report", AR25]]),
            P("bankid", "BankID & onboarding", "Customers sign in and sign with BankID, which joined Vipps and BankAxept in a 2018 merger; a new digital service sets up a company and its bank account in one process, about 20 days faster.",
              s=["con", "sme"], lc="open", o="P", at="BankID", neo=[0, ""], src=[["Konkurransetilsynet: OECD note on mobile payments, 2025", OECD], ["DNB: 2025 annual report", AR25]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Loyalty & offers", "blurb": "Fuel discounts, Priceless.", "div": "dnb", "rev": "pm", "products": [
            P("programmes", "Pluss, SAGA & Private Banking programmes", "Customer programmes with partner discounts, insurance discounts and advice; SAGA adds lounges and Private Banking a concierge and year-round travel insurance.",
              s=["con", "aff"], lc="grow", neo=[1, "Benefits run through the Mastercard credit card."], src=[["DNB: Pluss", PLUSS], ["DNB: Private Banking cards", PB]]),
            P("circlek", "Fuel & charging discounts", "Up to 138 øre a litre off fuel at Circle K in the welcome period, plus a DNB discount of 1% to 2% when paid with a DNB Mastercard, and 6% to 10% off EV charging.", short="Circle K discounts",
              s=["con"], lc="everyday", o="P", at="Circle K", neo=[2, "Paid only on DNB Mastercard."],
              src=[["DNB: Circle K discount", CIRCLEK], ["DNB: DNB Mastercard", DNBMC]]),
            P("priceless", "Priceless presales", "DNB Mastercard holders get Mastercard Presale and Preferred tickets for concerts through Mastercard's Live Nation partnership, with shows listed into 2027.", short="Priceless",
              s=["con"], lc="beyond", o="P", at="Mastercard, Live Nation", neo=[3, "Mastercard's own programme."],
              src=[["DNB: Priceless concerts", PRICELESS]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: everyday banking packages, a quarter of Norway's mortgages and its biggest estate agent, the country's largest fund house and pension provider, banking for one company in three, large corporate and shipping lending, DNB Finans and DNB Carnegie.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Everyday banking", "blurb": "2.4m personal customers.", "div": "dnb", "rev": "pm", "products": [
            P("packages", "Accounts & packages", "Current accounts for 2.4 million personal customers in Norway in packages for children, youth, Ung (18–28), Pluss, SAGA and Private Banking; 28% of personal deposits.",
              s=["con"], lc="everyday", neo=[1, "Visa debit, Mastercard credit."], src=[["DNB: 2025 annual report", AR25], ["DNB: Pluss", PLUSS]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Mortgages & property", "blurb": "24% of mortgages.", "div": "dnb", "rev": "pm", "products": [
            P("mortgages", "Mortgages", "About 24% of Norwegian mortgages and 22.2% of household credit (May 2026), funded partly through DNB Boligkreditt's AAA covered bonds.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["DNB: Q2 2026 report", Q2], ["DNB: 2025 annual report", AR25]]),
            P("eiendom", "DNB Eiendom", "The group's estate agency: 19,005 homes sold in 2025, about 14% of the market, and a 14.4% share in Q2 2026.",
              s=["home"], lc="beyond", neo=[0, ""], src=[["DNB: 2025 annual report", AR25], ["DNB: Q2 2026 report", Q2]]),
        ]},
        {"id": "4.3", "ic": "coins", "name": "Savings, wealth & pensions", "blurb": "NOK 1.8trn under management.", "div": "wm", "rev": "pm", "products": [
            P("wealth", "Funds & asset management", "Record assets under management of NOK 1,782 billion and a record NOK 46 billion net inflow in Q2 2026; 39% of Norwegian mutual-fund savings, through DNB Asset Management and Carnegie Fonder.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["DNB: Q2 2026 report", Q2], ["DNB: Q2 2026 release", Q2PR]]),
            P("pension", "DNB Livsforsikring", "Norway's leading pension provider: about 1.4 million personal customers and 33,000 company agreements at end-2025.",
              s=["aff", "sme"], lc="grow", neo=[0, ""], src=[["DNB: 2025 annual report", AR25]]),
            P("privatebanking", "Private Banking", "For clients with at least NOK 6 million to invest, in Norway and through DNB Luxembourg; market leader for clients with advanced advisory needs in Q2 2026.",
              s=["aff"], lc="grow", neo=[1, "World Elite Mastercard."], src=[["DNB: Private Banking cards", PB], ["DNB: Q2 2026 report", Q2]]),
        ]},
        {"id": "4.4", "ic": "briefcase", "name": "SME banking", "blurb": "One company in three.", "div": "dnb", "rev": "bmn", "products": [
            P("sme", "Corporate customers Norway", "About 244,000 corporate customers, the bank for one Norwegian company in three; 33% of corporate deposits; SME lending up 2.0% in Q2 2026.",
              s=["sme"], lc="borrow", neo=[1, "Visa Business debit; Corporate Mastercard credit."], src=[["DNB: about us", OMOSS], ["DNB: Q2 2026 release", Q2PR], ["DNB: 2025 annual report", AR25]]),
        ]},
        {"id": "4.5", "ic": "earth", "name": "Large corporates & finance", "blurb": "Shipping, energy, seafood.", "div": "finans", "rev": "lci", "products": [
            P("lci", "Large corporates & international", "The largest corporates, international clients and financial institutions, specialising in energy, shipping, seafood, healthcare and TMT; lending up 8.7% year on year in Q2 2026.",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="Commercial cards beyond the 250-employee limit of the SEB Kort card.",
              src=[["DNB: Q2 2026 release", Q2PR], ["DNB: 2025 annual report", AR25]]),
            P("finans", "DNB Finans", "Car and asset finance and leasing across the Nordics, a separate subsidiary since January 2026; 81% of car loans to personal customers are sold digitally.",
              s=["con", "sme"], lc="borrow", st="new", ay="Jan 2026", neo=[0, ""], src=[["DNB: 2025 annual report", AR25], ["DNB: debt-investor presentation, Aug 2026", DEBT]]),
        ]},
        {"id": "4.6", "ic": "chart-candlestick", "name": "DNB Carnegie", "blurb": "Nordic investment bank.", "div": "carnegie", "rev": "lci", "products": [
            P("carnegie", "DNB Carnegie", "DNB Markets and Carnegie combined from March 2025: the most active equity capital markets bank in Western Europe by deals this year to 7 July 2026, and top of the Extel survey for the tenth year.",
              s=["inv", "corp"], lc="grow", st="new", ay="Mar 2025", o="A", neo=[0, ""], src=[["DNB: Q2 2026 report", Q2], ["Carnegie: completion, Mar 2025", CARNEGIE_DONE]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach DNB: the mobile bank and the Spare app, Sbanken for digital-first customers, business apps, and 52 branch offices.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Mobile bank & Spare", "blurb": "1.3m active users.", "div": "dnb", "rev": "pm", "products": [
            P("app", "DNB mobile bank", "1.3 million active users, about 30% of Norwegians over 17; 71% of personal transfers are made in the app, rated 4.7 in the App Store.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["DNB: debt-investor presentation, Aug 2026", DEBT], ["DNB: about us", OMOSS]]),
            P("spare", "Spare savings app", "Norway's largest savings platform by DNB's count, with 730,000 users (November 2024) and 65% of DNB's fund purchases.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["DNB: debt-investor presentation, Aug 2026", DEBT]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Sbanken", "blurb": "The digital brand.", "div": "sbanken", "rev": "pm", "products": [
            P("sbanken", "Sbanken from DNB", "A fully digital second brand for customers who want to bank online, part of DNB since 2022; Sbanken customers got Apple Pay back in December 2024.",
              s=["con"], lc="everyday", o="A", neo=[None, "Card network not confirmed ⚠."], src=[["DNB: 2025 annual report", AR25], ["DNB Nyheter: Apple Pay, Dec 2024", APPLEPAY]]),
        ]},
        {"id": "5.3", "ic": "briefcase-business", "name": "Business apps", "blurb": "SME users up 111%.", "div": "dnb", "rev": "bmn", "products": [
            P("bizapp", "DNB Bedrift & Corporate Card apps", "The DNB Bedrift mobile app, whose active users have grown 111% since 2022, and SEB Kort's Corporate Card app for DNB Corporate Mastercard holders.",
              s=["sme"], lc="everyday", neo=[1, "Corporate Card app serves the Mastercard card."], src=[["DNB: debt-investor presentation, Aug 2026", DEBT], ["DNB: Corporate Mastercard", CORPMC]]),
        ]},
        {"id": "5.4", "ic": "building", "name": "Branches & advisers", "blurb": "52 offices.", "div": "dnb", "rev": "pm", "products": [
            P("branches", "Branches, advisers & estate agents", "52 branch offices (November 2024, down from 220 in 2010), customer centres, Private Banking advisers and DNB Eiendom estate agents; 98% of savings products are sold digitally.",
              s=["con", "home"], lc="open", neo=[0, ""], src=[["DNB: debt-investor presentation, Aug 2026", DEBT]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at DNB", "blurb": "Credit on Mastercard, debit on Visa.", "products": [
        P("mcatdnb", "Mastercard at DNB", "Every DNB consumer credit card is a Mastercard, up to World Elite for Private Banking, with Priceless presales and DNB-funded fuel discounts; the Corporate Mastercard is issued by SEB Kort. Debit, personal and business, is Visa, alongside BankAxept. Mastercard also clears Norway's interbank payments for Bits. No network agreement is public ⚠.",
          s=["con"], div="group", rev="other", mc="The relationship this map is drawn for.",
          src=[["DNB: DNB Mastercard", DNBMC], ["DNB: Pluss", PLUSS], ["DNB: Corporate Mastercard", CORPMC], ["The Paypers: Mastercard and Bits, May 2025", BITS]]),
    ]},
    {"id": "pillar-market", "name": "Norwegian payments", "blurb": "BankAxept, Vipps, mobile.", "products": [
        P("market", "The Norwegian market", "BankAxept carried 46% of card transactions in 2025 (49% in 2024) and international cards 54%; mobile was 27% of terminal payments, up from 12%; cash was 3% of payments. Banks earned NOK 11.8 billion from payment services, 55% of it from cards.",
          s=["con"], div="group", rev="other", src=[["Norges Bank: retail payment services 2025", NB25]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
