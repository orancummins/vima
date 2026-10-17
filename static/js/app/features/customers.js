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
    detail: Object.assign({ tab: 'customers', customer: _current, os: null, replace: !!replace }, patch),
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
  });
}
