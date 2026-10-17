// -------------------------------------------------------------------
// features/customers.js
// The Customers tab: a list of customers (templates/index.html, from
// customers/), and each customer's business read as a platform, on the
// same layer picture as the Platform tab. A customer's page is served at
// /customers/<id>/ (customers/__init__.py) and runs the same bridge
// (mcos/web/mcos-bridge.js), so it speaks the same messages as the
// Platform frame (see features/operatingSystem.js):
//   frame → shell  {type:'mcos:ready'}  {type:'mcos:state', state, host}
//                  {type:'vima:navigate', tab, api|bundle|uc}  {type:'vima:shortcut', key}
//   shell → frame  {type:'mcos:goto', target}  {type:'mcos:visibility', visible}
//                  {type:'mcos:glide', phase:'reveal'}  {type:'vima:theme', theme}
//
// Each customer's frame is created the first time it opens and kept, so
// its opening animation plays once and it keeps its place.
//
// The URL carries ?tab=customers&customer=<id>&os=<target> (core/history.js);
// this module reports changes with 'vima:nav-state' and is told where to go
// with 'vima:customer-goto'.
// -------------------------------------------------------------------
import { $ } from '../core/dom.js';
import { _appPath } from '../core/net.js';
import { _currentThemeMode, _postThemeToEmbeddedFrame } from '../core/theme.js';
import { _navigateStudio } from './operatingSystem.js';

const CUSTOMERS = window.__CUSTOMERS__ || [];
const byId = Object.fromEntries(CUSTOMERS.map((c) => [c.id, c]));

const _frames = {};      // id -> { el, ready, pending, loaded, state }
let _visible = false;    // the tab is showing
let _current = null;     // customer on screen, or null for the list
let _request = null;     // { id, target } asked for before the tab shows

export function customerById(id) {
  return byId[id] || null;
}

function _post(f, msg) {
  if (!f || !f.el.contentWindow) return;
  try { f.el.contentWindow.postMessage(msg, window.location.origin); } catch (_) {}
}

function _report(patch, replace) {
  document.dispatchEvent(new CustomEvent('vima:nav-state', {
    detail: Object.assign({ tab: 'customers', customer: _current, os: null, cf: _cfString() || null, replace: !!replace }, patch),
  }));
}

function _frame(id, target) {
  if (_frames[id]) return _frames[id];
  const host = $('cust-frame-host');
  const c = byId[id];
  const el = document.createElement('iframe');
  el.className = 'os-frame cust-frame';
  el.dataset.customer = id;
  el.setAttribute('aria-label', `${c.name}, read as a platform`);
  // The bridge reads the hash on start, so a first target rides along.
  el.src = _appPath(`/customers/${encodeURIComponent(id)}/`) + (target ? '#' + encodeURIComponent(target) : '');
  const f = { el, ready: false, pending: null, loaded: false, state: target || '' };
  el.addEventListener('load', () => {
    f.loaded = true;
    if (_current === id) host.classList.add('os-frame-host--loaded');
    _postThemeToEmbeddedFrame(el, _currentThemeMode());
  });
  host.appendChild(el);
  _frames[id] = f;
  return f;
}

function _showList() {
  $('cust-index').classList.remove('hidden');
  $('cust-view').classList.add('hidden');
  _setActiveFrame(null);
}

function _setActiveFrame(id) {
  for (const [fid, f] of Object.entries(_frames)) {
    const on = fid === id && _visible;
    f.el.classList.toggle('cust-frame--active', fid === id);
    if (f.ready) {
      _post(f, { type: 'mcos:visibility', visible: on });
      if (on) _post(f, { type: 'mcos:glide', phase: 'reveal' });
    }
  }
}

