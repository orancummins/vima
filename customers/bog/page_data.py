"""Bank of Georgia, as a platform: the data behind ``Bank_of_Georgia_Platform.html``.

``python customers/build_page.py bog`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Bank_of_Georgia_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bog_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bog_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Bank of Georgia'
PAGE = 'Bank_of_Georgia_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Bank of Georgia Platform"
KICKER = f"Bank of Georgia · Lion Finance Group · as at {AS_OF}"
H1 = '<h1>Bank of Georgia <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Bank of Georgia's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Bank of Georgia's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Bank of Georgia's colours"

PIN = (41.69, 44.8, 'Tbilisi')
PIN_FACING = 'Georgia and the Caucasus'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail Banking', 'sme': 'SME Banking', 'cib': 'Corporate & Investment Banking', 'afs': 'Armenian Financial Services', 'other': 'Other Businesses & Corporate Center'}
DIV = {'lfg': 'Lion Finance Group', 'bog': 'Bank of Georgia', 'solo': 'SOLO', 'gt': 'Galt & Taggart', 'da': 'Digital Area', 'ameria': 'Ameriabank', 'bnb': 'BNB (Belarus)'}
DEFAULT_DIV = 'bog'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F2F2", "panel-2": "#F0E8E7", "ink": "#21110D", "ink-2": "#48302C",
    "muted": "#99887F", "faint": "#A89F9B", "line": "#E1DAD7", "line-2": "#D4CCC8", "focus": "#FF5C0A",
    "accent": "#FF5C0A", "link": "#B54700", "gold": "#FF5C0A", "gold-deep": "#903900", "gold-ink": "#B54700",
    "l1": "#592300", "l2": "#903900", "l3": "#D36415", "l4": "#CB7E5D", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#A44D14", "l2f": "#FF5C0A", "l3f": "#DE8452", "l4f": "#D8AD9F",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#21110D", "shadow": "rgba(54,20,8,.22)", "wash-a": "rgba(255,92,10,.14)",
    "wash-b": "rgba(216,173,159,.10)", "gb2": "#A44D14", "gb3": "#FF5C0A", "gb4": "#E6BFB6", "brand-grad": "linear-gradient(90deg,#903900,#FF5C0A 55%,#E6BFB6)",
    "gold-grad": "linear-gradient(135deg,#E6BFB6 0%,#FF5C0A 45%,#903900 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0A", "panel": "#211816", "panel-2": "#332623", "ink": "#F7F3F3", "ink-2": "#E6DDDD",
    "muted": "#CEC7C4", "faint": "#B7B1AD", "line": "#5F5049", "line-2": "#93827A", "focus": "#FF5C0A",
    "accent": "#FF5C0A", "link": "#E6BFB6", "gold": "#FF5C0A", "gold-deep": "#E2A996", "gold-ink": "#E6BFB6",
    "l1": "#E6BFB6", "l2": "#E0B0A1", "l3": "#E8C2AB", "l4": "#ECCCC4", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#A44D14", "l2f": "#FF5C0A", "l3f": "#DE8452", "l4f": "#D8AD9F",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090505", "wash-a": "rgba(255,92,10,.12)", "wash-b": "rgba(216,173,159,.06)",
    "gb2": "#A44D14", "gb3": "#FF5C0A", "gb4": "#E6BFB6", "gold-grad": "linear-gradient(135deg,#F3D4CD 0%,#DA9F8A 45%,#FF5C0A 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
