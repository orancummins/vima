"""U.S. Bank, as a platform: the data behind ``US_Bank_Platform.html``.

``python customers/build_page.py usbank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``US_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from usbank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from usbank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'U.S. Bank'
PAGE = 'US_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "U.S. Bank Platform"
KICKER = f"U.S. Bancorp · as at {AS_OF}"
H1 = '<h1>U.S. Bank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: U.S. Bank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in U.S. Bank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in U.S. Bank's colours"

PIN = (44.98, -93.27, 'Minneapolis')
PIN_FACING = 'the Americas and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'wccib': 'Wealth, Corporate, Commercial & Institutional Banking', 'cbb': 'Consumer & Business Banking', 'pay': 'Payment Services', 'tcs': 'Treasury & Corporate Support'}
DIV = {'usb': 'U.S. Bancorp', 'bank': 'U.S. Bank', 'cards': 'U.S. Bank Cards', 'elavon': 'Elavon', 'elan': 'Elan Financial Services', 'wealth': 'U.S. Bank Wealth Management', 'btig': 'BTIG'}
DEFAULT_DIV = 'usb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F3F6", "panel-2": "#E4E9EE", "ink": "#0A0F19", "ink-2": "#1A212B",
    "muted": "#404451", "faint": "#636772", "line": "#C8CBD6", "line-2": "#A8ACBB", "focus": "#001E79",
    "accent": "#001E79", "link": "#00125E", "gold": "#001E79", "gold-deep": "#000F51", "gold-ink": "#00125E",
    "l1": "#000B3A", "l2": "#000F51", "l3": "#0A1963", "l4": "#294181", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0A1854", "l2f": "#001E79", "l3f": "#1D3999", "l4f": "#6786C2",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A0F19", "shadow": "rgba(6,16,39,.22)", "wash-a": "rgba(0,30,121,.14)",
    "wash-b": "rgba(103,134,194,.10)", "gb2": "#0A1854", "gb3": "#001E79", "gb4": "#8BA9D8", "brand-grad": "linear-gradient(90deg,#000F51,#001E79 55%,#8BA9D8)",
    "gold-grad": "linear-gradient(135deg,#8BA9D8 0%,#001E79 45%,#000F51 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090A0D", "panel": "#101418", "panel-2": "#171B21", "ink": "#F2F5F7", "ink-2": "#D3D9DF",
    "muted": "#A1A5B1", "faint": "#7D818D", "line": "#272A33", "line-2": "#393C46", "focus": "#5982D1",
    "accent": "#5177C9", "link": "#8BA9D8", "gold": "#5177C9", "gold-deep": "#5982D1", "gold-ink": "#8BA9D8",
    "l1": "#8BA9D8", "l2": "#6A8DCE", "l3": "#7A8FDB", "l4": "#A6BDE2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0A1854", "l2f": "#001E79", "l3f": "#1D3999", "l4f": "#6786C2",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050708", "wash-a": "rgba(0,30,121,.12)", "wash-b": "rgba(103,134,194,.06)",
    "gb2": "#0A1854", "gb3": "#001E79", "gb4": "#8BA9D8", "gold-grad": "linear-gradient(135deg,#BED2F0 0%,#456EC5 45%,#001E79 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
