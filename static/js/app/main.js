import {
  APIS, USE_CASES, RUNTIME_MODE, SERVER_MODE, NON_US_MODE,
  OPEN_FINANCE_US_API_ID, SERVER_MODE_TOOLTIP, NON_US_TOOLTIP,
  THEME_STORAGE_KEY, SCRIPT_ROOT, ROOT_EL,
} from './core/env.js';
import { $ } from './core/dom.js';
import { _appPath, _nativeFetch } from './core/net.js';
import { escapeHtml } from './core/html.js';
import {
  _currentThemeMode, _postThemeToEmbeddedFrame, _syncEmbeddedUseCaseTheme,
  _applyThemeMode, _toggleThemeMode, initTheme,
} from './core/theme.js';
import {
  apiCallsOpen, apiCallsClose, apiCallsToggle, apiCallsClear,
  _startPolling, _stopPolling,
} from './features/apiCallLog.js';
import { startUsIpStatusPolling, refreshUsIpStatus } from './features/usIpStatus.js';
import {
  initApisSnippets, apisSnippetsClose, apisSnippetsToggle,
  apisSnippetsIsVisible, apisSnippetsFollowApi, apisSnippetsRefreshOp,
} from './features/apiSnippets.js';
import { _isNonUsBlockedApiId, _isNonUsBlockedUseCaseById } from './core/region.js';
import { loadUseCases, getBundlesCache, getUseCasesCache } from './core/catalog.js';
import {
  getCurrentApiId, setCurrentApiId, getCurrentOpId, setCurrentOpId,
  getCurrentState, setCurrentState, currentApi, currentOp,
  ioCache, lastOpByApi,
} from './core/state.js';
import {
  _resetLaunchBanner, _showLaunchBannerPending,
  _showLaunchBanner, _buildTestCredentialsBlock,
} from './workbench/launchBanner.js';
import {
  HTTP_REASONS, setStatus, _findFirstUrl, _findKey,
  fmt, fmtWithoutHeaders, renderIoPanel, updateHeaderToggleBtn,
  headersVisible, lastIoData, initHeaderToggles,
} from './workbench/io.js';
import { setSimUI, fetchSimStatus, initSimToggle } from './workbench/simToggle.js';
import { showOfinSetupModal, initOfinSetupModal } from './features/ofinSetupModal.js';
import './features/bundles.js';
import './features/autoProvision.js';
import './features/infoModal.js';

