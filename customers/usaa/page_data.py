"""USAA, as a platform: the data behind ``USAA_Platform.html``.

``python customers/build_page.py usaa`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``USAA_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from usaa_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from usaa_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'USAA'
PAGE = 'USAA_Platform.html'
AS_OF = "17 October 2026"
TITLE = "USAA Platform"
KICKER = f"United Services Automobile Association · as at {AS_OF}"
H1 = '<h1>USAA <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: USAA's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in USAA's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in USAA's colours"

PIN = (29.42, -98.49, 'San Antonio')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'pc': 'Property & Casualty', 'bank': 'Banking', 'life': 'Life Insurance', 'corp': 'Association & corporate'}
DIV = {'usaa': 'USAA (the association)', 'fsb': 'USAA Federal Savings Bank', 'pcco': 'USAA P&C insurers', 'lifeco': 'USAA Life Insurance Company', 'alliance': 'USAA Alliance Services (Perks)', 'uis': 'USAA Investment Services'}
DEFAULT_DIV = 'usaa'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F4F5", "panel-2": "#E5EBEC", "ink": "#0C1216", "ink-2": "#1C2326",
    "muted": "#3E4348", "faint": "#61666B", "line": "#C9CED3", "line-2": "#A8AFB5", "focus": "#12395B",
    "accent": "#12395B", "link": "#0E2A48", "gold": "#12395B", "gold-deep": "#0C253F", "gold-ink": "#0E2A48",
    "l1": "#091B2E", "l2": "#0C253F", "l3": "#162F4D", "l4": "#34536B", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#152A42", "l2f": "#12395B", "l3f": "#2F577D", "l4f": "#7199B0",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0C1216", "shadow": "rgba(11,24,32,.22)", "wash-a": "rgba(18,57,91,.14)",
    "wash-b": "rgba(113,153,176,.10)", "gb2": "#152A42", "gb3": "#12395B", "gb4": "#94B8C9", "brand-grad": "linear-gradient(90deg,#0C253F,#12395B 55%,#94B8C9)",
    "gold-grad": "linear-gradient(135deg,#94B8C9 0%,#12395B 45%,#0C253F 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090B0C", "panel": "#111516", "panel-2": "#181C1E", "ink": "#F3F5F6", "ink-2": "#D4DBDD",
    "muted": "#A1A7AC", "faint": "#7C8287", "line": "#262A2D", "line-2": "#363A3E", "focus": "#689CBB",
    "accent": "#558BAD", "link": "#94B8C9", "gold": "#558BAD", "gold-deep": "#689CBB", "gold-ink": "#94B8C9",
    "l1": "#94B8C9", "l2": "#76A2BC", "l3": "#87A8C9", "l4": "#AEC9D7", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#152A42", "l2f": "#12395B", "l3f": "#2F577D", "l4f": "#7199B0",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050707", "wash-a": "rgba(18,57,91,.12)", "wash-b": "rgba(113,153,176,.06)",
    "gb2": "#152A42", "gb3": "#12395B", "gb4": "#94B8C9", "gold-grad": "linear-gradient(135deg,#C5DCE7 0%,#558BAD 45%,#12395B 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
