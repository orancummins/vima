"""Mercado Pago, as a platform: the data behind ``Mercado_Pago_Platform.html``.

``python customers/build_page.py mercadopago`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Mercado_Pago_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from mercadopago_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from mercadopago_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Mercado Pago'
PAGE = 'Mercado_Pago_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Mercado Pago Platform"
KICKER = f"Mercado Pago, Mercado Libre's fintech · as at {AS_OF}"
H1 = '<h1>Mercado Pago <span class="os">Platform</span></h1>'
SERVES = 'who Mercado Pago serves'

PALETTE_NOTE = ("Palette: Mercado Pago's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Mercado Pago's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Mercado Pago's colours"

PIN = (-34.6, -58.38, 'Buenos Aires')
PIN_FACING = 'Latin America'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'acq': 'Acquiring', 'svc': 'Fintech services', 'credit': 'Credit', 'grp': 'Mercado Libre group'}
DIV = {'grp': 'MercadoLibre, Inc.', 'mp': 'Mercado Pago (region)', 'br': 'Mercado Pago Brazil', 'mx': 'Mercado Pago Mexico', 'ar': 'Mercado Pago Argentina', 'cl': 'Mercado Pago Chile', 'credito': 'Mercado Crédito'}
DEFAULT_DIV = 'mp'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F7F7", "panel-2": "#E7F0F0", "ink": "#0D1D21", "ink-2": "#2A4346",
    "muted": "#5D6F75", "faint": "#7E8B90", "line": "#D6DEE0", "line-2": "#C3CDD0", "focus": "#009ED6",
    "accent": "#009ED6", "link": "#006FA5", "gold": "#009ED6", "gold-deep": "#005F8C", "gold-ink": "#006FA5",
    "l1": "#003B57", "l2": "#005F8C", "l3": "#148CCB", "l4": "#56AEC9", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#13719E", "l2f": "#00BCFF", "l3f": "#4AB3DD", "l4f": "#9BCDD7",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0D1D21", "shadow": "rgba(8,45,53,.22)", "wash-a": "rgba(0,188,255,.14)",
    "wash-b": "rgba(155,205,215,.10)", "gb2": "#13719E", "gb3": "#00BCFF", "gb4": "#B3DFE5", "brand-grad": "linear-gradient(90deg,#005F8C,#00BCFF 55%,#B3DFE5)",
    "gold-grad": "linear-gradient(135deg,#B3DFE5 0%,#00BCFF 45%,#005F8C 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0F0F", "panel": "#161F20", "panel-2": "#222F31", "ink": "#F3F7F7", "ink-2": "#DCE6E6",
    "muted": "#C1C9CC", "faint": "#AAB2B4", "line": "#46565C", "line-2": "#74888F", "focus": "#00BCFF",
    "accent": "#00BCFF", "link": "#B3DFE5", "gold": "#00BCFF", "gold-deep": "#92D3E1", "gold-ink": "#B3DFE5",
    "l1": "#B3DFE5", "l2": "#9DD4DF", "l3": "#A8D5E7", "l4": "#C2E6EB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#13719E", "l2f": "#00BCFF", "l3f": "#4AB3DD", "l4f": "#9BCDD7",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050908", "wash-a": "rgba(0,188,255,.12)", "wash-b": "rgba(155,205,215,.06)",
    "gb2": "#13719E", "gb3": "#00BCFF", "gb4": "#B3DFE5", "gold-grad": "linear-gradient(135deg,#CCEFF3 0%,#85C9D9 45%,#00BCFF 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
