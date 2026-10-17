"""Eurobank, as a platform: the data behind ``Eurobank_Platform.html``.

``python customers/build_page.py eurobank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Eurobank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from eurobank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from eurobank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Eurobank'
PAGE = 'Eurobank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Eurobank Platform"
KICKER = f"Eurobank · as at {AS_OF}"
H1 = '<h1>Eurobank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Eurobank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Eurobank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Eurobank's colours"

PIN = (37.98, 23.73, 'Athens')
PIN_FACING = 'Greece, Cyprus and Bulgaria'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'greece': 'Greece', 'cyprus': 'Cyprus', 'bulgaria': 'Bulgaria', 'group': 'Group & Luxembourg'}
DIV = {'group': 'Eurobank Group', 'gr': 'Eurobank (Greece)', 'cy': 'Eurobank Cyprus', 'postbank': 'Postbank (Bulgaria)', 'lux': 'Eurobank Luxembourg', 'eurolife': 'Eurolife & insurance'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F4", "panel-2": "#F0E6EB", "ink": "#1F0C12", "ink-2": "#422831",
    "muted": "#7B6166", "faint": "#918084", "line": "#DFD4D6", "line-2": "#CEC1C4", "focus": "#EA002A",
    "accent": "#EA002A", "link": "#A20014", "gold": "#EA002A", "gold-deep": "#830010", "gold-ink": "#A20014",
    "l1": "#52000A", "l2": "#830010", "l3": "#BB1323", "l4": "#C54862", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#931221", "l2f": "#EA002A", "l3f": "#DA3C54", "l4f": "#D493A5",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1F0C12", "shadow": "rgba(51,8,19,.22)", "wash-a": "rgba(234,0,42,.14)",
    "wash-b": "rgba(212,147,165,.10)", "gb2": "#931221", "gb3": "#EA002A", "gb4": "#E3ADBE", "brand-grad": "linear-gradient(90deg,#830010,#EA002A 55%,#E3ADBE)",
    "gold-grad": "linear-gradient(135deg,#E3ADBE 0%,#EA002A 45%,#830010 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0A0C", "panel": "#1F1519", "panel-2": "#2F2025", "ink": "#F7F3F5", "ink-2": "#E5DBDF",
    "muted": "#C8BCBE", "faint": "#AEA3A5", "line": "#564145", "line-2": "#846B6F", "focus": "#DF89A0",
    "accent": "#D67B92", "link": "#E3ADBE", "gold": "#D67B92", "gold-deep": "#DF89A0", "gold-ink": "#E3ADBE",
    "l1": "#E3ADBE", "l2": "#DC95A9", "l3": "#E5A1AB", "l4": "#EABDCB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#931221", "l2f": "#EA002A", "l3f": "#DA3C54", "l4f": "#D493A5",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090507", "wash-a": "rgba(234,0,42,.12)", "wash-b": "rgba(212,147,165,.06)",
    "gb2": "#931221", "gb3": "#EA002A", "gb4": "#E3ADBE", "gold-grad": "linear-gradient(135deg,#F2C9D7 0%,#D67B92 45%,#EA002A 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
