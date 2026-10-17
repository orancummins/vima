"""Wise, as a platform: the data behind ``Wise_Platform.html``.

``python customers/build_page.py wise`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Wise_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from wise_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from wise_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Wise'
PAGE = 'Wise_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Wise Platform"
KICKER = f"Wise · as at {AS_OF}"
H1 = '<h1>Wise <span class="os">Platform</span></h1>'
SERVES = 'who Wise serves'

PALETTE_NOTE = ("Palette: Wise's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Wise's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Wise's colours"

PIN = (51.52, -0.08, 'London')
PIN_FACING = 'Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'xb': 'Cross-border revenue', 'card': 'Card revenue', 'other': 'Other transaction revenue', 'interest': 'Interest income', 'grp': 'Group'}
DIV = {'wise': 'Wise (personal)', 'biz': 'Wise Business', 'plat': 'Wise Platform', 'assets': 'Wise Assets', 'us': 'Wise US Inc.', 'grp': 'Wise Group plc'}
DEFAULT_DIV = 'wise'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F5F6F3", "panel-2": "#EEF0EA", "ink": "#1A2212", "ink-2": "#48533A",
    "muted": "#66705F", "faint": "#848C7E", "line": "#E3E6E0", "line-2": "#C8CEC5", "focus": "#51A51A",
    "accent": "#51A51A", "link": "#367A14", "gold": "#51A51A", "gold-deep": "#449A19", "gold-ink": "#367A14",
    "l1": "#295B0F", "l2": "#449A19", "l3": "#7ED457", "l4": "#B2D29B", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#5DB632", "l2f": "#9FE870", "l3f": "#B0DB97", "l4f": "#D1DFC3",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#0B0F14", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#1A2212", "shadow": "rgba(35,55,17,.22)", "wash-a": "rgba(159,232,112,.14)",
    "wash-b": "rgba(209,223,195,.10)", "gb2": "#5DB632", "gb3": "#9FE870", "gb4": "#DFEAD2", "brand-grad": "linear-gradient(90deg,#449A19,#9FE870 55%,#DFEAD2)",
    "gold-grad": "linear-gradient(135deg,#DFEAD2 0%,#9FE870 45%,#449A19 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0E100C", "panel": "#20241B", "panel-2": "#33392C", "ink": "#F6F7F4", "ink-2": "#E7E9E3",
    "muted": "#DADDD8", "faint": "#CACDC9", "line": "#67745F", "line-2": "#ACB4A7", "focus": "#9FE870",
    "accent": "#9FE870", "link": "#DFEAD2", "gold": "#9FE870", "gold-deep": "#D1E4BF", "gold-ink": "#DFEAD2",
    "l1": "#DFEAD2", "l2": "#D4E4C5", "l3": "#D7EACC", "l4": "#E3EDD8", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#5DB632", "l2f": "#9FE870", "l3f": "#B0DB97", "l4f": "#D1DFC3",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080906", "wash-a": "rgba(159,232,112,.12)", "wash-b": "rgba(209,223,195,.06)",
    "gb2": "#5DB632", "gb3": "#9FE870", "gb4": "#DFEAD2", "gold-grad": "linear-gradient(135deg,#E6F1DA 0%,#CADFB7 45%,#9FE870 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
