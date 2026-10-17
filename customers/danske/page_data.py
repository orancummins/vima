"""Danske Bank, as a platform: the data behind ``Danske_Bank_Platform.html``.

``python customers/build_page.py danske`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Danske_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from danske_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from danske_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Danske Bank'
PAGE = 'Danske_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Danske Bank Platform"
KICKER = f"Danske Bank · as at {AS_OF}"
H1 = '<h1>Danske Bank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Danske Bank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Danske Bank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Danske Bank's colours"

PIN = (55.68, 12.57, 'Copenhagen')
PIN_FACING = 'the Nordics and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'personal': 'Personal Customers', 'business': 'Business Customers', 'lci': 'Large Corporates & Institutions', 'danica': 'Danica', 'other': 'Northern Ireland & Group Functions'}
DIV = {'group': 'Danske Bank Group', 'dk': 'Danske Bank Denmark', 'nordic': 'Danske Bank Finland & Sweden', 'uk': 'Danske Bank UK (Northern Bank)', 'rd': 'Realkredit Danmark', 'danica': 'Danica Pension', 'invest': 'Danske Invest', 'mobilepay': 'Vipps MobilePay (associate)'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E2EBED", "ink": "#091116", "ink-2": "#141D21",
    "muted": "#2B3036", "faint": "#51575D", "line": "#C2CAD2", "line-2": "#9CA7B2", "focus": "#002346",
    "accent": "#002346", "link": "#001C3F", "gold": "#002346", "gold-deep": "#001A3A", "gold-ink": "#001C3F",
    "l1": "#00152F", "l2": "#001A3A", "l3": "#061D3C", "l4": "#1E405F", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#071C38", "l2f": "#002346", "l3f": "#164375", "l4f": "#5390BA",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#091116", "shadow": "rgba(5,21,33,.22)", "wash-a": "rgba(0,35,70,.14)",
    "wash-b": "rgba(83,144,186,.10)", "gb2": "#071C38", "gb3": "#002346", "gb4": "#7CB3D2", "brand-grad": "linear-gradient(90deg,#001A3A,#002346 55%,#7CB3D2)",
    "gold-grad": "linear-gradient(135deg,#7CB3D2 0%,#002346 45%,#001A3A 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#080B0C", "panel": "#0E1315", "panel-2": "#13181B", "ink": "#F2F6F7", "ink-2": "#D0DADD",
    "muted": "#949EA7", "faint": "#6E757D", "line": "#1F2429", "line-2": "#30363C", "focus": "#4393CB",
    "accent": "#387EB2", "link": "#7CB3D2", "gold": "#387EB2", "gold-deep": "#4393CB", "gold-ink": "#7CB3D2",
    "l1": "#7CB3D2", "l2": "#569AC8", "l3": "#699CD6", "l4": "#9CC6DF", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#071C38", "l2f": "#002346", "l3f": "#164375", "l4f": "#5390BA",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050708", "wash-a": "rgba(0,35,70,.12)", "wash-b": "rgba(83,144,186,.06)",
    "gb2": "#071C38", "gb3": "#002346", "gb4": "#7CB3D2", "gold-grad": "linear-gradient(135deg,#B8DCEE 0%,#387EB2 45%,#002346 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
