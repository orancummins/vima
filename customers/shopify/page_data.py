"""Shopify Inc., as a platform: the data behind ``Shopify_Platform.html``.

``python customers/build_page.py shopify`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Shopify_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from shopify_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from shopify_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Shopify'
PAGE = 'Shopify_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Shopify Platform"
KICKER = f"Shopify Inc., read through payments · as at {AS_OF}"
H1 = '<h1>Shopify <span class="os">Platform</span></h1>'
SERVES = 'who Shopify serves'

PALETTE_NOTE = ("Palette: Shopify's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Shopify's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Shopify's colours"

PIN = (45.42, -75.7, 'Ottawa')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'sub': 'Subscription solutions', 'mer': 'Merchant solutions', 'grp': 'Corporate'}
DIV = {'shopify': 'Shopify', 'payments': 'Shopify Payments', 'shoppay': 'Shop Pay', 'finance': 'Balance & Credit', 'capital': 'Shopify Capital', 'ai': 'AI & Catalog', 'grp': 'Shopify Inc.'}
DEFAULT_DIV = 'shopify'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F5F5F3", "panel-2": "#EDEEE9", "ink": "#191C12", "ink-2": "#3D4032",
    "muted": "#696D61", "faint": "#858980", "line": "#DCDED9", "line-2": "#C9CBC6", "focus": "#7CA038",
    "accent": "#7CA038", "link": "#537227", "gold": "#7CA038", "gold-deep": "#4E6A25", "gold-ink": "#537227",
    "l1": "#304217", "l2": "#4E6A25", "l3": "#79A045", "l4": "#9CAE77", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#617D38", "l2f": "#95BF47", "l3f": "#9FB974", "l4f": "#C2C9AD",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#191C12", "shadow": "rgba(36,42,20,.22)", "wash-a": "rgba(149,191,71,.14)",
    "wash-b": "rgba(194,201,173,.10)", "gb2": "#617D38", "gb3": "#95BF47", "gb4": "#D4D9C2", "brand-grad": "linear-gradient(90deg,#4E6A25,#95BF47 55%,#D4D9C2)",
    "gold-grad": "linear-gradient(135deg,#D4D9C2 0%,#95BF47 45%,#4E6A25 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0D0E0C", "panel": "#1D1E19", "panel-2": "#2C2E27", "ink": "#F6F6F4", "ink-2": "#E3E4DF",
    "muted": "#C9CBC6", "faint": "#B2B4AF", "line": "#55594E", "line-2": "#878B7F", "focus": "#95BF47",
    "accent": "#95BF47", "link": "#D4D9C2", "gold": "#95BF47", "gold-deep": "#C4CEA9", "gold-ink": "#D4D9C2",
    "l1": "#D4D9C2", "l2": "#C8CFB0", "l3": "#CDD8BA", "l4": "#DDE1CD", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#617D38", "l2f": "#95BF47", "l3f": "#9FB974", "l4f": "#C2C9AD",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080806", "wash-a": "rgba(149,191,71,.12)", "wash-b": "rgba(194,201,173,.06)",
    "gb2": "#617D38", "gb3": "#95BF47", "gb4": "#D4D9C2", "gold-grad": "linear-gradient(135deg,#E6E9D6 0%,#BAC59E 45%,#95BF47 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
