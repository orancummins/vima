"""Banco de Reservas de la República Dominicana, as a platform: the data behind ``Banreservas_Platform.html``.

``python customers/build_page.py banreservas`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Banreservas_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from banreservas_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from banreservas_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Banreservas'
PAGE = 'Banreservas_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Banreservas Platform"
KICKER = f"Banco de Reservas de la República Dominicana · as at {AS_OF}"
H1 = '<h1>Banreservas <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Banreservas's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Banreservas's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Banreservas's colours"

PIN = (18.47, -69.93, 'Santo Domingo')
PIN_FACING = 'the Caribbean and Latin America'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'personal': 'Personal & SME banking', 'corporate': 'Corporate & investment banking', 'gov': 'Government business', 'tourism': 'Tourism business', 'central': 'Treasury, subsidiaries & central'}
DIV = {'br': 'Banreservas', 'mio': 'MIO Banreservas', 'seguros': 'Seguros Reservas', 'afp': 'AFP Reservas', 'invres': 'Inversiones & Reservas', 'fundacion': 'Fundación Reservas del País'}
DEFAULT_DIV = 'br'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E4EDEE", "ink": "#0A151A", "ink-2": "#1C2A2E",
    "muted": "#465159", "faint": "#687278", "line": "#C9D1D7", "line-2": "#ABB6BD", "focus": "#005088",
    "accent": "#005088", "link": "#003667", "gold": "#005088", "gold-deep": "#002E57", "gold-ink": "#003667",
    "l1": "#00213D", "l2": "#002E57", "l3": "#0B3E6F", "l4": "#2C668B", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0B365D", "l2f": "#005088", "l3f": "#1F6AA4", "l4f": "#6CA9C4",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A151A", "shadow": "rgba(6,29,40,.22)", "wash-a": "rgba(0,80,136,.14)",
    "wash-b": "rgba(108,169,196,.10)", "gb2": "#0B365D", "gb3": "#005088", "gb4": "#8FC5D9", "brand-grad": "linear-gradient(90deg,#002E57,#005088 55%,#8FC5D9)",
    "gold-grad": "linear-gradient(135deg,#8FC5D9 0%,#005088 45%,#002E57 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090C0D", "panel": "#111719", "panel-2": "#182023", "ink": "#F2F6F7", "ink-2": "#D4DEE0",
    "muted": "#A4AEB4", "faint": "#828B91", "line": "#2A3237", "line-2": "#3F484F", "focus": "#5FAED3",
    "accent": "#4C9EC7", "link": "#8FC5D9", "gold": "#4C9EC7", "gold-deep": "#5FAED3", "gold-ink": "#8FC5D9",
    "l1": "#8FC5D9", "l2": "#6FB2D0", "l3": "#7FB3DC", "l4": "#A9D3E3", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0B365D", "l2f": "#005088", "l3f": "#1F6AA4", "l4f": "#6CA9C4",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,80,136,.12)", "wash-b": "rgba(108,169,196,.06)",
    "gb2": "#0B365D", "gb3": "#005088", "gb4": "#8FC5D9", "gold-grad": "linear-gradient(135deg,#BFE4F0 0%,#4C9EC7 45%,#005088 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
