"""Sumitomo Mitsui Card, as a platform: the data behind ``Sumitomo_Mitsui_Card_Platform.html``.

``python customers/build_page.py smcc`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Sumitomo_Mitsui_Card_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from smcc_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from smcc_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'SMBC Card'
PAGE = 'Sumitomo_Mitsui_Card_Platform.html'
AS_OF = "17 October 2026"
TITLE = "SMBC Card Platform"
KICKER = f"Sumitomo Mitsui Card Company, Limited · as at {AS_OF}"
H1 = '<h1>SMBC Card <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: SMBC Card's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in SMBC Card's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in SMBC Card's colours"

PIN = (35.65, 139.79, 'Tokyo')
PIN_FACING = 'Japan and Asia-Pacific'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'card': 'Card shopping', 'finance': 'Finance & consumer loans', 'merchant': 'Merchant & acquiring', 'guarantee': 'Loan guarantees & other'}
DIV = {'smcc': 'Sumitomo Mitsui Card', 'smfg': 'SMBC Group', 'olive': 'Olive (with SMBC)', 'stera': 'stera', 'smbccf': 'SMBC Consumer Finance', 'vpoint': 'V POINT MARKETING', 'partners': 'Co-brand & processing partners'}
DEFAULT_DIV = 'smcc'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F3", "panel-2": "#E3EDE7", "ink": "#091711", "ink-2": "#15221C",
    "muted": "#2D3935", "faint": "#535F5C", "line": "#C3D2CD", "line-2": "#9EB2AC", "focus": "#004B34",
    "accent": "#004B34", "link": "#004231", "gold": "#004B34", "gold-deep": "#003D2E", "gold-ink": "#004231",
    "l1": "#003024", "l2": "#003D2E", "l3": "#064033", "l4": "#1F624C", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#073B2E", "l2f": "#004B34", "l3f": "#17795D", "l4f": "#54BB91",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#091711", "shadow": "rgba(5,34,23,.22)", "wash-a": "rgba(0,75,52,.14)",
    "wash-b": "rgba(84,187,145,.10)", "gb2": "#073B2E", "gb3": "#004B34", "gb4": "#7DD3AD", "brand-grad": "linear-gradient(90deg,#003D2E,#004B34 55%,#7DD3AD)",
    "gold-grad": "linear-gradient(135deg,#7DD3AD 0%,#004B34 45%,#003D2E 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#080C0A", "panel": "#0F1512", "panel-2": "#131C18", "ink": "#F2F7F4", "ink-2": "#D0DDD6",
    "muted": "#95A8A2", "faint": "#6F7E7A", "line": "#1E2725", "line-2": "#2E3836", "focus": "#45CC97",
    "accent": "#39B586", "link": "#7DD3AD", "gold": "#39B586", "gold-deep": "#45CC97", "gold-ink": "#7DD3AD",
    "l1": "#7DD3AD", "l2": "#58C89B", "l3": "#6BD6B9", "l4": "#9DDFC2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#073B2E", "l2f": "#004B34", "l3f": "#17795D", "l4f": "#54BB91",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050806", "wash-a": "rgba(0,75,52,.12)", "wash-b": "rgba(84,187,145,.06)",
    "gb2": "#073B2E", "gb3": "#004B34", "gb4": "#7DD3AD", "gold-grad": "linear-gradient(135deg,#B9EFD6 0%,#39B586 45%,#004B34 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
