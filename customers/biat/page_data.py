"""Banque Internationale Arabe de Tunisie (BIAT), as a platform: the data behind ``BIAT_Platform.html``.

``python customers/build_page.py biat`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``BIAT_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from biat_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from biat_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BIAT'
PAGE = 'BIAT_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BIAT Platform"
KICKER = f"Banque Internationale Arabe de Tunisie · as at {AS_OF}"
H1 = '<h1>BIAT <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BIAT's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BIAT's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BIAT's colours"

PIN = (36.8, 10.18, 'Tunis')
PIN_FACING = 'Tunisia and North Africa'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail banking (individuals, diaspora, professionals)', 'corp': 'Corporate & institutional banking', 'bfi': 'Financing, investment & markets', 'group': 'Group & central'}
DIV = {'biat': 'BIAT (the bank)', 'retail': 'BIAT retail network', 'cib': 'BIAT corporate & BFI', 'assur': 'Assurances BIAT', 'tv': 'Tunisie Valeurs', 'france': 'BIAT France', 'tech': 'BIAT Innovation & Technology'}
DEFAULT_DIV = 'biat'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F4F5", "panel-2": "#E6EAEC", "ink": "#0E1217", "ink-2": "#21272C",
    "muted": "#4E5258", "faint": "#6F7378", "line": "#CDD0D5", "line-2": "#B1B5BB", "focus": "#204070",
    "accent": "#204070", "link": "#182C54", "gold": "#204070", "gold-deep": "#142647", "gold-ink": "#182C54",
    "l1": "#0E1A31", "l2": "#142647", "l3": "#23365E", "l4": "#445B7A", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#1F2F4E", "l2f": "#204070", "l3f": "#3F5B8B", "l4f": "#839AB2",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0E1217", "shadow": "rgba(14,23,33,.22)", "wash-a": "rgba(32,64,112,.14)",
    "wash-b": "rgba(131,154,178,.10)", "gb2": "#1F2F4E", "gb3": "#204070", "gb4": "#A2B7CA", "brand-grad": "linear-gradient(90deg,#142647,#204070 55%,#A2B7CA)",
    "gold-grad": "linear-gradient(135deg,#A2B7CA 0%,#204070 45%,#142647 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0B0C", "panel": "#131618", "panel-2": "#1B1F22", "ink": "#F3F5F6", "ink-2": "#D7DCDE",
    "muted": "#AAADB2", "faint": "#888C90", "line": "#2F3237", "line-2": "#464A4F", "focus": "#7C9BBB",
    "accent": "#6B8BAE", "link": "#A2B7CA", "gold": "#6B8BAE", "gold-deep": "#7C9BBB", "gold-ink": "#A2B7CA",
    "l1": "#A2B7CA", "l2": "#87A2BC", "l3": "#96A9C9", "l4": "#B7C8D7", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#1F2F4E", "l2f": "#204070", "l3f": "#3F5B8B", "l4f": "#839AB2",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060707", "wash-a": "rgba(32,64,112,.12)", "wash-b": "rgba(131,154,178,.06)",
    "gb2": "#1F2F4E", "gb3": "#204070", "gb4": "#A2B7CA", "gold-grad": "linear-gradient(135deg,#CBDAE5 0%,#6B8BAE 45%,#204070 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
