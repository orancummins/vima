"""Banco Bradesco, as a platform: the data behind ``Bradesco_Platform.html``.

``python customers/build_page.py bradesco`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Bradesco_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bradesco_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bradesco_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Bradesco'
PAGE = 'Bradesco_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Bradesco Platform"
KICKER = f"Banco Bradesco · as at {AS_OF}"
H1 = '<h1>Bradesco <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Bradesco's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Bradesco's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Bradesco's colours"

PIN = (-23.53, -46.79, 'Osasco')
PIN_FACING = 'Latin America'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'ind': 'Banking: individuals', 'msme': 'Banking: micro, small & mid-sized firms', 'large': 'Banking: large corporates', 'ins': 'Insurance, pensions & capitalisation', 'group': 'Group & centre'}
DIV = {'bradesco': 'Bradesco', 'cartoes': 'Bradesco Cartões & Bradescard', 'digio': 'Digio', 'principal': 'Principal, Prime & Private', 'seguros': 'Bradesco Seguros & Bradsaúde', 'elopar': 'Elopar (Elo, Livelo, Alelo)', 'cielo': 'Cielo', 'bbi': 'Bradesco BBI & Corporate'}
DEFAULT_DIV = 'bradesco'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F4", "panel-2": "#EFE6EA", "ink": "#1D0C12", "ink-2": "#3C262E",
    "muted": "#7A6367", "faint": "#908184", "line": "#DDD2D4", "line-2": "#CABDC0", "focus": "#CC092F",
    "accent": "#CC092F", "link": "#8F0619", "gold": "#CC092F", "gold-deep": "#740514", "gold-ink": "#8F0619",
    "l1": "#4B030D", "l2": "#740514", "l3": "#A41828", "l4": "#B8425C", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#821524", "l2f": "#CC092F", "l3f": "#D0344F", "l4f": "#CD8EA0",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1D0C12", "shadow": "rgba(47,9,19,.22)", "wash-a": "rgba(204,9,47,.14)",
    "wash-b": "rgba(205,142,160,.10)", "gb2": "#821524", "gb3": "#CC092F", "gb4": "#DEA9BB", "brand-grad": "linear-gradient(90deg,#740514,#CC092F 55%,#DEA9BB)",
    "gold-grad": "linear-gradient(135deg,#DEA9BB 0%,#CC092F 45%,#740514 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0E0A0C", "panel": "#1D1518", "panel-2": "#2C1F23", "ink": "#F7F3F5", "ink-2": "#E3DADE",
    "muted": "#C3B7BA", "faint": "#A79D9F", "line": "#4E3D41", "line-2": "#776266", "focus": "#D8849C",
    "accent": "#CF758D", "link": "#DEA9BB", "gold": "#CF758D", "gold-deep": "#D8849C", "gold-ink": "#DEA9BB",
    "l1": "#DEA9BB", "l2": "#D790A5", "l3": "#E09DA8", "l4": "#E6BBC9", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#821524", "l2f": "#CC092F", "l3f": "#D0344F", "l4f": "#CD8EA0",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080507", "wash-a": "rgba(204,9,47,.12)", "wash-b": "rgba(205,142,160,.06)",
    "gb2": "#821524", "gb3": "#CC092F", "gb4": "#DEA9BB", "gold-grad": "linear-gradient(135deg,#F0C9D7 0%,#CF758D 45%,#CC092F 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
