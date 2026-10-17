"""Amazon, as a platform: the data behind ``Amazon_Platform.html``.

``python customers/build_page.py amazon`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Amazon_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from amazon_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from amazon_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Amazon'
PAGE = 'Amazon_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Amazon Platform"
KICKER = f"Amazon.com, Inc., read through payments · as at {AS_OF}"
H1 = '<h1>Amazon <span class="os">Platform</span></h1>'
SERVES = 'who Amazon serves'

PALETTE_NOTE = ("Palette: Amazon's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Amazon's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Amazon's colours"

PIN = (47.62, -122.34, 'Seattle')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'na': 'North America', 'intl': 'International', 'aws': 'AWS', 'grp': 'Corporate'}
DIV = {'amazon': 'Amazon', 'pay': 'Amazon Pay', 'aws': 'AWS', 'business': 'Amazon Business', 'india': 'Amazon Pay India', 'grp': 'Amazon.com, Inc.'}
DEFAULT_DIV = 'amazon'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F3F2", "panel-2": "#F0EAE7", "ink": "#21160D", "ink-2": "#46362A",
    "muted": "#958A7A", "faint": "#A59F97", "line": "#E0DCD6", "line-2": "#D2CDC6", "focus": "#D68100",
    "accent": "#D68100", "link": "#905F00", "gold": "#D68100", "gold-deep": "#8C5C00", "gold-ink": "#905F00",
    "l1": "#573900", "l2": "#8C5C00", "l3": "#CB9114", "l4": "#C99856", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#9E6F13", "l2f": "#FF9900", "l3f": "#DDA64A", "l4f": "#D7B99B",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#21160D", "shadow": "rgba(53,31,8,.22)", "wash-a": "rgba(255,153,0,.14)",
    "wash-b": "rgba(215,185,155,.10)", "gb2": "#9E6F13", "gb3": "#FF9900", "gb4": "#E5CAB3", "brand-grad": "linear-gradient(90deg,#8C5C00,#FF9900 55%,#E5CAB3)",
    "gold-grad": "linear-gradient(135deg,#E5CAB3 0%,#FF9900 45%,#8C5C00 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0C0A", "panel": "#201A16", "panel-2": "#312922", "ink": "#F7F4F3", "ink-2": "#E6DFDC",
    "muted": "#CCC8C1", "faint": "#B4B0AA", "line": "#5C5346", "line-2": "#8F8474", "focus": "#FF9900",
    "accent": "#FF9900", "link": "#E5CAB3", "gold": "#FF9900", "gold-deep": "#E1BB92", "gold-ink": "#E5CAB3",
    "l1": "#E5CAB3", "l2": "#DFBE9D", "l3": "#E7D0A8", "l4": "#EBD5C2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#9E6F13", "l2f": "#FF9900", "l3f": "#DDA64A", "l4f": "#D7B99B",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090605", "wash-a": "rgba(255,153,0,.12)", "wash-b": "rgba(215,185,155,.06)",
    "gb2": "#9E6F13", "gb3": "#FF9900", "gb4": "#E5CAB3", "gold-grad": "linear-gradient(135deg,#F3DDCC 0%,#D9B185 45%,#FF9900 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
