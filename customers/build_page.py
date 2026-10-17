#!/usr/bin/env python3
"""Build a customer's standalone page from SNB's, with that customer's data.

The SNB page (``customers/snb/SNB_Operating_System.html``) is one
self-contained file: the layer-picture engine, its styles, embedded fonts
and SNB's data. Other customers' pages are the same engine with their own
data, palette and wording, so rather than keep more copies of the engine by
hand this script takes SNB's page as the template and swaps in, from
``customers/<id>/page_data.py``:

* the inventory (layers, areas, products and their sources), the journeys,
  the kinds of user and the lens, and the picture's own tile list, generated
  from the same inventory so the two cannot drift;
* the customer's palette (with Mastercard's colours for the lens);
* the lens's wording: SNB's page reads every area through NEO, its digital
  bank; these pages read every area through Mastercard (how deep Mastercard
  goes in it), which is what Solution Studio is for;
* the heading, the globe's pin and a few phrases.

Every swap must match exactly once, so a change to the template fails here
loudly rather than leaving SNB's words in another bank's page.

Usage::

    python customers/build_page.py citi        # writes customers/citi/<PAGE>
    python customers/build_page.py citizens
"""
from __future__ import annotations

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
TEMPLATE = os.path.join(HERE, "snb", "SNB_Operating_System.html")

D = None   # the customer's page_data module, set by load()


def load(cid: str):
    """Import customers/<cid>/page_data.py (and the modules beside it) as D."""
    global D
    folder = os.path.join(HERE, cid)
    if not os.path.isfile(os.path.join(folder, "page_data.py")):
        raise SystemExit(f"customers/{cid}/page_data.py not found")
    sys.path.insert(0, folder)
    import page_data  # noqa: PLC0415
    D = page_data
    return os.path.join(folder, D.PAGE)


def js(v) -> str:
    return json.dumps(v, ensure_ascii=False)


def swap(src: str, old: str, new: str, count: int = 1) -> str:
    n = src.count(old)
    if n != count:
        raise SystemExit(f"template changed: expected {count} of {old[:80]!r}, found {n}")
    return src.replace(old, new)


def swap_block(src: str, start: str, end: str, new: str) -> str:
    """Replace from ``start`` up to (not including) ``end``."""
    i = src.find(start)
    if i < 0 or src.find(start, i + 1) >= 0:
        raise SystemExit(f"template changed: {start[:60]!r} is not there exactly once")
    j = src.index(end, i)
    return src[:i] + new + src[j:]


# ---------------------------------------------------------------------------
# The inventory (inside the MAP IIFE)
# ---------------------------------------------------------------------------

def product_js(p: dict) -> str:
    extra = {k: v for k, v in p.items() if k not in ("id", "n", "d")}
    return f"P({js(p['id'])},{js(p['n'])},{js(p['d'])},{js(extra)})"


def inventory_js() -> str:
    users = ", ".join(f"{k}:{js(label)}" for k, label, _icon in D.USERS)
    out = [
        "const MAP=(function(){",
        "const USERS = {\n  " + users + "\n};",
        f"const LC = {js(D.LC)};",
        f"const ST = {js(D.ST)};",
        f"const OR = {js(D.OR)};",
        f"const REV = {js(D.REV)};",
        f"const DIV = {js(D.DIV)};",
        "",
        'function P(id,n,d,x){ return Object.assign({id,n,d,s:[],lc:"beyond",st:"active",o:"B",src:[]},x||{}); }',
        "",
        "const LAYERS = [",
        ' {id:"U", name:"Users", analogy:"who the bank serves", color:"--lu", users:true,',
        f"  desc:{js(D.USERS_DESC)},",
        "  tiles: Object.keys(USERS).map(k=>({id:\"u-\"+k, name:USERS[k], user:k, products:[]}))},",
    ]
    for L in reversed(D.LAYERS):   # top of the stack first, like the template
        out.append("")
        out.append(f' {{id:{js(L["id"])}, name:{js(L["name"])}, analogy:{js(L["analogy"])}, color:{js(L["color"])},')
        out.append(f"  desc:{js(L['desc'])},")
        out.append("  tiles:[")
        for t in L["tiles"]:
            out.append(f'   {{id:{js(t["id"])}, name:{js(t["name"])}, blurb:{js(t["blurb"])}, '
                       f'div:{js(t["div"])}, rev:{js(t["rev"])}, products:[')
            out.extend("    " + product_js(p) + "," for p in t["products"])
            out.append("   ]},")
        out.append("  ]},")
    out.append("];")
    out.append("")
    out.append("const PILLARS = [")
    for pl in D.PILLARS:
        out.append(f' {{id:{js(pl["id"])}, name:{js(pl["name"])}, color:"--lu", blurb:{js(pl["blurb"])}, products:[')
        out.extend("   " + product_js(p) + "," for p in pl["products"])
        out.append(" ]},")
    out.append("];")
    out.append("")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Journeys, users, the picture's tiles and the lens
