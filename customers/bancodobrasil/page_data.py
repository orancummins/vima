"""Banco do Brasil, as a platform: the data behind ``Banco_do_Brasil_Platform.html``.

``python customers/build_page.py bancodobrasil`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Banco_do_Brasil_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bancodobrasil_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bancodobrasil_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Banco do Brasil'
PAGE = 'Banco_do_Brasil_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Banco do Brasil Platform"
KICKER = f"Banco do Brasil · as at {AS_OF}"
H1 = '<h1>Banco do Brasil <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Banco do Brasil's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Banco do Brasil's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Banco do Brasil's colours"

PIN = (-15.79, -47.88, 'Brasília')
PIN_FACING = 'Latin America'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'ind': 'Individuals', 'comp': 'Companies', 'agro': 'Agribusiness', 'gov': 'Government', 'group': 'Group, insurance & stakes'}
DIV = {'bb': 'Banco do Brasil', 'ourocard': 'Ourocard', 'seguridade': 'BB Seguridade', 'asset': 'BB Asset & Consórcios', 'elo': 'BB Elo Cartões (Elo, Cielo, Livelo, Alelo)', 'intl': 'Banco Patagonia & BB Americas', 'bbts': 'BBTS'}
DEFAULT_DIV = 'bb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F4F7", "panel-2": "#E9ECF1", "ink": "#0E1324", "ink-2": "#333D54",
    "muted": "#9EA1B2", "faint": "#B3B5BD", "line": "#DDDEE6", "line-2": "#D6D7DE", "focus": "#465EFF",
    "accent": "#465EFF", "link": "#000FD9", "gold": "#465EFF", "gold-deep": "#000CAB", "gold-ink": "#000FD9",
    "l1": "#000866", "l2": "#000CAB", "l3": "#3039EA", "l4": "#8492D8", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#1823C5", "l2f": "#465EFF", "l3f": "#7C87E6", "l4f": "#B6C0E2",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0E1324", "shadow": "rgba(9,20,60,.22)", "wash-a": "rgba(70,94,255,.14)",
    "wash-b": "rgba(182,192,226,.10)", "gb2": "#1823C5", "gb3": "#465EFF", "gb4": "#C8D2EC", "brand-grad": "linear-gradient(90deg,#000CAB,#465EFF 55%,#C8D2EC)",
    "gold-grad": "linear-gradient(135deg,#C8D2EC 0%,#465EFF 45%,#000CAB 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0B0D10", "panel": "#191C25", "panel-2": "#282C3A", "ink": "#F3F5F8", "ink-2": "#E1E4E9",
    "muted": "#D2D3DA", "faint": "#C1C2C9", "line": "#575A72", "line-2": "#9A9DAE", "focus": "#B0BDE9",
    "accent": "#A7B3E3", "link": "#C8D2EC", "gold": "#A7B3E3", "gold-deep": "#B0BDE9", "gold-ink": "#C8D2EC",
    "l1": "#C8D2EC", "l2": "#B8C3E8", "l3": "#C0C4EE", "l4": "#D0D8F0", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#1823C5", "l2f": "#465EFF", "l3f": "#7C87E6", "l4f": "#B6C0E2",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060709", "wash-a": "rgba(70,94,255,.12)", "wash-b": "rgba(182,192,226,.06)",
    "gb2": "#1823C5", "gb3": "#465EFF", "gb4": "#C8D2EC", "gold-grad": "linear-gradient(135deg,#D3DDF5 0%,#A7B3E3 45%,#465EFF 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
