// -------------------------------------------------------------------
// features/apiGuide.js
// API Guide compact single-step coach. Extracted verbatim from main.js.
// Sets window.ApiGuide (public surface preserved). Reads workbench state
// via imported currentApi() and drives selection via imported selectOp().
// -------------------------------------------------------------------
import { $ } from '../core/dom.js';
import { currentApi } from '../core/state.js';
import { selectOp } from '../workbench/core.js';

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
  export const ApiGuide = (function () {
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