function _showCustomer(id, target) {
  const c = byId[id];
  if (!c) { _current = null; _showList(); return; }
  _current = id;
  $('cust-index').classList.add('hidden');
  $('cust-view').classList.remove('hidden');
  $('cust-bar-logos').replaceChildren(...(c.logos || []).map((lg) => {
    const img = document.createElement('img');
    img.className = 'cust-bar-logo';
    img.src = _appPath(lg.url);
    img.alt = '';
    img.style.setProperty('--chip', lg.bg);
    return img;
  }));
  $('cust-bar-name').textContent = c.name;
  $('cust-bar-meta').textContent = [(c.brands || []).join(' · '), c.country, `as at ${c.as_of}`].filter(Boolean).join(' · ');
  $('cust-bar-standalone').href = _appPath(`/customers/${encodeURIComponent(id)}/${c.page}`);

  const existed = !!_frames[id];
  const f = _frame(id, target);
  $('cust-frame-host').classList.toggle('os-frame-host--loaded', f.loaded);
  _setActiveFrame(id);
  if (existed && target !== undefined && target !== null) {
    if (f.ready) _post(f, { type: 'mcos:goto', target });
    else f.pending = target;
  }
}

/** Called by core/nav.js when the Customers tab is shown. */
export function showCustomers() {
  _visible = true;
  if (_request) {
    const r = _request;
    _request = null;
    if (r.id) _showCustomer(r.id, r.target);
    else { _current = null; _showList(); }
  } else if (_current) {
    // Back on the tab: the customer it was showing, where it was.
    // After the tab click has recorded the bare tab, which this replaces.
    _showCustomer(_current);
    const id = _current;
    setTimeout(() => { if (_visible && _current === id) _report({ customer: id, os: _frames[id].state || null }, true); }, 0);
  } else {
    _showList();
    // The tab click recorded the bare tab; put the list's filters back in the URL.
    if (_cfString()) setTimeout(() => { if (_visible && !_current) _report({ customer: null, os: null }, true); }, 0);
  }
}

/** Called by core/nav.js when any other tab is shown. */
export function hideCustomers() {
  if (!_visible) return;
  _visible = false;
  _setActiveFrame(_current);
}

/** Switch to the Customers tab and open a customer, optionally at a place in its picture. */
export function openCustomer(id, target) {
  if (!byId[id]) return;
  const tabBtn = document.querySelector('.top-tab[data-top-tab="customers"]');
  const switching = tabBtn && !tabBtn.classList.contains('active');
  _request = { id, target: target || '' };
  if (switching) tabBtn.click();   // the tab click records the bare tab ...
  else showCustomers();
  _report({ customer: id, os: target || null }, switching);   // ... which this replaces
}

// -------------------------------------------------------------------
// Finding a customer in the list: search, facets (kind, region, sub-region,
// Mastercard depth), sort, grouping and density. The cards are rendered by
// the template; this shows, hides, orders and groups them. The state is one
// string carried in the URL as ?cf= (core/history.js), e.g.
//   ?tab=customers&cf=t%3Dbank%26r%3Deu%26sort%3Dmc
// -------------------------------------------------------------------
const MACRO_ORDER = ['na', 'lac', 'eu', 'mea', 'ap'];
const MC_ORDER = ['deep', 'mixed', 'light'];
const MC_LABEL = { deep: 'Deep', mixed: 'Partial', light: 'Light', none: 'Not mapped' };
const TYPE_ORDER = ['bank', 'digital', 'issuer', 'payments', 'wallet', 'merchant', 'tech'];
// Short chip labels, so each facet fits on one line at laptop width.
const TYPE_SHORT = { bank: 'Banks', digital: 'Digital banks', issuer: 'Card issuers', payments: 'Payments',
  wallet: 'Wallets & fintech', merchant: 'Merchants', tech: 'Big tech' };
const MACRO_SHORT = { na: 'North America', lac: 'Latin America', eu: 'Europe', mea: 'Middle East & Africa', ap: 'Asia-Pacific' };

const _f = { q: '', t: '', r: '', s: '', m: '', sort: 'featured', group: '', view: 'logos' };
const _DEFAULTS = Object.assign({}, _f);

