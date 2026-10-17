"""NatWest Group, as a platform: the data behind ``NatWest_Group_Platform.html``.

``python customers/build_page.py natwest`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``NatWest_Group_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from natwest_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from natwest_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'NatWest'
PAGE = 'NatWest_Group_Platform.html'
AS_OF = "17 October 2026"
TITLE = "NatWest Platform"
KICKER = f"NatWest Group · as at {AS_OF}"
H1 = '<h1>NatWest <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: NatWest's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in NatWest's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in NatWest's colours"

PIN = (51.51, -0.09, 'London')
PIN_FACING = 'the UK and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail Banking', 'pbwm': 'Private Banking & Wealth Management', 'ci': 'Commercial & Institutional', 'grp': 'Central items'}
DIV = {'nwg': 'NatWest Group', 'natwest': 'NatWest', 'rbs': 'Royal Bank of Scotland', 'ulster': 'Ulster Bank', 'coutts': 'Coutts', 'mettle': 'Mettle', 'tyl': 'Tyl', 'grp': 'NatWest Group'}
DEFAULT_DIV = 'nwg'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F3F2F5", "panel-2": "#E8E5EC", "ink": "#110C16", "ink-2": "#1F1A24",
    "muted": "#403943", "faint": "#645E67", "line": "#CEC8D2", "line-2": "#AFA6B3", "focus": "#3C1053",
    "accent": "#3C1053", "link": "#340D43", "gold": "#3C1053", "gold-deep": "#2E0C3C", "gold-ink": "#340D43",
    "l1": "#22092D", "l2": "#2E0C3C", "l3": "#391446", "l4": "#523166", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#32133E", "l2f": "#3C1053", "l3f": "#5F2C78", "l4f": "#926DAF",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#110C16", "shadow": "rgba(22,10,31,.22)", "wash-a": "rgba(60,16,83,.14)",
    "wash-b": "rgba(146,109,175,.10)", "gb2": "#32133E", "gb3": "#3C1053", "gb4": "#AE91C8", "brand-grad": "linear-gradient(90deg,#2E0C3C,#3C1053 55%,#AE91C8)",
    "gold-grad": "linear-gradient(135deg,#AE91C8 0%,#3C1053 45%,#2E0C3C 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A090C", "panel": "#131116", "panel-2": "#1A171D", "ink": "#F4F3F6", "ink-2": "#D7D4DC",
    "muted": "#A69EAA", "faint": "#807984", "line": "#28232A", "line-2": "#39333C", "focus": "#9564BA",
    "accent": "#9566B6", "link": "#AE91C8", "gold": "#9566B6", "gold-deep": "#9564BA", "gold-ink": "#AE91C8",
    "l1": "#AE91C8", "l2": "#9A72BA", "l3": "#B383C8", "l4": "#C2ACD6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#32133E", "l2f": "#3C1053", "l3f": "#5F2C78", "l4f": "#926DAF",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060507", "wash-a": "rgba(60,16,83,.12)", "wash-b": "rgba(146,109,175,.06)",
    "gb2": "#32133E", "gb3": "#3C1053", "gb4": "#AE91C8", "gold-grad": "linear-gradient(135deg,#D5C4E7 0%,#8652AB 45%,#3C1053 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
