/* Solution Studio bridge for the Mastercard Operating System layer picture.

   Runs after the vendored picture's own scripts (mcos/vendor/), whose
   top-level functions and state are visible from here: openTile,
   openProduct, detailHtml, renderSide, setFocus, pickOut, st, MAP and so on.
   The vendored file is never edited; this script wraps a few of those
   functions to add Solution Studio's links, and drives the rest.

   It talks to the shell (static/js/app/features/operatingSystem.js) with
   same-origin postMessage:
     in   {type:'mcos:goto', target}  {type:'mcos:visibility', visible}
     out  {type:'mcos:ready'}  {type:'mcos:state', state, host}
          {type:'vima:navigate', tab, api|bundle|uc}  {type:'vima:shortcut', key}

   A target is the picture's hash: '' (the stack), 'open', 'U', 'L1'…'L5',
   't-<area>', 'p-<product>' or 'o-<outcome>'. */
/* The vendored picture's top-level names (checked by tools/sync_mcos.py). */
/* global MAP, st, OUTCOMES, LAYERS, TILE, PADS, sraf:writable, st0:writable, reduce, f, esc,
   spin, renderSide, renderPick, openTile, openProduct, closeDrawer, drawerOpen, setFocus, pickOut,
   clearPick, openStack, closeStack, endIntro, DOTS, phi, OX, GR, GY, DEG */
