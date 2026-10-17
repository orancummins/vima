"""DBS Group, as a platform: the data behind ``DBS_Platform.html``.

``python customers/build_page.py dbs`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``DBS_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from dbs_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from dbs_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'DBS'
PAGE = 'DBS_Platform.html'
AS_OF = "17 October 2026"
TITLE = "DBS Platform"
KICKER = f"DBS Group Holdings · as at {AS_OF}"
H1 = '<h1>DBS <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: DBS's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in DBS's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in DBS's colours"

PIN = (1.28, 103.85, 'Singapore')
PIN_FACING = 'Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'cbg': 'Consumer Banking/Wealth Management', 'ibg': 'Institutional Banking', 'gfm': 'Markets Trading', 'oth': 'Others'}
DIV = {'dbs': 'DBS Group', 'posb': 'POSB', 'hk': 'DBS Hong Kong', 'tw': 'DBS Taiwan', 'india': 'DBS India', 'treasures': 'DBS Treasures', 'ddex': 'DBS Digital Exchange', 'paylah': 'DBS PayLah!'}
DEFAULT_DIV = 'dbs'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F2F3", "panel-2": "#F1E8EA", "ink": "#230E10", "ink-2": "#503136",
    "muted": "#7B6262", "faint": "#938383", "line": "#E4DBDB", "line-2": "#D4C8C8", "focus": "#FF3333",
    "accent": "#FF3333", "link": "#CD0C00", "gold": "#FF3333", "gold-deep": "#A20900", "gold-ink": "#CD0C00",
    "l1": "#620500", "l2": "#A20900", "l3": "#E93222", "l4": "#D4787A", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#BA2016", "l2f": "#FF3333", "l3f": "#E4716F", "l4f": "#DFAFB4",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#230E10", "shadow": "rgba(58,9,13,.22)", "wash-a": "rgba(255,51,51,.14)",
    "wash-b": "rgba(223,175,180,.10)", "gb2": "#BA2016", "gb3": "#FF3333", "gb4": "#EAC2C8", "brand-grad": "linear-gradient(90deg,#A20900,#FF3333 55%,#EAC2C8)",
    "gold-grad": "linear-gradient(135deg,#EAC2C8 0%,#FF3333 45%,#A20900 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#100B0C", "panel": "#23181A", "panel-2": "#382628", "ink": "#F8F3F4", "ink-2": "#E8DFE2",
    "muted": "#D6CDCD", "faint": "#C3BBBB", "line": "#6C5252", "line-2": "#A59090", "focus": "#FF3333",
    "accent": "#FF3333", "link": "#EAC2C8", "gold": "#FF3333", "gold-deep": "#E7A8AE", "gold-ink": "#EAC2C8",
    "l1": "#EAC2C8", "l2": "#E5B1B6", "l3": "#ECBBB9", "l4": "#EECCD1", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#BA2016", "l2f": "#FF3333", "l3f": "#E4716F", "l4f": "#DFAFB4",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090607", "wash-a": "rgba(255,51,51,.12)", "wash-b": "rgba(223,175,180,.06)",
    "gb2": "#BA2016", "gb3": "#FF3333", "gb4": "#EAC2C8", "gold-grad": "linear-gradient(135deg,#F4D1D7 0%,#E19EA3 45%,#FF3333 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
