"""Nabil Bank, as a platform: the data behind ``Nabil_Bank_Platform.html``.

``python customers/build_page.py nabil`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Nabil_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from nabil_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from nabil_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Nabil'
PAGE = 'Nabil_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Nabil Platform"
KICKER = f"Nabil Bank Limited · as at {AS_OF}"
H1 = '<h1>Nabil <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Nabil's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Nabil's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Nabil's colours"

PIN = (27.71, 85.32, 'Kathmandu')
PIN_FACING = 'Nepal and South Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'fi': 'Financial intermediation', 'treasury': 'Treasury operations', 'trade': 'Trade finance', 'cards': 'Cards, e-banking & channels'}
DIV = {'nabil': 'Nabil Bank', 'nbank': 'nBank', 'remit': 'Nabil Remit', 'invest': 'Nabil Investment Banking', 'stock': 'Nabil Stock Dealer'}
DEFAULT_DIV = 'nabil'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F6F3", "panel-2": "#E6EEE8", "ink": "#0D1C12", "ink-2": "#25382B",
    "muted": "#62766B", "faint": "#808E87", "line": "#D1DBD5", "line-2": "#BAC6C0", "focus": "#11A955",
    "accent": "#11A955", "link": "#0D7943", "gold": "#11A955", "gold-deep": "#0A673A", "gold-ink": "#0D7943",
    "l1": "#074325", "l2": "#0A673A", "l3": "#1D905A", "l4": "#44A76E", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#197347", "l2f": "#12B25A", "l3f": "#37BF77", "l4f": "#8BC7A0",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0D1C12", "shadow": "rgba(11,43,23,.22)", "wash-a": "rgba(18,178,90,.14)",
    "wash-b": "rgba(139,199,160,.10)", "gb2": "#197347", "gb3": "#12B25A", "gb4": "#A7D9B7", "brand-grad": "linear-gradient(90deg,#0A673A,#12B25A 55%,#A7D9B7)",
    "gold-grad": "linear-gradient(135deg,#A7D9B7 0%,#12B25A 45%,#0A673A 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0E0B", "panel": "#141C17", "panel-2": "#1E2922", "ink": "#F3F7F4", "ink-2": "#D9E2DB",
    "muted": "#B4BFB9", "faint": "#97A29C", "line": "#3A4840", "line-2": "#5C6D64", "focus": "#12B25A",
    "accent": "#12B25A", "link": "#A7D9B7", "gold": "#12B25A", "gold-deep": "#82D19F", "gold-ink": "#A7D9B7",
    "l1": "#A7D9B7", "l2": "#8ED0A5", "l3": "#9BDBBA", "l4": "#BAE3C7", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#197347", "l2f": "#12B25A", "l3f": "#37BF77", "l4f": "#8BC7A0",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060806", "wash-a": "rgba(18,178,90,.12)", "wash-b": "rgba(139,199,160,.06)",
    "gb2": "#197347", "gb3": "#12B25A", "gb4": "#A7D9B7", "gold-grad": "linear-gradient(135deg,#C9EDD4 0%,#73C792 45%,#12B25A 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
