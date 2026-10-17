"""Landsbankinn, as a platform: the data behind ``Landsbankinn_Platform.html``.

``python customers/build_page.py landsbankinn`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Landsbankinn_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from landsbankinn_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from landsbankinn_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Landsbankinn'
PAGE = 'Landsbankinn_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Landsbankinn Platform"
KICKER = f"Landsbankinn hf. · as at {AS_OF}"
H1 = '<h1>Landsbankinn <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Landsbankinn's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Landsbankinn's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Landsbankinn's colours"

PIN = (64.15, -21.94, 'Reykjavík')
PIN_FACING = 'Iceland and the North Atlantic'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'personal': 'Personal Banking', 'corporate': 'Corporate Banking', 'am': 'Asset Management & Capital Markets', 'tm': 'TM tryggingar', 'other': 'Treasury & other divisions'}
DIV = {'lb': 'Landsbankinn', 'tm': 'TM tryggingar', 'landsbref': 'Landsbréf', 'yayland': 'Yayland', 'aukakronur': 'Aukakrónur'}
DEFAULT_DIV = 'lb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F4F5", "panel-2": "#E6EAEC", "ink": "#0E1316", "ink-2": "#21272A",
    "muted": "#4B5055", "faint": "#6D7175", "line": "#CDD0D4", "line-2": "#B0B4B9", "focus": "#20446A",
    "accent": "#20446A", "link": "#183050", "gold": "#20446A", "gold-deep": "#142944", "gold-ink": "#183050",
    "l1": "#0E1D2F", "l2": "#142944", "l3": "#233959", "l4": "#435D76", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#1E314B", "l2f": "#20446A", "l3f": "#3E6086", "l4f": "#819DB0",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0E1316", "shadow": "rgba(14,24,32,.22)", "wash-a": "rgba(32,68,106,.14)",
    "wash-b": "rgba(129,157,176,.10)", "gb2": "#1E314B", "gb3": "#20446A", "gb4": "#A1BAC8", "brand-grad": "linear-gradient(90deg,#142944,#20446A 55%,#A1BAC8)",
    "gold-grad": "linear-gradient(135deg,#A1BAC8 0%,#20446A 45%,#142944 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0B0C", "panel": "#131617", "panel-2": "#1B1E21", "ink": "#F3F5F6", "ink-2": "#D7DCDD",
    "muted": "#A8ADB1", "faint": "#868A8E", "line": "#2E3135", "line-2": "#44484C", "focus": "#7B9EB9",
    "accent": "#6A8EAB", "link": "#A1BAC8", "gold": "#6A8EAB", "gold-deep": "#7B9EB9", "gold-ink": "#A1BAC8",
    "l1": "#A1BAC8", "l2": "#86A5BA", "l3": "#95ACC7", "l4": "#B7CAD6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#1E314B", "l2f": "#20446A", "l3f": "#3E6086", "l4f": "#819DB0",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060707", "wash-a": "rgba(32,68,106,.12)", "wash-b": "rgba(129,157,176,.06)",
    "gb2": "#1E314B", "gb3": "#20446A", "gb4": "#A1BAC8", "gold-grad": "linear-gradient(135deg,#CBDBE5 0%,#6A8EAB 45%,#20446A 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
