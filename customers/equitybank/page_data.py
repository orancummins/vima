"""Equity Bank, as a platform: the data behind ``Equity_Bank_Platform.html``.

``python customers/build_page.py equitybank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Equity_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from equitybank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from equitybank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Equity'
PAGE = 'Equity_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Equity Platform"
KICKER = f"Equity Bank · Equity Group Holdings · as at {AS_OF}"
H1 = '<h1>Equity <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Equity's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Equity's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Equity's colours"

PIN = (-1.29, 36.82, 'Nairobi')
PIN_FACING = 'East and Central Africa'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'kenya': 'Equity Bank Kenya', 'regional': 'Regional banking subsidiaries', 'insurance': 'Equity Insurance Group', 'nonbank': 'Finserve, EIB & other non-banking'}
DIV = {'egh': 'Equity Group Holdings', 'ebkl': 'Equity Bank Kenya', 'bcdc': 'Equity BCDC (DRC)', 'region': 'Uganda, Rwanda, Tanzania & South Sudan', 'finserve': 'Finserve (Equitel)', 'insure': 'Equity Insurance Group', 'eib': 'Equity Investment Bank', 'egf': 'Equity Group Foundation'}
DEFAULT_DIV = 'egh'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F5F2F3", "panel-2": "#EDE8E9", "ink": "#1A0F10", "ink-2": "#37292B",
    "muted": "#746666", "faint": "#8D8282", "line": "#DAD3D3", "line-2": "#C6BDBD", "focus": "#A32A29",
    "accent": "#A32A29", "link": "#73231D", "gold": "#A32A29", "gold-deep": "#5E1C18", "gold-ink": "#73231D",
    "l1": "#3D120F", "l2": "#5E1C18", "l3": "#86362E", "l4": "#9F5455", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#6B2B27", "l2f": "#A32A29", "l3f": "#B14E4B", "l4f": "#C09599",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1A0F10", "shadow": "rgba(39,15,17,.22)", "wash-a": "rgba(163,42,41,.14)",
    "wash-b": "rgba(192,149,153,.10)", "gb2": "#6B2B27", "gb3": "#A32A29", "gb4": "#D4B0B4", "brand-grad": "linear-gradient(90deg,#5E1C18,#A32A29 55%,#D4B0B4)",
    "gold-grad": "linear-gradient(135deg,#D4B0B4 0%,#A32A29 45%,#5E1C18 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0D0B0B", "panel": "#1B1617", "panel-2": "#292021", "ink": "#F6F3F4", "ink-2": "#E1DBDC",
    "muted": "#BFB7B7", "faint": "#A39C9B", "line": "#493E3E", "line-2": "#6F6262", "focus": "#C88F94",
    "accent": "#BD8185", "link": "#D4B0B4", "gold": "#BD8185", "gold-deep": "#C88F94", "gold-ink": "#D4B0B4",
    "l1": "#D4B0B4", "l2": "#C9999E", "l3": "#D3A8A6", "l4": "#DEC1C4", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#6B2B27", "l2f": "#A32A29", "l3f": "#B14E4B", "l4f": "#C09599",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080607", "wash-a": "rgba(163,42,41,.12)", "wash-b": "rgba(192,149,153,.06)",
    "gb2": "#6B2B27", "gb3": "#A32A29", "gb4": "#D4B0B4", "gold-grad": "linear-gradient(135deg,#E9CFD3 0%,#BD8185 45%,#A32A29 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
