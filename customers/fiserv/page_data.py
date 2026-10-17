"""Fiserv, as a platform: the data behind ``Fiserv_Platform.html``.

``python customers/build_page.py fiserv`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Fiserv_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from fiserv_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from fiserv_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Fiserv'
PAGE = 'Fiserv_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Fiserv Platform"
KICKER = f"Fiserv, Inc. · as at {AS_OF}"
H1 = '<h1>Fiserv <span class="os">Platform</span></h1>'
SERVES = "who Fiserv serves"

PALETTE_NOTE = ("Palette: Fiserv's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Fiserv's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Fiserv's colours"

PIN = (43.04, -87.91, 'Milwaukee')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'merch': 'Merchant Solutions', 'fin': 'Financial Solutions', 'grp': 'Corporate'}
DIV = {'fiserv': 'Fiserv', 'clover': 'Clover', 'carat': 'Carat', 'star': 'STAR Network', 'fin': 'Financial Solutions'}
DEFAULT_DIV = 'fiserv'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F4F5", "panel-2": "#E7EAEB", "ink": "#0E1316", "ink-2": "#212629",
    "muted": "#4B5053", "faint": "#6C7174", "line": "#CDD1D3", "line-2": "#B0B6B8", "focus": "#254162",
    "accent": "#254162", "link": "#1C2F4A", "gold": "#254162", "gold-deep": "#18283F", "gold-ink": "#1C2F4A",
    "l1": "#111C2C", "l2": "#18283F", "l3": "#263753", "l4": "#465B70", "l5": "#2A2630",
    "lu": "#76717A", "l1f": "#213046", "l2f": "#254162", "l3f": "#435E7F", "l4f": "#849BAC",
    "l5f": "#443E4A", "luf": "#A5A1AA", "l1t": "#EEF4F9", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#101820", "l5t": "#FFFFFF", "slot": "#0E1316", "shadow": "rgba(15,24,31,.22)", "wash-a": "rgba(37,65,98,.14)",
    "wash-b": "rgba(132,155,172,.10)", "gb2": "#213046", "gb3": "#254162", "gb4": "#A3B8C5", "brand-grad": "linear-gradient(90deg,#213046,#FF6600 55%,#FFB27A)",
    "gold-grad": "linear-gradient(135deg,#A3B8C5 0%,#254162 45%,#18283F 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0B0C", "panel": "#131517", "panel-2": "#1B1E20", "ink": "#F3F5F6", "ink-2": "#D7DBDD",
    "muted": "#A8ADB0", "faint": "#868A8D", "line": "#2E3133", "line-2": "#43474A", "focus": "#7F9CB3",
    "accent": "#6E8CA5", "link": "#A3B8C5", "gold": "#6E8CA5", "gold-deep": "#7F9CB3", "gold-ink": "#A3B8C5",
    "l1": "#A3B8C5", "l2": "#8AA2B5", "l3": "#99ABC2", "l4": "#B9C9D3", "l5": "#D6D4D8",
    "lu": "#96919B", "l1f": "#213046", "l2f": "#254162", "l3f": "#435E7F", "l4f": "#849BAC",
    "l5f": "#76717A", "luf": "#76717A", "slot": "#060707", "wash-a": "rgba(37,65,98,.12)", "wash-b": "rgba(132,155,172,.06)",
    "gb2": "#213046", "gb3": "#254162", "gb4": "#A3B8C5", "gold-grad": "linear-gradient(135deg,#CCDAE3 0%,#6E8CA5 45%,#254162 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
