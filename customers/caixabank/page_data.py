"""CaixaBank, as a platform: the data behind ``CaixaBank_Platform.html``.

``python customers/build_page.py caixabank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``CaixaBank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from caixabank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from caixabank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'CaixaBank'
PAGE = 'CaixaBank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "CaixaBank Platform"
KICKER = f"CaixaBank Group · as at {AS_OF}"
H1 = '<h1>CaixaBank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: CaixaBank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in CaixaBank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in CaixaBank's colours"

PIN = (39.47, -0.38, 'Valencia')
PIN_FACING = 'Spain and Portugal'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'bank': 'Banking and insurance', 'bpi': 'BPI', 'centre': 'Corporate centre'}
DIV = {'group': 'CaixaBank Group', 'caixabank': 'CaixaBank', 'bpi': 'Banco BPI', 'imagin': 'imagin', 'cpc': 'CaixaBank Payments & Consumer', 'comercia': 'Comercia Global Payments', 'vida': 'VidaCaixa'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F6F6", "panel-2": "#E6EFEF", "ink": "#0C1B1E", "ink-2": "#263B3E",
    "muted": "#5D6E74", "faint": "#7C888E", "line": "#D2DADD", "line-2": "#BDC7CB", "focus": "#009AD8",
    "accent": "#009AD8", "link": "#006397", "gold": "#009AD8", "gold-deep": "#00507B", "gold-ink": "#006397",
    "l1": "#00344F", "l2": "#00507B", "l3": "#1173AD", "l4": "#3D9EC0", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#105F89", "l2f": "#009AD8", "l3f": "#2FA3D7", "l4f": "#8CC4D1",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0C1B1E", "shadow": "rgba(7,40,49,.22)", "wash-a": "rgba(0,154,216,.14)",
    "wash-b": "rgba(140,196,209,.10)", "gb2": "#105F89", "gb3": "#009AD8", "gb4": "#A7D9E1", "brand-grad": "linear-gradient(90deg,#00507B,#009AD8 55%,#A7D9E1)",
    "gold-grad": "linear-gradient(135deg,#A7D9E1 0%,#009AD8 45%,#00507B 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0E0E", "panel": "#141D1E", "panel-2": "#1F2A2D", "ink": "#F2F7F7", "ink-2": "#D9E3E4",
    "muted": "#B8C1C4", "faint": "#9DA5A9", "line": "#3D4B50", "line-2": "#63737A", "focus": "#009AD8",
    "accent": "#009AD8", "link": "#A7D9E1", "gold": "#009AD8", "gold-deep": "#82CBDD", "gold-ink": "#A7D9E1",
    "l1": "#A7D9E1", "l2": "#8ECCDA", "l3": "#9BCCE4", "l4": "#BAE1E8", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#105F89", "l2f": "#009AD8", "l3f": "#2FA3D7", "l4f": "#8CC4D1",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,154,216,.12)", "wash-b": "rgba(140,196,209,.06)",
    "gb2": "#105F89", "gb3": "#009AD8", "gb4": "#A7D9E1", "gold-grad": "linear-gradient(135deg,#C8ECF2 0%,#73BED3 45%,#009AD8 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
