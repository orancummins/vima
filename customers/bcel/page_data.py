"""BCEL (Banque pour le Commerce Extérieur Lao Public), as a platform: the data behind ``BCEL_Platform.html``.

``python customers/build_page.py bcel`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``BCEL_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bcel_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bcel_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BCEL'
PAGE = 'BCEL_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BCEL Platform"
KICKER = f"Banque pour le Commerce Extérieur Lao Public · as at {AS_OF}"
H1 = '<h1>BCEL <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BCEL's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BCEL's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BCEL's colours"

PIN = (17.97, 102.61, 'Vientiane')
PIN_FACING = 'Laos and the Mekong'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail & digital', 'corporate': 'Corporate & SME lending', 'treasury': 'Treasury, FX & trade', 'group': 'Group & investments'}
DIV = {'bcel': 'BCEL', 'bcelone': 'BCEL One', 'onepay': 'OnePay', 'cards': 'BCEL Cards', 'bcome': 'BCOME', 'lapnet': 'LAPNet (20% owned)', 'jv': 'Joint ventures & BCEL-KT'}
DEFAULT_DIV = 'bcel'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F3", "panel-2": "#EFE8EA", "ink": "#1F0E11", "ink-2": "#432D32",
    "muted": "#796465", "faint": "#918284", "line": "#E0D7D7", "line-2": "#D1C7C8", "focus": "#E81820",
    "accent": "#E81820", "link": "#9F1310", "gold": "#E81820", "gold-deep": "#800F0D", "gold-ink": "#9F1310",
    "l1": "#4F0908", "l2": "#800F0D", "l3": "#BB2B25", "l4": "#BF6167", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#922220", "l2f": "#E81820", "l3f": "#D0585A", "l4f": "#D2A1A8",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#1F0E11", "shadow": "rgba(49,12,16,.22)", "wash-a": "rgba(232,24,32,.14)",
    "wash-b": "rgba(210,161,168,.10)", "gb2": "#922220", "gb3": "#E81820", "gb4": "#E1B8BF", "brand-grad": "linear-gradient(90deg,#800F0D,#E81820 55%,#E1B8BF)",
    "gold-grad": "linear-gradient(135deg,#E1B8BF 0%,#E81820 45%,#800F0D 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0C", "panel": "#1F1719", "panel-2": "#302325", "ink": "#F7F3F4", "ink-2": "#E5DDDF",
    "muted": "#CBC2C3", "faint": "#B4ABAC", "line": "#5B4949", "line-2": "#8D7778", "focus": "#DA9AA2",
    "accent": "#D28D95", "link": "#E1B8BF", "gold": "#D28D95", "gold-deep": "#DA9AA2", "gold-ink": "#E1B8BF",
    "l1": "#E1B8BF", "l2": "#D9A3AB", "l3": "#E2AEAE", "l4": "#E7C6CB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#922220", "l2f": "#E81820", "l3f": "#D0585A", "l4f": "#D2A1A8",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080607", "wash-a": "rgba(232,24,32,.12)", "wash-b": "rgba(210,161,168,.06)",
    "gb2": "#922220", "gb3": "#E81820", "gb4": "#E1B8BF", "gold-grad": "linear-gradient(135deg,#EFCFD6 0%,#D28D95 45%,#E81820 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
