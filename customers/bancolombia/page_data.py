"""Bancolombia, as a platform: the data behind ``Bancolombia_Platform.html``.

``python customers/build_page.py bancolombia`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Bancolombia_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bancolombia_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bancolombia_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Bancolombia'
PAGE = 'Bancolombia_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Bancolombia Platform"
KICKER = f"Bancolombia (Grupo Cibest) · as at {AS_OF}"
H1 = '<h1>Bancolombia <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Bancolombia's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Bancolombia's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Bancolombia's colours"

PIN = (6.25, -75.56, 'Medellín')
PIN_FACING = 'Colombia and Central America'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'colombia': 'Bancolombia (Colombia)', 'camerica': 'Central America', 'digital': 'Nequi & digital businesses', 'nonbank': 'Leasing, consumer finance & other'}
DIV = {'cibest': 'Grupo Cibest', 'bancolombia': 'Bancolombia', 'nequi': 'Nequi', 'wompi': 'Wompi', 'wenia': 'Wenia', 'agricola': 'Banco Agrícola', 'bam': 'BAM', 'sufi': 'Sufi & Renting Colombia'}
DEFAULT_DIV = 'bancolombia'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F5F2", "panel-2": "#F0EDE8", "ink": "#221D0D", "ink-2": "#4C432F",
    "muted": "#A39F8C", "faint": "#B1AFA5", "line": "#E3E1D9", "line-2": "#D8D6CE", "focus": "#AF9302",
    "accent": "#AF9302", "link": "#756A01", "gold": "#AF9302", "gold-deep": "#998A01", "gold-ink": "#756A01",
    "l1": "#5D5401", "l2": "#998A01", "l3": "#E3D319", "l4": "#CFBD6D", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#AFA017", "l2f": "#FDDA24", "l3f": "#E0CF64", "l4f": "#DCCFA9",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#0B0F14", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#221D0D", "shadow": "rgba(56,45,9,.22)", "wash-a": "rgba(253,218,36,.14)",
    "wash-b": "rgba(220,207,169,.10)", "gb2": "#AFA017", "gb3": "#FDDA24", "gb4": "#E8DBBD", "brand-grad": "linear-gradient(90deg,#998A01,#FDDA24 55%,#E8DBBD)",
    "gold-grad": "linear-gradient(135deg,#E8DBBD 0%,#FDDA24 45%,#998A01 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#100E0B", "panel": "#221F17", "panel-2": "#353125", "ink": "#F7F6F3", "ink-2": "#E7E4DE",
    "muted": "#D3D1C9", "faint": "#BEBDB5", "line": "#67634F", "line-2": "#9E9A87", "focus": "#FDDA24",
    "accent": "#FDDA24", "link": "#E8DBBD", "gold": "#FDDA24", "gold-deep": "#E4D4A1", "gold-ink": "#E8DBBD",
    "l1": "#E8DBBD", "l2": "#E3D4AB", "l3": "#EAE3B4", "l4": "#EDE2C9", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#AFA017", "l2f": "#FDDA24", "l3f": "#E0CF64", "l4f": "#DCCFA9",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090706", "wash-a": "rgba(253,218,36,.12)", "wash-b": "rgba(220,207,169,.06)",
    "gb2": "#AFA017", "gb3": "#FDDA24", "gb4": "#E8DBBD", "gold-grad": "linear-gradient(135deg,#F3E8D0 0%,#DDCD96 45%,#FDDA24 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
