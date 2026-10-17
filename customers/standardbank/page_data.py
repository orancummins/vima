"""Standard Bank Group, as a platform: the data behind ``Standard_Bank_Platform.html``.

``python customers/build_page.py standardbank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Standard_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from standardbank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from standardbank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Standard Bank'
PAGE = 'Standard_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Standard Bank Platform"
KICKER = f"Standard Bank Group · as at {AS_OF}"
H1 = '<h1>Standard Bank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Standard Bank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Standard Bank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Standard Bank's colours"

PIN = (-26.2, 28.04, 'Johannesburg')
PIN_FACING = 'Africa'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'ppb': 'Personal & Private Banking', 'bcb': 'Business & Commercial Banking', 'cib': 'Corporate & Investment Banking', 'iam': 'Insurance & Asset Management', 'group': 'Group & central'}
DIV = {'sbg': 'Standard Bank Group', 'sbsa': 'Standard Bank South Africa', 'africa': 'Africa Regions (Stanbic)', 'diners': 'Diners Club SA', 'shyft': 'Shyft', 'liberty': 'Liberty & STANLIB', 'offshore': 'Standard Bank Offshore'}
DEFAULT_DIV = 'sbg'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F4F6", "panel-2": "#E5EAEF", "ink": "#0B121C", "ink-2": "#202A35",
    "muted": "#555B6A", "faint": "#747A86", "line": "#CDD1DA", "line-2": "#B3B8C3", "focus": "#0033AA",
    "accent": "#0033AA", "link": "#001E7B", "gold": "#0033AA", "gold-deep": "#001966", "gold-ink": "#001E7B",
    "l1": "#001145", "l2": "#001966", "l3": "#0E2989", "l4": "#3357A1", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0D256F", "l2f": "#0033AA", "l3f": "#244EBC", "l4f": "#7A9ACA",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0B121C", "shadow": "rgba(7,21,44,.22)", "wash-a": "rgba(0,51,170,.14)",
    "wash-b": "rgba(122,154,202,.10)", "gb2": "#0D256F", "gb3": "#0033AA", "gb4": "#99B7DD", "brand-grad": "linear-gradient(90deg,#001966,#0033AA 55%,#99B7DD)",
    "gold-grad": "linear-gradient(135deg,#99B7DD 0%,#0033AA 45%,#001966 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090B0E", "panel": "#12171B", "panel-2": "#1B2027", "ink": "#F2F5F7", "ink-2": "#D6DDE2",
    "muted": "#ACB1BB", "faint": "#8E929B", "line": "#323742", "line-2": "#4E5461", "focus": "#6E97D7",
    "accent": "#5D86CC", "link": "#99B7DD", "gold": "#5D86CC", "gold-deep": "#6E97D7", "gold-ink": "#99B7DD",
    "l1": "#99B7DD", "l2": "#7CA0D4", "l3": "#8BA2DF", "l4": "#B0C7E5", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0D256F", "l2f": "#0033AA", "l3f": "#244EBC", "l4f": "#7A9ACA",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050708", "wash-a": "rgba(0,51,170,.12)", "wash-b": "rgba(122,154,202,.06)",
    "gb2": "#0D256F", "gb3": "#0033AA", "gb4": "#99B7DD", "gold-grad": "linear-gradient(135deg,#C3D8F1 0%,#5D86CC 45%,#0033AA 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
