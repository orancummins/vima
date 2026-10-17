"""Republic Bank, as a platform: the data behind ``Republic_Bank_Platform.html``.

``python customers/build_page.py republicbank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Republic_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from republicbank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from republicbank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Republic Bank'
PAGE = 'Republic_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Republic Bank Platform"
KICKER = f"Republic Bank · Republic Financial Holdings · as at {AS_OF}"
H1 = '<h1>Republic Bank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Republic Bank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Republic Bank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Republic Bank's colours"

PIN = (10.65, -61.51, 'Port of Spain')
PIN_FACING = 'the Caribbean'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail & commercial banking', 'ofs': 'Other financial services', 'region': 'Regional banks', 'group': 'Group & central'}
DIV = {'rfhl': 'Republic Financial Holdings', 'rbl': 'Republic Bank (T&T)', 'endcash': 'Endcash', 'wealth': 'Wealth & insurance', 'caribbean': 'Caribbean banks', 'ghana': 'Republic Bank (Ghana)'}
DEFAULT_DIV = 'rbl'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F6", "panel-2": "#E5EFEF", "ink": "#0B1A1D", "ink-2": "#23383A",
    "muted": "#5D6E74", "faint": "#7B898D", "line": "#CFD8DC", "line-2": "#B8C4C8", "focus": "#008FC3",
    "accent": "#008FC3", "link": "#005D8A", "gold": "#008FC3", "gold-deep": "#004D71", "gold-ink": "#005D8A",
    "l1": "#00324A", "l2": "#004D71", "l3": "#106B9C", "l4": "#3995B2", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0F597D", "l2f": "#008FC3", "l3f": "#279DCD", "l4f": "#84C1CD",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0B1A1D", "shadow": "rgba(7,39,46,.22)", "wash-a": "rgba(0,143,195,.14)",
    "wash-b": "rgba(132,193,205,.10)", "gb2": "#0F597D", "gb3": "#008FC3", "gb4": "#A1D7DF", "brand-grad": "linear-gradient(90deg,#004D71,#008FC3 55%,#A1D7DF)",
    "gold-grad": "linear-gradient(135deg,#A1D7DF 0%,#008FC3 45%,#004D71 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0E0E", "panel": "#131C1D", "panel-2": "#1D282A", "ink": "#F2F7F7", "ink-2": "#D8E3E3",
    "muted": "#B3BCC0", "faint": "#969FA3", "line": "#38454A", "line-2": "#59696F", "focus": "#008FC3",
    "accent": "#008FC3", "link": "#A1D7DF", "gold": "#008FC3", "gold-deep": "#79C9DA", "gold-ink": "#A1D7DF",
    "l1": "#A1D7DF", "l2": "#86CAD8", "l3": "#93CAE2", "l4": "#B5E0E7", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0F597D", "l2f": "#008FC3", "l3f": "#279DCD", "l4f": "#84C1CD",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,143,195,.12)", "wash-b": "rgba(132,193,205,.06)",
    "gb2": "#0F597D", "gb3": "#008FC3", "gb4": "#A1D7DF", "gold-grad": "linear-gradient(135deg,#C5EDF1 0%,#69BCD0 45%,#008FC3 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
