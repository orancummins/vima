// ===========================================================================
// Auto-Provision Modal
// ===========================================================================
(function () {
  'use strict';

  const RUNTIME_MODE = window.__RUNTIME_MODE__ || {};
  const SERVER_MODE = !!RUNTIME_MODE.server_mode;
  const NON_US_MODE = !!RUNTIME_MODE.non_us_mode;
  const SCRIPT_ROOT = (document.body?.dataset?.scriptRoot || '').replace(/\/$/, '');

  function _appPath(path) {
    if (typeof path !== 'string') return path;
    if (!path.startsWith('/')) return path;
    if (!SCRIPT_ROOT) return path;
    return `${SCRIPT_ROOT}${path}`;
  }

  let APIS = [];
  let legacyToId = {};
  let _catalogPromise = null;

  function _fallbackCatalogFromWindowApis() {
    // Prefer the full provision catalog embedded at page load time.
    if (Array.isArray(window.__PROVISION_CATALOG__) && window.__PROVISION_CATALOG__.length) {
      return window.__PROVISION_CATALOG__;
    }
    // Last-resort: reconstruct minimal entries from the API manifest list.
    const windowApis = Array.isArray(window.__APIS__) ? window.__APIS__ : [];
    return windowApis.map(function (a) {
      return {
        id: a.id,
        legacy_id: a.legacy_id,
        name: a.name,
        configured: a.configured || false,
        docs_url: a.docs_url || '',
        provision_note: '',
        requires_owner_approval: false,
        auto_provisionable: true,
        manual_onboarding_url: '',
        disabled_in_non_us: false,
        disabled_reason: '',
      };
    });
  }

  function _setCatalog(apis) {
    APIS = Array.isArray(apis) ? apis : [];
    legacyToId = {};
    APIS.forEach(function (a) {
      if (a && a.legacy_id) legacyToId[a.legacy_id] = a.id;
    });
  }

  function ensureCatalog() {
    if (_catalogPromise) return _catalogPromise;
    _catalogPromise = fetch('/provision/catalog', { cache: 'no-store' })
      .then(function (r) { return r.json(); })
      .then(function (data) {
        const apis = data && Array.isArray(data.apis) ? data.apis : [];
        if (!apis.length) throw new Error('Empty provisioning catalog');
        _setCatalog(apis);
        return APIS;
      })
      .catch(function () {
        _setCatalog(_fallbackCatalogFromWindowApis());
        return APIS;
      });
    return _catalogPromise;
  }

  const modal        = document.getElementById('prov-modal');
  const overlay      = document.getElementById('prov-overlay');
  const screenWelcome  = document.getElementById('prov-screen-welcome');
  const screenSelect   = document.getElementById('prov-screen-select');
  const screenProgress = document.getElementById('prov-screen-progress');
  const apiGrid      = document.getElementById('prov-api-grid');
  const selectAllCb  = document.getElementById('prov-select-all');
  const statusGrid   = document.getElementById('prov-status-grid');
  const logEl        = document.getElementById('prov-log');

  if (!modal) return;
  if (SERVER_MODE) {
    modal.classList.add('prov-hidden');
    return;
  }

  // ÔöÇÔöÇ Show/hide helpers ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
  function showScreen(screen) {
    [screenWelcome, screenSelect, screenProgress].forEach(function (s) {
      s && s.classList.add('prov-hidden');
    });
    screen && screen.classList.remove('prov-hidden');
  }

  function openModal() {
    modal.classList.remove('prov-hidden');
    document.body.style.overflow = 'hidden';
    showScreen(screenWelcome);
  }

  function closeModal() {
    modal.classList.add('prov-hidden');
    document.body.style.overflow = '';
  }

  // ÔöÇÔöÇ API selection grid ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
  function updateSelectAllState() {
    if (!selectAllCb || !apiGrid) return;
    var cbs = apiGrid.querySelectorAll('.prov-api-cb:not(:disabled)');
    if (!cbs.length) {
      selectAllCb.checked = false;
      selectAllCb.indeterminate = false;
      return;
    }
    var checked = Array.from(cbs).filter(function (cb) { return cb.checked; }).length;
    selectAllCb.checked = checked === cbs.length;
    selectAllCb.indeterminate = checked > 0 && checked < cbs.length;
  }

  function setAllApiSelections(checked) {
    if (!apiGrid) return;
    var cbs = apiGrid.querySelectorAll('.prov-api-cb:not(:disabled)');
    cbs.forEach(function (cb) { cb.checked = checked; });
    updateSelectAllState();
  }

  function _escAttr(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/"/g, '&quot;')
      .replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function buildApiGrid() {
    if (!apiGrid) return;
    apiGrid.innerHTML = '';
    var autoProvisionable = 0;
    var defaultChecked = 0;
    APIS.forEach(function (api) {
      var manual = api.auto_provisionable === false;
      var blockedNonUs = NON_US_MODE && api.disabled_in_non_us === true;
      var configured = api.configured === true;
      // Default-select only APIs that don't yet have keys provisioned.
      // Already-provisioned APIs render unchecked + green-tinted with a
      // tooltip, but remain selectable so users can re-provision them.
      var checked = !manual && !blockedNonUs && !configured;
      var note = manual ? '' : (api.provision_note || api.note || '');
      if (blockedNonUs) note = api.disabled_reason || NON_US_TOOLTIP;
      var label = document.createElement('label');
      var labelClass = 'prov-api-item';
      if (manual) labelClass += ' prov-api-item--manual';
      if (blockedNonUs) labelClass += ' prov-api-item--manual';
      if (configured && !manual) labelClass += ' prov-api-item--configured';
      label.className = labelClass;
      if (blockedNonUs) label.title = note;
      if (configured && !manual) label.title = 'Key already provisioned \u2014 select to re-provision';
      var cbAttrs = 'class="prov-api-cb" data-id="' + _escAttr(api.id) + '"' +
                    (manual || blockedNonUs ? ' disabled' : '') +
                    (checked ? ' checked' : '');
      var badges = '';
      if (manual) badges += '<span class="prov-api-badge">Manual onboarding</span>';
      if (blockedNonUs) badges += '<span class="prov-api-badge">Non-US mode</span>';
      var nameHtml = '<span class="prov-api-name">' +
                     '<span class="prov-api-name-text">' + _escAttr(api.name) + '</span>' +
                     badges +
                     '</span>';
      var noteHtml = '';
      if (note) {
        noteHtml = '<span class="prov-api-note">' + _escAttr(note) + '</span>';
      }
      var linkHtml = '';
      label.innerHTML =
        '<input type="checkbox" ' + cbAttrs + '>' +
        '<span class="prov-api-text">' + nameHtml + noteHtml + linkHtml + '</span>';
      apiGrid.appendChild(label);
      if (!manual && !blockedNonUs) autoProvisionable++;
      if (checked) defaultChecked++;
    });
    if (selectAllCb) {
      selectAllCb.checked = autoProvisionable > 0 && defaultChecked === autoProvisionable;
      selectAllCb.indeterminate = defaultChecked > 0 && defaultChecked < autoProvisionable;
    }
  }

  // ÔöÇÔöÇ Status grid (progress screen) ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
  var _apiStatus = {};  // id ÔåÆ 'pending' | 'running' | 'done' | 'failed'

  function buildStatusGrid(selectedIds) {
    if (!statusGrid) return;
    statusGrid.innerHTML = '';
    _apiStatus = {};
    selectedIds.forEach(function (id) {
      var api = APIS.find(function (a) { return a.id === id; }) || { id: id, name: id };
      _apiStatus[id] = 'pending';
      var card = document.createElement('div');
      card.className = 'prov-status-card prov-status-pending';
      card.id = 'prov-status-' + id;
      card.innerHTML =
        '<span class="prov-status-dot"></span>' +
        '<span class="prov-status-name">' + api.name + '</span>' +
        '<span class="prov-status-label">Pending</span>';
      statusGrid.appendChild(card);
    });
  }

  function setApiStatus(id, status) {
    _apiStatus[id] = status;
    var card = document.getElementById('prov-status-' + id);
    if (!card) return;
    card.className = 'prov-status-card prov-status-' + status;
    var labels = { pending: 'Pending', running: 'ProvisioningÔÇª', done: 'Done Ô£ô', failed: 'Failed Ô£ù' };
    var labelEl = card.querySelector('.prov-status-label');
    if (labelEl) labelEl.textContent = labels[status] || status;
  }

  // ÔöÇÔöÇ Log line parser ÔÇö extract per-API start events (best-effort) ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
  function resolveApiId(rawId) {
    // rawId may be a legacy id (e.g. 'binlookup') or canonical id (e.g. 'bin_lookup').
    return legacyToId[rawId] || rawId;
  }

  function parseLogLine(line) {
    // Mark cards as "running" when provisioning starts for an API.
    var mStart = line.match(/Provisioning '([\w_-]+)'/);
    if (mStart) {
      var id = resolveApiId(mStart[1]);
      if (_apiStatus[id] === 'pending') setApiStatus(id, 'running');
      return;
    }
    // Mark as "done" when the orchestrator logs a per-API success.
    var mDone = line.match(/Provisioned '([\w_-]+)'/);
    if (mDone) {
      setApiStatus(resolveApiId(mDone[1]), 'done');
      return;
    }
    // Mark as "failed" when the orchestrator logs a per-API failure.
    var mFail = line.match(/Failed to provision '([\w_-]+)'/);
    if (mFail) {
      setApiStatus(resolveApiId(mFail[1]), 'failed');
      return;
    }
  }

  // Fetch authoritative configured state for each selected API and update
  // its card accordingly. Called after provisioning finishes. Cards that
  // already have an authoritative log-derived status (done/failed) are left
  // alone ÔÇö only cards still showing pending/running are reconciled.
  function refreshCardStates(selectedIds) {
    return fetch('/provision/status', { cache: 'no-store' })
      .then(function (r) { return r.json(); })
      .catch(function () { return null; })
      .then(function (data) {
        if (!data || !Array.isArray(data.apis)) return;
        var byId = {};
        data.apis.forEach(function (a) { byId[a.id] = a; });
        selectedIds.forEach(function (id) {
          var current = _apiStatus[id];
          if (current === 'done' || current === 'failed') return;
          var entry = byId[id];
          if (entry && entry.configured) {
            setApiStatus(id, 'done');
          } else {
            setApiStatus(id, 'failed');
          }
        });
      });
  }

  // ÔöÇÔöÇ Log append ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
  function appendLog(text) {
    if (!logEl) return;
    var line = document.createElement('div');
    line.className = 'prov-log-line';
    var clean = text.replace(/^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+ \| \w+\s+\| [^-]+ - /, '');
    line.textContent = clean || text;
    logEl.appendChild(line);
    logEl.scrollTop = logEl.scrollHeight;
  }

  // ÔöÇÔöÇ Start provisioning ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
  function startProvisioning(selectedIds) {
    buildStatusGrid(selectedIds);
    showScreen(screenProgress);

    var body = { apis: selectedIds, password: 'foobar!!' };

    fetch('/provision/start', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    })
      .then(function (r) { return r.json(); })
      .then(function (data) {
        if (data.error) {
          onProvisionFailed(selectedIds, data.error);
          return;
        }
        streamJob(data.job_id, selectedIds);
      })
      .catch(function (err) { onProvisionFailed(selectedIds, String(err)); });
  }

  function streamJob(jobId, selectedIds) {
    var es = new EventSource(_appPath('/provision/stream/' + jobId));
    var _provDone = false;
    var _provFailed = false;
    var _provFailMessage = '';

    es.onmessage = function (e) {
      var raw = e.data;
      // Sentinels are sent unquoted; regular log lines are JSON-encoded strings
      if (raw === '__DONE__') {
        _provDone = true;
        es.close();
        if (_provFailed) onProvisionFailed(selectedIds, _provFailMessage);
        else onProvisionDone(selectedIds);
        return;
      }
      if (raw === '__IMPORT_COMPLETE__') { appendLog('Ô£à Keys imported ÔÇö Mastercard Solution Studio is ready!'); return; }
      if (raw.startsWith('__IMPORT_ERROR__')) {
        _provFailed = true;
        _provFailMessage = raw.replace('__IMPORT_ERROR__:', '').trim() || 'Could not import generated keys.';
        appendLog('ERROR: ' + _provFailMessage);
        return;
      }
      if (raw === '__NO_ZIP__') {
        _provFailed = true;
        _provFailMessage = 'Provisioning completed but no vima-config.zip was produced. Check the log above for errors, then import keys manually.';;
        appendLog('ERROR: ' + _provFailMessage);
        return;
      }
      if (raw.startsWith('__PROVISION_FAILED__:')) {
        _provFailed = true;
        _provFailMessage = raw.slice('__PROVISION_FAILED__:'.length) || 'Provisioning failed.';
        appendLog('ERROR: ' + _provFailMessage);
        return;
      }
      var line = raw;
      try { line = JSON.parse(raw); } catch (_) {}
      if (line) { parseLogLine(line); appendLog(line); }
    };
    es.onerror = function () {
      es.close();
      if (!_provDone) {
        // Connection dropped before __DONE__ reached the browser ÔÇö still refresh
        // card states from the server so cards don't stay stuck orange.
        if (_provFailed) onProvisionFailed(selectedIds, _provFailMessage);
        else onProvisionDone(selectedIds);
      }
    };
  }

  function onProvisionFailed(selectedIds, message) {
    (selectedIds || []).forEach(function (id) { setApiStatus(id, 'failed'); });
    var titleEl = document.getElementById('prov-progress-title');
    var subtitleEl = document.getElementById('prov-progress-subtitle');
    var activationNote = document.getElementById('prov-activation-note');
    var footer = document.getElementById('prov-progress-footer');
    var reloadBtn = document.getElementById('prov-btn-reload');
    var msg = message || 'Provisioning failed. Check the log below and try again.';
    if (titleEl) titleEl.textContent = 'Provisioning Failed';
    if (subtitleEl) subtitleEl.textContent = msg;
    if (activationNote) activationNote.style.display = 'none';
    if (reloadBtn) reloadBtn.textContent = 'Reload & Try Again';
    if (footer) footer.style.display = '';
    appendLog('');
    appendLog('Provisioning failed. ' + msg);
  }

  function onProvisionDone(selectedIds) {
    // Refresh card states from authoritative server status before showing
    // the "Provisioning Complete!" UI.
    refreshCardStates(selectedIds || []).then(function () {
      var titleEl = document.getElementById('prov-progress-title');
      var subtitleEl = document.getElementById('prov-progress-subtitle');
      var activationNote = document.getElementById('prov-activation-note');
      var footer = document.getElementById('prov-progress-footer');
      if (titleEl) titleEl.textContent = 'Provisioning Complete!';
      if (subtitleEl) subtitleEl.textContent = 'Your API keys have been provisioned and imported into Mastercard Solution Studio.';
      if (activationNote) activationNote.style.display = '';
      if (footer) footer.style.display = '';
      appendLog('');
      appendLog('­ƒÄë Done! Click below to reload and start exploring.');
    });
  }

  // ÔöÇÔöÇ Wire up buttons ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
  var btnAuto   = document.getElementById('prov-btn-auto');
  var btnManual = document.getElementById('prov-btn-manual');
  var btnSkip   = document.getElementById('prov-btn-skip');
  var btnBack   = document.getElementById('prov-back-select');
  var btnStart  = document.getElementById('prov-btn-start');
  var btnReload = document.getElementById('prov-btn-reload');

  btnAuto && btnAuto.addEventListener('click', function () {
    ensureCatalog().then(function () {
      buildApiGrid();
      showScreen(screenSelect);
    });
  });

  // Triggered by "Yes, Generate New Keys" in the config modal
  document.addEventListener('prov:open-select', function () {
    modal.classList.remove('prov-hidden');
    document.body.style.overflow = 'hidden';
    ensureCatalog().then(function () {
      buildApiGrid();
      showScreen(screenSelect);
    });
  });

  btnManual && btnManual.addEventListener('click', function () {
    closeModal();
    var cfgTrigger = document.getElementById('cfg-trigger-btn');
    if (cfgTrigger) cfgTrigger.click();
  });

  btnSkip && btnSkip.addEventListener('click', closeModal);
  overlay && overlay.addEventListener('click', function () {
    if (!screenProgress.classList.contains('prov-hidden')) return;
    closeModal();
  });

  btnBack && btnBack.addEventListener('click', function () { showScreen(screenWelcome); });

  selectAllCb && selectAllCb.addEventListener('change', function () {
    setAllApiSelections(!!selectAllCb.checked);
  });

  apiGrid && apiGrid.addEventListener('change', function (e) {
    var target = e.target;
    if (target && target.classList && target.classList.contains('prov-api-cb')) {
      updateSelectAllState();
    }
  });

  btnStart && btnStart.addEventListener('click', function () {
    var cbs = apiGrid ? apiGrid.querySelectorAll('.prov-api-cb:checked') : [];
    var selectedIds = Array.from(cbs).map(function (cb) { return cb.dataset.id; });
    if (selectedIds.length === 0) { alert('Please select at least one API.'); return; }
    startProvisioning(selectedIds);
  });

  btnReload && btnReload.addEventListener('click', function () { location.reload(); });

  // ÔöÇÔöÇ Auto-show on load if setup is needed ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
  ensureCatalog();

  fetch('/provision/status')
    .then(function (r) { return r.json(); })
    .then(function (data) {
      if (data.needs_setup) openModal();
    })
    .catch(function () { /* ignore ÔÇö don't block app */ });

})();
