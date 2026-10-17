"""Nordea Bank Abp, as a platform: the data behind ``Nordea_Platform.html``.

``python customers/build_page.py nordea`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Nordea_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from nordea_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from nordea_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Nordea'
PAGE = 'Nordea_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Nordea Platform"
KICKER = f"Nordea Bank Abp · as at {AS_OF}"
H1 = '<h1>Nordea <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Nordea's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Nordea's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Nordea's colours"

PIN = (60.17, 24.94, 'Helsinki')
PIN_FACING = 'the Nordics'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'pb': 'Personal Banking', 'bb': 'Business Banking', 'lci': 'Large Corporates & Institutions', 'awm': 'Asset & Wealth Management', 'other': 'Group functions & other'}
DIV = {'group': 'Nordea Group', 'se': 'Nordea Sweden', 'fi': 'Nordea Finland', 'dk': 'Nordea Denmark', 'no': 'Nordea Norway', 'lp': 'Nordea Life & Pension', 'nam': 'Nordea Asset Management', 'finance': 'Nordea Finance'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F2F6", "panel-2": "#E5E7EE", "ink": "#0B0C1B", "ink-2": "#1F2233",
    "muted": "#505065", "faint": "#717182", "line": "#CCCCD9", "line-2": "#B1B1C1", "focus": "#0000A0",
    "accent": "#0000A0", "link": "#070075", "gold": "#0000A0", "gold-deep": "#060062", "gold-ink": "#070075",
    "l1": "#040042", "l2": "#060062", "l3": "#160D81", "l4": "#31349B", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#120D6A", "l2f": "#0000A0", "l3f": "#2622B5", "l4f": "#767EC8",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0B0C1B", "shadow": "rgba(6,9,43,.22)", "wash-a": "rgba(0,0,160,.14)",
    "wash-b": "rgba(118,126,200,.10)", "gb2": "#120D6A", "gb3": "#0000A0", "gb4": "#96A0DC", "brand-grad": "linear-gradient(90deg,#060062,#0000A0 55%,#96A0DC)",
    "gold-grad": "linear-gradient(135deg,#96A0DC 0%,#0000A0 45%,#060062 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090A0D", "panel": "#12131B", "panel-2": "#1A1C26", "ink": "#F2F3F7", "ink-2": "#D6D9E1",
    "muted": "#AAAAB9", "faint": "#8A8A98", "line": "#30303F", "line-2": "#4A4A5C", "focus": "#6A73D6",
    "accent": "#6B73D1", "link": "#96A0DC", "gold": "#6B73D1", "gold-deep": "#6A73D6", "gold-ink": "#96A0DC",
    "l1": "#96A0DC", "l2": "#7982D3", "l3": "#8A88DE", "l4": "#AEB5E5", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#120D6A", "l2f": "#0000A0", "l3f": "#2622B5", "l4f": "#767EC8",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050608", "wash-a": "rgba(0,0,160,.12)", "wash-b": "rgba(118,126,200,.06)",
    "gb2": "#120D6A", "gb3": "#0000A0", "gb4": "#96A0DC", "gold-grad": "linear-gradient(135deg,#C2C9F1 0%,#5860CB 45%,#0000A0 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
