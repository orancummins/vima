"""Barclays, as a platform: the data behind ``Barclays_Platform.html``.

``python customers/build_page.py barclays`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Barclays_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from barclays_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from barclays_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Barclays'
PAGE = 'Barclays_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Barclays Platform"
KICKER = f"Barclays PLC · as at {AS_OF}"
H1 = '<h1>Barclays <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Barclays's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Barclays's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Barclays's colours"

PIN = (51.51, -0.02, 'London')
PIN_FACING = 'Europe and the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'uk': 'Barclays UK', 'ukcb': 'Barclays UK Corporate Bank', 'pbwm': 'Private Bank & Wealth Management', 'ib': 'Barclays Investment Bank', 'us': 'Barclays US Consumer Bank', 'grp': 'Head Office'}
DIV = {'barclays': 'Barclays', 'barclaycard': 'Barclaycard', 'uk': 'Barclays UK', 'us': 'Barclays US', 'ib': 'Barclays Investment Bank', 'pay': 'Barclays Payments', 'grp': 'Barclays PLC'}
DEFAULT_DIV = 'barclays'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F6", "panel-2": "#E4EEEF", "ink": "#09181B", "ink-2": "#1B2D2F",
    "muted": "#455759", "faint": "#677879", "line": "#C8D7D8", "line-2": "#AABDBE", "focus": "#006187",
    "accent": "#006187", "link": "#004366", "gold": "#006187", "gold-deep": "#003957", "gold-ink": "#004366",
    "l1": "#00283D", "l2": "#003957", "l3": "#064B73", "l4": "#27748F", "l5": "#231E38",
    "lu": "#706A81", "l1f": "#074160", "l2f": "#006187", "l3f": "#187DAA", "l4f": "#68B7C8",
    "l5f": "#3C3652", "luf": "#A09BB0", "l1t": "#E8FBFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#04222C", "l5t": "#FFFFFF", "slot": "#09181B", "shadow": "rgba(4,34,42,.22)", "wash-a": "rgba(0,97,135,.14)",
    "wash-b": "rgba(104,183,200,.10)", "gb2": "#074160", "gb3": "#006187", "gb4": "#8BD1DD", "brand-grad": "linear-gradient(90deg,#074160,#00AEEF 55%,#7FD8F7)",
    "gold-grad": "linear-gradient(135deg,#8BD1DD 0%,#006187 45%,#003957 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090D0D", "panel": "#111819", "panel-2": "#172224", "ink": "#F2F7F7", "ink-2": "#D3E0E1",
    "muted": "#A3B4B5", "faint": "#818F92", "line": "#293538", "line-2": "#3E4C4F", "focus": "#59C0D9",
    "accent": "#46B1CD", "link": "#8BD1DD", "gold": "#46B1CD", "gold-deep": "#59C0D9", "gold-ink": "#8BD1DD",
    "l1": "#8BD1DD", "l2": "#6AC1D5", "l3": "#7AC0E1", "l4": "#A6DCE6", "l5": "#D3D0DB",
    "lu": "#908AA2", "l1f": "#074160", "l2f": "#006187", "l3f": "#187DAA", "l4f": "#68B7C8",
    "l5f": "#706A81", "luf": "#706A81", "slot": "#050808", "wash-a": "rgba(0,97,135,.12)", "wash-b": "rgba(104,183,200,.06)",
    "gb2": "#074160", "gb3": "#006187", "gb4": "#8BD1DD", "gold-grad": "linear-gradient(135deg,#BDECF2 0%,#46B1CD 45%,#006187 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
