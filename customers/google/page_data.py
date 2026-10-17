"""Google, as a platform: the data behind ``Google_Platform.html``.

``python customers/build_page.py google`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Google_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from google_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from google_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Google'
PAGE = 'Google_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Google Platform"
KICKER = f"Google (Alphabet Inc.), read through payments · as at {AS_OF}"
H1 = '<h1>Google <span class="os">Platform</span></h1>'
SERVES = 'who Google Pay serves'

PALETTE_NOTE = ("Palette: Google's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Google's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Google's colours"

PIN = (37.42, -122.08, 'Mountain View')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'services': 'Google Services', 'cloud': 'Google Cloud', 'grp': 'Alphabet-level'}
DIV = {'pay': 'Google Pay & Wallet', 'india': 'Google Pay India', 'commerce': 'Shopping & AI commerce', 'agents': 'Agentic payments', 'cloud': 'Google Cloud', 'grp': 'Alphabet Inc.'}
DEFAULT_DIV = 'pay'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F5F7", "panel-2": "#E9EEF0", "ink": "#0F1822", "ink-2": "#33424F",
    "muted": "#636C7A", "faint": "#838992", "line": "#DCDFE4", "line-2": "#C8CCD2", "focus": "#4285F4",
    "accent": "#4285F4", "link": "#0B46C4", "gold": "#4285F4", "gold-deep": "#09389B", "gold-ink": "#0B46C4",
    "l1": "#05225D", "l2": "#09389B", "l3": "#2F63DE", "l4": "#7FA0D0", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#204EB3", "l2f": "#4285F4", "l3f": "#789CDE", "l4f": "#B3C7DD",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0F1822", "shadow": "rgba(12,32,56,.22)", "wash-a": "rgba(66,133,244,.14)",
    "wash-b": "rgba(179,199,221,.10)", "gb2": "#204EB3", "gb3": "#4285F4", "gb4": "#C5D8E9", "brand-grad": "linear-gradient(90deg,#09389B,#4285F4 55%,#C5D8E9)",
    "gold-grad": "linear-gradient(135deg,#C5D8E9 0%,#4285F4 45%,#09389B 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0B0E10", "panel": "#191E23", "panel-2": "#272F37", "ink": "#F3F6F7", "ink-2": "#E0E5E8",
    "muted": "#CFD2D7", "faint": "#BDBFC4", "line": "#555D6C", "line-2": "#939AA6", "focus": "#4285F4",
    "accent": "#4285F4", "link": "#C5D8E9", "gold": "#4285F4", "gold-deep": "#ADC7E4", "gold-ink": "#C5D8E9",
    "l1": "#C5D8E9", "l2": "#B5CBE3", "l3": "#BDCDEA", "l4": "#CFDEED", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#204EB3", "l2f": "#4285F4", "l3f": "#789CDE", "l4f": "#B3C7DD",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060809", "wash-a": "rgba(66,133,244,.12)", "wash-b": "rgba(179,199,221,.06)",
    "gb2": "#204EB3", "gb3": "#4285F4", "gb4": "#C5D8E9", "gold-grad": "linear-gradient(135deg,#D3E4F2 0%,#A3BDDE 45%,#4285F4 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
