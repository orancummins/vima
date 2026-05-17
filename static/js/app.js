(() => {
  const APIS = window.__APIS__ || [];
  const USE_CASES = window.__USE_CASES__ || [];

  const $ = (id) => document.getElementById(id);

  // -------------------------------------------------------------------
  // API Calls Logger — polls /api-call-log for outbound Mastercard calls
  // -------------------------------------------------------------------
  let API_CALLS_VISIBLE = false;
  const API_CALL_LOG = [];
  let _lastSeq = 0;
  let _pollTimer = null;
  let _currentUcId = null;

  function _startPolling() {
    if (_pollTimer) return;
    _pollTimer = setInterval(_pollApiLog, 1500);
    _pollApiLog(); // immediate first fetch
  }

  function _stopPolling() {
    if (_pollTimer) { clearInterval(_pollTimer); _pollTimer = null; }
  }

  function _pollApiLog() {
    _nativeFetch(`/api-call-log?since=${_lastSeq}`)
      .then(r => r.json())
      .then(d => {
        const newCalls = d.calls || [];
        if (newCalls.length) {
          newCalls.forEach(e => {
            API_CALL_LOG.unshift(e);
            if (e.seq > _lastSeq) _lastSeq = e.seq;
          });
          if (API_CALL_LOG.length > 50) API_CALL_LOG.length = 50;
          apiCallsRefresh();
        }
      })
      .catch(() => {});
  }

  // Keep native fetch reference for internal use
  const _nativeFetch = window.fetch.bind(window);

  function apiCallsRefresh() {
    const badge = $('api-calls-fab-badge');
    if (badge) {
      badge.textContent = API_CALL_LOG.length;
      badge.classList.toggle('hidden', API_CALL_LOG.length === 0);
    }
    const countEl = $('api-calls-count');
    if (countEl) countEl.textContent = API_CALL_LOG.length || '';
    if (!API_CALLS_VISIBLE) return;
    const body = $('api-calls-body');
    if (!body) return;
    if (!API_CALL_LOG.length) {
      body.innerHTML = `<p class="api-calls-empty">No API calls yet. Perform an action to see calls here.</p>`;
      return;
    }
    body.innerHTML = API_CALL_LOG.map((e, idx) => apiCallEntryHtml(e, idx)).join('');
    // Auto-expand the most recent (first) entry
    const firstEntry = body.querySelector('.api-calls-entry');
    if (firstEntry) firstEntry.classList.add('api-calls-entry--open');
    body.querySelectorAll('[data-expand-call]').forEach(el => {
      el.addEventListener('click', () => el.closest('.api-calls-entry').classList.toggle('api-calls-entry--open'));
    });
    body.querySelectorAll('[data-copy-call]').forEach(btn => {
      btn.addEventListener('click', () => {
        const entry = API_CALL_LOG[+btn.dataset.copyCall];
        if (!entry) return;
        navigator.clipboard.writeText(JSON.stringify({
          request: entry.requestBody, response: entry.responseBody,
        }, null, 2));
        btn.textContent = 'Copied';
        setTimeout(() => btn.textContent = 'Copy', 900);
      });
    });
  }

  function apiCallEntryHtml(e, idx) {
    // Show just the path+host portion nicely
    let displayUrl = e.url || '';
    try {
      const u = new URL(displayUrl);
      displayUrl = u.host + u.pathname + (u.search || '');
    } catch(_) {}
    const statusCls = e.status === null ? 'pending'
      : e.status === 'ERR' ? 'err'
      : e.status >= 200 && e.status < 300 ? 'ok' : 'bad';
    const elapsed = e.elapsed_ms != null ? `${e.elapsed_ms}ms` : '';
    const time = e.ts || '';
    return `
      <div class="api-calls-entry" data-seq="${e.seq}">
        <div class="api-calls-entry-head" data-expand-call>
          <span class="api-calls-method api-calls-method--${e.method.toLowerCase()}">${escapeHtml(e.method)}</span>
          <span class="api-calls-url" title="${escapeHtml(e.url)}">${escapeHtml(displayUrl)}</span>
          <span class="api-calls-status api-calls-status--${statusCls}">${e.status == null ? '…' : escapeHtml(String(e.status))}</span>
          <span class="api-calls-time">${escapeHtml(elapsed || time)}</span>
          <span class="api-calls-chevron">▾</span>
        </div>
        <div class="api-calls-entry-body">
          ${e.requestBody != null ? `<div class="api-calls-section"><div class="api-calls-section-label">Request body</div><pre class="api-calls-pre">${escapeHtml(JSON.stringify(e.requestBody, null, 2))}</pre></div>` : ''}
          <div class="api-calls-section">
            <div class="api-calls-section-label">Response${e.status ? ' · ' + e.status : ''}</div>
            ${e.responseBody !== null && e.responseBody !== undefined
              ? `<pre class="api-calls-pre">${escapeHtml(JSON.stringify(e.responseBody, null, 2))}</pre>`
              : `<p class="api-calls-pending">Waiting for response…</p>`}
          </div>
          <div class="api-calls-copy-row"><button class="api-calls-copy-btn" data-copy-call="${idx}">Copy</button></div>
        </div>
      </div>`;
  }

  function apiCallsOpen() {
    API_CALLS_VISIBLE = true;
    _startPolling();
    const drawer = $('api-calls-drawer');
    if (drawer) drawer.classList.remove('hidden');
    const fab = $('api-calls-fab');
    if (fab) {
      fab.classList.add('api-calls-fab--active');
      const lbl = fab.querySelector('.api-calls-fab-label');
      if (lbl) lbl.textContent = 'Hide Calls';
    }
    apiCallsRefresh();
  }

  function apiCallsClose() {
    API_CALLS_VISIBLE = false;
    // Keep polling for badge updates even when drawer is closed
    const drawer = $('api-calls-drawer');
    if (drawer) drawer.classList.add('hidden');
    const fab = $('api-calls-fab');
    if (fab) {
      fab.classList.remove('api-calls-fab--active');
      const lbl = fab.querySelector('.api-calls-fab-label');
      if (lbl) lbl.textContent = 'Show API Calls';
    }
  }

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
      return `<div class="uc-sidebar-api-badge ${configured ? 'configured' : 'unconfigured'}"><span class="uc-sidebar-api-dot"></span>${escapeHtml(name)}</div>`;
    }).join('');
    container.classList.remove('hidden');
  }

  const HTTP_REASONS = {
    100:"Continue",101:"Switching Protocols",200:"OK",201:"Created",202:"Accepted",
    204:"No Content",206:"Partial Content",301:"Moved Permanently",302:"Found",
    304:"Not Modified",400:"Bad Request",401:"Unauthorized",403:"Forbidden",
    404:"Not Found",405:"Method Not Allowed",406:"Not Acceptable",
    409:"Conflict",410:"Gone",422:"Unprocessable Entity",429:"Too Many Requests",
    500:"Internal Server Error",501:"Not Implemented",502:"Bad Gateway",
    503:"Service Unavailable",504:"Gateway Timeout",
  };
  function setStatus(code) {
    const el = $("resp-status");
    if (code == null) { el.textContent = ""; el.className = "status-pill"; el.title = ""; return; }
    const s = String(code);
    el.textContent = s;
    el.className = "status-pill s" + s[0];
    el.title = HTTP_REASONS[Number(code)] || "";
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
      $("panel-usecases").classList.toggle("hidden", tab !== "usecases");
      const fab = $('api-calls-fab');
      if (fab) fab.classList.toggle('hidden', tab !== 'usecases');
      if (tab !== 'usecases') { apiCallsClose(); _stopPolling(); }
      else _startPolling();
    });
  });

  // Home panel CTA buttons — switch to APIs or Use Cases tab
  document.querySelectorAll('.home-cta[data-switch-tab]').forEach(function(btn) {
    btn.addEventListener('click', function() {
      const tabBtn = document.querySelector('.top-tab[data-top-tab="' + btn.dataset.switchTab + '"]');
      if (tabBtn) tabBtn.click();
    });
  });

  // Honour ?tab=apis / ?tab=usecases from home page CTAs
  const _urlTab = new URLSearchParams(location.search).get('tab');
  if (_urlTab === 'usecases' || _urlTab === 'apis') {
    const btn = document.querySelector(`.top-tab[data-top-tab="${_urlTab}"]`);
    if (btn) btn.click();
  } else {
    document.body.style.overflow = 'hidden'; // home is the default tab
    const hdr = document.querySelector('.header');
    if (hdr) hdr.classList.add('header--home');
  }

  // ---------------------------------------------------------------------
  // API state
  // ---------------------------------------------------------------------
  let currentApiId = null;  // null = About panel shown; set when user selects an API
  let currentOpId = null;
  let currentState = {};

  // Cache of last request/response per (apiId, opId), plus last op per api.
  const ioCache = {};            // ioCache[apiId][opId] = { request, response, statusCode, hint }
  const lastOpByApi = {};        // lastOpByApi[apiId] = opId

  function currentApi() {
    return APIS.find((a) => a.id === currentApiId);
  }
  function currentOp() {
    const a = currentApi();
    if (!a) return null;
    return a.operations.find((o) => o.id === currentOpId);
  }

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
      const cfgBtn = document.getElementById('cfg-btn');
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
      document.querySelectorAll("[data-api-id]").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      currentApiId = btn.dataset.apiId;
      currentOpId = null;
      if (window._showApiWorkbench) window._showApiWorkbench();
      renderApi();
    });
  });

  // ---------------------------------------------------------------------
  // Render API
  // ---------------------------------------------------------------------
  function renderApi() {
    const api = currentApi();
    if (!api) return;
    $("api-title").textContent = api.name;
    $("api-desc").textContent = api.description || "";
    const docs = $("api-docs");
    if (api.docs_url) {
      docs.href = api.docs_url;
      docs.style.display = "inline-flex";
    } else {
      docs.style.display = "none";
    }

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
    fetch(`/explorer/${api.id}/state`)
      .then((r) => r.json())
      .then((d) => {
        currentState = d.state || {};
        renderStateStrip();
        // refresh param defaults if an op is open
        if (currentOpId) renderParams();
      })
      .catch(() => {});
  }

  function renderStateStrip() {
    const api = currentApi();
    const strip = $("state-strip");
    strip.innerHTML = "";
    const schema = api.state_schema || [];
    if (!api.configured) {
      const w = document.createElement("div");
      w.className = "state-pill";
      w.innerHTML = `<span class="k">⚠</span><span class="v">Not configured — check .env</span>`;
      w.style.borderColor = "#eb001b";
      w.style.color = "#a01010";
      strip.appendChild(w);
    }
    schema.forEach((s) => {
      const v = currentState[s.key];
      const pill = document.createElement("div");
      pill.className = "state-pill" + (v ? "" : " empty");
      pill.innerHTML = `<span class="k">${s.label}:</span><span class="v">${v || "—"}</span>`;
      strip.appendChild(pill);
    });
  }

  // ---------------------------------------------------------------------
  // Select operation
  // ---------------------------------------------------------------------
  function selectOp(opId) {
    currentOpId = opId;
    lastOpByApi[currentApiId] = opId;
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
  }

  function restoreIo() {
    const cached = (ioCache[currentApiId] || {})[currentOpId];
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
      $('op-hint').innerHTML = cached.hintHtml || '';    } else {
      lastIoData.request = null;
      lastIoData.response = null;
      $("req-body").textContent = "—";
      $("resp-body").textContent = "—";
      $("resp-status").textContent = "";
      $("resp-status").className = "status-pill";      $('resp-status').title = "";      $("op-hint").innerHTML = "";
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
        value = currentState[k] || "";
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
        const accounts = currentState.accounts || [];
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
    const cached = (ioCache[currentApiId] || {})[currentOpId];
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
    $("req-body").textContent = "Sending…";
    $("resp-body").textContent = "";
    $("resp-status").textContent = "";    $('resp-status').className = "status-pill";
    $('resp-status').title = "";    try {
      const r = await fetch(`/explorer/${api.id}/execute`, {
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
      // Hints
      $("op-hint").innerHTML = "";
      if (data.hints && data.hints.note) {
        const n = document.createElement("div");
        n.className = "muted";
        n.style.padding = "10px";
        n.style.background = "#fff7ed";
        n.style.border = "1px solid #fbd9a8";
        n.style.borderRadius = "6px";
        n.textContent = data.hints.note;
        $("op-hint").appendChild(n);
      }
      if (data.hints && data.hints.open_link) {
        const a = document.createElement("a");
        a.href = data.hints.open_link;
        a.target = "_blank";
        a.rel = "noopener";
        a.textContent = "Open Data Connect ↗";
        const note = document.createElement("div");
        note.className = "muted";
        note.textContent = "Open in a new tab, complete the FinBank flow, then run Refresh Accounts.";
        $("op-hint").appendChild(note);
        $("op-hint").appendChild(a);
      }      // Browser-action button: shown when op.browser_action is true.
      // Prefers hints.browser_launch_url; falls back to first URL found in response body.
      if (op.browser_action) {
        const launchUrl = (data.hints && data.hints.browser_launch_url)
          ? data.hints.browser_launch_url
          : _findFirstUrl(data.response && data.response.body);
        const launchNote = (data.hints && data.hints.browser_launch_note)
          || "Browser interaction required — complete the flow, then proceed to the next step.";
        if (launchUrl) {
          const wrap = document.createElement("div");
          wrap.style.cssText = "margin-top:10px;padding:10px 12px;background:#f0f7ff;border:1px solid #b6d4f7;border-radius:6px;display:flex;align-items:center;gap:12px;";
          const noteEl = document.createElement("span");
          noteEl.className = "muted";
          noteEl.style.fontSize = "13px";
          noteEl.textContent = launchNote;
          const btn = document.createElement("a");
          btn.href = launchUrl;
          btn.target = "_blank";
          btn.rel = "noopener";
          btn.textContent = "Launch 3DS Method ↗";
          btn.style.cssText = "flex-shrink:0;padding:7px 14px;background:#005b99;color:#fff;border-radius:5px;text-decoration:none;font-size:13px;font-weight:600;white-space:nowrap;";
          wrap.appendChild(noteEl);
          wrap.appendChild(btn);
          $("op-hint").appendChild(wrap);
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
        headersVisible: { ...headersVisible },
      };
      // Update state
      if (data.state) {
        currentState = data.state;
        renderStateStrip();
      }
    } catch (e) {
      $("resp-body").textContent = String(e);
    } finally {
      $("op-send").disabled = false;
      $("op-send").textContent = "Send";
    }
  });

  // Recursively find the first https:// URL string in a JSON object/array.
  function _findFirstUrl(obj) {
    if (obj == null) return null;
    if (typeof obj === "string" && /^https?:\/\//i.test(obj)) return obj;
    if (Array.isArray(obj)) {
      for (const v of obj) { const r = _findFirstUrl(v); if (r) return r; }
    } else if (typeof obj === "object") {
      for (const v of Object.values(obj)) { const r = _findFirstUrl(v); if (r) return r; }
    }
    return null;
  }

  // Recursively find the first value for `key` in a JSON object/array.
  function _findKey(obj, key) {
    if (obj == null) return null;
    if (Array.isArray(obj)) {
      for (const v of obj) { const r = _findKey(v, key); if (r) return r; }
    } else if (typeof obj === "object") {
      if (obj[key] != null && typeof obj[key] === "string" && obj[key]) return obj[key];
      for (const v of Object.values(obj)) { const r = _findKey(v, key); if (r) return r; }
    }
    return null;
  }

  function fmt(obj) {
    if (obj == null) return "—";
    try { return JSON.stringify(obj, null, 2); }
    catch { return String(obj); }
  }

  // -----------------------------------------------------------------------
  // Headers toggle
  // -----------------------------------------------------------------------
  // Track whether headers are shown for each panel
  const headersVisible = { request: false, response: false };
  // Store the last raw request/response objects so we can re-render on toggle
  let lastIoData = { request: null, response: null };

  function fmtWithoutHeaders(obj) {
    if (obj == null) return "—";
    try {
      const copy = { ...obj };
      delete copy.headers;
      return JSON.stringify(copy, null, 2);
    } catch { return String(obj); }
  }

  function renderIoPanel(panel, obj) {
    // panel = 'request' | 'response'
    const elId = panel === 'request' ? 'req-body' : 'resp-body';
    const el = $(elId);
    if (!obj) { el.textContent = "—"; return; }
    el.textContent = headersVisible[panel] ? fmt(obj) : fmtWithoutHeaders(obj);
  }

  function updateHeaderToggleBtn(panel) {
    const btnId = panel === 'request' ? 'req-headers-toggle' : 'resp-headers-toggle';
    const btn = $(btnId);
    if (!btn) return;
    btn.textContent = headersVisible[panel] ? 'Hide Headers' : 'Show Headers';
    btn.classList.toggle('active', headersVisible[panel]);
  }

  document.querySelectorAll('.btn-toggle-headers').forEach(btn => {
    btn.addEventListener('click', () => {
      const panel = btn.dataset.panel;
      headersVisible[panel] = !headersVisible[panel];
      updateHeaderToggleBtn(panel);
      renderIoPanel(panel, lastIoData[panel]);
    });
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
      API_CALL_LOG.length = 0;
      apiCallsClose();
    }
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
    } else if (uc.render === "binlookup") {
      renderBinLookup();
    } else if (uc.render === "clarity") {
      renderClarity();
    } else if (uc.render === "easysavings") {
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
      renderSonicBrand();
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
    const body = $("uc-body");
    if (!body) return;
    body.innerHTML = `<div class="enrich-loading"><div class="enrich-spinner"></div><p>Loading transactions…</p></div>`;
    fetch("/usecases/enrichment/data")
      .then(r => r.json())
      .then(d => {
        ENRICH.data = d.transactions || [];
        ENRICH.enriched.clear();
        if (!ENRICH.data.length) {
          body.innerHTML = `<p class="muted">No transactions to enrich.</p>`;
          return;
        }
        enrichRender();
      })
      .catch((e) => {
        body.innerHTML = `<p class="muted">Could not load transactions: ${escapeHtml(String(e.message || e))}</p>`;
      });
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

  const REC = {
    cid: "9013023139",
    accounts: [],
    selectedAccount: "",
    streams: [],
    transactions: [],
    loading: false,
  };

  const REC_FREQ_LABELS = {
    WEEKLY: "Weekly", BIWEEKLY: "Bi-weekly", MONTHLY: "Monthly",
    BIMONTHLY: "Bi-monthly", QUARTERLY: "Quarterly", ANNUAL: "Annual", UNKNOWN: "Irregular",
  };

  function recFreqClass(freq) {
    return "rec-chip--freq-" + (freq || "unknown").toLowerCase();
  }

  function recLogoHtml(name) {
    const initials = (name || "?").replace(/[^A-Za-z0-9 ]/g, "").trim().split(" ")
      .slice(0, 2).map(w => w[0] || "").join("").toUpperCase() || "?";
    const colors = ["#6366f1","#0ea5e9","#10b981","#f59e0b","#ec4899","#8b5cf6","#ef4444","#14b8a6"];
    const idx = (name || "").split("").reduce((s, c) => s + c.charCodeAt(0), 0) % colors.length;
    return `<svg viewBox="0 0 44 44"><rect width="44" height="44" rx="12" fill="${colors[idx]}"/><text x="22" y="30" text-anchor="middle" font-size="16" font-weight="700" fill="white">${escapeHtml(initials)}</text></svg>`;
  }

  function recDaysBadgeHtml(dateStr) {
    if (!dateStr) return "";
    const parts = dateStr.split("-");
    if (parts.length < 3) return "";
    const next = new Date(parseInt(parts[0]), parseInt(parts[1]) - 1, parseInt(parts[2]));
    const today = new Date(); today.setHours(0, 0, 0, 0);
    const diff = Math.round((next - today) / 86400000);
    if (diff < 0) return `<span class="rec-days-badge rec-days-badge--past">${Math.abs(diff)}d ago</span>`;
    if (diff === 0) return `<span class="rec-days-badge rec-days-badge--soon">Today</span>`;
    if (diff <= 7) return `<span class="rec-days-badge rec-days-badge--soon">In ${diff}d</span>`;
    return `<span class="rec-days-badge rec-days-badge--future">In ${diff}d</span>`;
  }

  function recFmtDate(dateStr) {
    if (!dateStr) return "—";
    const parts = dateStr.split("-");
    if (parts.length < 3) return dateStr;
    const d = new Date(parseInt(parts[0]), parseInt(parts[1]) - 1, parseInt(parts[2]));
    return d.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });
  }

  function recFmtAmt(n) {
    const abs = Math.abs(n);
    return "$" + abs.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }

  function renderRecurring() {
    fetch("/explorer/ofin/state").then(r => r.json()).then(d => {
      REC.cid = (d.state || {}).customer_id || REC.cid;
      recRender();
    }).catch(() => recRender());
  }

  function recRender() {
    const body = $("uc-body");
    if (!body) return;

    const totalMonthly = REC.streams
      .filter(s => s.type !== "CREDIT" && s.frequency === "MONTHLY")
      .reduce((sum, s) => sum + Math.abs(s.amount), 0);
    const totalCredits = REC.streams
      .filter(s => s.type === "CREDIT")
      .reduce((sum, s) => sum + Math.abs(s.amount), 0);
    const totalStreams = REC.streams.length;

    const summaryHtml = totalStreams > 0 ? `
      <div class="rec-summary-strip">
        <div class="rec-summary-card">
          <label>Recurring Streams</label>
          <span>${totalStreams}</span>
        </div>
        <div class="rec-summary-card">
          <label>Monthly Outflows</label>
          <span class="rec-amt-debit">${recFmtAmt(totalMonthly)}</span>
        </div>
        <div class="rec-summary-card">
          <label>Recurring Credits</label>
          <span class="rec-amt-credit">${recFmtAmt(totalCredits)}</span>
        </div>
      </div>
    ` : "";

    const debits  = REC.streams.filter(s => s.type !== "CREDIT");
    const credits = REC.streams.filter(s => s.type === "CREDIT");

    function sectionHtml(streams, kind) {
      if (!streams.length) return "";
      const badgeCls = kind === "credit" ? "rec-section-badge--credit" : "rec-section-badge--debit";
      const title    = kind === "credit" ? "Incoming (Credits)" : "Outgoing (Debits)";
      return `
        <div>
          <div class="rec-section-head">
            <h3>${title}</h3>
            <span class="rec-section-badge ${badgeCls}">${streams.length}</span>
          </div>
          <div class="rec-grid">
            ${streams.map(recCardHtml).join("")}
          </div>
        </div>
      `;
    }

    const resultsHtml = totalStreams > 0 ? `
      ${summaryHtml}
      ${sectionHtml(credits, "credit")}
      ${sectionHtml(debits, "debit")}
      ${recTxnListHtml(REC.transactions, REC.streams)}
    ` : `
      <div class="rec-hero">
        <div class="rec-hero-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="9"/>
            <path d="M12 7v1m0 8v1M7 12h1m8 0h1"/>
          </svg>
        </div>
        <h3>No streams detected yet</h3>
        <p>Enter a Customer ID and click Load Accounts, then choose accounts and click Analyse Recurring to detect patterns.</p>
        <div class="rec-hero-chips">
          <span class="rec-hero-chip">Subscriptions</span>
          <span class="rec-hero-chip">Bills &amp; Utilities</span>
          <span class="rec-hero-chip">Salary &amp; Income</span>
          <span class="rec-hero-chip">Loan Repayments</span>
        </div>
      </div>
    `;

    body.innerHTML = `
      <div class="rec-stage">
        <div class="rec-controlbar">
          <div class="rec-controls-row">
            <div class="rec-field">
              <label>Customer ID</label>
              <input id="rec-cid" type="text" value="${escapeHtml(REC.cid)}" placeholder="e.g. 9013023139" style="width:160px">
            </div>
            <button class="rec-btn rec-btn--secondary" id="rec-load-accts">Load Accounts</button>
            <div class="rec-field rec-field--grow" id="rec-acct-wrap" style="display:none">
              <label>Account (optional filter)</label>
              <select id="rec-acct-select" style="min-width:220px">
                <option value="">— all accounts —</option>
              </select>
            </div>
            <button class="rec-btn rec-btn--primary" id="rec-go" ${REC.loading || !REC.selectedAccount ? "disabled" : ""}>
              ${REC.loading ? `<span class="psi-spinner"></span>` : "Analyse Recurring"}
            </button>
          </div>
          <p class="rec-hint">${!REC.accounts.length ? "Load accounts first, then select an account to analyse." : !REC.selectedAccount ? "Select an account from the dropdown to enable analysis." : "Identifies repeating debit and credit patterns — subscriptions, bills, salary, and more — across connected accounts."}</p>
        </div>

        ${REC.loading ? `
          <div class="rec-loading-state">
            <div class="rec-spinner"></div>
            <span>Detecting recurring patterns…</span>
          </div>
        ` : resultsHtml}
      </div>
    `;

    recWire();

    // Restore account dropdown if we already have accounts
    if (REC.accounts.length) recPopulateAccounts();
  }

  function recCardHtml(s) {
    const isDebit   = s.type !== "CREDIT";
    const amtCls    = isDebit ? "rec-card-amount--debit" : "rec-card-amount--credit";
    const amtSign   = isDebit ? "-" : "+";
    const freqLabel = REC_FREQ_LABELS[s.frequency] || s.frequency;
    const freqCls   = recFreqClass(s.frequency);
    const regLabel  = s.regularity === "REGULAR" ? "Regular" : s.regularity === "IRREGULAR" ? "Irregular" : null;
    const regCls    = s.regularity === "REGULAR" ? "rec-chip--reg" : "rec-chip--irreg";

    return `
      <div class="rec-card">
        <div class="rec-card-top">
          <div class="rec-card-logo">${recLogoHtml(s.merchantName)}</div>
          <div class="rec-card-meta">
            <div class="rec-card-name">${escapeHtml(s.merchantName)}</div>
            ${s.description && s.description !== s.merchantName
              ? `<div class="rec-card-desc">${escapeHtml(s.description)}</div>` : ""}
          </div>
          <div class="rec-card-amount ${amtCls}">${amtSign}${recFmtAmt(s.amount)}</div>
        </div>
        <div class="rec-card-chips">
          <span class="rec-chip ${freqCls}">${escapeHtml(freqLabel)}</span>
          ${s.category ? `<span class="rec-chip rec-chip--cat">${escapeHtml(s.category)}</span>` : ""}
          ${regLabel ? `<span class="rec-chip ${regCls}">${regLabel}</span>` : ""}
        </div>
        <div class="rec-card-footer">
          <div class="rec-next-date">
            <label>Next expected</label>
            <span>${recFmtDate(s.nextExpectedDate)}</span>
          </div>
          ${s.count ? `<div class="rec-next-date"><label>Detected</label><span>${s.count} txn${s.count !== 1 ? "s" : ""}</span></div>` : ""}
          ${recDaysBadgeHtml(s.nextExpectedDate)}
        </div>
      </div>
    `;
  }

  function recPopulateAccounts() {
    const sel = document.getElementById("rec-acct-select");
    const wrap = document.getElementById("rec-acct-wrap");
    if (!sel || !wrap) return;
    sel.innerHTML = `<option value="">— select an account —</option>`;
    REC.accounts.forEach(a => {
      const opt = document.createElement("option");
      opt.value = a.id;
      const num = a.number ? `••${String(a.number).slice(-4)}` : a.id;
      opt.textContent = `${num} · ${a.type} — ${a.name}`;
      sel.appendChild(opt);
    });
    // Restore previously selected account after re-render
    if (REC.selectedAccount) sel.value = REC.selectedAccount;
    wrap.style.display = "";
  }

  function recWire() {
    const cidInput = document.getElementById("rec-cid");
    const loadBtn  = document.getElementById("rec-load-accts");
    const goBtn    = document.getElementById("rec-go");

    if (cidInput) cidInput.addEventListener("input", () => { REC.cid = cidInput.value.trim(); });

    if (loadBtn) loadBtn.addEventListener("click", async () => {
      const cid = (document.getElementById("rec-cid") || {}).value || REC.cid;
      REC.cid = cid.trim();
      if (!REC.cid) return;
      loadBtn.disabled = true; loadBtn.textContent = "Loading…";
      try {
        const r = await fetch("/usecases/recurring/action", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ action: "get_accounts", params: { customer_id: REC.cid } }),
        });
        const d = await r.json();
        if (d.error) { alert("Error: " + d.error); return; }
        REC.accounts = d.accounts || [];
        REC.selectedAccount = "";
        recRender();  // re-renders with account dropdown visible
      } catch (e) {
        alert("Failed to load accounts: " + e);
      } finally {
        loadBtn.disabled = false; loadBtn.textContent = "Load Accounts";
      }
    });

    const acctSelEl = document.getElementById("rec-acct-select");
    if (acctSelEl) acctSelEl.addEventListener("change", () => {
      REC.selectedAccount = acctSelEl.value;
      recRender();
    });

    if (goBtn) goBtn.addEventListener("click", async () => {
      const cid = (document.getElementById("rec-cid") || {}).value || REC.cid;
      REC.cid = cid.trim();
      if (!REC.cid) { alert("Please enter a Customer ID"); return; }
      if (!REC.selectedAccount) { alert("Select an account before analysing."); return; }
      const acctId = REC.selectedAccount;
      REC.loading = true;
      REC.transactions = [];
      recRender();
      try {
        const post = (action, params) => fetch("/usecases/recurring/action", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ action, params }),
        }).then(r => r.json());

        const [recD, txnD] = await Promise.all([
          post("get_recurring",    { customer_id: REC.cid, account_ids: acctId }),
          post("get_transactions", { customer_id: REC.cid, account_id: acctId }),
        ]);

        REC.loading = false;
        if (recD.error) { REC.streams = []; recRenderError(recD.error, recD.detail); return; }
        REC.streams      = recD.streams || [];
        REC.transactions = txnD.transactions || [];
        recRender();
      } catch (e) {
        REC.loading = false;
        recRenderError(String(e));
      }
    });
  }

  function recTxnListHtml(transactions, streams) {
    if (!transactions.length) return "";

    // Build a lowercase set of recurring merchant names for quick lookup
    const recurringNames = new Set(
      streams.map(s => (s.merchantName || "").toLowerCase().trim()).filter(Boolean)
    );
    const isRecurring = t => {
      const payee = (t.normalizedPayee || "").toLowerCase().trim();
      if (payee && recurringNames.has(payee)) return true;
      const desc = (t.description || "").toLowerCase();
      for (const n of recurringNames) { if (n && desc.includes(n)) return true; }
      return false;
    };
    const getStream = t => {
      const payee = (t.normalizedPayee || "").toLowerCase().trim();
      const desc  = (t.description || "").toLowerCase();
      return streams.find(s => {
        const n = (s.merchantName || "").toLowerCase().trim();
        return n && (payee === n || desc.includes(n));
      });
    };

    let recurCount = 0;
    const rows = transactions.map(t => {
      const rec = isRecurring(t);
      if (rec) recurCount++;
      const stream  = rec ? getStream(t) : null;
      const isCredit = t.amount > 0;
      const rowCls  = rec ? (isCredit ? "rec-txn--credit-stream" : "rec-txn--debit-stream") : "";
      const date    = t.date ? new Date(t.date * 1000).toLocaleDateString("en-US", { month: "short", day: "numeric" }) : "—";
      const amtStr  = (isCredit ? "+" : "") + recFmtAmt(t.amount);
      const amtCls  = isCredit ? "rec-txn-amt--credit" : "rec-txn-amt--debit";
      const freqLabel = stream ? (REC_FREQ_LABELS[stream.frequency] || stream.frequency) : "";
      const freqBadge = freqLabel ? `<span class="rec-txn-freq">${escapeHtml(freqLabel)}</span>` : "";
      const displayName = t.normalizedPayee || t.description;
      return `
        <div class="rec-txn-row ${rowCls}">
          <div class="rec-txn-date">${date}</div>
          <div class="rec-txn-info">
            <div class="rec-txn-name">${escapeHtml(displayName)}</div>
            ${t.category ? `<div class="rec-txn-cat">${escapeHtml(t.category)}</div>` : ""}
          </div>
          ${freqBadge}
          <div class="rec-txn-amt ${amtCls}">${amtStr}</div>
        </div>`;
    }).join("");

    return `
      <div class="rec-section-head" style="margin-top:24px">
        <h3>Transactions <span style="font-weight:400;color:#9a9a9a;font-size:14px">· last 90 days</span></h3>
        <span class="rec-section-badge">${transactions.length}</span>
      </div>
      <div class="rec-txn-legend">
        <span class="rec-txn-legend--recurring">&#8635; ${recurCount} recurring</span>
        <span>${transactions.length - recurCount} one-off</span>
      </div>
      <div class="rec-txn-list">${rows}</div>`;
  }

  function recRenderError(msg, detail) {
    const body = $("uc-body");
    if (!body) return;
    body.innerHTML = `
      <div class="rec-stage">
        <div class="rec-error">
          <strong>Could not retrieve recurring transactions</strong><br>
          ${escapeHtml(msg)}
          ${detail ? `<pre style="margin:8px 0 0;font-size:11px;overflow:auto">${escapeHtml(JSON.stringify(detail, null, 2))}</pre>` : ""}
        </div>
        <button class="rec-btn rec-btn--secondary" id="rec-err-back" style="align-self:flex-start;margin-top:4px">← Back</button>
      </div>`;
    const backBtn = body.querySelector("#rec-err-back");
    if (backBtn) backBtn.addEventListener("click", () => { REC.loading = false; recRender(); });
  }

  // ===================== Payment Success Indicator Use Case =====================

  const PSI = {
    cid: "9013023139",
    accounts: [],
    selectedAccountId: null,
    amount: 500,
    result: null,
    loading: false,
    selectedDay: 0,    // index into dailyResults for factor breakdown
  };

  const PSI_RISK_COLORS = { low: "#10b981", medium: "#f59e0b", high: "#ef4444" };
  const PSI_RISK_BG    = { low: "#d1fae5", medium: "#fef3c7", high: "#fee2e2" };
  const PSI_RISK_TEXT  = { low: "#065f46", medium: "#92400e", high: "#991b1b" };
  const PSI_FACTOR_LABELS = {
    recentBalance:     "Recent Balance",
    balanceHistory:    "Balance History",
    nsfHistory:        "NSF History",
    recentNsfHistory:  "Recent NSF Activity",
    recurringNsf:      "Recurring NSF",
    spendHistory:      "Spend Trend",
    depositHistory:    "Deposit Trend",
    transactionAmount: "Transaction Size",
  };

  function renderPsi() {
    fetch("/explorer/ofin/state").then(r => r.json()).then(d => {
      PSI.cid = (d.state || {}).customer_id || PSI.cid;
      psiRender();
    }).catch(() => psiRender());
  }

  function psiShortDate(iso) {
    if (!iso) return "";
    const [, m, day] = iso.split("-");
    const months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
    return months[parseInt(m,10)-1] + " " + parseInt(day,10);
  }

  function psiRender() {
    const body = $("uc-body");
    if (!body) return;
    body.innerHTML = `
      <div class="psi-stage">
        <div class="psi-controlbar">
          <div class="psi-controls-row">
            <div class="psi-field psi-field--grow">
              <label>Customer ID</label>
              <input id="psi-cid" value="${escapeHtml(PSI.cid)}" placeholder="Enter customer ID" />
            </div>
            <button class="btn" id="psi-load-btn">Load Accounts</button>
          </div>
          ${PSI.accounts.length ? `
          <div class="psi-controls-row">
            <div class="psi-field psi-field--grow">
              <label>Account</label>
              <select id="psi-account-sel">
                ${PSI.accounts.map(a => {
                  const bal = a.balance != null
                    ? ` · $${Number(a.balance).toLocaleString("en-US",{minimumFractionDigits:2,maximumFractionDigits:2})}`
                    : "";
                  return `<option value="${escapeHtml(a.id)}" ${PSI.selectedAccountId === a.id ? "selected" : ""}>${escapeHtml(a.name)} · ${escapeHtml(a.number)} · ${escapeHtml(a.type)}${bal}</option>`;
                }).join("")}
              </select>
            </div>
            <div class="psi-field">
              <label>Amount (USD)</label>
              <div class="psi-amount-wrap">
                <span class="psi-amount-dollar">$</span>
                <input id="psi-amount" type="number" min="1" step="0.01" value="${PSI.amount}" />
              </div>
            </div>
            <button class="btn btn-primary" id="psi-run-btn" ${PSI.loading ? "disabled" : ""}>
              ${PSI.loading
                ? `<span class="psi-spinner"></span>Assessing…`
                : `<svg viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.8" style="width:14px;height:14px;flex-shrink:0"><path d="M9 1v16M1 9h16"/></svg>Run Assessment`}
            </button>
          </div>
          ` : `<p class="psi-hint">Enter a Customer ID and load their accounts to begin.</p>`}
        </div>

        <div class="psi-disclaimer">
          <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" style="width:13px;height:13px;flex-shrink:0"><path d="M8 1.5L1 14h14L8 1.5z"/><path d="M8 6v4M8 11.5v.5"/></svg>
          NOTE: THIS IS NOT RUNNING THE PRODUCTION PSI MODEL — TREAT RESULTS AS ILLUSTRATIVE
        </div>

        <div id="psi-result-area">
          ${PSI.loading ? `<div class="psi-loading-state"><div class="psi-spinner psi-spinner--lg"></div><p>Calling Payment Success Indicator API…</p></div>` : ""}
          ${!PSI.loading && PSI.result ? psiResultHtml(PSI.result) : ""}
          ${!PSI.loading && !PSI.result && !PSI.accounts.length ? psiHeroHtml() : ""}
        </div>
      </div>
    `;
    psiWire();
  }

  function psiHeroHtml() {
    return `
      <div class="psi-hero">
        <div class="psi-hero-icon">
          <svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5">
            <circle cx="24" cy="24" r="20"/>
            <path d="M24 14v10l6 4"/>
          </svg>
        </div>
        <h3>Real-time Payment Risk Assessment</h3>
        <p>PSI evaluates the likelihood of an ACH payment succeeding — before you send it. Load a customer's accounts above to get started.</p>
        <div class="psi-hero-chips">
          <span class="psi-hero-chip">Real-time balance check</span>
          <span class="psi-hero-chip">10-day NSF risk forecast</span>
          <span class="psi-hero-chip">Fraud signal detection</span>
        </div>
      </div>`;
  }

  function psiGaugeSvg(score, level) {
    const colors = { low: "#10b981", medium: "#f59e0b", high: "#ef4444" };
    const fgColor = colors[level] || colors.medium;
    const r = 54;
    const total = Math.PI * r; // semicircle arc length ≈ 169.6
    const filled = (score / 100) * total;
    return `
      <div class="psi-gauge">
        <svg viewBox="0 0 144 80" class="psi-gauge-svg">
          <path d="M18 72 A54 54 0 0 1 126 72"
            fill="none" stroke="#f0f1f5" stroke-width="11" stroke-linecap="round"/>
          <path d="M18 72 A54 54 0 0 1 126 72"
            fill="none" stroke="${fgColor}" stroke-width="11" stroke-linecap="round"
            stroke-dasharray="${filled.toFixed(1)} ${(total + 4).toFixed(1)}"/>
          <text x="72" y="62" text-anchor="middle"
            font-size="30" font-weight="900" fill="${fgColor}" font-family="inherit">${score}</text>
          <text x="72" y="74" text-anchor="middle"
            font-size="9" fill="#bbb" font-family="inherit">out of 100</text>
        </svg>
        <div class="psi-gauge-label psi-gauge-label--${level}">${
          level === "low" ? "Low risk" : level === "medium" ? "Moderate risk" : "High risk"
        }</div>
      </div>`;
  }

  function psiResultHtml(r) {
    if (r.error) {
      return `<div class="psi-error-card"><span class="psi-error-icon">⚠</span><div><strong>Assessment failed</strong><p>${escapeHtml(r.error)}</p></div></div>`;
    }

    const daily = r.dailyResults || [];
    const hasNsf = daily.length > 0;
    const selDay = daily[PSI.selectedDay] || daily[0] || {};
    const unauth = r.unauthorizedReturnRisk;

    // Best settlement day (lowest nsfScore)
    let bestIdx = 0;
    daily.forEach((d, i) => { if (d.nsfScore < daily[bestIdx].nsfScore) bestIdx = i; });

    // Verdict: based on today's (first day's) risk level
    const verdictLevel = (daily[0] || {}).riskLevel || (unauth || {}).riskLevel || "low";
    const VERDICT = {
      low:    { icon: "✓", title: "Low Risk · Ready to Send",
                sub: "Confidence is high that this payment will clear successfully." },
      medium: { icon: "⚠", title: "Moderate Risk · Proceed with Caution",
                sub: "Consider settling on the recommended date to reduce NSF return risk." },
      high:   { icon: "✗", title: "High Return Risk · Consider Delaying",
                sub: "This account shows elevated NSF risk today. Settling on the recommended date significantly lowers that risk." },
    };
    const verdict = VERDICT[verdictLevel] || VERDICT.medium;

    const amtFmt = n => "$" + Number(n).toLocaleString("en-US", {minimumFractionDigits:2, maximumFractionDigits:2});
    const balance = r.availableBalance;
    const amount  = r.amount || 0;
    const covered = balance != null ? balance >= amount : null;

    return `
      <div class="psi-result">

        <!-- Verdict banner -->
        <div class="psi-verdict psi-verdict--${verdictLevel}">
          <div class="psi-verdict-icon">${verdict.icon}</div>
          <div class="psi-verdict-body">
            <div class="psi-verdict-title">${verdict.title}</div>
            <div class="psi-verdict-sub">${verdict.sub}</div>
          </div>
          ${hasNsf ? `
          <div class="psi-verdict-recommend">
            <span class="psi-verdict-rec-label">Recommended settlement</span>
            <span class="psi-verdict-rec-date">${escapeHtml(psiShortDate(daily[bestIdx].date))}</span>
          </div>` : ""}
        </div>

        <!-- Main grid: gauge + details -->
        <div class="psi-main-grid">

          ${hasNsf ? `
          <div class="psi-gauge-card">
            <div class="psi-card-label">NSF Return Risk</div>
            ${psiGaugeSvg(Math.round(selDay.nsfScore ?? 0), selDay.riskLevel || verdictLevel)}
            <div class="psi-gauge-meta">
              <span class="psi-indicator-badge psi-ibadge--${selDay.riskLevel}">${escapeHtml(selDay.indicator || "")}</span>
              <span class="psi-card-sub">Settlement confidence: <strong>${Math.round(selDay.confidence ?? 0)}%</strong></span>
            </div>
            <p class="psi-card-desc">NSF return probability (0–100). Lower is better. Click a day in the timeline to compare dates.</p>
          </div>` : ""}

          <div class="psi-details-card">
            <div class="psi-detail-row">
              <span class="psi-detail-label">Transaction amount</span>
              <span class="psi-detail-value">${amtFmt(amount)}</span>
            </div>
            ${balance != null ? `
            <div class="psi-detail-row">
              <span class="psi-detail-label">Available balance</span>
              <span class="psi-detail-value psi-detail-value--balance">${amtFmt(balance)}</span>
            </div>
            <div class="psi-detail-row">
              <span class="psi-detail-label">Coverage</span>
              <span class="psi-detail-value ${covered ? "psi-detail-ok" : "psi-detail-warn"}">${covered ? "✓ Covered" : "✗ Insufficient"}</span>
            </div>` : ""}
            ${r.settleByDate ? `
            <div class="psi-detail-row">
              <span class="psi-detail-label">Settle by</span>
              <span class="psi-detail-value">${escapeHtml(psiShortDate(r.settleByDate))}</span>
            </div>` : ""}
            ${r.requestDate ? `
            <div class="psi-detail-row">
              <span class="psi-detail-label">Assessment date</span>
              <span class="psi-detail-value">${escapeHtml(r.requestDate)}</span>
            </div>` : ""}

            ${unauth ? `
            <div class="psi-detail-divider"></div>
            <div class="psi-card-label" style="padding:12px 0 8px">Unauthorized Return Risk</div>
            <div class="psi-unauth-row">
              <div class="psi-unauth-score psi-score--${unauth.riskLevel}">${Math.round(unauth.score ?? 0)}</div>
              <div>
                <span class="psi-indicator-badge psi-ibadge--${unauth.riskLevel}">${escapeHtml(unauth.indicator || "")}</span>
                <div class="psi-card-sub" style="margin-top:5px">First/third-party fraud signal.<br>Score 0–100 — lower is better.</div>
              </div>
            </div>` : ""}
          </div>
        </div>

        ${hasNsf ? `
        <!-- Timeline: NSF risk by day (shorter = safer) -->
        <div class="psi-timeline">
          <div class="psi-timeline-head">
            <div>
              <div class="psi-section-title">10-Day Settlement Window</div>
              <div class="psi-section-sub">NSF risk by settlement date — shorter bars are safer. Click any day to inspect risk factors.</div>
            </div>
          </div>
          <div class="psi-timeline-bars" id="psi-bars">
            ${daily.map((d, i) => {
              const isBest = i === bestIdx;
              const isSel  = i === PSI.selectedDay;
              const barH   = Math.max(4, Math.round(d.nsfScore * 1.6));
              return `<div class="psi-day ${isBest ? "psi-day--best" : ""} ${isSel ? "psi-day--selected" : ""}" data-day-idx="${i}">
                ${isBest ? `<div class="psi-day-best-label">Best</div>` : ""}
                <div class="psi-day-conf">${Math.round(d.nsfScore)}</div>
                <div class="psi-day-bar-wrap">
                  <div class="psi-day-bar psi-bar--${d.riskLevel}" style="height:${barH}px"></div>
                </div>
                <div class="psi-day-date">${escapeHtml(psiShortDate(d.date))}</div>
                <div class="psi-day-badge psi-badge--${d.riskLevel}">${d.riskLevel === "low" ? "Low" : d.riskLevel === "medium" ? "Med" : "High"}</div>
              </div>`;
            }).join("")}
          </div>
          <div class="psi-timeline-legend">
            <span class="psi-legend-item psi-legend--low">Low risk</span>
            <span class="psi-legend-item psi-legend--medium">Moderate</span>
            <span class="psi-legend-item psi-legend--high">High risk</span>
            <span class="psi-legend-best">★ Best settlement day</span>
          </div>
        </div>
        ` : r.nsfError ? `<div class="psi-error-card"><span class="psi-error-icon">⚠</span><div><strong>NSF score unavailable</strong><p>${escapeHtml((r.nsfError.message || r.nsfError.title || JSON.stringify(r.nsfError)))}</p></div></div>` : ""}

        ${selDay.reasons && Object.values(selDay.reasons).some(v => v > 0) ? `
        <!-- Risk factor breakdown -->
        <div class="psi-factors">
          <div class="psi-section-title">Risk Factor Breakdown <span class="psi-factors-date">— ${escapeHtml(psiShortDate(selDay.date))}</span></div>
          <div class="psi-section-sub" style="margin-bottom:16px">Component scores driving the NSF risk assessment. Higher = more risk.</div>
          <div class="psi-factors-grid">
            ${Object.entries(selDay.reasons).map(([key, val]) => `
              <div class="psi-factor">
                <div class="psi-factor-header">
                  <div class="psi-factor-label">${escapeHtml(PSI_FACTOR_LABELS[key] || key)}</div>
                  <span class="psi-factor-score" style="color:${psiFactorColor(val)}">${val}</span>
                </div>
                <div class="psi-factor-track">
                  <div class="psi-factor-fill" style="width:${val}%; background:${psiFactorColor(val)}"></div>
                </div>
              </div>
            `).join("")}
          </div>
        </div>` : ""}

      </div>
    `;
  }

  function psiFactorColor(v) {
    if (v >= 66) return "#ef4444";
    if (v >= 33) return "#f59e0b";
    return "#10b981";
  }

  function psiWire() {
    const loadBtn = $("psi-load-btn");
    const runBtn  = $("psi-run-btn");

    if (loadBtn) {
      loadBtn.addEventListener("click", () => {
        PSI.cid = ($("psi-cid") || {}).value?.trim() || PSI.cid;
        psiLoadAccounts();
      });
    }
    const cidInput = $("psi-cid");
    if (cidInput) {
      cidInput.addEventListener("keydown", e => {
        if (e.key === "Enter") { PSI.cid = cidInput.value.trim(); psiLoadAccounts(); }
      });
    }

    const sel = $("psi-account-sel");
    if (sel) {
      sel.addEventListener("change", () => { PSI.selectedAccountId = sel.value; });
      if (!PSI.selectedAccountId) PSI.selectedAccountId = sel.value;
    }

    if (runBtn) {
      runBtn.addEventListener("click", () => {
        const amtInput = $("psi-amount");
        PSI.amount = parseFloat(amtInput?.value || "500") || 500;
        PSI.selectedAccountId = $("psi-account-sel")?.value || PSI.selectedAccountId;
        psiRunAssessment();
      });
    }

    // Day click → update selected day for factor breakdown
    const barsEl = $("psi-bars");
    if (barsEl) {
      barsEl.querySelectorAll("[data-day-idx]").forEach(el => {
        el.addEventListener("click", () => {
          PSI.selectedDay = parseInt(el.dataset.dayIdx, 10);
          psiRender();
        });
      });
    }
  }

  function psiLoadAccounts() {
    const area = $("psi-result-area");
    if (area) area.innerHTML = `<div class="psi-loading-state"><div class="psi-spinner psi-spinner--lg"></div><p>Loading accounts…</p></div>`;
    fetch("/usecases/psi/action", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "get_accounts", params: { customer_id: PSI.cid } }),
    }).then(r => r.json()).then(d => {
      if (d.error) {
        const area2 = $("psi-result-area");
        if (area2) area2.innerHTML = `<div class="psi-error-card"><span class="psi-error-icon">⚠</span><div><strong>Could not load accounts</strong><p>${escapeHtml(d.error)}</p></div></div>`;
        return;
      }
      PSI.accounts = d.accounts || [];
      PSI.selectedAccountId = PSI.accounts[0]?.id || null;
      PSI.result = null;
      PSI.selectedDay = 0;
      psiRender();
    }).catch(() => {
      const area2 = $("psi-result-area");
      if (area2) area2.innerHTML = `<div class="psi-error-card"><span class="psi-error-icon">⚠</span><div><strong>Request failed</strong><p>Could not reach the server.</p></div></div>`;
    });
  }

  function psiRunAssessment() {
    PSI.loading = true;
    PSI.result = null;
    psiRender();
    fetch("/usecases/psi/action", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        action: "score",
        params: { customer_id: PSI.cid, account_id: PSI.selectedAccountId, amount: PSI.amount },
      }),
    }).then(r => r.json()).then(d => {
      PSI.loading = false;
      PSI.selectedDay = 0;
      PSI.result = d.result || (d.error ? { error: d.error } : { error: "No result returned" });
      psiRender();
    }).catch(() => {
      PSI.loading = false;
      PSI.result = { error: "Request failed — check network and try again." };
      psiRender();
    });
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
    const body = $("uc-body");
    if (!body) return;
    body.innerHTML = `
      <div class="bin-stage">
        <nav class="bin-tabs" role="tablist">
          <button class="bin-tab${BIN_TAB === "lookup" ? " bin-tab--active" : ""}" id="bin-tab-lookup" role="tab">
            <svg width="13" height="13" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="5" width="16" height="12" rx="2"/><path d="M6 9h8M6 13h4" stroke-linecap="round"/></svg>
            Single Lookup
          </button>
          <button class="bin-tab${BIN_TAB === "batch" ? " bin-tab--active" : ""}" id="bin-tab-batch" role="tab">
            <svg width="13" height="13" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="10" cy="5" rx="7" ry="3"/><path d="M3 5v4c0 1.657 3.134 3 7 3s7-1.343 7-3V5"/><path d="M3 9v4c0 1.657 3.134 3 7 3s7-1.343 7-3V9"/></svg>
            Batch Search
            ${BIN_DB.status === "loaded" ? `<span class="bin-tab-badge">${BIN_DB.count.toLocaleString()}</span>` : ""}
          </button>
        </nav>
        <div class="bin-tab-content">
          ${BIN_TAB === "lookup" ? _binLookupPanelHtml() : binDbPanelHtml()}
        </div>
      </div>`;
    // Tab switching
    document.getElementById("bin-tab-lookup")?.addEventListener("click", () => {
      if (BIN_TAB === "lookup") return;
      BIN_TAB = "lookup";
      renderBinLookup();
    });
    document.getElementById("bin-tab-batch")?.addEventListener("click", () => {
      if (BIN_TAB === "batch") return;
      BIN_TAB = "batch";
      renderBinLookup();
      _binDbSyncStatus();
    });
    if (BIN_TAB === "lookup") {
      binWire();
    } else {
      binDbWire();
    }
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

      <details class="bin-raw-details">
        <summary>Full API response</summary>
        <pre class="bin-raw-pre">${escapeHtml(JSON.stringify(card.raw, null, 2))}</pre>
      </details>`;
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
            <a class="bin-db-csv-btn" href="/usecases/binlookup/download-bins" download="bin_ranges.csv"
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
          : `<svg width="13" height="13" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 10a6 6 0 1 1 12 0" stroke-linecap="round"/><path d="M4 10l-2-2 2-2"/></svg> Load into VIMA`;
    }
  }

  function _binDbRefreshResults() {
    const el = document.getElementById("bin-db-results");
    if (el) el.innerHTML = binDbResultsHtml();
    // re-wire row expand
    const tbody = el && el.querySelector(".bin-db-table tbody");
    if (tbody) {
      tbody.addEventListener("click", e => {
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
    return USE_CASES.find(u => u.id === "clarity");
  }
  function _clarityPresets() {
    const m = _clarityManifest();
    return (m && m.presets) || [];
  }
  function _clarityPreset(key) {
    return _clarityPresets().find(p => p.value === key);
  }

  function renderClarity() {
    if (!CLARITY.presetKey) {
      const presets = _clarityPresets();
      CLARITY.presetKey = presets.length ? presets[0].value : null;
    }
    clarityRender();
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

  // ---------------- Personal Finance Manager ----------------
  // Refined palette — Stripe-inspired (muted, modern)
  const PFM_CATEGORY_COLORS = {
    "Food and Drink": "#f97316", "Restaurants": "#f97316", "Groceries": "#f59e0b",
    "Shopping": "#ec4899", "Travel": "#3b82f6", "Transportation": "#0ea5e9",
    "Bills & Utilities": "#8b5cf6", "Service": "#8b5cf6", "Health & Fitness": "#10b981",
    "Entertainment": "#f43f5e", "Income": "#0f7050", "Transfer": "#64748b",
    "Cash & ATM": "#475569", "Education": "#06b6d4", "Personal Care": "#d946ef",
    "Home": "#14b8a6", "Other": "#94a3b8", "Deposit": "#0f7050",
  };
  function pfmColor(cat) { return PFM_CATEGORY_COLORS[cat] || "#94a3b8"; }

  // Inline SVG icons (lucide-style)
  const ICON = {
    user:   `<svg class="pfm-i" viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/></svg>`,
    bell:   `<svg class="pfm-i" viewBox="0 0 24 24"><path d="M6 9a6 6 0 1 1 12 0c0 7 3 8 3 8H3s3-1 3-8z"/><path d="M10 21a2 2 0 0 0 4 0"/></svg>`,
    lock:   `<svg class="pfm-i" viewBox="0 0 24 24"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 1 1 8 0v4"/></svg>`,
    bank:   `<svg class="pfm-i" viewBox="0 0 24 24"><path d="M3 10 12 4l9 6"/><path d="M5 10v9M9 10v9M15 10v9M19 10v9"/><path d="M3 21h18"/></svg>`,
    download:`<svg class="pfm-i" viewBox="0 0 24 24"><path d="M12 4v12"/><path d="m7 11 5 5 5-5"/><path d="M5 20h14"/></svg>`,
    info:   `<svg class="pfm-i" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 11v5"/><circle cx="12" cy="8" r="0.5" fill="currentColor"/></svg>`,
    home:   `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="m3 11 9-7 9 7"/><path d="M5 10v10h14V10"/></svg>`,
    cards:  `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18"/></svg>`,
    chart:  `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>`,
    gear:   `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg>`,
    arrowUp:  `<svg class="pfm-i" viewBox="0 0 24 24"><path d="M12 19V5"/><path d="m5 12 7-7 7 7"/></svg>`,
    arrowDown:`<svg class="pfm-i" viewBox="0 0 24 24"><path d="M12 5v14"/><path d="m5 12 7 7 7-7"/></svg>`,
    plus:   `<svg class="pfm-i" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg>`,
    more:   `<svg class="pfm-i" viewBox="0 0 24 24"><circle cx="6" cy="12" r="1" fill="currentColor"/><circle cx="12" cy="12" r="1" fill="currentColor"/><circle cx="18" cy="12" r="1" fill="currentColor"/></svg>`,
    search: `<svg class="pfm-i" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>`,
    chev:   `<svg class="pfm-i pfm-i-sm" viewBox="0 0 24 24"><path d="m9 6 6 6-6 6"/></svg>`,
    chevLeft:`<svg class="pfm-i" viewBox="0 0 24 24"><path d="m15 6-6 6 6 6"/></svg>`,
    link:   `<svg class="pfm-i" viewBox="0 0 24 24"><path d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg>`,
    sparkles:`<svg class="pfm-i" viewBox="0 0 24 24"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.5 5.5l2.8 2.8M15.7 15.7l2.8 2.8M5.5 18.5l2.8-2.8M15.7 8.3l2.8-2.8"/></svg>`,
    // Account-type icons
    acctChecking: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18M7 15h4"/></svg>`,
    acctSavings:  `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M19 7c0-2-3-3-7-3S5 5 5 7v10c0 2 3 3 7 3s7-1 7-3z"/><path d="M5 12c0 2 3 3 7 3s7-1 7-3"/></svg>`,
    acctCard:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18"/><path d="M7 15h3"/></svg>`,
    acctLoan:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/><path d="M5 17H3v-5l2-4h11l4 5v4h-2"/><path d="M9 17h6"/></svg>`,
    acctMortgage: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="m3 11 9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/></svg>`,
    acctInvest:   `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 17l6-6 4 4 8-8"/><path d="M14 7h7v7"/></svg>`,
    acctOther:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>`,
    // Category icons (used in transaction rows & sheet)
    catFood:      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11h18l-1 9H4z"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>`,
    catRest:      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3v18M5 3h4v6a2 2 0 0 1-4 0z"/><path d="M17 3v9a3 3 0 0 1-3 3v6"/></svg>`,
    catGroc:      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 5h2l2 12h12l2-8H6"/><circle cx="9" cy="20" r="1"/><circle cx="17" cy="20" r="1"/></svg>`,
    catShop:      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M6 7h12l-1 13H7z"/><path d="M9 7a3 3 0 0 1 6 0"/></svg>`,
    catTravel:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 16 21 8l-3 12-5-3-5 5z"/></svg>`,
    catTrans:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/><path d="M3 13h18v-3l-2-4H5l-2 4z"/></svg>`,
    catBills:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6M9 16h4"/></svg>`,
    catHealth:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M20 12c0 5-8 9-8 9s-8-4-8-9a5 5 0 0 1 8-4 5 5 0 0 1 8 4z"/></svg>`,
    catEnt:       `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="18" height="14" rx="2"/><path d="M10 11l5 3-5 3z" fill="currentColor"/></svg>`,
    catIncome:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="m5 12 7 7 7-7"/></svg>`,
    catTransfer:  `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7h13M16 3l4 4-4 4"/><path d="M17 17H4M8 13l-4 4 4 4"/></svg>`,
    catCash:      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="18" height="10" rx="2"/><circle cx="12" cy="12" r="2.5"/></svg>`,
    catEdu:       `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="m2 9 10-5 10 5-10 5z"/><path d="M6 11v5c0 1.5 3 3 6 3s6-1.5 6-3v-5"/></svg>`,
    catCare:      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="5"/><path d="M8 14h8l-1 7H9z"/></svg>`,
    catHome:      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="m3 11 9-7 9 7"/><path d="M5 10v10h14V10"/></svg>`,
    catOther:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18"/></svg>`,
  };

  function pfmCatIcon(cat) {
    const map = {
      "Food and Drink": ICON.catFood, "Restaurants": ICON.catRest, "Groceries": ICON.catGroc,
      "Shopping": ICON.catShop, "Travel": ICON.catTravel, "Transportation": ICON.catTrans,
      "Bills & Utilities": ICON.catBills, "Service": ICON.catBills, "Health & Fitness": ICON.catHealth,
      "Entertainment": ICON.catEnt, "Income": ICON.catIncome, "Transfer": ICON.catTransfer,
      "Cash & ATM": ICON.catCash, "Education": ICON.catEdu, "Personal Care": ICON.catCare,
      "Home": ICON.catHome, "Deposit": ICON.catIncome,
    };
    return map[cat] || ICON.catOther;
  }
  function pfmAcctIcon(type) {
    const map = {
      checking: ICON.acctChecking, savings: ICON.acctSavings, creditCard: ICON.acctCard,
      loan: ICON.acctLoan, mortgage: ICON.acctMortgage, investment: ICON.acctInvest,
    };
    return map[type] || ICON.acctOther;
  }

  const ACCT_ICON = {
    checking: true, savings: true, creditCard: true,
    loan: true, mortgage: true, investment: true,
  };

  function fmtMoney(n) {
    const sign = n < 0 ? "-" : "";
    const v = Math.abs(n).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    return `${sign}$${v}`;
  }
  function fmtMoneyShort(n) {
    const abs = Math.abs(n);
    const sign = n < 0 ? "-" : "";
    if (abs >= 1000) return `${sign}$${(abs / 1000).toFixed(1)}k`;
    return `${sign}$${abs.toFixed(0)}`;
  }
  function fmtDate(ts) {
    if (!ts) return "";
    const d = new Date(ts * 1000);
    return d.toLocaleDateString("en-US", { month: "short", day: "numeric" });
  }

  const PFM_DEFAULT_CID = "9013023139";

  function renderPfm() {
    fetch("/explorer/ofin/state").then((r) => r.json()).then((d) => {
      const cid = (d.state || {}).customer_id || PFM_DEFAULT_CID;
      pfmRender(cid);
    }).catch(() => pfmRender(PFM_DEFAULT_CID));
  }

  // PFM state
  const PFM = {
    cid: "",
    data: null,
    tab: "home",        // home | accounts | insights | settings
    txnQuery: "",
    selectedAcct: null, // when set, accounts tab shows detail
    clockTimer: null,
  };

  function pfmRender(initialCustomerId) {
    const body = $("uc-body");
    const descEl = $("uc-desc");
    const descText = descEl ? descEl.textContent : "";
    if (descEl) descEl.textContent = "";
    body.innerHTML = `
      <div class="pfm-stage">
        <div class="pfm-info">
          <p class="pfm-info-desc">${escapeHtml(descText)}</p>
          <div class="pfm-controlbar">
            <span class="label">Customer ID</span>
            <input id="pfm-cid" placeholder="e.g. 9013023139" value="${initialCustomerId || ""}" />
            <button class="btn btn-primary" id="pfm-load">Load</button>
            <button class="btn" id="pfm-connect-btn">Connect new bank</button>
            <a
              href="https://developer.mastercard.com/open-finance-us/documentation/integration-and-testing/test-the-apis/#test-personas"
              target="_blank"
              rel="noopener"
              style="font-size:12px;color:#6b7280;text-decoration:none;white-space:nowrap"
              title="Mastercard Developers Test Personas"
            >
              Test Personas ↗
            </a>
          </div>
        </div>

        <div class="pfm-phone-wrap">
        <div class="iphone">
          <div class="iphone-screen">
            <div class="iphone-notch" id="pfm-island">
              <div class="pill-content">
                <span class="pill-dot"></span>
                <span id="pfm-island-text">Open Finance · Live</span>
              </div>
            </div>
            <div class="iphone-status">
              <span id="pfm-clock">9:41</span>
              <span class="right">
                <svg viewBox="0 0 18 12" width="17" height="12" fill="currentColor"><rect x="0" y="8" width="3" height="4" rx="0.5"/><rect x="5" y="5" width="3" height="7" rx="0.5"/><rect x="10" y="2" width="3" height="10" rx="0.5"/><rect x="15" y="0" width="3" height="12" rx="0.5"/></svg>
                <svg viewBox="0 0 18 12" width="17" height="12" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M1 5a11 11 0 0 1 16 0"/><path d="M4 8a7 7 0 0 1 10 0"/><circle cx="9" cy="10.5" r="1" fill="currentColor" stroke="none"/></svg>
                <span class="battery"><span></span></span>
              </span>
            </div>
            <div class="pfm-app" id="pfm-app"></div>
            <div class="pfm-tabbar" id="pfm-tabbar">
              <button data-tab="home">${ICON.home}<span>Home</span></button>
              <button data-tab="accounts">${ICON.cards}<span>Accounts</span></button>
              <button data-tab="insights">${ICON.chart}<span>Insights</span></button>
              <button data-tab="settings">${ICON.gear}<span>Settings</span></button>
            </div>
            <div class="pfm-sheet-backdrop" id="pfm-sheet-backdrop"></div>
            <div class="pfm-sheet" id="pfm-sheet"></div>
            <div class="iphone-home-indicator"></div>
          </div>
        </div>
        </div>
      </div>
    `;
    $("pfm-load").addEventListener("click", () => pfmLoad($("pfm-cid").value.trim()));
    $("pfm-cid").addEventListener("keydown", (e) => {
      if (e.key === "Enter") pfmLoad($("pfm-cid").value.trim());
    });
    $("pfm-connect-btn").addEventListener("click", () => pfmStartConnect());

    // Wire tab bar
    $("pfm-tabbar").querySelectorAll("button").forEach((btn) => {
      btn.addEventListener("click", () => {
        PFM.tab = btn.dataset.tab;
        PFM.selectedAcct = null;
        pfmDrawTabs();
        pfmDrawScreen();
      });
    });
    // Sheet dismiss
    $("pfm-sheet-backdrop").addEventListener("click", pfmCloseSheet);

    // Live clock
    pfmStartClock();

    pfmDrawTabs();
    if (initialCustomerId) pfmLoad(initialCustomerId);
    else pfmShowConnect("Enter a Customer ID above and tap Load.");
  }

  function pfmStartClock() {
    if (PFM.clockTimer) clearInterval(PFM.clockTimer);
    const tick = () => {
      const el = document.getElementById("pfm-clock");
      if (!el) { clearInterval(PFM.clockTimer); return; }
      const d = new Date();
      let h = d.getHours(), m = d.getMinutes();
      el.textContent = `${h}:${String(m).padStart(2, "0")}`;
    };
    tick();
    PFM.clockTimer = setInterval(tick, 15000);
  }

  function pfmDrawTabs() {
    const bar = document.getElementById("pfm-tabbar");
    if (!bar) return;
    bar.querySelectorAll("button").forEach((b) => {
      b.classList.toggle("active", b.dataset.tab === PFM.tab);
    });
  }

  function pfmIslandFlash(text) {
    const el = document.getElementById("pfm-island");
    const tx = document.getElementById("pfm-island-text");
    if (!el || !tx) return;
    tx.textContent = text;
    el.classList.add("expanded");
    clearTimeout(el._t);
    el._t = setTimeout(() => el.classList.remove("expanded"), 2200);
  }

  function pfmShowConnect(msg) {
    $("pfm-app").innerHTML = `
      <div class="pfm-connect">
        <div class="ic-wrap">${ICON.link}</div>
        <h3>Connect a bank</h3>
        <p>${escapeHtml(msg || "Link a customer's bank accounts via Open Finance to see balances, spending, and transactions here.")}</p>
        <p style="margin-top:6px;font-size:12px;color:#6b7280;line-height:1.5">
          For test details on connecting a new bank, use Mastercard Developers Test Personas:
          <a href="https://developer.mastercard.com/open-finance-us/documentation/integration-and-testing/test-the-apis/#test-personas" target="_blank" rel="noopener">Test Personas ↗</a>
        </p>
        <button class="btn btn-primary" id="pfm-inapp-connect">Connect new bank</button>
      </div>
    `;
    const b = document.getElementById("pfm-inapp-connect");
    if (b) b.addEventListener("click", () => pfmStartConnect());
  }

  function pfmLoad(cid) {
    if (!cid) { pfmShowConnect("Enter a Customer ID."); return; }
    PFM.cid = cid;
    $("pfm-app").innerHTML = `<div class="pfm-connect"><div class="ic-wrap">${ICON.sparkles}</div><p>Loading accounts and transactions…</p></div>`;
    pfmIslandFlash("Loading…");
    fetch(`/usecases/pfm/data?customer_id=${encodeURIComponent(cid)}`)
      .then((r) => r.json().then((d) => ({ ok: r.ok, d })))
      .then(({ ok, d }) => {
        if (!ok || d.error) { pfmShowConnect(d.error || "Could not load data."); return; }
        PFM.data = d;
        PFM.data.recurring = null;
        PFM.tab = "home";
        PFM.selectedAcct = null;
        pfmIslandFlash(`Loaded · ${d.accounts.length} accounts`);
        pfmDrawTabs();
        pfmDrawScreen();
        pfmLazyLoad(cid, d.transactions || []);
      })
      .catch((e) => pfmShowConnect("Network error: " + e.message));
  }

  // Show a simple spinner message inside the iPhone screen (during post-Connect load)
  function pfmShowConnectLoading(msg) {
    const app = document.getElementById("pfm-app");
    if (!app) return;
    app.innerHTML = `<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;gap:14px;padding:24px">
      <div class="spinner" style="width:32px;height:32px;border:3px solid #e5e7eb;border-top-color:#2563eb;border-radius:50%;animation:pfm-spin 0.8s linear infinite"></div>
      <p style="font-size:13px;color:#6b7280;text-align:center;margin:0">${msg}</p>
    </div>`;
  }

  // Load accounts for cid after Connect, retrying if accounts or transactions are missing.
  // On the first attempt with accounts but no transactions, triggers a server-side refresh.
  function pfmLoadWithRetry(cid, maxTries, _refreshed) {
    if (!cid) { pfmShowConnect("No customer — please try again."); return; }
    fetch(`/usecases/pfm/data?customer_id=${encodeURIComponent(cid)}`)
      .then(r => r.json())
      .then(d => {
        if (d.error) { pfmShowConnect("Error loading accounts: " + d.error); return; }
        const accs = d.accounts || [];
        const txns = d.transactions || [];
        // Retry if no accounts yet
        if (accs.length === 0 && maxTries > 1) {
          pfmShowConnectLoading("Waiting for accounts… (" + maxTries + " retries left)");
          setTimeout(() => pfmLoadWithRetry(cid, maxTries - 1, _refreshed), 3000);
          return;
        }
        // Accounts exist but no transactions — trigger a server-side refresh once, then retry
        if (accs.length > 0 && txns.length === 0 && !_refreshed && maxTries > 1) {
          pfmShowConnectLoading("Refreshing account data…");
          fetch("/usecases/pfm/action", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ action: "refresh_accounts", params: { customer_id: cid } }),
          }).finally(() => {
            setTimeout(() => pfmLoadWithRetry(cid, maxTries - 1, true), 4000);
          });
          return;
        }
        // We have data (or exhausted retries) — render the home screen
        PFM.cid = cid;
        PFM.data = d;
        PFM.data.recurring = null;
        PFM.tab = "home";
        PFM.selectedAcct = null;
        pfmIslandFlash(`Loaded · ${accs.length} accounts · ${txns.length} transactions`);
        pfmDrawTabs();
        pfmDrawScreen();
        pfmLazyLoad(cid, txns);
      })
      .catch(() => {
        if (maxTries > 1) setTimeout(() => pfmLoadWithRetry(cid, maxTries - 1, _refreshed), 3000);
        else pfmShowConnect("Could not load accounts — please try again.");
      });
  }

  // ---------- Lazy enrichment + recurring (fires after initial load) ----------
  function pfmLazyLoad(cid, txns) {
    if (!cid || !PFM.data) return;
    PFM.data.recurring = null; // null = loading, [] = loaded-empty

    // 1. Enrich transactions in the background
    const payload = (txns || []).slice(0, 50)
      .map(t => ({ id: String(t.id), description: t.description || "", amount: t.amount, date: t.date, account_id: t.account_id || "" }))
      .filter(t => t.description);
    if (payload.length) {
      fetch("/usecases/pfm/action", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "enrich_transactions", params: { transactions: payload } }),
      })
      .then(r => r.json())
      .then(d => {
        if (!d.enriched || !PFM.data) return;
        let changed = false;
        PFM.data.transactions.forEach(t => {
          const e = d.enriched[String(t.id)];
          if (!e) return;
          if (e.name) { t.enrichedName = e.name; changed = true; }
          if (e.logoUrl) t.logoUrl = e.logoUrl;
          if (e.isRecurring) t.isRecurring = true;
          if (e.category) t.enrichedCategory = e.category;
        });
        if (changed) pfmDrawScreen();
      })
      .catch(() => {});
    }

    // 2. Fetch recurring streams in the background
    fetch("/usecases/pfm/action", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "get_recurring", params: { customer_id: cid } }),
    })
    .then(r => r.json())
    .then(d => {
      if (!PFM.data) return;
      PFM.data.recurring = d.streams || [];
      pfmDrawScreen();
    })
    .catch(() => {
      if (PFM.data) { PFM.data.recurring = []; pfmDrawScreen(); }
    });
  }

  // ---------- In-app Connect Experience ----------
  // Calls: create_customer → generate connect_url → open in popup (Finicity
  // Connect refuses to run in an iframe — error 1412). The iPhone shows a
  // waiting screen and polls for accounts; when they appear we load Home.
  function pfmStartConnect() {
    const app = document.getElementById("pfm-app");
    if (!app) return;
    const cidInput = $("pfm-cid");
    const existing = cidInput && cidInput.value.trim();

    pfmShowConnectWaiting("Preparing Connect…", null);
    pfmIslandFlash("Open Finance · Connect");

    // Always create a new customer for "Connect new bank" — this matches the
    // original request (Create Customer → Connect URL) and avoids reloading
    // the old user after the popup closes.
    const ensureCustomer = fetch("/usecases/pfm/action", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "create_customer", params: {} }),
    }).then((r) => r.json());

    ensureCustomer
      .then((res) => {
        if (!res || res.error || !res.customer_id) {
          throw new Error(res && res.error ? res.error : "Could not create customer");
        }
        PFM.cid = String(res.customer_id);
        if (cidInput) cidInput.value = PFM.cid;
        return fetch("/usecases/pfm/action", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ action: "connect_url", params: { customer_id: PFM.cid } }),
        }).then((r) => r.json());
      })
      .then((res) => {
        if (!res || res.error || !res.connect_url) {
          throw new Error(res && res.error ? res.error : "Could not generate Connect URL");
        }
        PFM._connectUrl = res.connect_url;
        // Open Connect in a popup window (Finicity blocks iframe embedding).
        pfmOpenConnectPopup(res.connect_url);
        pfmShowConnectWaiting(`Customer ${PFM.cid}`, res.connect_url);
        pfmPollForAccounts(PFM.cid);
      })
      .catch((e) => pfmShowConnect("Connect error: " + e.message));
  }

  function pfmOpenConnectPopup(url) {
    try {
      const w = 480, h = 760;
      const left = Math.max(0, window.screenX + (window.outerWidth - w) / 2);
      const top = Math.max(0, window.screenY + (window.outerHeight - h) / 2);
      const features = [
        "popup=yes",
        `width=${w}`,
        `height=${h}`,
        `left=${left}`,
        `top=${top}`,
        "resizable=yes",
        "scrollbars=yes",
        "menubar=no",
        "toolbar=no",
        "location=no",
        "status=no",
        "noopener=no",
      ].join(",");
      const win = window.open(url, "vima-connect", features);
      if (!win) return null;
      try { win.focus(); } catch (_) {}
      PFM._connectWin = win;
      // When the popup closes, give Finicity a few seconds to process the
      // newly-linked accounts before fetching, then retry if still empty.
      const watchClose = setInterval(() => {
        try {
          if (win.closed) {
            clearInterval(watchClose);
            PFM._pollStop = true;
            pfmShowConnectLoading("Linking accounts…");
            setTimeout(() => pfmLoadWithRetry(PFM.cid, 8), 3000);
          }
        } catch (_) { clearInterval(watchClose); }
      }, 800);
      PFM._connectWatcher = watchClose;
      return win;
    } catch (_) { return null; }
  }

  function pfmShowConnectWaiting(title, url) {
    const app = document.getElementById("pfm-app");
    if (!app) return;
    const hasUrl = !!url;
    app.innerHTML = `
      <div class="pfm-connect-frame">
        <div class="topbar">
          <button id="pfm-connect-cancel">${ICON.chevLeft} Cancel</button>
          <h4>${escapeHtml(title)}</h4>
          <span style="width:60px"></span>
        </div>
        <div class="loading">
          <div class="spinner"></div>
          <div style="text-align:center;max-width:220px;line-height:1.6;font-size:13px;color:#6a6a6a">
            ${hasUrl
              ? `Select your bank in the popup window, then come back here.`
              : escapeHtml(title)}
          </div>
          ${hasUrl ? `
            <button class="btn btn-primary" id="pfm-connect-done" style="margin-top:16px">Done — load my accounts</button>
            <button class="btn" id="pfm-connect-reopen" style="margin-top:6px">Re-open Connect window</button>
          ` : ""}
        </div>
      </div>
    `;
    const stopConnect = () => {
      PFM._pollStop = true;
      try { clearInterval(PFM._connectWatcher); } catch (_) {}
      try { if (PFM._connectWin && !PFM._connectWin.closed) PFM._connectWin.close(); } catch (_) {}
    };
    const cancel = document.getElementById("pfm-connect-cancel");
    if (cancel) cancel.addEventListener("click", () => {
      stopConnect();
      if (PFM.cid && PFM.data) pfmDrawScreen();
      else if (PFM.cid) pfmLoad(PFM.cid);
      else pfmShowConnect("Connect cancelled.");
    });
    const done = document.getElementById("pfm-connect-done");
    if (done) done.addEventListener("click", () => {
      stopConnect();
      if (PFM.cid) pfmLoadWithRetry(PFM.cid, 8);
      else pfmShowConnect("No customer — please try again.");
    });
    const reopen = document.getElementById("pfm-connect-reopen");
    if (reopen) reopen.addEventListener("click", () => {
      if (PFM._connectUrl) pfmOpenConnectPopup(PFM._connectUrl);
    });
  }


  function pfmPollForAccounts(cid) {
    PFM._pollStop = false;
    const started = Date.now();
    const tick = () => {
      if (PFM._pollStop) return;
      if (Date.now() - started > 5 * 60 * 1000) return; // 5 min cap
      fetch(`/usecases/pfm/data?customer_id=${encodeURIComponent(cid)}`)
        .then((r) => r.json())
        .then((d) => {
          if (PFM._pollStop) return;
          if (d && Array.isArray(d.accounts) && d.accounts.length > 0) {
            PFM.data = d;
            PFM.tab = "home";
            PFM.selectedAcct = null;
            pfmIslandFlash(`Linked · ${d.accounts.length} accounts`);
            pfmDrawTabs();
            pfmDrawScreen();
            return;
          }
          setTimeout(tick, 4000);
        })
        .catch(() => setTimeout(tick, 6000));
    };
    setTimeout(tick, 4000);
  }

  function pfmDrawScreen() {
    const app = document.getElementById("pfm-app");
    if (!app || !PFM.data) return;
    let html = "";
    if (PFM.tab === "home") html = pfmScreenHome();
    else if (PFM.tab === "accounts") html = PFM.selectedAcct ? pfmScreenAcctDetail() : pfmScreenAccounts();
    else if (PFM.tab === "insights") html = pfmScreenInsights();
    else if (PFM.tab === "settings") html = pfmScreenSettings();
    app.innerHTML = `<div class="pfm-screen">${html}</div>`;
    app.scrollTop = 0;
    pfmWireScreen();
  }

  // ---------- Home screen ----------
  function pfmScreenHome() {
    const d = PFM.data, s = d.summary || {};
    const accounts = d.accounts || [];
    const txns = d.transactions || [];
    const cats = d.categories || [];
    const heroBalance = s.assets || 0;
    const net = s.monthly_income - s.monthly_spend;
    const netPct = s.monthly_income > 0 ? Math.round((net / s.monthly_income) * 100) : 0;

    // 7-day spend sparkline
    const spark = pfmSparkline(txns, 7);

    const acctList = accounts.slice(0, 4).map(pfmAcctRow).join("") || pfmEmptyLine("No accounts linked.");
    const stackBar = pfmStackBar(cats);
    const stackLegend = cats.slice(0, 5).map(pfmLegendRow).join("") || pfmEmptyLine("No spending this month.");
    const txnList = pfmGroupedTxns(txns.slice(0, 12));

    // Subscriptions section — null = still loading, [] = none found
    const recurring = d.recurring;
    const subs = recurring ? recurring.filter(s => s.type === "DEBIT") : null;
    const incStreams = recurring ? recurring.filter(s => s.type === "CREDIT") : null;
    let subsSection = "";
    if (recurring === null) {
      subsSection = `
        <div class="pfm-section-title"><h4>Subscriptions</h4><span class="pfm-enriching-label">loading…</span></div>
        <div class="pfm-sub-skeleton"></div>`;
    } else if (subs.length) {
      subsSection = `
        <div class="pfm-section-title"><h4>Subscriptions</h4><span style="font-size:11px;color:#9a9a9a;font-weight:600">${subs.length}</span></div>
        <div class="pfm-sub-scroll">${subs.slice(0, 8).map(pfmSubCard).join("")}</div>`;
    }
    let incSection = "";
    if (incStreams && incStreams.length) {
      incSection = `
        <div class="pfm-section-title"><h4>Regular Income</h4><span style="font-size:11px;color:#9a9a9a;font-weight:600">${incStreams.length}</span></div>
        <div class="pfm-sub-scroll">${incStreams.slice(0, 4).map(pfmSubCard).join("")}</div>`;
    }

    return `
      <div class="pfm-greet">
        <div>
          <div class="hello">${pfmGreeting()}</div>
          <h3>Welcome back</h3>
        </div>
        <div class="pfm-avatar" title="Profile">V</div>
      </div>
      <div class="pfm-hero" data-action="cycle-hero">
        <div class="label">Total Balance</div>
        <div class="amount">${fmtMoney(heroBalance)}</div>
        <div class="trend ${net >= 0 ? "pos" : "neg"}">
          ${net >= 0 ? ICON.arrowUp : ICON.arrowDown}
          ${fmtMoney(Math.abs(net))} this month
        </div>
        <div class="spark">${spark}</div>
      </div>
      <div class="pfm-quick">
        <button data-quick="send"><span class="ic">${ICON.arrowUp}</span>Send</button>
        <button data-quick="request"><span class="ic">${ICON.arrowDown}</span>Request</button>
        <button data-quick="pay"><span class="ic">${ICON.plus}</span>Pay</button>
        <button data-quick="more"><span class="ic">${ICON.more}</span>More</button>
      </div>
      <div class="pfm-section-title"><h4>Accounts</h4>
        <button class="link" data-goto="accounts">${accounts.length} linked ${ICON.chev}</button></div>
      <div class="pfm-card">${acctList}</div>

      <div class="pfm-section-title"><h4>This Month</h4>
        <button class="link" data-goto="insights">Insights ${ICON.chev}</button></div>
      <div class="pfm-card" style="padding:14px">
        <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:4px">
          <span style="font-size:12px;color:#6a6a6a;font-weight:500">Spent</span>
          <span style="font-size:20px;font-weight:700;letter-spacing:-0.3px;font-feature-settings:tnum">${fmtMoney(s.monthly_spend)}</span>
        </div>
        ${stackBar}
        <div class="pfm-legend">${stackLegend}</div>
      </div>

      ${subsSection}
      ${incSection}

      <div class="pfm-section-title"><h4>Recent</h4>
        <button class="link" data-goto="accounts">All ${ICON.chev}</button></div>
      ${txnList}
    `;
  }

  function pfmSubCard(s) {
    const freq = { WEEKLY: "/ wk", BIWEEKLY: "/ 2 wk", MONTHLY: "/ mo", QUARTERLY: "/ qtr", ANNUAL: "/ yr" };
    const label = freq[s.frequency] || ("/ " + (s.frequency || "?").toLowerCase());
    const color = pfmColor(s.category);
    const initials = (s.merchantName || "?").slice(0, 2).toUpperCase();
    const isIncome = s.type === "CREDIT";
    return `
      <div class="pfm-sub-card">
        <div class="pfm-sub-avatar" style="background:${color}1a;color:${color}">${initials}</div>
        <div class="pfm-sub-name">${escapeHtml(s.merchantName)}</div>
        <div class="pfm-sub-freq">${escapeHtml(label)}</div>
        <div class="pfm-sub-amt ${isIncome ? "pos" : ""}">${isIncome ? "+" : ""}${fmtMoney(Math.abs(s.amount))}</div>
      </div>
    `;
  }

  function pfmGreeting() {
    const h = new Date().getHours();
    if (h < 12) return "Good morning";
    if (h < 18) return "Good afternoon";
    return "Good evening";
  }

  // 7-day spending sparkline (SVG)
  function pfmSparkline(txns, days) {
    const now = Date.now() / 1000;
    const dayMs = 24 * 3600;
    const buckets = new Array(days).fill(0);
    txns.forEach((t) => {
      if (!t.date || t.amount >= 0) return;
      const age = (now - t.date) / dayMs;
      const idx = days - 1 - Math.floor(age);
      if (idx >= 0 && idx < days) buckets[idx] += Math.abs(t.amount);
    });
    const max = Math.max(...buckets, 1);
    const W = 280, H = 44, padX = 4;
    const stepX = (W - padX * 2) / (days - 1 || 1);
    const points = buckets.map((v, i) => `${padX + i * stepX},${H - 4 - (v / max) * (H - 12)}`).join(" ");
    // Area path
    const area = `M${padX},${H} L${points.replace(/ /g, " L")} L${W - padX},${H} Z`;
    return `<svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="none" style="width:100%;height:100%">
      <defs><linearGradient id="pfm-spark-grad" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#635bff" stop-opacity="0.25"/>
        <stop offset="100%" stop-color="#635bff" stop-opacity="0"/>
      </linearGradient></defs>
      <path d="${area}" fill="url(#pfm-spark-grad)"/>
      <polyline points="${points}" fill="none" stroke="#635bff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>`;
  }

  // Stacked horizontal category bar
  function pfmStackBar(cats) {
    if (!cats.length) return `<div class="pfm-stack"></div>`;
    const segs = cats.slice(0, 8).map((c) =>
      `<span style="width:${Math.max(c.pct, 1)}%;background:${pfmColor(c.category)}"></span>`
    ).join("");
    return `<div class="pfm-stack">${segs}</div>`;
  }

  function pfmLegendRow(c) {
    return `
      <div class="pfm-legend-row">
        <div class="l">
          <span class="cat-dot" style="background:${pfmColor(c.category)}"></span>
          <span class="name">${escapeHtml(c.category)}</span>
        </div>
        <div class="r">
          <span class="pct">${c.pct}%</span>
          <span class="amt">${fmtMoney(c.amount)}</span>
        </div>
      </div>
    `;
  }

  // ---------- Accounts screen ----------
  function pfmScreenAccounts() {
    const d = PFM.data;
    const accounts = d.accounts || [];
    const txns = d.transactions || [];
    const filtered = PFM.txnQuery
      ? txns.filter((t) => (t.name || "").toLowerCase().includes(PFM.txnQuery.toLowerCase())
                        || (t.category || "").toLowerCase().includes(PFM.txnQuery.toLowerCase()))
      : txns;

    return `
      <div class="pfm-screen-title">Accounts</div>
      <div class="pfm-card">${accounts.map(pfmAcctRow).join("") || pfmEmptyLine("No accounts linked.")}</div>
      <div class="pfm-section-title"><h4>Transactions</h4>
        <span style="font-size:11px;color:#9a9a9a;font-weight:600">${filtered.length}</span></div>
      <div class="pfm-txn-search">
        ${ICON.search}
        <input id="pfm-search" type="text" placeholder="Search transactions" value="${escapeHtml(PFM.txnQuery)}" />
      </div>
      ${pfmGroupedTxns(filtered)}
    `;
  }

  function pfmScreenAcctDetail() {
    const a = PFM.selectedAcct;
    const txns = (PFM.data.transactions || []).filter((t) => String(t.account_id) === String(a.id));
    const iconCls = ACCT_ICON[a.type] ? a.type : "other";
    return `
      <button class="link" data-back style="background:none;border:none;color:#635bff;font-weight:600;padding:8px 0;cursor:pointer;display:inline-flex;align-items:center;gap:4px;font-size:13px">${ICON.chevLeft} Accounts</button>
      <div style="display:flex;align-items:center;gap:14px;margin:6px 0 16px">
        <div class="pfm-acct-icon ${iconCls}" style="width:48px;height:48px;border-radius:14px">${pfmAcctIcon(a.type)}</div>
        <div>
          <div style="font-size:18px;font-weight:700;letter-spacing:-0.3px">${escapeHtml(a.name)}</div>
          <div style="font-size:12px;color:#6a6a6a;text-transform:capitalize">${escapeHtml(a.type)} · ${escapeHtml(a.number)}</div>
        </div>
      </div>
      <div class="pfm-hero" style="cursor:default">
        <div class="label">Current Balance</div>
        <div class="amount ${a.balance < 0 ? "" : ""}" style="${a.balance < 0 ? "color:#df1b41" : ""}">${fmtMoney(a.balance)}</div>
        <div style="display:flex;gap:24px;margin-top:14px;font-size:12px">
          <div><div style="color:#6a6a6a;font-size:10px;text-transform:uppercase;letter-spacing:0.6px;font-weight:600">Available</div><div style="font-weight:700;margin-top:2px;font-feature-settings:tnum">${fmtMoney(a.available_balance != null ? a.available_balance : a.balance)}</div></div>
          <div><div style="color:#6a6a6a;font-size:10px;text-transform:uppercase;letter-spacing:0.6px;font-weight:600">Currency</div><div style="font-weight:700;margin-top:2px">${escapeHtml(a.currency || "USD")}</div></div>
          <div><div style="color:#6a6a6a;font-size:10px;text-transform:uppercase;letter-spacing:0.6px;font-weight:600">Activity</div><div style="font-weight:700;margin-top:2px">${txns.length} txns</div></div>
        </div>
      </div>
      <div class="pfm-section-title"><h4>Transactions</h4>
        <span style="font-size:11px;color:#9a9a9a;font-weight:600">${txns.length}</span></div>
      ${pfmGroupedTxns(txns)}
    `;
  }

  // ---------- Insights screen ----------
  function pfmScreenInsights() {
    const d = PFM.data, s = d.summary || {};
    const cats = d.categories || [];
    const txns = d.transactions || [];
    const total = cats.reduce((acc, c) => acc + (c.amount || 0), 0) || 0;

    // Compute 4-week cashflow
    const weeks = pfmWeekly(txns, 4);
    // Compute day-of-week spending heatmap
    const heat = pfmHeatmap(txns);
    // Top merchants
    const merchants = pfmTopMerchants(txns);

    // Insight: most-spent category
    const top = cats[0];
    const avgPerDay = total / 30;

    return `
      <div class="pfm-screen-title">Insights</div>

      <div class="pfm-kpi-grid">
        <div class="pfm-kpi">
          <div class="k">Spent · 30d</div>
          <div class="v">${fmtMoney(total)}</div>
          <div class="sub">${fmtMoney(avgPerDay)} / day avg</div>
        </div>
        <div class="pfm-kpi">
          <div class="k">Income · 30d</div>
          <div class="v pos">${fmtMoney(s.monthly_income)}</div>
          <div class="sub ${s.monthly_income > s.monthly_spend ? "pos" : "neg"}">
            ${s.monthly_income > s.monthly_spend ? "↑" : "↓"} ${fmtMoney(Math.abs(s.monthly_income - s.monthly_spend))} net
          </div>
        </div>
      </div>

      ${top ? `
      <div class="pfm-tip">
        <div class="ic">${ICON.sparkles}</div>
        <div class="body">
          You spent <strong>${fmtMoney(top.amount)}</strong> on <strong>${escapeHtml(top.category)}</strong> this month — ${top.pct}% of your total spend.
        </div>
      </div>` : ""}

      <div class="pfm-isection">
        <h5>Weekly cashflow</h5>
        <p class="desc">Income vs. spend, last 4 weeks</p>
        ${pfmCashflowChart(weeks)}
        <div style="display:flex;gap:14px;margin-top:12px;font-size:11px;font-weight:600;color:#6a6a6a">
          <span style="display:inline-flex;align-items:center;gap:6px"><span style="width:8px;height:8px;background:#0f7050;border-radius:2px"></span>Income</span>
          <span style="display:inline-flex;align-items:center;gap:6px"><span style="width:8px;height:8px;background:#e5e5e5;border-radius:2px"></span>Spend</span>
        </div>
      </div>

      <div class="pfm-isection">
        <h5>Category breakdown</h5>
        <p class="desc">${fmtMoney(total)} spent across ${cats.length} categories</p>
        ${pfmStackBar(cats)}
        <div class="pfm-legend">${cats.map(pfmLegendRow).join("") || pfmEmptyLine("No spending data.")}</div>
      </div>

      <div class="pfm-isection">
        <h5>Spending by weekday</h5>
        <p class="desc">When you spend the most</p>
        ${pfmHeatmapHtml(heat)}
      </div>

      <div class="pfm-isection">
        <h5>Top merchants</h5>
        <p class="desc">Where your money goes</p>
        ${merchants.length ? merchants.map((m, i) => `
          <div class="pfm-merchant">
            <div class="l">
              <div class="rank">${i + 1}</div>
              <div>
                <div class="nm">${escapeHtml(m.name)}</div>
                <div class="ct">${m.count} ${m.count === 1 ? "transaction" : "transactions"} · ${escapeHtml(m.category)}</div>
              </div>
            </div>
            <div class="am">${fmtMoney(m.total)}</div>
          </div>
        `).join("") : pfmEmptyLine("No merchant data.")}
      </div>
    `;
  }

  // 4-week income/spend buckets
  function pfmWeekly(txns, n) {
    const now = Date.now() / 1000;
    const week = 7 * 24 * 3600;
    const buckets = [];
    for (let i = n - 1; i >= 0; i--) {
      const start = now - (i + 1) * week;
      const end = now - i * week;
      let income = 0, spend = 0;
      txns.forEach((t) => {
        if (t.date >= start && t.date < end) {
          if (t.amount > 0) income += t.amount;
          else spend += Math.abs(t.amount);
        }
      });
      buckets.push({ income, spend, label: `W${n - i}` });
    }
    return buckets;
  }

  function pfmCashflowChart(weeks) {
    const max = Math.max(1, ...weeks.flatMap((w) => [w.income, w.spend]));
    return `<div class="pfm-cashflow">
      ${weeks.map((w) => {
        const hi = (w.income / max) * 100;
        const hs = (w.spend / max) * 100;
        return `<div class="pfm-cashflow-bar">
          <div class="bars">
            <span class="b income" style="height:${Math.max(hi, 2)}%" title="Income ${fmtMoney(w.income)}"></span>
            <span class="b spend" style="height:${Math.max(hs, 2)}%" title="Spend ${fmtMoney(w.spend)}"></span>
          </div>
          <span class="lbl">${escapeHtml(w.label)}</span>
        </div>`;
      }).join("")}
    </div>`;
  }

  // Day-of-week spending heatmap (intensity by total spend on that weekday in last 30d)
  function pfmHeatmap(txns) {
    const now = Date.now() / 1000;
    const cutoff = now - 30 * 24 * 3600;
    const totals = [0, 0, 0, 0, 0, 0, 0];
    txns.forEach((t) => {
      if (!t.date || t.amount >= 0 || t.date < cutoff) return;
      const d = new Date(t.date * 1000);
      totals[d.getDay()] += Math.abs(t.amount);
    });
    const max = Math.max(...totals, 1);
    return totals.map((v) => ({ amt: v, pct: v / max }));
  }
  function pfmHeatmapHtml(heat) {
    const dows = ["S", "M", "T", "W", "T", "F", "S"];
    return `
      <div class="pfm-heatmap">${dows.map((d) => `<div class="dow">${d}</div>`).join("")}</div>
      <div class="pfm-heatmap" style="margin-top:2px">${heat.map((h) => {
        const opacity = 0.08 + h.pct * 0.85;
        return `<div class="day" style="background:rgba(99,91,255,${opacity.toFixed(2)})" title="${fmtMoney(h.amt)}">${h.amt > 0 ? fmtMoneyShort(h.amt) : ""}</div>`;
      }).join("")}</div>
    `;
  }

  function pfmTopMerchants(txns) {
    const now = Date.now() / 1000;
    const cutoff = now - 30 * 24 * 3600;
    const map = {};
    txns.forEach((t) => {
      if (!t.date || t.amount >= 0 || t.date < cutoff) return;
      const key = t.name || "Unknown";
      if (!map[key]) map[key] = { name: key, total: 0, count: 0, category: t.category };
      map[key].total += Math.abs(t.amount);
      map[key].count += 1;
    });
    return Object.values(map).sort((a, b) => b.total - a.total).slice(0, 5);
  }

  // ---------- Settings screen ----------
  function pfmScreenSettings() {
    return `
      <div class="pfm-screen-title">Settings</div>
      <div class="pfm-settings-card">
        <div class="pfm-setting-row" data-action="open-profile">
          <div class="left"><div class="ic" style="background:#eff4ff;color:#2563eb">${ICON.user}</div>
            <div><div class="label">Profile</div><div class="val" style="font-size:11px">Customer ${escapeHtml(PFM.cid)}</div></div></div>
          <span class="val">${ICON.chev}</span>
        </div>
        <div class="pfm-setting-row" data-action="toggle-notif">
          <div class="left"><div class="ic" style="background:#fff4e5;color:#c2410c">${ICON.bell}</div>
            <div class="label">Notifications</div></div>
          <div class="pfm-toggle" id="pfm-tog-notif"></div>
        </div>
        <div class="pfm-setting-row" data-action="toggle-bio">
          <div class="left"><div class="ic" style="background:#ecfdf5;color:#0f7050">${ICON.lock}</div>
            <div class="label">Face ID</div></div>
          <div class="pfm-toggle" id="pfm-tog-bio"></div>
        </div>
      </div>
      <div class="pfm-settings-card">
        <div class="pfm-setting-row">
          <div class="left"><div class="ic" style="background:#f3f0ff;color:#635bff">${ICON.bank}</div>
            <div class="label">Linked accounts</div></div>
          <span class="val">${(PFM.data.accounts || []).length}</span>
        </div>
        <div class="pfm-setting-row">
          <div class="left"><div class="ic" style="background:#fef2f2;color:#df1b41">${ICON.download}</div>
            <div class="label">Export data</div></div>
          <span class="val">${ICON.chev}</span>
        </div>
        <div class="pfm-setting-row">
          <div class="left"><div class="ic" style="background:#f4f4f5;color:#6a6a6a">${ICON.info}</div>
            <div class="label">About</div></div>
          <span class="val">v1.0.0</span>
        </div>
      </div>
      <p style="text-align:center;font-size:11px;color:#9a9a9a;margin-top:14px;font-weight:500">Powered by Mastercard Open Finance</p>
    `;
  }

  // ---------- Helpers (rows) ----------
  function pfmAcctRow(a) {
    const iconCls = ACCT_ICON[a.type] ? a.type : "other";
    return `
      <div class="pfm-acct" data-acct-id="${escapeHtml(String(a.id))}">
        <div class="left">
          <div class="pfm-acct-icon ${iconCls}">${pfmAcctIcon(a.type)}</div>
          <div>
            <div class="name">${escapeHtml(a.name)}</div>
            <div class="meta">${escapeHtml(a.type)} · ${escapeHtml(a.number)}</div>
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:6px">
          <div class="bal ${a.balance < 0 ? "neg" : ""}">${fmtMoney(a.balance)}</div>
          <span class="chev">${ICON.chev}</span>
        </div>
      </div>
    `;
  }
  function pfmCatRow(c) {
    const color = pfmColor(c.category);
    return `
      <div class="pfm-cat-row">
        <div class="top">
          <span class="cat"><span class="cat-dot" style="background:${color}"></span>${escapeHtml(c.category)}</span>
          <span class="amt">${fmtMoney(c.amount)} · ${c.pct}%</span>
        </div>
        <div class="bar"><span style="width:${Math.max(c.pct, 3)}%;background:${color}"></span></div>
      </div>
    `;
  }
  function pfmTxnRow(t) {
    const isPos = t.amount > 0;
    const cat = t.enrichedCategory || t.category;
    const color = pfmColor(cat);
    const displayName = t.enrichedName || t.name;
    const iconHtml = t.logoUrl
      ? `<img src="${escapeHtml(t.logoUrl)}" class="pfm-txn-logo-img" alt="" loading="lazy">`
      : `<div class="pfm-txn-icon" style="background:${color}1a;color:${color}">${pfmCatIcon(cat)}</div>`;
    const recurBadge = t.isRecurring ? `<span class="pfm-recurring-badge">↻</span>` : "";
    return `
      <div class="pfm-txn" data-txn-id="${escapeHtml(String(t.id || ""))}">
        <div class="left">
          ${iconHtml}
          <div class="info">
            <div class="name">${escapeHtml(displayName)}${recurBadge}</div>
            <div class="meta">${escapeHtml(cat)}</div>
          </div>
        </div>
        <div class="amt ${isPos ? "pos" : "neg"}">${isPos ? "+" : ""}${fmtMoney(t.amount)}</div>
      </div>
    `;
  }
  function pfmEmptyLine(msg) {
    return `<p class="muted" style="font-size:12px;padding:8px;text-align:center">${escapeHtml(msg)}</p>`;
  }

  function pfmGroupedTxns(txns) {
    if (!txns.length) return pfmEmptyLine("No transactions match.");
    // Group by date label
    const groups = {};
    const order = [];
    txns.forEach((t) => {
      const k = fmtDate(t.date) || "—";
      if (!groups[k]) { groups[k] = []; order.push(k); }
      groups[k].push(t);
    });
    return order.map((k) => `
      <div class="pfm-txn-group">
        <div class="pfm-txn-group-date">${escapeHtml(k)}</div>
        <div class="pfm-txn-list">${groups[k].map(pfmTxnRow).join("")}</div>
      </div>
    `).join("");
  }

  // ---------- Wire interactions for current screen ----------
  function pfmWireScreen() {
    const app = document.getElementById("pfm-app");
    if (!app) return;

    // Account row → drill in
    app.querySelectorAll("[data-acct-id]").forEach((el) => {
      el.addEventListener("click", () => {
        const a = (PFM.data.accounts || []).find((x) => String(x.id) === el.dataset.acctId);
        if (!a) return;
        PFM.selectedAcct = a;
        PFM.tab = "accounts";
        pfmIslandFlash(a.name);
        pfmDrawTabs();
        pfmDrawScreen();
      });
    });

    // Txn row → open sheet
    app.querySelectorAll("[data-txn-id]").forEach((el) => {
      el.addEventListener("click", () => {
        const t = (PFM.data.transactions || []).find((x) => String(x.id) === el.dataset.txnId);
        if (t) pfmOpenSheet(t);
      });
    });

    // Section "Go to" buttons
    app.querySelectorAll("[data-goto]").forEach((el) => {
      el.addEventListener("click", () => {
        PFM.tab = el.dataset.goto;
        PFM.selectedAcct = null;
        pfmDrawTabs();
        pfmDrawScreen();
      });
    });

    // Back from account detail
    const back = app.querySelector("[data-back]");
    if (back) back.addEventListener("click", () => {
      PFM.selectedAcct = null;
      pfmDrawScreen();
    });

    // Quick actions
    app.querySelectorAll("[data-quick]").forEach((el) => {
      el.addEventListener("click", () => {
        const labels = { send: "Send money", request: "Request", pay: "Pay bill", more: "More" };
        pfmIslandFlash(labels[el.dataset.quick] || "Action");
      });
    });

    // Search
    const search = document.getElementById("pfm-search");
    if (search) {
      search.addEventListener("input", (e) => {
        PFM.txnQuery = e.target.value;
        // Re-render only the bottom group, keep focus
        const cursor = search.selectionStart;
        pfmDrawScreen();
        const s2 = document.getElementById("pfm-search");
        if (s2) { s2.focus(); s2.setSelectionRange(cursor, cursor); }
      });
    }

    // Toggles
    const t1 = document.getElementById("pfm-tog-notif");
    if (t1) t1.addEventListener("click", () => t1.classList.toggle("off"));
    const t2 = document.getElementById("pfm-tog-bio");
    if (t2) { t2.classList.add("off"); t2.addEventListener("click", () => t2.classList.toggle("off")); }

    // Hero tap → cycle island flash
    const hero = app.querySelector('[data-action="cycle-hero"]');
    if (hero) hero.addEventListener("click", () => {
      const s = PFM.data.summary || {};
      pfmIslandFlash(`Net Worth · ${fmtMoney(s.net_worth)}`);
    });
  }

  function pfmOpenSheet(t) {
    const isPos = t.amount > 0;
    const cat = t.enrichedCategory || t.category;
    const color = pfmColor(cat);
    const displayName = t.enrichedName || t.name;
    const acct = (PFM.data.accounts || []).find((a) => String(a.id) === String(t.account_id));
    const sheet = document.getElementById("pfm-sheet");
    const back = document.getElementById("pfm-sheet-backdrop");
    if (!sheet || !back) return;
    const logoHtml = t.logoUrl
      ? `<img src="${escapeHtml(t.logoUrl)}" class="pfm-sheet-logo" alt="" loading="lazy">`
      : `<div class="pfm-sheet-icon" style="background:${color}1a;color:${color}">${pfmCatIcon(cat)}</div>`;
    const recurRow = t.isRecurring
      ? `<div class="pfm-sheet-row"><span class="k">Recurring</span><span class="v" style="color:#635bff;font-weight:600">↻ Yes</span></div>`
      : "";
    sheet.innerHTML = `
      <div class="pfm-sheet-handle"></div>
      ${logoHtml}
      <h3>${escapeHtml(displayName)}</h3>
      <div class="sheet-amount ${isPos ? "pos" : ""}">${isPos ? "+" : ""}${fmtMoney(t.amount)}</div>
      <div class="pfm-sheet-row"><span class="k">Category</span><span class="v">${escapeHtml(cat)}</span></div>
      <div class="pfm-sheet-row"><span class="k">Date</span><span class="v">${fmtDate(t.date)}</span></div>
      <div class="pfm-sheet-row"><span class="k">Status</span><span class="v">${escapeHtml(t.status || "Posted")}</span></div>
      <div class="pfm-sheet-row"><span class="k">Account</span><span class="v">${escapeHtml(acct ? acct.name : t.account_id || "—")}</span></div>
      ${recurRow}
      ${t.description ? `<div class="pfm-sheet-row"><span class="k">Raw description</span><span class="v" style="max-width:60%;font-size:12px">${escapeHtml(t.description)}</span></div>` : ""}
      <div class="pfm-sheet-row"><span class="k">Transaction ID</span><span class="v" style="font-family:var(--mono);font-size:11px">${escapeHtml(String(t.id || "—"))}</span></div>
    `;
    requestAnimationFrame(() => {
      sheet.classList.add("visible");
      back.classList.add("visible");
    });
  }
  function pfmCloseSheet() {
    const sheet = document.getElementById("pfm-sheet");
    const back = document.getElementById("pfm-sheet-backdrop");
    if (sheet) sheet.classList.remove("visible");
    if (back) back.classList.remove("visible");
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

  function _esManifest() { return USE_CASES.find(u => u.id === "easysavings"); }

  function renderEasySavings() {
    const m = _esManifest();
    if (m && m.defaults) {
      if (!ES._inited) {
        ES.bin = m.defaults.bin || ES.bin;
        ES.country = m.defaults.country || ES.country;
        ES.language = m.defaults.language || ES.language;
        ES._inited = true;
      }
    }
    esRender();
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
  // "Near Me" merchant discovery — search for nearby merchants on a map.

  const PL = {
    lat: "38.7468239",
    lng: "-90.7460708",
    distance: "15",
    unit: "MILE",
    countryCode: "US",
    industry: "EAP",
    cityName: "",
    places: [],
    total: 0,
    loading: false,
    error: null,
    selected: null,     // locationId of place being viewed in detail panel
    detailLoading: false,
    detail: null,       // full detail from /places/{id}
  };

  function _plManifest() { return USE_CASES.find(u => u.id === "places"); }

  function renderPlaces() {
    const m = _plManifest();
    if (m && m.defaults && !PL._inited) {
      Object.assign(PL, m.defaults);
      PL._inited = true;
    }
    plRender();
  }

  function plRender() {
    const body = $("uc-body");
    if (!body) return;

    const m = _plManifest();
    const presets = (m && m.industryPresets) || [];

    body.innerHTML = `
      <div class="pl-stage">
        <div class="pl-form-card">
          <div class="pl-form-header">
            <div class="pl-form-title">Merchant Discovery</div>
            <div class="pl-form-sub">Find merchants near a location that accept Mastercard.</div>
          </div>
          <div class="pl-form-row">
            <div class="pl-field">
              <label for="pl-lat">Latitude</label>
              <input id="pl-lat" type="text" value="${escapeHtml(PL.lat)}" placeholder="e.g. 38.7468">
            </div>
            <div class="pl-field">
              <label for="pl-lng">Longitude</label>
              <input id="pl-lng" type="text" value="${escapeHtml(PL.lng)}" placeholder="e.g. -90.7461">
            </div>
            <div class="pl-field">
              <label for="pl-distance">Distance</label>
              <input id="pl-distance" type="text" value="${escapeHtml(PL.distance)}" placeholder="15" style="width:60px">
            </div>
            <div class="pl-field">
              <label for="pl-unit">Unit</label>
              <select id="pl-unit">
                <option value="MILE"${PL.unit === "MILE" ? " selected" : ""}>Miles</option>
                <option value="KM"${PL.unit === "KM" ? " selected" : ""}>Km</option>
              </select>
            </div>
            <div class="pl-field">
              <label for="pl-country">Country</label>
              <input id="pl-country" type="text" value="${escapeHtml(PL.countryCode)}" placeholder="US" style="width:50px" maxlength="2">
            </div>
            <div class="pl-field">
              <label for="pl-industry">Industry</label>
              <select id="pl-industry">
                ${presets.map(p =>
                  '<option value="' + escapeHtml(p.value) + '"' + (PL.industry === p.value ? ' selected' : '') + '>' + escapeHtml(p.label) + '</option>'
                ).join("")}
              </select>
            </div>
            <button class="pl-btn pl-btn--primary" id="pl-search-btn"${PL.loading ? " disabled" : ""}>
              ${PL.loading
                ? '<span class="pl-spinner"></span>Searching…'
                : '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" style="width:15px;height:15px;flex-shrink:0"><circle cx="9" cy="9" r="6"/><path d="M15 15l3 3" stroke-linecap="round"/></svg>Search'}
            </button>
          </div>
        </div>
        <div class="pl-result" id="pl-result">
          ${plResultHtml()}
        </div>
      </div>`;
    plWire();
  }

  function plResultHtml() {
    if (PL.loading) {
      return '<div class="pl-loading"><div class="pl-spinner pl-spinner--lg"></div><p>Searching nearby merchants…</p></div>';
    }
    if (PL.error) {
      return '<div class="pl-error">' + escapeHtml(String(PL.error)) + '</div>';
    }
    if (!PL.places.length) {
      return plHeroHtml();
    }

    // Map + list layout
    const center = plCenter();
    const mapHtml = plMapHtml(center);

    return `
      <div class="pl-summary-strip">
        <div class="pl-summary-item"><label>Merchants found</label><span>${PL.total}</span></div>
        <div class="pl-summary-item"><label>Showing</label><span>${PL.places.length}</span></div>
        <div class="pl-summary-item"><label>Radius</label><span>${escapeHtml(PL.distance)} ${PL.unit === "KM" ? "km" : "mi"}</span></div>
      </div>
      ${mapHtml}
      <div class="pl-list" id="pl-list">
        ${PL.places.map((p, i) => plCardHtml(p, i)).join("")}
      </div>
      ${PL.detail ? plDetailPanelHtml(PL.detail) : ""}`;
  }

  function plCenter() {
    if (PL.places.length) {
      const lats = PL.places.filter(p => p.lat != null).map(p => p.lat);
      const lngs = PL.places.filter(p => p.lng != null).map(p => p.lng);
      if (lats.length && lngs.length) {
        return {
          lat: lats.reduce((a, b) => a + b, 0) / lats.length,
          lng: lngs.reduce((a, b) => a + b, 0) / lngs.length,
        };
      }
    }
    return { lat: parseFloat(PL.lat) || 38.7468, lng: parseFloat(PL.lng) || -90.7461 };
  }

  function plMapHtml(center) {
    // Leaflet container. Initialization happens after render in plInitMap().
    return `
      <div class="pl-map-wrap">
        <div class="pl-map-frame" id="pl-leaflet-map" data-center-lat="${center.lat}" data-center-lng="${center.lng}"></div>
        <div class="pl-map-count">${PL.places.length} merchant${PL.places.length !== 1 ? "s" : ""}</div>
      </div>`;
  }

  function plCardHtml(place, idx) {
    const initials = (place.name || "?").replace(/[^A-Za-z0-9 ]/g, "").trim().split(" ")
      .slice(0, 2).map(w => (w[0] || "").toUpperCase()).join("") || "?";
    const colors = ["#6366f1","#0ea5e9","#10b981","#f59e0b","#ec4899","#8b5cf6","#ef4444","#14b8a6","#f97316","#3b82f6"];
    const color = colors[idx % colors.length];

    const capBadges = (place.capabilities || []).slice(0, 5).map(c =>
      '<span class="pl-cap-badge' + (c === "NFC / Contactless" ? ' pl-cap-badge--nfc' : '') + '">' + escapeHtml(c) + '</span>'
    ).join("");

    const statusCls = place.isInBusiness ? "pl-status--open" : "pl-status--closed";
    const statusLabel = place.isInBusiness ? "Active" : "Inactive";

    return `
      <div class="pl-card" data-pl-idx="${idx}" data-pl-id="${escapeHtml(String(place.locationId || ''))}">
        <div class="pl-card-left">
          <div class="pl-card-avatar" style="background:${color}">
            <span>${escapeHtml(initials)}</span>
          </div>
        </div>
        <div class="pl-card-body">
          <div class="pl-card-top">
            <div class="pl-card-name">${escapeHtml(place.name)}</div>
            <span class="pl-status ${statusCls}">${statusLabel}</span>
            ${place.isNewBusiness ? '<span class="pl-new-badge">New</span>' : ""}
          </div>
          ${place.address ? '<div class="pl-card-addr">' + escapeHtml(place.address) + '</div>' : ""}
          ${place.phone ? '<div class="pl-card-phone">' + escapeHtml(place.phone) + '</div>' : ""}
          <div class="pl-card-meta">
            ${place.mccCode ? '<span class="pl-meta-chip">MCC ' + escapeHtml(place.mccCode) + '</span>' : ""}
            ${place.industry ? '<span class="pl-meta-chip">' + escapeHtml(place.industry) + '</span>' : ""}
            ${place.geocodeQuality ? '<span class="pl-meta-chip">' + escapeHtml(place.geocodeQuality) + '</span>' : ""}
            ${place.posTerminals ? '<span class="pl-meta-chip">' + place.posTerminals + ' POS</span>' : ""}
          </div>
          ${capBadges ? '<div class="pl-card-caps">' + capBadges + '</div>' : ""}
          ${place.website ? '<a class="pl-card-link" href="' + escapeHtml(place.website) + '" target="_blank" rel="noopener">' + escapeHtml(place.website.replace(/^https?:\/\//, "").replace(/\/$/, "")) + ' ↗</a>' : ""}
        </div>
        <button class="pl-card-detail-btn" data-detail-id="${escapeHtml(String(place.locationId || ''))}" title="View details">
          <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M7 4l6 6-6 6"/></svg>
        </button>
      </div>`;
  }

  function plDetailPanelHtml(d) {
    const rows = [];
    if (d.legalName)            rows.push(["Legal Name", d.legalName]);
    if (d.aggregateMerchantName) rows.push(["Brand", d.aggregateMerchantName]);
    if (d.parentMerchantName)   rows.push(["Parent", d.parentMerchantName]);
    if (d.mccCode)              rows.push(["MCC", d.mccCode]);
    if (d.industry)             rows.push(["Industry", d.industry]);
    if (d.superIndustry)        rows.push(["Super-industry", d.superIndustry]);
    if (d.geocodeQuality)       rows.push(["Geocode quality", d.geocodeQuality]);
    if (d.channel)              rows.push(["Channel", d.channel === "b" ? "Brick & mortar" : d.channel === "e" ? "E-commerce" : d.channel]);
    if (d.posTerminals)         rows.push(["POS terminals", String(d.posTerminals)]);
    if (d.firstSeen)            rows.push(["First seen", d.firstSeen]);
    if (d.lastSeen)             rows.push(["Last seen", d.lastSeen]);
    if (d.phone)                rows.push(["Phone", d.phone]);
    if (d.website)              rows.push(["Website", d.website]);

    const caps = (d.capabilities || []).map(c =>
      '<span class="pl-detail-cap">' + escapeHtml(c) + '</span>'
    ).join("");

    return `
      <div class="pl-detail-backdrop" id="pl-detail-backdrop"></div>
      <div class="pl-detail-panel" id="pl-detail-panel">
        <div class="pl-detail-head">
          <div>
            <div class="pl-detail-name">${escapeHtml(d.name)}</div>
            ${d.address ? '<div class="pl-detail-addr">' + escapeHtml(d.address) + '</div>' : ""}
          </div>
          <button class="pl-detail-close" id="pl-detail-close" title="Close">✕</button>
        </div>
        ${caps ? '<div class="pl-detail-caps">' + caps + '</div>' : ""}
        <div class="pl-detail-grid">
          ${rows.map(([k, v]) =>
            '<div class="pl-detail-key">' + escapeHtml(k) + '</div><div class="pl-detail-val">' + escapeHtml(v) + '</div>'
          ).join("")}
        </div>
        ${d.lat != null && d.lng != null ? plDetailMapHtml(d) : ""}
      </div>`;
  }

  function plDetailMapHtml(d) {
    return `
      <div class="pl-detail-map">
        <div class="pl-map-frame" id="pl-detail-leaflet-map" data-lat="${d.lat}" data-lng="${d.lng}" data-name="${escapeHtml(d.name || '')}"></div>
      </div>`;
  }

  function plHeroHtml() {
    return `
      <div class="pl-hero">
        <div class="pl-hero-icon">
          <svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5">
            <path d="M24 4C16.3 4 10 10.3 10 18c0 10 14 26 14 26s14-16 14-26c0-7.7-6.3-14-14-14z"/>
            <circle cx="24" cy="18" r="6"/>
          </svg>
        </div>
        <h3>Discover merchants near any location</h3>
        <p>Enter coordinates or a city, choose an industry filter and search radius, then click <strong>Search</strong> to explore merchants accepting Mastercard — with NFC, EMV, and digital wallet capabilities.</p>
        <div class="pl-hero-chips">
          <span class="pl-hero-chip">Global coverage</span>
          <span class="pl-hero-chip">NFC & EMV data</span>
          <span class="pl-hero-chip">Business status</span>
          <span class="pl-hero-chip">Payment capabilities</span>
        </div>
      </div>`;
  }

  function plWire() {
    // Bind form inputs
    const ids = { "pl-lat": "lat", "pl-lng": "lng", "pl-distance": "distance", "pl-country": "countryCode" };
    for (const [elId, key] of Object.entries(ids)) {
      const el = document.getElementById(elId);
      if (el) el.addEventListener("input", () => { PL[key] = el.value.trim(); });
    }
    const unitSel = document.getElementById("pl-unit");
    if (unitSel) unitSel.addEventListener("change", () => { PL.unit = unitSel.value; });
    const indSel = document.getElementById("pl-industry");
    if (indSel) indSel.addEventListener("change", () => { PL.industry = indSel.value; });

    // Search button
    const searchBtn = document.getElementById("pl-search-btn");
    if (searchBtn) searchBtn.addEventListener("click", () => plSearch());

    // Detail buttons
    document.querySelectorAll("[data-detail-id]").forEach(btn => {
      btn.addEventListener("click", (e) => {
        e.stopPropagation();
        plShowDetail(btn.dataset.detailId);
      });
    });

    // Close detail panel
    const closeBtn = document.getElementById("pl-detail-close");
    const backdrop = document.getElementById("pl-detail-backdrop");
    if (closeBtn) closeBtn.addEventListener("click", () => { PL.detail = null; PL.selected = null; plRender(); });
    if (backdrop) backdrop.addEventListener("click", () => { PL.detail = null; PL.selected = null; plRender(); });

    // Animate detail panel in
    if (PL.detail) {
      const panel = document.getElementById("pl-detail-panel");
      const bg = document.getElementById("pl-detail-backdrop");
      if (panel) requestAnimationFrame(() => panel.classList.add("visible"));
      if (bg) requestAnimationFrame(() => bg.classList.add("visible"));
    }

    // Initialize Leaflet maps (deferred until library is loaded)
    plInitMaps();
  }

  function plInitMaps() {
    if (typeof L === "undefined") {
      // Leaflet not loaded yet — retry shortly
      setTimeout(plInitMaps, 80);
      return;
    }

    // --- Results map: all merchants ---
    const mapEl = document.getElementById("pl-leaflet-map");
    if (mapEl && !mapEl._plInited) {
      mapEl._plInited = true;
      const centerLat = parseFloat(mapEl.dataset.centerLat);
      const centerLng = parseFloat(mapEl.dataset.centerLng);
      const map = L.map(mapEl, { scrollWheelZoom: false }).setView([centerLat, centerLng], 12);
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      }).addTo(map);

      const markers = [];
      PL.places.forEach((p, idx) => {
        if (p.lat == null || p.lng == null) return;
        const marker = L.marker([p.lat, p.lng]).addTo(map);
        marker.bindPopup(plPopupHtml(p, idx), { maxWidth: 280 });
        marker.on("popupopen", (ev) => {
          const root = ev.popup.getElement();
          if (!root) return;
          const btn = root.querySelector("[data-popup-detail]");
          if (btn) btn.addEventListener("click", () => plShowDetail(btn.dataset.popupDetail), { once: true });
        });
        markers.push(marker);
      });

      if (markers.length > 1) {
        const group = L.featureGroup(markers);
        map.fitBounds(group.getBounds().pad(0.15));
      } else if (markers.length === 1) {
        map.setView(markers[0].getLatLng(), 14);
      }

      // Re-render on container resize (e.g. flex layout shift)
      setTimeout(() => map.invalidateSize(), 200);
    }

    // --- Detail map: single merchant ---
    const detailEl = document.getElementById("pl-detail-leaflet-map");
    if (detailEl && !detailEl._plInited) {
      detailEl._plInited = true;
      const lat = parseFloat(detailEl.dataset.lat);
      const lng = parseFloat(detailEl.dataset.lng);
      const name = detailEl.dataset.name || "";
      if (!isNaN(lat) && !isNaN(lng)) {
        const map = L.map(detailEl, { scrollWheelZoom: false }).setView([lat, lng], 15);
        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
          maxZoom: 19,
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        }).addTo(map);
        L.marker([lat, lng]).addTo(map).bindPopup("<b>" + escapeHtml(name) + "</b>").openPopup();
        setTimeout(() => map.invalidateSize(), 250);
      }
    }
  }

  function plPopupHtml(p, idx) {
    const caps = (p.capabilities || []).slice(0, 4).map(c =>
      '<span class="pl-popup-cap">' + escapeHtml(c) + '</span>'
    ).join("");
    return `
      <div class="pl-popup">
        <div class="pl-popup-name">${escapeHtml(p.name || "Merchant")}</div>
        ${p.address ? '<div class="pl-popup-addr">' + escapeHtml(p.address) + '</div>' : ""}
        <div class="pl-popup-meta">
          ${p.mccCode ? '<span class="pl-popup-chip">MCC ' + escapeHtml(p.mccCode) + '</span>' : ""}
          ${p.industry ? '<span class="pl-popup-chip">' + escapeHtml(p.industry) + '</span>' : ""}
          ${p.isInBusiness ? '<span class="pl-popup-chip pl-popup-chip--ok">Active</span>' : '<span class="pl-popup-chip pl-popup-chip--off">Inactive</span>'}
        </div>
        ${caps ? '<div class="pl-popup-caps">' + caps + '</div>' : ""}
        ${p.phone ? '<div class="pl-popup-row">📞 ' + escapeHtml(p.phone) + '</div>' : ""}
        ${p.website ? '<div class="pl-popup-row">🔗 <a href="' + escapeHtml(p.website) + '" target="_blank" rel="noopener">' + escapeHtml(p.website.replace(/^https?:\/\//, "").replace(/\/$/, "")) + '</a></div>' : ""}
        ${p.locationId ? '<button class="pl-popup-btn" data-popup-detail="' + escapeHtml(String(p.locationId)) + '">View full details →</button>' : ""}
      </div>`;
  }

  function plSearch() {
    if (!PL.countryCode) return;
    PL.loading = true;
    PL.places = [];
    PL.error = null;
    PL.detail = null;
    PL.selected = null;
    plRender();

    fetch("/usecases/places/action", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        action: "search",
        params: {
          latitude: PL.lat,
          longitude: PL.lng,
          radiusSearch: !!(PL.lat && PL.lng),
          distance: PL.distance,
          unit: PL.unit,
          countryCode: PL.countryCode,
          industry: PL.industry,
          cityName: PL.cityName,
        },
      }),
    })
      .then(r => r.json())
      .then(d => {
        PL.loading = false;
        if (d.error) {
          PL.error = typeof d.error === "string" ? d.error : JSON.stringify(d.error);
        } else {
          PL.places = d.places || [];
          PL.total = d.total || PL.places.length;
        }
        plRender();
      })
      .catch(err => {
        PL.loading = false;
        PL.error = err.message || String(err);
        plRender();
      });
  }

  function plShowDetail(locationId) {
    if (!locationId || PL.detailLoading) return;
    PL.selected = locationId;
    PL.detailLoading = true;
    // Eagerly show from cached search data — render once now
    const cached = PL.places.find(p => String(p.locationId) === String(locationId));
    if (cached) { PL.detail = cached; }
    plRender();

    fetch("/usecases/places/action", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "detail", params: { location_id: locationId } }),
    })
      .then(r => r.json())
      .then(d => {
        PL.detailLoading = false;
        if (d.error) {
          // Keep the cached version if detail fetch fails
          if (!PL.detail) { PL.error = typeof d.error === "string" ? d.error : JSON.stringify(d.error); plRender(); }
        } else if (d.place) {
          // Only re-render if the detail response adds new information
          const hasNew = JSON.stringify(d.place) !== JSON.stringify(PL.detail);
          PL.detail = d.place;
          if (hasNew) plRender();
        }
      })
      .catch(() => { PL.detailLoading = false; });
  }

  // ===================== Online Identity Verification Use Case =====================
  // Simulated journey. No real API calls; toggle reveals what each provider
  // would contribute behind the scenes.

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
    const body = $("uc-body");
    if (!body) return;
    body.innerHTML = `
      <div class="idv-wrap${IDV.reveal ? ' idv-reveal-on' : ''}">
        <div class="idv-toolbar">
          <div class="idv-stepper" id="idv-stepper"></div>
          <div class="idv-toolbar-right">
            <label class="idv-toggle">
              <input type="checkbox" id="idv-reveal-cb" ${IDV.reveal ? 'checked' : ''}>
              <span class="idv-toggle-track"><span class="idv-toggle-thumb"></span></span>
              <span class="idv-toggle-label">Reveal what's happening</span>
            </label>
          </div>
        </div>
        <div class="idv-split">
          <div class="idv-browser">
            <div class="idv-browser-chrome">
              <span class="idv-dot r"></span><span class="idv-dot y"></span><span class="idv-dot g"></span>
              <div class="idv-url">
                <span class="idv-lock">🔒</span>
                <span id="idv-url-text">www.medicare.gov</span>
              </div>
            </div>
            <div class="idv-page" id="idv-page"></div>
          </div>
          <aside class="idv-bts" id="idv-bts"></aside>
        </div>
      </div>
    `;
    idvRender();

    document.getElementById("idv-reveal-cb").addEventListener("change", (e) => {
      IDV.reveal = !!e.target.checked;
      const wrap = body.querySelector(".idv-wrap");
      if (wrap) wrap.classList.toggle("idv-reveal-on", IDV.reveal);
      // Sync reveal state inside modal if open
      const mw = document.querySelector('.idv-modal-wrap');
      if (mw) mw.classList.toggle('idv-reveal-on', IDV.reveal);
    });
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

  const SPECIALS = {
    eligible: "US",
    destination: "JP",
    product: "MWE",
    category: "",
    loading: false,
    error: null,
    data: null,        // { offers, benefits, programs, merchants, partial_errors }
    activeTab: "offers",
    _inited: false,
  };

  const SPECIALS_MARKETS = [
    { v: "US", label: "United States", flag: "🇺🇸" },
    { v: "GB", label: "United Kingdom", flag: "🇬🇧" },
    { v: "JP", label: "Japan",          flag: "🇯🇵" },
    { v: "SG", label: "Singapore",      flag: "🇸🇬" },
    { v: "HK", label: "Hong Kong",      flag: "🇭🇰" },
    { v: "AU", label: "Australia",      flag: "🇦🇺" },
    { v: "DE", label: "Germany",        flag: "🇩🇪" },
    { v: "FR", label: "France",         flag: "🇫🇷" },
    { v: "BR", label: "Brazil",         flag: "🇧🇷" },
    { v: "IN", label: "India",          flag: "🇮🇳" },
  ];

  const SPECIALS_PRODUCTS = [
    { v: "MST", label: "Standard",     accent: "#64748b" },
    { v: "MGD", label: "Gold",         accent: "#c8a24c" },
    { v: "MPL", label: "Platinum",     accent: "#94a3b8" },
    { v: "MWP", label: "World",        accent: "#1e293b" },
    { v: "MWE", label: "World Elite",  accent: "#000000" },
    { v: "MBC", label: "Business",     accent: "#0f766e" },
  ];

  const SPECIALS_CATEGORIES = [
    { v: "",              label: "All categories", icon: "✨" },
    { v: "Dining",        label: "Dining",        icon: "🍽️" },
    { v: "Shopping",      label: "Shopping",      icon: "🛍️" },
    { v: "Travel",        label: "Travel",        icon: "✈️" },
    { v: "Entertainment", label: "Entertainment", icon: "🎭" },
    { v: "Sports",        label: "Sports",        icon: "⚽" },
    { v: "Wellness",      label: "Wellness",      icon: "🧘" },
    { v: "Lifestyle",     label: "Lifestyle",     icon: "💎" },
  ];

  function specialsManifest() {
    return (USE_CASES || []).find(u => u.id === "specials");
  }

  function renderSpecials() {
    if (!SPECIALS._inited) {
      const m = specialsManifest();
      if (m && m.defaults) {
        SPECIALS.eligible    = m.defaults.eligible_markets || SPECIALS.eligible;
        SPECIALS.destination = m.defaults.destination_markets || SPECIALS.destination;
        SPECIALS.product     = m.defaults.mastercard_product || SPECIALS.product;
        SPECIALS.category    = m.defaults.category || "";
      }
      SPECIALS._inited = true;
    }
    specialsRender();
  }

  function specialsRender() {
    const body = $("uc-body");
    if (!body) return;
    body.innerHTML = `
      <div class="sp-wrap">
        ${specialsControlBarHtml()}
        <div class="sp-canvas">${specialsCanvasHtml()}</div>
      </div>`;
    specialsWire();
  }

  function specialsControlBarHtml() {
    const elig = SPECIALS_MARKETS.find(m => m.v === SPECIALS.eligible) || SPECIALS_MARKETS[0];
    const dest = SPECIALS_MARKETS.find(m => m.v === SPECIALS.destination) || SPECIALS_MARKETS[2];
    const prod = SPECIALS_PRODUCTS.find(p => p.v === SPECIALS.product) || SPECIALS_PRODUCTS[4];

    const marketOpts = (sel) => SPECIALS_MARKETS.map(m =>
      `<option value="${m.v}" ${m.v === sel ? "selected" : ""}>${m.flag} ${m.label}</option>`
    ).join("");

    const productOpts = SPECIALS_PRODUCTS.map(p =>
      `<option value="${p.v}" ${p.v === SPECIALS.product ? "selected" : ""}>${p.label}</option>`
    ).join("");

    return `
      <div class="sp-control">
        <div class="sp-control-left">
          <div class="sp-card-chip" style="--accent:${prod.accent}">
            <div class="sp-card-chip-brand">mastercard</div>
            <div class="sp-card-chip-emv"></div>
            <div class="sp-card-chip-tier">${escapeHtml(prod.label)}</div>
            <div class="sp-card-chip-circles">
              <span class="sp-cc sp-cc-red"></span>
              <span class="sp-cc sp-cc-yellow"></span>
            </div>
          </div>
        </div>
        <div class="sp-control-fields">
          <label class="sp-field">
            <span class="sp-field-label">Card</span>
            <select id="sp-product" class="sp-select">${productOpts}</select>
          </label>
          <label class="sp-field">
            <span class="sp-field-label">Issued in</span>
            <select id="sp-eligible" class="sp-select">${marketOpts(SPECIALS.eligible)}</select>
          </label>
          <div class="sp-arrow">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" style="width:18px;height:18px"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </div>
          <label class="sp-field">
            <span class="sp-field-label">Travelling to</span>
            <select id="sp-destination" class="sp-select">${marketOpts(SPECIALS.destination)}</select>
          </label>
          <button id="sp-go" class="sp-btn sp-btn-primary"${SPECIALS.loading ? " disabled" : ""}>
            ${SPECIALS.loading
              ? '<span class="sp-spinner"></span>Searching'
              : '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" style="width:14px;height:14px"><circle cx="9" cy="9" r="6"/><path d="M15 15l3 3" stroke-linecap="round"/></svg>Find perks'}
          </button>
        </div>
      </div>
      <div class="sp-catbar">
        ${SPECIALS_CATEGORIES.map(c => `
          <button class="sp-cat${SPECIALS.category === c.v ? " sp-cat-active" : ""}" data-cat="${escapeHtml(c.v)}">
            <span class="sp-cat-icon">${c.icon}</span>${escapeHtml(c.label)}
          </button>`).join("")}
      </div>
    `;
  }

  function specialsCanvasHtml() {
    if (SPECIALS.loading) {
      return `
        <div class="sp-loading">
          <div class="sp-loading-grid">
            ${Array.from({length: 6}).map(() => '<div class="sp-skel"></div>').join("")}
          </div>
        </div>`;
    }
    if (SPECIALS.error) {
      return `
        <div class="sp-empty sp-empty-error">
          <div class="sp-empty-icon">⚠️</div>
          <h3>Couldn't reach Priceless Specials</h3>
          <p>${escapeHtml(String(SPECIALS.error))}</p>
        </div>`;
    }
    if (!SPECIALS.data) {
      return specialsHeroHtml();
    }
    const d = SPECIALS.data;
    const counts = {
      offers:    (d.offers || []).length,
      benefits:  (d.benefits || []).length,
      programs:  (d.programs || []).length,
      merchants: (d.merchants || []).length,
    };
    const total = counts.offers + counts.benefits + counts.programs + counts.merchants;
    if (!total) {
      return `
        <div class="sp-empty">
          <div class="sp-empty-icon">🧭</div>
          <h3>No perks found for that combination</h3>
          <p>Try a different destination, card tier or category.</p>
        </div>`;
    }
    return `
      ${specialsSummaryHtml(counts)}
      ${specialsTabsHtml(counts)}
      <div class="sp-pane">${specialsPaneHtml()}</div>
    `;
  }

  function specialsSummaryHtml(counts) {
    const dest = SPECIALS_MARKETS.find(m => m.v === SPECIALS.destination) || {};
    return `
      <div class="sp-summary">
        <div class="sp-summary-head">
          <div class="sp-summary-title">
            <span class="sp-summary-flag">${dest.flag || ""}</span>
            <div>
              <div class="sp-summary-eyebrow">Perks waiting in</div>
              <div class="sp-summary-place">${escapeHtml(dest.label || SPECIALS.destination)}</div>
            </div>
          </div>
        </div>
        <div class="sp-stats">
          <div class="sp-stat">
            <div class="sp-stat-value">${counts.offers}</div>
            <div class="sp-stat-label">Offers</div>
          </div>
          <div class="sp-stat">
            <div class="sp-stat-value">${counts.benefits}</div>
            <div class="sp-stat-label">Card benefits</div>
          </div>
          <div class="sp-stat">
            <div class="sp-stat-value">${counts.programs}</div>
            <div class="sp-stat-label">Programs</div>
          </div>
          <div class="sp-stat">
            <div class="sp-stat-value">${counts.merchants}</div>
            <div class="sp-stat-label">Merchants</div>
          </div>
        </div>
      </div>`;
  }

  function specialsTabsHtml(counts) {
    const tabs = [
      { id: "offers",    label: "Offers",     count: counts.offers },
      { id: "benefits",  label: "Benefits",   count: counts.benefits },
      { id: "programs",  label: "Programs",   count: counts.programs },
      { id: "merchants", label: "Merchants",  count: counts.merchants },
    ];
    return `
      <div class="sp-tabs">
        ${tabs.map(t => `
          <button class="sp-tab${SPECIALS.activeTab === t.id ? " sp-tab-active" : ""}" data-tab="${t.id}"${t.count ? "" : " disabled"}>
            ${escapeHtml(t.label)}<span class="sp-tab-count">${t.count}</span>
          </button>`).join("")}
      </div>`;
  }

  function specialsPaneHtml() {
    const d = SPECIALS.data || {};
    if (SPECIALS.activeTab === "offers")    return specialsOffersHtml(d.offers || []);
    if (SPECIALS.activeTab === "benefits")  return specialsBenefitsHtml(d.benefits || []);
    if (SPECIALS.activeTab === "programs")  return specialsProgramsHtml(d.programs || []);
    if (SPECIALS.activeTab === "merchants") return specialsMerchantsHtml(d.merchants || []);
    return "";
  }

  function specialsOffersHtml(list) {
    if (!list.length) return '<div class="sp-empty-mini">No offers in this slice.</div>';
    return `<div class="sp-grid sp-grid-offers">${list.map(specialsOfferCard).join("")}</div>`;
  }

  function specialsOfferCard(o) {
    const initials = (o.merchantName || "?").trim().slice(0, 2).toUpperCase();
    const logo = o.merchantLogo
      ? `<img src="${escapeHtml(o.merchantLogo)}" alt="" class="sp-logo-img" loading="lazy" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'sp-logo-fb',textContent:'${escapeHtml(initials)}'}))">`
      : `<div class="sp-logo-fb">${escapeHtml(initials)}</div>`;
    const dates = [o.startDate && "From " + o.startDate, o.endDate && "Until " + o.endDate].filter(Boolean).join(" · ");
    return `
      <div class="sp-card sp-offer">
        <div class="sp-offer-head">
          <div class="sp-logo">${logo}</div>
          <div class="sp-offer-meta">
            <div class="sp-offer-merch">${escapeHtml(o.merchantName || "Merchant")}</div>
            ${o.category ? `<div class="sp-offer-cat">${escapeHtml(o.category)}</div>` : ""}
          </div>
          ${o.discount ? `<div class="sp-offer-discount">${escapeHtml(o.discount)}</div>` : ""}
        </div>
        <div class="sp-offer-title">${escapeHtml(o.title)}</div>
        ${o.description ? `<div class="sp-offer-desc">${escapeHtml(o.description)}</div>` : ""}
        ${dates ? `<div class="sp-offer-dates">${escapeHtml(dates)}</div>` : ""}
        <div class="sp-offer-foot">
          ${o.redemptionUrl
            ? `<a class="sp-btn sp-btn-primary sp-btn-sm" href="${escapeHtml(o.redemptionUrl)}" target="_blank" rel="noopener">Redeem<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" style="width:12px;height:12px"><path d="M7 13l6-6M9 7h4v4" stroke-linecap="round"/></svg></a>`
            : `<span class="sp-pill">Auto-applied</span>`}
          ${o.termsUrl ? `<a class="sp-link" href="${escapeHtml(o.termsUrl)}" target="_blank" rel="noopener">Terms</a>` : ""}
        </div>
      </div>`;
  }

  function specialsBenefitsHtml(list) {
    if (!list.length) return '<div class="sp-empty-mini">No card benefits available for this combination.</div>';
    return `<div class="sp-grid sp-grid-benefits">${list.map(specialsBenefitCard).join("")}</div>`;
  }

  function specialsBenefitCard(b) {
    return `
      <div class="sp-card sp-benefit">
        <div class="sp-benefit-icon">${b.icon ? `<img src="${escapeHtml(b.icon)}" alt="" onerror="this.replaceWith(Object.assign(document.createElement('span'),{textContent:'★'}))">` : "★"}</div>
        <div class="sp-benefit-body">
          <div class="sp-benefit-title">${escapeHtml(b.title)}</div>
          ${b.category ? `<div class="sp-benefit-cat">${escapeHtml(b.category)}</div>` : ""}
          ${b.description ? `<div class="sp-benefit-desc">${escapeHtml(b.description)}</div>` : ""}
          ${b.endDate ? `<div class="sp-benefit-foot">Valid until ${escapeHtml(b.endDate)}</div>` : ""}
        </div>
        ${b.url ? `<a class="sp-link sp-benefit-link" href="${escapeHtml(b.url)}" target="_blank" rel="noopener">Details →</a>` : ""}
      </div>`;
  }

  function specialsProgramsHtml(list) {
    if (!list.length) return '<div class="sp-empty-mini">No programs running for this market.</div>';
    return `<div class="sp-grid sp-grid-programs">${list.map(specialsProgramCard).join("")}</div>`;
  }

  function specialsProgramCard(p) {
    const hero = p.image
      ? `<div class="sp-program-hero" style="background-image:url('${encodeURI(p.image)}')"></div>`
      : `<div class="sp-program-hero sp-program-hero-blank">${escapeHtml((p.title || "P").slice(0,1).toUpperCase())}</div>`;
    return `
      <div class="sp-card sp-program">
        ${hero}
        <div class="sp-program-body">
          <div class="sp-program-title">${escapeHtml(p.title)}</div>
          ${p.description ? `<div class="sp-program-desc">${escapeHtml(p.description)}</div>` : ""}
          ${p.url ? `<a class="sp-link" href="${escapeHtml(p.url)}" target="_blank" rel="noopener">Explore →</a>` : ""}
        </div>
      </div>`;
  }

  function specialsMerchantsHtml(list) {
    if (!list.length) return '<div class="sp-empty-mini">No participating merchants found.</div>';
    return `<div class="sp-merch-grid">${list.map(specialsMerchantTile).join("")}</div>`;
  }

  function specialsMerchantTile(m) {
    const initials = (m.name || "?").trim().slice(0, 2).toUpperCase();
    const logo = m.logo
      ? `<img src="${escapeHtml(m.logo)}" alt="" loading="lazy" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'sp-merch-fb',textContent:'${escapeHtml(initials)}'}))">`
      : `<div class="sp-merch-fb">${escapeHtml(initials)}</div>`;
    return `
      <div class="sp-merch-tile" title="${escapeHtml(m.name)}">
        <div class="sp-merch-logo">${logo}</div>
        <div class="sp-merch-name">${escapeHtml(m.name)}</div>
        ${m.category ? `<div class="sp-merch-cat">${escapeHtml(m.category)}</div>` : ""}
      </div>`;
  }

  function specialsHeroHtml() {
    return `
      <div class="sp-hero">
        <div class="sp-hero-eyebrow">Priceless Specials</div>
        <h2 class="sp-hero-title">Where will your card<br/><span class="sp-grad-text">take you next?</span></h2>
        <p class="sp-hero-sub">Mastercard curates merchant offers, card-tier benefits and marketing programs for every market in its network. Pick your card and where you're heading — we'll surface the perks waiting at the other end.</p>
        <div class="sp-hero-chips">
          <span class="sp-hero-chip">🍽️ Dining</span>
          <span class="sp-hero-chip">✈️ Travel</span>
          <span class="sp-hero-chip">🛍️ Shopping</span>
          <span class="sp-hero-chip">🎭 Entertainment</span>
          <span class="sp-hero-chip">💎 Lifestyle</span>
        </div>
        <button id="sp-hero-go" class="sp-btn sp-btn-primary sp-btn-lg">
          Show me perks
          <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" style="width:14px;height:14px"><path d="M5 10h10M11 5l5 5-5 5" stroke-linecap="round"/></svg>
        </button>
      </div>`;
  }

  function specialsWire() {
    const sel = (id) => document.getElementById(id);
    const prod = sel("sp-product");      if (prod) prod.addEventListener("change", e => { SPECIALS.product = e.target.value; specialsRender(); });
    const elig = sel("sp-eligible");     if (elig) elig.addEventListener("change", e => { SPECIALS.eligible = e.target.value; specialsRender(); });
    const dest = sel("sp-destination");  if (dest) dest.addEventListener("change", e => { SPECIALS.destination = e.target.value; specialsRender(); });
    const go   = sel("sp-go");           if (go)   go.addEventListener("click", specialsSearch);
    const hgo  = sel("sp-hero-go");      if (hgo)  hgo.addEventListener("click", specialsSearch);

    document.querySelectorAll(".sp-cat").forEach(btn => {
      btn.addEventListener("click", () => {
        SPECIALS.category = btn.dataset.cat || "";
        if (SPECIALS.data) specialsSearch();
        else specialsRender();
      });
    });
    document.querySelectorAll(".sp-tab").forEach(btn => {
      btn.addEventListener("click", () => {
        if (btn.disabled) return;
        SPECIALS.activeTab = btn.dataset.tab;
        specialsRender();
      });
    });
  }

  function specialsSearch() {
    if (SPECIALS.loading) return;
    SPECIALS.loading = true;
    SPECIALS.error = null;
    SPECIALS.activeTab = "offers";
    specialsRender();

    fetch("/usecases/specials/action", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        action: "search",
        params: {
          eligible_markets:    SPECIALS.eligible,
          destination_markets: SPECIALS.destination,
          mastercard_product:  SPECIALS.product,
          category:            SPECIALS.category,
          language:            "en-US",
        },
      }),
    })
      .then(r => r.json())
      .then(d => {
        SPECIALS.loading = false;
        if (d.error) {
          SPECIALS.error = typeof d.error === "string" ? d.error : JSON.stringify(d.error);
          SPECIALS.data = null;
        } else {
          SPECIALS.data = d;
          // Pick the first non-empty tab.
          const order = ["offers", "benefits", "programs", "merchants"];
          SPECIALS.activeTab = order.find(t => (d[t] || []).length) || "offers";
        }
        specialsRender();
      })
      .catch(err => {
        SPECIALS.loading = false;
        SPECIALS.error = err.message || String(err);
        specialsRender();
      });
  }

  // ===================== Find A Card Use Case =====================

  // ===================== Sonic Branding Use Case =====================

  // Load the real Mastercard Sonic Web SDK (once)
  function _ensureMcSonicScript(cb) {
    // If already defined and ready, fire immediately
    if (customElements.get('mc-sonic')) { cb(); return; }
    // If script tag exists but not yet defined, wait
    if (document.querySelector('script[data-mc-sonic]')) {
      customElements.whenDefined('mc-sonic').then(cb);
      return;
    }
    const s = document.createElement('script');
    s.src = 'https://sonicsdk.mastercard.com/assets/js/latest/js/mc-sonic.min.js';
    s.setAttribute('data-mc-sonic', '1');
    s.onload = () => customElements.whenDefined('mc-sonic').then(cb);
    s.onerror = () => {
      const body = $('uc-body');
      if (body) body.innerHTML = '<div class="pl-error">Failed to load Mastercard Sonic SDK. Check your network connection and try again.</div>';
    };
    document.head.appendChild(s);
  }

  // Play mc-sonic reliably: element must already be in DOM, custom element must be defined
  function _playWhenReady(el) {
    customElements.whenDefined('mc-sonic').then(() => setTimeout(() => el.play(), 80));
  }

  // Launch the real mc-sonic component in a centred modal dialog
  window._sonicLaunch = function(cue, type, bg) {
    const modal = document.createElement('div');
    modal.className = 'sonic-modal-backdrop';
    modal.innerHTML =
      '<div class="sonic-modal">' +
        '<div class="sonic-modal-body"></div>' +
      '</div>';
    document.body.appendChild(modal);

    const dismiss = () => { if (modal.parentNode) modal.remove(); };

    const body = modal.querySelector('.sonic-modal-body');

    if (type === 'sound-only') {
      // Sound-only: compact modal with a playing indicator
      modal.querySelector('.sonic-modal').classList.add('sonic-modal--sound');
      body.innerHTML = '<div class="sonic-modal-playing"><span class="sonic-modal-note">🔊</span><span>Playing Mastercard Sonic…</span></div>';
      const audio = document.createElement('mc-sonic');
      audio.setAttribute('type', 'sound-only');
      audio.setAttribute('sonicCue', cue);
      audio.style.cssText = 'position:fixed;opacity:0;pointer-events:none;width:1px;height:1px;top:-9999px;';
      document.body.appendChild(audio);
      _playWhenReady(audio);
      const done = () => { audio.remove(); dismiss(); };
      audio.addEventListener('sonicCompletion', done, { once: true });
      setTimeout(done, 5000);
      return;
    }

    // Animated: mc-sonic needs explicit pixel dimensions to render its shadow DOM
    modal.querySelector('.sonic-modal').classList.add('sonic-modal--anim');
    const el = document.createElement('mc-sonic');
    el.setAttribute('type', type);
    el.setAttribute('sonicCue', cue);
    if (bg) el.setAttribute('sonicBackground', bg);
    el.style.cssText = 'display:block;width:100%;height:100%;';
    body.appendChild(el);
    _playWhenReady(el);
    el.addEventListener('sonicCompletion', dismiss, { once: true });
    setTimeout(dismiss, 3500);
  };

  const SONIC_CUES = [
    {
      id: 'checkout',
      label: 'Checkout',
      icon: '🛒',
      desc: 'Played at the moment a Mastercard payment is approved at checkout — online or in-store. This is the primary sonic signature.',
      contexts: ['Online checkout', 'POS terminal', 'Mobile wallet', 'In-app purchase'],
    },
    {
      id: 'securedby',
      label: 'Secured by Mastercard',
      icon: '🔒',
      desc: 'Played to reassure the cardholder that their transaction or session is protected by Mastercard security (e.g. 3DS, Identity Check).',
      contexts: ['3DS challenge', 'Identity verification', 'Fraud prevention', 'Passkey confirmation'],
    },
  ];

  const SONIC_TYPES = [
    { type: 'default', bg: 'black', label: 'Sound + Animation', sublabel: 'Dark background', icon: '🎵', btnClass: 'sonic-btn-dark' },
    { type: 'default', bg: 'white', label: 'Sound + Animation', sublabel: 'Light background', icon: '🎵', btnClass: 'sonic-btn-light' },
    { type: 'animation-only', bg: 'black', label: 'Animation Only', sublabel: 'Dark background', icon: '✨', btnClass: 'sonic-btn-dark' },
    { type: 'animation-only', bg: 'white', label: 'Animation Only', sublabel: 'Light background', icon: '✨', btnClass: 'sonic-btn-light' },
    { type: 'sound-only', bg: null, label: 'Sound Only', sublabel: 'No animation', icon: '🔊', btnClass: 'sonic-btn-sound' },
  ];

  const SONIC_RULES = [
    {
      heading: 'Always use',
      mod: 'always',
      items: [
        'Payment approved / accepted at checkout',
        'Mastercard Identity Check confirmation',
        'Successful 3DS authentication',
        'Any positive Mastercard-branded journey end-state',
      ],
    },
    {
      heading: 'Use carefully',
      mod: 'careful',
      items: [
        'Partner or merchant apps (written Mastercard approval required)',
        'Non-payment confirmations (consider Animation Only)',
        'Ambient / IoT environments where audio may be disruptive',
      ],
    },
    {
      heading: 'Never use',
      mod: 'never',
      items: [
        'Declined, failed, or error states',
        'Loading or processing states',
        'Competitor-branded or co-branded screens without approval',
        'Modified, remixed, or re-recorded versions',
      ],
    },
  ];

  function renderSonicBrand() {
    const body = $('uc-body');
    if (!body) return;

    body.innerHTML = `<div class="fac-loading"><div class="fac-spinner"></div><p>Loading Mastercard Sonic SDK…</p></div>`;

    _ensureMcSonicScript(() => {
      const cueCards = SONIC_CUES.map(cue => {
        const variantBtns = SONIC_TYPES.map(t => {
          const bgAttr = t.bg ? `, ${t.bg}` : '';
          return `
            <button class="sonic-variant-btn ${t.btnClass}"
              onclick="window._sonicLaunch('${cue.id}','${t.type}',${t.bg ? `'${t.bg}'` : 'null'})">
              <span class="sonic-vbtn-icon">${t.icon}</span>
              <span class="sonic-vbtn-text">
                <strong>${escapeHtml(t.label)}</strong>
                <span>${escapeHtml(t.sublabel)}</span>
              </span>
              <span class="sonic-vbtn-play">▶</span>
            </button>`;
        }).join('');

        return `
          <div class="sonic-cue-card">
            <div class="sonic-cue-header">
              <span class="sonic-cue-icon">${cue.icon}</span>
              <div>
                <h4 class="sonic-cue-label">${escapeHtml(cue.label)}</h4>
                <p class="sonic-cue-desc">${escapeHtml(cue.desc)}</p>
              </div>
            </div>
            <div class="sonic-cue-contexts">
              ${cue.contexts.map(c => `<span class="sonic-ctx-tag">${escapeHtml(c)}</span>`).join('')}
            </div>
            <div class="sonic-variants">${variantBtns}</div>
          </div>`;
      }).join('');

      const rulesHtml = SONIC_RULES.map(r => `
        <div class="sonic-rule sonic-rule--${r.mod}">
          <h5 class="sonic-rule-head">${escapeHtml(r.heading)}</h5>
          <ul class="sonic-rule-list">
            ${r.items.map(i => `<li>${escapeHtml(i)}</li>`).join('')}
          </ul>
        </div>`).join('');

      body.innerHTML = `
        <div class="sonic-ui">
          <div class="sonic-hero">
            <div class="sonic-hero-visual">
              <span class="sonic-hero-circles">
                <span class="sonic-hero-ring r1"></span>
                <span class="sonic-hero-ring r2"></span>
                <span class="sonic-hero-ring r3"></span>
                <span class="sonic-hero-mc"><span class="r"></span><span class="y"></span></span>
              </span>
            </div>
            <div class="sonic-hero-text">
              <p class="sonic-hero-eyebrow">Mastercard Web SDK</p>
              <h2 class="sonic-hero-title">Sonic Branding</h2>
              <p class="sonic-hero-sub">The real Mastercard sonic identity — two cues, three playback types, two backgrounds. Click any variant below to hear and see the authentic sound and animation.</p>
            </div>
          </div>

          <section class="sonic-section">
            <h3 class="sonic-section-title">Sound Cues &amp; Variants</h3>
            <p class="muted sonic-section-sub">Each button launches the real <code>mc-sonic</code> web component from the Mastercard Sonic Web SDK.</p>
            <div class="sonic-cue-grid">${cueCards}</div>
          </section>

          <section class="sonic-section">
            <h3 class="sonic-section-title">Interactive Demo — KICKS Checkout</h3>
            <p class="muted sonic-section-sub">The reference implementation. Select Mastercard (4444) as payment method and confirm the order to trigger the real acceptance sound and animation.</p>
            <div class="sonic-iframe-wrap">
              <iframe
                class="sonic-demo-frame"
                src="/static/sonic-app-web/index.html"
                title="Sonic Branding KICKS Demo"
                loading="lazy"
              ></iframe>
              <div class="sonic-demo-unavailable" style="display:none" id="sonic-demo-fallback">
                <span>🎵</span>
                <p>
                  Unable to load the embedded KICKS demo.
                  <a href="/static/sonic-app-web/index.html" target="_blank" rel="noopener">Open in a new tab ↗</a>
                </p>
              </div>
            </div>
          </section>

          <section class="sonic-section">
            <h3 class="sonic-section-title">Brand Guidelines</h3>
            <div class="sonic-rules">${rulesHtml}</div>
          </section>
        </div>
      `;

      const demoFrame = body.querySelector('.sonic-demo-frame');
      const demoFallback = body.querySelector('#sonic-demo-fallback');
      if (demoFrame && demoFallback) {
        demoFrame.addEventListener('error', () => {
          demoFrame.style.display = 'none';
          demoFallback.style.display = 'flex';
        });
      }
    });
  }

  function renderFindACard() {
    const body = $("uc-body");
    if (!body) return;
    body.innerHTML = `<div class="fac-loading"><div class="fac-spinner"></div><p>Checking service…</p></div>`;

    _nativeFetch("/usecases/findacard/health")
      .then(r => r.json())
      .then(({ online }) => {
        // Update the sidebar button with a coloured status dot
        const sidebarBtn = document.querySelector('[data-uc-id="findacard"]');
        if (sidebarBtn) {
          let dot = sidebarBtn.querySelector('.api-item-status');
          if (!dot) {
            dot = document.createElement('span');
            sidebarBtn.appendChild(dot);
          }
          dot.textContent = '●';
          dot.className = `api-item-status ${online ? 'ok' : 'err'}`;
          dot.title = online ? 'Running on port 5432' : 'Not running on port 5432';
        }

        if (online) {
          body.innerHTML = `
            <div class="fac-stage">
              <iframe class="fac-frame" src="http://localhost:5432" title="Find A Card" sandbox="allow-scripts allow-same-origin allow-forms allow-popups"></iframe>
            </div>`;
        } else {
          body.innerHTML = `
            <div class="fac-offline">
              <div class="fac-offline-icon">
                <svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5">
                  <circle cx="24" cy="24" r="18"/>
                  <path d="M24 14v12M24 34v1" stroke-linecap="round"/>
                </svg>
              </div>
              <h3>Service not running</h3>
              <p>Find A Card must be running locally on port 5432 for you to see this use case.</p>
              <button class="fac-retry-btn" id="fac-retry">Try again</button>
            </div>`;
          const retryBtn = document.getElementById('fac-retry');
          if (retryBtn) retryBtn.addEventListener('click', renderFindACard);
        }
      })
      .catch(() => {
        const body2 = $("uc-body");
        if (body2) body2.innerHTML = `<div class="fac-offline"><p>Could not reach health check endpoint.</p></div>`;
      });
  }

  function escapeHtml(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
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
    }

    function ucShowWorkbench() {
      if (aboutBtn)   aboutBtn.classList.remove('active');
      if (aboutPanel) aboutPanel.classList.add('hidden');
      if (workbench)  workbench.classList.remove('hidden');
      if (contentSec) contentSec.classList.remove('uc--about');
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
      // Close fullscreen overlay if open so #uc-body returns to normal position
      document.getElementById('uc-fullscreen-overlay')?.querySelector('.uc-fullscreen-reduce-btn')?.click();
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
    let _placeholder = null; // comment node that marks where uc-body lives

    function ucOpenFullscreen() {
      if (document.getElementById('uc-fullscreen-overlay')) return;
      const ucBody = document.getElementById('uc-body');
      if (!ucBody) return;

      // Mark the original position
      _placeholder = document.createComment('uc-body-placeholder');
      ucBody.parentNode.insertBefore(_placeholder, ucBody);

      // Build overlay
      const overlay = document.createElement('div');
      overlay.id = 'uc-fullscreen-overlay';
      overlay.className = 'uc-fullscreen-overlay';
      const titleText = (document.getElementById('uc-title') || {}).textContent || 'Use Case';
      overlay.innerHTML = `
        <div class="uc-fullscreen-topbar">
          <span class="uc-fullscreen-title">${escapeHtml(titleText)}</span>
          <button class="uc-fullscreen-reduce-btn">
            <svg width="14" height="14" viewBox="0 0 15 15" fill="none"><path d="M5 10L1 14M1 14h4M1 14v-4M10 5l4-4M14 4V1M14 1h-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
            Reduce
          </button>
        </div>
        <div class="uc-fullscreen-body" id="uc-fullscreen-body"></div>
      `;
      document.body.appendChild(overlay);
      overlay.querySelector('#uc-fullscreen-body').appendChild(ucBody);

      // Dismiss handlers
      const dismiss = ucCloseFullscreen;
      overlay.querySelector('.uc-fullscreen-reduce-btn').addEventListener('click', dismiss);
      _onKey = (e) => { if (e.key === 'Escape') dismiss(); };
      document.addEventListener('keydown', _onKey);
    }

    function ucCloseFullscreen() {
      const overlay = document.getElementById('uc-fullscreen-overlay');
      if (!overlay) return;
      const ucBody = document.getElementById('uc-body');
      if (ucBody && _placeholder && _placeholder.parentNode) {
        _placeholder.parentNode.insertBefore(ucBody, _placeholder);
        _placeholder.parentNode.removeChild(_placeholder);
      }
      overlay.remove();
      if (_onKey) { document.removeEventListener('keydown', _onKey); _onKey = null; }
    }

    popoutBtn.addEventListener('click', ucOpenFullscreen);
  })();

  // ---------------------------------------------------------------------
  // Init
  // ---------------------------------------------------------------------
  // Wire API Calls FAB and drawer
  const _fabBtn = $('api-calls-fab');
  if (_fabBtn) _fabBtn.addEventListener('click', () => { if (API_CALLS_VISIBLE) apiCallsClose(); else apiCallsOpen(); });
  const _acClose = $('api-calls-close');
  if (_acClose) _acClose.addEventListener('click', apiCallsClose);
  const _acClear = $('api-calls-clear');
  if (_acClear) _acClear.addEventListener('click', () => { API_CALL_LOG.length = 0; apiCallsRefresh(); });

  if (currentApiId) renderApi();
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

    let _groups = [];       // loaded config groups
    let _unlocked = false;  // edit mode flag
    let _pending = {};      // { KEY: newValue } for unsaved file uploads

    // ── Open / close ────────────────────────────────────────────────────────
    function cfgOpen() {
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

    triggerBtn && triggerBtn.addEventListener('click', cfgOpen);
    closeBtn && closeBtn.addEventListener('click', cfgClose);
    overlay && overlay.addEventListener('click', cfgClose);
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
      fetch('/config')
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

      const nameEl = document.createElement('span');
      const currentPath = _pending[f.key] !== undefined ? _pending[f.key] : f.value;
      nameEl.className = 'cfg-file-name' + (currentPath ? ' set' : '');
      nameEl.textContent = currentPath
        ? currentPath.split('/').pop().split('\\').pop()
        : 'No file set';
      wrap.appendChild(nameEl);

      if (_unlocked) {
        const fileInput = document.createElement('input');
        fileInput.type = 'file';
        fileInput.accept = '.p12,.pkcs12';
        fileInput.className = 'cfg-file-input';

        const uploadBtn = document.createElement('button');
        uploadBtn.className = 'cfg-upload-btn';
        uploadBtn.textContent = currentPath ? 'Replace' : 'Upload .p12';
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
                nameEl.textContent = data.filename;
                nameEl.className = 'cfg-file-name set';
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
    document.addEventListener('mousemove', function (e) {
      if (!tooltip.classList.contains('cfg-hidden')) cfgTooltipPos(e);
    });
    document.addEventListener('click', function () { cfgTooltipHide(); });

    function escHtml(s) {
      return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
    }
  }());

})();