# ---------------------------------------------------------------------------

def picture_js() -> str:
    who = {**{k: v for k, v in D.WHO.items()}, "mc": "Mastercard"}
    out = ["/* Who and what: the journeys. A step is the area it lands on, the product, a short label and the part it plays. */",
           f"const WHO = {js(who)};", "const OUTCOMES = ["]
    for o in D.OUTCOMES:
        out.append(f" {{id:{js(o['id'])}, who:{js(o['who'])}, name:{js(o['name'])}, why:{js(o['why'])},")
        out.append("  steps:" + js([{"at": s[0], "p": s[1], "t": s[2]} for s in o["steps"]]) + "},")
    out.append("];")
    out.append("")
    out.append("/* One icon per kind of user, in the same order as USERS. */")
    out.append(f"const UKEYS={js([k for k, _l, _i in D.USERS])}, "
               f"UICON={js({**{k: i for k, _l, i in D.USERS}, 'mc': 'credit-card'})};")
    out.append("const svgi=(name,cls)=>`<svg class=\"${cls}\" viewBox=\"0 0 24 24\" aria-hidden=\"true\">${ICONS[name]}</svg>`;")
    out.append(f"const USERS={js([label for _k, label, _i in D.USERS])};")
    out.append("const LAYERS=[")
    for L in D.LAYERS:
        tiles = []
        for t in L["tiles"]:
            names = [p.get("short", p["n"]) for p in t["products"]]
            tiles.append({"id": t["id"], "ic": t["ic"], "n": t["name"], "b": t["blurb"], "c": len(names), "p": names[:3]})
        dark = ",dark:true" if L.get("dark") else ""
        out.append(f' {{id:{js(L["id"])},name:{js(L["name"])},an:{js(L["analogy"])},kind:{js(L["kind"])}{dark},')
        out.append(f"  desc:{js(L['desc'])},")
        out.append("  tiles:[\n" + ",\n".join("   " + js(t) for t in tiles) + "]},")
    out.append("];")
    out.append("LAYERS.forEach((L,i)=>{L.i=i;L.k=i+1;L.total=L.tiles.reduce((n,t)=>n+t.c,0);});")
    out.append("")
    out.append("/* ---------- the Mastercard lens ----------")
    out.append(f"   Source: this project's {D.SHORT} research, as at {D.AS_OF}. One depth per layer and per area.")
    out.append("   d is Mastercard's depth: 3 Mastercard's own product or network runs it, 2 the whole capability rides on")
    out.append(f"   Mastercard, 1 partly (beside Visa, Amex or {D.SHORT}'s own rails), 0 not Mastercard, null nothing public.")
    out.append("   A Mastercard entry is [name, what it is, status, note, 1 if taken from background knowledge and not source-checked]. */")
    out.append(f"const VS={js(D.LENS)};")
    out.append("")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Palette
# ---------------------------------------------------------------------------

def set_vars(block: str, values: dict) -> str:
    for k, v in values.items():
        block, n = re.subn(rf"(--{re.escape(k)}:)[^;]+;", lambda m, v=v: m.group(1) + v + ";", block, count=1)
        if not n:
            raise SystemExit(f"template changed: --{k} not in a palette block")
    return block


def palette(src: str) -> str:
    start = src.index(":root{\n  --ground:")
    end = src.index("*{box-sizing:border-box}", start)
    css = src[start:end]
    light_end = css.index("@media (prefers-color-scheme: dark)")
    light, rest = css[:light_end], css[light_end:]
    light = set_vars(light, D.PALETTE_LIGHT)
    rest = set_vars(rest, D.PALETTE_DARK)                     # inside @media
    second = rest.index(':root[data-theme="dark"]')
    rest = rest[:second] + set_vars(rest[second:], D.PALETTE_DARK)
    css = light + rest
    return src[:start] + css + src[end:]


