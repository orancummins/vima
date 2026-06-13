// ===========================================================================
// API Calls Logger - polls /api-call-log for outbound Mastercard calls
// ===========================================================================
import { $ } from '../core/dom.js';
import { _nativeFetch } from '../core/net.js';
import { escapeHtml } from '../core/html.js';

  let API_CALLS_VISIBLE = false;
  const API_CALL_LOG = [];
  let _lastSeq = 0;
  let _pollTimer = null;

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
          <span class="api-calls-status api-calls-status--${statusCls}">${e.status == null ? 'Ã¢â‚¬Â¦' : escapeHtml(String(e.status))}</span>
          <span class="api-calls-time">${escapeHtml(elapsed || time)}</span>
          <span class="api-calls-chevron">Ã¢â€“Â¾</span>
        </div>
        <div class="api-calls-entry-body">
          ${e.requestBody != null ? `<div class="api-calls-section"><div class="api-calls-section-label">Request body</div><pre class="api-calls-pre">${escapeHtml(JSON.stringify(e.requestBody, null, 2))}</pre></div>` : ''}
          <div class="api-calls-section">
            <div class="api-calls-section-label">Response${e.status ? ' Ã‚Â· ' + e.status : ''}</div>
            ${e.responseBody !== null && e.responseBody !== undefined
              ? `<pre class="api-calls-pre">${escapeHtml(JSON.stringify(e.responseBody, null, 2))}</pre>`
              : `<p class="api-calls-pending">Waiting for responseÃ¢â‚¬Â¦</p>`}
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

function apiCallsToggle() {
  if (API_CALLS_VISIBLE) apiCallsClose();
  else apiCallsOpen();
}

function apiCallsClear() {
  API_CALL_LOG.length = 0;
  apiCallsRefresh();
}

export {
  apiCallsOpen, apiCallsClose, apiCallsToggle, apiCallsClear,
  _startPolling, _stopPolling,
};