const _fold = (s) => (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
const _haystack = Object.fromEntries(CUSTOMERS.map((c) => [c.id, _fold([
  c.name, c.short, (c.brands || []).join(' '), c.country, c.geo && c.geo.subregion, c.geo && c.geo.macro_label,
  c.type_label, c.tagline,
].join(' '))]));

const _val = {
  t: (c) => c.type || 'bank',
  r: (c) => (c.geo && c.geo.macro) || '',
  s: (c) => (c.geo && c.geo.subregion) || '',
  m: (c) => (c.mc && c.mc.level) || 'none',
};

function _cfString() {
  const p = new URLSearchParams();
  for (const k of Object.keys(_DEFAULTS)) if (_f[k] && _f[k] !== _DEFAULTS[k]) p.set(k, _f[k]);
  return p.toString();
}

function _cfLoad(str) {
  Object.assign(_f, _DEFAULTS);
  const p = new URLSearchParams(str || '');
  for (const k of Object.keys(_DEFAULTS)) if (p.get(k)) _f[k] = p.get(k);
  if (_f.s && !_f.r) _f.s = '';
}

function _matches(c, except) {
  if (except !== 'q' && _f.q) {
    const words = _fold(_f.q).split(/\s+/).filter(Boolean);
    if (!words.every((w) => _haystack[c.id].includes(w))) return false;
  }
  for (const k of ['t', 'r', 's', 'm']) {
    if (k !== except && _f[k] && _val[k](c) !== _f[k]) return false;
  }
  return true;
}

function _facetOptions(k) {
  // Every value present, in a stable order, with how many customers match the other filters.
  const counts = {};
  const labels = {};
  for (const c of CUSTOMERS) {
    if (k === 's' && _val.r(c) !== _f.r) continue;
    const v = _val[k](c);
    labels[v] = k === 't' ? (TYPE_SHORT[v] || c.type_label) : k === 'r' ? (MACRO_SHORT[v] || c.geo.macro_label)
      : k === 's' ? v : MC_LABEL[v];
    counts[v] = (counts[v] || 0) + (_matches(c, k) ? 1 : 0);
  }
  const order = k === 't' ? TYPE_ORDER : k === 'r' ? MACRO_ORDER : k === 'm' ? [...MC_ORDER, 'none'] : null;
  const keys = Object.keys(labels).sort((a, b) => (order
    ? order.indexOf(a) - order.indexOf(b)
    : labels[a].localeCompare(labels[b])));
  return keys.map((v) => ({ v, label: labels[v], n: counts[v] }));
}

function _chip(k, v, label, n, on) {
  const b = document.createElement('button');
  b.type = 'button';
  b.className = 'cust-chip' + (on ? ' cust-chip--on' : '') + (k === 'm' && v ? ` cust-chip--mc cust-mc--${v}` : '');
  b.dataset.facet = k;
  b.dataset.value = v;
  b.setAttribute('aria-pressed', on ? 'true' : 'false');
  b.disabled = !on && n === 0;
  b.innerHTML = '';
  b.append(label);
  if (n !== null) {
    const s = document.createElement('span');
    s.className = 'cust-chip-n';
    s.textContent = n;
    b.append(s);
  }
  return b;
}

function _renderFacets() {
  for (const k of ['t', 'r', 's', 'm']) {
    const row = document.querySelector(`.cust-facet[data-facet="${k}"]`);
    if (!row) continue;
    if (k === 's') row.classList.toggle('hidden', !_f.r);
    if (k === 's' && !_f.r) continue;
    const opts = _facetOptions(k);
    const all = CUSTOMERS.filter((c) => _matches(c, k) && (k !== 's' || _val.r(c) === _f.r)).length;
    row.querySelector('.cust-chips').replaceChildren(
      _chip(k, '', 'All', all, !_f[k]),
      ...opts.map((o) => _chip(k, o.v, o.label, o.n, _f[k] === o.v)),
    );
  }
}

function _sortKey(c) {
  switch (_f.sort) {
    case 'name': return [_fold(c.name)];
    case 'country': return [_fold(c.geo.hq), _fold(c.name)];
    case 'mc': return [-(c.mc ? c.mc.share : -1), _fold(c.name)];
    case 'products': return [-(c.counts.products || 0), _fold(c.name)];
    default: return [c.order || 0, _fold(c.name)];
  }
}

function _groupOf(c) {
  switch (_f.group) {
    case 'macro': return [MACRO_ORDER.indexOf(_val.r(c)), c.geo.macro_label];
    case 'sub': return [MACRO_ORDER.indexOf(_val.r(c)) * 100, `${c.geo.macro_label} · ${c.geo.subregion}`];
    case 'type': return [TYPE_ORDER.indexOf(_val.t(c)), c.type_label];
    case 'mc': return [[...MC_ORDER, 'none'].indexOf(_val.m(c)), `Mastercard depth: ${MC_LABEL[_val.m(c)].toLowerCase()}`];
    default: return [0, ''];
  }
}

function _cmp(a, b) {
  for (let i = 0; i < Math.max(a.length, b.length); i++) {
    if (a[i] < b[i]) return -1;
    if (a[i] > b[i]) return 1;
  }
  return 0;
}

function _applyFilters() {
  const grid = $('cust-grid');
  if (!grid) return;
  const cards = Object.fromEntries([...grid.querySelectorAll('.cust-card[data-cust]')].map((el) => [el.dataset.cust, el]));
  const shown = CUSTOMERS.filter((c) => _matches(c));
  const list = shown.slice().sort((a, b) => {
    const ga = _groupOf(a); const gb = _groupOf(b);
    return _cmp([ga[0], ga[1]], [gb[0], gb[1]]) || _cmp(_sortKey(a), _sortKey(b));
  });
  const kids = [];
  let group = null;
  for (const c of list) {
    const g = _groupOf(c)[1];
    if (_f.group && g !== group) {
      group = g;
      const h = document.createElement('h2');
      h.className = 'cust-group';
      h.textContent = g;
      const n = document.createElement('span');
      n.className = 'cust-group-n';
      n.textContent = list.filter((x) => _groupOf(x)[1] === g).length;
      h.append(n);
      kids.push(h);
    }
    kids.push(cards[c.id]);
  }
  for (const c of CUSTOMERS) if (cards[c.id] && !shown.includes(c)) { cards[c.id].hidden = true; kids.push(cards[c.id]); }
  for (const c of shown) if (cards[c.id]) cards[c.id].hidden = false;
  grid.replaceChildren(...kids);
  grid.classList.toggle('cust-grid--list', _f.view === 'list');
  grid.classList.toggle('hidden', _f.view === 'logos');
  _renderWall(shown);
  const groupCtl = $('cust-group') && $('cust-group').closest('.cust-ctl');
  if (groupCtl) groupCtl.classList.toggle('cust-ctl--off', _f.view === 'logos');   // the wall is always by region

  _renderFacets();
  const q = $('cust-q');
  if (q && q.value !== _f.q) q.value = _f.q;
  if ($('cust-sort')) $('cust-sort').value = _f.sort;
  if ($('cust-group')) $('cust-group').value = _f.group;
  document.querySelectorAll('[data-cust-view]').forEach((b) => b.setAttribute('aria-pressed', b.dataset.custView === _f.view ? 'true' : 'false'));
  const filtered = !!(_f.q || _f.t || _f.r || _f.s || _f.m);
  const count = $('cust-count');
  count.replaceChildren();
  if (filtered) {
    const b = document.createElement('b');
    b.textContent = shown.length;
    count.append(b, ` of ${CUSTOMERS.length}`);
  }
  _renderTokens();
  $('cust-clear').classList.toggle('hidden', !filtered);
  $('cust-empty').classList.toggle('hidden', shown.length > 0);
}

// The logo wall: every shown customer's logo, under its region and then its sub-region, in the chosen sort.
function _wallTile(c) {
  const b = document.createElement('button');
  b.type = 'button';
  b.className = 'cust-tile';
  b.dataset.customerOpen = c.id;
  b.title = [c.name, c.type_label, c.country, c.mc ? c.mc.label : ''].filter(Boolean).join(' · ');
  if (c.accent) b.style.setProperty('--cust', c.accent);
  const chip = document.createElement('span');
  chip.className = 'cust-tile-logo';
  const lg = (c.logos || [])[0];
  if (lg) {
    chip.style.setProperty('--chip', lg.bg || '#fff');
    const img = document.createElement('img');
    img.src = _appPath(lg.url);
    img.alt = lg.alt || c.name;
    img.loading = 'lazy';
    img.decoding = 'async';
    chip.append(img);
  } else {
    chip.classList.add('cust-tile-logo--mark');
    chip.textContent = c.short || c.name;
  }
  const name = document.createElement('span');
  name.className = 'cust-tile-name';
  name.textContent = c.name.length <= 20 ? c.name : (c.short || c.name);   // short names can be bare tickers (CFG, JPMC)
  const meta = document.createElement('span');
  meta.className = 'cust-tile-meta';
  meta.textContent = c.geo.hq || c.country;
  if (c.mc) {
    const dot = document.createElement('span');
    dot.className = `cust-tile-mc cust-mc--${c.mc.level}`;
    dot.title = c.mc.label;
    meta.prepend(dot);
  }
  b.append(chip, name, meta);
  return b;
}

function _renderWall(shown) {
  const wall = $('cust-wall');
  if (!wall) return;
  wall.classList.toggle('hidden', _f.view !== 'logos');
  if (_f.view !== 'logos') return;
  const regions = [];
  for (const m of MACRO_ORDER) {
    const inRegion = shown.filter((c) => _val.r(c) === m).sort((a, b) => _cmp(_sortKey(a), _sortKey(b)));
    if (!inRegion.length) continue;
    const sec = document.createElement('section');
    sec.className = 'cust-region';
    const h = document.createElement('h2');
    h.className = 'cust-region-head';
    const t = document.createElement('span');
    t.textContent = inRegion[0].geo.macro_label;
    const n = document.createElement('span');
    n.className = 'cust-region-n';
    n.textContent = inRegion.length;
    h.append(t, n);
    sec.append(h);
    const subs = [...new Set(inRegion.map((c) => c.geo.subregion))];
    for (const sub of subs) {
      const row = document.createElement('div');
      row.className = 'cust-subregion';
      const label = document.createElement('div');
      label.className = 'cust-subregion-label';
      const members = inRegion.filter((c) => c.geo.subregion === sub);
      label.append(sub);
      const k = document.createElement('span');
      k.textContent = members.length;
      label.append(k);
      const tiles = document.createElement('div');
      tiles.className = 'cust-tiles';
      tiles.append(...members.map(_wallTile));
      row.append(label, tiles);
      sec.append(row);
    }
    regions.push(sec);
  }
  wall.replaceChildren(...regions);
}

// One removable token per active filter, under the facets (and the only trace of them once the panel folds).
function _tokenLabel(k) {
  const c = CUSTOMERS.find((x) => _val[k](x) === _f[k]);
  if (k === 't') return TYPE_SHORT[_f.t] || (c ? c.type_label : _f.t);
  if (k === 'r') return MACRO_SHORT[_f.r] || (c ? c.geo.macro_label : _f.r);
  if (k === 's') return _f.s;
  return `Mastercard: ${(MC_LABEL[_f.m] || _f.m).toLowerCase()}`;
}

function _renderTokens() {
  const host = $('cust-tokens');
  if (!host) return;
  const toks = [];
  if (_f.q) toks.push(['q', `“${_f.q}”`]);
  for (const k of ['t', 'r', 's', 'm']) if (_f[k]) toks.push([k, _tokenLabel(k)]);
  host.replaceChildren(...toks.map(([k, label]) => {
    const t = document.createElement('button');
    t.type = 'button';
    t.className = 'cust-token';
    t.dataset.clear = k;
    t.title = 'Remove this filter';
    t.append(label);
    const x = document.createElement('span');
    x.className = 'cust-token-x';
    x.setAttribute('aria-hidden', 'true');
    x.textContent = '×';
    t.append(x);
    return t;
  }));
  const n = toks.filter(([k]) => k !== 'q').length;
  const badge = $('cust-filters-n');
  if (badge) { badge.textContent = n || ''; badge.classList.toggle('hidden', !n); }
}

// The facets sit under the compact row and open with "Filters".
function _initToggle() {
  const toggle = $('cust-filters-toggle');
  const facets = $('cust-facets');
  if (!toggle || !facets) return;
  toggle.addEventListener('click', () => {
    const open = facets.hidden;
    facets.hidden = !open;
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    $('cust-tools').classList.toggle('cust-tools--open', open);
  });
}

let _qTimer = null;
function _setFilter(patch, { replace = false } = {}) {
  Object.assign(_f, patch);
  if ('r' in patch && !patch.s) _f.s = '';
  _applyFilters();
  if (_visible && !_current) _report({ customer: null, os: null }, replace);
}

function _initFilters() {
  if (!$('cust-tools')) return;
  document.addEventListener('click', (e) => {
    const chip = e.target.closest('.cust-chip');
    if (chip) {
      const k = chip.dataset.facet;
      const v = chip.dataset.value;
      _setFilter({ [k]: _f[k] === v ? '' : v });
      return;
    }
    const view = e.target.closest('[data-cust-view]');
    if (view) { _setFilter({ view: view.dataset.custView }, { replace: true }); return; }
    const tok = e.target.closest('.cust-token');
    if (tok) { _setFilter(tok.dataset.clear === 'r' ? { r: '', s: '' } : { [tok.dataset.clear]: '' }); return; }
    if (e.target.closest('#cust-clear, [data-cust-clear]')) _setFilter({ q: '', t: '', r: '', s: '', m: '' });
  });
  $('cust-q').addEventListener('input', (e) => {
    _f.q = e.target.value;
    _applyFilters();
    clearTimeout(_qTimer);   // one history entry per pause, not per keystroke
    _qTimer = setTimeout(() => { if (_visible && !_current) _report({ customer: null, os: null }, true); }, 400);
  });
  $('cust-q').addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && _f.q) { e.stopPropagation(); _setFilter({ q: '' }, { replace: true }); }
    if (e.key === 'Enter') {
      const first = CUSTOMERS.find((c) => _matches(c));
      const shown = CUSTOMERS.filter((c) => _matches(c));
      if (shown.length === 1 && first) openCustomer(first.id);
    }
  });
  // "/" jumps to the search box from anywhere on the list (not while typing elsewhere).
  document.addEventListener('keydown', (e) => {
    if (e.key !== '/' || e.metaKey || e.ctrlKey || e.altKey || !_visible || _current) return;
    const t = e.target;
    if (t && (t.isContentEditable || /^(input|textarea|select)$/i.test(t.tagName))) return;
    e.preventDefault();
    $('cust-q').focus();
    $('cust-q').select();
  });
  _initToggle();
  $('cust-sort').addEventListener('change', (e) => _setFilter({ sort: e.target.value }, { replace: true }));
  if ($('cust-group')) $('cust-group').addEventListener('change', (e) => _setFilter({ group: e.target.value }, { replace: true }));
  _applyFilters();
}

