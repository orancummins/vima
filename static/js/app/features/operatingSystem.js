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
//                  {type:'mcos:globe', atGlobe, rect}  where its globe is (for the glide)
//                  {type:'vima:navigate', tab, api|bundle|uc}
//                  {type:'vima:shortcut', key}        ⌘K / Ctrl+K inside the frame
//   shell → frame  {type:'mcos:goto', target}
//                  {type:'mcos:visibility', visible}
//                  {type:'mcos:globe-rect'}            where is your globe?
//                  {type:'mcos:glide', phase, rot}     'hold' hides its globe, 'reveal' shows it at rot
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

function _ensureFrame(glide) {
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
  _frame.src = _appPath('/mcos/index.html') + (glide ? '?glide=1' : '') +
    (_pending ? '#' + encodeURIComponent(_pending) : '');
  _pending = null;
  _frame.addEventListener('load', () => {
    host.classList.add('os-frame-host--loaded');
    _postThemeToEmbeddedFrame(_frame, _currentThemeMode());
  });
  host.appendChild(_frame);
}

/** Called by core/nav.js when the Operating System tab is shown. `fromHome`
 *  is the Home globe's place (captureHomeGlobe) when coming from Home. */
export function showOs(fromHome) {
  _visible = true;
  _ensureFrame(!!fromHome);
  if (_ready) _post({ type: 'mcos:visibility', visible: true });
  if (fromHome) _startGlide(fromHome);
}

/** Called by core/nav.js when any other tab is shown. */
export function hideOs() {
  if (!_visible) return;
  _visible = false;
  _endGlide(true);
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

// ---------- the Home globe glides into the picture ----------
// The picture's opening globe is drawn exactly like the Home globe
// (mcos/web/mcos-bridge.js), so switching Home → Operating System moves one
// globe rather than swapping two: a copy of the Home canvas glides and
// scales onto the picture's globe, which then appears at the same rotation.
const HOME_OUTLINE = 0.32 * 0.668;   // the Home globe's outline radius, as a share of its canvas width
let _glide = null;

/** Called by core/nav.js before it hides Home: where the Home globe is now, or null. */
export function captureHomeGlobe() {
  const panel = $('panel-home');
  const canvas = $('home-globe');
  if (!panel || panel.classList.contains('hidden') || !canvas) return null;
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return null;
  const r = canvas.getBoundingClientRect();
  if (!r.width) return null;
  return { canvas, left: r.left, top: r.top, w: r.width, h: r.height,
    cx: r.left + r.width / 2, cy: r.top + r.height / 2, r: r.width * HOME_OUTLINE };
}

function _startGlide(from) {
  _endGlide(true);
  const ov = document.createElement('canvas');
  ov.className = 'os-glide';
  ov.width = from.canvas.width;
  ov.height = from.canvas.height;
  Object.assign(ov.style, { left: from.left + 'px', top: from.top + 'px', width: from.w + 'px', height: from.h + 'px' });
  document.body.appendChild(ov);
  const ctx = ov.getContext('2d');
  // The Home globe keeps turning while hidden; copy it every frame.
  const g = { ov, from, raf: 0, timer: 0, moved: false };
  const copy = () => {
    ctx.clearRect(0, 0, ov.width, ov.height);
    ctx.drawImage(from.canvas, 0, 0);
    g.raf = requestAnimationFrame(copy);
  };
  copy();
  g.timer = setTimeout(() => _endGlide(), 2500);   // the picture never answered: just fade out
  _glide = g;
  if (_ready) {
    _post({ type: 'mcos:glide', phase: 'hold' });
    _post({ type: 'mcos:globe-rect' });
  }
}

function _moveGlide(msg) {
  const g = _glide;
  if (!g || g.moved) return;
  if (!msg.atGlobe || !msg.rect || !_frame) { _endGlide(); return; }
  const fr = _frame.getBoundingClientRect();
  const to = { cx: fr.left + msg.rect.cx, cy: fr.top + msg.rect.cy, r: msg.rect.r };
  g.moved = true;
  g.ov.style.transition = 'transform 0.9s cubic-bezier(.45,.05,.25,1)';
  g.ov.style.transform = `translate(${to.cx - g.from.cx}px, ${to.cy - g.from.cy}px) scale(${to.r / g.from.r})`;
  g.ov.addEventListener('transitionend', () => _endGlide(), { once: true });
}

function _endGlide(instant) {
  const g = _glide;
  if (!g) return;
  _glide = null;
  clearTimeout(g.timer);
  const rot = typeof window.__homeGlobeRot === 'function' ? window.__homeGlobeRot() : undefined;
  _post({ type: 'mcos:glide', phase: 'reveal', rot });
  const remove = () => { cancelAnimationFrame(g.raf); g.ov.remove(); };
  if (instant) { remove(); return; }
  g.ov.style.transition = 'opacity 0.3s ease';
  g.ov.style.opacity = '0';
  setTimeout(remove, 320);
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
      if (_glide) {
        _post({ type: 'mcos:glide', phase: 'hold' });
        _post({ type: 'mcos:globe-rect' });
      }
      break;
    case 'mcos:globe':
      _moveGlide(msg);
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
