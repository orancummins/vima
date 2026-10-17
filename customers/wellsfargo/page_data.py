"""Wells Fargo, as a platform: the data behind ``Wells_Fargo_Platform.html``.

``python customers/build_page.py wellsfargo`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Wells_Fargo_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from wellsfargo_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from wellsfargo_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Wells Fargo'
PAGE = 'Wells_Fargo_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Wells Fargo Platform"
KICKER = f"Wells Fargo & Company · as at {AS_OF}"
H1 = '<h1>Wells Fargo <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Wells Fargo's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Wells Fargo's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Wells Fargo's colours"

PIN = (37.79, -122.4, 'San Francisco')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'cbl': 'Consumer Banking & Lending', 'cb': 'Commercial Banking', 'cib': 'Corporate & Investment Banking', 'wim': 'Wealth & Investment Management', 'corp': 'Corporate'}
DIV = {'wfc': 'Wells Fargo & Company', 'wf': 'Wells Fargo', 'cards': 'Wells Fargo Credit Cards', 'wfms': 'Wells Fargo Merchant Services', 'premier': 'Wells Fargo Premier', 'advisors': 'Wells Fargo Advisors', 'pb': 'Wells Fargo Private Bank'}
DEFAULT_DIV = 'wfc'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F3", "panel-2": "#EFE8EA", "ink": "#1E0F11", "ink-2": "#422D31",
    "muted": "#907B7C", "faint": "#A29797", "line": "#DFD7D7", "line-2": "#D0C6C7", "focus": "#DD1E25",
    "accent": "#DD1E25", "link": "#981715", "gold": "#DD1E25", "gold-deep": "#7A1310", "gold-ink": "#981715",
    "l1": "#4C0B0A", "l2": "#7A1310", "l3": "#B22F29", "l4": "#BA6167", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#8B2623", "l2f": "#DD1E25", "l3f": "#CA595B", "l4f": "#CFA1A7",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#1E0F11", "shadow": "rgba(47,13,17,.22)", "wash-a": "rgba(221,30,37,.14)",
    "wash-b": "rgba(207,161,167,.10)", "gb2": "#8B2623", "gb3": "#DD1E25", "gb4": "#DFB8BF", "brand-grad": "linear-gradient(90deg,#7A1310,#DD1E25 55%,#DFB8BF)",
    "gold-grad": "linear-gradient(135deg,#DFB8BF 0%,#DD1E25 45%,#7A1310 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0E0B0C", "panel": "#1F1719", "panel-2": "#2F2325", "ink": "#F7F3F4", "ink-2": "#E4DDDF",
    "muted": "#CAC1C2", "faint": "#B2AAAA", "line": "#584849", "line-2": "#8A7576", "focus": "#D79AA2",
    "accent": "#CE8E95", "link": "#DFB8BF", "gold": "#CE8E95", "gold-deep": "#D79AA2", "gold-ink": "#DFB8BF",
    "l1": "#DFB8BF", "l2": "#D7A4AB", "l3": "#DFAEAE", "l4": "#E6C6CB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#8B2623", "l2f": "#DD1E25", "l3f": "#CA595B", "l4f": "#CFA1A7",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080607", "wash-a": "rgba(221,30,37,.12)", "wash-b": "rgba(207,161,167,.06)",
    "gb2": "#8B2623", "gb3": "#DD1E25", "gb4": "#DFB8BF", "gold-grad": "linear-gradient(135deg,#EED0D6 0%,#CE8E95 45%,#DD1E25 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
