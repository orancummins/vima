"""Halyk Bank, as a platform: the data behind ``Halyk_Bank_Platform.html``.

``python customers/build_page.py halyk`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Halyk_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from halyk_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from halyk_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Halyk'
PAGE = 'Halyk_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Halyk Platform"
KICKER = f"Halyk Bank · as at {AS_OF}"
H1 = '<h1>Halyk <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Halyk's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Halyk's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Halyk's colours"

PIN = (43.24, 76.95, 'Almaty')
PIN_FACING = 'Central Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail (B2C)', 'corporate': 'Corporate banking', 'sme': 'SME banking', 'other': 'Insurance, international & other'}
DIV = {'group': 'Halyk Group', 'bank': 'Halyk Bank', 'tenge': 'Tenge Bank (Uzbekistan)', 'georgia': 'Halyk Bank Georgia', 'ins': 'Halyk Life & Halyk Insurance', 'finance': 'Halyk Finance & Halyk Invest', 'life': 'Halyk Market & lifestyle'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F4", "panel-2": "#E5EEE9", "ink": "#0B1A15", "ink-2": "#1E2F29",
    "muted": "#4B5D59", "faint": "#6D7C78", "line": "#CBD7D4", "line-2": "#AEBEBB", "focus": "#068C6E",
    "accent": "#068C6E", "link": "#046858", "gold": "#068C6E", "gold-deep": "#04584A", "gold-ink": "#046858",
    "l1": "#033D33", "l2": "#04584A", "l3": "#107264", "l4": "#328D76", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0F5F52", "l2f": "#068C6E", "l3f": "#26A58C", "l4f": "#74C2A9",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0B1A15", "shadow": "rgba(8,40,30,.22)", "wash-a": "rgba(6,140,110,.14)",
    "wash-b": "rgba(116,194,169,.10)", "gb2": "#0F5F52", "gb3": "#068C6E", "gb4": "#95D7BF", "brand-grad": "linear-gradient(90deg,#04584A,#068C6E 55%,#95D7BF)",
    "gold-grad": "linear-gradient(135deg,#95D7BF 0%,#068C6E 45%,#04584A 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090D0C", "panel": "#121916", "panel-2": "#192420", "ink": "#F2F7F5", "ink-2": "#D5E0DB",
    "muted": "#A7B6B2", "faint": "#869491", "line": "#2D3A37", "line-2": "#455350", "focus": "#068C6E",
    "accent": "#068C6E", "link": "#95D7BF", "gold": "#068C6E", "gold-deep": "#68D0AF", "gold-ink": "#95D7BF",
    "l1": "#95D7BF", "l2": "#77CEB2", "l3": "#86D9C9", "l4": "#AEE1CF", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0F5F52", "l2f": "#068C6E", "l3f": "#26A58C", "l4f": "#74C2A9",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050806", "wash-a": "rgba(6,140,110,.12)", "wash-b": "rgba(116,194,169,.06)",
    "gb2": "#0F5F52", "gb3": "#068C6E", "gb4": "#95D7BF", "gold-grad": "linear-gradient(135deg,#C2EEDE 0%,#56C4A3 45%,#068C6E 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
