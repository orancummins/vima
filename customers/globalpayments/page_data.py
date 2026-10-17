"""Global Payments, as a platform: the data behind ``Global_Payments_Platform.html``.

``python customers/build_page.py globalpayments`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Global_Payments_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from globalpayments_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from globalpayments_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Global Payments'
PAGE = 'Global_Payments_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Global Payments Platform"
KICKER = f"Global Payments Inc. & Worldpay · as at {AS_OF}"
H1 = '<h1>Global Payments <span class="os">Platform</span></h1>'
SERVES = "who Global Payments serves"

PALETTE_NOTE = ("Palette: Global Payments's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Global Payments's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Global Payments's colours"

PIN = (33.75, -84.39, 'Atlanta')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'ent': 'Enterprise', 'plat': 'Platforms', 'smb': 'SMB', 'grp': 'Other & corporate'}
DIV = {'gpn': 'Global Payments', 'worldpay': 'Worldpay', 'heartland': 'Heartland', 'genius': 'Genius', 'grp': 'Global Payments Inc.'}
DEFAULT_DIV = 'gpn'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F3F6", "panel-2": "#E4E7EE", "ink": "#0A0D1A", "ink-2": "#1C202E",
    "muted": "#464A58", "faint": "#686D78", "line": "#C9CDD7", "line-2": "#ABB0BD", "focus": "#000987",
    "accent": "#000987", "link": "#000166", "gold": "#000987", "gold-deep": "#000157", "gold-ink": "#000166",
    "l1": "#00013D", "l2": "#000157", "l3": "#0C0B6E", "l4": "#2C358A", "l5": "#331F37",
    "lu": "#7F6B80", "l1f": "#0B0B5C", "l2f": "#000987", "l3f": "#1F25A3", "l4f": "#6C7BC4",
    "l5f": "#4E3751", "luf": "#AD9CAF", "l1t": "#E8ECFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#06092A", "l5t": "#FFFFFF", "slot": "#0A0D1A", "shadow": "rgba(6,11,40,.22)", "wash-a": "rgba(0,9,135,.14)",
    "wash-b": "rgba(108,123,196,.10)", "gb2": "#0B0B5C", "gb3": "#000987", "gb4": "#8F9ED9", "brand-grad": "linear-gradient(90deg,#0B0B5C,#3A3FD9 55%,#E5003B)",
    "gold-grad": "linear-gradient(135deg,#8F9ED9 0%,#000987 45%,#000157 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090A0D", "panel": "#111319", "panel-2": "#181A23", "ink": "#F2F4F7", "ink-2": "#D4D8E0",
    "muted": "#A4A9B4", "faint": "#828591", "line": "#2A2D37", "line-2": "#3F424E", "focus": "#5F71D3",
    "accent": "#4C5DC7", "link": "#8F9ED9", "gold": "#4C5DC7", "gold-deep": "#5F71D3", "gold-ink": "#8F9ED9",
    "l1": "#8F9ED9", "l2": "#6F7FD0", "l3": "#7F82DC", "l4": "#A9B5E3", "l5": "#DAD1DB",
    "lu": "#9F8BA1", "l1f": "#0B0B5C", "l2f": "#000987", "l3f": "#1F25A3", "l4f": "#6C7BC4",
    "l5f": "#7F6B80", "luf": "#7F6B80", "slot": "#050608", "wash-a": "rgba(0,9,135,.12)", "wash-b": "rgba(108,123,196,.06)",
    "gb2": "#0B0B5C", "gb3": "#000987", "gb4": "#8F9ED9", "gold-grad": "linear-gradient(135deg,#BFCAF0 0%,#4C5DC7 45%,#000987 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