# ---------------------------------------------------------------------------
# Wording
# ---------------------------------------------------------------------------

LENS_SWAPS = [
    ("Palette: SNB's greens for the bank, from the deep foundation to the bright access layer, graphite for the people, and\n"
     "   NEO's own colour kept for the lens that reads the stack through the digital bank.",
     "{palette_note}"),
    # comments that name SNB or NEO
    ("/* ---------- the NEO lens: the switch, the list and the dialog block ---------- */",
     "/* ---------- the Mastercard lens: the switch, the list and the dialog block ---------- */"),
    ("/* ================= the NEO lens =================\n"
     "   One switch re-reads the stack through NEO. The NEO colour fills an area's column to its depth: full for NEO-native,\n"
     "   lighter for shared or partial, grey for SNB-only, a dashed outline where nothing public says either way. */",
     "/* ================= the Mastercard lens =================\n"
     "   One switch re-reads the stack through Mastercard. Mastercard's colour fills an area's column to its depth: full where\n"
     "   Mastercard runs it, lighter for shared or partial, grey where it is not Mastercard, a dashed outline where nothing public says. */"),
    ("/* ---------- the NEO lens ----------\n"
     "   One switch re-reads the same stack through NEO, SNB's digital bank. Every capability area carries a depth:\n"
     "   3 NEO-native (built in or for NEO), 2 in NEO on SNB's shared engine, 1 partly there, 0 not in NEO, null nothing public to go on.",
     "/* ---------- the Mastercard lens ----------\n"
     "   One switch re-reads the same stack through Mastercard. Every capability area carries a depth:\n"
     "   3 Mastercard-run, 2 on Mastercard, 1 partly Mastercard, 0 not Mastercard, null nothing public to go on."),
    ("/* the five slices: foundation (deep emerald), rails (SNB green), services (teal), lines (sea green), access (bright mint); graphite for the people */",
     "/* {slices_note} */"),
    ("/* the globe: SNB's deep, mid and bright greens */", "/* {globe_note} */"),
    ("/* NEO: the lens colour */", "/* the lens colour: Mastercard */"),
    ("/* Product inventory: Saudi National Bank as at 16 October 2026, with NEO marked wherever it reaches.",
     "/* Product inventory: {bank} as at {as_of}, with Mastercard marked wherever it reaches."),
    # the key above the picture
    ('<span class="vk n3"><b>NEO</b>NEO-native</span>', '<span class="vk n3"><b>MC</b>Mastercard-run</span>'),
    ('<span class="vk n2"><b>Yes</b>In NEO</span>', '<span class="vk n2"><b>Yes</b>On Mastercard</span>'),
    ('<span class="vk n1"><b>Part</b>Partly in NEO</span>', '<span class="vk n1"><b>Part</b>Partly Mastercard</span>'),
    ('<span class="vk n0"><b>—</b>SNB only</span>', '<span class="vk n0"><b>—</b>Not Mastercard</span>'),
    ("The height of a column is NEO's depth in that area: built in or for NEO, offered in NEO on SNB's shared engine, only partly there, or not there at all.",
     "The height of a column is Mastercard's depth in that area: run on Mastercard's own products or network, riding wholly on Mastercard, partly (beside Visa, Amex or {bank}'s own rails), or not at all."),
    ('<span class="neo" aria-hidden="true"></span>NEO lens', '<span class="neo" aria-hidden="true"></span>Mastercard lens'),
    # the lens's scale
    ('VMAG=["SNB only, or nowhere yet","part of it, or only through the SNB app","the whole capability, on SNB\'s shared engine","built in or for NEO"]',
     'VMAG=["{bank}\'s own, or another network\'s","part of it, beside Visa, Amex or {bank}\'s own rails","the whole capability rides on Mastercard","Mastercard\'s own product or network runs it"]'),
    ('const vshort=d=>d==null?"?":d===3?"NEO":d===2?"Yes":d===1?"Part":"—";',
     'const vshort=d=>d==null?"?":d===3?"MC":d===2?"Yes":d===1?"Part":"—";'),
    ('const vlong=d=>d==null?"Can\'t tell":d===3?"NEO-native":d===2?"In NEO":d===1?"Partly in NEO":"Not in NEO";',
     'const vlong=d=>d==null?"Can\'t tell":d===3?"Mastercard-run":d===2?"On Mastercard":d===1?"Partly Mastercard":"Not Mastercard";'),
    # the side panel and dialogs
    ("Each capability area is a column as tall as NEO's depth in it, in NEO's green;",
     "Each capability area is a column as tall as Mastercard's depth in it, in Mastercard's orange;"),
    ("one for each layer of Saudi National Bank as an operating system", "one for each layer of {bank} as a platform"),
    ("The grouping is this map's own, not an SNB product bundle.", "The grouping is this map's own, not a {bank} product bundle."),
    ("Most products serve several of them; NEO was built for the first three.", "Most products serve several of them."),
    ('const SUBV="The same five slices, read through NEO. A tall column is an area NEO runs itself; a short one is an area NEO only reaches through the SNB app; a flat one is SNB only. Click a disc for its areas, or an area for what NEO and SNB each put there.";',
     'const SUBV="The same five slices, read through Mastercard. A tall column is an area Mastercard\'s own products or network run; a short one is an area Mastercard shares with Visa, Amex or {bank}\'s own rails; a flat one has no Mastercard in it. Click a disc for its areas, or an area for what Mastercard and {bank} each put there.";'),
    ("none.forEach(x=>out.push(`<span>${esc(x[0])}: not in NEO</span>`));",
     "none.forEach(x=>out.push(`<span>${esc(x[0])}: not Mastercard</span>`));"),
    ("are NEO-native, ${n.n2} are in NEO, ${n.n1} are partly in NEO, ${n.n0} are not in NEO",
     "are Mastercard-run, ${n.n2} are on Mastercard, ${n.n1} are partly Mastercard, ${n.n0} are not Mastercard"),
    ('<span class="n3"><b>${n.n3}</b>NEO-native</span><span class="n2"><b>${n.n2}</b>in NEO</span>',
     '<span class="n3"><b>${n.n3}</b>Mastercard-run</span><span class="n2"><b>${n.n2}</b>on Mastercard</span>'),
    ('<span class="n0"><b>${n.n0}</b>SNB only</span>', '<span class="n0"><b>${n.n0}</b>not Mastercard</span>'),
    ('<h2 class="vsec">NEO at a glance</h2>', '<h2 class="vsec">Mastercard at {bank}, at a glance</h2>'),
    ('<h2 class="vsec">Two front doors, one bank</h2><div class="vsides"><div style="--k:var(--neof)"><b>NEO</b>',
     '<h2 class="vsec">Mastercard, and everything else</h2><div class="vsides"><div style="--k:var(--neof)"><b>Mastercard</b>'),
    ('<div style="--k:var(--l5f)"><b>SNB</b>${esc(VS.sides.snb.dir)}', '<div style="--k:var(--l5f)"><b>{bank} &amp; others</b>${esc(VS.sides.snb.dir)}'),
    ('<div class="vsides"><div style="--k:var(--neof)"><b>NEO</b>${esc(v.neo)}</div><div style="--k:var(--l5f)"><b>SNB</b>${esc(v.snb)}</div></div>',
     '<div class="vsides"><div style="--k:var(--neof)"><b>Mastercard</b>${esc(v.neo)}</div><div style="--k:var(--l5f)"><b>{bank} &amp; others</b>${esc(v.snb)}</div></div>'),
    ("Open what NEO and SNB each put here", "Open what Mastercard and {bank} each put here"),
    ('<span class="vl neo"><b>NEO</b>${vnames(x.v,3)}</span><span class="vl"><b>SNB</b>',
     '<span class="vl neo"><b>Mastercard</b>${vnames(x.v,3)}</span><span class="vl"><b>{bank}</b>'),
    ('"0":["unconf","Not in NEO"]};', '"0":["unconf","Not Mastercard"]};'),
    ("/* Opens an area's dialog in the lens: the depth, then what NEO puts here, ahead of SNB's own products. */",
     "/* Opens an area's dialog in the lens: the depth, then what Mastercard puts here, ahead of {bank}'s own products. */"),
    ('<h4 class="vh" style="--k:var(--neof)">NEO · ${real.length} ${real.length===1?"feature":"features"} here</h4>',
     '<h4 class="vh" style="--k:var(--neof)">Mastercard · ${real.length} ${real.length===1?"piece":"pieces"} here</h4>'),
    ('<div class="fact"><div class="dl">In NEO</div>', '<div class="fact"><div class="dl">Mastercard</div>'),
    ('const mh=el("h4","vh",`SNB · ${live.length}', 'const mh=el("h4","vh",`{bank} · ${live.length}'),
]


