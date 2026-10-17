"""BRAC Bank PLC, as a platform: the data behind ``BRAC_Bank_Platform.html``.

``python customers/build_page.py brac`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``BRAC_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from brac_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from brac_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BRAC Bank'
PAGE = 'BRAC_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BRAC Bank Platform"
KICKER = f"BRAC Bank PLC · as at {AS_OF}"
H1 = '<h1>BRAC Bank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BRAC Bank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BRAC Bank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BRAC Bank's colours"

PIN = (23.78, 90.4, 'Dhaka')
PIN_FACING = 'Bangladesh and South Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'sme': 'SME Banking', 'retail': 'Retail Banking', 'wholesale': 'Wholesale Banking', 'group': 'Subsidiaries & central'}
DIV = {'brac': 'BRAC Bank', 'tara': 'TARA', 'astha': 'Astha', 'bkash': 'bKash', 'saajan': 'BRAC Saajan', 'epl': 'BRAC EPL'}
DEFAULT_DIV = 'brac'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F6", "panel-2": "#E5EDEF", "ink": "#0B171D", "ink-2": "#223237",
    "muted": "#596770", "faint": "#79838B", "line": "#CED5DB", "line-2": "#B5BFC5", "focus": "#006CB5",
    "accent": "#006CB5", "link": "#004682", "gold": "#006CB5", "gold-deep": "#003A6B", "gold-ink": "#004682",
    "l1": "#002647", "l2": "#003A6B", "l3": "#0F5292", "l4": "#367DA9", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0E4575", "l2f": "#006CB5", "l3f": "#2580C4", "l4f": "#7EB4CB",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0B171D", "shadow": "rgba(7,33,45,.22)", "wash-a": "rgba(0,108,181,.14)",
    "wash-b": "rgba(126,180,203,.10)", "gb2": "#0E4575", "gb3": "#006CB5", "gb4": "#9DCDDE", "brand-grad": "linear-gradient(90deg,#003A6B,#006CB5 55%,#9DCDDE)",
    "gold-grad": "linear-gradient(135deg,#9DCDDE 0%,#006CB5 45%,#003A6B 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0D0E", "panel": "#131A1C", "panel-2": "#1C2529", "ink": "#F2F6F7", "ink-2": "#D7E0E2",
    "muted": "#AFB8BD", "faint": "#91999E", "line": "#353F45", "line-2": "#535F67", "focus": "#73B8D8",
    "accent": "#62AACE", "link": "#9DCDDE", "gold": "#62AACE", "gold-deep": "#73B8D8", "gold-ink": "#9DCDDE",
    "l1": "#9DCDDE", "l2": "#81BCD6", "l3": "#8FBDE0", "l4": "#B2D8E6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0E4575", "l2f": "#006CB5", "l3f": "#2580C4", "l4f": "#7EB4CB",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,108,181,.12)", "wash-b": "rgba(126,180,203,.06)",
    "gb2": "#0E4575", "gb3": "#006CB5", "gb4": "#9DCDDE", "gold-grad": "linear-gradient(135deg,#C4E6F1 0%,#62AACE 45%,#006CB5 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
