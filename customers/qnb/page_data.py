"""QNB Group, as a platform: the data behind ``QNB_Group_Platform.html``.

``python customers/build_page.py qnb`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``QNB_Group_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from qnb_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from qnb_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'QNB'
PAGE = 'QNB_Group_Platform.html'
AS_OF = "17 October 2026"
TITLE = "QNB Platform"
KICKER = f"QNB Group · as at {AS_OF}"
H1 = '<h1>QNB <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: QNB's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in QNB's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in QNB's colours"

PIN = (25.29, 51.53, 'Doha')
PIN_FACING = 'the Middle East'

ALLOWED_MENTIONS: tuple[str, ...] = ('Saudi',)

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Consumer Banking', 'corp': 'Corporate & Institutional Banking', 'awm': 'Asset & Wealth Management', 'intl': 'International Banking'}
DIV = {'qnb': 'QNB Group', 'qatar': 'QNB Qatar', 'turkiye': 'QNB Türkiye', 'enpara': 'Enpara Bank', 'egypt': 'QNB Egypt', 'branches': 'International branches'}
DEFAULT_DIV = 'qnb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E4ECEE", "ink": "#0A1319", "ink-2": "#1A252A",
    "muted": "#3E464E", "faint": "#616970", "line": "#C7CFD6", "line-2": "#A7B1BA", "focus": "#003D74",
    "accent": "#003D74", "link": "#002A5B", "gold": "#003D74", "gold-deep": "#00254F", "gold-ink": "#002A5B",
    "l1": "#001B39", "l2": "#00254F", "l3": "#0A305F", "l4": "#28577D", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0A2B52", "l2f": "#003D74", "l3f": "#1C5996", "l4f": "#659EC1",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A1319", "shadow": "rgba(6,25,38,.22)", "wash-a": "rgba(0,61,116,.14)",
    "wash-b": "rgba(101,158,193,.10)", "gb2": "#0A2B52", "gb3": "#003D74", "gb4": "#89BDD7", "brand-grad": "linear-gradient(90deg,#00254F,#003D74 55%,#89BDD7)",
    "gold-grad": "linear-gradient(135deg,#89BDD7 0%,#003D74 45%,#00254F 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090B0D", "panel": "#101518", "panel-2": "#161D21", "ink": "#F2F6F7", "ink-2": "#D3DCDF",
    "muted": "#9FA8B0", "faint": "#7C848B", "line": "#262C31", "line-2": "#373D44", "focus": "#57A2D1",
    "accent": "#4390C4", "link": "#89BDD7", "gold": "#4390C4", "gold-deep": "#57A2D1", "gold-ink": "#89BDD7",
    "l1": "#89BDD7", "l2": "#68A7CE", "l3": "#79A9DA", "l4": "#A5CDE2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0A2B52", "l2f": "#003D74", "l3f": "#1C5996", "l4f": "#659EC1",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050708", "wash-a": "rgba(0,61,116,.12)", "wash-b": "rgba(101,158,193,.06)",
    "gb2": "#0A2B52", "gb3": "#003D74", "gb4": "#89BDD7", "gold-grad": "linear-gradient(135deg,#BDDFF0 0%,#4390C4 45%,#003D74 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
