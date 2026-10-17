"""PKO Bank Polski's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the 1H 2026 results, presentation and Directors'
Report (13 August 2026), the 2025 results (12 March 2026) and the 2025–2027 strategy (24 October 2024).
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly
on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://www.pkobp.pl/en/investor-relations/financial-reports/periodic-report-for-the-first-half-of-2026"
PRES = "https://www.pkobp.pl/api/public/a0b0d69d-2a85-428f-bb0c-58da1b3a2ce3.pdf"
DR = "https://www.pkobp.pl/api/public/6627aaa6-1940-43cb-a47a-3e36e30c38ae.pdf"
CFS = "https://www.pkobp.pl/api/public/57cf6f76-c47b-4c5c-a17d-ed72de0980bd.pdf"
FY25 = "https://www.pkobp.pl/en/investor-relations/financial-reports/2025-annual-report"
STRAT = "https://www.pkobp.pl/en/investor-relations/current-reports/report-no-552024-pko-bank-polski-sa-group-strategy-for-years-2025-2027"
CARDS = "https://www.pkobp.pl/klient-indywidualny/karty-platnosci"
BLIKC = "https://www.pkobp.pl/klient-indywidualny/karty-platnosci/plac-zblizeniowo-blik"
MCPLAT = "https://www.pkobp.pl/klient-indywidualny/karty-platnosci/karta-kredytowa-mastercard-platinum"
PRZEJ = "https://www.pkobp.pl/klient-indywidualny/karty-platnosci/karta-kredytowa-przejrzysta"
VINF = "https://www.pkobp.pl/klient-indywidualny/karty-platnosci/karta-kredytowa-visa-infinite"
DEBIT = "https://www.pkobp.pl/klient-indywidualny/karty-platnosci/uniwersalna-karta-do-konta"
VMOB = "https://www.pkobp.pl/klient-indywidualny/karty-platnosci/visa-mobile"
APAY = "https://www.pkobp.pl/klient-indywidualny/karty-platnosci/apple-pay"
GPAY = "https://www.pkobp.pl/klient-indywidualny/karty-platnosci/google-pay"
JUNIOR = "https://www.pkobp.pl/klient-indywidualny/karty-platnosci/karta-debetowa-dziecka"
BIZCARDS = "https://www.pkobp.pl/firmy/karty-firmowe"
BIZDEBIT = "https://www.pkobp.pl/firmy/karty-firmowe/karta-firmowa-do-konta"
POS = "https://www.pkobp.pl/firmy/uslugi-dla-firm/terminal-platniczy"
ALLEGRO = "https://www.pkobp.pl/klient-indywidualny/karty-platnosci/allegroklik"
BLIK25 = "https://www.blik.com/en/nearly-3-bn-blik-transactions-in-2025-and-over-2-m-new-users"
MCPSP = "https://rzmlaw.com/en/mastercard-joins-polski-standard-platnosci-and-becomes-a-participant-of-the-blik-system"
EVO = "https://www.retailbankerinternational.com/news/evo-payments-to-acquire-66-stake-in-pko-bp-subsidiary-eservice-081113/"
KZZ = "https://www.pkobp.pl/aktualnosci/promocje/nawet-1000-zl-w-promocji-z-pko-kontem-za-zero-karta-visa-i-samsung"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · state anchor · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Poland's largest bank with PLN 608 billion of assets and an 18.4% ROE, the State Treasury as anchor shareholder, a nine-member board under Szymon Midera, and the 2025–2027 strategy \"The Number 1, full stop\".",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "PLN 608bn assets, ROE 18.4%.", "div": "pko", "rev": "tc", "products": [
            P("balance", "Balance sheet & earnings", "Net profit of PLN 5.29 billion in 1H 2026 (ROE 18.4%, cost/income 31.6%, cost of risk 30 bp) and PLN 10.7 billion in 2025 (ROE 19.5%); total assets PLN 608 billion; CET1 15.55%; 19.88% of Polish loans and 21.32% of savings at 30 June 2026. Moody's rates deposits A2.",
              s=["con"], neo=[0, ""], src=[["1H 2026 results", H1], ["Presentation 1H 2026", PRES], ["2025 results", FY25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "State-anchored, Midera as CEO.", "div": "pko", "rev": "tc", "products": [
            P("owners", "Listing & ownership", "Listed in Warsaw since November 2004 and the largest domestic bank on the exchange, worth PLN 129 billion at 30 June 2026; the State Treasury holds 29.43%, Nationale-Nederlanden OFE 7.03% and Allianz Polska OFE 5.90%. Founded in 1919 as the Postal Savings Bank ⚠.",
              s=["corp"], o="I", neo=[0, ""], src=[["Presentation 1H 2026", PRES]]),
            P("board", "Management & Supervisory Boards", "President Szymon Midera; vice-presidents Krzysztof Dresler (finance), Piotr Mazur (risk), Ludmiła Falak-Cyniak (corporate and investment), Tomasz Pol (retail and corporate), Mariusz Zarzycki (technology), Michał Sobolewski, Wojciech Papierak and Piotr Stolarczyk (both June 2026). Supervisory Board chaired by Tomasz Siemiątkowski.",
              s=["corp"], st="flux", neo=[0, ""], src=[["Directors' Report 1H 2026", DR]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology", "blurb": "Cloud data, 468 robotised processes.", "div": "pko", "rev": "tc", "products": [
            P("tech", "Cloud, data & automation", "A behavioural-data architecture on Google Cloud Platform, a Digital Data Platform with an unstructured-data store linked to the SzukAI search engine, and 468 robotised processes that have completed 517 million tasks.",
              s=["corp"], o="P", at="Google Cloud", neo=[0, ""], src=[["Directors' Report 1H 2026", DR]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy 2025–2027", "blurb": "Number 1, full stop.", "div": "pko", "rev": "tc", "products": [
            P("strategy", "The Number 1, full stop", "Seven pillars adopted in October 2024: everyday needs (15 million individual customers by 2027), ecosystems (2.5 million customers through partners), savings (27% household share), branches (600 in a new format), business (18% of financing), energy transition and Europe. 2027 targets: ROE above 18%, cost/income below 35%. Cash-loan and mortgage share targets already met by mid-2026.",
              s=["corp"], st="active", ay="Oct 2024", neo=[0, ""], src=[["Strategy 2025–2027", STRAT], ["Presentation 1H 2026", PRES]]),
            P("intl", "Polish bank in Europe", "Corporate branches in Germany, Czechia, Slovakia and Romania, representative offices in Sweden, Lithuania and Austria (opened 1H 2026), aiming for twelve foreign units across the EU.",
              s=["corp"], st="new", neo=[0, ""],
              mc="Expansion into nine more EU markets needs cross-border cards and acceptance.",
              src=[["Directors' Report 1H 2026", DR], ["Strategy 2025–2027", STRAT]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: 9.9 million Visa debit cards, a credit book split between Mastercard and Visa, BLIK codes and contactless BLIK on Mastercard terminals, phone wallets and Visa Mobile, terminals with eService, and SEPA Instant and euro links through BLIK.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "9.9 million, on Visa.", "div": "pko", "rev": "retail", "products": [
            P("debit", "Account debit card", "Over 9.9 million debit cards out of 11.1 million cards at 30 June 2026. The account card is a Visa, usable without FX conversion in 19 currencies, with Visa Benefit discounts; Konto za Zero is sold with a Visa card.", short="Debit (Visa)",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="The core of the card book sits with Visa.",
              src=[["Universal account card", DEBIT], ["Konto za Zero with Visa, 2026", KZZ], ["Directors' Report 1H 2026", DR]]),
            P("junior", "PKO Junior card", "A debit card for children aged 6 to 12 on the PKO Junior account; chargebacks run under Visa rules.",
              s=["young"], lc="open", o="P", at="Visa", neo=[0, "Visa."], src=[["Child's debit card", JUNIOR]]),
            P("bizdebit", "Business debit cards", "PKO Visa Biznes Wielowalutowa, one card for the PLN account and currency sub-accounts, and PKO Visa Business Waluta for EUR or USD.",
              s=["sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Business cards", BIZCARDS], ["Business debit card", BIZDEBIT]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "965k cards, split.", "div": "pko", "rev": "retail", "products": [
            P("mcplat", "PKO Mastercard Platinum", "Credit limit of PLN 5,000 to 200,000, travel insurance, concierge, no FX fee and Mastercard Priceless points (Bezcenne Chwile).", short="Mastercard Platinum",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard card."],
              mc="Mastercard's flagship card at PKO.",
              src=[["PKO Mastercard Platinum", MCPLAT]]),
            P("przejrzysta", "Przejrzysta (Transparent) card", "The mass-market credit card, capped at PLN 80 a year in fees, issued in both Visa and Mastercard versions.", short="Przejrzysta (Visa & Mastercard)",
              s=["con"], lc="borrow", o="P", at="Visa, Mastercard", neo=[1, "Both networks."], src=[["Przejrzysta credit card", PRZEJ]]),
            P("visainf", "PKO Visa Infinite", "The premium card: limit of PLN 50,000 to 1 million, Priority Pass lounges and Fast Track at Warsaw Chopin.",
              s=["con", "saver"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["PKO Visa Infinite", VINF]]),
            P("zappka", "Żappka Pay card", "Agreed in April 2026 with Żappka Pay (Żabka Group): a card with a credit limit and deferred payment in the Żappka app, usable wherever Visa is accepted, issued with Visa and Planet Pay.",
              s=["con", "young"], lc="borrow", st="new", ay="Apr 2026", o="P", at="Żabka, Visa, Planet Pay", neo=[0, "Visa."],
              mc="A new retail-ecosystem card went to Visa in 2026.",
              src=[["Directors' Report 1H 2026", DR]]),
            P("bizcredit", "PKO Euro Biznes credit card", "Business credit card with up to PLN 50,000 of limit ⚠ network not stated on the bank's page.",
              s=["sme"], lc="borrow", neo=[None, "Network not stated."], src=[["Business cards", BIZCARDS]]),
        ]},
        {"id": "2.3", "ic": "zap", "name": "BLIK", "blurb": "516m contactless BLIK payments.", "div": "blik", "rev": "retail", "products": [
            P("blikc", "Contactless BLIK", "Phone payments with no card, at any Mastercard contactless terminal worldwide and converted at Mastercard rates with no PKO fee; 516.6 million transactions to 30 June 2026, 104.6 million in 1H 2026 alone.", short="Contactless BLIK (Mastercard)",
              s=["con", "young"], lc="move", o="P", at="BLIK, Mastercard", neo=[2, "Runs on Mastercard acceptance."],
              mc="Mastercard's largest flow at PKO, carried under the BLIK brand.",
              src=[["Contactless BLIK", BLIKC], ["Directors' Report 1H 2026", DR], ["Mastercard joins BLIK's operator, Apr 2020", MCPSP]]),
            P("blik", "BLIK codes & phone transfers", "PKO co-owns Polski Standard Płatności, BLIK's operator; BLIK did 2.9 billion transactions worth PLN 441.5 billion in 2025 for 20.7 million users, half of them online.",
              s=["con", "sme"], lc="move", o="P", at="Polski Standard Płatności", neo=[0, "Domestic scheme; Mastercard is a shareholder."],
              src=[["BLIK: 2025 results, Feb 2026", BLIK25], ["Mastercard joins BLIK's operator, Apr 2020", MCPSP]]),
            P("paylater", "PKO Pay Later", "Buy now, pay later in the app: about 395,000 active users, PLN 566 million of limits and 21 million purchases worth PLN 3.1 billion to date, 99% of them paid by BLIK code.",
              s=["con"], lc="borrow", o="B", neo=[0, "BLIK."], src=[["Directors' Report 1H 2026", DR]]),
        ]},
        {"id": "2.4", "ic": "wallet", "name": "Wallets & online", "blurb": "Apple Pay to Visa Mobile.", "div": "pko", "rev": "retail", "products": [
            P("wallets", "Phone & watch wallets", "Apple Pay, Google Pay, Samsung Pay, Garmin Pay, Xiaomi Pay and SwatchPAY! for PKO's Visa and Mastercard cards, personal and business.",
              s=["con", "sme"], lc="move", o="P", at="Apple, Google, Samsung", neo=[1, "Visa and Mastercard tokens."],
              src=[["Apple Pay", APAY], ["Google Pay", GPAY], ["Cards and payments", CARDS]]),
            P("visamobile", "Visa Mobile", "Pay online by phone number and confirm in the app, for every PKO personal Visa card.",
              s=["con"], lc="move", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa's own checkout is live; Click to Pay is not mentioned.",
              src=[["Visa Mobile", VMOB]]),
            P("placez", "Płacę z PKO", "PKO's own online payment option listed on its cards and payments page ⚠ details not read.",
              s=["con"], lc="move", o="B", neo=[None, "Not documented."], src=[["Cards and payments", CARDS]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "Terminals with eService.", "div": "pko", "rev": "corp", "products": [
            P("terminals", "Payment terminals", "Countertop and mobile terminals, SmartPOS and the eService soft-POS app sold by PKO, taking Visa, Mastercard, BLIK and Tap to Pay on iPhone; ordered fully remotely since 1H 2026. eService has been majority-owned by EVO since 2013 under a 20-year alliance ⚠ current ownership.",
              s=["sme"], lc="move", o="P", at="eService", neo=[1, "Accepts Visa, Mastercard and BLIK."],
              src=[["Payment terminal", POS], ["EVO buys 66% of eService, Nov 2013", EVO], ["Presentation 1H 2026", PRES]]),
        ]},
        {"id": "2.6", "ic": "arrow-left-right", "name": "Instant & cross-border", "blurb": "SEPA Instant, BLIK to Bizum.", "div": "pko", "rev": "corp", "products": [
            P("sepainst", "SEPA Instant & ISO 20022", "Instant euro transfers for iPKO biznes clients, 24/7, to the EU, SEPA area and UK at standard SEPA prices (1H 2026), and ISO 20022 international payments.",
              s=["corp", "sme"], lc="move", st="new", neo=[0, ""], src=[["Presentation 1H 2026", PRES], ["Directors' Report 1H 2026", DR]]),
            P("bizum", "BLIK's euro links", "BLIK's first pilot euro transfer from Spain's Bizum went to PKO Bank Polski, through the EuroPA alliance (reported February 2026).",
              s=["con"], lc="move", st="new", ay="Feb 2026", o="P", at="BLIK, Bizum", neo=[0, "Account-to-account."], src=[["BLIK: 2025 results, Feb 2026", BLIK25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: face and selfie checks and interbank behavioural fraud screening, bots that handled 13.8 million conversations in a half-year, rewards through Allegro Klik and the Kropka app, and a cloud data platform.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "PKO ID and behavioural checks.", "div": "pko", "rev": "retail", "products": [
            P("pkoid", "PKO ID & selfie checks", "Face-recognition login and transfer approval in the app and online, selfie confirmation for risky transfers, and identity checks in the app before a helpline call (227,000 calls).",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, "PKO's own."], src=[["Directors' Report 1H 2026", DR]]),
            P("behav", "Behavioural fraud screening", "Sectoral Behavioural Verification shares signals between banks to stop scams, with a new helpline for reporting fraudulent transactions and bots confirming 1.1 million card payments.",
              s=["con", "sme"], lc="everyday", st="new", o="P", neo=[0, "Interbank, not Mastercard."],
              mc="Scam and behavioural tools are being built without Mastercard.",
              src=[["Directors' Report 1H 2026", DR], ["Presentation 1H 2026", PRES]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & bots", "blurb": "13.8m bot conversations.", "div": "pko", "rev": "retail", "products": [
            P("bots", "Voice assistant & bots", "Bots handled 13.8 million conversations in 1H 2026 and 97 million to date; the app's voice assistant handled 41.6 million.",
              s=["con"], lc="everyday", o="B", neo=[0, ""],
              mc="An assistant at this scale is ground for agentic payments.",
              src=[["Directors' Report 1H 2026", DR]]),
            P("docai", "LLM & document AI", "First large-language-model deployment, Document Intelligence for credit files, SzukAI semantic search, and an AI forecasting project with the Warsaw School of Economics.",
              s=["corp"], lc="beyond", st="new", o="B", neo=[0, ""], src=[["Presentation 1H 2026", PRES], ["Directors' Report 1H 2026", DR]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & offers", "blurb": "Allegro Klik, Kropka.", "div": "pko", "rev": "retail", "products": [
            P("allegro", "Allegro Klik", "A PKO account linked to Allegro for one-click payments and 1–3% cashback; more than 350,000 PKO customers by mid-2026.",
              s=["con"], lc="grow", st="new", o="P", at="Allegro", neo=[0, "Account-linked, not card."],
              mc="Poland's biggest marketplace is wired to the account, not a card.",
              src=[["Presentation 1H 2026", PRES], ["Allegro Klik", ALLEGRO]]),
            P("kropka", "Kropka", "A game-and-lottery app launched in June 2026 with PKO BP Finat: points for logging in and paying cashless, prizes worth over PLN 3.5 million paid into PKO accounts.",
              s=["con", "young"], lc="grow", st="new", ay="Jun 2026", o="B", neo=[0, ""], src=[["Directors' Report 1H 2026", DR]]),
            P("benefits", "Card benefits", "Visa Benefit discounts on Visa debit and credit cards, and Mastercard Priceless points on the Mastercard Platinum card.",
              s=["con"], lc="grow", o="P", at="Visa, Mastercard", neo=[1, "Visa Benefit and Mastercard Priceless."],
              src=[["Universal account card", DEBIT], ["PKO Mastercard Platinum", MCPLAT]]),
        ]},
        {"id": "3.4", "ic": "chart-column", "name": "Data & operations", "blurb": "10m e-documents.", "div": "pko", "rev": "tc", "products": [
            P("data", "Data & valuation models", "A machine-learning property valuation tool, centralised litigation data and a new AML survey across digital credit channels.",
              s=["home", "corp"], lc="beyond", o="B", neo=[0, ""], src=[["Directors' Report 1H 2026", DR]]),
            P("edocs", "Paperless operations", "Ten million documents sent on a durable digital medium in 1H 2026, saving about PLN 28 million, with e-signature in the app.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["Directors' Report 1H 2026", DR]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: 30% of new Polish mortgages, 9.9 million accounts and a fast-growing cash-loan book, savings, funds and insurance, 679,000 small firms, corporate and investment banking with PKO Leasing, and KREDOBANK in Ukraine.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Mortgages", "blurb": "30% of new sales.", "div": "hipo", "rev": "retail", "products": [
            P("mortgages", "Mortgages", "PLN 137.8 billion of PLN mortgages (+13.9% a year) and 30.3% of new sales in 1H 2026 (PLN 21.4 billion); the Digital Mortgage is signed fully remotely, 59.4% of new loans at a fixed rate.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["Presentation 1H 2026", PRES], ["Directors' Report 1H 2026", DR]]),
            P("hipo", "PKO Bank Hipoteczny", "The group's mortgage bank, funding home loans with covered bonds that retail customers can now buy online.",
              s=["home", "saver"], lc="borrow", neo=[0, ""], src=[["Directors' Report 1H 2026", DR]]),
        ]},
        {"id": "4.2", "ic": "hand-coins", "name": "Accounts & loans", "blurb": "9.9m accounts.", "div": "pko", "rev": "retail", "products": [
            P("accounts", "Current accounts", "9.9 million current accounts and 11.9 million retail customers at 30 June 2026; PKO Konto za Zero and the PKO Junior account for children.",
              s=["con", "young"], lc="open", neo=[0, "Visa debit."], src=[["Presentation 1H 2026", PRES], ["Konto za Zero with Visa, 2026", KZZ]]),
            P("cashloan", "Cash loans", "PLN 52.6 billion of consumer loans (+21.5% a year) and a 22.3% share of cash loans; about 90% signed digitally.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Presentation 1H 2026", PRES], ["Directors' Report 1H 2026", DR]]),
        ]},
        {"id": "4.3", "ic": "coins", "name": "Savings, funds & insurance", "blurb": "PLN 721bn of savings.", "div": "tfi", "rev": "retail", "products": [
            P("deposits", "Deposits & Treasury bonds", "PLN 338.5 billion of household deposits (23.79% share) and PLN 153.9 billion of retail Treasury bonds held through PKO; bonds can now be bought in the app.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["Presentation 1H 2026", PRES]]),
            P("tfi", "PKO TFI & brokerage", "PKO TFI manages PLN 87.8 billion (18.44% of the fund market, 2.3 million clients, PPK leader with 30.5%); the brokerage is second in equity turnover with 10.6%.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["Directors' Report 1H 2026", DR]]),
            P("insurance", "PKO Życie & PKO TU", "PKO Dom, PKO Moto, life and business policies; gross written premium more than doubled to PLN 0.78 billion in 1H 2026.",
              s=["con", "home"], lc="grow", st="new", neo=[0, ""], src=[["Presentation 1H 2026", PRES], ["Directors' Report 1H 2026", DR]]),
        ]},
        {"id": "4.4", "ic": "briefcase", "name": "Small firms", "blurb": "679k firms.", "div": "pko", "rev": "retail", "products": [
            P("firms", "Small-firm banking", "679,000 small firms and PLN 36.5 billion of financing; free accounts for start-ups, Allegro Kapitał loans and SME loans through Allegro for firms with PLN 15–60 million of revenue.",
              s=["sme"], lc="open", neo=[0, "Visa business debit."], src=[["Presentation 1H 2026", PRES], ["Directors' Report 1H 2026", DR]]),
        ]},
        {"id": "4.5", "ic": "building-2", "name": "Corporate & leasing", "blurb": "PLN 100bn to corporates.", "div": "leasing", "rev": "corp", "products": [
            P("cib", "Corporate & investment banking", "32,000 corporates and PLN 100.3 billion of financing; 47 syndicated deals in 1H 2026, bookrunner for Allegro and Pepco, defence and dual-use guarantees with BGK, and the iPKO dealer FX platform.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Presentation 1H 2026", PRES], ["Directors' Report 1H 2026", DR]]),
            P("leasing", "PKO Leasing & PKO Masterlease", "Leasing, factoring and fleet: PKO Masterlease formed in February 2026 with 45,829 vehicles (2,233 electric); Automarket.pl sold 5,339 vehicles in 1H 2026 (+29%).",
              s=["sme", "corp"], lc="borrow", st="new", ay="Feb 2026", neo=[0, ""],
              mc="A 45,800-vehicle fleet with no fleet-card network named.",
              src=[["Directors' Report 1H 2026", DR], ["Presentation 1H 2026", PRES]]),
        ]},
        {"id": "4.6", "ic": "earth", "name": "Ukraine", "blurb": "KREDOBANK, Lviv.", "div": "kredo", "rev": "retail", "products": [
            P("kredo", "KREDOBANK", "A universal bank based in Lviv with 64 branches, lending mainly to corporate and SME clients and listed among Ukraine's 16 systemically important banks.",
              s=["corp", "sme"], lc="everyday", o="A", neo=[None, "Card networks not checked."], src=[["Presentation 1H 2026", PRES]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the IKO app on 8.7 million phones and PKO Junior, iPKO and iPKO biznes online, 954 branches, 224 agencies and 3,138 ATMs, and partners from Allegro to Żabka.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "IKO app", "blurb": "8.7m active apps.", "div": "pko", "rev": "retail", "products": [
            P("iko", "IKO mobile app", "8.7 million active apps and 6.9 million monthly users; 85% of active customers are digital. New in 2026: eSIM sales, Treasury bonds, selfie checks and a personalised start screen.",
              s=["con", "sme"], lc="everyday", o="B", neo=[1, "Hosts contactless BLIK on Mastercard."], src=[["Presentation 1H 2026", PRES], ["Directors' Report 1H 2026", DR]]),
            P("juniorapp", "PKO Junior app", "Ten years old in 2026; children made their first million contactless BLIK payments in it.",
              s=["young"], lc="open", o="B", neo=[1, "Children's contactless BLIK runs on Mastercard."], src=[["Directors' Report 1H 2026", DR]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Online banking", "blurb": "iPKO and iPKO biznes.", "div": "pko", "rev": "corp", "products": [
            P("ipko", "iPKO & iPKO biznes", "iPKO for individuals and small firms (79,000 firms online) and iPKO biznes for 23,900 corporates, now with SEPA Instant and the iPKO dealer FX platform.",
              s=["sme", "corp"], lc="everyday", o="B", neo=[0, ""], src=[["Presentation 1H 2026", PRES]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & ATMs", "blurb": "954 branches.", "div": "pko", "rev": "retail", "products": [
            P("branches", "Branches, agencies & ATMs", "954 branches (897 retail, 57 corporate), 224 agencies and 3,138 ATMs at 30 June 2026; 600 branches to be in a new advisory format by 2027.",
              s=["con", "home"], lc="everyday", st="flux", neo=[0, ""], src=[["Presentation 1H 2026", PRES], ["Strategy 2025–2027", STRAT]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners & ecosystems", "blurb": "Allegro, Żabka, Samsung.", "div": "pko", "rev": "retail", "products": [
            P("partners", "Ecosystem partners", "Allegro (Klik and SME loans), Żabka's Żappka app, Samsung mortgage and account offers, mortgage intermediaries and Automarket.pl, under the strategy's aim of 2.5 million customers through ecosystems.",
              s=["con", "home", "sme"], lc="open", st="new", o="P", at="Allegro, Żabka, Samsung", neo=[0, ""],
              mc="The ecosystem pillar is where offers and open-finance services could plug in.",
              src=[["Strategy 2025–2027", STRAT], ["Directors' Report 1H 2026", DR]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at PKO", "blurb": "Visa debit, BLIK on Mastercard.", "products": [
        P("mcatpko", "Mastercard at PKO", "PKO's 9.9 million debit cards, its business cards, Visa Infinite, Visa Mobile and the new Żappka card are Visa. Mastercard has the Platinum credit card and one version of the Przejrzysta card, and, larger than both, contactless BLIK: 516.6 million phone payments on Mastercard acceptance since launch. Mastercard has owned part of BLIK's operator since April 2020.",
          s=["con"], div="pko", rev="tc", mc="The relationship this map is drawn for.",
          src=[["Contactless BLIK", BLIKC], ["Mastercard joins BLIK's operator, Apr 2020", MCPSP], ["Universal account card", DEBIT]]),
    ]},
    {"id": "pillar-market", "name": "Polish banking", "blurb": "BLIK, bank tax, CHF loans.", "products": [
        P("market", "The Polish market", "BLIK is the domestic champion (2.9 billion transactions in 2025). Banks pay a tax on certain financial institutions (PLN 727 million for PKO in 1H 2026), still carry the cost of Swiss-franc mortgage litigation, and face UOKiK interchange proceedings open since 2001. No stablecoin or tokenised-deposit work by PKO was found ⚠; Poland's national Visa/Mastercard split was not checked ⚠.",
          s=["con"], div="pko", rev="tc", src=[["BLIK: 2025 results, Feb 2026", BLIK25], ["Consolidated statements 1H 2026", CFS]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
