"""Vietcombank, as a platform: the data behind ``Vietcombank_Platform.html``.

``python customers/build_page.py vietcombank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Vietcombank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from vietcombank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from vietcombank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Vietcombank'
PAGE = 'Vietcombank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Vietcombank Platform"
KICKER = f"Joint Stock Commercial Bank for Foreign Trade of Vietnam · as at {AS_OF}"
H1 = '<h1>Vietcombank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Vietcombank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Vietcombank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Vietcombank's colours"

PIN = (21.02, 105.86, 'Hanoi')
PIN_FACING = 'Vietnam and Asia-Pacific'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail banking', 'wholesale': 'Wholesale banking', 'markets': 'Capital & markets', 'group': 'Group & subsidiaries'}
DIV = {'vcb': 'Vietcombank', 'cards': 'Vietcombank cards', 'digi': 'VCB Digibank', 'vcbneo': 'VCBNeo', 'vcbs': 'VCBS & VCB Leasing', 'laos': 'Vietcombank Laos', 'remit': 'VCB Money & Remittance'}
DEFAULT_DIV = 'vcb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F2", "panel-2": "#E3EDE5", "ink": "#09170E", "ink-2": "#15231A",
    "muted": "#2F3B35", "faint": "#55625B", "line": "#C3D3CB", "line-2": "#9FB3A9", "focus": "#005028",
    "accent": "#005028", "link": "#004526", "gold": "#005028", "gold-deep": "#003F23", "gold-ink": "#004526",
    "l1": "#00311B", "l2": "#003F23", "l3": "#07432A", "l4": "#206641", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#073E26", "l2f": "#005028", "l3f": "#187C4C", "l4f": "#56BB7F",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#09170E", "shadow": "rgba(5,34,17,.22)", "wash-a": "rgba(0,80,40,.14)",
    "wash-b": "rgba(86,187,127,.10)", "gb2": "#073E26", "gb3": "#005028", "gb4": "#7FD39D", "brand-grad": "linear-gradient(90deg,#003F23,#005028 55%,#7FD39D)",
    "gold-grad": "linear-gradient(135deg,#7FD39D 0%,#005028 45%,#003F23 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#080C0A", "panel": "#0F1611", "panel-2": "#131C17", "ink": "#F2F7F3", "ink-2": "#D0DDD4",
    "muted": "#97A9A0", "faint": "#718078", "line": "#1D2621", "line-2": "#27302B", "focus": "#48CD7E",
    "accent": "#39B76F", "link": "#7FD39D", "gold": "#39B76F", "gold-deep": "#48CD7E", "gold-ink": "#7FD39D",
    "l1": "#7FD39D", "l2": "#5AC986", "l3": "#6CD7A5", "l4": "#9EDFB6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#073E26", "l2f": "#005028", "l3f": "#187C4C", "l4f": "#56BB7F",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050805", "wash-a": "rgba(0,80,40,.12)", "wash-b": "rgba(86,187,127,.06)",
    "gb2": "#073E26", "gb3": "#005028", "gb4": "#7FD39D", "gold-grad": "linear-gradient(135deg,#B9EFCC 0%,#39B76F 45%,#005028 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
