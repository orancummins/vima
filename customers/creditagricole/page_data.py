"""Crédit Agricole, as a platform: the data behind ``Credit_Agricole_Platform.html``.

``python customers/build_page.py creditagricole`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Credit_Agricole_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from creditagricole_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from creditagricole_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Crédit Agricole'
PAGE = 'Credit_Agricole_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Crédit Agricole Platform"
KICKER = f"Crédit Agricole Group · as at {AS_OF}"
H1 = '<h1>Crédit Agricole <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Crédit Agricole's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Crédit Agricole's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Crédit Agricole's colours"

PIN = (48.82, 2.32, 'Montrouge')
PIN_FACING = 'Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail Banking (Regional Banks, LCL, international)', 'ag': 'Asset Gathering', 'sfs': 'Specialised Financial Services', 'lc': 'Large Customers', 'cc': 'Corporate Centre'}
DIV = {'group': 'Crédit Agricole Group', 'rb': 'Regional Banks', 'lcl': 'LCL', 'italia': 'Crédit Agricole Italia', 'intl': 'CA Polska, Egypt & Ukraine', 'caps': 'CA Payment Services & CAWL', 'capfm': 'CA Personal Finance & Mobility', 'large': 'CACIB, CACEIS & Amundi'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F3", "panel-2": "#E3EEE8", "ink": "#091913", "ink-2": "#192922",
    "muted": "#3B4A46", "faint": "#5E6D69", "line": "#C6D5D1", "line-2": "#A5B8B3", "focus": "#006C50",
    "accent": "#006C50", "link": "#005645", "gold": "#006C50", "gold-deep": "#004B3C", "gold-ink": "#005645",
    "l1": "#00372C", "l2": "#004B3C", "l3": "#09594B", "l4": "#267861", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#094D40", "l2f": "#006C50", "l3f": "#1B9074", "l4f": "#61C09E",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#091913", "shadow": "rgba(6,37,26,.22)", "wash-a": "rgba(0,108,80,.14)",
    "wash-b": "rgba(97,192,158,.10)", "gb2": "#094D40", "gb3": "#006C50", "gb4": "#87D6B7", "brand-grad": "linear-gradient(90deg,#004B3C,#006C50 55%,#87D6B7)",
    "gold-grad": "linear-gradient(135deg,#87D6B7 0%,#006C50 45%,#004B3C 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090D0B", "panel": "#101714", "panel-2": "#16201C", "ink": "#F2F7F4", "ink-2": "#D2DFD8",
    "muted": "#9DAFAA", "faint": "#798985", "line": "#242F2C", "line-2": "#333F3C", "focus": "#53D0A5",
    "accent": "#3FC397", "link": "#87D6B7", "gold": "#3FC397", "gold-deep": "#53D0A5", "gold-ink": "#87D6B7",
    "l1": "#87D6B7", "l2": "#65CDA7", "l3": "#76D9C3", "l4": "#A3E1C9", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#094D40", "l2f": "#006C50", "l3f": "#1B9074", "l4f": "#61C09E",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050806", "wash-a": "rgba(0,108,80,.12)", "wash-b": "rgba(97,192,158,.06)",
    "gb2": "#094D40", "gb3": "#006C50", "gb4": "#87D6B7", "gold-grad": "linear-gradient(135deg,#BCEFDA 0%,#3FC397 45%,#006C50 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
