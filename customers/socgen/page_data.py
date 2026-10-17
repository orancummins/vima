"""Société Générale, as a platform: the data behind ``Societe_Generale_Platform.html``.

``python customers/build_page.py socgen`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Societe_Generale_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from socgen_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from socgen_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'SocGen'
PAGE = 'Societe_Generale_Platform.html'
AS_OF = "17 October 2026"
TITLE = "SocGen Platform"
KICKER = f"Société Générale · as at {AS_OF}"
H1 = '<h1>SocGen <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: SocGen's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in SocGen's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in SocGen's colours"

PIN = (48.89, 2.24, 'Paris')
PIN_FACING = 'Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'frpb': 'French Retail, Private Banking & Insurance', 'gbis': 'Global Banking & Investor Solutions', 'mibs': 'Mobility, International Retail Banking & Financial Services', 'corp': 'Corporate Centre'}
DIV = {'group': 'Société Générale', 'sg': 'SG network (France)', 'bourso': 'BoursoBank', 'kb': 'Komerční banka', 'brd': 'BRD', 'ayvens': 'Ayvens', 'cf': 'Consumer finance', 'cib': 'SG CIB & SG-Forge'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F4", "panel-2": "#EFE6EA", "ink": "#1F0C11", "ink-2": "#412730",
    "muted": "#796064", "faint": "#907F82", "line": "#DED3D5", "line-2": "#CEC0C3", "focus": "#E60028",
    "accent": "#E60028", "link": "#9F0012", "gold": "#E60028", "gold-deep": "#81000F", "gold-ink": "#9F0012",
    "l1": "#52000A", "l2": "#81000F", "l3": "#B71222", "l4": "#C4455F", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#901120", "l2f": "#E60028", "l3f": "#D93951", "l4f": "#D391A3",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1F0C11", "shadow": "rgba(50,8,18,.22)", "wash-a": "rgba(230,0,40,.14)",
    "wash-b": "rgba(211,145,163,.10)", "gb2": "#901120", "gb3": "#E60028", "gb4": "#E3ABBD", "brand-grad": "linear-gradient(90deg,#81000F,#E60028 55%,#E3ABBD)",
    "gold-grad": "linear-gradient(135deg,#E3ABBD 0%,#E60028 45%,#81000F 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0A0C", "panel": "#1F1518", "panel-2": "#2E2024", "ink": "#F7F3F5", "ink-2": "#E5DADF",
    "muted": "#C7BBBD", "faint": "#ADA2A4", "line": "#544044", "line-2": "#82696D", "focus": "#DE889E",
    "accent": "#D57990", "link": "#E3ABBD", "gold": "#D57990", "gold-deep": "#DE889E", "gold-ink": "#E3ABBD",
    "l1": "#E3ABBD", "l2": "#DC93A7", "l3": "#E59FA9", "l4": "#E9BCCA", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#901120", "l2f": "#E60028", "l3f": "#D93951", "l4f": "#D391A3",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090507", "wash-a": "rgba(230,0,40,.12)", "wash-b": "rgba(211,145,163,.06)",
    "gb2": "#901120", "gb3": "#E60028", "gb4": "#E3ABBD", "gold-grad": "linear-gradient(135deg,#F2C9D7 0%,#D57990 45%,#E60028 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
