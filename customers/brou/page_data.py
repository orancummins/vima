"""Banco República (BROU), as a platform: the data behind ``Banco_Republica_BROU_Platform.html``.

``python customers/build_page.py brou`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Banco_Republica_BROU_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from brou_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from brou_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BROU'
PAGE = 'Banco_Republica_BROU_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BROU Platform"
KICKER = f"Banco de la República Oriental del Uruguay · as at {AS_OF}"
H1 = '<h1>BROU <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BROU's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BROU's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BROU's colours"

PIN = (-34.907, -56.209, 'Montevideo')
PIN_FACING = 'Uruguay and Latin America'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'personas': 'Retail Banking (Personas)', 'corporativa': 'Corporate Division', 'finanzas': 'Finance & treasury', 'central': 'Central & group'}
DIV = {'brou': 'BROU', 'recompensa': 'BROU Recompensa', 'bam': 'BROU a Mano', 'sistarbanc': 'Sistarbanc', 'afisa': 'República AFISA', 'afap': 'República AFAP', 'micro': 'República Microfinanzas', 'ny': 'BROU New York'}
DEFAULT_DIV = 'brou'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E5EDEF", "ink": "#0B171C", "ink-2": "#213137",
    "muted": "#58656F", "faint": "#78828A", "line": "#CED5DA", "line-2": "#B5BEC5", "focus": "#0066B3",
    "accent": "#0066B3", "link": "#004281", "gold": "#0066B3", "gold-deep": "#00366A", "gold-ink": "#004281",
    "l1": "#002447", "l2": "#00366A", "l3": "#0E4E90", "l4": "#3579A7", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0E4274", "l2f": "#0066B3", "l3f": "#257BC2", "l4f": "#7DB1CB",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0B171C", "shadow": "rgba(7,31,45,.22)", "wash-a": "rgba(0,102,179,.14)",
    "wash-b": "rgba(125,177,203,.10)", "gb2": "#0E4274", "gb3": "#0066B3", "gb4": "#9CCADD", "brand-grad": "linear-gradient(90deg,#00366A,#0066B3 55%,#9CCADD)",
    "gold-grad": "linear-gradient(135deg,#9CCADD 0%,#0066B3 45%,#00366A 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0D0E", "panel": "#13191C", "panel-2": "#1C2428", "ink": "#F2F6F7", "ink-2": "#D7E0E2",
    "muted": "#AFB7BD", "faint": "#91989E", "line": "#343E45", "line-2": "#525E66", "focus": "#72B5D8",
    "accent": "#61A7CE", "link": "#9CCADD", "gold": "#61A7CE", "gold-deep": "#72B5D8", "gold-ink": "#9CCADD",
    "l1": "#9CCADD", "l2": "#80B9D6", "l3": "#8EBAE0", "l4": "#B2D6E6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0E4274", "l2f": "#0066B3", "l3f": "#257BC2", "l4f": "#7DB1CB",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,102,179,.12)", "wash-b": "rgba(125,177,203,.06)",
    "gb2": "#0E4274", "gb3": "#0066B3", "gb4": "#9CCADD", "gold-grad": "linear-gradient(135deg,#C4E5F1 0%,#61A7CE 45%,#0066B3 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
