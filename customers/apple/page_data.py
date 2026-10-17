"""Apple, as a platform: the data behind ``Apple_Platform.html``.

``python customers/build_page.py apple`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Apple_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from apple_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from apple_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Apple'
PAGE = 'Apple_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Apple Platform"
KICKER = f"Apple Inc., read through payments · as at {AS_OF}"
H1 = '<h1>Apple <span class="os">Platform</span></h1>'
SERVES = 'who Apple Pay serves'

PALETTE_NOTE = ("Palette: Apple's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Apple's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Apple's colours"

PIN = (37.33, -122.01, 'Cupertino')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'americas': 'Americas', 'europe': 'Europe', 'china': 'Greater China', 'japan': 'Japan', 'rap': 'Rest of Asia Pacific', 'grp': 'Corporate'}
DIV = {'pay': 'Apple Pay', 'wallet': 'Apple Wallet', 'card': 'Apple Card', 'cash': 'Apple Cash', 'ttp': 'Tap to Pay & NFC', 'grp': 'Apple Inc.'}
DEFAULT_DIV = 'pay'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F3F3F3", "panel-2": "#E7E7E8", "ink": "#0F0F0F", "ink-2": "#191919",
    "muted": "#2C2C2C", "faint": "#535354", "line": "#C9C9C9", "line-2": "#A5A5A5", "focus": "#1D1D1F",
    "accent": "#1D1D1F", "link": "#1B1B1D", "gold": "#1D1D1F", "gold-deep": "#1A1A1C", "gold-ink": "#1B1B1D",
    "l1": "#161617", "l2": "#1A1A1C", "l3": "#1C1C1D", "l4": "#39393B", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#1C1C1D", "l2f": "#1D1D1F", "l3f": "#404043", "l4f": "#828285",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0F0F0F", "shadow": "rgba(18,18,19,.22)", "wash-a": "rgba(29,29,31,.14)",
    "wash-b": "rgba(130,130,133,.10)", "gb2": "#1C1C1D", "gb3": "#1D1D1F", "gb4": "#A4A4A6", "brand-grad": "linear-gradient(90deg,#1A1A1C,#1D1D1F 55%,#A4A4A6)",
    "gold-grad": "linear-gradient(135deg,#A4A4A6 0%,#1D1D1F 45%,#1A1A1C 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0A0A", "panel": "#111111", "panel-2": "#161616", "ink": "#F4F4F4", "ink-2": "#D5D6D6",
    "muted": "#9B9B9C", "faint": "#727272", "line": "#242424", "line-2": "#353537", "focus": "#828387",
    "accent": "#78787C", "link": "#A4A4A6", "gold": "#78787C", "gold-deep": "#828387", "gold-ink": "#A4A4A6",
    "l1": "#A4A4A6", "l2": "#8A8B8E", "l3": "#9B9B9F", "l4": "#BBBBBD", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#1C1C1D", "l2f": "#1D1D1F", "l3f": "#404043", "l4f": "#828285",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060606", "wash-a": "rgba(29,29,31,.12)", "wash-b": "rgba(130,130,133,.06)",
    "gb2": "#1C1C1D", "gb3": "#1D1D1F", "gb4": "#A4A4A6", "gold-grad": "linear-gradient(135deg,#D2D2D4 0%,#707074 45%,#1D1D1F 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