(() => {
  initTheme();

  function _markRuntimeBlockedMenuItems() {
    if (!NON_US_MODE) return;
    document.querySelectorAll('[data-api-id]').forEach((btn) => {
      if (_isNonUsBlockedApiId(btn.dataset.apiId)) {
        btn.classList.add('api-item--disabled');
        btn.setAttribute('aria-disabled', 'true');
        btn.setAttribute('title', NON_US_TOOLTIP);
      }
    });
    document.querySelectorAll('[data-uc-id]').forEach((btn) => {
      if (_isNonUsBlockedUseCaseById(btn.dataset.ucId)) {
        btn.classList.add('api-item--disabled');
        btn.setAttribute('aria-disabled', 'true');
        btn.setAttribute('title', NON_US_TOOLTIP);
      }
    });
  }

  _markRuntimeBlockedMenuItems();

  // Current use-case id (tracked here; API Calls Logger lives in
  // features/apiCallLog.js).
  let _currentUcId = null;

  function updateUcSidebar(uc) {
    const container = $('uc-sidebar-apis');
    const list = $('uc-sidebar-apis-list');
    if (!container || !list) return;
    const ucApis = (uc && uc.apis) || [];
    if (!ucApis.length) { container.classList.add('hidden'); return; }
    list.innerHTML = ucApis.map(apiId => {
      const apiManifest = APIS.find(a => a.id === apiId);
      const configured = apiManifest ? apiManifest.configured : false;
      const name = apiManifest ? apiManifest.name : apiId;
      const known = !!apiManifest;
      const title = known ? `Open ${name} in APIs tab` : `${apiId} (not registered)`;
      return `<button type="button" class="uc-sidebar-api-badge ${configured ? 'configured' : 'unconfigured'}${known ? '' : ' disabled'}" data-uc-api-link="${escapeHtml(apiId)}" title="${escapeHtml(title)}"${known ? '' : ' disabled'}><span class="uc-sidebar-api-dot"></span>${escapeHtml(name)}</button>`;
    }).join('');
    // Wire click → switch to APIs tab and select the API.
    list.querySelectorAll('[data-uc-api-link]').forEach(btn => {
      btn.addEventListener('click', (ev) => {
        ev.preventDefault();
        const apiId = btn.getAttribute('data-uc-api-link');
        if (!apiId) return;
        const tabBtn = document.querySelector('.top-tab[data-top-tab="apis"]');
        if (tabBtn) tabBtn.click();
        setTimeout(() => {
          const apiBtn = document.querySelector('[data-api-id="' + apiId + '"]');
          if (apiBtn) apiBtn.click();
        }, 0);
      });
    });
    container.classList.remove('hidden');
  }

  // ---------------------------------------------------------------------
  // How To modal
  // ---------------------------------------------------------------------
  const modal = $("how-to-modal");
  $("btn-how-to").addEventListener("click", () => {
    const api = currentApi();
    $("modal-title").textContent = api ? "How to Use: " + api.name : "How To Use These APIs";
    $("modal-body").innerHTML = (api && api.how_to) || "<p>No guide available for this API.</p>";
    modal.classList.remove("hidden");
  });
  $("modal-close").addEventListener("click", () => modal.classList.add("hidden"));
  modal.addEventListener("click", (e) => { if (e.target === modal) modal.classList.add("hidden"); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") modal.classList.add("hidden"); });

  // ---------------------------------------------------------------------
  // API Guide — compact single-step coach.
  //
  // Shows ONE step at a time (no scrolling) for the selected API's curated
  // `guide` sequence. Progress dots, a step title + one-line hint, and a
  // single action button. Draggable; remembers position + per-API progress.
  //
  // Guide step schema (manifest `guide` array):
  //   { op, title, summary }                              — api_call step
  //   { type:"manual", id, title, summary, done_label }   — manual step
  //
  // Public surface:
  //   ApiGuide.show() / hide() / toggle()
  //   ApiGuide.markOpDone(opId) — called by send-handler on 2xx; advances
  //   ApiGuide.refresh()        — re-render after API switch
  //   ApiGuide.syncCurrentOp()  — keep action button state in sync
  // -----------------------------------------------------------------------
  const ApiGuide = (function () {
    try {
    const LS_KEY      = 'vima:apiGuide:v1';
    const LS_DONE_KEY = 'vima:apiGuide:done:v1';
    const panel       = $("api-guide-panel");
    if (!panel) {
      return { show(){}, hide(){}, toggle(){}, markOpDone(){}, refresh(){}, syncCurrentOp(){} };
    }
    const handle      = $("api-guide-drag-handle");
    const dotsEl      = $("ag-dots");
    const badgeNum    = $("ag-badge-num");
    const eyebrowEl   = $("ag-eyebrow");
    const titleEl     = $("ag-title");
    const descEl      = $("ag-desc");
    const actionBtn   = $("ag-action");
    const actionLabel = $("ag-action-label");
    const btnClose    = $("api-guide-close");
    const btnReset    = $("api-guide-reset");
    const btnOpen     = $("btn-api-guide");

    // ---- Persistence ----------------------------------------------------
    function loadState() {
      try { return JSON.parse(localStorage.getItem(LS_KEY) || '{}') || {}; } catch (e) { return {}; }
    }
    function saveState(st) {
      try { localStorage.setItem(LS_KEY, JSON.stringify(st)); } catch (e) {}
    }
    function loadDone() {
      try { return JSON.parse(localStorage.getItem(LS_DONE_KEY) || '{}') || {}; } catch (e) { return {}; }
    }
    function saveDone(d) {
      try { localStorage.setItem(LS_DONE_KEY, JSON.stringify(d)); } catch (e) {}
    }

    let state = loadState();
    let done  = loadDone();
    if (typeof state.visible !== 'boolean') state.visible = false;

    // ---- Position -------------------------------------------------------
    function clamp(v, min, max) { return Math.max(min, Math.min(max, v)); }
    const DEFAULT_W = 296;
    function applyPosition() {
      panel.style.width = DEFAULT_W + 'px';
      const w   = panel.offsetWidth  || DEFAULT_W;
      const h   = panel.offsetHeight || 260;
      const pad = 16;
      const maxX = Math.max(pad, window.innerWidth  - w - pad);
      const maxY = Math.max(pad, window.innerHeight - h - pad);
      let x = (typeof state.x === 'number') ? clamp(state.x, pad, maxX) : maxX;
      let y = (typeof state.y === 'number') ? clamp(state.y, pad, maxY)
                                            : Math.max(pad, window.innerHeight - h - 120);
      panel.style.left = x + 'px';
      panel.style.top  = y + 'px';
      state.x = x; state.y = y;
    }

    // ---- Guide resolution ----------------------------------------------
    function resolveGuide(api) {
      if (!api) return [];
      const opMap = {};
      (api.operations || []).forEach((op) => { opMap[op.id] = op; });
      if (Array.isArray(api.guide) && api.guide.length) {
        return api.guide.map((g, idx) => {
          const stepType = g.type || 'api_call';
          if (stepType === 'manual' || stepType === 'info') {
            return {
              stepType,
              opId:      g.id || ('manual_' + idx),
              opName:    g.title || g.id || '—',
              summary:   g.summary || '',
              doneLabel: g.done_label || 'Continue',
            };
          }
          const op = opMap[g.op];
          if (!op) return null;
          return {
            stepType: 'api_call',
            opId:     op.id,
            opName:   g.title || op.name,
            summary:  g.summary || op.description || '',
          };
        }).filter(Boolean);
      }
      // Auto-derived fallback: skip destructive ops.
      const depr = new Set(api.deprecated_categories || []);
      const DESTR = /\b(delete|destroy|remove|revoke|cancel|disconnect|expire|invalidate|wipe|purge|drop|reset|undo|unlink)\b/i;
      return (api.operations || [])
        .filter((op) => {
          if (depr.has(op.category)) return false;
          if (op.method && op.method.toUpperCase() === 'DELETE') return false;
          return !DESTR.test((op.id || '') + ' ' + (op.name || ''));
        })
        .map((op) => ({ stepType: 'api_call', opId: op.id, opName: op.name, summary: op.description || '' }));
    }

    function firstUndone(guide, apiDone) {
      return guide.find((s) => !apiDone[s.opId]) || null;
    }

    // Auto-select the workbench operation for the active api_call step.
    function autoSelectStep() {
      const api = currentApi();
      if (!api) return;
      const guide   = resolveGuide(api);
      const apiDone = done[api.id] || {};
      const next    = firstUndone(guide, apiDone);
      if (!next || next.stepType !== 'api_call') return;
      if (typeof selectOp === 'function') {
        selectOp(next.opId);
        const btn = document.querySelector('.op-btn[data-op-id="' + CSS.escape(next.opId) + '"]');
        if (btn) btn.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }

    // ---- Rendering: ONE step at a time ---------------------------------
    function render() {
      const api   = currentApi();
      const guide = resolveGuide(api);

      // Progress dots.
      if (dotsEl) {
        dotsEl.innerHTML = '';
        const apiDone = (api && done[api.id]) || {};
        const next = firstUndone(guide, apiDone);
        guide.forEach((s) => {
          const dot = document.createElement('span');
          dot.className = 'ag-dot';
          if (apiDone[s.opId])      dot.classList.add('ag-dot--done');
          else if (s === next)      dot.classList.add('ag-dot--current');
          dotsEl.appendChild(dot);
        });
      }

      if (!api || !guide.length) {
        panel.classList.remove('ag--complete', 'ag--manual');
        if (badgeNum)  badgeNum.textContent = '–';
        if (eyebrowEl) eyebrowEl.textContent = '';
        if (titleEl)   titleEl.textContent = api ? 'No guide for this API' : 'Select an API';
        if (descEl)    descEl.textContent = '';
        setAction(null);
        return;
      }

      const apiDone = done[api.id] || {};
      const next    = firstUndone(guide, apiDone);

      if (!next) {
        // Completed.
        panel.classList.add('ag--complete');
        panel.classList.remove('ag--manual');
        if (badgeNum)  badgeNum.innerHTML = '<svg width="20" height="20" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 8.5 6.5 12 13 4"/></svg>';
        if (eyebrowEl) eyebrowEl.textContent = 'All done';
        if (titleEl)   titleEl.textContent = 'Sequence complete';
        if (descEl)    descEl.textContent = 'A notification is on its way to your webhook.';
        setAction({ complete: true });
        return;
      }

      panel.classList.remove('ag--complete');
      panel.classList.toggle('ag--manual', next.stepType === 'manual');
      const idx = guide.indexOf(next) + 1;
      if (badgeNum)  badgeNum.textContent = String(idx);
      if (eyebrowEl) eyebrowEl.textContent = 'Step ' + idx + ' of ' + guide.length;
      if (titleEl)   titleEl.textContent = next.opName;
      if (descEl)    descEl.textContent = next.summary;
      setAction(next);
    }

    // ---- Action button --------------------------------------------------
    let actionMode = null; // 'send' | 'manual' | 'complete' | null
    function setAction(step) {
      if (!actionBtn) return;
      if (!step) {
        actionMode = null;
        actionBtn.hidden = true;
        return;
      }
      actionBtn.hidden = false;
      if (step.complete) {
        actionMode = 'complete';
        if (actionLabel) actionLabel.textContent = 'Start over';
        actionBtn.disabled = false;
        actionBtn.classList.add('ag-action--ghost');
        return;
      }
      actionBtn.classList.remove('ag-action--ghost');
      if (step.stepType === 'manual') {
        actionMode = 'manual';
        if (actionLabel) actionLabel.textContent = step.doneLabel || 'Continue';
        actionBtn.disabled = false;
      } else {
        actionMode = 'send';
        if (actionLabel) actionLabel.textContent = 'Send Request';
        const mainBtn = $("op-send");
        actionBtn.disabled = !mainBtn || mainBtn.disabled;
      }
    }

    function onAction() {
      if (actionMode === 'complete') { resetProgress(); return; }
      if (actionMode === 'manual')   { markManualDone(); return; }
      // send
      const mainBtn = $("op-send");
      if (!mainBtn || mainBtn.disabled) return;
      actionBtn.classList.remove('ag-action--press');
      void actionBtn.offsetWidth;
      actionBtn.classList.add('ag-action--press');
      try { mainBtn.scrollIntoView({ behavior: 'smooth', block: 'center' }); } catch (e) {}
      mainBtn.classList.remove('op-send--ghost-press');
      void mainBtn.offsetWidth;
      mainBtn.classList.add('op-send--ghost-press');
      setTimeout(() => { mainBtn.classList.remove('op-send--ghost-press'); mainBtn.click(); }, 200);
    }

    // ---- Visibility -----------------------------------------------------
    function applyVisibility() {
      // When hiding, move focus out of the panel first — leaving a focused
      // descendant under aria-hidden is an accessibility violation.
      if (!state.visible && panel.contains(document.activeElement)) {
        try { document.activeElement.blur(); } catch (e) {}
      }
      panel.classList.toggle('hidden', !state.visible);
      panel.setAttribute('aria-hidden', state.visible ? 'false' : 'true');
      if (btnOpen) {
        btnOpen.setAttribute('aria-pressed', state.visible ? 'true' : 'false');
        btnOpen.classList.toggle('btn-api-guide--active', state.visible);
      }
      if (state.visible) requestAnimationFrame(applyPosition);
    }

    function show() {
      state.visible = true;
      saveState(state);
      render();
      applyVisibility();
      panel.classList.remove('ag--enter');
      void panel.offsetWidth;
      panel.classList.add('ag--enter');
      setTimeout(autoSelectStep, 60);
    }
    function hide() {
      state.visible = false;
      saveState(state);
      applyVisibility();
    }
    function toggle() { state.visible ? hide() : show(); }

    function resetProgress() {
      const api = currentApi();
      if (!api) return;
      done[api.id] = {};
      saveDone(done);
      render();
      setTimeout(autoSelectStep, 60);
    }

    // ---- Advance --------------------------------------------------------
    function markOpDone(opId) {
      const api = currentApi();
      if (!api) return;
      done[api.id] = done[api.id] || {};
      if (done[api.id][opId]) return;
      done[api.id][opId] = true;
      saveDone(done);
      if (state.visible) {
        render();
        setTimeout(autoSelectStep, 300);
      }
    }

    function markManualDone() {
      const api = currentApi();
      if (!api) return;
      const guide   = resolveGuide(api);
      const apiDone = done[api.id] || {};
      const next    = firstUndone(guide, apiDone);
      if (!next || next.stepType !== 'manual') return;
      done[api.id] = done[api.id] || {};
      done[api.id][next.opId] = true;
      saveDone(done);
      render();
      setTimeout(autoSelectStep, 300);
    }

    function syncCurrentOp() {
      if (!state.visible) return;
      // Keep the action button's enabled state in sync with the workbench.
      if (actionMode === 'send') {
        const mainBtn = $("op-send");
        if (actionBtn) actionBtn.disabled = !mainBtn || mainBtn.disabled;
      }
    }

    // ---- Wiring ---------------------------------------------------------
    if (actionBtn) actionBtn.addEventListener('click', onAction);
    if (btnClose)  btnClose.addEventListener('click', hide);
    if (btnReset)  btnReset.addEventListener('click', resetProgress);
    if (btnOpen)   btnOpen.addEventListener('click', toggle);

    // Mirror disabled-state changes from the main Send button.
    const mainSendBtn = $("op-send");
    if (mainSendBtn && window.MutationObserver) {
      new MutationObserver(syncCurrentOp).observe(mainSendBtn, {
        attributes: true, attributeFilter: ['disabled'],
        childList: true, characterData: true, subtree: true,
      });
    }

    // ---- Drag -----------------------------------------------------------
    let drag = null;
    function onDragStart(e) {
      if (e.target.closest('.ag-x, .ag-action, .ag-restart')) return;
      const pt = (e.touches && e.touches[0]) || e;
      drag = { startX: pt.clientX, startY: pt.clientY,
               origX: state.x || panel.offsetLeft, origY: state.y || panel.offsetTop, moved: false };
      panel.classList.add('ag--dragging');
      document.addEventListener('mousemove', onDragMove);
      document.addEventListener('mouseup',   onDragEnd);
      document.addEventListener('touchmove', onDragMove, { passive: false });
      document.addEventListener('touchend',  onDragEnd);
      if (e.cancelable) e.preventDefault();
    }
    function onDragMove(e) {
      if (!drag) return;
      const pt = (e.touches && e.touches[0]) || e;
      const dx = pt.clientX - drag.startX;
      const dy = pt.clientY - drag.startY;
      if (Math.abs(dx) > 2 || Math.abs(dy) > 2) drag.moved = true;
      const pad = 8;
      const x = clamp(drag.origX + dx, pad, window.innerWidth  - panel.offsetWidth  - pad);
      const y = clamp(drag.origY + dy, pad, window.innerHeight - panel.offsetHeight - pad);
      state.x = x; state.y = y;
      panel.style.left = x + 'px';
      panel.style.top  = y + 'px';
      if (e.cancelable) e.preventDefault();
    }
    function onDragEnd() {
      if (!drag) return;
      panel.classList.remove('ag--dragging');
      document.removeEventListener('mousemove', onDragMove);
      document.removeEventListener('mouseup',   onDragEnd);
      document.removeEventListener('touchmove', onDragMove);
      document.removeEventListener('touchend',  onDragEnd);
      if (drag.moved) saveState(state);
      drag = null;
    }
    if (handle) {
      handle.addEventListener('mousedown',  onDragStart);
      handle.addEventListener('touchstart', onDragStart, { passive: false });
    }
    window.addEventListener('resize', () => { if (state.visible) applyPosition(); });

    // Restore on load.
    setTimeout(function () {
      try {
        if (state.visible) { render(); applyVisibility(); }
      } catch (err) {
        if (window.console) console.warn('[ApiGuide] init failed:', err);
      }
    }, 0);

    return {
      show, hide, toggle,
      markOpDone,
      refresh: () => { if (state.visible) { render(); applyVisibility(); } },
      syncCurrentOp,
    };
    } catch (err) {
      if (window.console) console.warn('[ApiGuide] disabled:', err);
      return { show(){}, hide(){}, toggle(){}, markOpDone(){}, refresh(){}, syncCurrentOp(){} };
    }
  })();
  window.ApiGuide = ApiGuide;

  // ---------------------------------------------------------------------
  // Top tabs
  // ---------------------------------------------------------------------
  document.querySelectorAll(".top-tab").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".top-tab").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      const tab = btn.dataset.topTab;
      document.body.style.overflow = tab === 'home' ? 'hidden' : '';
      const hdr = document.querySelector('.header');
      if (hdr) hdr.classList.toggle('header--home', tab === 'home');
      $("panel-home").classList.toggle("hidden", tab !== "home");
      $("panel-apis").classList.toggle("hidden", tab !== "apis");
      const bp = $("panel-bundles");
      if (bp) bp.classList.toggle("hidden", tab !== "bundles");
      $("panel-usecases").classList.toggle("hidden", tab !== "usecases");
      const fab = $('api-calls-fab');
      if (fab) fab.classList.toggle('hidden', tab !== 'usecases');
      const snipFab = $('apis-snippets-fab');
      if (snipFab) snipFab.classList.toggle('hidden', tab !== 'apis');
      // ViMA chat edit is only available on Use Cases
      const editBtnTop = $('global-edit-btn');
      if (editBtnTop) editBtnTop.classList.toggle('hidden', tab !== 'usecases' || SERVER_MODE);
      if (tab !== 'usecases') { apiCallsClose(); _stopPolling(); }
      else _startPolling();
      if (tab !== 'apis') apisSnippetsClose();
    });
  });

  // Home panel CTA buttons — switch to APIs or Use Cases tab
  document.querySelectorAll('.home-cta[data-switch-tab]').forEach(function(btn) {
    btn.addEventListener('click', function() {
      const tabBtn = document.querySelector('.top-tab[data-top-tab="' + btn.dataset.switchTab + '"]');
      if (tabBtn) tabBtn.click();
    });
  });

  // ---------------------------------------------------------------------
  // Browser history integration (Back / Forward buttons)
  // ---------------------------------------------------------------------
  // Every in-app navigation already happens via clicks on a known set of
  // elements (top tabs, sidebar items, bundle/API/use-case rows). We listen
  // for those clicks on the document AFTER the original handlers have run
  // and push the resulting state to the URL via the History API. A popstate
  // listener replays the click-driven handlers when the user goes Back /
  // Forward, guarded by ``_applyingHistory`` so the synthetic clicks don't
  // loop back through this same recorder.
  // ---------------------------------------------------------------------
  let _applyingHistory = false;
  let _navState = { tab: 'home' };

  function _stateToUrl(state) {
    const params = new URLSearchParams();
    if (state.tab && state.tab !== 'home') params.set('tab', state.tab);
    if (state.bundle) params.set('bundle', state.bundle);
    if (state.api) params.set('api', state.api);
    if (state.uc) params.set('uc', state.uc);
    const qs = params.toString();
    return location.pathname + (qs ? '?' + qs : '');
  }

  function _pushNavState(patch, { replace = false } = {}) {
    if (_applyingHistory) return;
    // Merge; clearing tab also clears tab-scoped selections.
    const next = Object.assign({}, _navState, patch);
    // Stringified comparison — avoids duplicate entries when the user
    // clicks the same row twice.
    if (!replace && _stateToUrl(next) === _stateToUrl(_navState)) return;
    _navState = next;
    const url = _stateToUrl(next);
    try {
      history[replace ? 'replaceState' : 'pushState'](next, '', url);
    } catch (_) { /* ignore — some sandboxed contexts disallow pushState */ }
  }

  function _applyNavState(state) {
    _applyingHistory = true;
    try {
      const tab = state.tab || 'home';
      const tabBtn = document.querySelector(`.top-tab[data-top-tab="${tab}"]`);
      if (tabBtn) tabBtn.click();
      if (state.bundle) {
        const bBtn = document.querySelector(`[data-bundle-id="${state.bundle}"]`);
        if (bBtn) bBtn.click();
      }
      if (state.api) {
        const aBtn = document.querySelector(`[data-api-id="${state.api}"]`);
        if (aBtn) aBtn.click();
      }
      if (state.uc) {
        const uBtn = document.querySelector(`[data-uc-id="${state.uc}"]`);
        if (uBtn) uBtn.click();
      }
    } finally {
      _applyingHistory = false;
      _navState = Object.assign({ tab: 'home' }, state);
    }
  }

  // Bubble-phase document recorder — fires after element handlers complete.
  document.addEventListener('click', (e) => {
    if (_applyingHistory) return;
    const t = e.target.closest('.top-tab, [data-bundle-id], [data-api-id], [data-uc-id]');
    if (!t) return;
    // Every nav click — whether from a real user gesture or a synthetic
    // ``.click()`` issued by another handler (e.g. a home-page CTA that
    // switches tabs, or a chip that opens an API) — gets its own history
    // entry. Earlier we collapsed synthetic clicks via ``replace`` to
    // avoid "intermediate hops", but that ate the home entry whenever a
    // CTA jumped from home to a tab, leaving Back to exit the app.
    if (t.matches('.top-tab')) {
      const tab = t.dataset.topTab;
      // Switching tabs clears the in-tab selection so Back goes to the bare tab.
      _pushNavState({ tab, bundle: null, api: null, uc: null });
    } else if (t.matches('[data-bundle-id]')) {
      // Each per-tab selection also clears the *other* tabs' selections,
      // otherwise stale ?api=… / ?uc=… ride along in the URL and get
      // re-applied when the user pops back to a different tab.
      _pushNavState({ tab: 'bundles', bundle: t.dataset.bundleId, api: null, uc: null });
    } else if (t.matches('[data-api-id]')) {
      _pushNavState({ tab: 'apis', api: t.dataset.apiId, bundle: null, uc: null });
    } else if (t.matches('[data-uc-id]')) {
      _pushNavState({ tab: 'usecases', uc: t.dataset.ucId, bundle: null, api: null });
    }
  });

  window.addEventListener('popstate', (e) => {
    const state = e.state || (function () {
      const p = new URLSearchParams(location.search);
      return {
        tab: p.get('tab') || 'home',
        bundle: p.get('bundle'),
        api: p.get('api'),
        uc: p.get('uc'),
      };
    })();
    _applyNavState(state);
  });

  // Honour ?tab=apis / ?tab=usecases / ?bundle=… / ?api=… / ?uc=… from
  // shared links or home-page CTAs. Replace (not push) so the first Back
  // press lands on the previous site, not on an empty home view.
  (function _bootstrapNavFromUrl() {
    const p = new URLSearchParams(location.search);
    const initial = {
      tab: p.get('tab'),
      bundle: p.get('bundle'),
      api: p.get('api'),
      uc: p.get('uc'),
    };
    // Infer tab from a deep-link selection if no explicit ?tab=.
    if (!initial.tab) {
      if (initial.bundle) initial.tab = 'bundles';
      else if (initial.api) initial.tab = 'apis';
      else if (initial.uc) initial.tab = 'usecases';
      else initial.tab = 'home';
    }
    if (initial.tab !== 'home' || initial.bundle || initial.api || initial.uc) {
      _applyNavState(initial);
    } else {
      document.body.style.overflow = 'hidden'; // home is the default tab
      const hdr = document.querySelector('.header');
      if (hdr) hdr.classList.add('header--home');
    }
    _pushNavState(initial, { replace: true });
  })();
  startUsIpStatusPolling();
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible') refreshUsIpStatus();
  });

  // ---------------------------------------------------------------------
  // API state lives in core/state.js (currentApiId/currentOpId/currentState,
  // ioCache, lastOpByApi, currentApi(), currentOp()) — imported above.
  // ---------------------------------------------------------------------

  // ---------------------------------------------------------------------
  // API About panel & globe
  // ---------------------------------------------------------------------
  (function () {
    const aboutBtn = document.getElementById('api-about-btn');
    const aboutPanel = document.getElementById('api-about-panel');
    const workbench = document.getElementById('api-workbench');

    const apisPanel = document.getElementById('panel-apis');

    function showAbout() {
      document.querySelectorAll('[data-api-id]').forEach(b => b.classList.remove('active'));
      if (aboutBtn) aboutBtn.classList.add('active');
      if (aboutPanel) aboutPanel.classList.remove('hidden');
      if (workbench) workbench.classList.add('hidden');
      if (apisPanel) apisPanel.classList.add('panel--about');
    }

    function showWorkbench() {
      if (aboutBtn) aboutBtn.classList.remove('active');
      if (aboutPanel) aboutPanel.classList.add('hidden');
      if (workbench) workbench.classList.remove('hidden');
      if (apisPanel) apisPanel.classList.remove('panel--about');
    }

    if (aboutBtn) aboutBtn.addEventListener('click', showAbout);

    // "Keys & Config" shortcut inside the about panel
    const keysLink = document.getElementById('aap-open-keys');
    if (keysLink) keysLink.addEventListener('click', () => {
      // The header button was renamed cfg-btn -> cfg-trigger-btn; fall
      // back to the legacy id so older templates still work.
      const cfgBtn = document.getElementById('cfg-trigger-btn')
                  || document.getElementById('cfg-btn');
      if (cfgBtn) cfgBtn.click();
    });

    // Expose for API item clicks
    window._showApiWorkbench = showWorkbench;

    // Grey globe animation
    const canvas = document.getElementById('aap-globe');
    if (canvas) {
      const ctx = canvas.getContext('2d');
      const SIZE = 820, RADIUS = SIZE * 0.32, CX = SIZE / 2, CY = SIZE / 2;
      const SPEED = 0.003, TOTAL_DOTS = 90;
      const pts = [];
      for (let i = 0; i < TOTAL_DOTS; i++) {
        const phi = Math.acos(-1 + (2 * i) / TOTAL_DOTS);
        const theta = Math.sqrt(TOTAL_DOTS * Math.PI) * phi;
        pts.push({ x: Math.cos(theta) * Math.sin(phi), y: Math.sin(theta) * Math.sin(phi), z: Math.cos(phi) });
      }
      let rot = 0, last = null;
      function renderGlobe(ts) {
        const delta = last ? Math.min((ts - last) / 16.667, 2) : 1;
        last = ts;
        ctx.clearRect(0, 0, SIZE, SIZE);
        const gOpacity = 0.18;
        ctx.lineWidth = 0.9;
        for (let lat = -80; lat <= 80; lat += 20) {
          const lR = (lat * Math.PI) / 180;
          for (let seg = 0; seg < 360; seg += 5) {
            const l0 = ((seg * Math.PI) / 180) + rot;
            const l1 = (((seg + 5) * Math.PI) / 180) + rot;
            const z0 = Math.cos(lR) * Math.sin(l0), z1 = Math.cos(lR) * Math.sin(l1);
            const a = gOpacity * Math.max(0, Math.min(1, ((z0 + z1) / 2 + 0.4) / 0.8));
            if (a < 0.005) continue;
            const s0 = 1 / (1.8 - z0), s1 = 1 / (1.8 - z1);
            ctx.strokeStyle = `rgba(255,110,20,${a})`;
            ctx.beginPath();
            ctx.moveTo(CX + Math.cos(lR) * Math.cos(l0) * RADIUS * s0, CY + Math.sin(lR) * RADIUS * s0);
            ctx.lineTo(CX + Math.cos(lR) * Math.cos(l1) * RADIUS * s1, CY + Math.sin(lR) * RADIUS * s1);
            ctx.stroke();
          }
        }
        for (let lon = 0; lon < 360; lon += 20) {
          for (let seg = -88; seg < 90; seg += 5) {
            const l0 = (seg * Math.PI) / 180, l1 = ((seg + 5) * Math.PI) / 180;
            const lR = ((lon * Math.PI) / 180) + rot;
            const z0 = Math.cos(l0) * Math.sin(lR), z1 = Math.cos(l1) * Math.sin(lR);
            const a = gOpacity * Math.max(0, Math.min(1, ((z0 + z1) / 2 + 0.4) / 0.8));
            if (a < 0.005) continue;
            const s0 = 1 / (1.8 - z0), s1 = 1 / (1.8 - z1);
            ctx.strokeStyle = `rgba(255,110,20,${a})`;
            ctx.beginPath();
            ctx.moveTo(CX + Math.cos(l0) * Math.cos(lR) * RADIUS * s0, CY + Math.sin(l0) * RADIUS * s0);
            ctx.lineTo(CX + Math.cos(l1) * Math.cos(lR) * RADIUS * s1, CY + Math.sin(l1) * RADIUS * s1);
            ctx.stroke();
          }
        }
        const projected = pts.map(p => {
          const rx = p.x * Math.cos(rot) - p.z * Math.sin(rot);
          const rz = p.x * Math.sin(rot) + p.z * Math.cos(rot);
          const sc = 1 / (1.8 - rz);
          const fade = Math.max(0, Math.min(1, (rz + 0.2) / 0.4));
          return { px: CX + rx * RADIUS * sc, py: CY + p.y * RADIUS * sc, rz, sc, alpha: 0.15 + fade * 0.75 };
        });
        projected.filter(p => p.rz > -0.18).sort((a, b) => a.rz - b.rz).forEach(p => {
          const r = Math.round(255);
          const g = Math.round(110 + p.alpha * 40);
          ctx.shadowColor = `rgba(255,80,0,${p.alpha * 0.8})`;
          ctx.shadowBlur = 8 * p.sc;
          ctx.fillStyle = `rgba(${r},${g},20,${p.alpha})`;
          ctx.beginPath();
          ctx.arc(p.px, p.py, 2.5 * p.sc, 0, Math.PI * 2);
          ctx.fill();
        });
        ctx.shadowBlur = 0;
        rot += SPEED * delta;
        requestAnimationFrame(renderGlobe);
      }
      requestAnimationFrame(renderGlobe);
    }

    // Set initial state
    showAbout();
  })();

  // ---------------------------------------------------------------------
  // API list (sidebar)
  // ---------------------------------------------------------------------
  document.querySelectorAll("[data-api-id]").forEach((btn) => {
    btn.addEventListener("click", () => {
      if (_isNonUsBlockedApiId(btn.dataset.apiId)) return;
      document.querySelectorAll("[data-api-id]").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      setCurrentApiId(btn.dataset.apiId);
      setCurrentOpId(null);
      if (window._showApiWorkbench) window._showApiWorkbench();
      renderApi();
      // Refresh the floating API Guide to reflect the newly-selected API.
      if (window.ApiGuide) ApiGuide.refresh();
      // If the Python snippets drawer is open, follow the selection so
      // it shows the snippet for the API the user just picked.
      apisSnippetsFollowApi(getCurrentApiId());
    });
  });

  // ---------------------------------------------------------------------
  function renderApiPairs(api) {
    const el = document.getElementById('api-pairs');
    if (!el) return;
    const complements = Array.isArray(api.complements) ? api.complements : [];
    const requires = Array.isArray(api.requires) ? api.requires : [];
    const bundles = Array.isArray(api.bundles) ? api.bundles : [];
    function _updateContextSection() {
      const section = document.getElementById('api-context-section');
      if (!section) return;
      const strip = document.getElementById('state-strip');
      const hasStrip = strip && strip.children.length > 0;
      section.hidden = !hasStrip && el.hidden;
    }
    if (!complements.length && !requires.length && !bundles.length) {
      el.hidden = true;
      el.innerHTML = '';
      _updateContextSection();
      return;
    }
    function chip(id, kind) {
      const ref = APIS.find((a) => a.id === id);
      if (!ref) return '';
      const cls = 'api-pair-chip api-pair-chip--' + kind + (ref.configured ? ' configured' : '');
      return `<button class="${cls}" data-pair-api="${escapeHtml(id)}" title="${kind === 'requires' ? 'Required' : 'APIs often paired with'} — ${ref.configured ? 'configured' : 'not configured'}">
        <span class="api-pair-dot ${ref.configured ? 'ok' : 'off'}"></span>${escapeHtml(ref.name)}
      </button>`;
    }
    let html = '';
    if (requires.length) {
      html += '<div class="api-pairs-row"><span class="api-pairs-label">Requires</span><div class="api-pairs-chips">' +
        requires.map((id) => chip(id, 'requires')).join('') + '</div></div>';
    }
    if (complements.length) {
      html += '<div class="api-pairs-row"><span class="api-pairs-label">APIs often paired with</span><div class="api-pairs-chips">' +
        complements.map((id) => chip(id, 'complement')).join('') + '</div></div>';
    }
    if (bundles.length) {
      const bundleChips = bundles.map((bid) => {
        const cached = (getBundlesCache() || []).find((b) => b.id === bid);
        const label = cached ? cached.name : bid;
        const accent = (cached && cached.accent) || '#ffcb05';
        return `<button class="api-pair-chip api-pair-chip--bundle" data-pair-bundle="${escapeHtml(bid)}" style="--bundle-accent: ${escapeHtml(accent)};"><span class="api-pair-chip-dot"></span>${escapeHtml(label)}</button>`;
      }).join('');
      html += '<div class="api-pairs-row"><span class="api-pairs-label">Part of bundles</span><div class="api-pairs-chips">' + bundleChips + '</div></div>';
    }
    // "See it working in use cases" — any use case whose manifest lists
    // this API id under `apis`.
    const matchingUseCases = (getUseCasesCache() || []).filter((uc) =>
      Array.isArray(uc.apis) && uc.apis.includes(api.id)
    );
    if (matchingUseCases.length) {
      const ucChips = matchingUseCases.map((uc) => {
        const accent = uc.accent || '#ff6a00';
        return `<button class="api-pair-chip api-pair-chip--usecase" data-pair-usecase="${escapeHtml(uc.id)}" style="--bundle-accent: ${escapeHtml(accent)};" title="Open the ${escapeHtml(uc.name || uc.id)} use case"><span class="api-pair-chip-dot"></span>${escapeHtml(uc.name || uc.id)}</button>`;
      }).join('');
      html += '<div class="api-pairs-row"><span class="api-pairs-label">See it working in use cases</span><div class="api-pairs-chips">' + ucChips + '</div></div>';
    } else if (!getUseCasesCache()) {
      // Cache not loaded yet — re-render once it arrives.
      loadUseCases().then(() => {
        if (currentApi() && currentApi().id === api.id) renderApiPairs(api);
      });
    }
    el.hidden = false;
    _updateContextSection();
    el.innerHTML = html;
    el.querySelectorAll('[data-pair-api]').forEach((b) => {
      b.addEventListener('click', () => {
        const btn = document.querySelector(`[data-api-id="${b.dataset.pairApi}"]`);
        if (btn) btn.click();
      });
    });
    el.querySelectorAll('[data-pair-bundle]').forEach((b) => {
      b.addEventListener('click', () => {
        const bundlesTabBtn = document.querySelector('.top-tab[data-top-tab="bundles"]');
        if (bundlesTabBtn) bundlesTabBtn.click();
        setTimeout(() => {
          const sideBtn = document.querySelector(`[data-bundle-id="${b.dataset.pairBundle}"]`);
          if (sideBtn) sideBtn.click();
        }, 0);
      });
    });
    el.querySelectorAll('[data-pair-usecase]').forEach((b) => {
      b.addEventListener('click', () => {
        const ucId = b.dataset.pairUsecase;
        if (typeof _isNonUsBlockedUseCaseById === 'function' && _isNonUsBlockedUseCaseById(ucId)) return;
        const ucTabBtn = document.querySelector('.top-tab[data-top-tab="usecases"]');
        if (ucTabBtn) ucTabBtn.click();
        setTimeout(() => {
          const sideBtn = document.querySelector(`[data-uc-id="${ucId}"]`);
          if (sideBtn) sideBtn.click();
        }, 0);
      });
    });
  }

  // ---------------------------------------------------------------------
  // Render API
  // ---------------------------------------------------------------------
  function renderApi() {
    const api = currentApi();
    if (!api) return;
    if (_isNonUsBlockedApiId(api.id)) return;
    $("api-title").textContent = api.name;
    $("api-desc").textContent = api.description || "";
    const docs = $("api-docs");

    // Simulator toggle — fetch current status for this API
    fetchSimStatus(api.id);
    if (docs) {
      if (api.docs_url) {
        docs.href = api.docs_url;
        docs.style.display = "inline-flex";
      } else {
        docs.style.display = "none";
      }
    }

    // "Often paired with" — render complement chips and a small "part of N
    // solution bundles" hint, sourced from the manifest fields shipped by
    // /catalog (apis.complements + apis.bundles).
    renderApiPairs(api);

    // Operations list grouped by category
    const cats = {};
    (api.categories || []).forEach((c) => (cats[c] = []));
    (api.operations || []).forEach((op) => {
      (cats[op.category] = cats[op.category] || []).push(op);
    });
    const opsEl = $("op-categories");
    opsEl.innerHTML = "";
    const deprecatedCats = new Set(api.deprecated_categories || []);
    Object.entries(cats).forEach(([cat, ops]) => {
      if (!ops.length) return;
      const isDepr = deprecatedCats.has(cat);
      const h = document.createElement("div");
      h.className = "op-cat-name" + (isDepr ? " op-cat-deprecated" : "");
      h.innerHTML = escapeHtml(cat) + (isDepr ? ' <span class="op-depr-badge">Deprecated</span>' : '');
      opsEl.appendChild(h);
      ops.forEach((op) => {
        const b = document.createElement("button");
        b.className = "op-btn" + (isDepr ? " op-btn-deprecated" : "");
        b.textContent = op.name;
        b.dataset.opId = op.id;
        if (op.description) b.title = op.description;
        if (isDepr) b.disabled = true;
        else b.addEventListener("click", () => selectOp(op.id));
        opsEl.appendChild(b);
      });
    });

    // Clear panels (will be repopulated from cache if a prior op exists)
    $("op-method").textContent = "—";
    $("op-method").className = "op-method";
    $("op-name").textContent = "Select an operation";
    $("op-desc").textContent = "";
    $("op-note").innerHTML = "";
    $("op-params").innerHTML = "";
    $("op-hint").innerHTML = "";
    _resetLaunchBanner();
    $("op-send").disabled = true;
    $("req-body").textContent = "—";
    $("resp-body").textContent = "—";
    $("resp-status").textContent = "";
    $("resp-status").className = "status-pill";    $('resp-status').title = "";
    lastIoData.request = null;
    lastIoData.response = null;
    refreshState();

    // Restore the last-used operation for this API, or fall back to the first.
    const lastOp = lastOpByApi[api.id];
    if (lastOp && api.operations.some((o) => o.id === lastOp)) {
      selectOp(lastOp);
    } else if (api.operations && api.operations.length > 0) {
      selectOp(api.operations[0].id);
    }
  }

  function refreshState() {
    const api = currentApi();
    if (!api) return;
    _nativeFetch(`/explorer/${api.id}/state`)
      .then((r) => r.json())
      .then((d) => {
        setCurrentState(d.state || {});
        renderStateStrip();
        // refresh param defaults if an op is open
        if (getCurrentOpId()) renderParams();
        // Show Open Finance setup guide every time (unless suppressed)
          if (api.id === 'open_finance' && !NON_US_MODE) {
          showOfinSetupModal();
        }
      })
      .catch(() => {});
  }

  function renderStateStrip() {
    const api = currentApi();
    const strip = $("state-strip");
    strip.innerHTML = "";
    const schema = api.state_schema || [];
    const hasContent = !api.configured || schema.length > 0;
    if (!api.configured) {
      const w = document.createElement("div");
      w.className = "state-pill";
      w.innerHTML = `<span class="k">⚠</span><span class="v">Not configured — check .env</span>`;
      w.style.borderColor = "#eb001b";
      w.style.color = "#a01010";
      strip.appendChild(w);
    }
    schema.forEach((s) => {
      const v = getCurrentState()[s.key];
      const pill = document.createElement("div");
      pill.className = "state-pill" + (v ? "" : " empty");
      pill.innerHTML = `<span class="k">${s.label}:</span><span class="v">${v || "—"}</span>`;
      strip.appendChild(pill);
    });
    // Show or hide the whole context section depending on whether there is
    // state content — the api-pairs visibility is handled separately.
    const section = document.getElementById('api-context-section');
    if (section) {
      const pairsEl = document.getElementById('api-pairs');
      const pairsHasContent = pairsEl && !pairsEl.hidden;
      if (!hasContent && !pairsHasContent) {
        section.hidden = true;
      } else {
        section.hidden = false;
      }
    }
  }

  // ---------------------------------------------------------------------
  // Select operation
  // ---------------------------------------------------------------------
  function selectOp(opId) {
    setCurrentOpId(opId);
    lastOpByApi[getCurrentApiId()] = opId;
    document.querySelectorAll(".op-btn").forEach((b) => {
      b.classList.toggle("active", b.dataset.opId === opId);
    });
    const op = currentOp();
    if (!op) return;
    $("op-method").textContent = op.method || "POST";
    $("op-method").className = "op-method " + (op.method || "POST");
    $("op-name").textContent = op.name;
    $("op-desc").textContent = op.description || "";
    $("op-note").innerHTML = op.note || "";
    $("op-send").disabled = false;
    $("op-hint").innerHTML = "";
    renderParams();    restoreIo();
    // Keep the floating API Guide's "current step" highlight in sync.
    if (window.ApiGuide) ApiGuide.syncCurrentOp();
    // If the View Code panel is open for this API, refresh it so the
    // snippet tracks whichever operation the user has chosen.
    apisSnippetsRefreshOp(getCurrentApiId());
  }

  function restoreIo() {
    const cached = (ioCache[getCurrentApiId()] || {})[getCurrentOpId()];
    if (cached) {
      // Restore header-visibility state for this cached result
      if (cached.headersVisible) {
        headersVisible.request = cached.headersVisible.request;
        headersVisible.response = cached.headersVisible.response;
        updateHeaderToggleBtn('request');
        updateHeaderToggleBtn('response');
      }
      lastIoData.request = cached.request;
      lastIoData.response = cached.response;
      renderIoPanel('request', cached.request);
      renderIoPanel('response', cached.response);
      if (cached.statusCode != null) {
        setStatus(cached.statusCode);
      } else {
        setStatus(null);
      }
      $('op-hint').innerHTML = cached.hintHtml || '';
      if (cached.launch) {
        _showLaunchBanner(cached.launch);
      } else if (currentOp() && currentOp().browser_action) {
        _showLaunchBannerPending();
      } else {
        _resetLaunchBanner();
      }
    } else {
      lastIoData.request = null;
      lastIoData.response = null;
      $("req-body").textContent = "—";
      $("resp-body").textContent = "—";
      $("resp-status").textContent = "";
      $("resp-status").className = "status-pill";      $('resp-status').title = "";      $("op-hint").innerHTML = "";
      if (currentOp() && currentOp().browser_action) {
        _showLaunchBannerPending();
      } else {
        _resetLaunchBanner();
      }
      previewRequest();
    }
  }

  function resolveDefault(def) {
    if (typeof def !== "string") return def;
    return def.replace("${timestamp}", String(Math.floor(Date.now() / 1000)));
  }

  function renderParams() {
    const op = currentOp();
    const wrap = $("op-params");
    wrap.innerHTML = "";
    (op.params || []).forEach((p) => {
      const row = document.createElement("div");
      row.className = "param-row";
      const labelHtml = `<label>${p.label || p.name}
        ${p.required ? '<span class="hint">required</span>' : ""}
        ${p.warning ? `<span class="param-warning">&#9888; ${p.warning}</span>` : ""}
      </label>`;
      let value = "";
      if (p.source && p.source.startsWith("state:")) {
        const k = p.source.slice("state:".length);
        value = getCurrentState()[k] || "";
      }
      if (!value && p.default != null) value = resolveDefault(p.default);
      // Cross-API prefill: auto-fill card_reference / card_ref from the most
      // recently returned cardReference (e.g. Consent → Create Consent).
      if (!value && (p.name === "card_reference" || p.name === "card_ref")) {
        try {
          const saved = localStorage.getItem("vima:cardReference");
          if (saved) value = saved;
        } catch (e) { /* ignore */ }
      }

      let input;
      if (p.type === "select" && Array.isArray(p.options)) {
        input = document.createElement("select");
        p.options.forEach((opt) => {
          const o = document.createElement("option");
          const isObj = opt && typeof opt === "object";
          o.value = isObj ? opt.value : opt;
          o.textContent = isObj ? opt.label : opt;
          if (o.value === String(value)) o.selected = true;
          input.appendChild(o);
        });
      } else if (p.type === "account_select") {
        input = document.createElement("select");
        const accounts = getCurrentState().accounts || [];
        if (!accounts.length) {
          const opt = document.createElement("option");
          opt.value = "";
          opt.textContent = "— no accounts loaded — run Refresh Accounts first —";
          opt.disabled = true;
          opt.selected = true;
          input.appendChild(opt);
        } else {
          accounts.forEach((a) => {
            const opt = document.createElement("option");
            opt.value = a.id;
            const num = a.number ? `••${String(a.number).slice(-4)}` : a.id;
            const type = a.type ? ` · ${a.type}` : "";
            const name = a.name ? ` — ${a.name}` : "";
            opt.textContent = `${num}${type}${name}`;
            if (String(a.id) === String(value)) opt.selected = true;
            input.appendChild(opt);
          });
        }
      } else if (p.type === "provider_select") {
        // Populated by Open Finance EU → Get Providers. Items: {id, name, country}.
        input = document.createElement("select");
        const providers = getCurrentState().providers || [];
        if (!providers.length) {
          const opt = document.createElement("option");
          opt.value = "";
          opt.textContent = "— no providers loaded — run Get Providers first —";
          opt.disabled = true;
          opt.selected = true;
          input.appendChild(opt);
        } else {
          providers.forEach((pr) => {
            const opt = document.createElement("option");
            opt.value = pr.id;
            const country = pr.country ? ` [${pr.country}]` : "";
            opt.textContent = `${pr.name || pr.id}${country}`;
            if (String(pr.id) === String(value)) opt.selected = true;
            input.appendChild(opt);
          });
        }
      } else if (p.type === "redirect_url_select") {
        // Editable dropdown: pick a known redirect URL or type a custom one.
        // Implemented as <input list="..."> + <datalist> so the user can both
        // pick from the seeded list and free-text a different value.
        input = document.createElement("input");
        input.type = "text";
        input.value = value;
        input.placeholder = "https://...";
        const urls = getCurrentState().redirect_urls || [];
        if (urls.length) {
          const listId = `redirect-urls-${p.name}-${Math.random().toString(36).slice(2, 8)}`;
          const dl = document.createElement("datalist");
          dl.id = listId;
          urls.forEach((u) => {
            const o = document.createElement("option");
            o.value = u;
            dl.appendChild(o);
          });
          input.setAttribute("list", listId);
          row.appendChild(dl);
          // Default to the first known URL if the field is empty.
          if (!value) input.value = urls[0];
        }
      } else {
        input = document.createElement("input");
        input.type = p.type === "number" ? "number" : "text";
        input.value = value;
        input.placeholder = p.label || p.name;
      }
      input.dataset.name = p.name;
      input.addEventListener("input", previewRequest);
      input.addEventListener("change", previewRequest);
      row.innerHTML = labelHtml;
      row.appendChild(input);
      wrap.appendChild(row);
    });
    previewRequest();
  }

  function collectParams() {
    const params = {};
    document.querySelectorAll("#op-params input, #op-params select").forEach((i) => {
      if (i.value !== "") params[i.dataset.name] = i.value;
    });
    return params;
  }

  function previewRequest() {
    // Only overwrite request panel if we don't have a real cached response for this op.
    const cached = (ioCache[getCurrentApiId()] || {})[getCurrentOpId()];
    if (cached) return;
    const op = currentOp();
    if (!op) return;
    const preview = {
      method: op.method || "POST",
      operation: op.id,
      params: collectParams(),
      note: "Preview — click Send to execute. The actual upstream HTTP request will be shown here after sending.",
    };
    $("req-body").textContent = fmt(preview);
  }

  // ---------------------------------------------------------------------
  // Send
  // ---------------------------------------------------------------------
  $("op-send").addEventListener("click", async () => {
    const api = currentApi();
    const op = currentOp();
    if (!api || !op) return;
    const params = collectParams();
    $("op-send").disabled = true;
    $("op-send").textContent = "Sending…";
    $("resp-status").textContent = "";
    $('resp-status').className = "status-pill";
    $('resp-status').title = "";
    const _dots = '<div class="sending-dots"><span></span><span></span><span></span></div>';
    $('resp-body').innerHTML = _dots;
    try {
      const r = await _nativeFetch(`/explorer/${api.id}/execute`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ operation: op.id, params }),
      });
      const data = await r.json();
      lastIoData.request = data.request;
      lastIoData.response = data.response;
      renderIoPanel('request', data.request);
      renderIoPanel('response', data.response);
      // Auto-capture cardReference from any response for cross-API prefill.
      const capturedCardRef = _findKey(data.response && data.response.body, "cardReference")
        || _findKey(data.data, "cardReference");
      if (capturedCardRef) {
        try { localStorage.setItem("vima:cardReference", capturedCardRef); } catch (e) {}
      }
      const s = data.response && data.response.status_code;
      if (s != null) {
        setStatus(s);
      }
      // Mark the step done in the floating API Guide on any 2xx response.
      if (s != null && s >= 200 && s < 300 && window.ApiGuide) {
        ApiGuide.markOpDone(op.id);
      }
      // Hints
      $("op-hint").innerHTML = "";
      _resetLaunchBanner();
      if (data.hints && data.hints.note) {
        const n = document.createElement("div");
        n.className = "muted op-hint-card op-hint-card--note";
        n.textContent = data.hints.note;
        $("op-hint").appendChild(n);
      }
      if (data.hints && data.hints.open_link) {
        _showLaunchBanner({
          url: data.hints.open_link,
          label: data.hints.open_link_label || "Launch Connect ↗",
          note: data.hints.open_link_note
            || "Open in a new tab, complete the bank login flow, then run the next step.",
          testCredentials: data.hints.test_credentials || null,
        });
      } else if (data.hints && data.hints.test_credentials) {
        // No launch URL yet (call hasn't been made or returned an error),
        // but we still want to surface the sandbox test PSU credentials
        // so the user knows what to log in with. Render as a standalone
        // card in the op-hint area.
        const card = document.createElement("div");
        card.className = "op-hint-card op-hint-card--creds";
        card.appendChild(_buildTestCredentialsBlock(data.hints.test_credentials));
        $("op-hint").appendChild(card);
      }      // Browser-action button: shown when op.browser_action is true.
      // Prefers hints.browser_launch_url; falls back to first URL found in response body.
      if (op.browser_action) {
        const launchUrl = (data.hints && data.hints.browser_launch_url)
          ? data.hints.browser_launch_url
          : _findFirstUrl(data.response && data.response.body);
        const launchNote = (data.hints && data.hints.browser_launch_note)
          || "Browser interaction required — complete the flow, then proceed to the next step.";
        if (launchUrl) {
          // Update the top-of-panel banner with the real URL so it's
          // immediately visible without scrolling.
          _showLaunchBanner({ url: launchUrl, label: "Launch 3DS Method ↗", note: launchNote });
        } else {
          // Call succeeded but no URL yet — keep the pending state.
          _showLaunchBannerPending();
        }
      }
      if (data.hints && data.hints.pdf_base64) {
        const binary = atob(data.hints.pdf_base64);
        const bytes = new Uint8Array(binary.length);
        for (let i = 0; i < binary.length; i++) bytes[i] = binary.charCodeAt(i);
        const blob = new Blob([bytes], { type: "application/pdf" });
        const blobUrl = URL.createObjectURL(blob);
        const btn = document.createElement("a");
        btn.href = blobUrl;
        btn.target = "_blank";
        btn.rel = "noopener";
        btn.textContent = "View PDF Statement ↗";
        btn.style.cssText = "display:inline-block;margin-top:8px;padding:7px 14px;background:#005b99;color:#fff;border-radius:5px;text-decoration:none;font-size:13px;font-weight:600;";
        const dl = document.createElement("a");
        dl.href = blobUrl;
        dl.download = "statement.pdf";
        dl.textContent = "Download PDF";
        dl.style.cssText = "display:inline-block;margin-top:8px;margin-left:8px;padding:7px 14px;background:#f4f6fa;color:#005b99;border:1px solid #c5d0df;border-radius:5px;text-decoration:none;font-size:13px;font-weight:600;";
        $('op-hint').appendChild(btn);
        $('op-hint').appendChild(dl);
      }      // Cache for restore on API/op switch.
      const apiBucket = (ioCache[api.id] = ioCache[api.id] || {});
      apiBucket[op.id] = {
        request: data.request,
        response: data.response,
        statusCode: s,
        hintHtml: $('op-hint').innerHTML,
        launch: (data.hints && data.hints.open_link) ? {
          url: data.hints.open_link,
          label: data.hints.open_link_label || "Launch Connect ↗",
          note: data.hints.open_link_note
            || "Open in a new tab, complete the bank login flow, then run the next step.",
          testCredentials: data.hints.test_credentials || null,
        } : (op.browser_action && data.hints && data.hints.browser_launch_url) ? {
          url: data.hints.browser_launch_url,
          label: "Launch 3DS Method ↗",
          note: data.hints.browser_launch_note
            || "Browser interaction required — complete the flow, then proceed to the next step.",
          testCredentials: null,
        } : null,
        headersVisible: { ...headersVisible },
      };
      // Update state
      if (data.state) {
        setCurrentState(data.state);
        renderStateStrip();
      }
      // Open Finance: show setup guide if refresh_accounts returns no accounts
      if (api.id === 'open_finance' && op.id === 'refresh_accounts' && !NON_US_MODE) {
        const respBody = data.response && data.response.body;
        const accounts = _findKey(respBody, 'accounts') || (Array.isArray(respBody) ? respBody : null);
        const isError = data.response && data.response.status_code >= 400;
        if (isError || (accounts != null && (Array.isArray(accounts) ? accounts.length === 0 : false))) {
          showOfinSetupModal();
        }
      }
    } catch (e) {
      $("resp-body").textContent = String(e);
    } finally {
      $("op-send").disabled = false;
      $("op-send").textContent = "Send";
    }
  });

  // ---------------------------------------------------------------------
  // Copy buttons
  // ---------------------------------------------------------------------
  document.querySelectorAll("[data-copy]").forEach((b) => {
    b.addEventListener("click", () => {
      const el = $(b.dataset.copy);
      navigator.clipboard.writeText(el ? el.textContent : "");
      const t = b.textContent;
      b.textContent = "Copied";
      setTimeout(() => (b.textContent = t), 900);
    });
  });

  // ---------------------------------------------------------------------
  // Use cases
  // ---------------------------------------------------------------------
  function renderUseCase(id) {
    const uc = USE_CASES.find((u) => u.id === id) || USE_CASES[0];
    if (!uc) return;
    // Clear log and close drawer when switching use cases
    if (uc.id !== _currentUcId) {
      apiCallsClear();
      apiCallsClose();
    }
    // Restore Full Screen button (hidden when a webview use case is active)
    const _wvRefresh = document.getElementById('uc-webview-refresh-btn');
    if (_wvRefresh) _wvRefresh.remove();
    const _popoutBtn = document.getElementById('uc-popout-btn');
    if (_popoutBtn) _popoutBtn.hidden = false;
    _parkActiveWebview();

    _currentUcId = uc.id;
    updateUcSidebar(uc);
    const title = $("uc-title"); if (title) title.textContent = uc.name;
    const desc = $("uc-desc"); if (desc) desc.textContent = uc.description || "";
    if (uc.render === "pfm") {
      renderPfm();
    } else if (uc.render === "enrichment") {
      renderEnrichment();
    } else if (uc.render === "recurring") {
      renderRecurring();
    } else if (uc.render === "psi") {
      renderPsi();
    } else if (uc.render === "bin_lookup") {
      renderBinLookup();
    } else if (uc.render === "consumer_clarity") {
      renderClarity();
    } else if (uc.render === "easy_savings") {
      renderEasySavings();
    } else if (uc.render === "places") {
      renderPlaces();
    } else if (uc.render === "identity") {
      renderIdentity();
    } else if (uc.render === "specials") {
      renderSpecials();
    } else if (uc.render === "findacard") {
      renderFindACard();
    } else if (uc.render === "sonic") {
      renderSonic();
    } else if (uc.render === "txnotify") {
      renderTxNotify();
    } else if (uc.render === "testchat") {
      renderTestChat();
    } else if (uc.render === "the_wire") {
      renderTheWire();
    } else {
      $("uc-body").innerHTML = `<p class="muted">${(uc.apis && uc.apis.length)
        ? "Composes: " + uc.apis.join(", ")
        : "Use cases composed from the APIs above will appear here."}</p>`;
    }
  }

  // ===================== Data Enrichment Use Case =====================
  // Shows raw transaction strings transforming into structured enriched data.
  // Each row has a "before" (raw) and "after" (enriched) state that the user
  // can trigger one-by-one or all at once.

  const ENRICH_CAT_COLORS = {
    "Groceries & Dining": "#f97316",
    "Coffee Shops":        "#f97316",
    "Shopping":            "#ec4899",
    "Shopping & Retail":   "#ec4899",
    "Rental Car & Taxi":   "#0ea5e9",
    "Transportation":      "#0ea5e9",
    "Travel & Vacation":   "#3b82f6",
    "Streaming Services":  "#f43f5e",
    "Entertainment":       "#f43f5e",
    "Groceries":           "#10b981",
    "Bills & Utilities":   "#8b5cf6",
    "Income":              "#0f7050",
  };

  function enrichCatColor(cat, group) {
    return ENRICH_CAT_COLORS[cat] || ENRICH_CAT_COLORS[group] || "#94a3b8";
  }

  function enrichLogoHtml(e) {
    if (e.logoUrl) {
      return `<img src="${escapeHtml(e.logoUrl)}" alt="${escapeHtml(e.name)}" class="enrich-logo-img" loading="lazy">`;
    }
    const initials = (e.name || "?").slice(0, 2).toUpperCase();
    const color = enrichCatColor(e.category, e.categoryGroup);
    return `<svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="20" fill="${color}"/><text x="20" y="26" text-anchor="middle" font-size="14" fill="white">${initials}</text></svg>`;
  }

  // State: which rows have been enriched
  const ENRICH = { enriched: new Set(), data: [] };

  function renderEnrichment() {
    _renderCachedWebview('enrichment', 'enrichment-webview-frame', _appPath('/enrichment/index.html'), 'Data Enrichment');
  }

  function enrichRender() {
    const body = $("uc-body");
    if (!body || !ENRICH.data.length) return;
    const allDone = ENRICH.enriched.size === ENRICH.data.length;
    body.innerHTML = `
      <div class="enrich-stage">
        <div class="enrich-header">
          <div class="enrich-header-text">
            <h2>Transaction Enrichment</h2>
            <p>Raw bank statement text is transformed into structured, human-readable merchant data — powering better UX, smarter categorisation, and richer insights.</p>
          </div>
          <div class="enrich-header-actions">
            ${allDone
              ? `<button class="enrich-btn-reset" id="enrich-reset">Reset demo</button>`
              : `<button class="enrich-btn-all" id="enrich-all">Enrich all</button>`
            }
          </div>
        </div>

        <div class="enrich-pipeline-legend">
          <div class="enrich-legend-item"><span class="enrich-legend-dot raw"></span>Raw input</div>
          <div class="enrich-legend-arrow">→</div>
          <div class="enrich-legend-item"><span class="enrich-legend-dot enriched"></span>Enriched output</div>
        </div>

        <div class="enrich-rows" id="enrich-rows">
          ${ENRICH.data.map(enrichRowHtml).join("")}
        </div>

        <div class="enrich-footer">
          <div class="enrich-stats">
            <div class="enrich-stat">
              <div class="enrich-stat-val">${ENRICH.enriched.size}</div>
              <div class="enrich-stat-lbl">Enriched</div>
            </div>
            <div class="enrich-stat">
              <div class="enrich-stat-val">${ENRICH.data.length - ENRICH.enriched.size}</div>
              <div class="enrich-stat-lbl">Pending</div>
            </div>
            <div class="enrich-stat">
              <div class="enrich-stat-val">${ENRICH.data.length > 0 ? Math.round(ENRICH.enriched.size / ENRICH.data.length * 100) : 0}%</div>
              <div class="enrich-stat-lbl">Complete</div>
            </div>
          </div>
          <div class="enrich-progress-bar">
            <div class="enrich-progress-fill" style="width:${ENRICH.data.length > 0 ? Math.round(ENRICH.enriched.size / ENRICH.data.length * 100) : 0}%"></div>
          </div>
        </div>
      </div>
    `;
    enrichWire();
  }

  function enrichRowHtml(txn) {
    const done = ENRICH.enriched.has(txn.id);
    const e = txn.enriched;
    const amtCls = txn.amount < 0 ? "neg" : "pos";
    const amtStr = (txn.amount < 0 ? "-" : "+") + "$" + Math.abs(txn.amount).toFixed(2);

    if (done && e) {
      const catColor = enrichCatColor(e.category, e.categoryGroup);
      const logo = enrichLogoHtml(e);
      const extraChips = [
        e.isRecurring ? `<span class="enrich-chip enrich-chip--flag">Recurring</span>` : "",
        e.isEcommerce ? `<span class="enrich-chip enrich-chip--flag">E-commerce</span>` : "",
      ].join("");
      const locationHtml = e.location ? `
              <span class="enrich-meta-item">
                <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M8 2a4 4 0 0 1 4 4c0 3-4 8-4 8S4 9 4 6a4 4 0 0 1 4-4z"/><circle cx="8" cy="6" r="1.5" fill="currentColor" stroke="none"/></svg>
                ${escapeHtml(e.location)}
              </span>` : "";
      const websiteHost = e.website ? e.website.replace(/^https?:\/\//, "").replace(/\/$/, "") : null;
      const websiteHtml = websiteHost ? `
              <span class="enrich-meta-item">
                <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 2c-2 2-2 8 0 12M8 2c2 2 2 8 0 12M2 8h12"/></svg>
                <a class="enrich-meta-website" href="${escapeHtml(e.website)}" target="_blank" rel="noopener noreferrer">${escapeHtml(websiteHost)}</a>
              </span>` : "";
      const confidence = Math.round(e.confidence || e.categoryScore || 0);
      return `
        <div class="enrich-row enrich-row--done" data-txn-id="${escapeHtml(txn.id)}">
          <div class="enrich-row-logo">${logo}</div>
          <div class="enrich-row-body">
            <div class="enrich-row-top">
              <div class="enrich-row-name">${escapeHtml(e.name)}</div>
              <div class="enrich-row-amount ${amtCls}">${amtStr}</div>
            </div>
            <div class="enrich-row-chips">
              ${e.categoryGroup ? `<span class="enrich-chip enrich-chip--cat" style="--chip-color:${catColor}">${escapeHtml(e.categoryGroup)}</span>` : ""}
              ${e.category ? `<span class="enrich-chip enrich-chip--sub">${escapeHtml(e.category)}</span>` : ""}
              ${extraChips}
            </div>
            <div class="enrich-row-meta">
              ${locationHtml}
              ${websiteHtml}
              <span class="enrich-meta-item enrich-meta-date">${escapeHtml(txn.date)}</span>
            </div>
            <div class="enrich-row-raw-label">
              <span class="enrich-label-raw">RAW</span>
              <code class="enrich-raw-text">${escapeHtml(txn.raw)}</code>
            </div>
            <div class="enrich-confidence">
              <span class="enrich-confidence-label">Confidence</span>
              <div class="enrich-confidence-bar"><div class="enrich-confidence-fill" style="width:${confidence}%"></div></div>
              <span class="enrich-confidence-pct">${confidence}%</span>
            </div>
          </div>
        </div>
      `;
    }

    // Raw (un-enriched) state
    return `
      <div class="enrich-row enrich-row--raw" data-txn-id="${escapeHtml(txn.id)}">
        <div class="enrich-row-logo enrich-row-logo--blank">
          <svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="20" fill="#e5e7eb"/><text x="20" y="26" text-anchor="middle" font-size="15" fill="#9ca3af">?</text></svg>
        </div>
        <div class="enrich-row-body">
          <div class="enrich-row-top">
            <code class="enrich-raw-big">${escapeHtml(txn.raw)}</code>
            <div class="enrich-row-amount ${amtCls}">${amtStr}</div>
          </div>
          <div class="enrich-row-chips">
            <span class="enrich-chip enrich-chip--unknown">Category unknown</span>
            <span class="enrich-chip enrich-chip--unknown">Merchant unknown</span>
          </div>
          <div class="enrich-row-meta">
            <span class="enrich-meta-item enrich-meta-date">${escapeHtml(txn.date)}</span>
          </div>
        </div>
        <button class="enrich-btn-row" data-enrich-id="${escapeHtml(txn.id)}" title="Enrich this transaction">
          <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M10 3v14M3 10h14"/></svg>
          Enrich
        </button>
      </div>
    `;
  }

  function enrichWire() {
    const body = $("uc-body");
    if (!body) return;

    body.querySelectorAll("[data-enrich-id]").forEach(btn => {
      btn.addEventListener("click", () => enrichOne(btn.dataset.enrichId));
    });

    const allBtn = document.getElementById("enrich-all");
    if (allBtn) allBtn.addEventListener("click", () => enrichAll());

    const resetBtn = document.getElementById("enrich-reset");
    if (resetBtn) resetBtn.addEventListener("click", () => {
      ENRICH.enriched.clear();
      enrichRender();
    });
  }

  function enrichOne(id) {
    const row = document.querySelector(`[data-txn-id="${CSS.escape(id)}"]`);
    if (!row || ENRICH.enriched.has(id)) return;

    // Loading shimmer
    row.classList.add("enrich-row--loading");
    const btn = row.querySelector("[data-enrich-id]");
    if (btn) { btn.disabled = true; btn.textContent = "Enriching…"; }

    fetch("/usecases/enrichment/action", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "enrich", params: { ids: [id] } }),
    })
      .then(r => r.json())
      .then(d => {
        const result = (d.transactions || []).find(t => t.id === id);
        if (result && result.enriched) {
          const idx = ENRICH.data.findIndex(t => t.id === id);
          if (idx !== -1) ENRICH.data[idx] = result;
          ENRICH.enriched.add(id);
          enrichRender();
          const enriched = document.querySelector(`[data-txn-id="${CSS.escape(id)}"]`);
          if (enriched) enriched.scrollIntoView({ behavior: "smooth", block: "nearest" });
          return;
        }
        const errMsg = d.error
          ? d.error + (d.detail ? " — " + (typeof d.detail === "string" ? d.detail : JSON.stringify(d.detail)) : "")
          : "No enrichment returned";
        throw new Error(errMsg);
      })
      .catch(err => {
        row.classList.remove("enrich-row--loading");
        if (btn) { btn.disabled = false; btn.textContent = "Enrich"; }
        const existing = row.querySelector(".enrich-row-error");
        if (existing) existing.remove();
        const msg = document.createElement("div");
        msg.className = "enrich-row-error";
        msg.textContent = String(err.message || err);
        row.appendChild(msg);
      });
  }

  function enrichAll() {
    const pending = ENRICH.data.filter(t => !ENRICH.enriched.has(t.id));
    if (!pending.length) return;

    // Mark all pending rows as loading
    pending.forEach(t => {
      const row = document.querySelector(`[data-txn-id="${CSS.escape(t.id)}"]`);
      if (row) {
        row.classList.add("enrich-row--loading");
        const btn = row.querySelector("[data-enrich-id]");
        if (btn) { btn.disabled = true; btn.textContent = "Enriching…"; }
      }
    });

    fetch("/usecases/enrichment/action", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "enrich", params: { ids: pending.map(t => t.id) } }),
    })
      .then(r => r.json())
      .then(d => {
        const byId = {};
        (d.transactions || []).forEach(t => { byId[t.id] = t; });
        const failedIds = new Set(d.failedIds || []);
        const errMsg = d.error
          ? d.error + (d.detail ? " — " + (typeof d.detail === "string" ? d.detail : JSON.stringify(d.detail)) : "")
          : null;

        pending.forEach((t, i) => {
          const result = byId[t.id];
          if (result && result.enriched) {
            // Stagger reveal for visual delight
            setTimeout(() => {
              const idx = ENRICH.data.findIndex(x => x.id === t.id);
              if (idx !== -1) ENRICH.data[idx] = result;
              ENRICH.enriched.add(t.id);
              enrichRender();
            }, i * 150);
            return;
          }
          // Row was not returned — surface the error inline
          const row = document.querySelector(`[data-txn-id="${CSS.escape(t.id)}"]`);
          if (!row) return;
          row.classList.remove("enrich-row--loading");
          const btn = row.querySelector("[data-enrich-id]");
          if (btn) { btn.disabled = false; btn.textContent = "Enrich"; }
          if (errMsg && (failedIds.size === 0 || failedIds.has(t.id))) {
            const existing = row.querySelector(".enrich-row-error");
            if (existing) existing.remove();
            const msg = document.createElement("div");
            msg.className = "enrich-row-error";
            msg.textContent = errMsg;
            row.appendChild(msg);
          }
        });
      })
      .catch(err => {
        pending.forEach(t => {
          const row = document.querySelector(`[data-txn-id="${CSS.escape(t.id)}"]`);
          if (!row) return;
          row.classList.remove("enrich-row--loading");
          const btn = row.querySelector("[data-enrich-id]");
          if (btn) { btn.disabled = false; btn.textContent = "Enrich"; }
        });
        alert("Enrichment failed: " + (err.message || err));
      });
  }

  // ===================== Recurring Transactions Use Case =====================
  // Rendered as a sandboxed iframe pointing to /recurring/index.html.
  // All Recurring UI lives in usecases/recurring/ — edit there to change the look.

  function renderRecurring() {
    _renderCachedWebview('recurring', 'recurring-webview-frame', _appPath('/recurring/index.html'), 'Recurring Transactions');
  }

  // ===================== Payment Success Indicator Use Case =====================
  // Rendered as a sandboxed iframe pointing to /psi/index.html.
  // All PSI UI lives in usecases/psi/ — edit there to change the look.

  function renderPsi() {
    _renderCachedWebview('psi', 'psi-webview-frame', _appPath('/psi/index.html'), 'Payment Success Indicator');
  }

  // ===================== BIN Lookup Use Case =====================
  // Renders a beautifully animated payment card annotated with all the
  // data returned by the Mastercard BIN Resource Lookup API.

  const BIN = { bin: "543210", card: null, loading: false };
  const BIN_DB = { status: "idle", count: 0, loadedAt: null, error: null, searchQuery: "", results: [], searching: false, expandedIdx: null, page: 1, pages: 0, total: 0, persisted: false };
  let BIN_TAB = "lookup"; // "lookup" | "batch"

  const BIN_PRESET_OPTIONS = [
    { value: "543210", label: "543210 — Buckeye State Credit Union (US)" },
    { value: "111102", label: "111102 — Arab Bank PLC (JO)" },
    { value: "356600", label: "356600 — Credencial Argentina SA (AR)" },
    { value: "520000", label: "520000 — Orange Bank (FR)" },
    { value: "541111", label: "541111 — Entropay Limited (CH)" },
  ];

  function renderBinLookup() {
    _renderCachedWebview('bin_lookup', 'binlookup-webview-frame', _appPath('/bin_lookup/index.html'), 'BIN Lookup');
  }

  function _binLookupPanelHtml() {
    return `
      <div class="bin-form-row">
        <div class="bin-field">
          <label for="bin-select">BIN / Issuer</label>
          <select id="bin-select">
            ${BIN_PRESET_OPTIONS.map(o =>
              `<option value="${escapeHtml(o.value)}"${o.value === BIN.bin ? " selected" : ""}>${escapeHtml(o.label)}</option>`
            ).join("")}
          </select>
        </div>
        <button class="bin-lookup-btn" id="bin-lookup-btn"${BIN.loading ? " disabled" : ""}>
          ${BIN.loading
            ? `<span class="psi-spinner"></span>Looking up…`
            : `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" style="width:15px;height:15px;flex-shrink:0"><circle cx="9" cy="9" r="6"/><path d="M15 15l3 3" stroke-linecap="round"/></svg>Look Up Card`}
        </button>
      </div>
      <div class="bin-scene" id="bin-scene">
        ${BIN.card ? binSceneHtml(BIN.card) : ""}
      </div>`;
  }

  function binEmptySceneHtml() {
    return `
      <div class="bin-card-wrap" id="bin-card-wrap">
        <div class="bin-card bin-card--empty">
          <div class="bin-card-gloss"></div>
          <div class="bin-card-inner">
            <div class="bin-card-top-row">
              <div class="bin-issuer-line">SELECT A BIN TO BEGIN</div>
              ${_binContactlessSvg()}
            </div>
            <div class="bin-chip-row">${_binChipSvg()}</div>
            <div class="bin-number-row"><span class="bin-num-placeholder">•••• •••• •••• ••••</span></div>
            <div class="bin-card-footer-row">
              <div><div class="bin-card-sublabel">CARD HOLDER</div><div class="bin-card-name">VALUED CUSTOMER</div></div>
              <div><div class="bin-card-sublabel">EXPIRES</div><div class="bin-card-expiry">••/••</div></div>
              <div class="bin-card-netlogo"></div>
            </div>
          </div>
        </div>
      </div>
      <p class="bin-empty-hint">Choose a BIN above and click <strong>Look Up Card</strong>.</p>`;
  }

  function binSceneHtml(card) {
    const grad = `linear-gradient(135deg, ${escapeHtml(card.color1)} 0%, ${escapeHtml(card.color2)} 100%)`;
    const funding = (card.fundingSource || "").toLowerCase();
    const fundingLabel = { credit: "Credit", debit: "Debit", prepaid: "Prepaid", none: "None" }[funding] || card.fundingSource || "—";
    const clipPath = _binCardClipPath(funding);
    return `
      <div class="bin-annotated-layout">
        <!-- Left callouts: Issuer · Brand · ICA -->
        <div class="bin-callouts bin-callouts--left">
          ${_binCallout("Issuer",   escapeHtml(card.issuerName),  "left",  0)}
          ${_binCallout("Brand",    escapeHtml(card.brandLabel),  "left",  1)}
          ${card.ica ? _binCallout("ICA", escapeHtml(card.ica),  "left",  2) : ""}
        </div>

        <!-- Card -->
        <div class="bin-card-wrap" id="bin-card-wrap" style="opacity:0;transform:translateY(18px) scale(0.97)">
          <div class="bin-card" style="background:${grad};${clipPath ? 'clip-path:' + clipPath : ''}">
            <div class="bin-card-gloss"></div>
            <div class="bin-card-inner">
              <div class="bin-card-top-row">
                <div class="bin-issuer-line">${escapeHtml(card.displayName.toUpperCase())}</div>
                ${_binContactlessSvg()}
              </div>
              <div class="bin-chip-row">${_binChipSvg()}</div>
              <div class="bin-number-row" id="bin-number-row">${_binNumberHtml(card.binNum)}</div>
              <div class="bin-card-footer-row">
                <div class="bin-card-product-badge">${escapeHtml(card.product)}</div>
                <div class="bin-card-country-tag">${card.flagEmoji ? card.flagEmoji + " " : ""}${escapeHtml(card.countryName)}</div>
                <div class="bin-card-netlogo">${_binNetworkSvg(card.network)}</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right callouts: Country · Funding · Segment -->
        <div class="bin-callouts bin-callouts--right">
          ${_binCallout("Country",  (card.flagEmoji ? card.flagEmoji + " " : "") + escapeHtml(card.countryName), "right", 0)}
          ${_binCallout("Funding",  fundingLabel, "right", 1, funding ? "bin-callout-value--" + funding : "")}
          ${_binCallout("Segment",  escapeHtml(card.consumerLabel), "right", 2)}
        </div>
      </div>

      <!-- Capabilities grid -->
      <div class="bin-capability-grid" id="bin-cap-grid">
        ${card.productCode ? _binCapChip("Product", card.productCode + " — " + card.product, "neutral") : _binCapChip("Product", card.product, "neutral")}
        ${card.billingCurrency ? _binCapChip("Billing Currency", card.billingCurrency, "neutral") : ""}
        ${_binCapChip("Local Use",   card.localUse        ? "Domestic Only"          : "International",  card.localUse        ? "warn" : "ok")}
        ${_binCapChip("MoneySend",   card.moneySend       ? "Enabled"                : "Not Enabled",    card.moneySend       ? "ok"   : "dim")}
        ${_binCapChip("Fast Fund",   card.fastFund        ? (card.fastFundDomesticOnly ? "Domestic Only" : "Full Support") : "Not Supported", card.fastFund ? "ok" : "dim")}
        ${_binCapChip("DCC",         card.dccEnabled      ? "Supported"              : "Not Supported",  card.dccEnabled      ? "ok"   : "dim")}
        ${card.authorizationOnly ? _binCapChip("Auth Only", "Yes", "warn") : _binCapChip("Auth Only", "No", "")}
        ${funding === 'prepaid' ? _binCapChip("Reloadable", card.nonReloadable ? "No" : "Yes", card.nonReloadable ? "warn" : "ok") : (card.nonReloadable ? _binCapChip("Non-Reloadable", "Yes", "warn") : "")}
        ${card.governmentRange       ? _binCapChip("Government",      "Public Sector","info") : ""}
        ${_binCapChip("Smart Data",  card.smartData       ? "Enrolled"               : "Not Enrolled",   card.smartData       ? "ok"   : "dim")}
        ${card.isToken               ? _binCapChip("Token BIN",       "Network Token","info") : ""}
      </div>

      <!-- Mobile chip grid (shown only on narrow screens) -->
      <div class="bin-chips-mobile">
        ${_binChip("Issuer",    card.issuerName, 0)}
        ${_binChip("Network",   card.network,    1)}
        ${_binChip("Country",   (card.flagEmoji ? card.flagEmoji + " " : "") + card.countryName, 2)}
        ${_binChip("Product",   card.product,    3)}
        ${_binChip("Segment",   card.consumerLabel, 4)}
        ${_binChip("Funding",   fundingLabel,    5)}
        ${_binChip("BIN",       card.binNum,     6)}
        ${card.productCode ? _binChip("Product Code", card.productCode, 7) : ""}
      </div>

    `;
  }

  // ─── HTML helpers ────────────────────────────────────────────────────────

  function _binCallout(label, value, side, idx, valueCls) {
    return `
      <div class="bin-callout bin-callout--${side}" data-co-idx="${idx}" style="opacity:0">
        <div class="bin-callout-text">
          <div class="bin-callout-label">${escapeHtml(label)}</div>
          <div class="bin-callout-value${valueCls ? " " + valueCls : ""}">${value}</div>
        </div>
        <div class="bin-callout-line"></div>
        <div class="bin-callout-dot"></div>
      </div>`;
  }

  function _binChip(label, value, idx) {
    return `
      <div class="bin-chip" data-chip-idx="${idx}" style="opacity:0;transform:translateY(10px)">
        <div class="bin-chip-label">${escapeHtml(label)}</div>
        <div class="bin-chip-value">${value}</div>
      </div>`;
  }

  function _binCapChip(label, value, modifier) {
    return `<div class="bin-cap-chip${modifier ? " bin-cap-chip--" + modifier : ""}" data-cap-idx style="opacity:0;transform:translateY(12px) scale(0.95)">
      <div class="bin-cap-label">${escapeHtml(label)}</div>
      <div class="bin-cap-value">${escapeHtml(value)}</div>
    </div>`;
  }

  function _binNumberHtml(bin) {
    const padded = String(bin).padEnd(16, "x");
    const masked = 16 - bin.length;
    let mIdx = 0;
    const groups = [padded.slice(0,4), padded.slice(4,8), padded.slice(8,12), padded.slice(12,16)];
    return groups.map((grp, gi) => {
      const chars = grp.split("").map((ch, ci) => {
        const pos = gi * 4 + ci;
        const real = pos < bin.length;
        if (real) {
          return `<span class="bin-digit bin-digit--real" data-pos="${pos}">${ch}</span>`;
        } else {
          const n = (mIdx++ % 9) + 1;
          return `<span class="bin-digit bin-digit--masked" data-pos="${pos}" data-n="${n}">${n}</span>`;
        }
      }).join("");
      return `<span class="bin-grp">${chars}</span>`;
    }).join('<span class="bin-grp-space"> </span>');
  }

  function _binNetworkSvg(network) {
    if (network === "Mastercard") return `
      <svg viewBox="0 0 52 34" class="bin-net-svg" aria-label="Mastercard">
        <circle cx="19" cy="17" r="13" fill="#eb001b" opacity="0.93"/>
        <circle cx="33" cy="17" r="13" fill="#f79e1b" opacity="0.93"/>
        <path d="M26 7a13 13 0 0 1 0 20A13 13 0 0 1 26 7z" fill="#ff5f00" opacity="0.86"/>
      </svg>`;
    if (network === "Visa") return `
      <svg viewBox="0 0 72 24" class="bin-net-svg" aria-label="Visa">
        <text x="1" y="20" font-family="Arial,sans-serif" font-size="22" font-style="italic" font-weight="900" fill="white" letter-spacing="-1">VISA</text>
      </svg>`;
    if (network === "Amex") return `
      <svg viewBox="0 0 72 24" class="bin-net-svg" aria-label="American Express">
        <text x="1" y="19" font-family="Arial,sans-serif" font-size="14" font-weight="700" fill="white" letter-spacing="1">AMEX</text>
      </svg>`;
    if (network === "Discover") return `
      <svg viewBox="0 0 72 24" class="bin-net-svg" aria-label="Discover">
        <text x="1" y="19" font-family="Arial,sans-serif" font-size="11" font-weight="700" fill="white">DISCOVER</text>
      </svg>`;
    return `<svg viewBox="0 0 72 24" class="bin-net-svg"><text x="1" y="19" font-family="Arial,sans-serif" font-size="11" fill="white">${escapeHtml(network)}</text></svg>`;
  }

  function _binChipSvg() {
    return `<svg viewBox="0 0 44 34" class="bin-chip-svg" aria-hidden="true">
      <rect width="44" height="34" rx="5" fill="#c8a830"/>
      <rect x="3" y="3" width="38" height="28" rx="4" fill="#e2bb44" stroke="#a88820" stroke-width="0.6"/>
      <line x1="3"  y1="12" x2="41" y2="12" stroke="#a88820" stroke-width="0.6"/>
      <line x1="3"  y1="22" x2="41" y2="22" stroke="#a88820" stroke-width="0.6"/>
      <line x1="15" y1="3"  x2="15" y2="31" stroke="#a88820" stroke-width="0.6"/>
      <line x1="29" y1="3"  x2="29" y2="31" stroke="#a88820" stroke-width="0.6"/>
      <rect x="15" y="12" width="14" height="10" rx="1.5" fill="#c8a420" stroke="#a88820" stroke-width="0.4"/>
    </svg>`;
  }

  function _binCardClipPath(funding) {
    // Card dimensions: 342×215, border-radius 17
    // 6mm ≈ 23px, 3mm ≈ 11.5px
    const W = 342, H = 215, R = 17;
    const ny = H / 2;     // 107.5 — notch centre Y
    const nh = 11.5;      // half-height of opening (3mm)
    const nd = 5.75;      // depth into card (1.5mm — halved from 3mm)
    const nr = 4;         // credit corner radius (1mm)
    const yt = ny - nh;   // 96 — top of notch
    const yb = ny + nh;   // 119 — bottom of notch
    const nx = W - nd;    // inner wall X
    const base = `M ${R} 0 L ${W-R} 0 Q ${W} 0 ${W} ${R} `;
    const tail = ` L ${W} ${H-R} Q ${W} ${H} ${W-R} ${H} L ${R} ${H} Q 0 ${H} 0 ${H-R} L 0 ${R} Q 0 0 ${R} 0 Z`;
    let notch = '';
    if (funding === 'debit') {
      // Circular arc — same half-height (35.3px) but depth halved to 5.75px.
      // dR derived from: depth = dR - sqrt(dR²-h²)  →  dR = (h²+depth²)/(2*depth)
      const cy2 = 150, dHalf = 35.3, dDepth = 5.75;
      const dR = (dHalf*dHalf + dDepth*dDepth) / (2*dDepth); // ≈ 111.3
      const dyt = (cy2 - dHalf).toFixed(1);
      const dyb = (cy2 + dHalf).toFixed(1);
      notch = `L ${W} ${dyt} A ${dR.toFixed(1)} ${dR.toFixed(1)} 0 0 0 ${W} ${dyb}`;
    } else if (funding === 'credit') {
      // Trapezoid converging inward: depth halved to 5.75px
      const ccy = 150, cnd = 5.75, cs = 54.25;
      const citx = W - cnd;
      const dyOff = cnd / Math.tan(72 * Math.PI / 180);
      const eyT = ccy - cs / 2;
      const eyB = ccy + cs / 2;
      const iyT = eyT + dyOff;
      const iyB = eyB - dyOff;
      notch = `L ${W} ${eyT.toFixed(1)} L ${citx} ${iyT.toFixed(1)} L ${citx} ${iyB.toFixed(1)} L ${W} ${eyB.toFixed(1)}`;
    } else if (funding === 'prepaid') {
      // Scalene triangle: depth halved to 5.75px
      const pcy = 150, pnd = 5.75, pOpen = 70;
      const py1 = pcy - pOpen / 2;
      const py2 = pcy + pOpen / 2;
      const pA = (-pOpen + Math.sqrt(4*pOpen*pOpen - 9*pnd*pnd)) / 3;
      notch = `L ${W} ${py1.toFixed(1)} L ${(W-pnd).toFixed(1)} ${(py1+pA).toFixed(1)} L ${W} ${py2.toFixed(1)}`;
    } else {
      return '';
    }
    return `path('${base}${notch}${tail}')`;
  }

  function _binContactlessSvg() {
    return `<svg viewBox="0 0 24 24" class="bin-contactless-svg" fill="none" aria-hidden="true">
      <path d="M12 5a7 7 0 0 1 0 14" stroke="rgba(255,255,255,0.45)" stroke-width="2" stroke-linecap="round"/>
      <path d="M12 8.5a3.5 3.5 0 0 1 0 7" stroke="rgba(255,255,255,0.45)" stroke-width="2" stroke-linecap="round"/>
      <circle cx="12" cy="12" r="1.5" fill="rgba(255,255,255,0.45)"/>
    </svg>`;
  }

  // ─── Animation ───────────────────────────────────────────────────────────

  function binAnimateIn() {
    // 1. Card glides smoothly into view — no spring overshoot
    const wrap = document.getElementById("bin-card-wrap");
    if (wrap) {
      wrap.style.opacity = "0";
      wrap.style.transform = "translateY(18px) scale(0.97)";
      wrap.style.transition = "none";
      void wrap.offsetWidth;
      wrap.style.transition = "opacity 0.5s ease, transform 0.5s cubic-bezier(0.22,1,0.36,1)";
      wrap.style.opacity = "1";
      wrap.style.transform = "translateY(0) scale(1)";
    }
    // 2. BIN digits appear left-to-right, smoothly
    document.querySelectorAll("#bin-number-row .bin-digit--real").forEach((el, i) => {
      el.style.opacity = "0";
      el.style.transform = "translateY(6px)";
      setTimeout(() => {
        el.style.transition = "opacity 0.2s ease, transform 0.2s ease";
        el.style.opacity = "1";
        el.style.transform = "translateY(0)";
      }, 220 + i * 45);
    });
    // 3. Masked digits cycle through numbers then settle
    const maskedEls = document.querySelectorAll("#bin-number-row .bin-digit--masked");
    maskedEls.forEach((el, i) => {
      const finalN = parseInt(el.dataset.n, 10);
      const delay = 280 + i * 40;
      const cycles = 6;
      let tick = 0;
      el.style.opacity = "0";
      setTimeout(() => {
        el.style.transition = "opacity 0.15s ease";
        el.style.opacity = "1";
        const interval = setInterval(() => {
          tick++;
          el.textContent = ((tick % 9) + 1).toString();
          if (tick >= cycles) {
            clearInterval(interval);
            el.textContent = finalN.toString();
          }
        }, 60);
      }, delay);
    });
    // 4. Side callouts slide in
    document.querySelectorAll(".bin-callout").forEach(el => {
      const idx = parseInt(el.dataset.coIdx || "0");
      const left = el.classList.contains("bin-callout--left");
      el.style.opacity = "0";
      el.style.transform = `translateX(${left ? -18 : 18}px)`;
      setTimeout(() => {
        el.style.transition = "opacity 0.38s ease, transform 0.42s cubic-bezier(0.22,1,0.36,1)";
        el.style.opacity = "1";
        el.style.transform = "translateX(0)";
      }, 480 + idx * 90);
    });
    // 4. Mobile chips
    document.querySelectorAll(".bin-chip").forEach(el => {
      const idx = parseInt(el.dataset.chipIdx || "0");
      el.style.opacity = "0";
      el.style.transform = "translateY(10px)";
      setTimeout(() => {
        el.style.transition = "opacity 0.35s ease, transform 0.35s ease";
        el.style.opacity = "1";
        el.style.transform = "translateY(0)";
      }, 380 + idx * 75);
    });
    // 5. Capability chips cascade in
    document.querySelectorAll(".bin-cap-chip").forEach((el, i) => {
      el.style.opacity = "0";
      el.style.transform = "translateY(12px) scale(0.95)";
      setTimeout(() => {
        el.style.transition = "opacity 0.30s ease, transform 0.35s cubic-bezier(0.34,1.1,0.64,1)";
        el.style.opacity = "1";
        el.style.transform = "translateY(0) scale(1)";
      }, 700 + i * 55);
    });
  }

  // ─── BIN Ranges DB panel ─────────────────────────────────────────────────

  function binDbStatusHtml() {
    const s = BIN_DB.status;
    if (s === "loaded") {
      const ago = BIN_DB.loadedAt ? _binTimeAgo(BIN_DB.loadedAt) : "";
      const diskNote = BIN_DB.persisted
        ? ` <span class="bin-db-badge-disk" title="Restored from local database"><svg width="10" height="10" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="10" cy="6" rx="7" ry="3"/><path d="M3 6v4c0 1.657 3.134 3 7 3s7-1.343 7-3V6"/><path d="M3 10v4c0 1.657 3.134 3 7 3s7-1.343 7-3v-4"/></svg> Saved locally</span>`
        : "";
      return `<span class="bin-db-badge bin-db-badge--ok">
        <svg width="10" height="10" viewBox="0 0 10 10"><circle cx="5" cy="5" r="4.5" fill="#1f9d55"/></svg>
        ${BIN_DB.count.toLocaleString()} ranges loaded${ago ? " · " + ago : ""}
      </span>${diskNote}`;
    }
    if (s === "loading") {
      return `<span class="bin-db-badge bin-db-badge--loading">
        <span class="psi-spinner" style="width:10px;height:10px;border-width:1.5px"></span> Loading…
      </span>`;
    }
    if (s === "error") {
      return `<span class="bin-db-badge bin-db-badge--err">
        <svg width="10" height="10" viewBox="0 0 10 10"><circle cx="5" cy="5" r="4.5" fill="#eb001b"/></svg>
        Error${BIN_DB.error ? ": " + escapeHtml(BIN_DB.error) : ""}
      </span>`;
    }
    return `<span class="bin-db-badge bin-db-badge--idle">
      <svg width="10" height="10" viewBox="0 0 10 10"><circle cx="5" cy="5" r="4.5" fill="#aaa"/></svg>
      Not loaded
    </span>`;
  }

  function _binDbPaginationHtml() {
    if (BIN_DB.pages <= 1) return "";
    const p = BIN_DB.page, pp = BIN_DB.pages;
    // Build page number buttons — always show first, last, and a window around current
    const btns = [];
    const window = 2;
    let prev = null;
    for (let i = 1; i <= pp; i++) {
      if (i === 1 || i === pp || (i >= p - window && i <= p + window)) {
        if (prev !== null && i > prev + 1) btns.push(null); // ellipsis
        btns.push(i);
        prev = i;
      }
    }
    const pageNums = btns.map(i =>
      i === null
        ? `<span class="bin-db-pg-ellipsis">…</span>`
        : `<button class="bin-db-pg-btn${i === p ? " bin-db-pg-btn--active" : ""}" data-pg="${i}">${i}</button>`
    ).join("");
    return `
      <div class="bin-db-pagination">
        <button class="bin-db-pg-btn bin-db-pg-nav" data-pg="${p - 1}"${p <= 1 ? " disabled" : ""}>
          <svg width="12" height="12" viewBox="0 0 12 12"><path d="M8 2L4 6l4 4" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        ${pageNums}
        <button class="bin-db-pg-btn bin-db-pg-nav" data-pg="${p + 1}"${p >= pp ? " disabled" : ""}>
          <svg width="12" height="12" viewBox="0 0 12 12"><path d="M4 2l4 4-4 4" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <span class="bin-db-pg-info">${BIN_DB.total.toLocaleString()} result${BIN_DB.total === 1 ? "" : "s"}</span>
      </div>`;
  }

  function binDbResultsHtml() {
    if (BIN_DB.searching) {
      return `<div class="bin-db-results-placeholder"><span class="psi-spinner"></span> Searching…</div>`;
    }
    if (!BIN_DB.searchQuery) return "";
    if (!BIN_DB.results.length) {
      return `<div class="bin-db-results-placeholder">No results for <strong>${escapeHtml(BIN_DB.searchQuery)}</strong></div>`;
    }
    const rows = BIN_DB.results.map((r, i) => {
      const country = r.country && typeof r.country === "object" ? r.country.name : String(r.country || "—");
      const expanded = BIN_DB.expandedIdx === i;
      const low = r.lowAccountRange || "";
      const high = r.highAccountRange || "";
      const range = low === high ? low : `${low}–${high.slice(-6)}`;
      return `
        <tr class="bin-db-row${expanded ? " bin-db-row--open" : ""}" data-idx="${i}">
          <td class="bin-db-cell bin-db-cell--bin">${escapeHtml(String(r.binNum || ""))}</td>
          <td class="bin-db-cell">${escapeHtml(r.customerName || "—")}</td>
          <td class="bin-db-cell">${escapeHtml(country)}</td>
          <td class="bin-db-cell">${escapeHtml(r.acceptanceBrand || "—")}</td>
          <td class="bin-db-cell">${escapeHtml(r.fundingSource || "—")}</td>
          <td class="bin-db-cell bin-db-cell--expand">${expanded ? "▲" : "▼"}</td>
        </tr>
        ${expanded ? `<tr class="bin-db-expand-row">
          <td colspan="6">
            <div class="bin-db-expand-body">
              <div class="bin-db-expand-grid">
                ${_binDbDetailPair("Range", escapeHtml(range))}
                ${_binDbDetailPair("BIN Length", escapeHtml(String(r.binLength || "—")))}
                ${_binDbDetailPair("Product", escapeHtml(r.productDescription || "—"))}
                ${_binDbDetailPair("Product Code", escapeHtml(r.productCode || "—"))}
                ${_binDbDetailPair("ICA", escapeHtml(String(r.ica || "—")))}
                ${_binDbDetailPair("Country Code", escapeHtml(r.country && r.country.alpha3 ? r.country.alpha3 : "—"))}
                ${_binDbDetailPair("Funding", escapeHtml(r.fundingSource || "—"))}
                ${_binDbDetailPair("Consumer Type", escapeHtml(r.consumerType || "—"))}
                ${_binDbDetailPair("Prepaid", escapeHtml(r.anonymousPrepaidIndicator || "—"))}
                ${_binDbDetailPair("Smart Data", escapeHtml(String(r.smartDataEnabled ?? "—")))}
                ${_binDbDetailPair("Local Use", escapeHtml(String(r.localUse ?? "—")))}
                ${_binDbDetailPair("Auth Only", escapeHtml(String(r.authorizationOnly ?? "—")))}
                ${_binDbDetailPair("Govt Range", escapeHtml(String(r.governmentRange ?? "—")))}
                ${_binDbDetailPair("Program", escapeHtml(r.programName || "—"))}
                ${_binDbDetailPair("Vertical", escapeHtml(r.vertical || "—"))}
              </div>
              <div class="bin-db-expand-actions">
                <button class="bin-db-visualize-btn" data-visualize-bin="${escapeHtml(String(r.binNum || ""))}" data-visualize-label="${escapeHtml((r.binNum ? String(r.binNum) : "") + (r.customerName ? " — " + r.customerName : "") + (r.country && r.country.alpha3 ? " (" + r.country.alpha3 + ")" : ""))}">
                  <svg width="14" height="14" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" style="flex-shrink:0"><rect x="2" y="5" width="16" height="11" rx="2"/><path d="M2 9h16" stroke-linecap="round"/><circle cx="6" cy="13" r="1" fill="currentColor" stroke="none"/></svg>
                  Visualize as Card
                </button>
              </div>
            </div>
          </td>
        </tr>` : ""}
      `;
    }).join("");
    const topPagination = _binDbPaginationHtml();
    const bottomPagination = BIN_DB.pages > 1 ? `<div class="bin-db-results-footer">${_binDbPaginationHtml()}</div>` : "";
    return `
      ${topPagination}
      <table class="bin-db-table">
        <thead><tr>
          <th>BIN</th><th>Issuer</th><th>Country</th><th>Brand</th><th>Funding</th><th></th>
        </tr></thead>
        <tbody>${rows}</tbody>
      </table>
      ${bottomPagination}`;
  }

  function _binDbDetailPair(label, value) {
    return `<div class="bin-db-detail-pair"><span class="bin-db-detail-label">${label}</span><span class="bin-db-detail-value">${value}</span></div>`;
  }

  function _binTimeAgo(ts) {
    const sec = Math.floor(Date.now() / 1000) - ts;
    if (sec < 60) return "just now";
    if (sec < 3600) return `${Math.floor(sec / 60)}m ago`;
    if (sec < 86400) return `${Math.floor(sec / 3600)}h ago`;
    return `${Math.floor(sec / 86400)}d ago`;
  }

  function binDbPanelHtml() {
    const s = BIN_DB.status;
    const loaded = s === "loaded";
    const loading = s === "loading";
    return `
      <div class="bin-db-panel">
        <div class="bin-db-panel-header">
          <div class="bin-db-panel-title">
            <svg width="14" height="14" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="10" cy="5" rx="7" ry="3"/><path d="M3 5v5c0 1.657 3.134 3 7 3s7-1.343 7-3V5"/><path d="M3 10v5c0 1.657 3.134 3 7 3s7-1.343 7-3v-5"/></svg>
            BIN Ranges Database
          </div>
          <div class="bin-db-panel-actions">
            <a class="bin-db-csv-btn" href="${_appPath('/usecases/binlookup/download-bins')}" download="bin_ranges.csv"
               title="Download all BIN ranges as CSV${loaded ? " (" + BIN_DB.count.toLocaleString() + " rows)" : ""}">
              <svg width="13" height="13" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M10 3v10M6 9l4 4 4-4" stroke-linecap="round" stroke-linejoin="round"/><path d="M3 17h14" stroke-linecap="round"/></svg>
              CSV
            </a>
            <button class="bin-db-load-btn" id="bin-db-load-btn"${loading ? " disabled" : ""}>
              ${loading
                ? `<span class="psi-spinner" style="width:12px;height:12px;border-width:1.5px"></span> Loading…`
                : loaded
                  ? `<svg width="13" height="13" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 10a6 6 0 1 1 12 0" stroke-linecap="round"/><path d="M4 10l-2-2 2-2"/></svg> Reload`
                  : `<svg width="13" height="13" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 10a6 6 0 1 1 12 0" stroke-linecap="round"/><path d="M4 10l-2-2 2-2"/></svg> Load into Studio`}
            </button>
          </div>
        </div>
        <div class="bin-db-status-row" id="bin-db-status-row">${binDbStatusHtml()}</div>
        ${loaded ? `
        <div class="bin-db-search-row">
          <div class="bin-db-search-wrap">
            <svg class="bin-db-search-icon" width="14" height="14" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="9" r="6"/><path d="M15 15l3 3" stroke-linecap="round"/></svg>
            <input class="bin-db-search-input" id="bin-db-search-input" type="text"
              placeholder='Search BIN, issuer, country… or "Exact Issuer Name"'
              value="${escapeHtml(BIN_DB.searchQuery)}" autocomplete="off">
            ${BIN_DB.searchQuery ? `<button class="bin-db-search-clear" id="bin-db-search-clear" title="Clear">✕</button>` : ""}
          </div>
        </div>
        <div class="bin-db-results" id="bin-db-results">${binDbResultsHtml()}</div>
        ` : ""}
      </div>`;
  }

  let _binDbPollTimer = null;

  function binDbWire() {
    // Load button
    const loadBtn = document.getElementById("bin-db-load-btn");
    if (loadBtn) {
      loadBtn.addEventListener("click", async () => {
        const r = await _nativeFetch("/usecases/binlookup/bin-ranges/load", { method: "POST" });
        const d = await r.json();
        if (d.ok || d.message === "Already loading") {
          BIN_DB.status = "loading";
          _binDbRefreshStatus();
          _binDbStartPoll();
        }
      });
    }

    // Search input
    const inp = document.getElementById("bin-db-search-input");
    if (inp) {
      inp.addEventListener("input", _binDbOnSearch);
      inp.addEventListener("keydown", e => { if (e.key === "Escape") { BIN_DB.searchQuery = ""; _binDbRefreshResults(); } });
    }
    const clearBtn = document.getElementById("bin-db-search-clear");
    if (clearBtn) {
      clearBtn.addEventListener("click", () => { BIN_DB.searchQuery = ""; BIN_DB.results = []; _binDbRefreshAll(); });
    }

    // Row expand
    const tbody = document.querySelector(".bin-db-table tbody");
    if (tbody) {
      tbody.addEventListener("click", e => {
        // Visualize-as-card button (inside the expand row)
        const vbtn = e.target.closest("[data-visualize-bin]");
        if (vbtn) {
          e.stopPropagation();
          const bn = vbtn.getAttribute("data-visualize-bin");
          const lbl = vbtn.getAttribute("data-visualize-label") || bn;
          if (bn) _binVisualizeFromBatch(bn, lbl);
          return;
        }
        const row = e.target.closest("tr.bin-db-row");
        if (!row) return;
        const idx = parseInt(row.dataset.idx, 10);
        BIN_DB.expandedIdx = BIN_DB.expandedIdx === idx ? null : idx;
        _binDbRefreshResults();
      });
    }

    // On mount: sync status from server
    _binDbSyncStatus();
  }

  let _binDbSearchTimer = null;
  function _binDbOnSearch(e) {
    BIN_DB.searchQuery = e.target.value;
    BIN_DB.page = 1; // reset to first page on new query
    clearTimeout(_binDbSearchTimer);
    if (!BIN_DB.searchQuery) {
      BIN_DB.results = [];
      BIN_DB.total = 0;
      BIN_DB.pages = 0;
      BIN_DB.expandedIdx = null;
      _binDbRefreshAll();
      return;
    }
    BIN_DB.searching = true;
    _binDbRefreshResults();
    _binDbSearchTimer = setTimeout(() => _binDbExecSearch(1), 250);
  }

  async function _binDbExecSearch(page) {
    const q = BIN_DB.searchQuery;
    if (!q) return;
    const pg = page || BIN_DB.page || 1;
    const r = await _nativeFetch(`/usecases/binlookup/bin-ranges/search?q=${encodeURIComponent(q)}&page=${pg}`);
    const d = await r.json();
    if (BIN_DB.searchQuery !== q) return; // stale
    BIN_DB.searching = false;
    BIN_DB.expandedIdx = null;
    BIN_DB.results = d.results || [];
    BIN_DB.total = d.total || 0;
    BIN_DB.page = d.page || pg;
    BIN_DB.pages = d.pages || 0;
    _binDbRefreshResults();
  }

  function _binDbRefreshStatus() {
    const el = document.getElementById("bin-db-status-row");
    if (el) el.innerHTML = binDbStatusHtml();
    const loadBtn = document.getElementById("bin-db-load-btn");
    if (loadBtn) {
      const loading = BIN_DB.status === "loading";
      const loaded = BIN_DB.status === "loaded";
      loadBtn.disabled = loading;
      loadBtn.innerHTML = loading
        ? `<span class="psi-spinner" style="width:12px;height:12px;border-width:1.5px"></span> Loading…`
        : loaded
          ? `<svg width="13" height="13" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 10a6 6 0 1 1 12 0" stroke-linecap="round"/><path d="M4 10l-2-2 2-2"/></svg> Reload`
          : `<svg width="13" height="13" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 10a6 6 0 1 1 12 0" stroke-linecap="round"/><path d="M4 10l-2-2 2-2"/></svg> Load into MSS`;
    }
  }

  function _binDbRefreshResults() {
    const el = document.getElementById("bin-db-results");
    if (el) el.innerHTML = binDbResultsHtml();
    // re-wire row expand + visualize button
    const tbody = el && el.querySelector(".bin-db-table tbody");
    if (tbody) {
      tbody.addEventListener("click", e => {
        const vbtn = e.target.closest("[data-visualize-bin]");
        if (vbtn) {
          e.stopPropagation();
          const bn = vbtn.getAttribute("data-visualize-bin");
          const lbl = vbtn.getAttribute("data-visualize-label") || bn;
          if (bn) _binVisualizeFromBatch(bn, lbl);
          return;
        }
        const row = e.target.closest("tr.bin-db-row");
        if (!row) return;
        const idx = parseInt(row.dataset.idx, 10);
        BIN_DB.expandedIdx = BIN_DB.expandedIdx === idx ? null : idx;
        _binDbRefreshResults();
      });
    }
    // re-wire clear button
    const clearBtn = document.getElementById("bin-db-search-clear");
    if (clearBtn) {
      clearBtn.addEventListener("click", () => { BIN_DB.searchQuery = ""; BIN_DB.results = []; BIN_DB.total = 0; BIN_DB.pages = 0; BIN_DB.page = 1; _binDbRefreshAll(); });
    }
    // re-wire pagination buttons
    el && el.querySelectorAll(".bin-db-pg-btn[data-pg]").forEach(btn => {
      btn.addEventListener("click", async () => {
        if (btn.disabled) return;
        const pg = parseInt(btn.dataset.pg, 10);
        if (isNaN(pg) || pg < 1 || pg > BIN_DB.pages) return;
        BIN_DB.page = pg;
        BIN_DB.expandedIdx = null;
        BIN_DB.searching = true;
        _binDbRefreshResults();
        await _binDbExecSearch(pg);
        // Scroll results area into view
        el.scrollIntoView({ behavior: "smooth", block: "nearest" });
      });
    });
  }

  function _binDbRefreshAll() {
    const tc = document.querySelector(".bin-tab-content");
    if (!tc) { renderBinLookup(); return; }
    tc.innerHTML = binDbPanelHtml();
    binDbWire();
  }

  function _binDbStartPoll() {
    clearInterval(_binDbPollTimer);
    _binDbPollTimer = setInterval(_binDbSyncStatus, 2000);
  }

  async function _binDbSyncStatus() {
    try {
      const r = await _nativeFetch("/usecases/binlookup/bin-ranges/status");
      const d = await r.json();
      const prev = BIN_DB.status;
      BIN_DB.status = d.status;
      BIN_DB.count = d.count;
      BIN_DB.loadedAt = d.loaded_at;
      BIN_DB.error = d.error;
      BIN_DB.persisted = d.persisted || false;
      if (d.status !== "loading") {
        clearInterval(_binDbPollTimer);
        _binDbPollTimer = null;
        if ((prev === "loading" || prev === "idle") && d.status === "loaded") {
          // Update batch tab badge count and re-render tab content
          const tabBatchBtn = document.getElementById("bin-tab-batch");
          if (tabBatchBtn) {
            const badge = tabBatchBtn.querySelector(".bin-tab-badge");
            if (badge) badge.textContent = BIN_DB.count.toLocaleString();
            else tabBatchBtn.insertAdjacentHTML("beforeend", `<span class="bin-tab-badge">${BIN_DB.count.toLocaleString()}</span>`);
          }
          if (BIN_TAB === "batch") {
            const tc = document.querySelector(".bin-tab-content");
            if (tc) { tc.innerHTML = binDbPanelHtml(); binDbWire(); return; }
          }
          renderBinLookup();
          return;
        }
      }
      _binDbRefreshStatus();
    } catch (_) {}
  }

  // ─── Targeted refresh helpers ─────────────────────────────────────────────

  function _binRefreshLookupPanel() {
    // Refreshes only the tab content area without rebuilding the tabs
    const tc = document.querySelector(".bin-tab-content");
    if (!tc) { renderBinLookup(); return; }
    tc.innerHTML = _binLookupPanelHtml();
    binWire();
  }

  // Visualize a batch row as the animated card — switches to the Lookup tab
  // and reuses the existing card visualization code path.
  async function _binVisualizeFromBatch(binNum, label) {
    // Ensure the BIN appears in the select dropdown so the user can see what's loaded
    if (!BIN_PRESET_OPTIONS.some(o => o.value === binNum)) {
      BIN_PRESET_OPTIONS.unshift({ value: binNum, label: label || binNum });
    }
    BIN_TAB = "lookup";
    BIN.bin = binNum;
    BIN.loading = true;
    BIN.card = null;
    renderBinLookup();
    try {
      const r = await _nativeFetch("/usecases/binlookup/action", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "lookup", params: { account_range: binNum } }),
      });
      if (!r.ok) throw new Error(`HTTP ${r.status}: ${r.statusText}`);
      const d = await r.json();
      BIN.loading = false;
      if (d.error) {
        BIN.card = null;
        _binRefreshLookupPanel();
        const scene = document.getElementById("bin-scene");
        if (scene) scene.insertAdjacentHTML("beforeend", `<div class="bin-error-msg">${escapeHtml(String(d.error))}</div>`);
      } else if (!d.found) {
        BIN.card = null;
        _binRefreshLookupPanel();
        const scene = document.getElementById("bin-scene");
        if (scene) scene.insertAdjacentHTML("beforeend", `<div class="bin-notfound-msg">${escapeHtml(d.note || "No matching BIN found.")}</div>`);
      } else {
        BIN.card = d.card;
        _binRefreshLookupPanel();
        requestAnimationFrame(() => setTimeout(binAnimateIn, 30));
      }
    } catch (e) {
      console.error("BIN visualize error:", e);
      BIN.loading = false;
      BIN.card = null;
      _binRefreshLookupPanel();
      const scene = document.getElementById("bin-scene");
      if (scene) scene.insertAdjacentHTML("beforeend", `<div class="bin-error-msg">Error: ${escapeHtml(String(e.message))}</div>`);
    }
  }

  // ─── Wiring ──────────────────────────────────────────────────────────────

  function binWire() {
    const sel = document.getElementById("bin-select");
    if (sel) sel.addEventListener("change", () => { BIN.bin = sel.value; });

    const btn = document.getElementById("bin-lookup-btn");
    if (!btn) return;

    btn.addEventListener("click", async () => {
      const selEl = document.getElementById("bin-select");
      if (selEl) BIN.bin = selEl.value;
      if (!BIN.bin) return;

      BIN.loading = true;
      BIN.card = null;
      _binRefreshLookupPanel();

      try {
        const r = await _nativeFetch("/usecases/binlookup/action", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ action: "lookup", params: { account_range: BIN.bin } }),
        });
        if (!r.ok) {
          throw new Error(`HTTP ${r.status}: ${r.statusText}`);
        }
        const d = await r.json();
        BIN.loading = false;
        if (d.error) {
          BIN.card = null;
          _binRefreshLookupPanel();
          const scene = document.getElementById("bin-scene");
          if (scene) scene.insertAdjacentHTML("beforeend", `<div class="bin-error-msg">${escapeHtml(String(d.error))}</div>`);
        } else if (!d.found) {
          BIN.card = null;
          _binRefreshLookupPanel();
          const scene = document.getElementById("bin-scene");
          if (scene) scene.insertAdjacentHTML("beforeend", `<div class="bin-notfound-msg">${escapeHtml(d.note || "No matching BIN found.")}</div>`);
        } else {
          BIN.card = d.card;
          _binRefreshLookupPanel();
          requestAnimationFrame(() => setTimeout(binAnimateIn, 30));
        }
      } catch (e) {
        console.error("BIN Lookup error:", e);
        BIN.loading = false;
        BIN.card = null;
        _binRefreshLookupPanel();
        const scene = document.getElementById("bin-scene");
        if (scene) scene.insertAdjacentHTML("beforeend", `<div class="bin-error-msg">Error: ${escapeHtml(String(e.message))}</div>`);
      }
    });
  }

  // ===================== Consumer Clarity Use Case =====================
  // Turns cryptic statement descriptors into rich merchant identities.
  // Stripe-inspired before → after card.

  const CLARITY = {
    presetKey: null,
    loading: false,
    result: null,   // { found, raw, merchant, note }
  };

  function _clarityManifest() {
    return USE_CASES.find(u => u.id === "consumer_clarity");
  }
  function _clarityPresets() {
    const m = _clarityManifest();
    return (m && m.presets) || [];
  }
  function _clarityPreset(key) {
    return _clarityPresets().find(p => p.value === key);
  }

  function renderClarity() {
    _renderCachedWebview('consumer_clarity', 'clarity-webview-frame', _appPath('/consumer_clarity/index.html'), 'Consumer Clarity');
  }

  function clarityRender() {
    const body = $("uc-body");
    if (!body) return;
    const presets = _clarityPresets();
    body.innerHTML = `
      <div class="clarity-stage">
        <div class="clarity-form-card">
          <div class="clarity-form-header">
            <div class="clarity-form-title">Statement descriptor lookup</div>
            <div class="clarity-form-sub">Pick a sandbox transaction to enrich.</div>
          </div>
          <div class="clarity-form-row">
            <div class="clarity-field">
              <label for="clarity-select">Transaction</label>
              <select id="clarity-select">
                ${presets.map(p =>
                  `<option value="${escapeHtml(p.value)}"${p.value === CLARITY.presetKey ? " selected" : ""}>${escapeHtml(p.label)}</option>`
                ).join("")}
              </select>
            </div>
            <button class="clarity-btn" id="clarity-btn"${CLARITY.loading ? " disabled" : ""}>
              ${CLARITY.loading
                ? `<span class="clarity-spinner"></span>Enriching…`
                : `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" style="width:15px;height:15px;flex-shrink:0"><circle cx="9" cy="9" r="6"/><path d="M15 15l3 3" stroke-linecap="round"/></svg>Enrich`}
            </button>
          </div>
        </div>
        <div class="clarity-result" id="clarity-result">
          ${clarityResultHtml()}
        </div>
      </div>`;
    clarityWire();
  }

  function clarityResultHtml() {
    if (CLARITY.loading) {
      return `<div class="clarity-loading"><div class="clarity-spinner clarity-spinner--lg"></div><p>Calling Consumer Clarity API…</p></div>`;
    }
    if (!CLARITY.result) {
      return clarityHeroHtml();
    }
    if (CLARITY.result.error) {
      return `<div class="clarity-error">${escapeHtml(String(CLARITY.result.error))}</div>`;
    }

    const raw = CLARITY.result.raw || {};
    const rawText = (raw.cardAcceptorName || "—").toUpperCase();
    const rawSub = [raw.cardAcceptorLocation, raw.cardAcceptorRegionCode, raw.cardAcceptorCountryCode]
      .filter(Boolean).join(" · ");

    if (!CLARITY.result.found) {
      return `
        <div class="clarity-grid">
          ${clarityRawCardHtml(rawText, rawSub)}
          <div class="clarity-arrow">${_clarityArrowSvg()}</div>
          <div class="clarity-merchant-card clarity-merchant-card--empty">
            <div class="clarity-empty-icon">
              <svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="14" cy="14" r="10"/><path d="M22 22l6 6" stroke-linecap="round"/></svg>
            </div>
            <div class="clarity-empty-title">No match</div>
            <div class="clarity-empty-sub">${escapeHtml(CLARITY.result.note || "No matching merchant found.")}</div>
          </div>
        </div>`;
    }

    const m = CLARITY.result.merchant || {};
    return `
      <div class="clarity-grid">
        ${clarityRawCardHtml(rawText, rawSub)}
        <div class="clarity-arrow">${_clarityArrowSvg()}</div>
        ${clarityMerchantCardHtml(m)}
      </div>
      ${clarityFieldsHtml(m)}`;
  }

  function clarityRawCardHtml(name, sub) {
    return `
      <div class="clarity-raw-card">
        <div class="clarity-raw-label">Raw descriptor</div>
        <div class="clarity-raw-name">${escapeHtml(name)}</div>
        ${sub ? `<div class="clarity-raw-sub">${escapeHtml(sub)}</div>` : ""}
        <div class="clarity-raw-tag">Card statement</div>
      </div>`;
  }

  function clarityMerchantCardHtml(m) {
    const initials = (m.name || "?").slice(0, 2).toUpperCase();
    const logo = m.merchantLogo
      ? `<img src="${escapeHtml(m.merchantLogo)}" alt="${escapeHtml(m.name)}" class="clarity-merchant-logo-img" loading="lazy" onerror="this.outerHTML='<div class=&quot;clarity-merchant-logo-fallback&quot;>${escapeHtml(initials)}</div>'">`
      : `<div class="clarity-merchant-logo-fallback">${escapeHtml(initials)}</div>`;
    const addr = (m.addressLines || []).map(l => `<div class="clarity-addr-line">${escapeHtml(l)}</div>`).join("");
    const cat = m.categoryName
      ? `<span class="clarity-chip clarity-chip--cat">${escapeHtml(m.categoryName)}${m.categoryCode ? ` · MCC ${escapeHtml(String(m.categoryCode))}` : ""}</span>`
      : "";
    const receipt = m.receiptStatus === "RECEIPT_FOUND" || m.receiptUrl
      ? `<span class="clarity-chip clarity-chip--ok">Digital receipt available</span>` : "";
    const website = m.websiteUrl
      ? `<a class="clarity-link" href="${escapeHtml(m.websiteUrl)}" target="_blank" rel="noopener">Visit website ↗</a>`
      : "";
    return `
      <div class="clarity-merchant-card">
        <div class="clarity-merchant-head">
          <div class="clarity-merchant-logo">${logo}</div>
          <div class="clarity-merchant-name-block">
            <div class="clarity-merchant-name">${escapeHtml(m.name)}</div>
            <div class="clarity-merchant-tag">Enriched merchant</div>
          </div>
        </div>
        ${addr ? `<div class="clarity-merchant-addr">
          <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" style="width:14px;height:14px;flex-shrink:0;margin-top:2px;color:var(--muted)"><path d="M10 18s-6-5.5-6-10a6 6 0 0112 0c0 4.5-6 10-6 10z"/><circle cx="10" cy="8" r="2"/></svg>
          <div>${addr}</div>
        </div>` : ""}
        <div class="clarity-merchant-chips">
          ${cat}${receipt}
        </div>
        ${website ? `<div class="clarity-merchant-actions">${website}</div>` : ""}
      </div>`;
  }

  function clarityFieldsHtml(m) {
    const rows = [];
    if (m.categoryCode) rows.push(["Category code (MCC)", String(m.categoryCode)]);
    if (m.categoryName) rows.push(["Category", m.categoryName]);
    if (m.lat != null && m.lng != null) rows.push(["Coordinates", `${m.lat}, ${m.lng}`]);
    if (m.merchantStatus) rows.push(["Merchant status", m.merchantStatus]);
    if (m.receiptStatus) rows.push(["Receipt status", m.receiptStatus]);

    const hasMap = m.lat != null && m.lng != null;
    const hasIndustryLogo = !!m.industryLogo;
    const hasMedia = hasMap || hasIndustryLogo;

    let mediaHtml = "";
    if (hasMedia) {
      const mapHtml = hasMap ? clarityMapHtml(m.lat, m.lng, m.name) : "";
      const logoHtml = hasIndustryLogo ? `
        <div class="clarity-media-card">
          <div class="clarity-media-label">Industry logo</div>
          <div class="clarity-industry-logo-box">
            <img src="${escapeHtml(m.industryLogo)}" alt="Industry logo" class="clarity-industry-logo-img" loading="lazy">
          </div>
        </div>` : "";
      mediaHtml = `<div class="clarity-media-grid${hasMap && hasIndustryLogo ? "" : " clarity-media-grid--single"}">${mapHtml}${logoHtml}</div>`;
    }

    const detailsHtml = rows.length ? `
      <div class="clarity-details">
        <div class="clarity-details-title">Details</div>
        <div class="clarity-details-grid">
          ${rows.map(([k, v]) => `
            <div class="clarity-details-key">${escapeHtml(k)}</div>
            <div class="clarity-details-val">${escapeHtml(v)}</div>
          `).join("")}
        </div>
      </div>` : "";

    return mediaHtml + detailsHtml;
  }

  function clarityMapHtml(lat, lng, name) {
    const dLat = parseFloat(lat);
    const dLng = parseFloat(lng);
    if (!isFinite(dLat) || !isFinite(dLng)) return "";
    const delta = 0.01;
    const bbox = [dLng - delta, dLat - delta, dLng + delta, dLat + delta].join(",");
    const src = `https://www.openstreetmap.org/export/embed.html?bbox=${encodeURIComponent(bbox)}&layer=mapnik&marker=${dLat},${dLng}`;
    const link = `https://www.openstreetmap.org/?mlat=${dLat}&mlon=${dLng}#map=15/${dLat}/${dLng}`;
    return `
      <div class="clarity-media-card">
        <div class="clarity-media-label">Location</div>
        <div class="clarity-map-box">
          <iframe class="clarity-map-frame" src="${escapeHtml(src)}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="${escapeHtml(name || 'Merchant location')}"></iframe>
        </div>
        <a class="clarity-link clarity-map-link" href="${escapeHtml(link)}" target="_blank" rel="noopener">View larger map ↗</a>
      </div>`;
  }

  function clarityHeroHtml() {
    return `
      <div class="clarity-hero">
        <div class="clarity-hero-icon">
          <svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5">
            <rect x="8" y="14" width="32" height="22" rx="3"/>
            <path d="M8 22h32M14 30h6"/>
          </svg>
        </div>
        <h3>Turn cryptic statements into clear merchant identities</h3>
        <p>Pick a sandbox transaction above and click <strong>Enrich</strong> to see a raw descriptor transformed into a recognisable merchant — complete with logo, address, category, and receipt link.</p>
        <div class="clarity-hero-chips">
          <span class="clarity-hero-chip">Clean merchant name</span>
          <span class="clarity-hero-chip">Logo &amp; category</span>
          <span class="clarity-hero-chip">Address &amp; map</span>
          <span class="clarity-hero-chip">Digital receipts</span>
        </div>
      </div>`;
  }

  function _clarityArrowSvg() {
    return `<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 16h20M20 10l6 6-6 6"/></svg>`;
  }

  function clarityWire() {
    const sel = document.getElementById("clarity-select");
    if (sel) {
      sel.addEventListener("change", () => {
        CLARITY.presetKey = sel.value;
      });
    }
    const btn = document.getElementById("clarity-btn");
    if (!btn) return;
    btn.addEventListener("click", async () => {
      if (!CLARITY.presetKey) return;
      CLARITY.loading = true;
      CLARITY.result = null;
      clarityRender();
      try {
        const r = await _nativeFetch("/usecases/clarity/action", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ action: "lookup", params: { preset: CLARITY.presetKey } }),
        });
        if (!r.ok) throw new Error(`HTTP ${r.status}: ${r.statusText}`);
        const d = await r.json();
        CLARITY.loading = false;
        CLARITY.result = d;
        clarityRender();
      } catch (e) {
        console.error("Clarity lookup error:", e);
        CLARITY.loading = false;
        CLARITY.result = { error: e.message || String(e) };
        clarityRender();
      }
    });
  }

  // ===================== Personal Finance Manager Use Case =====================
  // Rendered as a sandboxed iframe pointing to /pfm/index.html.
  // All PFM UI lives in usecases/pfm/ — edit there to change the look.

  const _cachedUsecaseWebviews = new Map();

  function _getWebviewCacheHost() {
    let host = document.getElementById('uc-webview-cache-host');
    if (host) return host;
    host = document.createElement('div');
    host.id = 'uc-webview-cache-host';
    host.hidden = true;
    document.body.appendChild(host);
    return host;
  }

  function _parkActiveWebview() {
    const body = document.getElementById('uc-body');
    if (!body) return;
    const ucId = body.dataset.webviewUcId;
    const frame = body.querySelector('iframe.sonic-webview-frame');
    if (!ucId || !frame) return;
    _cachedUsecaseWebviews.set(ucId, frame);
    _getWebviewCacheHost().appendChild(frame);
    delete body.dataset.webviewUcId;
  }

  function _renderCachedWebview(ucId, frameId, src, title) {
    const body = $('uc-body');
    if (!body) return;

    let frame = _cachedUsecaseWebviews.get(ucId);
    if (!frame) {
      frame = document.createElement('iframe');
      frame.id = frameId;
      frame.className = 'sonic-webview-frame';
      frame.src = src;
      frame.title = title;
      _cachedUsecaseWebviews.set(ucId, frame);
    } else {
      frame.id = frameId;
      frame.title = title;
    }

    body.replaceChildren(frame);
    body.dataset.webviewUcId = ucId;
    _attachWebviewRefresh(frameId);
  }

  // Shared helper: hides the Full Screen button and injects a Refresh button
  // in its place in the uc-header. Call after setting uc-body innerHTML.
  function _attachWebviewRefresh(frameId) {
    const popout = document.getElementById('uc-popout-btn');
    if (!popout || document.getElementById('uc-webview-refresh-btn')) return;
    popout.hidden = true;
    const btn = document.createElement('button');
    btn.id = 'uc-webview-refresh-btn';
    btn.className = 'uc-popout-btn';
    btn.title = 'Refresh';
    btn.innerHTML = `<svg width="14" height="14" viewBox="0 0 15 15" fill="none" aria-hidden="true"><path d="M1.5 7.5a6 6 0 1 0 1.2-3.6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M1.5 2.5v2.5H4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg> Refresh`;
    popout.insertAdjacentElement('afterend', btn);
    const frame = document.getElementById(frameId);
    if (frame) {
      if (!frame.dataset.themeBridgeBound) {
        frame.addEventListener('load', () => _postThemeToEmbeddedFrame(frame, _currentThemeMode()));
        frame.dataset.themeBridgeBound = '1';
      }
      _postThemeToEmbeddedFrame(frame, _currentThemeMode());
      btn.addEventListener('click', () => {
        btn.classList.add('sonic-refresh--spinning');
        frame.src = frame.src;
        frame.addEventListener('load', () => btn.classList.remove('sonic-refresh--spinning'), { once: true });
      });
    }
  }

  function renderPfm() {
    _renderCachedWebview('pfm', 'pfm-webview-frame', _appPath('/pfm/index.html'), 'Personal Finance Manager');
  }

  // ===================== Easy Savings Use Case =====================
  // Browse SME merchant offers by BIN / country, then redeem a voucher.

  const ES = {
    bin: "52345678",
    country: "IND",
    language: "en-US",
    offers: [],
    total: 0,
    loading: false,
    redeeming: null,     // offer id currently being redeemed
    redemption: null,    // last redemption result
    error: null,
  };

  function _esManifest() { return USE_CASES.find(u => u.id === "easy_savings"); }

  function renderEasySavings() {
    _renderCachedWebview('easy_savings', 'easysavings-webview-frame', _appPath('/easy_savings/index.html'), 'Easy Savings');
  }

  function esRender() {
    const body = $("uc-body");
    if (!body) return;

    body.innerHTML = `
      <div class="es-stage">
        <div class="es-form-card">
          <div class="es-form-header">
            <div class="es-form-title">Browse Merchant Offers</div>
            <div class="es-form-sub">Enter a BIN and country to discover available SME savings.</div>
          </div>
          <div class="es-form-row">
            <div class="es-field">
              <label for="es-bin">BIN (8 digits)</label>
              <input id="es-bin" type="text" value="${escapeHtml(ES.bin)}" placeholder="e.g. 52345678" maxlength="8">
            </div>
            <div class="es-field">
              <label for="es-country">Country (ISO-3)</label>
              <input id="es-country" type="text" value="${escapeHtml(ES.country)}" placeholder="e.g. IND" maxlength="3">
            </div>
            <div class="es-field">
              <label for="es-lang">Language</label>
              <input id="es-lang" type="text" value="${escapeHtml(ES.language)}" placeholder="e.g. en-US" maxlength="10">
            </div>
            <button class="es-btn es-btn--primary" id="es-browse-btn"${ES.loading ? " disabled" : ""}>
              ${ES.loading
                ? '<span class="es-spinner"></span>Searching…'
                : '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" style="width:15px;height:15px;flex-shrink:0"><circle cx="9" cy="9" r="6"/><path d="M15 15l3 3" stroke-linecap="round"/></svg>Browse'}
            </button>
          </div>
        </div>
        <div class="es-result" id="es-result">
          ${esResultHtml()}
        </div>
      </div>`;
    esWire();
  }

  function esResultHtml() {
    if (ES.loading) {
      return '<div class="es-loading"><div class="es-spinner es-spinner--lg"></div><p>Fetching offers…</p></div>';
    }
    if (ES.error) {
      return '<div class="es-error">' + escapeHtml(String(ES.error)) + '</div>';
    }
    if (!ES.offers.length) {
      return esHeroHtml();
    }

    // Redemption banner
    let redemptionBanner = "";
    if (ES.redemption) {
      const r = ES.redemption;
      redemptionBanner = `
        <div class="es-redemption-banner">
          <div class="es-redemption-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
          </div>
          <div class="es-redemption-body">
            <div class="es-redemption-title">Offer redeemed successfully</div>
            ${r.orderId ? '<div class="es-redemption-detail"><span class="es-detail-label">Order ID</span> <code>' + escapeHtml(r.orderId) + '</code></div>' : ""}
            ${r.voucherCode ? '<div class="es-redemption-detail"><span class="es-detail-label">Voucher</span> <code class="es-voucher-code">' + escapeHtml(r.voucherCode) + '</code></div>' : ""}
            ${r.status ? '<div class="es-redemption-detail"><span class="es-detail-label">Status</span> ' + escapeHtml(r.status) + '</div>' : ""}
            ${r.redemptionUrl ? '<a class="es-link" href="' + escapeHtml(r.redemptionUrl) + '" target="_blank" rel="noopener">Redeem at merchant ↗</a>' : ""}
          </div>
          <button class="es-banner-close" id="es-banner-close" title="Dismiss">✕</button>
        </div>`;
    }

    return `
      ${redemptionBanner}
      <div class="es-summary-strip">
        <div class="es-summary-item">
          <label>Offers found</label>
          <span>${ES.total}</span>
        </div>
        <div class="es-summary-item">
          <label>BIN</label>
          <span><code>${escapeHtml(ES.bin)}</code></span>
        </div>
        <div class="es-summary-item">
          <label>Country</label>
          <span>${escapeHtml(ES.country)}</span>
        </div>
      </div>
      <div class="es-offer-grid">
        ${ES.offers.map(esOfferCardHtml).join("")}
      </div>`;
  }

  function esOfferCardHtml(offer) {
    const isRedeeming = ES.redeeming === offer.id;
    const initials = (offer.merchantName || "?").slice(0, 2).toUpperCase();
    const logo = offer.merchantLogo
      ? '<img src="' + escapeHtml(offer.merchantLogo) + '" alt="' + escapeHtml(offer.merchantName) + '" class="es-offer-logo-img" loading="lazy" onerror="this.outerHTML=\'<div class=&quot;es-offer-logo-fallback&quot;>' + escapeHtml(initials) + '</div>\'">'
      : '<div class="es-offer-logo-fallback">' + escapeHtml(initials) + '</div>';

    const discount = offer.discountValue
      ? '<span class="es-offer-discount">' + escapeHtml(offer.discountValue) + (offer.discountType ? " " + escapeHtml(offer.discountType) : "") + '</span>'
      : "";

    const dates = [];
    if (offer.startDate) dates.push("From " + escapeHtml(offer.startDate));
    if (offer.endDate) dates.push("Until " + escapeHtml(offer.endDate));
    const dateHtml = dates.length
      ? '<div class="es-offer-dates">' + dates.join(" · ") + '</div>'
      : "";

    return `
      <div class="es-offer-card" data-offer-id="${escapeHtml(offer.id)}">
        <div class="es-offer-top">
          <div class="es-offer-logo">${logo}</div>
          <div class="es-offer-name-block">
            <div class="es-offer-merchant">${escapeHtml(offer.merchantName)}</div>
            ${offer.category ? '<div class="es-offer-cat">' + escapeHtml(offer.category) + '</div>' : ""}
          </div>
          ${discount}
        </div>
        <div class="es-offer-title">${escapeHtml(offer.title)}</div>
        ${offer.description ? '<div class="es-offer-desc">' + escapeHtml(offer.description) + '</div>' : ""}
        ${dateHtml}
        <div class="es-offer-actions">
          <button class="es-btn es-btn--redeem" data-redeem-id="${escapeHtml(offer.id)}"${isRedeeming ? " disabled" : ""}>
            ${isRedeeming
              ? '<span class="es-spinner"></span>Redeeming…'
              : '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" style="width:14px;height:14px;flex-shrink:0"><path d="M5 10h10M10 5v10"/></svg>Redeem'}
          </button>
          ${offer.termsUrl ? '<a class="es-terms-link" href="' + escapeHtml(offer.termsUrl) + '" target="_blank" rel="noopener">Terms</a>' : ""}
        </div>
      </div>`;
  }

  function esHeroHtml() {
    return `
      <div class="es-hero">
        <div class="es-hero-icon">
          <svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5">
            <rect x="6" y="12" width="36" height="24" rx="4"/>
            <path d="M6 20h36"/>
            <circle cx="34" cy="30" r="3"/>
          </svg>
        </div>
        <h3>Discover card-linked merchant savings</h3>
        <p>Enter a BIN and country above, then click <strong>Browse</strong> to explore available SME offers — discounts, vouchers, and promotions that cardholders can redeem instantly.</p>
        <div class="es-hero-chips">
          <span class="es-hero-chip">Local SME offers</span>
          <span class="es-hero-chip">Instant vouchers</span>
          <span class="es-hero-chip">No cost to issuers</span>
          <span class="es-hero-chip">Global coverage</span>
        </div>
      </div>`;
  }

  function esWire() {
    const binInput = document.getElementById("es-bin");
    const countryInput = document.getElementById("es-country");
    const langInput = document.getElementById("es-lang");

    if (binInput) binInput.addEventListener("input", () => { ES.bin = binInput.value.trim(); });
    if (countryInput) countryInput.addEventListener("input", () => { ES.country = countryInput.value.trim(); });
    if (langInput) langInput.addEventListener("input", () => { ES.language = langInput.value.trim(); });

    const browseBtn = document.getElementById("es-browse-btn");
    if (browseBtn) {
      browseBtn.addEventListener("click", () => esBrowse());
    }

    // Redeem buttons
    document.querySelectorAll("[data-redeem-id]").forEach(btn => {
      btn.addEventListener("click", () => esRedeem(btn.dataset.redeemId));
    });

    // Dismiss redemption banner
    const closeBtn = document.getElementById("es-banner-close");
    if (closeBtn) {
      closeBtn.addEventListener("click", () => {
        ES.redemption = null;
        esRender();
      });
    }
  }

  function esBrowse() {
    if (!ES.bin || !ES.country || !ES.language) return;
    ES.loading = true;
    ES.offers = [];
    ES.error = null;
    ES.redemption = null;
    esRender();

    fetch("/usecases/easysavings/action", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "browse", params: { bin: ES.bin, country: ES.country, language: ES.language } }),
    })
      .then(r => r.json())
      .then(d => {
        ES.loading = false;
        if (d.error) {
          ES.error = typeof d.error === "string" ? d.error : JSON.stringify(d.error);
        } else {
          ES.offers = d.offers || [];
          ES.total = d.total || ES.offers.length;
        }
        esRender();
      })
      .catch(err => {
        ES.loading = false;
        ES.error = err.message || String(err);
        esRender();
      });
  }

  function esRedeem(offerId) {
    if (!offerId || ES.redeeming) return;
    ES.redeeming = offerId;
    ES.redemption = null;
    esRender();

    fetch("/usecases/easysavings/action", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "redeem", params: { bin: ES.bin, offer_id: offerId } }),
    })
      .then(r => r.json())
      .then(d => {
        ES.redeeming = null;
        if (d.error) {
          ES.error = typeof d.error === "string" ? d.error : JSON.stringify(d.error);
        } else {
          ES.redemption = d.redemption || {};
        }
        esRender();
      })
      .catch(err => {
        ES.redeeming = null;
        ES.error = err.message || String(err);
        esRender();
      });
  }

  // ===================== Places Use Case =====================
  // Rendered as a sandboxed iframe pointing to /places/index.html.
  // All Places UI lives in usecases/places/ — edit there to change the look.

  function renderPlaces() {
    _renderCachedWebview('places', 'places-webview-frame', _appPath('/places/index.html'), 'Places');
  }


  // ===================== Online Identity Verification Use Case =====================
  // Simulated journey. No real API calls; toggle reveals what each provider
  // would contribute behind the scenes.

  // Shared Mastercard Sonic helpers (used by IDV confirmation steps).
  function _ensureMcSonicScript(cb) {
    if (customElements.get('mc-sonic')) { cb(); return; }
    if (document.querySelector('script[data-mc-sonic]')) {
      customElements.whenDefined('mc-sonic').then(cb);
      return;
    }
    const s = document.createElement('script');
    s.src = 'https://sonicsdk.mastercard.com/assets/js/latest/js/mc-sonic.min.js';
    s.setAttribute('data-mc-sonic', '1');
    s.onload = () => customElements.whenDefined('mc-sonic').then(cb);
    s.onerror = () => {};   // silent — sonic is optional
    document.head.appendChild(s);
  }

  function _sonicLaunch(cue, type, bg) {
    const overlay = document.createElement('div');
    overlay.style.cssText = 'position:fixed;inset:0;z-index:99999;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.72);';
    document.body.appendChild(overlay);
    const dismiss = () => { if (overlay.parentNode) overlay.remove(); };
    overlay.addEventListener('click', dismiss);
    if (type === 'sound-only') {
      const audio = document.createElement('mc-sonic');
      audio.setAttribute('type', 'sound-only');
      audio.setAttribute('sonicCue', cue);
      audio.style.cssText = 'position:fixed;opacity:0;pointer-events:none;width:1px;height:1px;top:-9999px;';
      document.body.appendChild(audio);
      overlay.remove();
      customElements.whenDefined('mc-sonic').then(() => setTimeout(() => audio.play(), 80));
      const done = () => audio.remove();
      audio.addEventListener('sonicCompletion', done, { once: true });
      setTimeout(done, 5000);
      return;
    }
    const el = document.createElement('mc-sonic');
    el.setAttribute('type', type);
    el.setAttribute('sonicCue', cue);
    if (bg) el.setAttribute('sonicBackground', bg);
    el.style.cssText = 'display:block;width:360px;height:360px;';
    overlay.appendChild(el);
    customElements.whenDefined('mc-sonic').then(() => setTimeout(() => el.play(), 80));
    el.addEventListener('sonicCompletion', dismiss, { once: true });
    setTimeout(dismiss, 3500);
  }

  const IDV = {
    phase: 'home',      // home | login | verify | passkey | records
    step: 0,            // 0..4 (only meaningful when phase==='verify')
    reveal: false,      // background view toggle
    loginUser: '',
    loginPass: '',
    passkeyChoice: null, // 'enrolled' | 'skipped' | null
    form: {
      firstName: "Alex",
      lastName: "Morgan",
      email: "alex.morgan@gmail.com",
      dob: "1988-04-12",
      address: "1600 Pennsylvania Ave NW, Washington, DC 20500",
      phone: "+1 (202) 555-0123",
    },
    selectedBank: null,
    bankConnected: false,
    bankConsentGiven: false,    // user clicked "I consent" in bank modal
    bankModalOpen: false,
    bankModalStage: "intro",    // intro | connecting | done
    cardConsent: false,
    cardAuthorizing: false,     // overlay while "authorize & verify" runs
    selectedCardId: null,       // auto-picked from bank's cards on step 2
    visaLast8: "",              // user-entered last 8 when Visa is picked
    // populated when we land on the result screen
    result: null,
  };

  // Cards "pulled from Open Banking" — what we know about each. Keyed by bankId.
  const IDV_CARDS = [
    // Chase
    { id: "chase-mc",   bankId: "chase", brand: "Mastercard", network: "mc",
      issuer: "Chase Sapphire Preferred", last4: "9999", knownPan: true,
      display: "Mastercard •••• 9999" },
    { id: "chase-visa", bankId: "chase", brand: "Visa", network: "visa",
      issuer: "Chase Freedom Unlimited",  last4: "1042", knownPan: false, bin6: "414720",
      display: "Visa •••• 1042" },
    // Bank of America
    { id: "boa-visa",   bankId: "boa", brand: "Visa", network: "visa",
      issuer: "BoA Cash Rewards",        last4: "2207", knownPan: false, bin6: "424631",
      display: "Visa •••• 2207" },
    { id: "boa-mc",     bankId: "boa", brand: "Mastercard", network: "mc",
      issuer: "BoA Premium Rewards",     last4: "6611", knownPan: true,
      display: "Mastercard •••• 6611" },
    // Wells Fargo
    { id: "wells-visa", bankId: "wells", brand: "Visa", network: "visa",
      issuer: "Wells Fargo Active Cash", last4: "3380", knownPan: false, bin6: "446542",
      display: "Visa •••• 3380" },
    // Citi
    { id: "citi-mc",    bankId: "citi", brand: "Mastercard", network: "mc",
      issuer: "Citi Double Cash",        last4: "4418", knownPan: true,
      display: "Mastercard •••• 4418" },
    { id: "citi-visa",  bankId: "citi", brand: "Visa", network: "visa",
      issuer: "Citi Custom Cash",        last4: "7720", knownPan: false, bin6: "414709",
      display: "Visa •••• 7720" },
    // U.S. Bank
    { id: "usbank-visa", bankId: "usbank", brand: "Visa", network: "visa",
      issuer: "U.S. Bank Cash+",         last4: "8845", knownPan: false, bin6: "433228",
      display: "Visa •••• 8845" },
    // Capital One
    { id: "cap1-mc",    bankId: "capitalone", brand: "Mastercard", network: "mc",
      issuer: "Capital One Venture",     last4: "5031", knownPan: true,
      display: "Mastercard •••• 5031" },
    { id: "cap1-visa",  bankId: "capitalone", brand: "Visa", network: "visa",
      issuer: "Capital One Quicksilver", last4: "9912", knownPan: false, bin6: "414740",
      display: "Visa •••• 9912" },
  ];

  const IDV_STEPS = [
    { key: "bank",     label: "Connect bank" },
    { key: "personal", label: "Personal info" },
    { key: "card",     label: "Verify By Card" },
    { key: "review",   label: "Verifying…" },
  ];

  const IDV_BANKS = [
    { id: "chase",      name: "Chase",            color: "#117ACA" },
    { id: "boa",        name: "Bank of America",  color: "#E31837" },
    { id: "wells",      name: "Wells Fargo",      color: "#D71E28" },
    { id: "citi",       name: "Citi",             color: "#003B70" },
    { id: "usbank",     name: "U.S. Bank",        color: "#0C2074" },
    { id: "capitalone", name: "Capital One",      color: "#004977" },
  ];

  // Behind-the-scenes "signals" surfaced per step
  function idvSignals(step) {
    if (step === 0) {
      return {
        title: "Step 1 — US Open Finance proves bank ownership",
        provider: "US Open Finance (Connect)",
        items: [
          ["Connect URL",            "https://connect.openfinance.us/?session=…"],
          ["Customer ID",            "cust_91421"],
          ["Institution",            IDV.selectedBank ? IDV.selectedBank.name : "(awaiting selection)"],
          ["OAuth scope",            "accounts.read  owner.read"],
          ["Account-owner returned", IDV.bankConnected ? "ALEX MORGAN — used to pre-fill next step" : "(pending consent)"],
          ["Account funded > 90d",   IDV.bankConnected ? "true (KYC-passing)" : "(pending)"],
          ["AccountID stored",       IDV.bankConnected ? "acct_4192xxxx7733" : "(pending)"],
        ],
        callout: "POST openfinance/v2/customers/{id}/accounts/owner  →  accountOwner.name returned & cached",
      };
    }
    if (step === 1) {
      return {
        title: "Step 2 — Ekata silently scores the applicant",
        provider: "Ekata Identity Verification",
        items: [
          ["Device fingerprint",  "d8b2-fa17-3c91-aa05  (canvas+webGL+UA)"],
          ["IP address",          "73.118.42.207 (US, residential, no proxy)"],
          ["IP velocity",         "1 signup in last 24h — low"],
          ["Email risk",          (IDV.form.email || "(empty)") + " — seen 4y, low risk"],
          ["Phone-to-name match", (IDV.form.phone || "(empty)") + " ↔ " + (IDV.form.firstName + ' ' + IDV.form.lastName).trim() + " — match"],
          ["Address validity",    (IDV.form.address || "(empty)") + " — USPS deliverable"],
          ["Name ↔ DOB",          "consistent across public records"],
          ["Bank-owner agreement","applicant name == openfinance owner.name"],
        ],
        callout: "POST identitycheck.api/v5/identity  →  confidenceScore: 612 / 1000",
      };
    }
    if (step === 2) {
      const card = IDV_CARDS.find(c => c.id === IDV.selectedCardId) || IDV_CARDS[0];
      const isVisa = card.network === 'visa';
      const visaOk = (IDV.visaLast8 || '').length === 8;
      const items = [
        ["Selected card",         `${card.brand} •••• ${card.last4} — ${card.issuer}`],
        ["PAN source",            card.knownPan
            ? "Open Banking (full PAN previously shared by issuer)"
            : `Open Banking (BIN6 ${card.bin6} + last4 ${card.last4}; middle 8 collected from user)`],
        ["Middle-8 challenge",    isVisa ? (visaOk ? "passed — proves possession of physical card" : "(awaiting 8 digits)") : "not required — full PAN known"],
        ["Network",               isVisa ? "Visa (VbV / EMV 3DS)" : "Mastercard (Identity Check / EMV 3DS)"],
        ["3DS Method status",     "Y — device collection succeeded"],
        ["ACS flow",              "Frictionless (transStatus = Y)"],
        ["Cardholder name match", `${(IDV.form.firstName + ' ' + IDV.form.lastName).toUpperCase()} ↔ issuer-on-file — match`],
        ["AVS request",           `${IDV.form.address}`],
        ["AVS response",          "Y — street & ZIP match"],
        ["Auth type",             "$0 account-verification (no charge, no clearing)"],
        ["Card storage",          "not stored — used for identity verification only"],
        ["Consent reference",     "consent_13322909"],
      ];
      return {
        title: "Step 3 — Verify By Card",
        provider: isVisa ? "Visa VbV + AVS" : "Mastercard Identity Check + AVS",
        items,
        callout: "POST consents/v1/cards  →  POST authentications (3DS)  →  POST avs/check  →  transStatus: Y, avsResponse: Y",
      };
    }
    if (step === 3) {
      return {
        title: "Step 4 — Combining the signals",
        provider: "Decision engine",
        items: [
          ["US Open Finance ownership", "Owner name match — strong"],
          ["Ekata confidence",         "612 / 1000  (Tier B)"],
          ["Card 3DS",                 "Authenticated — strong"],
          ["Card AVS",                 "Street & ZIP match — strong"],
          ["Name agreement",           "3 / 3 sources (bank, applicant, card)"],
          ["Address agreement",        "3 / 3 sources (Ekata, US Open Finance, AVS)"],
          ["Document fallback",        "not required"],
          ["Risk band",                "Low"],
        ],
        callout: "score = 0.3·openfinance + 0.3·ekata + 0.2·3ds + 0.2·avs  →  0.91  (auto-approve)",
      };
    }
    return {
      title: "Step 5 — Identity established",
      provider: "Medicare.gov",
      items: [
        ["Identity assurance level", "IAL2 (NIST 800-63-3)"],
        ["Medicare account linked",  "MED-US-2026-118-44219"],
        ["Audit bundle stored",      "US Open Finance owner.json + Ekata score + Mastercard 3DS receipt"],
        ["PII never seen",           "PAN tokenized; raw bank credentials never left US Open Finance"],
      ],
      callout: "session.identityVerified = true  →  unlock Medicare account",
    };
  }

  function renderIdentity() {
    _renderCachedWebview('identity', 'identity-webview-frame', _appPath('/identity/index.html'), 'Online Identity Verification');
  }

  function idvOpenModal() {
    if (document.getElementById('idv-fullscreen-modal')) return;
    const modal = document.createElement('div');
    modal.id = 'idv-fullscreen-modal';
    modal.className = 'idv-fullscreen-modal';
    // Clone the inner split content into the modal with its own wrap
    modal.innerHTML = `
      <div class="idv-modal-inner">
        <div class="idv-modal-topbar">
          <div class="idv-modal-title">Online Identity Verification</div>
          <div class="idv-modal-controls">
            <label class="idv-toggle idv-modal-toggle">
              <input type="checkbox" id="idv-modal-reveal-cb" ${IDV.reveal ? 'checked' : ''}>
              <span class="idv-toggle-track"><span class="idv-toggle-thumb"></span></span>
              <span class="idv-toggle-label">Reveal what's happening</span>
            </label>
            <button class="idv-modal-reduce-btn" title="Exit full screen (Esc)">
              <svg width="15" height="15" viewBox="0 0 15 15" fill="none"><path d="M9.5 5.5l-4 4M5.5 5.5v4h4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><rect x="1" y="1" width="13" height="13" rx="2" stroke="currentColor" stroke-width="1.5"/></svg>
              Reduce
            </button>
          </div>
        </div>
        <div class="idv-modal-wrap${IDV.reveal ? ' idv-reveal-on' : ''}" id="idv-modal-wrap">
          <div class="idv-modal-toolbar" id="idv-modal-toolbar" style="display:none">
            <div class="idv-stepper" id="idv-modal-stepper"></div>
          </div>
          <div class="idv-split" id="idv-modal-split">
            <div class="idv-browser">
              <div class="idv-browser-chrome">
                <span class="idv-dot r"></span><span class="idv-dot y"></span><span class="idv-dot g"></span>
                <div class="idv-url">
                  <span class="idv-lock">🔒</span>
                  <span id="idv-modal-url-text">www.medicare.gov</span>
                </div>
              </div>
              <div class="idv-page" id="idv-modal-page"></div>
            </div>
            <aside class="idv-bts" id="idv-modal-bts"></aside>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(modal);

    // Wire modal reveal toggle
    document.getElementById('idv-modal-reveal-cb').addEventListener('change', (e) => {
      IDV.reveal = !!e.target.checked;
      document.getElementById('idv-modal-wrap').classList.toggle('idv-reveal-on', IDV.reveal);
      // Sync embedded toggle
      const cb = document.getElementById('idv-reveal-cb');
      if (cb) cb.checked = IDV.reveal;
      const embWrap = document.querySelector('.idv-wrap');
      if (embWrap) embWrap.classList.toggle('idv-reveal-on', IDV.reveal);
    });

    // Reduce / close handlers
    const dismiss = () => { modal.remove(); idvRender(); };
    modal.querySelector('.idv-modal-reduce-btn').addEventListener('click', dismiss);
    const onKey = (e) => { if (e.key === 'Escape') { dismiss(); document.removeEventListener('keydown', onKey); } };
    document.addEventListener('keydown', onKey);

    // Render into the modal
    idvRender();
  }

  function idvRender() {
    const inModal = !!document.getElementById('idv-fullscreen-modal');
    const urlId   = inModal ? 'idv-modal-url-text' : 'idv-url-text';
    const wrapSel = inModal ? '#idv-modal-wrap'    : '.idv-wrap';

    // URL bar
    const urlEl = document.getElementById(urlId);
    if (urlEl) urlEl.textContent = idvCurrentUrl();

    // Toolbar visibility
    const toolbarSel = inModal ? '#idv-modal-toolbar' : '.idv-toolbar';
    const toolbar = document.querySelector(toolbarSel);
    if (toolbar) toolbar.style.display = (IDV.phase === 'verify') ? '' : 'none';

    // BTS aside
    const wrap = document.querySelector(wrapSel);
    if (wrap) wrap.classList.toggle('idv-no-bts', IDV.phase !== 'verify');

    idvRenderPage();
    idvRenderBts();
  }

  function idvCurrentUrl() {
    switch (IDV.phase) {
      case 'home':    return 'www.medicare.gov';
      case 'login':   return 'www.medicare.gov/account/login';
      case 'verify':  return 'www.medicare.gov/account/verify';
      case 'passkey': return 'www.medicare.gov/account/passkey';
      case 'records': return 'www.medicare.gov/account/my-record';
      default:        return 'www.medicare.gov';
    }
  }

  function idvRenderStepper() {
    const el = document.getElementById("idv-stepper");
    if (!el) return;
    el.innerHTML = IDV_STEPS.map((s, i) => {
      const state = i < IDV.step ? "done" : i === IDV.step ? "active" : "todo";
      return `<div class="idv-step idv-step-${state}">
        <span class="idv-step-num">${i < IDV.step ? "✓" : (i + 1)}</span>
        <span class="idv-step-label">${escapeHtml(s.label)}</span>
      </div>`;
    }).join('<span class="idv-step-sep"></span>');
  }

  function idvPageStepPersonal() {
    const f = IDV.form;
    const bankName = IDV.selectedBank ? IDV.selectedBank.name : 'your bank';
    return `
      <div class="idv-screen">
        <div class="idv-brand">
          <div class="idv-crown idv-crown-med">M</div>
          <div>
            <h2>Confirm your information</h2>
            <p class="muted">We pre-filled this from <strong>${escapeHtml(bankName)}</strong>. Review and continue \u2014 we only share what's needed with Medicare.gov.</p>
          </div>
        </div>
        <h3 class="idv-screen-title">Your details</h3>
        <div class="idv-grid">
          <label>First name<input id="idv-f-first" value="${escapeHtml(f.firstName)}"></label>
          <label>Last name<input id="idv-f-last" value="${escapeHtml(f.lastName)}"></label>
          <label class="idv-col-2">Email<input id="idv-f-email" type="email" value="${escapeHtml(f.email)}"></label>
          <label>Date of birth<input id="idv-f-dob" type="date" value="${escapeHtml(f.dob)}"></label>
          <label>Phone<input id="idv-f-phone" value="${escapeHtml(f.phone)}"></label>
          <label class="idv-col-2">Home address<input id="idv-f-addr" value="${escapeHtml(f.address)}"></label>
        </div>
        <div class="idv-actions">
          <button class="btn btn-outline" id="idv-back-personal">Back</button>
          <button class="btn btn-primary" id="idv-next-personal">Continue</button>
        </div>
      </div>`;
  }

  function idvPageStepBank() {
    const sel = IDV.selectedBank;
    return `
      <div class="idv-screen">
        <h3 class="idv-screen-title">Connect your bank</h3>
        <p class="muted">We confirm you own the account in your name. Your password is never shared with us — <strong>US Open Finance</strong> handles the secure sign-in. We'll use the account holder details to pre-fill the next step.</p>
        <div class="idv-banks">
          ${IDV_BANKS.map(b => `
            <button class="idv-bank ${sel && sel.id === b.id ? 'idv-bank-sel' : ''}" data-bank="${b.id}">
              <span class="idv-bank-mark" style="background:${b.color}">${escapeHtml(b.name.slice(0,1))}</span>
              <span>${escapeHtml(b.name)}</span>
            </button>`).join('')}
        </div>
        ${sel ? `
          <div class="idv-bank-card">
            <div class="idv-bank-card-head" style="background:${sel.color}">
              <span>${escapeHtml(sel.name)} Online</span>
              <span class="idv-bank-secure">🔒 openfinance.us</span>
            </div>
            <div class="idv-bank-card-body">
              <label>Username<input value="alex.morgan" disabled></label>
              <label>Password<input type="password" value="••••••••" disabled></label>
              <button class="btn btn-primary" id="idv-connect-bank">Sign in &amp; share account ownership</button>
            </div>
          </div>` : `<p class="muted idv-hint">Pick your bank to continue.</p>`}
        ${IDV.bankModalOpen ? idvBankModal() : ''}
      </div>`;
  }

  function idvBankModal() {
    const sel = IDV.selectedBank || { name: "your bank", color: "#1a3a8f" };
    const stage = IDV.bankModalStage;
    let body = '';
    if (stage === 'intro') {
      body = `
        <div class="idv-modal-body">
          <div class="idv-modal-icon" style="background:${sel.color}">🏛️</div>
          <h4>Share account ownership with Medicare.gov?</h4>
          <p class="muted">${escapeHtml(sel.name)} will share, via US Open Finance, only the information needed to confirm your identity:</p>
          <ul class="idv-modal-list">
            <li><strong>Account holder name</strong> &mdash; to match against your application</li>
            <li><strong>Account status &amp; age</strong> &mdash; confirm account is funded and active</li>
            <li><strong>Last 4 of account number</strong> &mdash; for the audit record</li>
          </ul>
          <p class="muted idv-modal-fine">No transactions, balances or credentials will be shared. You can revoke this consent at any time.</p>
          <div class="idv-modal-actions">
            <button class="btn btn-outline" id="idv-modal-cancel">Cancel</button>
            <button class="btn btn-primary" id="idv-modal-consent">I consent</button>
          </div>
        </div>`;
    } else if (stage === 'connecting') {
      body = `
        <div class="idv-modal-body idv-modal-center">
          <div class="idv-spinner-lg"></div>
          <h4>Sharing account ownership…</h4>
          <ul class="idv-verify-list">
            <li class="idv-vli idv-vli-done">Signed in to ${escapeHtml(sel.name)}</li>
            <li class="idv-vli idv-vli-done">Consent recorded with US Open Finance</li>
            <li class="idv-vli idv-vli-active">Retrieving account owner…</li>
          </ul>
        </div>`;
    }
    return `
      <div class="idv-modal-backdrop">
        <div class="idv-modal">
          <div class="idv-modal-head">
            <span>US Open Finance</span>
            <span class="idv-modal-secure">🔒 openfinance.us</span>
          </div>
          ${body}
        </div>
      </div>`;
  }

  function idvPageStep2() {
    const bankId = IDV.selectedBank ? IDV.selectedBank.id : null;
    const bankName = IDV.selectedBank ? IDV.selectedBank.name : 'your bank';
    const bankCards = IDV_CARDS.filter(c => c.bankId === bankId);
    // Auto-pick a Mastercard first; fall back to first available card
    if (!IDV.selectedCardId || !bankCards.find(c => c.id === IDV.selectedCardId)) {
      const mcCard = bankCards.find(c => c.network === 'mc');
      IDV.selectedCardId = (mcCard || bankCards[0]) ? (mcCard || bankCards[0]).id : null;
    }
    const card = bankCards.find(c => c.id === IDV.selectedCardId) || bankCards[0];
    const isVisa = card && card.network === 'visa';
    const visaDigits = (IDV.visaLast8 || '').replace(/\D/g, '').slice(0, 8);
    const visaComplete = !isVisa || visaDigits.length === 8;
    const canContinue = !!card && IDV.cardConsent && visaComplete && !IDV.cardAuthorizing;
    const displayedPan = card ? (isVisa
      ? `${card.bin6.slice(0,4)} ${card.bin6.slice(4)}${(visaDigits.slice(0,2) || '••').padEnd(2,'•')}  ${(visaDigits.slice(2,6) || '••••').padEnd(4,'•')}  ${(visaDigits.slice(6,8) || '••').padEnd(2,'•')}${card.last4.slice(0,2)} ${card.last4.slice(2)}`
      : `5204  ${card.last4.slice(0,2)}••  ••••  ${card.last4}`) : '';
    return `
      <div class="idv-screen">
        <h3 class="idv-screen-title">Verify By Card</h3>
        <p class="muted">We confirm you hold this card: identity verification only — no payment will be taken.</p>
        <label class="idv-field">
          <span class="muted">Card on file from ${escapeHtml(bankName)}</span>
          <select id="idv-card-select" class="idv-select">
            ${bankCards.map(c => `<option value="${c.id}" ${c.id === (card && card.id) ? 'selected' : ''}>${escapeHtml(c.display)} — ${escapeHtml(c.issuer)}</option>`).join('')}
            <option value="__other__" disabled>— Choose other card (demo only) —</option>
          </select>
        </label>
        ${card ? `
        <div class="idv-card-visual idv-card-${card.network}">
          <div class="idv-card-top">
            <div class="idv-card-chip"></div>
            <div class="idv-card-brand">${isVisa
              ? '<span class="idv-visa-mark">VISA</span>'
              : '<span class="r"></span><span class="y"></span>'}</div>
          </div>
          <div class="idv-card-num">${displayedPan}</div>
          <div class="idv-card-row">
            <div><span class="muted">Cardholder</span><br>${escapeHtml(IDV.form.firstName + ' ' + IDV.form.lastName).toUpperCase()}</div>
            <div class="idv-card-issuer"><span class="muted">Issuer</span><br>${escapeHtml(card.issuer)}</div>
          </div>
        </div>` : '<p class="muted">No cards on file for this bank.</p>'}
        ${isVisa ? `
          <div class="idv-visa-block">
            <p class="muted idv-visa-note">Your bank only shared the first 6 and last 4 of this Visa card. Enter the middle <strong>8 digits</strong> to confirm you have the physical card.</p>
            <label class="idv-field">
              <span class="muted">Middle 8 digits</span>
              <input id="idv-visa-8" inputmode="numeric" maxlength="8" placeholder="••••••••" value="${escapeHtml(visaDigits)}" autocomplete="off">
            </label>
          </div>` : (card ? `
          <p class="muted idv-card-note">Your bank already shared this full card number with Open Banking, so no extra digits are required.</p>` : '')}
        <label class="idv-check">
          <input type="checkbox" id="idv-consent-cb" ${IDV.cardConsent ? 'checked' : ''}>
          <span>I authorize Medicare to verify my identity by checking this card with my issuer. No payment will be taken; the card is not stored.</span>
        </label>
        <div class="idv-actions">
          <button class="btn btn-outline" id="idv-back-2" ${IDV.cardAuthorizing ? 'disabled' : ''}>Back</button>
          <button class="btn btn-primary" id="idv-next-2" ${canContinue ? '' : 'disabled'}>
            Verify By Card
          </button>
        </div>
      </div>`;
  }

  function idvPageStep3() {
    return `
      <div class="idv-screen idv-screen-center">
        <div class="idv-spinner-lg"></div>
        <h3 class="idv-screen-title">Confirming who you are…</h3>
        <p class="muted">Cross-checking your bank, card and device signals.</p>
      </div>`;
  }

  function idvPageStep4() {
    return `
      <div class="idv-screen idv-screen-center">
        <div class="idv-tick">✓</div>
        <h3 class="idv-screen-title">You're verified</h3>
        <p class="muted">Your identity has been established. You can now access your Medicare account.</p>
        <div class="idv-result-card">
          <div class="idv-result-row"><span>Name</span><strong>${escapeHtml(IDV.form.firstName + ' ' + IDV.form.lastName)}</strong></div>
          <div class="idv-result-row"><span>Assurance level</span><strong>IAL2 (NIST 800-63-3)</strong></div>
          <div class="idv-result-row"><span>Risk band</span><strong class="idv-ok">Low</strong></div>
          <div class="idv-result-row"><span>Reference</span><strong>MED-US-2026-118-44219</strong></div>
        </div>
        <div class="idv-actions idv-actions-stack">
          <button class="btn btn-primary" id="idv-passkey">Use a passkey next time</button>
          <button class="btn btn-outline" id="idv-passkey-skip">Skip &mdash; access my records</button>
        </div>
      </div>`;
  }

  function idvRenderPage() {
    const inModal = !!document.getElementById('idv-fullscreen-modal');
    const page = document.getElementById(inModal ? 'idv-modal-page' : 'idv-page');
    if (!page) return;

    // Non-verify phases route here
    if (IDV.phase === 'home')    { page.innerHTML = idvPageHome();    return idvWireHome(page); }
    if (IDV.phase === 'login')   { page.innerHTML = idvPageLogin();   return idvWireLogin(page); }
    if (IDV.phase === 'passkey') { page.innerHTML = idvPagePasskey(); return idvWirePasskey(page); }
    if (IDV.phase === 'records') { page.innerHTML = idvPageRecords(); return idvWireRecords(page); }

    const renderers = [idvPageStepBank, idvPageStepPersonal, idvPageStep2, idvPageStep3, idvPageStep4];
    const bankName = IDV.selectedBank ? IDV.selectedBank.name : 'your bank';
    const bankColor = IDV.selectedBank ? IDV.selectedBank.color : '#1B6EC2';
    const bankInitial = IDV.selectedBank ? IDV.selectedBank.name.slice(0,1).toUpperCase() : '?';
    page.innerHTML = `
      <div class="med-page med-page-verify">
        <div class="med-topbar med-topbar-slim">
          <div class="med-topbar-inner">
            <span class="med-logo">
              <span class="med-logo-mark">M</span>
              <span class="med-logo-text">Medicare<span class="med-logo-dot">.gov</span></span>
            </span>
            <span class="med-account-pill">Identity verification</span>
          </div>
        </div>
        <div class="mcc-shell">
          <header class="mcc-header">
            <div class="mcc-brand">
              <span class="mcc-logo" aria-hidden="true"><span class="r"></span><span class="y"></span></span>
              <div class="mcc-brand-text">
                <strong>Mastercard ID Connect</strong>
                <span>Verifying you for <em>Medicare.gov</em> using your bank and card</span>
              </div>
            </div>
            <div class="mcc-pair">
              <span class="mcc-pair-pill">
                <span class="mcc-pair-dot" style="background:${bankColor}">${escapeHtml(bankInitial)}</span>
                ${escapeHtml(bankName)}
              </span>
              <span class="mcc-pair-link">↔</span>
              <span class="mcc-pair-pill">
                <span class="mcc-pair-card"><span class="r"></span><span class="y"></span></span>
                Your Mastercard
              </span>
            </div>
          </header>
          <div class="mcc-stepper" role="list">
            ${IDV_STEPS.map((s, i) => {
              const state = i < IDV.step ? 'done' : i === IDV.step ? 'active' : 'todo';
              return `<div class="mcc-step mcc-step-${state}" role="listitem">
                <span class="mcc-step-num">${i < IDV.step ? '✓' : (i + 1)}</span>
                <span class="mcc-step-label">${escapeHtml(s.label)}</span>
              </div>`;
            }).join('<span class="mcc-step-sep"></span>')}
          </div>
          <div class="mcc-body" id="idv-step-pane"></div>
          <footer class="mcc-foot">
            <span class="mcc-foot-lock">🔒</span>
            Secured by Mastercard. Your bank credentials and card details are never shared with Medicare.gov.
          </footer>
        </div>
      </div>
    `;
    const pane = document.getElementById('idv-step-pane');
    pane.innerHTML = renderers[IDV.step]();

    // Wiring per step
    if (IDV.step === 0) {
      // Step 0: Connect bank
      page.querySelectorAll(".idv-bank").forEach(btn => {
        btn.addEventListener("click", () => {
          const id = btn.dataset.bank;
          IDV.selectedBank = IDV_BANKS.find(b => b.id === id) || null;
          IDV.bankConnected = false;
          idvRender();
        });
      });
      const connectBtn = document.getElementById("idv-connect-bank");
      if (connectBtn) connectBtn.addEventListener("click", () => {
        IDV.bankModalOpen = true;
        IDV.bankModalStage = "intro";
        idvRender();
      });

      // Bank consent modal wiring
      const cancelBtn = document.getElementById("idv-modal-cancel");
      if (cancelBtn) cancelBtn.addEventListener("click", () => {
        IDV.bankModalOpen = false;
        idvRender();
      });
      const consentBtn = document.getElementById("idv-modal-consent");
      if (consentBtn) consentBtn.addEventListener("click", () => {
        IDV.bankModalStage = "connecting";
        idvRender();
        setTimeout(() => {
          IDV.bankModalOpen = false;
          IDV.bankConsentGiven = true;
          IDV.bankConnected = true;
          // Pre-fill personal info from bank account owner record
          IDV.form.firstName = IDV.form.firstName || "Alex";
          IDV.form.lastName  = IDV.form.lastName  || "Morgan";
          IDV.form.email     = IDV.form.email     || "alex.morgan@gmail.com";
          IDV.form.dob       = IDV.form.dob       || "1958-04-12";
          IDV.form.phone     = IDV.form.phone     || "+1 (202) 555-0123";
          IDV.form.address   = IDV.form.address   || "1600 Pennsylvania Ave NW, Washington DC";
          IDV.step = 1;
          idvRender();
        }, 1800);
      });
    } else if (IDV.step === 1) {
      // Step 1: Personal info (pre-filled from bank)
      const nx = document.getElementById("idv-next-personal");
      if (nx) nx.addEventListener("click", () => {
        IDV.form.firstName = document.getElementById("idv-f-first").value || IDV.form.firstName;
        IDV.form.lastName  = document.getElementById("idv-f-last").value  || IDV.form.lastName;
        IDV.form.email     = document.getElementById("idv-f-email").value || IDV.form.email;
        IDV.form.dob       = document.getElementById("idv-f-dob").value   || IDV.form.dob;
        IDV.form.phone     = document.getElementById("idv-f-phone").value || IDV.form.phone;
        IDV.form.address   = document.getElementById("idv-f-addr").value  || IDV.form.address;
        IDV.step = 2;
        idvRender();
      });
      const backP = document.getElementById("idv-back-personal");
      if (backP) backP.addEventListener("click", () => { IDV.step = 0; idvRender(); });
    } else if (IDV.step === 2) {
      const sel = document.getElementById("idv-card-select");
      if (sel) sel.addEventListener("change", () => {
        IDV.selectedCardId = sel.value;
        IDV.visaLast8 = "";
        idvRender();
      });
      const visaInput = document.getElementById("idv-visa-8");
      if (visaInput) {
        visaInput.addEventListener("input", () => {
          const cleaned = visaInput.value.replace(/\D/g, '').slice(0, 8);
          if (cleaned !== visaInput.value) visaInput.value = cleaned;
          IDV.visaLast8 = cleaned;
          // Update enabled state without re-render (preserve focus)
          const card = IDV_CARDS.find(c => c.id === IDV.selectedCardId);
          const visaComplete = !card || card.network !== 'visa' || cleaned.length === 8;
          const nb = document.getElementById("idv-next-2");
          if (nb) nb.disabled = !IDV.cardConsent || !visaComplete || IDV.cardAuthorizing;
        });
      }
      const cb = document.getElementById("idv-consent-cb");
      if (cb) cb.addEventListener("change", () => {
        IDV.cardConsent = cb.checked;
        const card = IDV_CARDS.find(c => c.id === IDV.selectedCardId);
        const visaComplete = !card || card.network !== 'visa' || (IDV.visaLast8 || '').length === 8;
        const nb = document.getElementById("idv-next-2");
        if (nb) nb.disabled = !cb.checked || !visaComplete || IDV.cardAuthorizing;
      });
      const backBtn = document.getElementById("idv-back-2");
      if (backBtn) backBtn.addEventListener("click", () => { IDV.step = 1; idvRender(); });
      const nextBtn = document.getElementById("idv-next-2");
      if (nextBtn) nextBtn.addEventListener("click", () => {
        if (IDV.cardAuthorizing) return;
        IDV.cardAuthorizing = true;
        IDV.step = 3;
        idvRender();
        _ensureMcSonicScript(() => _sonicLaunch('securedby', 'default', 'black'));
        setTimeout(() => {
          IDV.cardAuthorizing = false;
          IDV.step = 4;
          idvRender();
          // Auto-scroll the verified screen into view
          requestAnimationFrame(() => {
            const inModalScroll = !!document.getElementById('idv-fullscreen-modal');
            const screen = document.querySelector((inModalScroll ? '#idv-modal-page' : '#idv-page') + ' .idv-screen');
            if (screen && typeof screen.scrollIntoView === 'function') {
              screen.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
            const browser = document.querySelector('.idv-browser');
            if (browser) browser.scrollTo({ top: 0, behavior: 'smooth' });
            const inModal2 = !!document.getElementById('idv-fullscreen-modal');
            const page = document.getElementById(inModal2 ? 'idv-modal-page' : 'idv-page');
            if (page) page.scrollTo({ top: 0, behavior: 'smooth' });
            window.scrollTo({ top: 0, behavior: 'smooth' });
          });
        }, 1400);
      });
    } else if (IDV.step === 4) {
      const pk = document.getElementById("idv-passkey");
      if (pk) pk.addEventListener("click", () => {
        IDV.phase = 'passkey';
        idvRender();
      });
      const skip = document.getElementById("idv-passkey-skip");
      if (skip) skip.addEventListener("click", () => {
        IDV.passkeyChoice = 'skipped';
        IDV.phase = 'records';
        idvRender();
      });
    }
  }

  // ============== Medicare.gov sample pages ==============
  function idvPageHome() {
    return `
      <div class="med-page med-page-home">
        <div class="med-topbar med-topbar-clean">
          <div class="med-topbar-inner">
            <a class="med-logo" href="#" onclick="return false">
              <span class="med-logo-mark">M</span>
              <span class="med-logo-text">Medicare<span class="med-logo-dot">.gov</span></span>
            </a>
            <button class="med-login-btn" id="med-login-go">Log in</button>
          </div>
        </div>
        <section class="med-welcome">
          <svg class="med-welcome-wave" viewBox="0 0 800 600" preserveAspectRatio="none" aria-hidden="true">
            <path d="M -20 120 C 160 60, 380 180, 460 80 S 740 60, 820 180 S 620 360, 460 320 S 200 380, 100 480 S -40 560, 60 620"
                  fill="none" stroke="#2e7d6b" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>
          </svg>
          <div class="med-welcome-portrait" aria-hidden="true">
            <svg viewBox="0 0 220 240" width="100%" height="100%">
              <defs>
                <linearGradient id="medSkin" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#d2a279"/>
                  <stop offset="100%" stop-color="#a87a55"/>
                </linearGradient>
                <linearGradient id="medShirt" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%" stop-color="#3a5a7a"/>
                  <stop offset="100%" stop-color="#5a7a8a"/>
                </linearGradient>
              </defs>
              <!-- shirt -->
              <path d="M 20 240 L 30 170 Q 60 150, 110 150 Q 160 150, 190 170 L 200 240 Z" fill="url(#medShirt)"/>
              <!-- plaid lines -->
              <g stroke="#2a3f55" stroke-width="2" opacity="0.5">
                <line x1="50" y1="155" x2="55" y2="240"/>
                <line x1="90" y1="152" x2="92" y2="240"/>
                <line x1="130" y1="152" x2="132" y2="240"/>
                <line x1="170" y1="155" x2="172" y2="240"/>
                <line x1="25" y1="190" x2="200" y2="190"/>
                <line x1="22" y1="215" x2="200" y2="215"/>
              </g>
              <g stroke="#c97a3e" stroke-width="1.5" opacity="0.55">
                <line x1="70" y1="152" x2="73" y2="240"/>
                <line x1="150" y1="152" x2="153" y2="240"/>
                <line x1="25" y1="175" x2="200" y2="175"/>
                <line x1="22" y1="230" x2="200" y2="230"/>
              </g>
              <!-- neck -->
              <path d="M 90 145 Q 110 158, 130 145 L 130 160 Q 110 168, 90 160 Z" fill="url(#medSkin)"/>
              <!-- head -->
              <ellipse cx="110" cy="100" rx="55" ry="62" fill="url(#medSkin)"/>
              <!-- hair (silver) -->
              <path d="M 58 88 Q 60 50, 110 42 Q 160 50, 162 88 Q 158 70, 130 66 Q 110 72, 90 66 Q 62 70, 58 88 Z" fill="#c8c8c8"/>
              <path d="M 60 92 Q 70 80, 85 84 M 135 84 Q 150 80, 160 92" stroke="#a8a8a8" stroke-width="1.5" fill="none"/>
              <!-- eyes (smiling closed crescents) -->
              <path d="M 82 102 Q 90 96, 98 102" stroke="#3a2a1a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
              <path d="M 122 102 Q 130 96, 138 102" stroke="#3a2a1a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
              <!-- eyebrows -->
              <path d="M 78 92 Q 88 88, 100 92" stroke="#8a8a8a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
              <path d="M 120 92 Q 132 88, 142 92" stroke="#8a8a8a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
              <!-- cheeks (smile lines) -->
              <path d="M 70 118 Q 76 124, 80 122" stroke="#8a5a3a" stroke-width="1.2" fill="none" opacity="0.5"/>
              <path d="M 140 122 Q 144 124, 150 118" stroke="#8a5a3a" stroke-width="1.2" fill="none" opacity="0.5"/>
              <!-- nose -->
              <path d="M 110 110 Q 105 122, 108 130 Q 112 132, 116 130" stroke="#8a5a3a" stroke-width="1.5" fill="none" opacity="0.6"/>
              <!-- smile -->
              <path d="M 88 138 Q 110 152, 132 138" stroke="#5a2a1a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
              <path d="M 92 139 Q 110 148, 128 139 Q 110 144, 92 139 Z" fill="#fff"/>
            </svg>
          </div>
          <div class="med-welcome-text">
            <h1>Welcome to<br>Medicare</h1>
            <button class="med-cta-green" id="med-cta-start">Get Started with Medicare</button>
          </div>
        </section>
        <footer class="med-footer">
          <div><strong>An official website of the U.S. Centers for Medicare &amp; Medicaid Services</strong></div>
          <div class="med-footer-links">
            <a href="#" onclick="return false">Privacy</a>
            <a href="#" onclick="return false">Accessibility</a>
            <a href="#" onclick="return false">No FEAR Act</a>
            <a href="#" onclick="return false">FOIA</a>
            <a href="#" onclick="return false">Plain writing</a>
          </div>
        </footer>
      </div>`;
  }
  function idvWireHome(page) {
    const go = () => { IDV.phase = 'login'; idvRender(); };
    page.querySelector('#med-login-go').addEventListener('click', go);
    const cta = page.querySelector('#med-cta-start');
    if (cta) cta.addEventListener('click', go);
  }

  function idvPageLogin() {
    return `
      <div class="med-page med-page-narrow">
        <div class="med-topbar med-topbar-slim">
          <div class="med-topbar-inner">
            <a class="med-logo" href="#" id="med-back-home">
              <span class="med-logo-mark">M</span>
              <span class="med-logo-text">Medicare<span class="med-logo-dot">.gov</span></span>
            </a>
          </div>
        </div>
        <div class="med-login">
          <h2>Log in or create account</h2>
          <p class="muted">You can use any of the methods below to access your Medicare account.</p>

          <form class="med-login-form" onsubmit="return false">
            <label>Username
              <input type="text" id="med-user" placeholder="Enter your username" autocomplete="username">
            </label>
            <label>Password
              <input type="password" id="med-pass" placeholder="Enter your password" autocomplete="current-password">
            </label>
            <div class="med-login-extras">
              <label class="med-remember"><input type="checkbox"> Remember me</label>
              <a href="#" onclick="return false">Forgot username or password?</a>
            </div>
            <button class="med-btn-primary" type="submit" disabled>Log in</button>
          </form>

          <div class="med-login-or"><span>or</span></div>

          <button class="med-mc-connect" id="med-mc-connect">
            <span class="med-mc-logo"><span class="r"></span><span class="y"></span></span>
            <span class="med-mc-text">
              <strong>Continue with Mastercard ID Connect</strong>
              <span>Verify your identity instantly using your bank &amp; card &mdash; no password needed.</span>
            </span>
            <span class="med-mc-arrow">→</span>
          </button>

          ${IDV.passkeyChoice === 'enrolled' ? `
          <button class="med-mc-passkey" id="med-mc-passkey">
            <span class="med-mc-logo"><span class="r"></span><span class="y"></span></span>
            <span class="med-mc-text">
              <strong>Mastercard ID Passkey</strong>
              <span>Instant access — authenticate with Face ID, Touch ID or screen lock.</span>
            </span>
            <span class="med-mc-key">🔑</span>
          </button>` : ''}

          <p class="med-login-fine">By logging in, you agree to the <a href="#" onclick="return false">Terms of use</a> and <a href="#" onclick="return false">Privacy policy</a>.</p>
        </div>
      </div>`;
  }
  function idvWireLogin(page) {
    const back = page.querySelector('#med-back-home');
    if (back) back.addEventListener('click', (e) => { e.preventDefault(); IDV.phase = 'home'; idvRender(); });
    page.querySelector('#med-mc-connect').addEventListener('click', () => {
      IDV.phase = 'verify';
      IDV.step = 0;
      idvRender();
    });
    const passkeyBtn = page.querySelector('#med-mc-passkey');
    if (passkeyBtn) {
      passkeyBtn.addEventListener('click', () => {
        _ensureMcSonicScript(() => _sonicLaunch('securedby', 'default', 'black'));
        setTimeout(() => {
          IDV.phase = 'records';
          idvRender();
        }, 1800);
      });
    }
  }

  function idvPagePasskey() {
    return `
      <div class="med-page med-page-verify">
        <div class="med-topbar med-topbar-slim">
          <div class="med-topbar-inner">
            <span class="med-logo">
              <span class="med-logo-mark">M</span>
              <span class="med-logo-text">Medicare<span class="med-logo-dot">.gov</span></span>
            </span>
            <span class="med-account-pill">${escapeHtml(IDV.form.firstName + ' ' + IDV.form.lastName)}</span>
          </div>
        </div>
        <div class="mcc-shell">
          <header class="mcc-header">
            <div class="mcc-brand">
              <span class="mcc-logo" aria-hidden="true"><span class="r"></span><span class="y"></span></span>
              <div class="mcc-brand-text">
                <strong>Mastercard ID Connect</strong>
                <span>Identity verified for <em>Medicare.gov</em></span>
              </div>
            </div>
          </header>
          <div class="mcc-body mcc-passkey-body">
            <div class="med-passkey-icon">🔑</div>
            <h2>Use a passkey next time?</h2>
            <p class="muted">Skip the bank &amp; card check the next time you log in. Your device will use Face ID, Touch ID, or your screen lock to prove it's you.</p>
            <ul class="med-passkey-list">
              <li><strong>Faster.</strong> Log in with a tap or a glance.</li>
              <li><strong>Phishing-resistant.</strong> Passkeys can't be reused or stolen.</li>
              <li><strong>Private.</strong> Stored only on your device.</li>
            </ul>
            <div class="med-passkey-actions">
              <button class="med-btn-outline" id="med-passkey-skip">Not now</button>
              <button class="med-btn-primary" id="med-passkey-go">Set up passkey</button>
            </div>
          </div>
          <footer class="mcc-foot">
            <span class="mcc-foot-lock">🔒</span>
            Secured by Mastercard. Your bank credentials and card details are never shared with Medicare.gov.
          </footer>
        </div>
      </div>`;
  }
  function idvWirePasskey(page) {
    page.querySelector('#med-passkey-skip').addEventListener('click', () => {
      IDV.passkeyChoice = 'skipped';
      IDV.phase = 'records';
      idvRender();
    });
    page.querySelector('#med-passkey-go').addEventListener('click', (e) => {
      const btn = e.currentTarget;
      btn.disabled = true;
      btn.innerHTML = '<span class="idv-btn-spin"></span> Setting up…';
      setTimeout(() => {
        IDV.passkeyChoice = 'enrolled';
        IDV.phase = 'records';
        idvRender();
      }, 1100);
    });
  }

  function idvPageRecords() {
    const name = IDV.form.firstName + ' ' + IDV.form.lastName;
    const passkeyBadge = IDV.passkeyChoice === 'enrolled'
      ? '<span class="med-badge med-badge-ok">🔑 Passkey enabled</span>'
      : '<span class="med-badge med-badge-dim">Passkey not set</span>';
    return `
      <div class="med-page">
        <div class="med-topbar med-topbar-slim">
          <div class="med-topbar-inner">
            <span class="med-logo">
              <span class="med-logo-mark">M</span>
              <span class="med-logo-text">Medicare<span class="med-logo-dot">.gov</span></span>
            </span>
            <span class="med-account-pill">${escapeHtml(name)}</span>
          </div>
          <nav class="med-nav">
            <a class="active" href="#" onclick="return false">My record</a>
            <a href="#" onclick="return false">Plans</a>
            <a href="#" onclick="return false">Claims</a>
            <a href="#" onclick="return false">Messages</a>
            <a href="#" onclick="return false">Account settings</a>
          </nav>
        </div>
        <section class="med-record-head">
          <div>
            <h2>Welcome back, ${escapeHtml(IDV.form.firstName)}</h2>
            <p class="muted">Medicare Beneficiary Identifier &middot; 1EG4-TE5-MK73 &middot; ${passkeyBadge}</p>
          </div>
          <button class="med-btn-outline" id="med-logout">Log out</button>
        </section>
        <section class="med-record-grid">
          <div class="med-card">
            <h3>Personal information</h3>
            <dl class="med-dl">
              <dt>Name</dt><dd>${escapeHtml(name)}</dd>
              <dt>Date of birth</dt><dd>${escapeHtml(IDV.form.dob)}</dd>
              <dt>Address</dt><dd>${escapeHtml(IDV.form.address)}</dd>
              <dt>Phone</dt><dd>${escapeHtml(IDV.form.phone)}</dd>
              <dt>Email</dt><dd>${escapeHtml(IDV.form.email)}</dd>
            </dl>
          </div>
          <div class="med-card">
            <h3>Coverage</h3>
            <dl class="med-dl">
              <dt>Part A — Hospital</dt><dd><span class="med-pill med-pill-ok">Active</span> since 04/01/2023</dd>
              <dt>Part B — Medical</dt><dd><span class="med-pill med-pill-ok">Active</span> since 04/01/2023</dd>
              <dt>Part D — Drugs</dt><dd>Aetna SilverScript SmartSaver</dd>
              <dt>Medigap</dt><dd>Plan G — Mutual of Omaha</dd>
            </dl>
          </div>
          <div class="med-card med-card-wide">
            <h3>Recent claims</h3>
            <table class="med-table">
              <thead><tr><th>Date</th><th>Provider</th><th>Service</th><th>Billed</th><th>You may owe</th><th>Status</th></tr></thead>
              <tbody>
                <tr><td>05/02/2026</td><td>Sibley Memorial Hospital</td><td>Annual wellness visit</td><td>$284.00</td><td>$0.00</td><td><span class="med-pill med-pill-ok">Processed</span></td></tr>
                <tr><td>04/18/2026</td><td>Quest Diagnostics</td><td>Comprehensive metabolic panel</td><td>$62.40</td><td>$0.00</td><td><span class="med-pill med-pill-ok">Processed</span></td></tr>
                <tr><td>03/30/2026</td><td>Dr. Lina Park, MD</td><td>Cardiology follow-up</td><td>$310.00</td><td>$42.00</td><td><span class="med-pill med-pill-ok">Processed</span></td></tr>
                <tr><td>03/12/2026</td><td>CVS Pharmacy #4421</td><td>Atorvastatin 20mg (90-day)</td><td>$18.00</td><td>$5.00</td><td><span class="med-pill med-pill-warn">Pending</span></td></tr>
              </tbody>
            </table>
          </div>
          <div class="med-card">
            <h3>Prescriptions</h3>
            <ul class="med-list">
              <li><strong>Atorvastatin 20 mg</strong><span class="muted">Refill on 06/10/2026</span></li>
              <li><strong>Lisinopril 10 mg</strong><span class="muted">Refill on 06/22/2026</span></li>
              <li><strong>Metformin 500 mg</strong><span class="muted">Refill on 07/04/2026</span></li>
            </ul>
          </div>
          <div class="med-card">
            <h3>Upcoming appointments</h3>
            <ul class="med-list">
              <li><strong>Cardiology — Dr. Park</strong><span class="muted">06/04/2026 &middot; 10:30 AM</span></li>
              <li><strong>Annual flu vaccine</strong><span class="muted">09/15/2026 &middot; Walk-in</span></li>
            </ul>
          </div>
        </section>
      </div>`;
  }
  function idvWireRecords(page) {
    const lo = page.querySelector('#med-logout');
    if (lo) lo.addEventListener('click', () => {
      IDV.phase = 'home';
      IDV.step = 0;
      IDV.selectedBank = null;
      IDV.bankConnected = false;
      IDV.bankConsentGiven = false;
      IDV.bankModalOpen = false;
      IDV.cardConsent = false;
      IDV.cardAuthorizing = false;
      // passkeyChoice intentionally NOT reset on logout — passkeys persist on device
      idvRender();
    });
  }

  function idvRenderBts() {
    const inModal = !!document.getElementById('idv-fullscreen-modal');
    const el = document.getElementById(inModal ? 'idv-modal-bts' : 'idv-bts');
    if (!el) return;
    const s = idvSignals(IDV.step);
    el.innerHTML = `
      <div class="idv-bts-inner">
        <div class="idv-bts-head">
          <span class="idv-bts-tag">BEHIND THE SCENES</span>
          <h4>${escapeHtml(s.title)}</h4>
          <div class="idv-bts-provider">${escapeHtml(s.provider)}</div>
        </div>
        <ul class="idv-bts-list">
          ${s.items.map(([k, v]) => `
            <li><span class="idv-bts-k">${escapeHtml(k)}</span><span class="idv-bts-v">${escapeHtml(v)}</span></li>
          `).join('')}
        </ul>
        <div class="idv-bts-callout">${escapeHtml(s.callout)}</div>
        <p class="idv-bts-foot muted">Simulated data for illustration — no live API calls yet.</p>
      </div>
    `;
  }

  // ===================== Priceless Concierge (Specials) Use Case =====================

  function renderSpecials() {
    _renderCachedWebview('specials', 'specials-webview-frame', _appPath('/specials/index.html'), 'Priceless Concierge');
  }

  // ===================== Find A Card Use Case =====================
  // Rendered as a sandboxed iframe pointing to /findacard/index.html.
  // All Find A Card UI lives in usecases/findacard/ — edit there to change the look.

  function renderFindACard() {
    _renderCachedWebview('findacard', 'findacard-webview-frame', _appPath('/findacard/index.html'), 'Find A Card');
  }

  // ===================== The Wire Use Case =====================
  // Rendered as a sandboxed iframe pointing to /the_wire/index.html.
  // All The Wire UI lives in usecases/the_wire/ — edit there to change the look.

  function renderTheWire() {
    _renderCachedWebview('the_wire', 'the-wire-webview-frame', _appPath('/the_wire/index.html'), 'The Wire');
  }

  // ===================== Sonic Branding Use Case =====================
  // Rendered as a sandboxed iframe pointing to /sonic/index.html.
  // All sonic UI lives in usecases/sonic/ — edit there to change the look.

  function renderSonic() {
    _renderCachedWebview('sonic', 'sonic-webview-frame', _appPath('/sonic/index.html'), 'Sonic Branding');
  }

  function renderTxNotify() {
    _renderCachedWebview('txnotify', 'txnotify-webview-frame', _appPath('/txnotify/index.html'), 'Transaction Notifications Live');
  }

  // ---------------------------------------------------------------------
  // Use Case About panel & globe
  // ---------------------------------------------------------------------
  (function () {
    const aboutBtn   = document.getElementById('uc-about-btn');
    const aboutPanel = document.getElementById('uc-about-panel');
    const workbench  = document.getElementById('uc-workbench');
    const contentSec = document.getElementById('uc-content-section');

    function ucShowAbout() {
      document.querySelectorAll('[data-uc-id]').forEach(b => b.classList.remove('active'));
      if (aboutBtn)   aboutBtn.classList.add('active');
      if (aboutPanel) aboutPanel.classList.remove('hidden');
      if (workbench)  workbench.classList.add('hidden');
      if (contentSec) contentSec.classList.add('uc--about');
      const sidebarApis = document.getElementById('uc-sidebar-apis');
      if (sidebarApis) sidebarApis.classList.add('hidden');
      const editBtnTop = document.getElementById('global-edit-btn');
      if (editBtnTop) editBtnTop.classList.add('hidden');
    }

    function ucShowWorkbench() {
      if (aboutBtn)   aboutBtn.classList.remove('active');
      if (aboutPanel) aboutPanel.classList.add('hidden');
      if (workbench)  workbench.classList.remove('hidden');
      if (contentSec) contentSec.classList.remove('uc--about');
      const editBtnTop = document.getElementById('global-edit-btn');
      if (editBtnTop && !SERVER_MODE) editBtnTop.classList.remove('hidden');
    }

    if (aboutBtn) aboutBtn.addEventListener('click', ucShowAbout);
    window._showUcWorkbench = ucShowWorkbench;

    // Globe animation
    const canvas = document.getElementById('uc-globe');
    if (canvas) {
      const ctx = canvas.getContext('2d');
      const SIZE = 820, RADIUS = SIZE * 0.32, CX = SIZE / 2, CY = SIZE / 2;
      const SPEED = 0.003, TOTAL_DOTS = 90;
      const pts = [];
      for (let i = 0; i < TOTAL_DOTS; i++) {
        const phi = Math.acos(-1 + (2 * i) / TOTAL_DOTS);
        const theta = Math.sqrt(TOTAL_DOTS * Math.PI) * phi;
        pts.push({ x: Math.cos(theta) * Math.sin(phi), y: Math.sin(theta) * Math.sin(phi), z: Math.cos(phi) });
      }
      let rot = 0, last = null;
      function renderUcGlobe(ts) {
        const delta = last ? Math.min((ts - last) / 16.667, 2) : 1;
        last = ts;
        ctx.clearRect(0, 0, SIZE, SIZE);
        const gOpacity = 0.18;
        ctx.lineWidth = 0.9;
        for (let lat = -80; lat <= 80; lat += 20) {
          const lR = (lat * Math.PI) / 180;
          for (let seg = 0; seg < 360; seg += 5) {
            const l0 = ((seg * Math.PI) / 180) + rot;
            const l1 = (((seg + 5) * Math.PI) / 180) + rot;
            const z0 = Math.cos(lR) * Math.sin(l0), z1 = Math.cos(lR) * Math.sin(l1);
            const a = gOpacity * Math.max(0, Math.min(1, ((z0 + z1) / 2 + 0.4) / 0.8));
            if (a < 0.005) continue;
            const s0 = 1 / (1.8 - z0), s1 = 1 / (1.8 - z1);
            ctx.strokeStyle = `rgba(255,110,20,${a})`;
            ctx.beginPath();
            ctx.moveTo(CX + Math.cos(lR) * Math.cos(l0) * RADIUS * s0, CY + Math.sin(lR) * RADIUS * s0);
            ctx.lineTo(CX + Math.cos(lR) * Math.cos(l1) * RADIUS * s1, CY + Math.sin(lR) * RADIUS * s1);
            ctx.stroke();
          }
        }
        for (let lon = 0; lon < 360; lon += 20) {
          for (let seg = -88; seg < 90; seg += 5) {
            const l0 = (seg * Math.PI) / 180, l1 = ((seg + 5) * Math.PI) / 180;
            const lR = ((lon * Math.PI) / 180) + rot;
            const z0 = Math.cos(l0) * Math.sin(lR), z1 = Math.cos(l1) * Math.sin(lR);
            const a = gOpacity * Math.max(0, Math.min(1, ((z0 + z1) / 2 + 0.4) / 0.8));
            if (a < 0.005) continue;
            const s0 = 1 / (1.8 - z0), s1 = 1 / (1.8 - z1);
            ctx.strokeStyle = `rgba(255,110,20,${a})`;
            ctx.beginPath();
            ctx.moveTo(CX + Math.cos(l0) * Math.cos(lR) * RADIUS * s0, CY + Math.sin(l0) * RADIUS * s0);
            ctx.lineTo(CX + Math.cos(l1) * Math.cos(lR) * RADIUS * s1, CY + Math.sin(l1) * RADIUS * s1);
            ctx.stroke();
          }
        }
        const projected = pts.map(p => {
          const rx = p.x * Math.cos(rot) - p.z * Math.sin(rot);
          const rz = p.x * Math.sin(rot) + p.z * Math.cos(rot);
          const sc = 1 / (1.8 - rz);
          const fade = Math.max(0, Math.min(1, (rz + 0.2) / 0.4));
          return { px: CX + rx * RADIUS * sc, py: CY + p.y * RADIUS * sc, rz, sc, alpha: 0.15 + fade * 0.75 };
        });
        projected.filter(p => p.rz > -0.18).sort((a, b) => a.rz - b.rz).forEach(p => {
          const g = Math.round(110 + p.alpha * 40);
          ctx.shadowColor = `rgba(255,80,0,${p.alpha * 0.8})`;
          ctx.shadowBlur = 8 * p.sc;
          ctx.fillStyle = `rgba(255,${g},20,${p.alpha})`;
          ctx.beginPath();
          ctx.arc(p.px, p.py, 2.5 * p.sc, 0, Math.PI * 2);
          ctx.fill();
        });
        ctx.shadowBlur = 0;
        rot += SPEED * delta;
        requestAnimationFrame(renderUcGlobe);
      }
      requestAnimationFrame(renderUcGlobe);
    }

    // Set initial state
    ucShowAbout();
  })();

  document.querySelectorAll("[data-uc-id]").forEach((btn) => {
    btn.addEventListener("click", () => {
      if (_isNonUsBlockedUseCaseById(btn.dataset.ucId)) return;
      // Close fullscreen mode before switching use cases.
      document.querySelector('.uc-fullscreen-reduce-btn')?.click();
      if (window._showUcWorkbench) window._showUcWorkbench();
      document.querySelectorAll("[data-uc-id]").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      renderUseCase(btn.dataset.ucId);
    });
  });

  // -----------------------------------------------------------------------
  // Generic use-case full-screen popout
  // -----------------------------------------------------------------------
  (function () {
    const popoutBtn = document.getElementById('uc-popout-btn');
    if (!popoutBtn) return;

    let _onKey = null;

    function ucOpenFullscreen() {
      const workbench = document.getElementById('uc-workbench');
      if (!workbench || document.getElementById('uc-fullscreen-topbar')) return;

      const topbar = document.createElement('div');
      topbar.id = 'uc-fullscreen-topbar';
      topbar.className = 'uc-fullscreen-topbar';
      const titleText = (document.getElementById('uc-title') || {}).textContent || 'Use Case';
      topbar.innerHTML = `
        <span class="uc-fullscreen-title">${escapeHtml(titleText)}</span>
        <div class="uc-fullscreen-actions">
          <button class="theme-toggle uc-fullscreen-theme-toggle" type="button" aria-pressed="false" aria-label="Switch to light theme" title="Switch to light theme">
            <span class="theme-toggle-track" aria-hidden="true">
              <span class="theme-toggle-option theme-toggle-option--dark">Dark</span>
              <span class="theme-toggle-option theme-toggle-option--light">Light</span>
              <span class="theme-toggle-thumb"></span>
            </span>
          </button>
          <button class="uc-fullscreen-reduce-btn">
            <svg width="14" height="14" viewBox="0 0 15 15" fill="none"><path d="M5 10L1 14M1 14h4M1 14v-4M10 5l4-4M14 4V1M14 1h-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
            Reduce
          </button>
        </div>
      `;
      workbench.classList.add('uc-workbench--fullscreen');
      workbench.insertBefore(topbar, workbench.firstChild);
      topbar.querySelector('.uc-fullscreen-theme-toggle')?.addEventListener('click', _toggleThemeMode);
      _applyThemeMode(_currentThemeMode());

      // Dismiss handlers
      const dismiss = ucCloseFullscreen;
      topbar.querySelector('.uc-fullscreen-reduce-btn').addEventListener('click', dismiss);
      _onKey = (e) => { if (e.key === 'Escape') dismiss(); };
      document.addEventListener('keydown', _onKey);
    }

    function ucCloseFullscreen() {
      const workbench = document.getElementById('uc-workbench');
      const topbar = document.getElementById('uc-fullscreen-topbar');
      if (!workbench || !topbar) return;
      topbar.remove();
      workbench.classList.remove('uc-workbench--fullscreen');
      if (_onKey) { document.removeEventListener('keydown', _onKey); _onKey = null; }
    }

    popoutBtn.addEventListener('click', ucOpenFullscreen);
  })();

  // ---------------------------------------------------------------------
  // Init
  // ---------------------------------------------------------------------
  // Wire API Calls FAB and drawer
  const _fabBtn = $('api-calls-fab');
  if (_fabBtn) _fabBtn.addEventListener('click', () => { apiCallsToggle(); });
  const _acClose = $('api-calls-close');
  if (_acClose) _acClose.addEventListener('click', apiCallsClose);
  const _acClear = $('api-calls-clear');
  if (_acClear) _acClear.addEventListener('click', () => { apiCallsClear(); });

  // Wire APIs tab Python snippets FAB and modal.
  const _snipFab = $('apis-snippets-fab');
  if (_snipFab) _snipFab.addEventListener('click', () => { apisSnippetsToggle(); });
  const _snipClose = $('apis-snippets-close');
  if (_snipClose) _snipClose.addEventListener('click', apisSnippetsClose);
  // Click on the dimmed area outside the modal closes it.
  const _snipBackdrop = $('apis-snippets-backdrop');
  if (_snipBackdrop) _snipBackdrop.addEventListener('click', (e) => {
    if (e.target === _snipBackdrop) apisSnippetsClose();
  });
  // Escape closes when the modal is open.
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && apisSnippetsIsVisible()) apisSnippetsClose();
  });
  // Let the snippets drawer read the live workbench selection.
  initApisSnippets({
    getCurrentApiId: () => getCurrentApiId(),
    getCurrentOpId: () => getCurrentOpId(),
  });
  // Let the Open Finance setup modal jump into the workbench.
  initOfinSetupModal({ selectOp });
  // Wire the request/response Show/Hide Headers toggles.
  initHeaderToggles();
  // Wire the per-API Sim/Live simulator toggle.
  initSimToggle();

  if (getCurrentApiId()) renderApi();
  if (USE_CASES.length) {
    _startPolling(); // begin polling for badge updates immediately
  }

  // ===========================================================================
  // Config Panel
  // ===========================================================================
  (function () {
    const modal     = document.getElementById('cfg-modal');
    const overlay   = document.getElementById('cfg-overlay');
    const body      = document.getElementById('cfg-panel-body');
    const footer    = document.getElementById('cfg-panel-footer');
    const lockBtn   = document.getElementById('cfg-lock-btn');
    const lockIcon  = document.getElementById('cfg-lock-icon');
    const closeBtn  = document.getElementById('cfg-close-btn');
    const cancelBtn = document.getElementById('cfg-cancel-btn');
    const saveBtn   = document.getElementById('cfg-save-btn');
    const triggerBtn = document.getElementById('cfg-trigger-btn');
    const tooltip   = document.getElementById('cfg-tooltip');
    const exportBtn  = document.getElementById('cfg-export-btn');
    const importBtn  = document.getElementById('cfg-import-btn');
    const importFile = document.getElementById('cfg-import-file');

    // ── Auto Provision Keys ──────────────────────────────────────────────────
    const autogenBtn        = document.getElementById('cfg-autogen-btn');
    const autogenBanner     = document.getElementById('cfg-autogen-banner');
    const autogenCancel     = document.getElementById('cfg-autogen-cancel');
    const autogenConfirm    = document.getElementById('cfg-autogen-confirm');
    let activeTooltipTarget = null;

    function autogenShowBanner() {
      if (autogenBanner) autogenBanner.classList.remove('cfg-hidden');
    }
    function autogenHideBanner() {
      if (autogenBanner) autogenBanner.classList.add('cfg-hidden');
    }
    autogenBtn    && autogenBtn.addEventListener('click', autogenShowBanner);
    autogenCancel && autogenCancel.addEventListener('click', autogenHideBanner);
    autogenConfirm && autogenConfirm.addEventListener('click', function () {
      autogenHideBanner();
      cfgClose();
      document.dispatchEvent(new CustomEvent('prov:open-select'));
    });

    let _groups = [];       // loaded config groups
    let _unlocked = false;  // edit mode flag
    let _pending = {};      // { KEY: newValue } for unsaved file uploads

    // ── Export ──────────────────────────────────────────────────────────────
    exportBtn && exportBtn.addEventListener('click', function () {
      exportBtn.disabled = true;
      exportBtn.textContent = 'Exporting…';
      const a = document.createElement('a');
      a.href = _appPath('/config/export');
      a.download = 'vima-config.zip';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      setTimeout(function () {
        exportBtn.disabled = false;
        exportBtn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg> Export';
      }, 1500);
    });

    // ── Import ──────────────────────────────────────────────────────────────
    importBtn && importBtn.addEventListener('click', function () { importFile && importFile.click(); });
    importFile && importFile.addEventListener('change', function () {
      const file = importFile.files[0];
      if (!file) return;
      if (!confirm('This will overwrite your existing .env and key files with the contents of the zip. Continue?')) {
        importFile.value = '';
        return;
      }
      importBtn.disabled = true;
      importBtn.textContent = 'Importing…';
      const fd = new FormData();
      fd.append('file', file);
      fetch('/config/import', { method: 'POST', body: fd })
        .then(function (r) { return r.json(); })
        .then(function (data) {
          if (data.error) { alert('Import failed: ' + data.error); return; }
          alert('Imported ' + (data.imported || []).length + ' file(s). Reload the page for changes to take effect.');
          cfgLoad();
        })
        .catch(function () { alert('Import failed.'); })
        .finally(function () {
          importBtn.disabled = false;
          importBtn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg> Import';
          importFile.value = '';
        });
    });


    // ── Open / close ────────────────────────────────────────────────────────
    function cfgOpen() {
      if (SERVER_MODE) return;
      modal.classList.remove('cfg-hidden');
      document.body.style.overflow = 'hidden';
      cfgLoad();
    }
    function cfgClose() {
      modal.classList.add('cfg-hidden');
      document.body.style.overflow = '';
      if (_unlocked) cfgSetLocked(true);
      _pending = {};
    }

    if (triggerBtn && SERVER_MODE) {
      triggerBtn.title = SERVER_MODE_TOOLTIP;
    }
    triggerBtn && triggerBtn.addEventListener('click', cfgOpen);
    closeBtn && closeBtn.addEventListener('click', cfgClose);
    overlay && overlay.addEventListener('click', cfgClose);

    // ── Global Vima Chat edit modal ──────────────────────────────────────────
    (function () {
      const editBtn   = document.getElementById('global-edit-btn');
      const editModal = document.getElementById('global-edit-modal');
      const editClose = document.getElementById('global-edit-modal-close');
      const editIframe = document.getElementById('global-edit-modal-iframe');

      if (editBtn && SERVER_MODE) {
        editBtn.title = SERVER_MODE_TOOLTIP;
        editBtn.setAttribute('aria-disabled', 'true');
        editBtn.classList.add('hidden');
      }

      function openGlobalEdit() {
        if (SERVER_MODE) return;
        if (!editModal || !editIframe) return;

        // Build URL based on what is currently selected in the explorer.
        // Note: Vima Chat runs on 127.0.0.1:3333 (loopback only) and is
        // proxied through this app at /chat/* so it is never accessible as
        // a standalone web service.
        let url = _appPath('/chat/');
        const activeTab = document.querySelector('.top-tab.active')?.dataset?.topTab;
        if (activeTab === 'usecases' && _currentUcId) {
          const uc = USE_CASES.find(u => u.id === _currentUcId);
          if (uc) {
            url += '?type=usecases&item=' + encodeURIComponent(uc.name);
            if (uc.directory) url += '&cwd=' + encodeURIComponent(uc.directory);
          }
        } else if (activeTab === 'apis' && getCurrentApiId()) {
          const api = APIS.find(a => a.id === getCurrentApiId());
          if (api) {
            url += '?type=apis&item=' + encodeURIComponent(api.name);
            if (api.directory) url += '&cwd=' + encodeURIComponent(api.directory);
          }
        }

        editIframe.addEventListener('load', () => {
          _postThemeToEmbeddedFrame(editIframe, _currentThemeMode());
        }, { once: true });
        editIframe.src = url;
        editModal.style.display = 'flex';
        requestAnimationFrame(() => editModal.classList.add('tc-modal-backdrop--open'));
      }

      function closeGlobalEdit() {
        if (!editModal) return;
        // Auto-refresh the active use-case webview so changes appear immediately
        const activeFrame = document.querySelector('.sonic-webview-frame');
        if (activeFrame) activeFrame.src = activeFrame.src;
        editModal.classList.remove('tc-modal-backdrop--open');
        editModal.addEventListener('transitionend', () => {
          editModal.style.display = 'none';
          if (editIframe) editIframe.src = '';
          // Clear banner for next session
          const banner = document.getElementById('global-edit-banner');
          if (banner) { banner.className = 'tc-modal-banner tc-modal-banner--hidden'; banner.innerHTML = ''; }
        }, { once: true });
      }

      // ── Listen for done/restart signals from the chat iframe ───────────────
      window.addEventListener('message', function (e) {
        if (!e.data || e.data.type !== 'vima:chat-done') return;
        const text   = (e.data.response || '').toLowerCase();
        const banner = document.getElementById('global-edit-banner');
        if (!banner) return;

        const needsRestart = /restart(\s+the)?\s+(server|app|flask|vima)|python\s+app\.py|re-?start/.test(text);
        const needsHardRefresh = /hard[\s-]refresh|ctrl\s*\+\s*shift|cmd\s*\+\s*shift|force[\s-]refresh/.test(text);

        if (needsRestart) {
          banner.className = 'tc-modal-banner tc-modal-banner--restart';
          banner.innerHTML = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg> Server restart required — run <code style="background:rgba(255,255,255,0.1);padding:1px 4px;border-radius:3px">python app.py</code> to apply changes.`;
        } else if (needsHardRefresh) {
          banner.className = 'tc-modal-banner tc-modal-banner--refresh';
          banner.innerHTML = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg> Hard refresh recommended — press <code style="background:rgba(255,255,255,0.1);padding:1px 4px;border-radius:3px">Ctrl+Shift+R</code> (Win/Linux) or <code style="background:rgba(255,255,255,0.1);padding:1px 4px;border-radius:3px">Cmd+Shift+R</code> (Mac) after closing.`;
        } else {
          banner.className = 'tc-modal-banner tc-modal-banner--done';
          banner.innerHTML = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> Done — page refreshed automatically.`;
          // Auto-hide after 4s if no restart needed
          setTimeout(() => {
            if (banner.classList.contains('tc-modal-banner--done')) {
              banner.className = 'tc-modal-banner tc-modal-banner--hidden';
              banner.innerHTML = '';
            }
          }, 4000);
        }
      });

      editBtn   && editBtn.addEventListener('click', openGlobalEdit);
      editClose && editClose.addEventListener('click', closeGlobalEdit);
      editModal && editModal.addEventListener('click', e => {
        if (e.target === editModal) closeGlobalEdit();
      });
      document.addEventListener('keydown', e => {
        if (e.key === 'Escape' && editModal && editModal.style.display !== 'none') closeGlobalEdit();
      });
    })();
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !modal.classList.contains('cfg-hidden')) cfgClose();
    });

    // ── Lock / unlock ────────────────────────────────────────────────────────
    function cfgSetLocked(locked) {
      _unlocked = !locked;
      lockBtn.classList.toggle('unlocked', !locked);
      lockIcon.innerHTML = locked
        ? '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path>'
        : '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 9.9-1"></path>';
      lockBtn.title = locked ? 'Unlock to edit' : 'Lock (discard edits)';
      footer.classList.toggle('cfg-hidden', locked);
      if (_groups.length) cfgRender(_groups);
      if (locked) _pending = {};
    }

    lockBtn && lockBtn.addEventListener('click', function () {
      cfgSetLocked(_unlocked); // toggle
    });

    cancelBtn && cancelBtn.addEventListener('click', function () {
      cfgSetLocked(true);
      _pending = {};
    });

    // ── Load config from server ──────────────────────────────────────────────
    function cfgLoad() {
      body.innerHTML = '<div class="cfg-loading">Loading configuration\u2026</div>';
      fetch('/config', { cache: 'no-store' })
        .then(function (r) { return r.json(); })
        .then(function (data) {
          _groups = data.groups || [];
          cfgRender(_groups);
        })
        .catch(function (err) {
          body.innerHTML = '<div class="cfg-loading" style="color:var(--err)">Failed to load config.</div>';
        });
    }

    // ── Render ───────────────────────────────────────────────────────────────
    function cfgRender(groups) {
      body.innerHTML = '';
      groups.forEach(function (g) {
        const section = document.createElement('div');
        section.className = 'cfg-group';
        section.dataset.groupId = g.id;

        const hdr = document.createElement('div');
        hdr.className = 'cfg-group-header';
        hdr.innerHTML =
          '<div style="display:flex;align-items:baseline;gap:6px">' +
            '<span class="cfg-group-title">' + escHtml(g.title) + '</span>' +
            '<span class="cfg-group-subtitle">' + escHtml(g.subtitle) + '</span>' +
          '</div>' +
          '<a class="cfg-group-docs" href="' + escHtml(g.docs_url) + '" target="_blank" rel="noopener">' +
            'Docs ↗' +
          '</a>';
        section.appendChild(hdr);

        g.fields.forEach(function (f) {
          section.appendChild(cfgFieldEl(f));
        });

        body.appendChild(section);
      });
    }

    function cfgFieldEl(f) {
      const row = document.createElement('div');
      row.className = 'cfg-field';
      row.dataset.key = f.key;

      // Label
      const lbl = document.createElement('div');
      lbl.className = 'cfg-field-label';
      lbl.textContent = f.label;
      row.appendChild(lbl);

      // Value / control
      const mid = document.createElement('div');
      mid.style.minWidth = '0';

      if (f.type === 'file') {
        mid.appendChild(cfgFileEl(f));
      } else if (_unlocked) {
        const inp = document.createElement('input');
        inp.type = f.type === 'password' ? 'text' : 'text'; // always text in edit mode so value is visible
        inp.className = 'cfg-input';
        inp.value = _pending[f.key] !== undefined ? _pending[f.key] : f.value;
        inp.placeholder = f.value ? '' : 'Not set';
        inp.dataset.key = f.key;
        mid.appendChild(inp);
      } else {
        const val = document.createElement('div');
        if (!f.value) {
          val.className = 'cfg-field-val empty';
          val.textContent = 'Not configured';
        } else if (f.type === 'password') {
          val.className = 'cfg-field-val masked';
          val.textContent = '\u2022'.repeat(12);
          val.title = '(hidden) — unlock to view';
        } else {
          val.className = 'cfg-field-val';
          val.textContent = f.value;
        }
        mid.appendChild(val);
      }
      row.appendChild(mid);

      // Info icon
      const info = document.createElement('button');
      info.className = 'cfg-info-btn';
      info.textContent = 'i';
      info.setAttribute('aria-label', 'Info: ' + f.label);
      info.addEventListener('mouseenter', function (e) { cfgTooltipShow(f.info, e); });
      info.addEventListener('mouseleave', cfgTooltipHide);
      info.addEventListener('click', function (e) {
        e.stopPropagation();
        cfgTooltipShow(f.info, e);
      });
      row.appendChild(info);

      return row;
    }

    function cfgFileEl(f) {
      const wrap = document.createElement('div');
      wrap.className = 'cfg-file-row';

      const currentPath = _pending[f.key] !== undefined ? _pending[f.key] : f.value;
      const nameEl = document.createElement(_unlocked ? 'input' : 'span');
      nameEl.className = 'cfg-file-name' + (currentPath ? ' set' : '');

      if (_unlocked) {
        nameEl.type = 'text';
        nameEl.value = currentPath || '';
        nameEl.placeholder = 'config/keys/your-key-file.key';
        nameEl.addEventListener('input', function () {
          const v = (nameEl.value || '').trim();
          _pending[f.key] = v;
          nameEl.classList.toggle('set', !!v);
        });
      } else {
        nameEl.textContent = currentPath
          ? currentPath
          : 'No file set';
      }

      wrap.appendChild(nameEl);

      if (_unlocked) {
        const fileInput = document.createElement('input');
        fileInput.type = 'file';
        fileInput.accept = '.p12,.pkcs12,.pem,.key';
        fileInput.className = 'cfg-file-input';

        const uploadBtn = document.createElement('button');
        uploadBtn.className = 'cfg-upload-btn';
        uploadBtn.textContent = currentPath ? 'Replace' : 'Upload key file';
        uploadBtn.addEventListener('click', function () { fileInput.click(); });

        fileInput.addEventListener('change', function () {
          const file = fileInput.files[0];
          if (!file) return;
          const fd = new FormData();
          fd.append('file', file);
          uploadBtn.textContent = 'Uploading…';
          uploadBtn.disabled = true;
          fetch('/config/upload-key', { method: 'POST', body: fd })
            .then(function (r) { return r.json(); })
            .then(function (data) {
              if (data.error) {
                alert('Upload failed: ' + data.error);
              } else {
                _pending[f.key] = data.path;
                if (_unlocked) {
                  nameEl.value = data.path;
                  nameEl.classList.add('set');
                } else {
                  nameEl.textContent = data.path;
                  nameEl.className = 'cfg-file-name set';
                }
              }
            })
            .catch(function () { alert('Upload failed.'); })
            .finally(function () {
              uploadBtn.textContent = 'Replace';
              uploadBtn.disabled = false;
            });
        });

        wrap.appendChild(fileInput);
        wrap.appendChild(uploadBtn);
      }

      return wrap;
    }

    // ── Save ─────────────────────────────────────────────────────────────────
    saveBtn && saveBtn.addEventListener('click', function () {
      const updates = Object.assign({}, _pending);

      // Collect text/password inputs
      body.querySelectorAll('input.cfg-input[data-key]').forEach(function (inp) {
        updates[inp.dataset.key] = inp.value;
      });

      if (!Object.keys(updates).length) { cfgSetLocked(true); return; }

      saveBtn.disabled = true;
      saveBtn.textContent = 'Saving…';

      fetch('/config', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ updates: updates }),
      })
        .then(function (r) { return r.json(); })
        .then(function (data) {
          if (data.error) { alert('Save failed: ' + data.error); return; }
          // Flash saved rows
          (data.saved || []).forEach(function (key) {
            const row = body.querySelector('.cfg-field[data-key="' + key + '"]');
            if (row) { row.classList.remove('saved'); void row.offsetWidth; row.classList.add('saved'); }
          });
          _pending = {};
          cfgSetLocked(true);
          cfgLoad(); // reload to show updated values
        })
        .catch(function () { alert('Save failed.'); })
        .finally(function () {
          saveBtn.disabled = false;
          saveBtn.textContent = 'Save Changes';
        });
    });

    // ── Tooltip ──────────────────────────────────────────────────────────────
    function cfgTooltipShow(text, e) {
      if (!text) return;
      tooltip.textContent = text;
      tooltip.classList.remove('cfg-hidden');
      cfgTooltipPos(e);
    }
    function cfgTooltipPos(e) {
      const tx = e.clientX + 14;
      const ty = e.clientY + 14;
      const tw = tooltip.offsetWidth;
      const th = tooltip.offsetHeight;
      tooltip.style.left = (tx + tw > window.innerWidth - 8 ? tx - tw - 28 : tx) + 'px';
      tooltip.style.top  = (ty + th > window.innerHeight - 8 ? ty - th - 28 : ty) + 'px';
    }
    function cfgTooltipHide() { tooltip.classList.add('cfg-hidden'); }

    function cfgTooltipRestoreTitle(el) {
      if (!el) return;
      const storedTitle = el.getAttribute('data-tooltip-title');
      if (storedTitle != null) {
        el.setAttribute('title', storedTitle);
        el.removeAttribute('data-tooltip-title');
      }
    }

    function cfgTooltipTextFor(el) {
      if (!el) return '';
      return el.getAttribute('data-tooltip')
        || el.getAttribute('data-tooltip-title')
        || el.getAttribute('title')
        || '';
    }

    function cfgTooltipShowForTarget(target, e) {
      if (!target) return;
      const text = cfgTooltipTextFor(target);
      if (!text) return;
      if (target.hasAttribute('title')) {
        target.setAttribute('data-tooltip-title', target.getAttribute('title'));
        target.removeAttribute('title');
      }
      activeTooltipTarget = target;
      cfgTooltipShow(text, e);
    }

    function cfgTooltipHideForTarget(target) {
      if (!target) return;
      cfgTooltipRestoreTitle(target);
      if (activeTooltipTarget === target) activeTooltipTarget = null;
      cfgTooltipHide();
    }

    function cfgTooltipReset() {
      if (activeTooltipTarget) {
        cfgTooltipHideForTarget(activeTooltipTarget);
        return;
      }
      cfgTooltipHide();
    }

    document.addEventListener('mousemove', function (e) {
      if (!tooltip.classList.contains('cfg-hidden')) cfgTooltipPos(e);
    });
    document.addEventListener('click', function () { cfgTooltipReset(); });
    document.addEventListener('scroll', cfgTooltipReset, true);
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) cfgTooltipReset();
    });
    window.addEventListener('blur', cfgTooltipReset);

    document.addEventListener('mouseover', function (e) {
      const target = e.target.closest('[data-tooltip], [title]');
      if (!target || target === tooltip || tooltip.contains(target)) return;
      if (target.closest('#uc-body')) return;
      if (activeTooltipTarget && activeTooltipTarget !== target) {
        cfgTooltipHideForTarget(activeTooltipTarget);
      }
      if (activeTooltipTarget === target) return;
      cfgTooltipShowForTarget(target, e);
    });

    document.addEventListener('mouseout', function (e) {
      if (!activeTooltipTarget) return;
      const related = e.relatedTarget;
      if (related && activeTooltipTarget.contains(related)) return;
      if (e.target === activeTooltipTarget || activeTooltipTarget.contains(e.target)) {
        cfgTooltipHideForTarget(activeTooltipTarget);
      }
    });

    document.addEventListener('focusin', function (e) {
      const target = e.target.closest('[data-tooltip], [title]');
      if (!target) return;
      if (target.closest('#uc-body')) return;
      if (activeTooltipTarget && activeTooltipTarget !== target) {
        cfgTooltipHideForTarget(activeTooltipTarget);
      }
      const rect = target.getBoundingClientRect();
      cfgTooltipShowForTarget(target, {
        clientX: rect.left + Math.min(rect.width / 2, 24),
        clientY: rect.bottom,
      });
    });

    document.addEventListener('focusout', function (e) {
      if (!activeTooltipTarget) return;
      if (e.target === activeTooltipTarget || activeTooltipTarget.contains(e.target)) {
        cfgTooltipHideForTarget(activeTooltipTarget);
      }
    });

    function escHtml(s) {
      return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
    }
  }());

  // ===================== Test Chat Use Case =====================
  // Rendered as a sandboxed iframe pointing to /testchat/testchat.html.
  // All Test Chat UI lives in usecases/testchat/ — edit there to change the look.

  function renderTestChat() {
    _renderCachedWebview('testchat', 'testchat-webview-frame', _appPath('/testchat/testchat.html'), 'Test Chat');
  }

})();
