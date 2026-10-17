"""Grupo Financiero Banorte, as a platform: the data behind ``Banorte_Platform.html``.

``python customers/build_page.py banorte`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Banorte_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from banorte_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from banorte_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Banorte'
PAGE = 'Banorte_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Banorte Platform"
KICKER = f"Grupo Financiero Banorte · as at {AS_OF}"
H1 = '<h1>Banorte <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Banorte's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Banorte's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Banorte's colours"

PIN = (25.65, -100.36, 'Monterrey')
PIN_FACING = 'Mexico'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'banking': 'Banking', 'bap': 'Insurance, Pensions & Afore (BAP)', 'broker': 'Brokerage & Funds', 'other': 'Leasing, Factoring & Warehousing', 'group': 'Group & holding'}
DIV = {'gfn': 'Grupo Financiero Banorte', 'bank': 'Banco Mercantil del Norte', 'rappi': 'RappiCard (ex-Tarjetas del Futuro)', 'seguros': 'Seguros & Pensiones Banorte', 'afore': 'Afore XXI Banorte', 'casa': 'Casa de Bolsa & Fondos Banorte', 'uniteller': 'UniTeller', 'bineo': 'Bineo (being sold)'}
DEFAULT_DIV = 'gfn'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F4", "panel-2": "#EFE8EA", "ink": "#1F0E11", "ink-2": "#452E34",
    "muted": "#7B6466", "faint": "#8F8181", "line": "#E0D8D8", "line-2": "#D3C9CA", "focus": "#EC1C2D",
    "accent": "#EC1C2D", "link": "#A60E11", "gold": "#EC1C2D", "gold-deep": "#850B0E", "gold-ink": "#A60E11",
    "l1": "#520709", "l2": "#850B0E", "l3": "#C32424", "l4": "#C2646F", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#981F21", "l2f": "#EC1C2D", "l3f": "#D35C63", "l4f": "#D4A3AC",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#1F0E11", "shadow": "rgba(50,12,18,.22)", "wash-a": "rgba(236,28,45,.14)",
    "wash-b": "rgba(212,163,172,.10)", "gb2": "#981F21", "gb3": "#EC1C2D", "gb4": "#E2B9C2", "brand-grad": "linear-gradient(90deg,#850B0E,#EC1C2D 55%,#E2B9C2)",
    "gold-grad": "linear-gradient(135deg,#E2B9C2 0%,#EC1C2D 45%,#850B0E 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0C", "panel": "#201719", "panel-2": "#312427", "ink": "#F7F3F4", "ink-2": "#E5DDE0",
    "muted": "#CDC4C5", "faint": "#B6AEAE", "line": "#5D4A4C", "line-2": "#917B7D", "focus": "#DC9CA7",
    "accent": "#D4909A", "link": "#E2B9C2", "gold": "#D4909A", "gold-deep": "#DC9CA7", "gold-ink": "#E2B9C2",
    "l1": "#E2B9C2", "l2": "#DBA5AF", "l3": "#E3B0B2", "l4": "#E9C7CE", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#981F21", "l2f": "#EC1C2D", "l3f": "#D35C63", "l4f": "#D4A3AC",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090607", "wash-a": "rgba(236,28,45,.12)", "wash-b": "rgba(212,163,172,.06)",
    "gb2": "#981F21", "gb3": "#EC1C2D", "gb4": "#E2B9C2", "gold-grad": "linear-gradient(135deg,#F0D0D7 0%,#D4909A 45%,#EC1C2D 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
