"""Banco Itaú Paraguay, as a platform: the data behind ``Itau_Paraguay_Platform.html``.

``python customers/build_page.py itauparaguay`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Itau_Paraguay_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from itauparaguay_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from itauparaguay_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Itaú Paraguay'
PAGE = 'Itau_Paraguay_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Itaú Paraguay Platform"
KICKER = f"Banco Itaú Paraguay · as at {AS_OF}"
H1 = '<h1>Itaú Paraguay <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Itaú Paraguay's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Itaú Paraguay's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Itaú Paraguay's colours"

PIN = (-25.28, -57.63, 'Asunción')
PIN_FACING = 'Paraguay and the Southern Cone'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'personal': 'Personal Banking', 'business': 'Business Banking (Itaú Campo & IBBA)', 'markets': 'Institutional Treasury', 'central': 'Bank & central items'}
DIV = {'bipy': 'Banco Itaú Paraguay', 'pbank': 'Personal Bank', 'campo': 'Itaú Campo', 'ibba': 'Itaú BBA Paraguay', 'pont': 'Pont (Pik & Tienda Naranja)', 'sisters': 'Itaú Invest, Asset & Seguros', 'parent': 'Itaú Unibanco'}
DEFAULT_DIV = 'bipy'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F2F2", "panel-2": "#F0E8E7", "ink": "#21120D", "ink-2": "#46302A",
    "muted": "#75665D", "faint": "#8D827C", "line": "#E0DAD6", "line-2": "#D2CBC6", "focus": "#FF6200",
    "accent": "#FF6200", "link": "#AA4B00", "gold": "#FF6200", "gold-deep": "#8C3E00", "gold-ink": "#AA4B00",
    "l1": "#572600", "l2": "#8C3E00", "l3": "#CB6914", "l4": "#C97F56", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#9E5113", "l2f": "#FF6200", "l3f": "#DD864A", "l4f": "#D7AC9B",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#21120D", "shadow": "rgba(53,22,8,.22)", "wash-a": "rgba(255,98,0,.14)",
    "wash-b": "rgba(215,172,155,.10)", "gb2": "#9E5113", "gb3": "#FF6200", "gb4": "#E5BFB3", "brand-grad": "linear-gradient(90deg,#8C3E00,#FF6200 55%,#E5BFB3)",
    "gold-grad": "linear-gradient(135deg,#E5BFB3 0%,#FF6200 45%,#8C3E00 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0A", "panel": "#201816", "panel-2": "#312622", "ink": "#F7F3F3", "ink-2": "#E6DDDC",
    "muted": "#CCC5C1", "faint": "#B4AEAA", "line": "#5C4F46", "line-2": "#8F7E74", "focus": "#FF6200",
    "accent": "#FF6200", "link": "#E5BFB3", "gold": "#FF6200", "gold-deep": "#E1A992", "gold-ink": "#E5BFB3",
    "l1": "#E5BFB3", "l2": "#DFB09D", "l3": "#E7C2A8", "l4": "#EBCCC2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#9E5113", "l2f": "#FF6200", "l3f": "#DD864A", "l4f": "#D7AC9B",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090605", "wash-a": "rgba(255,98,0,.12)", "wash-b": "rgba(215,172,155,.06)",
    "gb2": "#9E5113", "gb3": "#FF6200", "gb4": "#E5BFB3", "gold-grad": "linear-gradient(135deg,#F3D5CC 0%,#D99F85 45%,#FF6200 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
