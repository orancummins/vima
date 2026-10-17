"""Citizens' Foundation layer, as at 17 October 2026 (see page_data.py for the format)."""
# ruff: noqa: E501

SEC = "https://www.sec.gov/Archives/edgar/data/"
Q3R = SEC + "0000759944/000075994426000206/a3q26earningsrelease.htm"
Q3F = SEC + "0000759944/000075994426000206/q326financialsupplement.htm"
Q4R = SEC + "759944/000075994426000017/a4q25earningsrelease.htm"
K10 = SEC + "759944/000075994426000028/cfg-20251231.htm"
NEWS = "https://investor.citizensbank.com/about-us/newsroom/latest-news/"
RATINGS = "https://investor.citizensbank.com/about-us/investor-relations/fixed-income-capital-information/credit-ratings.aspx"
CALL4Q = "https://finance.yahoo.com/news/citizens-financial-group-q4-earnings-162728449.html"
BD_AI = "https://www.bankingdive.com/news/citizens-ai-banking-reimagine-coughlin/815965/"
CIO = "https://tearsheet.co/banking/citizens-cio-on-the-ethos-that-led-the-bank-into-the-cloud-and-beyond/"
SEMAFOR = "https://www.semafor.com/article/07/24/2026/how-bruce-van-saun-united-citizens-against-americas-biggest-banks"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · charter · brand", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a $234 billion balance sheet, a board in the middle of a CEO succession, a Providence charter from 1828 and the RBS years, a bank that moved every application to the cloud, and a plan to earn 16 to 18% on tangible equity by late 2027.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & capital", "blurb": "$234 billion, CET1 10.5%.", "div": "cfg", "rev": "oth", "products": [
            P("balance", "Balance sheet", "Total assets of $234.5 billion, deposits of $185.2 billion and loans of $148.2 billion at 30 September 2026 (a loan-to-deposit ratio of 80%); commercial loans are about $77 billion and consumer loans about $71 billion, led by $37 billion of mortgages and $21 billion of home equity.",
              s=["inst"], neo=[0, ""], src=[["3Q26 earnings release", Q3R], ["3Q26 financial supplement", Q3F]]),
            P("earnings", "Earnings", "Revenue of $8.2 billion and net income of $1.83 billion in 2025; in 3Q26 revenue of $2.32 billion, net income of $636 million (up 29%) and a return on tangible common equity of 15.1%, up from 9.8% for 2024.",
              s=["inst"], neo=[0, ""], src=[["3Q26 earnings release", Q3R], ["4Q25 earnings release", Q4R]]),
            P("capital", "Capital & ratings", "CET1 ratio of 10.5%. Citizens Financial Group is rated BBB+ by S&P, Baa1 by Moody's and A- by Fitch, all stable; Citizens Bank, N.A. is A-, A3 and A-. The dividend rose to $0.52 in 3Q26 and the buyback authorisation to $1.95 billion.",
              s=["inst"], neo=[0, ""], src=[["Citizens: credit ratings, Sep 2026", RATINGS], ["3Q26 earnings release", Q3R]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Governance & leadership", "blurb": "A succession in view.", "div": "cfg", "rev": "oth", "products": [
            P("leadership", "Board & leadership", "Bruce Van Saun has been CEO since 2013 and is chairman; Brendan Coughlin, president since April 2025, has run Consumer, the Private Bank, Wealth and, since July 2026, Commercial Banking, and is seen as the likely successor. CFO Aunoy Banerjee (from October 2025); Ted Swimmer heads Commercial Banking, Sue deTray the Private Bank, Paul Casey Wealth, and Michael Ruttledge is CIO.",
              s=["inst"], neo=[0, ""], src=[["Citizens: Coughlin adds Commercial Banking, Jul 2026", NEWS + "2026/2026-07-08-213032849.aspx"], ["American Banker: Coughlin as next CEO, Jul 2026", "https://www.americanbanker.com/news/citizens-latest-move-further-positions-coughlin-as-next-ceo"]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Brand & heritage", "blurb": "Providence, 1828.", "div": "cfg", "rev": "oth", "products": [
            P("heritage", "High Street to Citizens", "Founded in Providence in 1828 as High Street Bank; owned by the Royal Bank of Scotland from 1988, which built it through Mellon's retail bank (2001) and Charter One (2004); floated on the NYSE in September 2014, the largest traditional US bank IPO, with RBS fully out in 2015. Market value about $27 billion in mid-October 2026.",
              s=["inst", "con"], o="I", neo=[0, ""], src=[["FY2025 10-K", K10], ["StockAnalysis: CFG", "https://stockanalysis.com/stocks/CFG/"]]),
            P("buildout", "The buildout by acquisition", "Franklin American Mortgage (2018), Clarfeld Financial Advisors (2019), JMP Group (2021, about $149 million), 80 HSBC East Coast branches and its online deposits (February 2022) and Investors Bancorp ($3.5 billion, April 2022), which took Citizens into the New York metro; then about 50 First Republic private bankers in 2023 after it lost the bids for SVB and First Republic.", short="Acquisitions 2018–23",
              s=["con", "aff", "corp"], o="A", neo=[0, ""], src=[["8-K: JMP closing, Nov 2021", SEC + "759944/000075994421000155/jmpclosingpressrelease.htm"], ["8-K: HSBC branches closing, Feb 2022", SEC + "759944/000075994422000022/hsbcclosingpressrelease.htm"], ["Banking Dive: Private Bank expansion, Mar 2026", "https://www.bankingdive.com/news/citizens-private-bank-expansion-hiring-wealth-coughlin/814399/"]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & data core", "blurb": "All in the cloud.", "div": "cfg", "rev": "oth", "products": [
            P("cloud", "Cloud & core", "Every business application runs on AWS or Azure, which Citizens calls a first for a super-regional bank; the last data centres are closing and moving off mainframes is one of five 'Next Gen Technology' pillars. FIS and Fiserv are the incumbent cores, and the president has questioned whether they will modernise fast enough. Infosys is the main engineering partner, including an AI hub in Bengaluru (February 2026).",
              s=["inst"], o="P", at="AWS, Microsoft, FIS, Fiserv, Infosys", neo=[0, ""], src=[["Tearsheet: Citizens' CIO on the cloud, Feb 2026", CIO], ["Banking Dive: Coughlin on AI, Mar 2026", BD_AI], ["Infosys: AI-first innovation hub, Feb 2026", "https://www.infosys.com/newsroom/press-releases/2026/collaborates-ai-first-innovation-hub.html"]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy", "blurb": "16–18% returns by late 2027.", "div": "cfg", "rev": "oth", "products": [
            P("strategy", "Return targets", "A return on tangible common equity of 16 to 18% by the second half of 2027 (15.1% in 3Q26), with 2026 guidance of net interest income up 10 to 12% and more than 500 basis points of positive operating leverage; buybacks of $700–850 million planned for 2026.",
              s=["inst"], neo=[0, ""], src=[["4Q25 call highlights, Jan 2026", CALL4Q], ["3Q26 earnings release", Q3R]]),
            P("reimagine", "Reimagine the Bank", "About 50 initiatives (AI, vendor consolidation, a smaller office footprint and simpler processes) aimed at about $100 million of pre-tax run-rate benefit by the end of 2026 and about $450 million by the end of 2028; it succeeded the TOP ('Tapping Our Potential') programmes.", short="Reimagine the Bank",
              s=["inst"], st="new", ay="2025", neo=[0, "Vendor consolidation could favour broader Mastercard bundles."],
              src=[["Banking Dive: Coughlin on AI, Mar 2026", BD_AI], ["PYMNTS: Reimagine the Bank, Jul 2026", "https://www.pymnts.com/?p=3968233"]]),
            P("onecitizens", "One Citizens & the New York push", "Private bankers and commercial bankers referring clients to each other (about 400 referrals a year), and a New York metro branch share of 2.1% against a target of 3 to 5%.",
              s=["aff", "sme", "corp"], neo=[0, ""], src=[["Semafor: Van Saun profile, Jul 2026", SEMAFOR], ["Banking Dive: Coughlin on AI, Mar 2026", BD_AI]]),
        ]},
    ],
}