def fill(text: str) -> str:
    return (text.replace("{as_of}", D.AS_OF).replace("{bank}", D.SHORT).replace("{palette_note}", D.PALETTE_NOTE)
            .replace("{slices_note}", D.SLICES_NOTE).replace("{globe_note}", D.GLOBE_NOTE))


def heading(src: str) -> str:
    src = swap(src, "<title>Saudi National Bank OS</title>", f"<title>{D.TITLE}</title>")
    src = swap(src, '<div class="kicker">Saudi National Bank · as at 16 October 2026</div>',
               f'<div class="kicker">{D.KICKER}</div>')
    src = swap(src, '<h1>SNB <span class="os">Operating System</span></h1>', D.H1)
    src = re.sub(r'<p class="sub">The Kingdom\'s largest bank.*?</p>', lambda _m: f'<p class="sub">{D.SUB}</p>', src, count=1, flags=re.S)
    src = swap(src, '<button id="md-ma" aria-pressed="true">SNB</button>', f'<button id="md-ma" aria-pressed="true">{D.SHORT}</button>')
    return src


def globe(src: str) -> str:
    lat, lon, city = D.PIN
    src = swap(src, "phi=-(46.7+22)*DEG, st0=0; /* opens with Arabia facing front */",
               f"phi=-({lon}+22)*DEG, st0=0; /* opens with {D.PIN_FACING} facing front */")
    src = swap(src, 'const PIN=[24.71,46.68,"Riyadh"];', f"const PIN=[{lat},{lon},{js(city)}];")
    return src


