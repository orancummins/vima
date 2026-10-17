"""FirstRand (FNB), as a platform: the data behind ``FirstRand_FNB_Platform.html``.

``python customers/build_page.py firstrand`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``FirstRand_FNB_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from firstrand_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from firstrand_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'FNB'
PAGE = 'FirstRand_FNB_Platform.html'
AS_OF = "17 October 2026"
TITLE = "FNB Platform"
KICKER = f"FirstRand (FNB) · as at {AS_OF}"
H1 = '<h1>FNB <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: FNB's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in FNB's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in FNB's colours"

PIN = (-26.11, 28.05, 'Johannesburg')
PIN_FACING = 'South Africa and Africa'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'fnb': 'FNB', 'rmb': 'RMB', 'wesbank': 'WesBank', 'centre': 'Centre & Group Treasury', 'uk': 'UK operations (discontinued)'}
DIV = {'frg': 'FirstRand', 'fnb': 'FNB', 'private': 'FNB Private', 'ebucks': 'eBucks', 'africa': 'FNB broader Africa', 'rmb': 'RMB', 'wesbank': 'WesBank', 'aldermore': 'Aldermore'}
DEFAULT_DIV = 'frg'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F5", "panel-2": "#E5EFEC", "ink": "#0B1C1B", "ink-2": "#203532",
    "muted": "#556B6B", "faint": "#758787", "line": "#CDDADA", "line-2": "#B3C3C4", "focus": "#00A4A7",
    "accent": "#00A4A7", "link": "#00737C", "gold": "#00A4A7", "gold-deep": "#006067", "gold-ink": "#00737C",
    "l1": "#004045", "l2": "#006067", "l3": "#0E7E8B", "l4": "#34A3A1", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0D6970", "l2f": "#00A9AC", "l3f": "#24B7BD", "l4f": "#7BCAC3",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0B1C1B", "shadow": "rgba(7,44,42,.22)", "wash-a": "rgba(0,169,172,.14)",
    "wash-b": "rgba(123,202,195,.10)", "gb2": "#0D6970", "gb3": "#00A9AC", "gb4": "#9ADDD5", "brand-grad": "linear-gradient(90deg,#006067,#00A9AC 55%,#9ADDD5)",
    "gold-grad": "linear-gradient(135deg,#9ADDD5 0%,#00A9AC 45%,#006067 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090E0D", "panel": "#131B1A", "panel-2": "#1B2726", "ink": "#F2F7F6", "ink-2": "#D6E2DF",
    "muted": "#ADBBBB", "faint": "#8E9C9C", "line": "#334242", "line-2": "#4F6262", "focus": "#00A9AC",
    "accent": "#00A9AC", "link": "#9ADDD5", "gold": "#00A9AC", "gold-deep": "#6FD7D0", "gold-ink": "#9ADDD5",
    "l1": "#9ADDD5", "l2": "#7DD5CD", "l3": "#8CDBDF", "l4": "#B1E5DF", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0D6970", "l2f": "#00A9AC", "l3f": "#24B7BD", "l4f": "#7BCAC3",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050807", "wash-a": "rgba(0,169,172,.12)", "wash-b": "rgba(123,202,195,.06)",
    "gb2": "#0D6970", "gb3": "#00A9AC", "gb4": "#9ADDD5", "gold-grad": "linear-gradient(135deg,#C3F1EB 0%,#5ECDC6 45%,#00A9AC 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
