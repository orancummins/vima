"""NatWest Group, as a platform: the data behind ``NatWest_Group_Platform.html``.

``python customers/build_page.py natwest`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``NatWest_Group_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from natwest_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from natwest_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'NatWest'
PAGE = 'NatWest_Group_Platform.html'
AS_OF = "17 October 2026"
TITLE = "NatWest Platform"
KICKER = f"NatWest Group · as at {AS_OF}"
H1 = '<h1>NatWest <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: NatWest's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in NatWest's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in NatWest's colours"

PIN = (51.51, -0.09, 'London')
PIN_FACING = 'the UK and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail Banking', 'pbwm': 'Private Banking & Wealth Management', 'ci': 'Commercial & Institutional', 'grp': 'Central items'}
DIV = {'nwg': 'NatWest Group', 'natwest': 'NatWest', 'rbs': 'Royal Bank of Scotland', 'ulster': 'Ulster Bank', 'coutts': 'Coutts', 'mettle': 'Mettle', 'tyl': 'Tyl', 'grp': 'NatWest Group'}
DEFAULT_DIV = 'nwg'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F3F1F6", "panel-2": "#E8E4EE", "ink": "#120A1A", "ink-2": "#241C2E",
    "muted": "#4E4658", "faint": "#6F6878", "line": "#CFC9D7", "line-2": "#B2ABBD", "focus": "#550384",
    "accent": "#550384", "link": "#460363", "gold": "#550384", "gold-deep": "#3B0255", "gold-ink": "#460363",
    "l1": "#29023B", "l2": "#3B0255", "l3": "#510D6C", "l4": "#642E88", "l5": "#36202A",
    "lu": "#7F6C73", "l1f": "#430D5A", "l2f": "#550384", "l3f": "#7522A0", "l4f": "#9B6EC2",
    "l5f": "#503842", "luf": "#AF9CA4", "l1t": "#F4E9FE", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#1C0729", "l5t": "#FFFFFF", "slot": "#120A1A", "shadow": "rgba(25,7,39,.22)", "wash-a": "rgba(85,3,132,.14)",
    "wash-b": "rgba(155,110,194,.10)", "gb2": "#430D5A", "gb3": "#550384", "gb4": "#B491D7", "brand-grad": "linear-gradient(90deg,#430D5A,#5A287D 55%,#C9A6E8)",
    "gold-grad": "linear-gradient(135deg,#B491D7 0%,#550384 45%,#3B0255 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0B090D", "panel": "#151119", "panel-2": "#1E1823", "ink": "#F4F2F7", "ink-2": "#D9D4E0",
    "muted": "#ABA4B4", "faint": "#8A8291", "line": "#312A37", "line-2": "#463F4E", "focus": "#9E62D0",
    "accent": "#914FC4", "link": "#B491D7", "gold": "#914FC4", "gold-deep": "#9E62D0", "gold-ink": "#B491D7",
    "l1": "#B491D7", "l2": "#A371CE", "l3": "#BC81DA", "l4": "#C6AAE2", "l5": "#DBD1D5",
    "lu": "#A08C94", "l1f": "#430D5A", "l2f": "#550384", "l3f": "#7522A0", "l4f": "#9B6EC2",
    "l5f": "#7F6C73", "luf": "#7F6C73", "slot": "#060508", "wash-a": "rgba(85,3,132,.12)", "wash-b": "rgba(155,110,194,.06)",
    "gb2": "#430D5A", "gb3": "#550384", "gb4": "#B491D7", "gold-grad": "linear-gradient(135deg,#D6C0EF 0%,#914FC4 45%,#550384 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
