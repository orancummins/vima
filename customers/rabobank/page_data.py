"""Rabobank, as a platform: the data behind ``Rabobank_Platform.html``.

``python customers/build_page.py rabobank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Rabobank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from rabobank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from rabobank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Rabobank'
PAGE = 'Rabobank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Rabobank Platform"
KICKER = f"Coöperatieve Rabobank U.A. · as at {AS_OF}"
H1 = '<h1>Rabobank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Rabobank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Rabobank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Rabobank's colours"

PIN = (52.09, 5.12, 'Utrecht')
PIN_FACING = 'Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'drb': 'Domestic Retail Banking', 'wr': 'Wholesale & Rural', 'lease': 'Leasing (DLL)', 'bpd': 'Property Development', 'grp': 'Group'}
DIV = {'group': 'Rabobank Group', 'nl': 'Rabobank Netherlands', 'wr': 'Rabobank Wholesale & Rural', 'dll': 'DLL', 'obvion': 'Obvion', 'freo': 'Freo & Alfam', 'bpd': 'BPD', 'invest': 'Rabo Investments'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F3F6", "panel-2": "#E5E8EF", "ink": "#0B0D1C", "ink-2": "#202435",
    "muted": "#545569", "faint": "#747585", "line": "#CDCDDA", "line-2": "#B2B3C3", "focus": "#0008A8",
    "accent": "#0008A8", "link": "#01007A", "gold": "#0008A8", "gold-deep": "#010066", "gold-ink": "#01007A",
    "l1": "#000044", "l2": "#010066", "l3": "#120E88", "l4": "#333BA0", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0F0D6E", "l2f": "#0008A8", "l3f": "#2327BA", "l4f": "#7985C9",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0B0D1C", "shadow": "rgba(7,11,44,.22)", "wash-a": "rgba(0,8,168,.14)",
    "wash-b": "rgba(121,133,201,.10)", "gb2": "#0F0D6E", "gb3": "#0008A8", "gb4": "#99A5DC", "brand-grad": "linear-gradient(90deg,#010066,#0008A8 55%,#99A5DC)",
    "gold-grad": "linear-gradient(135deg,#99A5DC 0%,#0008A8 45%,#010066 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090A0E", "panel": "#12141B", "panel-2": "#1B1D27", "ink": "#F2F4F7", "ink-2": "#D6DAE2",
    "muted": "#ACADBB", "faint": "#8D8E9B", "line": "#323341", "line-2": "#4E4E60", "focus": "#6D7CD7",
    "accent": "#6874D0", "link": "#99A5DC", "gold": "#6874D0", "gold-deep": "#6D7CD7", "gold-ink": "#99A5DC",
    "l1": "#99A5DC", "l2": "#7C89D4", "l3": "#8A8CDF", "l4": "#B0B9E5", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0F0D6E", "l2f": "#0008A8", "l3f": "#2327BA", "l4f": "#7985C9",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050608", "wash-a": "rgba(0,8,168,.12)", "wash-b": "rgba(121,133,201,.06)",
    "gb2": "#0F0D6E", "gb3": "#0008A8", "gb4": "#99A5DC", "gold-grad": "linear-gradient(135deg,#C2CCF1 0%,#5C69CC 45%,#0008A8 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
