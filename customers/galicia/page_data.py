"""Grupo Financiero Galicia, as a platform: the data behind ``Grupo_Financiero_Galicia_Platform.html``.

``python customers/build_page.py galicia`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Grupo_Financiero_Galicia_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from galicia_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from galicia_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Galicia'
PAGE = 'Grupo_Financiero_Galicia_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Galicia Platform"
KICKER = f"Grupo Financiero Galicia · as at {AS_OF}"
H1 = '<h1>Galicia <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Galicia's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Galicia's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Galicia's colours"

PIN = (-34.6, -58.38, 'Buenos Aires')
PIN_FACING = 'South America'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'bank': 'Galicia (bank)', 'naranja': 'Naranja X', 'insurance': 'Galicia Seguros', 'markets': 'Fondos Fima & Galicia Securities', 'group': 'Group & other'}
DIV = {'gfg': 'Grupo Financiero Galicia', 'galicia': 'Banco Galicia', 'galiciamas': 'Galicia Más (ex HSBC)', 'naranjax': 'Naranja X', 'nave': 'Nave', 'seguros': 'Galicia Seguros', 'fima': 'Fondos Fima', 'inviu': 'Inviu & Galicia Securities'}
DEFAULT_DIV = 'gfg'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F2", "panel-2": "#F0E8E7", "ink": "#20120C", "ink-2": "#45302A",
    "muted": "#75665D", "faint": "#8E837C", "line": "#E0DAD5", "line-2": "#D1CAC5", "focus": "#FA6400",
    "accent": "#FA6400", "link": "#A74D00", "gold": "#FA6400", "gold-deep": "#8A3F00", "gold-ink": "#A74D00",
    "l1": "#562700", "l2": "#8A3F00", "l3": "#C76A14", "l4": "#C87E53", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#9B5213", "l2f": "#FA6400", "l3f": "#DC8647", "l4f": "#D6AB99",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#20120C", "shadow": "rgba(52,22,8,.22)", "wash-a": "rgba(250,100,0,.14)",
    "wash-b": "rgba(214,171,153,.10)", "gb2": "#9B5213", "gb3": "#FA6400", "gb4": "#E5BFB1", "brand-grad": "linear-gradient(90deg,#8A3F00,#FA6400 55%,#E5BFB1)",
    "gold-grad": "linear-gradient(135deg,#E5BFB1 0%,#FA6400 45%,#8A3F00 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0A", "panel": "#201816", "panel-2": "#312621", "ink": "#F7F3F3", "ink-2": "#E6DDDC",
    "muted": "#CBC4C0", "faint": "#B3ACA8", "line": "#5B4E45", "line-2": "#8D7C72", "focus": "#FA6400",
    "accent": "#FA6400", "link": "#E5BFB1", "gold": "#FA6400", "gold-deep": "#E0A990", "gold-ink": "#E5BFB1",
    "l1": "#E5BFB1", "l2": "#DEAF9B", "l3": "#E7C2A6", "l4": "#EBCCC1", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#9B5213", "l2f": "#FA6400", "l3f": "#DC8647", "l4f": "#D6AB99",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090605", "wash-a": "rgba(250,100,0,.12)", "wash-b": "rgba(214,171,153,.06)",
    "gb2": "#9B5213", "gb3": "#FA6400", "gb4": "#E5BFB1", "gold-grad": "linear-gradient(135deg,#F3D5CB 0%,#D89F83 45%,#FA6400 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
