// -------------------------------------------------------------------
// workbench/core.js
// The API workbench's render/select/send core. These functions form a
// tightly mutually-recursive cluster (renderApi -> selectOp ->
// renderParams/restoreIo -> previewRequest, plus the send handler) and
// share the workbench selection state from core/state.js. Only renderApi
// and selectOp are needed by callers outside the cluster (the API sidebar
// click handler, the API Guide, the Open Finance setup modal, and the
// initial deep-link render); initSendHandler() wires the Send button.
//
// Extracted verbatim from main.js (Phase 5) -- indentation preserved to
// keep the move byte-faithful; no logic changes.
// -------------------------------------------------------------------
import { $ } from '../core/dom.js';
import { _nativeFetch } from '../core/net.js';
import { escapeHtml } from '../core/html.js';
import { APIS, NON_US_MODE } from '../core/env.js';
import {
  getCurrentApiId, getCurrentOpId, setCurrentOpId,
  getCurrentState, setCurrentState, currentApi, currentOp,
  ioCache, lastOpByApi,
} from '../core/state.js';
import { _isNonUsBlockedApiId, _isNonUsBlockedUseCaseById } from '../core/region.js';
import { loadUseCases, getBundlesCache, getUseCasesCache } from '../core/catalog.js';
import {
  setStatus, _findFirstUrl, _findKey, fmt,
  renderIoPanel, updateHeaderToggleBtn, headersVisible, lastIoData,
} from './io.js';
import {
  _resetLaunchBanner, _showLaunchBannerPending,
  _showLaunchBanner, _buildTestCredentialsBlock,
} from './launchBanner.js';
import { fetchSimStatus } from './simToggle.js';
import { apisSnippetsRefreshOp } from '../features/apiSnippets.js';
import { showOfinSetupModal } from '../features/ofinSetupModal.js';

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
  export function renderApi() {
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
  export function selectOp(opId) {
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
    if (window.ApiGuide) window.ApiGuide.syncCurrentOp();
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
  export function initSendHandler() {
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
        window.ApiGuide.markOpDone(op.id);
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
  }
