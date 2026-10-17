"""Uber Technologies, as a platform: the data behind ``Uber_Platform.html``.

``python customers/build_page.py uber`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Uber_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from uber_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from uber_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Uber'
PAGE = 'Uber_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Uber Platform"
KICKER = f"Uber Technologies, Inc., read through payments · as at {AS_OF}"
H1 = '<h1>Uber <span class="os">Platform</span></h1>'
SERVES = 'who Uber serves'

PALETTE_NOTE = ("Palette: Uber's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Uber's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Uber's colours"

PIN = (37.77, -122.39, 'San Francisco')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'mob': 'Mobility', 'del': 'Delivery', 'frt': 'Freight', 'grp': 'Corporate'}
DIV = {'uber': 'Uber', 'eats': 'Uber Eats', 'pro': 'Uber Pro & earner money', 'pay': 'Uber Payments', 'biz': 'Uber for Business', 'freight': 'Uber Freight', 'grp': 'Uber Technologies, Inc.'}
DEFAULT_DIV = 'uber'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F3F3F3", "panel-2": "#E7E8E8", "ink": "#0E0F10", "ink-2": "#181919",
    "muted": "#292A2A", "faint": "#515253", "line": "#C8C9CA", "line-2": "#A3A4A5", "focus": "#191C1F",
    "accent": "#191C1F", "link": "#181B1E", "gold": "#191C1F", "gold-deep": "#171A1D", "gold-ink": "#181B1E",
    "l1": "#141618", "l2": "#171A1D", "l3": "#191B1D", "l4": "#35393C", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#191B1D", "l2f": "#191C1F", "l3f": "#3B4044", "l4f": "#7D8388",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0E0F10", "shadow": "rgba(17,18,20,.22)", "wash-a": "rgba(25,28,31,.14)",
    "wash-b": "rgba(125,131,136,.10)", "gb2": "#191B1D", "gb3": "#191C1F", "gb4": "#9FA6A9", "brand-grad": "linear-gradient(90deg,#171A1D,#191C1F 55%,#9FA6A9)",
    "gold-grad": "linear-gradient(135deg,#9FA6A9 0%,#191C1F 45%,#171A1D 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0A0A", "panel": "#111111", "panel-2": "#151616", "ink": "#F4F4F4", "ink-2": "#D5D6D6",
    "muted": "#999B9C", "faint": "#707172", "line": "#232323", "line-2": "#333535", "focus": "#7C858B",
    "accent": "#717A7F", "link": "#9FA6A9", "gold": "#717A7F", "gold-deep": "#7C858B", "gold-ink": "#9FA6A9",
    "l1": "#9FA6A9", "l2": "#858D92", "l3": "#969CA2", "l4": "#B8BCBF", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#191B1D", "l2f": "#191C1F", "l3f": "#3B4044", "l4f": "#7D8388",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060606", "wash-a": "rgba(25,28,31,.12)", "wash-b": "rgba(125,131,136,.06)",
    "gb2": "#191B1D", "gb3": "#191C1F", "gb4": "#9FA6A9", "gold-grad": "linear-gradient(135deg,#CFD3D5 0%,#6A7277 45%,#191C1F 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
