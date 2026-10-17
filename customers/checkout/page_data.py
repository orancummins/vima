"""Checkout.com, as a platform: the data behind ``Checkout_com_Platform.html``.

``python customers/build_page.py checkout`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Checkout_com_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from checkout_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from checkout_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Checkout.com'
PAGE = 'Checkout_com_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Checkout.com Platform"
KICKER = f"Checkout.com · as at {AS_OF}"
H1 = '<h1>Checkout.com <span class="os">Platform</span></h1>'
SERVES = 'who Checkout.com serves'

PALETTE_NOTE = ("Palette: Checkout.com's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Checkout.com's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Checkout.com's colours"

PIN = (51.52, -0.09, 'London')
PIN_FACING = 'Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'accept': 'Acceptance', 'move': 'Money movement', 'protect': 'Protect & optimise', 'grp': 'Group'}
DIV = {'cko': 'Checkout.com', 'us': 'Checkout.com US', 'eu': 'Checkout SAS (EEA)', 'mena': 'Checkout.com MENA', 'apac': 'Checkout.com APAC', 'grp': 'Checkout.com Group'}
DEFAULT_DIV = 'cko'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F5F7", "panel-2": "#E8EDF0", "ink": "#0D1722", "ink-2": "#2D3D4A",
    "muted": "#626B7C", "faint": "#838893", "line": "#D8DCE2", "line-2": "#C8CCD4", "focus": "#186AFF",
    "accent": "#186AFF", "link": "#0038BD", "gold": "#186AFF", "gold-deep": "#002D96", "gold-ink": "#0038BD",
    "l1": "#001C5C", "l2": "#002D96", "l3": "#164DDD", "l4": "#668ECE", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#1441AB", "l2f": "#186AFF", "l3f": "#5B87E0", "l4f": "#A4BDDB",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0D1722", "shadow": "rgba(8,29,55,.22)", "wash-a": "rgba(24,106,255,.14)",
    "wash-b": "rgba(164,189,219,.10)", "gb2": "#1441AB", "gb3": "#186AFF", "gb4": "#BAD1E8", "brand-grad": "linear-gradient(90deg,#002D96,#186AFF 55%,#BAD1E8)",
    "gold-grad": "linear-gradient(135deg,#BAD1E8 0%,#186AFF 45%,#002D96 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0B0D0F", "panel": "#171D22", "panel-2": "#242C34", "ink": "#F3F6F8", "ink-2": "#DEE3E7",
    "muted": "#C7CAD1", "faint": "#B2B5BB", "line": "#4C5464", "line-2": "#818A99", "focus": "#9CBCE4",
    "accent": "#91B1DD", "link": "#BAD1E8", "gold": "#91B1DD", "gold-deep": "#9CBCE4", "gold-ink": "#BAD1E8",
    "l1": "#BAD1E8", "l2": "#A6C1E2", "l3": "#B0C3E9", "l4": "#C7D9ED", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#1441AB", "l2f": "#186AFF", "l3f": "#5B87E0", "l4f": "#A4BDDB",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060809", "wash-a": "rgba(24,106,255,.12)", "wash-b": "rgba(164,189,219,.06)",
    "gb2": "#1441AB", "gb3": "#186AFF", "gb4": "#BAD1E8", "gold-grad": "linear-gradient(135deg,#CEE1F4 0%,#91B1DD 45%,#186AFF 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
