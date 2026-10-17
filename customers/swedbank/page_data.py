"""Swedbank, as a platform: the data behind ``Swedbank_Platform.html``.

``python customers/build_page.py swedbank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Swedbank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from swedbank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from swedbank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Swedbank'
PAGE = 'Swedbank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Swedbank Platform"
KICKER = f"Swedbank AB · as at {AS_OF}"
H1 = '<h1>Swedbank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Swedbank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Swedbank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Swedbank's colours"

PIN = (59.36, 17.97, 'Stockholm')
PIN_FACING = 'Sweden and the Baltics'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'swe': 'Swedish Banking', 'baltic': 'Baltic Banking', 'ci': 'Corporates and Institutions', 'wealth': 'Wealth Management', 'other': 'Group Functions & Other'}
DIV = {'group': 'Swedbank Group', 'se': 'Swedbank Sweden', 'ee': 'Swedbank Estonia', 'lv': 'Swedbank Latvia', 'lt': 'Swedbank Lithuania', 'entercard': 'Entercard', 'pay': 'Swedbank Pay', 'robur': 'Swedbank Robur'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F2F2", "panel-2": "#F0E8E7", "ink": "#21120D", "ink-2": "#46302A",
    "muted": "#95847A", "faint": "#A59C97", "line": "#E0DAD6", "line-2": "#D2CAC6", "focus": "#FF5F00",
    "accent": "#FF5F00", "link": "#AF4B00", "gold": "#FF5F00", "gold-deep": "#8C3C00", "gold-ink": "#AF4B00",
    "l1": "#572500", "l2": "#8C3C00", "l3": "#CB6714", "l4": "#C97E56", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#9E4F13", "l2f": "#FF5F00", "l3f": "#DD844A", "l4f": "#D7AB9B",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#21120D", "shadow": "rgba(53,21,8,.22)", "wash-a": "rgba(255,95,0,.14)",
    "wash-b": "rgba(215,171,155,.10)", "gb2": "#9E4F13", "gb3": "#FF5F00", "gb4": "#E5BFB3", "brand-grad": "linear-gradient(90deg,#8C3C00,#FF5F00 55%,#E5BFB3)",
    "gold-grad": "linear-gradient(135deg,#E5BFB3 0%,#FF5F00 45%,#8C3C00 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0A", "panel": "#201816", "panel-2": "#312622", "ink": "#F7F3F3", "ink-2": "#E6DDDC",
    "muted": "#CCC5C1", "faint": "#B4AEAA", "line": "#5C4F46", "line-2": "#8F7E74", "focus": "#FF5F00",
    "accent": "#FF5F00", "link": "#E5BFB3", "gold": "#FF5F00", "gold-deep": "#E1A992", "gold-ink": "#E5BFB3",
    "l1": "#E5BFB3", "l2": "#DFAF9D", "l3": "#E7C2A8", "l4": "#EBCCC2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#9E4F13", "l2f": "#FF5F00", "l3f": "#DD844A", "l4f": "#D7AB9B",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090605", "wash-a": "rgba(255,95,0,.12)", "wash-b": "rgba(215,171,155,.06)",
    "gb2": "#9E4F13", "gb3": "#FF5F00", "gb4": "#E5BFB3", "gold-grad": "linear-gradient(135deg,#F3D4CC 0%,#D99E85 45%,#FF5F00 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
