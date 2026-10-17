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
    "ground": "#FFFFFF", "panel": "#F6F1F3", "panel-2": "#EEE4E7", "ink": "#1A0A0C", "ink-2": "#2E1C20",
    "muted": "#58464A", "faint": "#78686D", "line": "#D7C9CD", "line-2": "#BDABB0", "focus": "#870009",
    "accent": "#870009", "link": "#660001", "gold": "#870009", "gold-deep": "#570001", "gold-ink": "#660001",
    "l1": "#3D0001", "l2": "#570001", "l3": "#700A09", "l4": "#8C2A33", "l5": "#38341E",
    "lu": "#817F6A", "l1f": "#5E0909", "l2f": "#870009", "l3f": "#A61C22", "l4f": "#C66A79",
    "l5f": "#524E36", "luf": "#AFAD9C", "l1t": "#FFE8EC", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#2B0509", "l5t": "#FFFFFF", "slot": "#1A0A0C", "shadow": "rgba(41,5,10,.22)", "wash-a": "rgba(135,0,9,.14)",
    "wash-b": "rgba(198,106,121,.10)", "gb2": "#5E0909", "gb3": "#870009", "gb4": "#DB8D9D", "brand-grad": "linear-gradient(90deg,#5E0909,#EC0000 55%,#FF8A80)",
    "gold-grad": "linear-gradient(135deg,#DB8D9D 0%,#870009 45%,#570001 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0D090A", "panel": "#191113", "panel-2": "#23181A", "ink": "#F7F2F4", "ink-2": "#E0D4D8",
    "muted": "#B4A4A9", "faint": "#918285", "line": "#372A2C", "line-2": "#4E3F42", "focus": "#D65C6F",
    "accent": "#CA495B", "link": "#DB8D9D", "gold": "#CA495B", "gold-deep": "#D65C6F", "gold-ink": "#DB8D9D",
    "l1": "#DB8D9D", "l2": "#D26D7E", "l3": "#DE7D80", "l4": "#E4A8B4", "l5": "#DBDAD1",
    "lu": "#A29F8A", "l1f": "#5E0909", "l2f": "#870009", "l3f": "#A61C22", "l4f": "#C66A79",
    "l5f": "#817F6A", "luf": "#817F6A", "slot": "#080506", "wash-a": "rgba(135,0,9,.12)", "wash-b": "rgba(198,106,121,.06)",
    "gb2": "#5E0909", "gb3": "#870009", "gb4": "#DB8D9D", "gold-grad": "linear-gradient(135deg,#F1BEC9 0%,#CA495B 45%,#870009 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
