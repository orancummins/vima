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
    "ground": "#FFFFFF", "panel": "#F2F3F7", "panel-2": "#E8EAF0", "ink": "#0D1023", "ink-2": "#2F354D",
    "muted": "#666680", "faint": "#828493", "line": "#DADAE3", "line-2": "#C8C9D5", "focus": "#262AFF",
    "accent": "#262AFF", "link": "#0800C6", "gold": "#262AFF", "gold-deep": "#06009C", "gold-ink": "#0800C6",
    "l1": "#03005F", "l2": "#06009C", "l3": "#2518E8", "l4": "#6F74D1", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#1C15B3", "l2f": "#262AFF", "l3f": "#6665E2", "l4f": "#AAB0DD",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0D1023", "shadow": "rgba(9,13,57,.22)", "wash-a": "rgba(38,42,255,.14)",
    "wash-b": "rgba(170,176,221,.10)", "gb2": "#1C15B3", "gb3": "#262AFF", "gb4": "#BEC5E9", "brand-grad": "linear-gradient(90deg,#06009C,#262AFF 55%,#BEC5E9)",
    "gold-grad": "linear-gradient(135deg,#BEC5E9 0%,#262AFF 45%,#06009C 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0B0C10", "panel": "#181A23", "panel-2": "#252736", "ink": "#F3F4F8", "ink-2": "#DFE1E8",
    "muted": "#CACBD4", "faint": "#B7B7BF", "line": "#4F5068", "line-2": "#8989A0", "focus": "#A2AAE6",
    "accent": "#979EDF", "link": "#BEC5E9", "gold": "#979EDF", "gold-deep": "#A2AAE6", "gold-ink": "#BEC5E9",
    "l1": "#BEC5E9", "l2": "#ACB2E4", "l3": "#B6B5EB", "l4": "#C9CFEE", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#1C15B3", "l2f": "#262AFF", "l3f": "#6665E2", "l4f": "#AAB0DD",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060709", "wash-a": "rgba(38,42,255,.12)", "wash-b": "rgba(170,176,221,.06)",
    "gb2": "#1C15B3", "gb3": "#262AFF", "gb4": "#BEC5E9", "gold-grad": "linear-gradient(135deg,#D0D6F4 0%,#979EDF 45%,#262AFF 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
