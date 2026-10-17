"""Commerzbank, as a platform: the data behind ``Commerzbank_Platform.html``.

``python customers/build_page.py commerzbank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Commerzbank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from commerzbank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from commerzbank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Commerzbank'
PAGE = 'Commerzbank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Commerzbank Platform"
KICKER = f"Commerzbank AG · as at {AS_OF}"
H1 = '<h1>Commerzbank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Commerzbank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Commerzbank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Commerzbank's colours"

PIN = (50.11, 8.67, 'Frankfurt')
PIN_FACING = 'Germany and Poland'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'psbc': 'Private and Small-Business Customers', 'cc': 'Corporate Clients', 'mbank': 'mBank', 'oci': 'Others & Consolidation'}
DIV = {'cbk': 'Commerzbank Group', 'commerzbank': 'Commerzbank', 'comdirect': 'comdirect', 'mbank': 'mBank', 'globalpay': 'Commerz Globalpay', 'ucg': 'UniCredit position'}
DEFAULT_DIV = 'cbk'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F0F6F6", "panel-2": "#E2EDEC", "ink": "#081416", "ink-2": "#131E1F",
    "muted": "#272E31", "faint": "#4D5759", "line": "#C1CDD1", "line-2": "#9AABB0", "focus": "#002E3C",
    "accent": "#002E3C", "link": "#002839", "gold": "#002E3C", "gold-deep": "#002636", "gold-ink": "#002839",
    "l1": "#00202D", "l2": "#002636", "l3": "#052534", "l4": "#1C4C58", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#062633", "l2f": "#002E3C", "l3f": "#15576E", "l4f": "#4FAAB8",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#081416", "shadow": "rgba(5,28,32,.22)", "wash-a": "rgba(0,46,60,.14)",
    "wash-b": "rgba(79,170,184,.10)", "gb2": "#062633", "gb3": "#002E3C", "gb4": "#79C9D1", "brand-grad": "linear-gradient(90deg,#002636,#002E3C 55%,#79C9D1)",
    "gold-grad": "linear-gradient(135deg,#79C9D1 0%,#002E3C 45%,#002636 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#080C0C", "panel": "#0E1414", "panel-2": "#12191A", "ink": "#F2F7F7", "ink-2": "#CFDCDC",
    "muted": "#92A1A5", "faint": "#6B7679", "line": "#1F2629", "line-2": "#2E3739", "focus": "#3FB6CA",
    "accent": "#369BAE", "link": "#79C9D1", "gold": "#369BAE", "gold-deep": "#3FB6CA", "gold-ink": "#79C9D1",
    "l1": "#79C9D1", "l2": "#52B7C7", "l3": "#65B7D5", "l4": "#9AD7DE", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#062633", "l2f": "#002E3C", "l3f": "#15576E", "l4f": "#4FAAB8",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050807", "wash-a": "rgba(0,46,60,.12)", "wash-b": "rgba(79,170,184,.06)",
    "gb2": "#062633", "gb3": "#002E3C", "gb4": "#79C9D1", "gold-grad": "linear-gradient(135deg,#B7EAEE 0%,#369BAE 45%,#002E3C 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
