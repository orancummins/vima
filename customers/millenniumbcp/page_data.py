"""Millennium BCP, as a platform: the data behind ``Millennium_BCP_Platform.html``.

``python customers/build_page.py millenniumbcp`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Millennium_BCP_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from millenniumbcp_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from millenniumbcp_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Millennium bcp'
PAGE = 'Millennium_BCP_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Millennium bcp Platform"
KICKER = f"Millennium bcp · Banco Comercial Português · as at {AS_OF}"
H1 = '<h1>Millennium bcp <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Millennium bcp's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Millennium bcp's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Millennium bcp's colours"

PIN = (38.74, -9.14, 'Lisbon')
PIN_FACING = 'Portugal, Poland and Mozambique'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail Banking (Portugal)', 'companies': 'Companies, Corporate & Investment Banking', 'private': 'Private Banking', 'intl': 'International activity', 'other': 'Other & central'}
DIV = {'group': 'Millennium bcp group', 'bcp': 'Millennium bcp', 'activo': 'ActivoBank', 'prestige': 'Prestige & Private Banking', 'empresas': 'Millennium Empresas', 'poland': 'Bank Millennium (Poland)', 'bim': 'Millennium bim (Mozambique)', 'ageas': 'Millenniumbcp Ageas'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F1F5", "panel-2": "#EFE6EC", "ink": "#1E0C16", "ink-2": "#3D2533",
    "muted": "#7F6570", "faint": "#94848B", "line": "#DDD1D6", "line-2": "#CABCC2", "focus": "#D1005D",
    "accent": "#D1005D", "link": "#930039", "gold": "#D1005D", "gold-deep": "#78002E", "gold-ink": "#930039",
    "l1": "#4D001E", "l2": "#78002E", "l3": "#A71148", "l4": "#BB3C78", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#85103D", "l2f": "#D1005D", "l3f": "#D62A73", "l4f": "#D089AF",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1E0C16", "shadow": "rgba(48,7,29,.22)", "wash-a": "rgba(209,0,93,.14)",
    "wash-b": "rgba(208,137,175,.10)", "gb2": "#85103D", "gb3": "#D1005D", "gb4": "#E0A5C8", "brand-grad": "linear-gradient(90deg,#78002E,#D1005D 55%,#E0A5C8)",
    "gold-grad": "linear-gradient(135deg,#E0A5C8 0%,#D1005D 45%,#78002E 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0E0A0D", "panel": "#1E141A", "panel-2": "#2C1E26", "ink": "#F7F2F6", "ink-2": "#E4D9E0",
    "muted": "#C3B6BC", "faint": "#A79BA0", "line": "#4E3C44", "line-2": "#76606A", "focus": "#DC7FB0",
    "accent": "#D26FA2", "link": "#E0A5C8", "gold": "#D26FA2", "gold-deep": "#DC7FB0", "gold-ink": "#E0A5C8",
    "l1": "#E0A5C8", "l2": "#D98BB6", "l3": "#E398B7", "l4": "#E8B8D4", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#85103D", "l2f": "#D1005D", "l3f": "#D62A73", "l4f": "#D089AF",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080508", "wash-a": "rgba(209,0,93,.12)", "wash-b": "rgba(208,137,175,.06)",
    "gb2": "#85103D", "gb3": "#D1005D", "gb4": "#E0A5C8", "gold-grad": "linear-gradient(135deg,#F2C7E1 0%,#D26FA2 45%,#D1005D 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
