"""HBL, as a platform: the data behind ``HBL_Platform.html``.

``python customers/build_page.py hbl`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``HBL_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from hbl_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from hbl_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'HBL'
PAGE = 'HBL_Platform.html'
AS_OF = "17 October 2026"
TITLE = "HBL Platform"
KICKER = f"Habib Bank Limited · as at {AS_OF}"
H1 = '<h1>HBL <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: HBL's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in HBL's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in HBL's colours"

PIN = (24.86, 67.01, 'Karachi')
PIN_FACING = 'Pakistan, the Gulf and China'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail, consumer, SME & agriculture', 'corp': 'Corporate, commercial & investment banking', 'treasury': 'Treasury & financial institutions', 'incl': 'Branchless banking & microfinance', 'intl': 'International & correspondent'}
DIV = {'hbl': 'HBL', 'konnect': 'Konnect by HBL', 'mfb': 'HBL Microfinance Bank', 'islamic': 'HBL Islamic Banking', 'intl': 'HBL International', 'amc': 'HBL Asset Management', 'zarai': 'HBL Zarai Services'}
DEFAULT_DIV = 'hbl'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F4", "panel-2": "#E4EEEB", "ink": "#0A1A17", "ink-2": "#1B2D29",
    "muted": "#435453", "faint": "#667574", "line": "#C8D6D6", "line-2": "#A9BCBB", "focus": "#008078",
    "accent": "#008078", "link": "#006261", "gold": "#008078", "gold-deep": "#005453", "gold-ink": "#006261",
    "l1": "#003B3B", "l2": "#005453", "l3": "#0A6769", "l4": "#2B857D", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0B5858", "l2f": "#008078", "l3f": "#1E9E99", "l4f": "#69C3B4",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A1A17", "shadow": "rgba(6,39,35,.22)", "wash-a": "rgba(0,128,120,.14)",
    "wash-b": "rgba(105,195,180,.10)", "gb2": "#0B5858", "gb3": "#008078", "gb4": "#8DD8C9", "brand-grad": "linear-gradient(90deg,#005453,#008078 55%,#8DD8C9)",
    "gold-grad": "linear-gradient(135deg,#8DD8C9 0%,#008078 45%,#005453 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090D0C", "panel": "#111917", "panel-2": "#172220", "ink": "#F2F7F5", "ink-2": "#D4E0DC",
    "muted": "#A2B3B2", "faint": "#808F8E", "line": "#283534", "line-2": "#3C4A49", "focus": "#5CD2C0",
    "accent": "#49C6B5", "link": "#8DD8C9", "gold": "#49C6B5", "gold-deep": "#5CD2C0", "gold-ink": "#8DD8C9",
    "l1": "#8DD8C9", "l2": "#6CCFBF", "l3": "#7DDBD8", "l4": "#A8E3D7", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0B5858", "l2f": "#008078", "l3f": "#1E9E99", "l4f": "#69C3B4",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050807", "wash-a": "rgba(0,128,120,.12)", "wash-b": "rgba(105,195,180,.06)",
    "gb2": "#0B5858", "gb3": "#008078", "gb4": "#8DD8C9", "gold-grad": "linear-gradient(135deg,#BEF0E5 0%,#49C6B5 45%,#008078 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
