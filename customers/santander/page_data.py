"""Santander, as a platform: the data behind ``Santander_Platform.html``.

``python customers/build_page.py santander`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Santander_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from santander_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from santander_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Santander'
PAGE = 'Santander_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Santander Platform"
KICKER = f"Banco Santander · as at {AS_OF}"
H1 = '<h1>Santander <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Santander's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Santander's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Santander's colours"

PIN = (40.42, -3.7, 'Madrid')
PIN_FACING = 'Europe and the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail & Commercial Banking', 'dcb': 'Openbank', 'cib': 'Corporate & Investment Banking', 'wealth': 'Wealth Management & Insurance', 'pay': 'Payment Solutions', 'grp': 'Corporate Centre'}
DIV = {'san': 'Banco Santander', 'uk': 'Santander UK', 'es': 'Santander España', 'br': 'Santander Brasil', 'mx': 'Santander México', 'us': 'Santander US', 'openbank': 'Openbank', 'getnet': 'Getnet', 'grp': 'Santander Group'}
DEFAULT_DIV = 'san'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F3", "panel-2": "#F0E7E9", "ink": "#1F0C0E", "ink-2": "#42282C",
    "muted": "#7C6262", "faint": "#928181", "line": "#DFD4D4", "line-2": "#CFC2C2", "focus": "#EC0000",
    "accent": "#EC0000", "link": "#A30A00", "gold": "#EC0000", "gold-deep": "#830800", "gold-ink": "#A30A00",
    "l1": "#530500", "l2": "#830800", "l3": "#BC2013", "l4": "#C5494D", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#941A12", "l2f": "#EC0000", "l3f": "#DA413D", "l4f": "#D4949A",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1F0C0E", "shadow": "rgba(51,8,11,.22)", "wash-a": "rgba(236,0,0,.14)",
    "wash-b": "rgba(212,148,154,.10)", "gb2": "#941A12", "gb3": "#EC0000", "gb4": "#E3ADB5", "brand-grad": "linear-gradient(90deg,#830800,#EC0000 55%,#E3ADB5)",
    "gold-grad": "linear-gradient(135deg,#E3ADB5 0%,#EC0000 45%,#830800 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0A0B", "panel": "#1F1517", "panel-2": "#2F2022", "ink": "#F7F3F4", "ink-2": "#E5DBDD",
    "muted": "#C8BDBD", "faint": "#AFA4A4", "line": "#564242", "line-2": "#856B6B", "focus": "#DF8A92",
    "accent": "#D67C83", "link": "#E3ADB5", "gold": "#D67C83", "gold-deep": "#DF8A92", "gold-ink": "#E3ADB5",
    "l1": "#E3ADB5", "l2": "#DD969D", "l3": "#E5A4A1", "l4": "#EABEC4", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#941A12", "l2f": "#EC0000", "l3f": "#DA413D", "l4f": "#D4949A",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090506", "wash-a": "rgba(236,0,0,.12)", "wash-b": "rgba(212,148,154,.06)",
    "gb2": "#941A12", "gb3": "#EC0000", "gb4": "#E3ADB5", "gold-grad": "linear-gradient(135deg,#F3CAD0 0%,#D67C83 45%,#EC0000 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
