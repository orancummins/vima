"""Chime Financial, as a platform: the data behind ``Chime_Platform.html``.

``python customers/build_page.py chime`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Chime_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from chime_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from chime_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Chime'
PAGE = 'Chime_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Chime Platform"
KICKER = f"Chime Financial · as at {AS_OF}"
H1 = '<h1>Chime <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Chime's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Chime's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Chime's colours"

PIN = (37.79, -122.4, 'San Francisco')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'payments': 'Payments (interchange)', 'platform': 'Platform-related (MyPay, loans)', 'corp': 'Group & central'}
DIV = {'chime': 'Chime', 'banks': 'Partner banks (Bancorp, Stride)', 'chimebank': 'Chime Bank, N.A. (pending)', 'capital': 'Chime Capital', 'enterprise': 'Chime Enterprise', 'invest': 'Chime Invest (with Atomic)'}
DEFAULT_DIV = 'chime'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F6F3", "panel-2": "#E8EEE9", "ink": "#0E1D14", "ink-2": "#2B3D31",
    "muted": "#5D6F67", "faint": "#7E8A85", "line": "#D4DDD9", "line-2": "#C2CCC7", "focus": "#19A764",
    "accent": "#19A764", "link": "#12774E", "gold": "#19A764", "gold-deep": "#116F48", "gold-ink": "#12774E",
    "l1": "#0B462E", "l2": "#116F48", "l3": "#28A071", "l4": "#55B384", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#227F59", "l2f": "#1EC677", "l3f": "#4DC48E", "l4f": "#99CAAE",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0E1D14", "shadow": "rgba(13,44,27,.22)", "wash-a": "rgba(30,198,119,.14)",
    "wash-b": "rgba(153,202,174,.10)", "gb2": "#227F59", "gb3": "#1EC677", "gb4": "#B2DBC2", "brand-grad": "linear-gradient(90deg,#116F48,#1EC677 55%,#B2DBC2)",
    "gold-grad": "linear-gradient(135deg,#B2DBC2 0%,#1EC677 45%,#116F48 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0B0E0C", "panel": "#161D19", "panel-2": "#222C26", "ink": "#F3F7F4", "ink-2": "#DCE3DE",
    "muted": "#BCC5C1", "faint": "#A2ABA7", "line": "#43514A", "line-2": "#6B7D75", "focus": "#1EC677",
    "accent": "#1EC677", "link": "#B2DBC2", "gold": "#1EC677", "gold-deep": "#92D2AE", "gold-ink": "#B2DBC2",
    "l1": "#B2DBC2", "l2": "#9CD2B3", "l3": "#A8DBC5", "l4": "#C2E3CF", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#227F59", "l2f": "#1EC677", "l3f": "#4DC48E", "l4f": "#99CAAE",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060806", "wash-a": "rgba(30,198,119,.12)", "wash-b": "rgba(153,202,174,.06)",
    "gb2": "#227F59", "gb3": "#1EC677", "gb4": "#B2DBC2", "gold-grad": "linear-gradient(135deg,#CEEDDA 0%,#85C9A4 45%,#1EC677 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
