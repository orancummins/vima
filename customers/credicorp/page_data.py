"""Credicorp (BCP), as a platform: the data behind ``Credicorp_BCP_Platform.html``.

``python customers/build_page.py credicorp`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Credicorp_BCP_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from credicorp_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from credicorp_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Credicorp'
PAGE = 'Credicorp_BCP_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Credicorp Platform"
KICKER = f"Credicorp (BCP, Yape, Mibanco) · as at {AS_OF}"
H1 = '<h1>Credicorp <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Credicorp's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Credicorp's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Credicorp's colours"

PIN = (-12.08, -76.95, 'Lima')
PIN_FACING = 'Peru and the Andes'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'universal': 'Universal Banking', 'micro': 'Microfinance', 'insurance': 'Insurance & Pensions', 'ima': 'Investment Management & Advisory'}
DIV = {'credicorp': 'Credicorp', 'bcp': 'BCP', 'yape': 'Yape', 'mibanco': 'Mibanco', 'bcpbo': 'BCP Bolivia', 'tenpo': 'Tenpo', 'culqi': 'Culqi', 'pacifico': 'Pacífico & Prima'}
DEFAULT_DIV = 'credicorp'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E4ECEE", "ink": "#0A141A", "ink-2": "#1D292F",
    "muted": "#48515B", "faint": "#6A727A", "line": "#CAD0D7", "line-2": "#ACB5BE", "focus": "#00458C",
    "accent": "#00458C", "link": "#002E69", "gold": "#00458C", "gold-deep": "#002759", "gold-ink": "#002E69",
    "l1": "#001B3E", "l2": "#002759", "l3": "#0B3672", "l4": "#2D5F8D", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0B2F5F", "l2f": "#00458C", "l3f": "#205FA7", "l4f": "#6EA1C5",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A141A", "shadow": "rgba(6,26,41,.22)", "wash-a": "rgba(0,69,140,.14)",
    "wash-b": "rgba(110,161,197,.10)", "gb2": "#0B2F5F", "gb3": "#00458C", "gb4": "#90BFDA", "brand-grad": "linear-gradient(90deg,#002759,#00458C 55%,#90BFDA)",
    "gold-grad": "linear-gradient(135deg,#90BFDA 0%,#00458C 45%,#002759 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090C0D", "panel": "#111719", "panel-2": "#181F24", "ink": "#F2F6F7", "ink-2": "#D4DDE0",
    "muted": "#A5ADB5", "faint": "#848B92", "line": "#2B3239", "line-2": "#414951", "focus": "#61A4D4",
    "accent": "#4E93C8", "link": "#90BFDA", "gold": "#4E93C8", "gold-deep": "#61A4D4", "gold-ink": "#90BFDA",
    "l1": "#90BFDA", "l2": "#71AAD1", "l3": "#81ABDC", "l4": "#AACEE3", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0B2F5F", "l2f": "#00458C", "l3f": "#205FA7", "l4f": "#6EA1C5",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,69,140,.12)", "wash-b": "rgba(110,161,197,.06)",
    "gb2": "#0B2F5F", "gb3": "#00458C", "gb4": "#90BFDA", "gold-grad": "linear-gradient(135deg,#C0DFF0 0%,#4E93C8 45%,#00458C 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