def build() -> str:
    with open(TEMPLATE, encoding="utf-8") as f:
        src = f.read()
    src = palette(src)
    src = heading(src)
    src = globe(src)
    for old, new in LENS_SWAPS:
        src = swap(src, old, fill(new))
    # The lens's columns are painted from a fixed table of NEO greens, and its chips are inked in NEO's dark green.
    src = swap(src, '[["n3","#D9FFF0","#38E8A0","#19C98A","#0B6B47"],["n2","#F0FFF8","#8CF0C6","#5FD9A8","#2E8C64"],["n1","#F7FFFB","#C4F3DF","#A9E6CC","#5F9C80"]',
               '[["n3","#FFF1E0","#FF8A3D","#FF5F00","#B23A00"],["n2","#FFF6EC","#FFB070","#FF8A3D","#C2410C"],["n1","#FFFAF4","#FFD9B3","#FFC08A","#B8754A"]')
    src = swap(src, "#06201A", "#1F0A00", count=src.count("#06201A") or 1)
    src = swap_block(src, "const MAP=(function(){", "const APIS = [];", inventory_js())
    src = swap_block(src, "/* Who and what: the journeys.", "/* ---------- isometric geometry ---------- */", picture_js())
    # The Users layer says "who the bank serves"; a customer that is not a bank can say otherwise.
    serves = getattr(D, "SERVES", None)
    if serves:
        src = swap(src, "who the bank serves", serves, count=src.count("who the bank serves") or 1)
    # Products default to the bank's own division; SNB's code says "snb".
    src = swap(src, 'if(!p.div) p.div=T.div||"snb";', f'if(!p.div) p.div=T.div||{js(D.DEFAULT_DIV)};')
    leftovers = sorted(set(re.findall(r"[^\n]{0,40}\b(?:NEO|SNB|Saudi|Riyadh|NEONS|AlAhli)\b[^\n]{0,40}", src)))
    leftovers = [x for x in leftovers if not any(ok in x for ok in D.ALLOWED_MENTIONS)]
    if leftovers:
        raise SystemExit(f"SNB wording left in {D.SHORT}'s page:\n  " + "\n  ".join(leftovers[:20]))
    return src


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python customers/build_page.py <customer id>")
    out = load(sys.argv[1])
    page = build()
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"✓ {os.path.relpath(out, ROOT)} ({len(page) // 1024} KB)")
