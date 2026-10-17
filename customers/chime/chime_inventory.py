"""Chime Financial's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Chime's own unless a source says otherwise: the Q2 2026 results (5 August 2026), Q1 2026 results
(6 May 2026), Q4 and FY2025 results (26 February 2026) and the IPO prospectus (11 June 2025). ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://www.sec.gov/Archives/edgar/data/0001795586/000179558626000046/ex991q226.htm"
Q1 = "https://www.sec.gov/Archives/edgar/data/0001795586/000179558626000035/ex991q126.htm"
FY25 = "https://www.01net.it/chime-reports-fourth-quarter-and-full-year-2025-financial-results/"
PROSP = "https://www.sec.gov/Archives/edgar/data/1795586/000162828025030855/chimefinancialinc-finalpro.htm"
EIGHTK = "https://www.boardroomalpha.com/sec/chym-8-k-2026-08-05-0001795586-26-000046"
STRIDE = "https://chime.com/newsroom/chime-announces-agreement-to-acquire-stride-bank/"
PRIME = "https://www.chime.com/newsroom/news/americas-choice-for-banking-expands-lead-with-launch-of-chime-prime/"
ABPRIME = "https://www.americanbanker.com/payments/news/chime-moves-further-up-market-with-prime-offering"
ABQ4 = "https://www.americanbanker.com/news/chime-beats-q4-estimates-leans-into-trump-accounts"
INVEST = "https://www.pymnts.com/news/banking/2026/chime-expands-banking-app-to-include-investment-services/"
PYQ1 = "https://www.pymnts.com/earnings/2026/chime-leans-on-ai-pushes-upmarket-in-first-profitable-quarter"
DEBIT = "https://www.chime.com/debit-card/"
CREDIT = "https://www.chime.com/credit/"
HOME = "https://www.chime.com/"
NEWS = "https://www.chime.com/newsroom/"
ENT26 = "https://investors.chime.com/news-releases/news-release-details/chime-enterprise-adds-new-employer-partners-demand-grows"
ETECH = "https://www.chime.com/newsroom/chime-enterprise-adds-etech-as-newest-employer-partner-empowering-employees-with-chimes-comprehensive-fee-free-financial-wellness-suite/"
CFPB = "https://www.consumerfinance.gov/enforcement/actions/chime-financial-inc/"
BREACH = "https://bankingdive.com/news/hacktivist-group-stole-chime-customer-information-lawsuits-allege/819482/"
LAYOFF = "https://allwork.space/2026/07/chime-joins-fintech-layoff-wave-with-10-workforce-reduction-in-ai-efficiency-push/"
SACRA = "https://sacra.com/c/chime"
LINK = "https://help.chime.com/hc/en-us/articles/what-card-networks-can-i-link-to-my-chime-account-c2001b47"
NILSON = "https://nilsonreport.com/articles/mastercard-and-visa-cards-in-the-us-2025/"
TC = "https://techcrunch.com/2025/06/12/chime-almost-died-in-2016-turned-down-by-100-vcs-today-it-ipod-at-14-5b/"
FHN = "https://finhealthnetwork.org/research/chimes-spotme-a-new-model-for-cash-flow-support/"
AIBLOG = "https://chime.com/newsroom/from-tabular-to-transformers-event-sequence-models-for-financial-intelligence/"
MLS = "https://www.sportsbusinessjournal.com/Articles/2026/07/27/chime-making-debut-as-mls-all-star-presenting-sponsor/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "members · banks · own stack", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: 10.4 million active members and GAAP profit since Q1 2026, two partner banks and a deal to buy one of them, its own processor, and a push to make Chime the main account for everyday Americans.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "10.4m members, $670m a quarter.", "div": "chime", "rev": "corp", "products": [
            P("results", "Results", "Q2 2026 revenue of $670 million (up 27%), net income of $28 million, the second GAAP-profitable quarter in a row, and adjusted EBITDA of $102 million; FY2025 revenue of $2.2 billion with a $1.0 billion net loss from IPO stock compensation. FY2026 revenue guidance raised to $2.76–2.77 billion in September 2026.",
              s=["con"], neo=[0, ""], src=[["Q2 2026 results", Q2], ["Q4 and FY2025 results", FY25], ["Chime: Stride agreement and guidance, Sep 2026", STRIDE]]),
            P("members", "Active members & volume", "10.4 million active members at 30 June 2026 (up 20%), from 5.3 million in 2022; ARPAM of $260; purchase volume of $38 billion in the quarter and $134 billion in 2025.",
              s=["con"], neo=[0, "Visa volume."], src=[["Q2 2026 results", Q2], ["IPO prospectus, Jun 2025", PROSP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & oversight", "blurb": "Britt, Troughton; CFPB order.", "div": "chime", "rev": "corp", "products": [
            P("leadership", "Founders & executives", "Founded in 2012 as 1debit by Chris Britt (Chair and CEO) and Ryan King; Mark Troughton is President and, since 7 August 2026, interim CFO after Matt Newcomb stepped down; Janelle Sallenave is COO and Vineet Mehra Chief Growth Officer. About 1,500 staff after a 10% cut in July 2026 ⚠.",
              s=["con"], neo=[0, ""], src=[["8-K, Aug 2026", EIGHTK], ["American Banker: Q4 2025", ABQ4], ["IPO prospectus, Jun 2025", PROSP], ["Allwork: 10% cut, Jul 2026", LAYOFF]]),
            P("oversight", "Regulators & lawsuits", "A CFPB order in May 2024 ($3.25 million penalty, at least $1.3 million of redress) for slow refunds on closed accounts; proposed class actions from April 2026 alleging a data breach after an outage, which Chime disputes.",
              s=["con"], st="flux", neo=[0, ""], src=[["CFPB: enforcement action, May 2024", CFPB], ["Banking Dive: breach lawsuits, Apr 2026", BREACH]]),
        ]},
        {"id": "1.3", "ic": "building-2", "name": "Partner banks & charter", "blurb": "Buying Stride for $590m.", "div": "banks", "rev": "corp", "products": [
            P("partnerbanks", "The Bancorp Bank & Stride Bank", "Chime is not a bank: The Bancorp Bank, N.A. and Stride Bank, N.A. hold members' deposits and issue their cards, collect interchange and pass it to Chime; both are under $10 billion of assets and so exempt from the Durbin debit cap.",
              s=["con"], o="P", at="The Bancorp Bank, Stride Bank", neo=[0, "They issue Visa cards."], src=[["IPO prospectus, Jun 2025", PROSP], ["Chime home page", HOME]]),
            P("chimebank", "Chime Bank, N.A.", "Agreement of 8 September 2026 to buy Stride's parent for $590 million in cash (about 1.5 times tangible book); Stride becomes Chime Bank, N.A. and Chime a bank holding company. OCC and Federal Reserve approval needed; closing expected in the first half of 2027; assets to stay under $10 billion.", short="Chime Bank (Stride)",
              s=["con"], st="new", ay="Sep 2026", o="A", div="chimebank", neo=[None, "Network for the new issuer not announced."],
              mc="Owning its issuer makes the card network Chime's own decision from 2027.",
              src=[["Chime: agreement to acquire Stride Bank, Sep 2026", STRIDE]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "ChimeCore & AI", "blurb": "Own processor; 84% AI code.", "div": "chime", "rev": "corp", "products": [
            P("chimecore", "ChimeCore", "Chime's own processor and ledger, launched in 2024; credit moved first and the migration from Galileo finished in Q4 2025, cutting processing costs by about 60% at an exit cost of about $32.7 million.",
              s=["con"], st="new", ay="2024", o="B", neo=[0, ""],
              mc="An issuer processor of its own lowers the cost of changing or adding a network.",
              src=[["Q4 and FY2025 results", FY25], ["American Banker: Q4 2025", ABQ4], ["IPO prospectus, Jun 2025", PROSP]]),
            P("ai", "AI in engineering & risk", "AI-assisted code rose from about 29% to 84% of shipped code in four months (Q1 2026); event-sequence transformer models for risk and personalisation; a 10% workforce cut in July 2026 for smaller teams.",
              s=["con"], st="new", o="B", neo=[0, ""], src=[["PYMNTS: Q1 2026", PYQ1], ["Chime: event-sequence models", AIBLOG], ["8-K, Aug 2026", EIGHTK]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Primary account, up-market.", "div": "chime", "rev": "corp", "products": [
            P("strategy", "Strategy", "Be the primary account for everyday Americans, move up-market with Chime Prime, grow credit and liquidity products, run on its own stack and become a bank; first full year of GAAP profit in 2026.",
              s=["con", "prime"], neo=[0, ""], src=[["Q4 and FY2025 results", FY25], ["Q2 2026 results", Q2]]),
            P("deals", "IPO, deals & buybacks", "Nasdaq IPO at $27 on 12 June 2025 (about $14.5 billion); Salt Labs bought in 2024 for Chime Enterprise; a further $200 million buyback authorised in May 2026 and $222 million repurchased in the first half of 2026. Market value about $11.2 billion ⚠.",
              s=["con"], o="A", neo=[0, ""], src=[["IPO prospectus, Jun 2025", PROSP], ["TechCrunch: IPO, Jun 2025", TC], ["Q1 2026 results", Q1], ["Q2 2026 results", Q2]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: a Visa debit card for every member, the Chime Card on Visa, instant transfers out, direct deposit and linked cards in, 47,000 fee-free ATMs, and the network terms that pay for it all.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Chime Visa debit.", "div": "banks", "rev": "payments", "products": [
            P("debit", "Chime Visa Debit Card", "The core card, issued by Bancorp or Stride and accepted wherever Visa debit is, with Visa Zero Liability, real-time alerts and a lock in the app; interchange on it is the larger part of Chime's revenue.", short="Debit (Visa)",
              s=["con", "worker"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="The franchise Mastercard does not have: most of $134 billion of 2025 purchase volume, on Visa.",
              src=[["Chime: debit card", DEBIT], ["IPO prospectus, Jun 2025", PROSP]]),
            P("wallets", "Virtual card, Apple Pay & Google Pay", "A virtual card that members can add to Apple Pay and Google Pay and use with tap to pay.",
              s=["con"], lc="everyday", o="P", at="Apple, Google", neo=[0, "Visa tokens."], src=[["Chime: debit card", DEBIT]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Chime Card", "blurb": "Secured Visa credit, 27% of spend.", "div": "banks", "rev": "payments", "products": [
            P("chimecard", "Chime Card (secured Visa credit)", "Formerly Credit Builder (2020), relaunched with cash back on ChimeCore in Q3 2025: no annual fee, no interest and no credit check, the limit set by money moved into it. Credit was 27% of purchase volume in Q2 2026, from 16% in September 2025.", short="Chime Card (Visa)",
              s=["builder", "con"], lc="borrow", st="new", ay="Q3 2025", o="P", at="Visa", neo=[0, "Visa."],
              mc="The fastest-growing part of Chime's card spend, all on Visa.",
              src=[["Chime: Chime Card", CREDIT], ["Q4 and FY2025 results", FY25], ["Q2 2026 results", Q2]]),
            P("primecard", "Onyx metal card for Prime", "Chime Prime members get the Chime Card in a metal design with 5% cash back on a chosen category, Visa Signature Concierge and Priority Pass.",
              s=["prime"], lc="borrow", st="new", ay="Apr 2026", o="P", at="Visa, Priority Pass", neo=[0, "Visa Signature."], src=[["Chime: Chime Prime launch, Apr 2026", PRIME]]),
        ]},
        {"id": "2.3", "ic": "send", "name": "Instant transfers", "blurb": "OIT and Pay Anyone.", "div": "chime", "rev": "payments", "products": [
            P("oit", "Outbound Instant Transfer", "Instant transfers to outside accounts for a 1.75% fee, launched in January 2025 ⚠; about $1.4 billion of volume in Q2 2026, reported alongside purchase volume. The rail is not disclosed ⚠.", short="Instant transfers out",
              s=["con", "worker"], lc="move", st="new", ay="Jan 2025", o="B", neo=[None, "Rail not disclosed ⚠."],
              mc="Push-to-card payouts to Mastercard cards would ride Mastercard Send.",
              src=[["Sacra: Chime", SACRA], ["Q2 2026 results", Q2]]),
            P("payanyone", "Pay Anyone", "Free payments to friends and family, including people without Chime.",
              s=["con"], lc="move", o="B", neo=[None, "Rail for non-members not disclosed ⚠."], src=[["IPO prospectus, Jun 2025", PROSP]]),
        ]},
        {"id": "2.4", "ic": "arrow-left-right", "name": "Money in", "blurb": "Direct deposit, linked cards.", "div": "chime", "rev": "payments", "products": [
            P("directdeposit", "Direct deposit & Get Paid Early", "Pay by direct deposit up to two days early; qualifying direct deposits unlock SpotMe, Chime Plus and Chime Prime.",
              s=["con", "worker"], lc="open", o="B", neo=[0, "ACH."], src=[["Chime home page", HOME], ["IPO prospectus, Jun 2025", PROSP]]),
            P("linkcards", "Fund from a linked debit card", "Members can move money in from US-issued Visa and Mastercard debit cards ⚠ (help page no longer reachable).",
              s=["con"], lc="move", o="P", at="Visa, Mastercard", neo=[1, "Pulls from Mastercard debit cards ⚠."], src=[["Chime help: linkable card networks", LINK]]),
        ]},
        {"id": "2.5", "ic": "network", "name": "ATMs & cash", "blurb": "47,000 fee-free ATMs.", "div": "chime", "rev": "payments", "products": [
            P("atm", "Fee-free ATM network", "More than 47,000 fee-free ATMs through Allpoint, Visa Plus Alliance and FCTI machines in 7-Eleven and Speedway.",
              s=["con"], lc="everyday", o="P", at="Allpoint, Visa Plus Alliance, MoneyPass", neo=[0, "Visa Plus Alliance."], src=[["Chime: debit card", DEBIT], ["IPO prospectus, Jun 2025", PROSP]]),
            P("cashdeposit", "Cash deposits at retailers", "Cash deposits at Walgreens and other retailers through Interactive Communications International.",
              s=["con", "worker"], lc="everyday", o="P", at="Walgreens, InComm", neo=[0, ""], src=[["IPO prospectus, Jun 2025", PROSP]]),
        ]},
        {"id": "2.6", "ic": "scroll-text", "name": "Network terms", "blurb": "Interchange, Durbin-exempt.", "div": "banks", "rev": "payments", "products": [
            P("networkterms", "Network pricing & routing", "Chime has negotiated favourable pricing with card networks, contingent on conditions, with no terms disclosed; Regulation II requires a second, unaffiliated debit network (the prospectus names STAR as an example ⚠). Visa took about 70% of combined Visa and Mastercard US card volume in 2025.",
              s=["con"], lc="everyday", o="P", at="Visa, STAR ⚠", neo=[0, "Visa; STAR ⚠."],
              mc="No renewal date is public; Chime Bank in 2027 is the likely moment to revisit it.",
              src=[["IPO prospectus, Jun 2025", PROSP], ["Nilson: Mastercard and Visa in the US, 2025", NILSON]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: alerts, card locks and fraud models, membership tiers that reward direct deposit, credit-score building, and free tax filing with Trump Accounts built in.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Alerts, locks, own models.", "div": "chime", "rev": "payments", "products": [
            P("alerts", "Alerts, card lock & Zero Liability", "Real-time transaction alerts, turning card use off in the app, and Visa Zero Liability on the debit card.",
              s=["con"], lc="everyday", o="B", neo=[0, "Chime's and Visa's."], src=[["Chime: debit card", DEBIT]]),
            P("riskmodels", "Risk models", "In-house event-sequence AI models for fraud, risk and personalisation; MyPay's loss rate was 0.9% in Q2 2026. After the April 2026 outage, lawsuits alleged stolen identity data, which Chime denies.",
              s=["con", "worker"], lc="everyday", st="flux", o="B", neo=[0, "Chime's own."],
              mc="Identity checks and scam scoring are untouched ground at a fast-growing, under-served base.",
              src=[["Chime: event-sequence models", AIBLOG], ["Q2 2026 results", Q2], ["Banking Dive: breach lawsuits, Apr 2026", BREACH]]),
        ]},
        {"id": "3.2", "ic": "gem", "name": "Membership tiers", "blurb": "Chime Plus and Prime.", "div": "chime", "rev": "payments", "products": [
            P("chimeplus", "Chime Plus", "For members with a $200 qualifying direct deposit (or $400 over 34 days): 2% cash back on one chosen Chime Card category (up from 1.5% in April 2026) and a higher savings rate.",
              s=["con"], lc="grow", o="B", neo=[0, "Rewards on Visa."], src=[["Chime: Chime Prime launch, Apr 2026", PRIME], ["Chime: Chime Card", CREDIT]]),
            P("chimeprime", "Chime Prime", "Launched 2 April 2026 for members with $3,000 or more of monthly direct deposits: 5% cash back on a chosen category up to $1,500 a month, 3.75% savings APY at launch (4.00% shown in October ⚠), priority support and travel perks. Prime members generate more than twice the average ARPAM.", short="Chime Prime",
              s=["prime"], lc="grow", st="new", ay="Apr 2026", o="B", neo=[0, "Visa Signature perks."],
              mc="Premium benefits are Visa's today; World Elite and Priceless are the Mastercard answer.",
              src=[["Chime: Chime Prime launch, Apr 2026", PRIME], ["American Banker: Chime Prime, Apr 2026", ABPRIME], ["Q2 2026 results", Q2]]),
        ]},
        {"id": "3.3", "ic": "gauge", "name": "Credit building", "blurb": "28 points in eight months.", "div": "chime", "rev": "payments", "products": [
            P("creditscore", "Credit-score building", "Chime Card activity reported to Experian, TransUnion and Equifax: an average gain of 28 points after about eight months, and up to 70 points for the top tenth of members.",
              s=["builder"], lc="borrow", o="P", at="Experian, TransUnion, Equifax", neo=[0, ""], src=[["Chime: Chime Card", CREDIT]]),
        ]},
        {"id": "3.4", "ic": "receipt-text", "name": "Tax & Trump Accounts", "blurb": "Free filing in the app.", "div": "chime", "rev": "platform", "products": [
            P("tax", "Free tax filing", "Free tax filing in the Chime app since January 2025, with april as the e-file provider.",
              s=["con"], lc="beyond", ay="Jan 2025", o="P", at="april", neo=[0, ""], src=[["Chime: Chime Prime launch, Apr 2026", PRIME], ["Chime newsroom", NEWS]]),
            P("trumpaccounts", "Trump Accounts enrolment", "IRS Form 4547 enrolment built into tax filing in 2026, and a $1,000 match for employees' eligible children.",
              s=["con", "saver"], lc="grow", st="new", ay="2026", o="B", neo=[0, ""], src=[["American Banker: Q4 2025", ABQ4]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What members use: fee-free checking and savings, liquidity from SpotMe, MyPay and Instant Loans, investing from $1, and Chime Enterprise for employers and their staff.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Checking & savings", "blurb": "No fees, up to 4% APY.", "div": "banks", "rev": "payments", "products": [
            P("checking", "Chime Checking", "No monthly fees or minimum balance; Chime says more Americans choose it as their primary account than any other institution, and J.D. Power found it opened the most new US checking accounts.",
              s=["con", "worker"], lc="everyday", o="P", at="The Bancorp Bank, Stride Bank", neo=[0, "Visa debit."], src=[["Chime home page", HOME], ["Q4 and FY2025 results", FY25], ["Chime: Chime Prime launch, Apr 2026", PRIME]]),
            P("savings", "Chime Savings", "High-yield savings with automatic saving and goals, up to 4.00% APY for Prime ⚠, with part of deposits swept to community banks.",
              s=["saver", "prime"], lc="grow", o="P", at="The Bancorp Bank, Stride Bank", neo=[0, ""], src=[["Chime home page", HOME], ["IPO prospectus, Jun 2025", PROSP]]),
        ]},
        {"id": "4.2", "ic": "hand-coins", "name": "Liquidity", "blurb": "SpotMe, MyPay, Instant Loans.", "div": "chime", "rev": "platform", "products": [
            P("spotme", "SpotMe", "Fee-free overdraft up to $200 for members with $200 of qualifying direct deposits, fully launched in 2019.",
              s=["worker", "con"], lc="borrow", ay="2019", o="B", neo=[0, "On the Visa debit card."], src=[["IPO prospectus, Jun 2025", PROSP], ["Financial Health Network: SpotMe, Apr 2026", FHN]]),
            P("mypay", "MyPay", "Earned wage access of up to $750 before payday (up to $500 at the July 2024 launch): $4.5 billion originated in Q2 2026 at a 0.9% loss rate, more than $400 million of annualised revenue.", short="MyPay",
              s=["worker"], lc="borrow", st="new", ay="Jul 2024", o="B", neo=[0, ""],
              mc="Billions of instant advances a quarter are payout volume for a push-to-card rail.",
              src=[["Q2 2026 results", Q2], ["Q1 2026 results", Q1], ["Chime home page", HOME]]),
            P("instantloans", "Instant Loans", "Small instalment loans serviced by Chime Capital (APR up to 35.99%): about $400 million originated in 2025, $300 million in Q2 2026 alone, and more than $100 million of annualised revenue expected by the end of Q3.",
              s=["worker", "prime"], lc="borrow", st="new", o="B", div="capital", neo=[0, ""],
              mc="Cash-flow underwriting on linked accounts is where open finance would help.",
              src=[["Q2 2026 results", Q2], ["Q4 and FY2025 results", FY25], ["Chime: Chime Prime launch, Apr 2026", PRIME]]),
        ]},
        {"id": "4.3", "ic": "trending-up", "name": "Investing", "blurb": "Chime Invest from $1.", "div": "invest", "rev": "platform", "products": [
            P("invest", "Chime Invest", "Commission-free stocks, ETFs and managed portfolios from $1, launched on 20 July 2026, with Atomic Invest and Atomic Brokerage.",
              s=["saver"], lc="grow", st="new", ay="Jul 2026", o="P", at="Atomic Invest, Atomic Brokerage", neo=[0, ""], src=[["PYMNTS: Chime Invest, Jul 2026", INVEST], ["Q2 2026 results", Q2]]),
        ]},
        {"id": "4.4", "ic": "briefcase-business", "name": "Chime Enterprise", "blurb": "Workplace through employers.", "div": "enterprise", "rev": "platform", "products": [
            P("workplace", "Chime Workplace", "A fee-free financial-wellness suite for employers and their staff, launched on 31 March 2025 after the Salt Labs deal: earned wage access, high-yield savings and credit-building tools.",
              s=["employer", "worker"], lc="open", st="new", ay="Mar 2025", o="A", neo=[0, ""],
              mc="Pay-on-demand payouts to staff cards could ride Mastercard Move.",
              src=[["Chime: Etech joins Chime Enterprise, Aug 2025", ETECH], ["IPO prospectus, Jun 2025", PROSP]]),
            P("employers", "Employer partners", "Etech and Ubiquity (2025), Cedarhurst, eXp Realty and LRS (February 2026), First Student (65,000+ staff) and Allied Universal; two Q2 2026 partners employ more than 350,000 people.",
              s=["employer"], lc="open", st="new", o="P", at="Allied Universal, First Student", neo=[0, ""], src=[["Chime Enterprise partners, Feb 2026", ENT26], ["Q1 2026 results", Q1], ["Q2 2026 results", Q2]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How members reach Chime: a mobile app with 24/7 support, employers and payroll, and a sports-heavy brand that does the selling.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Chime app", "blurb": "Mobile-only, 24/7.", "div": "chime", "rev": "payments", "products": [
            P("app", "Chime app", "A mobile-only bank with more than a million five-star app-store reviews and NerdWallet's best overall checking account for 2026.",
              s=["con", "builder", "prime", "worker", "saver"], lc="everyday", o="B", neo=[0, ""], src=[["Chime home page", HOME]]),
            P("support", "24/7 support", "Round-the-clock member support, with priority service for Prime members.",
              s=["con", "prime"], lc="everyday", o="B", neo=[0, ""], src=[["Chime home page", HOME], ["Chime: Chime Prime launch, Apr 2026", PRIME]]),
        ]},
        {"id": "5.2", "ic": "users-round", "name": "Employers & payroll", "blurb": "Direct deposit is the gate.", "div": "enterprise", "rev": "platform", "products": [
            P("channels", "Employers & channel partners", "Chime Enterprise signs employers and channel partners; switching payroll to Chime unlocks SpotMe and the Plus and Prime tiers.",
              s=["employer", "worker"], lc="open", o="P", neo=[0, ""], src=[["Q4 and FY2025 results", FY25], ["Chime: Chime Prime launch, Apr 2026", PRIME]]),
        ]},
        {"id": "5.3", "ic": "flag", "name": "Brand & sport", "blurb": "MLS, Portland Fire.", "div": "chime", "rev": "corp", "products": [
            P("sponsorship", "Brand & sponsorships", "Major League Soccer's retail banking partner and presenting sponsor of the 2026 MLS All-Star game, the Portland Fire jersey patch, and athletes such as Son Heung-min.",
              s=["con"], lc="open", st="new", o="P", at="MLS, Portland Fire", neo=[0, ""], src=[["Sports Business Journal: MLS All-Star, Jul 2026", MLS], ["Chime newsroom", NEWS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Chime", "blurb": "All Visa; Mastercard at the edges.", "products": [
        P("mcatchime", "Mastercard at Chime", "Chime's debit card, its Chime Card and its ATM network are all Visa, and no Chime–Mastercard programme was found. Mastercard touches Chime only at the edges: members can fund accounts from Mastercard debit cards ⚠ and instant transfers to Mastercard cards would ride Mastercard Send ⚠. Chime Bank, from 2027, makes the network Chime's own choice.",
          s=["con"], div="chime", rev="corp", mc="The relationship this map is drawn for.",
          src=[["Chime: debit card", DEBIT], ["Chime: Chime Card", CREDIT], ["Chime: agreement to acquire Stride Bank, Sep 2026", STRIDE]]),
    ]},
    {"id": "pillar-market", "name": "US consumer banking", "blurb": "Durbin, charters, wage access.", "products": [
        P("market", "The US market", "Visa took about 70% of combined Visa and Mastercard US card volume in 2025; the Durbin cap spares issuers under $10 billion, which is why Chime will keep Chime Bank small; fintechs are buying charters, and earned wage access and small-dollar credit are growing under CFPB and state oversight ⚠.",
          s=["con"], div="chime", rev="corp", src=[["Nilson: Mastercard and Visa in the US, 2025", NILSON], ["IPO prospectus, Jun 2025", PROSP], ["Chime: agreement to acquire Stride Bank, Sep 2026", STRIDE]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
