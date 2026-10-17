"""Banco Pichincha, as a platform: the data behind ``Banco_Pichincha_Platform.html``.

``python customers/build_page.py pichincha`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Banco_Pichincha_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from pichincha_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from pichincha_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Pichincha'
PAGE = 'Banco_Pichincha_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Pichincha Platform"
KICKER = f"Banco Pichincha · as at {AS_OF}"
H1 = '<h1>Pichincha <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Pichincha's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Pichincha's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Pichincha's colours"

PIN = (-0.18, -78.47, 'Quito')
PIN_FACING = 'Ecuador and the Andes'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'personas': 'Personal banking', 'empresas': 'Corporate & SME', 'micro': 'Microfinance', 'intl': 'International', 'group': 'Group & treasury'}
DIV = {'bp': 'Banco Pichincha', 'deuna': 'Deuna', 'vecino': 'Mi Vecino', 'miles': 'Pichincha Miles', 'subs': 'Ecuador subsidiaries', 'espana': 'Banco Pichincha España', 'colombia': 'Banco Pichincha Colombia'}
DEFAULT_DIV = 'bp'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F5F2", "panel-2": "#F0ECE7", "ink": "#211C0D", "ink-2": "#463E2A",
    "muted": "#95917A", "faint": "#A5A397", "line": "#E0DFD6", "line-2": "#D2D0C6", "focus": "#A89200",
    "accent": "#A89200", "link": "#726900", "gold": "#A89200", "gold-deep": "#8C8100", "gold-ink": "#726900",
    "l1": "#575000", "l2": "#8C8100", "l3": "#CBC114", "l4": "#C9B656", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#9E9413", "l2f": "#FFDD00", "l3f": "#DDCC4A", "l4f": "#D7C99B",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#0B0F14", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#211C0D", "shadow": "rgba(53,43,8,.22)", "wash-a": "rgba(255,221,0,.14)",
    "wash-b": "rgba(215,201,155,.10)", "gb2": "#9E9413", "gb3": "#FFDD00", "gb4": "#E5D7B3", "brand-grad": "linear-gradient(90deg,#8C8100,#FFDD00 55%,#E5D7B3)",
    "gold-grad": "linear-gradient(135deg,#E5D7B3 0%,#FFDD00 45%,#8C8100 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0E0A", "panel": "#201D16", "panel-2": "#312D22", "ink": "#F7F6F3", "ink-2": "#E6E2DC",
    "muted": "#CCCBC1", "faint": "#B4B3AA", "line": "#5C5946", "line-2": "#8F8B74", "focus": "#FFDD00",
    "accent": "#FFDD00", "link": "#E5D7B3", "gold": "#FFDD00", "gold-deep": "#E1D092", "gold-ink": "#E5D7B3",
    "l1": "#E5D7B3", "l2": "#DFD09D", "l3": "#E7E1A8", "l4": "#EBE0C2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#9E9413", "l2f": "#FFDD00", "l3f": "#DDCC4A", "l4f": "#D7C99B",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090705", "wash-a": "rgba(255,221,0,.12)", "wash-b": "rgba(215,201,155,.06)",
    "gb2": "#9E9413", "gb3": "#FFDD00", "gb4": "#E5D7B3", "gold-grad": "linear-gradient(135deg,#F3E8CC 0%,#D9C885 45%,#FFDD00 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
