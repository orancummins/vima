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
    "ground": "#FFFFFF", "panel": "#F7F2F2", "panel-2": "#F0E8E7", "ink": "#21120D", "ink-2": "#46312A",
    "muted": "#75675D", "faint": "#8D827C", "line": "#E0DAD6", "line-2": "#D2CBC6", "focus": "#FA6400",
    "accent": "#FA6400", "link": "#AA4E00", "gold": "#FA6400", "gold-deep": "#8C4000", "gold-ink": "#AA4E00",
    "l1": "#572800", "l2": "#8C4000", "l3": "#CB6C14", "l4": "#C98156", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#9E5313", "l2f": "#FF6600", "l3f": "#DD884A", "l4f": "#D7AD9B",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#21120D", "shadow": "rgba(53,22,8,.22)", "wash-a": "rgba(255,102,0,.14)",
    "wash-b": "rgba(215,173,155,.10)", "gb2": "#9E5313", "gb3": "#FF6600", "gb4": "#E5C0B3", "brand-grad": "linear-gradient(90deg,#8C4000,#FF6600 55%,#E5C0B3)",
    "gold-grad": "linear-gradient(135deg,#E5C0B3 0%,#FF6600 45%,#8C4000 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0A", "panel": "#201816", "panel-2": "#312622", "ink": "#F7F3F3", "ink-2": "#E6DDDC",
    "muted": "#CCC5C1", "faint": "#B4AEAA", "line": "#5C4F46", "line-2": "#8F7F74", "focus": "#FF6600",
    "accent": "#FF6600", "link": "#E5C0B3", "gold": "#FF6600", "gold-deep": "#E1AB92", "gold-ink": "#E5C0B3",
    "l1": "#E5C0B3", "l2": "#DFB19D", "l3": "#E7C3A8", "l4": "#EBCDC2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#9E5313", "l2f": "#FF6600", "l3f": "#DD884A", "l4f": "#D7AD9B",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090605", "wash-a": "rgba(255,102,0,.12)", "wash-b": "rgba(215,173,155,.06)",
    "gb2": "#9E5313", "gb3": "#FF6600", "gb4": "#E5C0B3", "gold-grad": "linear-gradient(135deg,#F3D5CC 0%,#D9A185 45%,#FF6600 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
