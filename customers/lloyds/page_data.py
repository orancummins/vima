"""Lloyds Banking Group, as a platform: the data behind ``Lloyds_Banking_Group_Platform.html``.

``python customers/build_page.py lloyds`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Lloyds_Banking_Group_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from lloyds_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from lloyds_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Lloyds'
PAGE = 'Lloyds_Banking_Group_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Lloyds Platform"
KICKER = f"Lloyds Banking Group · as at {AS_OF}"
H1 = '<h1>Lloyds <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Lloyds's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Lloyds's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Lloyds's colours"

PIN = (51.51, -0.08, 'London')
PIN_FACING = 'the UK and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail', 'commercial': 'Commercial Banking', 'ipi': 'Insurance, Pensions & Investments', 'eic': 'Equity Investments & Central Items'}
DIV = {'lbg': 'Lloyds Banking Group', 'lloyds': 'Lloyds', 'halifax': 'Halifax', 'bos': 'Bank of Scotland', 'mbna': 'MBNA', 'widows': 'Scottish Widows', 'auto': 'Lloyds Auto', 'curve': 'Curve'}
DEFAULT_DIV = 'lbg'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F3", "panel-2": "#E3EEE8", "ink": "#091812", "ink-2": "#192821",
    "muted": "#3A4944", "faint": "#5E6C68", "line": "#C6D5D0", "line-2": "#A5B8B2", "focus": "#006A4A",
    "accent": "#006A4A", "link": "#005440", "gold": "#006A4A", "gold-deep": "#004A38", "gold-ink": "#005440",
    "l1": "#003729", "l2": "#004A38", "l3": "#095846", "l4": "#26775C", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#094C3C", "l2f": "#006A4A", "l3f": "#1B8E6E", "l4f": "#61BF99",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#091812", "shadow": "rgba(6,37,25,.22)", "wash-a": "rgba(0,106,74,.14)",
    "wash-b": "rgba(97,191,153,.10)", "gb2": "#094C3C", "gb3": "#006A4A", "gb4": "#86D6B3", "brand-grad": "linear-gradient(90deg,#004A38,#006A4A 55%,#86D6B3)",
    "gold-grad": "linear-gradient(135deg,#86D6B3 0%,#006A4A 45%,#004A38 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090D0B", "panel": "#101714", "panel-2": "#16201B", "ink": "#F2F7F4", "ink-2": "#D2DFD8",
    "muted": "#9DAEA9", "faint": "#788884", "line": "#232E2B", "line-2": "#323E3B", "focus": "#53D09F",
    "accent": "#3EC391", "link": "#86D6B3", "gold": "#3EC391", "gold-deep": "#53D09F", "gold-ink": "#86D6B3",
    "l1": "#86D6B3", "l2": "#64CCA2", "l3": "#75D9BE", "l4": "#A3E1C6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#094C3C", "l2f": "#006A4A", "l3f": "#1B8E6E", "l4f": "#61BF99",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050806", "wash-a": "rgba(0,106,74,.12)", "wash-b": "rgba(97,191,153,.06)",
    "gb2": "#094C3C", "gb3": "#006A4A", "gb4": "#86D6B3", "gold-grad": "linear-gradient(135deg,#BCEFD8 0%,#3EC391 45%,#006A4A 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