function _onMessage(e) {
  if (e.origin !== window.location.origin) return;
  const id = Object.keys(_frames).find((k) => _frames[k].el.contentWindow === e.source);
  if (!id) return;
  const f = _frames[id];
  const msg = e.data || {};
  switch (msg.type) {
    case 'mcos:ready': {
      f.ready = true;
      _postThemeToEmbeddedFrame(f.el, _currentThemeMode());
      const on = _visible && _current === id;
      _post(f, { type: 'mcos:visibility', visible: on });
      if (on) _post(f, { type: 'mcos:glide', phase: 'reveal' });
      if (f.pending !== null) {
        _post(f, { type: 'mcos:goto', target: f.pending });
        f.pending = null;
      }
      break;
    }
    case 'mcos:state':
      f.state = msg.state || '';
      if (!_visible || _current !== id) return;
      _report({ customer: id, os: msg.state || null }, !!msg.host);
      break;
    case 'vima:navigate':
      _navigateStudio(msg);
      break;
    case 'vima:shortcut':
      if (msg.key === 'k') {
        document.dispatchEvent(new KeyboardEvent('keydown', { key: 'k', metaKey: true, ctrlKey: true, bubbles: true }));
      }
      break;
    default:
      break;
  }
}

export function initCustomers() {
  if (!$('panel-customers')) return;
  window.addEventListener('message', _onMessage);

  document.addEventListener('click', (e) => {
    const open = e.target.closest('[data-customer-open]');
    if (open) {
      e.preventDefault();
      openCustomer(open.dataset.customerOpen);
      return;
    }
    if (e.target.closest('#cust-back')) {
      e.preventDefault();
      _current = null;
      _showList();
      _report({ customer: null, os: null });
    }
  });

  // Back / Forward and deep links (core/history.js), before the tab is clicked.
  document.addEventListener('vima:customer-goto', (e) => {
    const d = e.detail || {};
    _request = { id: d.customer || null, target: d.target || '' };
    _cfLoad(d.cf || '');
    _applyFilters();
  });

  _initFilters();
}
