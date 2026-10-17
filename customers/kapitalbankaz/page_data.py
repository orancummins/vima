"""Kapital Bank, as a platform: the data behind ``Kapital_Bank_Azerbaijan_Platform.html``.

``python customers/build_page.py kapitalbankaz`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Kapital_Bank_Azerbaijan_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from kapitalbankaz_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from kapitalbankaz_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Kapital Bank'
PAGE = 'Kapital_Bank_Azerbaijan_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Kapital Bank Platform"
KICKER = f"Kapital Bank OJSC (Birbank), Azerbaijan · as at {AS_OF}"
H1 = '<h1>Kapital Bank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Kapital Bank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Kapital Bank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Kapital Bank's colours"

PIN = (40.38, 49.86, 'Baku')
PIN_FACING = 'Azerbaijan and the Caucasus'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail Banking', 'corporate': 'Corporate Banking', 'treasury': 'Treasury', 'eco': 'Ecosystem'}
DIV = {'kb': 'Kapital Bank', 'birbank': 'Birbank', 'biznes': 'Birbank Biznes', 'private': 'Birbank Private', 'pashapay': 'PashaPay (m10, MilliÖn)', 'competo': 'Competo (Birmarket, Bir Bonus)', 'invest': 'Birbank Invest'}
DEFAULT_DIV = 'kb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F3", "panel-2": "#EEE7E9", "ink": "#1C0E11", "ink-2": "#3A282D",
    "muted": "#7C696B", "faint": "#938788", "line": "#DBD3D3", "line-2": "#C8BEBF", "focus": "#B61D29",
    "accent": "#B61D29", "link": "#801416", "gold": "#B61D29", "gold-deep": "#681112", "gold-ink": "#801416",
    "l1": "#430B0C", "l2": "#681112", "l3": "#942626", "l4": "#AB4E58", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#762022", "l2f": "#B61D29", "l3f": "#BF434A", "l4f": "#C6939C",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1C0E11", "shadow": "rgba(43,13,17,.22)", "wash-a": "rgba(182,29,41,.14)",
    "wash-b": "rgba(198,147,156,.10)", "gb2": "#762022", "gb3": "#B61D29", "gb4": "#D9AEB7", "brand-grad": "linear-gradient(90deg,#681112,#B61D29 55%,#D9AEB7)",
    "gold-grad": "linear-gradient(135deg,#D9AEB7 0%,#B61D29 45%,#681112 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0E0A0B", "panel": "#1C1517", "panel-2": "#2A2022", "ink": "#F7F3F4", "ink-2": "#E2DBDD",
    "muted": "#C1B8B9", "faint": "#A69D9E", "line": "#4C3F40", "line-2": "#746465", "focus": "#CF8C97",
    "accent": "#C57E89", "link": "#D9AEB7", "gold": "#C57E89", "gold-deep": "#CF8C97", "gold-ink": "#D9AEB7",
    "l1": "#D9AEB7", "l2": "#CF97A1", "l3": "#D9A3A6", "l4": "#E2BFC6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#762022", "l2f": "#B61D29", "l3f": "#BF434A", "l4f": "#C6939C",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080607", "wash-a": "rgba(182,29,41,.12)", "wash-b": "rgba(198,147,156,.06)",
    "gb2": "#762022", "gb3": "#B61D29", "gb4": "#D9AEB7", "gold-grad": "linear-gradient(135deg,#ECCDD4 0%,#C57E89 45%,#B61D29 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
