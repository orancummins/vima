"""Synchrony, as a platform: the data behind ``Synchrony_Platform.html``.

``python customers/build_page.py synchrony`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Synchrony_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from synchrony_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from synchrony_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Synchrony'
PAGE = 'Synchrony_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Synchrony Platform"
KICKER = f"Synchrony Financial · as at {AS_OF}"
H1 = '<h1>Synchrony <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Synchrony's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Synchrony's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Synchrony's colours"

PIN = (41.05, -73.54, 'Stamford')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'home': 'Home & Auto', 'digital': 'Digital', 'dv': 'Diversified & Value', 'health': 'Health & Wellness', 'life': 'Lifestyle', 'grp': 'Corporate'}
DIV = {'syf': 'Synchrony', 'carecredit': 'CareCredit', 'bank': 'Synchrony Bank', 'grp': 'Synchrony Financial'}
DEFAULT_DIV = 'syf'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F3F4F4", "panel-2": "#E7EBEB", "ink": "#0F1415", "ink-2": "#222728",
    "muted": "#4C5152", "faint": "#6D7273", "line": "#CED2D2", "line-2": "#B1B6B7", "focus": "#2C4B5B",
    "accent": "#2C4B5B", "link": "#213745", "gold": "#2C4B5B", "gold-deep": "#1C2F3B", "gold-ink": "#213745",
    "l1": "#142129", "l2": "#1C2F3B", "l3": "#2B3F4E", "l4": "#4B616B", "l5": "#29272F",
    "lu": "#747279", "l1f": "#253642", "l2f": "#2C4B5B", "l3f": "#4A6878", "l4f": "#89A0A7",
    "l5f": "#423F49", "luf": "#A4A2A9", "l1t": "#EFF6F8", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#121A1E", "l5t": "#FFFFFF", "slot": "#0F1415", "shadow": "rgba(17,26,29,.22)", "wash-a": "rgba(44,75,91,.14)",
    "wash-b": "rgba(137,160,167,.10)", "gb2": "#253642", "gb3": "#2C4B5B", "gb4": "#A7BCC1", "brand-grad": "linear-gradient(90deg,#253642,#FBC600 55%,#FFE27A)",
    "gold-grad": "linear-gradient(135deg,#A7BCC1 0%,#2C4B5B 45%,#1C2F3B 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0B0C", "panel": "#141616", "panel-2": "#1C1F1F", "ink": "#F4F5F5", "ink-2": "#D8DCDC",
    "muted": "#A9AEAF", "faint": "#878B8C", "line": "#2E3233", "line-2": "#444849", "focus": "#85A3AD",
    "accent": "#74949F", "link": "#A7BCC1", "gold": "#74949F", "gold-deep": "#85A3AD", "gold-ink": "#A7BCC1",
    "l1": "#A7BCC1", "l2": "#8FA9B0", "l3": "#9DB2BE", "l4": "#BCCCD0", "l5": "#D5D4D8",
    "lu": "#94929A", "l1f": "#253642", "l2f": "#2C4B5B", "l3f": "#4A6878", "l4f": "#89A0A7",
    "l5f": "#747279", "luf": "#747279", "slot": "#060707", "wash-a": "rgba(44,75,91,.12)", "wash-b": "rgba(137,160,167,.06)",
    "gb2": "#253642", "gb3": "#2C4B5B", "gb4": "#A7BCC1", "gold-grad": "linear-gradient(135deg,#CFDDE0 0%,#74949F 45%,#2C4B5B 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
