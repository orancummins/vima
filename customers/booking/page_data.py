"""Booking Holdings, as a platform: the data behind ``Booking_Holdings_Platform.html``.

``python customers/build_page.py booking`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Booking_Holdings_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from booking_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from booking_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Booking'
PAGE = 'Booking_Holdings_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Booking Platform"
KICKER = f"Booking Holdings Inc. · as at {AS_OF}"
H1 = '<h1>Booking <span class="os">Platform</span></h1>'
SERVES = 'who Booking Holdings serves'

PALETTE_NOTE = ("Palette: Booking's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Booking's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Booking's colours"

PIN = (41.12, -73.41, 'Norwalk')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'merchant': 'Merchant revenues', 'agency': 'Agency revenues', 'ads': 'Advertising & other', 'grp': 'Corporate'}
DIV = {'booking': 'Booking.com', 'priceline': 'Priceline', 'agoda': 'Agoda', 'kayak': 'KAYAK', 'opentable': 'OpenTable', 'bhfs': 'Booking Holdings Financial Services', 'grp': 'Booking Holdings Inc.'}
DEFAULT_DIV = 'booking'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F4F6", "panel-2": "#E4EBEE", "ink": "#0A121A", "ink-2": "#1B252D",
    "muted": "#434A54", "faint": "#666C75", "line": "#C8CED6", "line-2": "#A9B1BC", "focus": "#003680",
    "accent": "#003680", "link": "#002362", "gold": "#003680", "gold-deep": "#001F54", "gold-ink": "#002362",
    "l1": "#00163B", "l2": "#001F54", "l3": "#0A2B69", "l4": "#2B5385", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0B2658", "l2f": "#003680", "l3f": "#1E519E", "l4f": "#6998C3",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A121A", "shadow": "rgba(6,23,39,.22)", "wash-a": "rgba(0,54,128,.14)",
    "wash-b": "rgba(105,152,195,.10)", "gb2": "#0B2658", "gb3": "#003680", "gb4": "#8DB7D8", "brand-grad": "linear-gradient(90deg,#001F54,#003680 55%,#8DB7D8)",
    "gold-grad": "linear-gradient(135deg,#8DB7D8 0%,#003680 45%,#001F54 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090B0D", "panel": "#111519", "panel-2": "#171D22", "ink": "#F2F5F7", "ink-2": "#D4DCE0",
    "muted": "#A2A9B3", "faint": "#80868F", "line": "#282E35", "line-2": "#3C424A", "focus": "#5C98D2",
    "accent": "#4987C6", "link": "#8DB7D8", "gold": "#4987C6", "gold-deep": "#5C98D2", "gold-ink": "#8DB7D8",
    "l1": "#8DB7D8", "l2": "#6CA0CF", "l3": "#7DA2DB", "l4": "#A8C8E3", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0B2658", "l2f": "#003680", "l3f": "#1E519E", "l4f": "#6998C3",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050708", "wash-a": "rgba(0,54,128,.12)", "wash-b": "rgba(105,152,195,.06)",
    "gb2": "#0B2658", "gb3": "#003680", "gb4": "#8DB7D8", "gold-grad": "linear-gradient(135deg,#BEDBF0 0%,#4987C6 45%,#003680 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
