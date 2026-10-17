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
    "ground": "#FFFFFF", "panel": "#F2F6F6", "panel-2": "#E7F0F0", "ink": "#0C1C20", "ink-2": "#294043",
    "muted": "#5D6E74", "faint": "#7D8A8E", "line": "#D4DCDF", "line-2": "#C2CCCF", "focus": "#009FDB",
    "accent": "#009FDB", "link": "#006EA5", "gold": "#009FDB", "gold-deep": "#005985", "gold-ink": "#006EA5",
    "l1": "#003853", "l2": "#005985", "l3": "#1382BE", "l4": "#4BA8C6", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#126995", "l2f": "#00AEEF", "l3f": "#3FADDB", "l4f": "#95C9D4",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0C1C20", "shadow": "rgba(8,43,51,.22)", "wash-a": "rgba(0,174,239,.14)",
    "wash-b": "rgba(149,201,212,.10)", "gb2": "#126995", "gb3": "#00AEEF", "gb4": "#AEDCE4", "brand-grad": "linear-gradient(90deg,#005985,#00AEEF 55%,#AEDCE4)",
    "gold-grad": "linear-gradient(135deg,#AEDCE4 0%,#00AEEF 45%,#005985 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0E0F", "panel": "#151E1F", "panel-2": "#212D2F", "ink": "#F3F7F7", "ink-2": "#DBE5E5",
    "muted": "#BDC6C9", "faint": "#A5ADB0", "line": "#435257", "line-2": "#6D8087", "focus": "#00AEEF",
    "accent": "#00AEEF", "link": "#AEDCE4", "gold": "#00AEEF", "gold-deep": "#8BD0DF", "gold-ink": "#AEDCE4",
    "l1": "#AEDCE4", "l2": "#97D1DD", "l3": "#A2D1E6", "l4": "#BEE4EA", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#126995", "l2f": "#00AEEF", "l3f": "#3FADDB", "l4f": "#95C9D4",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050908", "wash-a": "rgba(0,174,239,.12)", "wash-b": "rgba(149,201,212,.06)",
    "gb2": "#126995", "gb3": "#00AEEF", "gb4": "#AEDCE4", "gold-grad": "linear-gradient(135deg,#CAEEF3 0%,#7EC5D7 45%,#00AEEF 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
