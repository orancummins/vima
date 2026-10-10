// -------------------------------------------------------------------
// features/operatingSystem.js
// The "Operating System" tab: the animated Mastercard Operating System
// layer picture (served at /mcos/, see mcos/__init__.py) in an iframe,
// plus the links between it and the rest of Solution Studio.
//
// The frame is created the first time the tab opens and kept afterwards, so
// the opening animation plays once and the picture keeps its state.
//
// Messages (same origin only; the bridge inside the frame is
// mcos/web/mcos-bridge.js):
//   frame → shell  {type:'mcos:ready'}
//                  {type:'mcos:state', state, host}   what the picture shows
//                  {type:'vima:navigate', tab, api|bundle|uc}
//                  {type:'vima:shortcut', key}        ⌘K / Ctrl+K inside the frame
//   shell → frame  {type:'mcos:goto', target}
//                  {type:'mcos:visibility', visible}
//                  {type:'vima:theme', theme}         (core/theme.js)
//
// A target is the picture's own hash: '' (the stack), 'open', 'U', 'L1'…'L5',
// 't-<area>', 'p-<product>' or 'o-<outcome>'.
// -------------------------------------------------------------------
import { $ } from '../core/dom.js';
import { _appPath } from '../core/net.js';
import { _currentThemeMode, _postThemeToEmbeddedFrame } from '../core/theme.js';
import { _isNonUsBlockedApiId, _isNonUsBlockedUseCaseById } from '../core/region.js';

const TARGETS = window.__MCOS_TARGETS__ || {};
const FRAME_ID = 'os-frame';

let _frame = null;
let _ready = false;
let _visible = false;
let _pending = null; // target to show once the frame is listening

/** Where a Studio API / bundle / use case sits in the picture, or ''. */
export function osTargetFor(kind, id) {
  return (id && TARGETS[kind] && TARGETS[kind][id]) || '';
}

function _post(msg) {
  if (!_frame || !_frame.contentWindow) return;
  try { _frame.contentWindow.postMessage(msg, window.location.origin); } catch (_) {}
}

function _ensureFrame() {
  if (_frame) return;
  const host = $('os-frame-host');
  if (!host) return;
  _frame = document.createElement('iframe');
  _frame.id = FRAME_ID;
  _frame.className = 'os-frame';
  // aria-label rather than title: Chrome shows an iframe's title as a
  // tooltip wherever the pointer rests inside it.
  _frame.setAttribute('aria-label', 'Mastercard Operating System');
  // The bridge reads the hash on start, so a pending target rides along here.
  _frame.src = _appPath('/mcos/index.html') + (_pending ? '#' + encodeURIComponent(_pending) : '');
  _pending = null;
  _frame.addEventListener('load', () => {
    host.classList.add('os-frame-host--loaded');
    _postThemeToEmbeddedFrame(_frame, _currentThemeMode());
  });
  host.appendChild(_frame);
}

/** Called by core/nav.js when the Operating System tab is shown. */
export function showOs() {
  _visible = true;
  _ensureFrame();
  if (_ready) _post({ type: 'mcos:visibility', visible: true });
}

/** Called by core/nav.js when any other tab is shown. */
export function hideOs() {
  if (!_visible) return;
  _visible = false;
  _post({ type: 'mcos:visibility', visible: false });
}

/** Show a target in the picture (the tab must already be, or be about to be, shown). */
export function gotoOs(target) {
  const t = target || '';
  if (_ready) _post({ type: 'mcos:goto', target: t });
  else _pending = t;
}

/** Switch to the Operating System tab and show a target in it. */
export function openOs(target) {
  // Set first so a frame created by the tab switch starts on the target
  // instead of playing the opening animation.
  if (!_ready) _pending = target || '';
  const tabBtn = document.querySelector('.top-tab[data-top-tab="os"]');
  if (tabBtn && !tabBtn.classList.contains('active')) tabBtn.click();
  else showOs();
  if (_ready) gotoOs(target);
}

function _navigateStudio(msg) {
  const sel = (attr, id) => `[${attr}="${window.CSS && CSS.escape ? CSS.escape(id) : id}"]`;
  let tab = '';
  let item = '';
  if (msg.tab === 'apis' && msg.api) {
    if (_isNonUsBlockedApiId(msg.api)) return;
    tab = 'apis'; item = sel('data-api-id', msg.api);
  } else if (msg.tab === 'bundles' && msg.bundle) {
    tab = 'bundles'; item = sel('data-bundle-id', msg.bundle);
  } else if (msg.tab === 'usecases' && msg.uc) {
    if (_isNonUsBlockedUseCaseById(msg.uc)) return;
    tab = 'usecases'; item = sel('data-uc-id', msg.uc);
  } else {
    return;
  }
  // Same click-the-tab-then-the-item pattern as the bundle and API pages,
  // so the URL and Back/Forward stay in step.
  const tabBtn = document.querySelector(`.top-tab[data-top-tab="${tab}"]`);
  if (tabBtn) tabBtn.click();
  setTimeout(() => {
    const btn = document.querySelector(item);
    if (btn) btn.click();
  }, 0);
}

function _onMessage(e) {
  if (e.origin !== window.location.origin) return;
  if (!_frame || e.source !== _frame.contentWindow) return;
  const msg = e.data || {};
  switch (msg.type) {
    case 'mcos:ready':
      _ready = true;
      _postThemeToEmbeddedFrame(_frame, _currentThemeMode());
      _post({ type: 'mcos:visibility', visible: _visible });
      if (_pending !== null) {
        _post({ type: 'mcos:goto', target: _pending });
        _pending = null;
      }
      break;
    case 'mcos:state':
      if (!_visible) return;
      document.dispatchEvent(new CustomEvent('vima:nav-state', {
        detail: { tab: 'os', os: msg.state || null, replace: !!msg.host },
      }));
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

export function initOperatingSystem() {
  window.addEventListener('message', _onMessage);

  // "See it in the Operating System" links anywhere in the shell.
  document.addEventListener('click', (e) => {
    const link = e.target.closest('[data-os-target]');
    if (!link || link.disabled) return;
    e.preventDefault();
    openOs(link.dataset.osTarget || '');
  });
  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Enter' && e.key !== ' ') return;
    const link = e.target.closest && e.target.closest('[data-os-target][role="button"]');
    if (!link) return;
    e.preventDefault();
    openOs(link.dataset.osTarget || '');
  });

  // Back / Forward (core/history.js) asks for a picture state.
  document.addEventListener('vima:os-goto', (e) => gotoOs((e.detail && e.detail.target) || ''));
}