(function () {
  "use strict";
  if (typeof MAP === "undefined" || typeof st === "undefined" || typeof openProduct !== "function") return;

  var ORIGIN = window.location.origin;
  var parentWin = window.parent !== window ? window.parent : null;
  var LINKS = { products: {}, outcomes: {} };
  var drawerTarget = "";
  var lastState = null;
  var hostChange = false;
  var timer = 0;

  function send(msg) {
    if (!parentWin) return;
    try { parentWin.postMessage(msg, ORIGIN); } catch (e) {}
  }
  function h(s) { return esc(s == null ? "" : s); }

  /* ---------- what Solution Studio has for a product ---------- */
  function studioFor(pid) { return LINKS.products[pid] || null; }
  function isLive(pid) {
    var s = studioFor(pid);
    return !!(s && (s.apis.length || s.use_cases.length));
  }
  function liveInTile(tileId) {
    var T = MAP.TILES[tileId];
    if (!T || !T.products) return 0;
    return T.products.filter(function (p) { return p.st !== "retired" && isLive(p.id); }).length;
  }

  var ICON_STUDIO = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7"/><path d="M8 7h9v9"/></svg>';

  function linkButton(kind, item) {
    var tab = kind === "api" ? "apis" : kind === "bundle" ? "bundles" : "usecases";
    var label = kind === "api" ? "API" : kind === "bundle" ? "Bundle" : "Use case";
    var dot = kind === "api" ? '<span class="mcos-dot' + (item.configured ? " ok" : "") + '" title="' + (item.configured ? "Keys configured" : "No keys yet — the simulator can answer") + '"></span>' : "";
    var blocked = !!item.blocked;
    var title = blocked ? item.title : "Open " + item.name + " in Solution Studio";
    return '<button type="button" class="mcos-link mcos-link--' + kind + '" data-studio-tab="' + tab + '" data-studio-id="' + h(item.id) + '" title="' + h(title) + '"' + (blocked ? " disabled" : "") + ">" +
      dot + '<span class="mcos-link-name">' + h(item.name) + '</span><span class="mcos-link-kind">' + label + "</span>" + ICON_STUDIO + "</button>";
  }

  function studioSection(pid) {
    var s = studioFor(pid);
    if (!s) return null;
    var html = s.apis.map(function (a) { return linkButton("api", a); }).join("") +
      s.use_cases.map(function (u) { return linkButton("usecase", u); }).join("") +
      s.bundles.map(function (b) { return linkButton("bundle", b); }).join("");
    if (!html) return null;
    var sec = document.createElement("div");
    sec.className = "dsec mcos-studio";
    sec.innerHTML = '<div class="dl">Try it in Solution Studio</div><div class="mcos-links">' + html + "</div>";
    return sec;
  }

  /* ---------- wrap the picture's own functions ---------- */
  var _detailHtml = window.detailHtml;
  window.detailHtml = function (p, solo) {
    var d = _detailHtml(p, solo);
    var sec = p && studioSection(p.id);
    if (sec) {
      var main = d.querySelector(".dmain");
      var sources = main && Array.prototype.find.call(main.querySelectorAll(":scope > .dsec"), function (x) { return x.querySelector(".links"); });
      if (sources) main.insertBefore(sec, sources); else if (main) main.appendChild(sec);
    }
    return d;
  };

  var _tagHtml = window.tagHtml;
  window.tagHtml = function (p) {
    var out = _tagHtml(p);
    if (p && isLive(p.id)) out += '<span class="badge studio">Live in Studio</span>';
    return out;
  };

  var _openTile = window.openTile;
  window.openTile = function (T) {
    _openTile(T);
    if (!T) return;
    drawerTarget = "t-" + T.id;
    var n = liveInTile(T.id), stats = document.getElementById("dstats");
    if (n && stats) stats.insertAdjacentHTML("beforeend", '<span class="stat stat--studio"><b>' + n + "</b>live in Solution Studio</span>");
    schedule();
  };

  var _openProduct = window.openProduct;
  window.openProduct = function (p) {
    _openProduct(p);
    if (!p) return;
    drawerTarget = "p-" + p.id;
    schedule();
  };

  var _renderSide = window.renderSide;
  window.renderSide = function () {
    _renderSide();
    var side = document.getElementById("side");
    if (!side) return;
    side.querySelectorAll(".tile[data-t]").forEach(function (b) {
      var n = liveInTile(b.dataset.t);
      if (n) b.insertAdjacentHTML("beforeend", '<span class="mcos-tile-studio">' + n + " live in Solution Studio</span>");
    });
    var o = !st.focus && st.out && OUTCOMES.find(function (x) { return x.id === st.out; });
    if (!o) return;
    side.querySelectorAll(".step[data-p]").forEach(function (li) {
      if (!isLive(li.dataset.p)) return;
      li.classList.add("mcos-live");
      var sm = li.querySelector(".sm");
      if (sm) sm.insertAdjacentHTML("beforeend", '<span class="mcos-step-tag">Live in Studio</span>');
    });
    var oc = LINKS.outcomes[o.id];
    if (oc && oc.bundles.length) {
      side.insertAdjacentHTML("beforeend", '<div class="mcos-cta"><div class="mcos-cta-eyebrow">Put it into practice</div><p class="mcos-cta-text">Solution Studio has these APIs wired up and ready to call, grouped as a bundle.</p><div class="mcos-links">' +
        oc.bundles.map(function (b) { return linkButton("bundle", b); }).join("") + "</div></div>");
    }
  };

  /* An orange marker on the rim of every pad with something to try in
     Studio: white-edged, so it reads on all five layer colours. PADS holds
     each pad's top centre in the same coordinates as the pad itself. */
  var SVGNS = "http://www.w3.org/2000/svg";
  function markPads() {
    var svg = document.getElementById("svg");
    if (!svg) return;
    svg.querySelectorAll(".blk[data-t]").forEach(function (b) {
      var n = liveInTile(b.dataset.t), at = PADS[b.dataset.t];
      b.classList.toggle("studio", n > 0);
      var pip = b.querySelector(".mcos-pip"), title = b.querySelector("title.mcos-title");
      if (!n || !at) {
        if (pip) pip.remove();
        if (title) title.remove();
        return;
      }
      if (!pip) {
        pip = document.createElementNS(SVGNS, "circle");
        pip.setAttribute("class", "mcos-pip");
        pip.setAttribute("r", "4.4");
        b.appendChild(pip);
      }
      pip.setAttribute("cx", f(at.x + 18.5));
      pip.setAttribute("cy", f(at.y - 9.5));
      if (!title) {
        title = document.createElementNS(SVGNS, "title");
        title.setAttribute("class", "mcos-title");
        b.insertBefore(title, b.firstChild);
      }
      title.textContent = n + " live in Solution Studio";
    });
  }
  /* Solution Studio's look for the picture itself. The picture paints its
     discs and its opening globe with gradients built in build(), coloured
     straight from the layer tokens. Point each stop at the --mc-* tokens in
     mcos-theme.css instead: the discs become dark glass plates tinted by
     their layer (frosted white in light mode), and the globe becomes the
     Home tab's wireframe globe, a faint glow rather than a solid sphere.
     The values are CSS variables, so the light/dark toggle applies without
     a rebuild. */
  function mix(k, tint, base) {
    return "color-mix(in oklab, var(--l" + k + "f) var(" + tint + "), var(" + base + "))";
  }
  var STOPS = { ug: ["var(--mc-utok-hi)", "var(--mc-utok)"] };
  for (var k = 1; k <= 5; k++) {
    STOPS["st" + k] = [mix(k, "--mc-top-tint", "--mc-plate"), mix(k, "--mc-top-tint-lo", "--mc-plate-deep")];
    STOPS["gs" + k] = [mix(k, "--mc-side-tint-lo", "--mc-plate-deep"), mix(k, "--mc-side-tint", "--mc-plate"),
      mix(k, "--mc-side-tint-lo", "--mc-plate"), mix(k, "--mc-side-tint-lo", "--mc-plate-deep")];
    STOPS["bt" + k] = [mix(k, "--mc-pad-tint", "--mc-pad"), mix(k, "--mc-pad-tint-lo", "--mc-pad")];
    STOPS["gc" + k] = [mix(k, "--mc-pad-tint-lo", "--mc-pad"), mix(k, "--mc-side-tint-lo", "--mc-plate-deep")];
  }
  // The opening globe: [colour, opacity] per stop.
  var GLOBE = {
    gg: [["var(--mc-globe-a)"], ["var(--mc-globe-a)"], ["var(--mc-globe-b)"], ["var(--mc-globe-c)"], ["var(--mc-globe-d)"]],
    gt: [["var(--mc-cut-a)"], ["var(--mc-cut-b)"]],
    ghl: [["var(--mc-globe-hl)", ".22"], ["var(--mc-globe-hl)", ".05"], ["var(--mc-globe-hl)", "0"]],
    grl: [["var(--mc-globe-rim)", "0"], ["var(--mc-globe-rim)", ".3"], ["var(--mc-globe-rim)", ".6"]],
    // The halo's first stop also fills the sphere, which is now see-through:
    // keep it as faint as the Home globe's inner glow.
    gha: [["var(--mc-halo)", ".12"], ["var(--mc-halo)", ".1"], ["var(--mc-halo)", ".04"], ["var(--mc-halo)", "0"]],
  };
  function restyleDefs() {
    var svg = document.getElementById("svg");
    if (!svg) return;
    Object.keys(STOPS).forEach(function (id) {
      var g = svg.querySelector("#" + id);
      if (!g) return;
      g.querySelectorAll("stop").forEach(function (stop, i) {
        if (STOPS[id][i]) stop.style.setProperty("stop-color", STOPS[id][i]);
      });
    });
    Object.keys(GLOBE).forEach(function (id) {
      var g = svg.querySelector("#" + id);
      if (!g) return;
      g.querySelectorAll("stop").forEach(function (stop, i) {
        var v = GLOBE[id][i];
        if (!v) return;
        stop.style.setProperty("stop-color", v[0]);
        if (v[1] !== undefined) stop.setAttribute("stop-opacity", v[1]);
      });
    });
  }

  /* The globe's continents, drawn as in the picture but with smaller dots,
     nearer the Home globe's fine dot sphere. Replaces the picture's
     drawGlobe(), which spin() calls by name every frame. */
  var DOT_SCALE = 0.58;
  window.drawGlobe = function () {
    var land = document.getElementById("gland"), mer = document.getElementById("gmer"), lat = document.getElementById("glat");
    if (!land) return;
    var d = "";
    for (var i = 0; i < DOTS.length; i++) {
      var q = DOTS[i], a = q[2] + phi, z = q[0] * Math.cos(a);
      if (z < .14) continue;
      var x = OX + GR * q[0] * Math.sin(a), y = GY - GR * q[1], r = GR * .0285 * DOT_SCALE * (.16 + .84 * z);
      d += "M" + f(x - r) + "," + f(y) + "a" + f(r) + "," + f(r) + " 0 1,0 " + f(2 * r) + ",0a" + f(r) + "," + f(r) + " 0 1,0 " + f(-2 * r) + ",0";
    }
    land.setAttribute("d", d);
    var m = "";
    for (var k = 0; k < 12; k++) {
      var ang = k * 30 * DEG + phi, c = Math.cos(ang), sn = Math.sin(ang);
      if (c <= .02) continue;
      m += "M" + OX + "," + (GY - GR) + "A" + f(Math.max(.01, GR * Math.abs(sn))) + "," + GR + " 0 0 " + (sn > 0 ? 1 : 0) + " " + OX + "," + (GY + GR);
    }
    mer.setAttribute("d", m);
    if (!lat.getAttribute("d")) {
      var n = LAYERS.length, h = 2 * GR / n, l = "";
      for (var j = 1; j < n; j++) {
        var yy = GY + GR - j * h, rr = Math.sqrt(GR * GR - (yy - GY) * (yy - GY));
        l += "M" + f(OX - rr) + "," + f(yy) + "H" + f(OX + rr);
      }
      lat.setAttribute("d", l);
    }
  };

  var _layout = window.layout;
  window.layout = function () { _layout(); restyleDefs(); markPads(); };

  /* ---------- where the picture is, for the shell's URL ---------- */
  function current() {
    if (drawerOpen() && drawerTarget) return drawerTarget;
    if (st.p < 1) return "";
    if (st.out) return "o-" + st.out;
    if (st.focus) return st.focus;
    if (st.open) return "open";
    return "";
  }
  function report() {
    timer = 0;
    var s = current();
    var host = hostChange;
    hostChange = false;
    if (s === lastState) return;
    lastState = s;
    send({ type: "mcos:state", state: s, host: host });
  }
  function schedule() { if (!timer) timer = setTimeout(report, 40); }
  document.addEventListener("click", schedule, true);
  document.addEventListener("keydown", schedule, true);

  /* ---------- go to a target ---------- */
  function clearPicks() {
    if (st.who || st.out || st.menu) { st.who = null; st.out = null; st.menu = null; renderPick(); }
  }
  function focusLayerOf(tile) {
    var own = tile && TILE[tile.id];
    var id = own ? own.L.id : null;
    clearPicks();
    if (id && st.focus !== id) setFocus(id); else if (!st.open) openStack();
  }
  function go(target) {
    var t = String(target || "");
    try { t = decodeURIComponent(t); } catch (e) {}
    hostChange = true;
    var m;
    if ((m = /^p-(.+)$/.exec(t)) && MAP.PRODUCTS[m[1]]) {
      var p = MAP.PRODUCTS[m[1]];
      endIntro(); focusLayerOf(p.tile); openProduct(p);
    } else if ((m = /^t-(.+)$/.exec(t)) && MAP.TILES[m[1]]) {
      var T = MAP.TILES[m[1]];
      endIntro(); focusLayerOf(T); openTile(T);
    } else if ((m = /^o-(.+)$/.exec(t)) && OUTCOMES.some(function (o) { return o.id === m[1]; })) {
      closeDrawer(); pickOut(m[1]);
    } else if (t === "U" || LAYERS.some(function (l) { return l.id === t; })) {
      closeDrawer(); clearPicks(); setFocus(t);
    } else if (t === "open" || t === "sliced") {
      closeDrawer(); clearPicks();
      if (st.focus) setFocus(null);
      openStack();
    } else {
      closeDrawer();
      if (st.p >= 1) {
        if (st.who || st.out) clearPick();
        else if (st.open || st.focus) closeStack();
      }
    }
    schedule();
  }

  /* ---------- pause while the tab is hidden ---------- */
  function setVisible(v) {
    document.documentElement.classList.toggle("mcos-paused", !v);
    var svg = document.getElementById("svg");
    try { if (svg) { if (v) svg.unpauseAnimations(); else svg.pauseAnimations(); } } catch (e) {}
    if (!v) {
      if (sraf) { cancelAnimationFrame(sraf); sraf = 0; st0 = 0; }
    } else {
      if (st.p < .1 && !sraf && !reduce) sraf = requestAnimationFrame(spin);
      // The shell's URL may have moved on while the tab was hidden.
      lastState = null; hostChange = true; schedule();
    }
  }

  /* ---------- events ---------- */
  window.addEventListener("message", function (e) {
    if (e.origin !== ORIGIN || e.source !== parentWin) return;
    var d = e.data || {};
    if (d.type === "mcos:goto") go(d.target);
    else if (d.type === "mcos:visibility") setVisible(!!d.visible);
  });
  window.addEventListener("hashchange", function () { go(location.hash.slice(1)); });

  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-studio-tab]");
    if (!b || b.disabled) return;
    e.preventDefault();
    var msg = { type: "vima:navigate", tab: b.dataset.studioTab };
    msg[b.dataset.studioTab === "apis" ? "api" : b.dataset.studioTab === "bundles" ? "bundle" : "uc"] = b.dataset.studioId;
    send(msg);
  });
  document.addEventListener("keydown", function (e) {
    if ((e.metaKey || e.ctrlKey) && (e.key === "k" || e.key === "K")) {
      e.preventDefault();
      send({ type: "vima:shortcut", key: "k" });
    }
  });

  /* ---------- start ---------- */
  var head = document.querySelector(".head");
  if (head && !head.querySelector(".mcos-legend")) {
    head.insertAdjacentHTML("beforeend", '<p class="mcos-legend"><span class="mcos-pip-key" aria-hidden="true"></span>Areas with an orange marker have APIs and use cases you can try live in Solution Studio.</p>');
  }

  function start(links) {
    if (links && links.products) LINKS = links;
    restyleDefs();
    if (st.p < .1) window.drawGlobe();
    markPads();
    renderSide();
    var h0 = location.hash.slice(1);
    if (/^[tp]-/.test(h0)) go(h0);
    else { lastState = current(); }
    send({ type: "mcos:ready" });
  }
  fetch("links.json", { credentials: "same-origin" })
    .then(function (r) { return r.ok ? r.json() : null; })
    .catch(function () { return null; })
    .then(start);
})();
