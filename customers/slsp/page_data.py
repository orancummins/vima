"""Slovenská sporiteľňa, as a platform: the data behind ``Slovenska_sporitelna_Platform.html``.

``python customers/build_page.py slsp`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Slovenska_sporitelna_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from slsp_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from slsp_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Slovenská sporiteľňa'
PAGE = 'Slovenska_sporitelna_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Slovenská sporiteľňa Platform"
KICKER = f"Slovenská sporiteľňa · as at {AS_OF}"
H1 = '<h1>Slovenská sporiteľňa <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Slovenská sporiteľňa's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Slovenská sporiteľňa's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Slovenská sporiteľňa's colours"

PIN = (48.16, 17.14, 'Bratislava')
PIN_FACING = 'Slovakia and Central Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail', 'corporates': 'Corporates', 'markets': 'Group Markets', 'alm': 'ALM & Local Corporate Center'}
DIV = {'slsp': 'Slovenská sporiteľňa', 'george': 'George', 'erste': 'Erste Group', 'gp': 'Global Payments (JV)', 'pss': 'Prvá stavebná sporiteľňa', 'social': 'SLSP Social Finance', 'foundation': 'Nadácia Slovenskej sporiteľne'}
DEFAULT_DIV = 'slsp'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F5F6", "panel-2": "#E8EDF0", "ink": "#0F1720", "ink-2": "#2F3C48",
    "muted": "#878F9C", "faint": "#A1A5AC", "line": "#D9DCE1", "line-2": "#CCCFD5", "focus": "#2870ED",
    "accent": "#2870ED", "link": "#0F3FAD", "gold": "#2870ED", "gold-deep": "#0C328A", "gold-ink": "#0F3FAD",
    "l1": "#071F55", "l2": "#0C328A", "l3": "#2555CD", "l4": "#6D90C6", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#20469F", "l2f": "#2870ED", "l3f": "#648BD5", "l4f": "#A8BDD6",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0F1720", "shadow": "rgba(12,30,52,.22)", "wash-a": "rgba(40,112,237,.14)",
    "wash-b": "rgba(168,189,214,.10)", "gb2": "#20469F", "gb3": "#2870ED", "gb4": "#BDD1E4", "brand-grad": "linear-gradient(90deg,#0C328A,#2870ED 55%,#BDD1E4)",
    "gold-grad": "linear-gradient(135deg,#BDD1E4 0%,#2870ED 45%,#0C328A 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0B0D0F", "panel": "#181D21", "panel-2": "#252C33", "ink": "#F3F6F7", "ink-2": "#DEE3E6",
    "muted": "#C7CAD0", "faint": "#B2B5BA", "line": "#4D5561", "line-2": "#828A97", "focus": "#A1BDDE",
    "accent": "#96B2D6", "link": "#BDD1E4", "gold": "#96B2D6", "gold-deep": "#A1BDDE", "gold-ink": "#BDD1E4",
    "l1": "#BDD1E4", "l2": "#AAC2DD", "l3": "#B4C4E5", "l4": "#C9D9EA", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#20469F", "l2f": "#2870ED", "l3f": "#648BD5", "l4f": "#A8BDD6",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060809", "wash-a": "rgba(40,112,237,.12)", "wash-b": "rgba(168,189,214,.06)",
    "gb2": "#20469F", "gb3": "#2870ED", "gb4": "#BDD1E4", "gold-grad": "linear-gradient(135deg,#D1E1F1 0%,#96B2D6 45%,#2870ED 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
