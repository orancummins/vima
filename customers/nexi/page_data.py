"""Nexi Group, as a platform: the data behind ``Nexi_Platform.html``.

``python customers/build_page.py nexi`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Nexi_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from nexi_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from nexi_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Nexi'
PAGE = 'Nexi_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Nexi Platform"
KICKER = f"Nexi Group · as at {AS_OF}"
H1 = '<h1>Nexi <span class="os">Platform</span></h1>'
SERVES = 'who Nexi serves'

PALETTE_NOTE = ("Palette: Nexi's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Nexi's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Nexi's colours"

PIN = (45.46, 9.19, 'Milan')
PIN_FACING = 'Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'ms': 'Merchant Solutions', 'iss': 'Issuing Solutions', 'dbs': 'Digital Banking Solutions', 'grp': 'Group'}
DIV = {'grp': 'Nexi Group', 'nexi': 'Nexi', 'nets': 'Nets', 'sia': 'SIA', 'computop': 'Computop', 'p24': 'Przelewy24'}
DEFAULT_DIV = 'grp'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F3F3F5", "panel-2": "#E8EAED", "ink": "#10111A", "ink-2": "#2B2E39",
    "muted": "#6D6D7C", "faint": "#8A8A93", "line": "#D4D4DB", "line-2": "#C0C0C8", "focus": "#2D32AA",
    "accent": "#2D32AA", "link": "#211F77", "gold": "#2D32AA", "gold-deep": "#1B1A61", "gold-ink": "#211F77",
    "l1": "#11103E", "l2": "#1B1A61", "l3": "#35328B", "l4": "#585DA4", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#2B296F", "l2f": "#2D32AA", "l3f": "#5253B4", "l4f": "#9A9FC2",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#10111A", "shadow": "rgba(16,19,40,.22)", "wash-a": "rgba(45,50,170,.14)",
    "wash-b": "rgba(154,159,194,.10)", "gb2": "#2B296F", "gb3": "#2D32AA", "gb4": "#B3B9D5", "brand-grad": "linear-gradient(90deg,#1B1A61,#2D32AA 55%,#B3B9D5)",
    "gold-grad": "linear-gradient(135deg,#B3B9D5 0%,#2D32AA 45%,#1B1A61 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0B0B0D", "panel": "#16171C", "panel-2": "#22232A", "ink": "#F3F4F6", "ink-2": "#DCDDE2",
    "muted": "#BABAC1", "faint": "#9F9FA6", "line": "#41414C", "line-2": "#676875", "focus": "#949BC9",
    "accent": "#868DBF", "link": "#B3B9D5", "gold": "#868DBF", "gold-deep": "#949BC9", "gold-ink": "#B3B9D5",
    "l1": "#B3B9D5", "l2": "#9EA4CA", "l3": "#AAAAD4", "l4": "#C3C8DF", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#2B296F", "l2f": "#2D32AA", "l3f": "#5253B4", "l4f": "#9A9FC2",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060708", "wash-a": "rgba(45,50,170,.12)", "wash-b": "rgba(154,159,194,.06)",
    "gb2": "#2B296F", "gb3": "#2D32AA", "gb4": "#B3B9D5", "gold-grad": "linear-gradient(135deg,#D0D5E9 0%,#868DBF 45%,#2D32AA 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
