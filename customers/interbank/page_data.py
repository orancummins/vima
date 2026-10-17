"""Interbank, as a platform: the data behind ``Interbank_Platform.html``.

``python customers/build_page.py interbank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Interbank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from interbank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from interbank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Interbank'
PAGE = 'Interbank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Interbank Platform"
KICKER = f"Interbank (Banco Internacional del Perú) · as at {AS_OF}"
H1 = '<h1>Interbank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Interbank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Interbank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Interbank's colours"

PIN = (-12.1, -77.03, 'Lima')
PIN_FACING = 'Peru and Latin America'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail Banking', 'commercial': 'Commercial Banking', 'payments': 'Payments (Izipay)', 'group': 'Treasury & IFS group'}
DIV = {'ifs': 'Intercorp Financial Services', 'interbank': 'Interbank', 'izipay': 'Izipay', 'plin': 'Plin', 'interseguro': 'Interseguro', 'inteligo': 'Inteligo'}
DEFAULT_DIV = 'interbank'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F2", "panel-2": "#E5EEE7", "ink": "#0B1B11", "ink-2": "#1F3326",
    "muted": "#51665B", "faint": "#72837A", "line": "#CCD9D2", "line-2": "#B1C2B9", "focus": "#00A24F",
    "accent": "#00A24F", "link": "#007641", "gold": "#00A24F", "gold-deep": "#006336", "gold-ink": "#007641",
    "l1": "#004324", "l2": "#006336", "l3": "#0D8350", "l4": "#329C62", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0D6B40", "l2f": "#00A24F", "l3f": "#23B66E", "l4f": "#77C896",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0B1B11", "shadow": "rgba(6,43,21,.22)", "wash-a": "rgba(0,162,79,.14)",
    "wash-b": "rgba(119,200,150,.10)", "gb2": "#0D6B40", "gb3": "#00A24F", "gb4": "#97DCAF", "brand-grad": "linear-gradient(90deg,#006336,#00A24F 55%,#97DCAF)",
    "gold-grad": "linear-gradient(135deg,#97DCAF 0%,#00A24F 45%,#006336 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090D0B", "panel": "#121B15", "panel-2": "#1A261F", "ink": "#F2F7F3", "ink-2": "#D6E1D9",
    "muted": "#ABB9B2", "faint": "#8B9992", "line": "#303F38", "line-2": "#4B5D54", "focus": "#00A24F",
    "accent": "#00A24F", "link": "#97DCAF", "gold": "#00A24F", "gold-deep": "#6BD695", "gold-ink": "#97DCAF",
    "l1": "#97DCAF", "l2": "#79D39C", "l3": "#88DFB5", "l4": "#AFE5C2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0D6B40", "l2f": "#00A24F", "l3f": "#23B66E", "l4f": "#77C896",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050806", "wash-a": "rgba(0,162,79,.12)", "wash-b": "rgba(119,200,150,.06)",
    "gb2": "#0D6B40", "gb3": "#00A24F", "gb4": "#97DCAF", "gold-grad": "linear-gradient(135deg,#C2F1D1 0%,#59CB88 45%,#00A24F 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
