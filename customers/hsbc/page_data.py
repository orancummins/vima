"""HSBC Holdings, as a platform: the data behind ``HSBC_Platform.html``.

``python customers/build_page.py hsbc`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``HSBC_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from hsbc_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from hsbc_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'HSBC'
PAGE = 'HSBC_Platform.html'
AS_OF = "17 October 2026"
TITLE = "HSBC Platform"
KICKER = f"HSBC Holdings · as at {AS_OF}"
H1 = '<h1>HSBC <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: HSBC's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in HSBC's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in HSBC's colours"

PIN = (51.505, -0.02, 'London')
PIN_FACING = 'Asia and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'hk': 'Hong Kong', 'uk': 'UK', 'cib': 'Corporate & Institutional Banking', 'iwpb': 'International Wealth & Premier Banking', 'cc': 'Corporate Centre'}
DIV = {'hsbc': 'HSBC Holdings', 'uk': 'HSBC UK', 'hk': 'HSBC Hong Kong', 'hangseng': 'Hang Seng Bank', 'fd': 'first direct', 'innov': 'HSBC Innovation Bank', 'mx': 'HSBC Mexico', 'me': 'HSBC Middle East'}
DEFAULT_DIV = 'hsbc'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F3", "panel-2": "#EFE6E9", "ink": "#1F0C0F", "ink-2": "#3F262C",
    "muted": "#84696B", "faint": "#988889", "line": "#DED2D3", "line-2": "#CCBEBF", "focus": "#DB0011",
    "accent": "#DB0011", "link": "#990003", "gold": "#DB0011", "gold-deep": "#7C0002", "gold-ink": "#990003",
    "l1": "#4F0002", "l2": "#7C0002", "l3": "#AF1211", "l4": "#C13E4C", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#8A1112", "l2f": "#DB0011", "l3f": "#D8313A", "l4f": "#D18D99",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1F0C0F", "shadow": "rgba(49,7,14,.22)", "wash-a": "rgba(219,0,17,.14)",
    "wash-b": "rgba(209,141,153,.10)", "gb2": "#8A1112", "gb3": "#DB0011", "gb4": "#E2A8B5", "brand-grad": "linear-gradient(90deg,#7C0002,#DB0011 55%,#E2A8B5)",
    "gold-grad": "linear-gradient(135deg,#E2A8B5 0%,#DB0011 45%,#7C0002 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0E0A0B", "panel": "#1E1417", "panel-2": "#2D1F22", "ink": "#F7F2F4", "ink-2": "#E4DADD",
    "muted": "#C5B8B9", "faint": "#AA9E9F", "line": "#513E3F", "line-2": "#7C6466", "focus": "#DD8392",
    "accent": "#D47482", "link": "#E2A8B5", "gold": "#D47482", "gold-deep": "#DD8392", "gold-ink": "#E2A8B5",
    "l1": "#E2A8B5", "l2": "#DB8F9D", "l3": "#E49C9F", "l4": "#E9BAC4", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#8A1112", "l2f": "#DB0011", "l3f": "#D8313A", "l4f": "#D18D99",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090507", "wash-a": "rgba(219,0,17,.12)", "wash-b": "rgba(209,141,153,.06)",
    "gb2": "#8A1112", "gb3": "#DB0011", "gb4": "#E2A8B5", "gold-grad": "linear-gradient(135deg,#F2C8D2 0%,#D47482 45%,#DB0011 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
