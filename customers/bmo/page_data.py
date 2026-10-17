"""BMO Financial Group, as a platform: the data behind ``BMO_Platform.html``.

``python customers/build_page.py bmo`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``BMO_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bmo_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bmo_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BMO'
PAGE = 'BMO_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BMO Platform"
KICKER = f"BMO Financial Group · as at {AS_OF}"
H1 = '<h1>BMO <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BMO's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BMO's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BMO's colours"

PIN = (43.65, -79.38, 'Toronto')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'cpc': 'Canadian P&C', 'usb': 'U.S. Banking', 'wm': 'Wealth Management', 'bcm': 'BMO Capital Markets', 'corp': 'Corporate Services'}
DIV = {'group': 'BMO Financial Group', 'canada': 'BMO (Canada)', 'us': 'BMO U.S.', 'blue': 'Blue Rewards', 'wealth': 'BMO Wealth Management', 'cm': 'BMO Capital Markets', 'moneris': 'Moneris'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F6", "panel-2": "#E5EEEF", "ink": "#0B181D", "ink-2": "#233539",
    "muted": "#5E6D76", "faint": "#7D888F", "line": "#CFD7DC", "line-2": "#B8C2C7", "focus": "#0079C1",
    "accent": "#0079C1", "link": "#004E89", "gold": "#0079C1", "gold-deep": "#004071", "gold-ink": "#004E89",
    "l1": "#002A4A", "l2": "#004071", "l3": "#0F5C9B", "l4": "#3887B0", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0F4C7C", "l2f": "#0079C1", "l3f": "#278BCC", "l4f": "#83B9CD",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0B181D", "shadow": "rgba(7,35,46,.22)", "wash-a": "rgba(0,121,193,.14)",
    "wash-b": "rgba(131,185,205,.10)", "gb2": "#0F4C7C", "gb3": "#0079C1", "gb4": "#A0D0DF", "brand-grad": "linear-gradient(90deg,#004071,#0079C1 55%,#A0D0DF)",
    "gold-grad": "linear-gradient(135deg,#A0D0DF 0%,#0079C1 45%,#004071 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0D0E", "panel": "#131B1D", "panel-2": "#1D272A", "ink": "#F2F7F7", "ink-2": "#D8E1E3",
    "muted": "#B2BBC0", "faint": "#959DA2", "line": "#384349", "line-2": "#59666E", "focus": "#78BEDA",
    "accent": "#68B0D0", "link": "#A0D0DF", "gold": "#68B0D0", "gold-deep": "#78BEDA", "gold-ink": "#A0D0DF",
    "l1": "#A0D0DF", "l2": "#85C1D7", "l3": "#93C2E1", "l4": "#B5DBE7", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0F4C7C", "l2f": "#0079C1", "l3f": "#278BCC", "l4f": "#83B9CD",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,121,193,.12)", "wash-b": "rgba(131,185,205,.06)",
    "gb2": "#0F4C7C", "gb3": "#0079C1", "gb4": "#A0D0DF", "gold-grad": "linear-gradient(135deg,#C5E8F1 0%,#68B0D0 45%,#0079C1 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
