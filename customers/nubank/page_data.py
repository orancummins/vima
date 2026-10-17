"""Nu Holdings, as a platform: the data behind ``Nubank_Platform.html``.

``python customers/build_page.py nubank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Nubank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from nubank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from nubank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Nubank'
PAGE = 'Nubank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Nubank Platform"
KICKER = f"Nu Holdings · as at {AS_OF}"
H1 = '<h1>Nubank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Nubank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Nubank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Nubank's colours"

PIN = (-23.56, -46.69, 'São Paulo')
PIN_FACING = 'Latin America'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'credit': 'Credit', 'fees': 'Fees & services', 'float': 'Deposits & float', 'grp': 'Group'}
DIV = {'nu': 'Nu Holdings', 'br': 'Nubank Brazil', 'mx': 'Nu México', 'co': 'Nu Colombia', 'us': 'Nu US', 'empresas': 'Nu Empresas', 'invest': 'Nu Investimentos'}
DEFAULT_DIV = 'nu'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F3F2F6", "panel-2": "#E9E7EF", "ink": "#150D1E", "ink-2": "#31273D",
    "muted": "#71637B", "faint": "#8A8190", "line": "#D9D2DD", "line-2": "#C6BECB", "focus": "#820AD1",
    "accent": "#820AD1", "link": "#630792", "gold": "#820AD1", "gold-deep": "#500676", "gold-ink": "#630792",
    "l1": "#33044C", "l2": "#500676", "l3": "#7B19A8", "l4": "#8944BB", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#601685", "l2f": "#820AD1", "l3f": "#9739D0", "l4f": "#AF90CE",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#150D1E", "shadow": "rgba(29,9,47,.22)", "wash-a": "rgba(130,10,209,.14)",
    "wash-b": "rgba(175,144,206,.10)", "gb2": "#601685", "gb3": "#820AD1", "gb4": "#C3ABDF", "brand-grad": "linear-gradient(90deg,#500676,#820AD1 55%,#C3ABDF)",
    "gold-grad": "linear-gradient(135deg,#C3ABDF 0%,#820AD1 45%,#500676 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0C0A0E", "panel": "#19151E", "panel-2": "#26202C", "ink": "#F4F3F7", "ink-2": "#DDDAE4",
    "muted": "#C0B9C4", "faint": "#A59FA9", "line": "#493F50", "line-2": "#72657B", "focus": "#B187D9",
    "accent": "#A678CF", "link": "#C3ABDF", "gold": "#A678CF", "gold-deep": "#B187D9", "gold-ink": "#C3ABDF",
    "l1": "#C3ABDF", "l2": "#B593D7", "l3": "#C99FE1", "l4": "#D0BCE6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#601685", "l2f": "#820AD1", "l3f": "#9739D0", "l4f": "#AF90CE",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060508", "wash-a": "rgba(130,10,209,.12)", "wash-b": "rgba(175,144,206,.06)",
    "gb2": "#601685", "gb3": "#820AD1", "gb4": "#C3ABDF", "gold-grad": "linear-gradient(135deg,#DBCAF0 0%,#A678CF 45%,#820AD1 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
