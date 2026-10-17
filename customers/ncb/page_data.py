"""National Commercial Bank Jamaica, as a platform: the data behind ``National_Commercial_Bank_Jamaica_Platform.html``.

``python customers/build_page.py ncb`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``National_Commercial_Bank_Jamaica_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from ncb_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from ncb_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'NCB'
PAGE = 'National_Commercial_Bank_Jamaica_Platform.html'
AS_OF = "17 October 2026"
TITLE = "NCB Platform"
KICKER = f"National Commercial Bank Jamaica · as at {AS_OF}"
H1 = '<h1>NCB <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: NCB's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in NCB's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in NCB's colours"

PIN = (17.99, -76.79, 'Kingston')
PIN_FACING = 'the Caribbean'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'csme': 'Consumer & SME Banking', 'pay': 'Payment Services', 'ccb': 'Corporate & Commercial Banking', 'tw': 'Treasury, Wealth & Investment Banking', 'ins': 'Insurance & Pensions'}
DIV = {'ncbfg': 'NCB Financial Group', 'ncbj': 'NCB Jamaica', 'lynk': 'Lynk', 'ncbcm': 'NCB Capital Markets', 'guardian': 'Guardian Group', 'clarien': 'Clarien'}
DEFAULT_DIV = 'ncbfg'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E5ECEE", "ink": "#0B151B", "ink-2": "#1F2C32",
    "muted": "#4E5962", "faint": "#6F7880", "line": "#CBD2D8", "line-2": "#B0B8C0", "focus": "#01529A",
    "accent": "#01529A", "link": "#013671", "gold": "#01529A", "gold-deep": "#012D5F", "gold-ink": "#013671",
    "l1": "#001F41", "l2": "#012D5F", "l3": "#0D3F7D", "l4": "#316A97", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0D3766", "l2f": "#01529A", "l3f": "#236AB0", "l4f": "#74A8C7",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0B151B", "shadow": "rgba(7,28,42,.22)", "wash-a": "rgba(1,82,154,.14)",
    "wash-b": "rgba(116,168,199,.10)", "gb2": "#0D3766", "gb3": "#01529A", "gb4": "#95C4DB", "brand-grad": "linear-gradient(90deg,#012D5F,#01529A 55%,#95C4DB)",
    "gold-grad": "linear-gradient(135deg,#95C4DB 0%,#01529A 45%,#012D5F 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090C0D", "panel": "#12181A", "panel-2": "#1A2125", "ink": "#F2F6F7", "ink-2": "#D5DEE1",
    "muted": "#A9B1B8", "faint": "#899097", "line": "#2F363D", "line-2": "#485159", "focus": "#68ABD5",
    "accent": "#569CC9", "link": "#95C4DB", "gold": "#569CC9", "gold-deep": "#68ABD5", "gold-ink": "#95C4DB",
    "l1": "#95C4DB", "l2": "#77B0D2", "l3": "#86B2DD", "l4": "#ADD2E4", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0D3766", "l2f": "#01529A", "l3f": "#236AB0", "l4f": "#74A8C7",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(1,82,154,.12)", "wash-b": "rgba(116,168,199,.06)",
    "gb2": "#0D3766", "gb3": "#01529A", "gb4": "#95C4DB", "gold-grad": "linear-gradient(135deg,#C1E1F0 0%,#569CC9 45%,#01529A 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
