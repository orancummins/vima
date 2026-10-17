"""Bank of Cyprus, as a platform: the data behind ``Bank_of_Cyprus_Platform.html``.

``python customers/build_page.py bankofcyprus`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Bank_of_Cyprus_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bankofcyprus_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bankofcyprus_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Bank of Cyprus'
PAGE = 'Bank_of_Cyprus_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Bank of Cyprus Platform"
KICKER = f"Bank of Cyprus Holdings · as at {AS_OF}"
H1 = '<h1>Bank of Cyprus <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Bank of Cyprus's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Bank of Cyprus's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Bank of Cyprus's colours"

PIN = (35.17, 33.36, 'Nicosia')
PIN_FACING = 'Cyprus and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'consumer': 'Consumer Banking', 'business': 'SME & Corporate Banking', 'intl': 'International (IBU & corporate)', 'ins': 'Insurance', 'jccrev': 'JCC & other'}
DIV = {'boc': 'Bank of Cyprus Group', 'bank': 'Bank of Cyprus', 'jcc': 'JCC Payment Systems', 'eurolife': 'EuroLife', 'genikes': 'Genikes Insurance', 'jinius': 'Jinius'}
DEFAULT_DIV = 'boc'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F6", "panel-2": "#E4EEED", "ink": "#0A181A", "ink-2": "#1B2C2D",
    "muted": "#435154", "faint": "#667275", "line": "#C8D4D6", "line-2": "#A9B8BC", "focus": "#006880",
    "accent": "#006880", "link": "#004A62", "gold": "#006880", "gold-deep": "#003F54", "gold-ink": "#004A62",
    "l1": "#002D3B", "l2": "#003F54", "l3": "#0A4F69", "l4": "#2B7785", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0B4558", "l2f": "#006880", "l3f": "#1E839E", "l4f": "#69BBC3",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A181A", "shadow": "rgba(6,36,39,.22)", "wash-a": "rgba(0,104,128,.14)",
    "wash-b": "rgba(105,187,195,.10)", "gb2": "#0B4558", "gb3": "#006880", "gb4": "#8DD5D8", "brand-grad": "linear-gradient(90deg,#003F54,#006880 55%,#8DD5D8)",
    "gold-grad": "linear-gradient(135deg,#8DD5D8 0%,#006880 45%,#003F54 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090D0D", "panel": "#111819", "panel-2": "#172122", "ink": "#F2F7F7", "ink-2": "#D4E0DF",
    "muted": "#A2B0B3", "faint": "#808C8F", "line": "#283235", "line-2": "#3C484A", "focus": "#5CC7D2",
    "accent": "#49B8C6", "link": "#8DD5D8", "gold": "#49B8C6", "gold-deep": "#5CC7D2", "gold-ink": "#8DD5D8",
    "l1": "#8DD5D8", "l2": "#6CC6CF", "l3": "#7DC7DB", "l4": "#A8DFE3", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0B4558", "l2f": "#006880", "l3f": "#1E839E", "l4f": "#69BBC3",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,104,128,.12)", "wash-b": "rgba(105,187,195,.06)",
    "gb2": "#0B4558", "gb3": "#006880", "gb4": "#8DD5D8", "gold-grad": "linear-gradient(135deg,#BEEEF0 0%,#49B8C6 45%,#006880 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
