// -------------------------------------------------------------------
// features/devProjects.js
// "Developer Projects" manager, opened from the API Configuration modal.
// Loads all Mastercard Developer projects (fetched + cached server-side in a
// background thread), lets the user filter and multi-select projects that are
// NOT in use and have NO production keys, and deletes them via a background
// job with live progress. Production and in-use projects are never selectable.
// -------------------------------------------------------------------
import { _nativeFetch } from '../core/net.js';
import { escapeHtml } from '../core/html.js';

let _projects = [];
const _selected = new Set();
let _loadPoll = null;
let _jobPoll = null;
let _deleting = false;

const $ = (id) => document.getElementById(id);

export function initDevProjects() {
  const openBtn = $('cfg-projects-btn');
  const modal = $('devprojects-modal');
  if (!openBtn || !modal || modal._wired) return;
  modal._wired = true;

  openBtn.addEventListener('click', open);
  $('dp-close-btn') && $('dp-close-btn').addEventListener('click', close);
  $('devprojects-overlay') && $('devprojects-overlay').addEventListener('click', close);
  $('dp-refresh-btn') && $('dp-refresh-btn').addEventListener('click', refresh);
  $('dp-search') && $('dp-search').addEventListener('input', render);
  $('dp-only-deletable') && $('dp-only-deletable').addEventListener('change', render);
  $('dp-select-all') && $('dp-select-all').addEventListener('change', onSelectAll);
  $('dp-delete-btn') && $('dp-delete-btn').addEventListener('click', onDelete);
}

function open() {
  const modal = $('devprojects-modal');
  if (!modal) return;
  modal.classList.remove('cfg-hidden');
  document.body.style.overflow = 'hidden';
  _selected.clear();
  _deleting = false;
  clearTimeout(_jobPoll); _jobPoll = null;
  const prog = $('dp-progress'); if (prog) prog.hidden = true;
  load();
}

function close() {
  const modal = $('devprojects-modal');
  if (!modal) return;
  modal.classList.add('cfg-hidden');
  if (!$('cfg-modal') || $('cfg-modal').classList.contains('cfg-hidden')) {
    document.body.style.overflow = '';
  }
  clearTimeout(_loadPoll); _loadPoll = null;
  clearTimeout(_jobPoll); _jobPoll = null;
}

function setBody(html) { const b = $('dp-body'); if (b) b.innerHTML = html; }

// Stable indeterminate loading indicator. Only (re)rendered when we aren't
// already showing it, so polling doesn't cause the label to flash.
function showLoading(label) {
  const b = $('dp-body');
  if (!b) return;
  if (b.querySelector('.dp-loading-track')) {
    const lbl = b.querySelector('.dp-loading-label');
    if (lbl && label) lbl.textContent = label;
    return;
  }
  b.innerHTML = '<div class="dp-loading"><div class="dp-loading-label">' +
    escapeHtml(label || 'Loading\u2026') + '</div><div class="dp-loading-track"></div></div>';
}

function load() {
  showLoading('Loading your projects from Mastercard\u2026');
  _nativeFetch('/developer-projects', { cache: 'no-store' })
    .then((r) => r.json())
    .then((d) => {
      if (d.status === 'unconfigured') {
        setBody('<div class="dp-empty">A Mastercard Developers admin key isn’t configured, so project management is unavailable.<br>Add <code>MCD_DEVELOPERS_API_*</code> to <code>config/.env</code> to enable it.</div>');
        return;
      }
      if (d.status === 'error') {
        setBody('<div class="dp-empty">Error loading projects: ' + escapeHtml(String(d.error || '')) + '</div>');
        return;
      }
      if (d.status === 'loading') {
        showLoading('Loading your projects from Mastercard\u2026 (first load can take a few seconds)');
        _loadPoll = setTimeout(load, 1200);
        return;
      }
      _projects = Array.isArray(d.projects) ? d.projects : [];
      // Drop selections that are no longer present/deletable.
      Array.from(_selected).forEach((id) => {
        const p = _projects.find((x) => x.id === id);
        if (!p || !p.deletable) _selected.delete(id);
      });
      render();
    })
    .catch(() => setBody('<div class="dp-empty">Couldn’t load projects.</div>'));
}

function refresh() {
  showLoading('Refreshing\u2026');
  _nativeFetch('/developer-projects/refresh', { method: 'POST' })
    .then(() => { _loadPoll = setTimeout(load, 600); })
    .catch(() => load());
}

function _filtered() {
  const q = ($('dp-search') && $('dp-search').value || '').trim().toLowerCase();
  const onlyDel = $('dp-only-deletable') && $('dp-only-deletable').checked;
  return _projects.filter((p) => {
    if (onlyDel && !p.deletable) return false;
    if (!q) return true;
    const hay = (p.name + ' ' + p.type + ' ' + p.id + ' ' + (p.services || []).join(' ') + ' ' + (p.region || '')).toLowerCase();
    return hay.indexOf(q) !== -1;
  });
}

function render() {
  const rows = _filtered();
  const total = _projects.length;
  const delCount = _projects.filter((p) => p.deletable).length;
  const inUse = _projects.filter((p) => p.in_use).length;
  const prod = _projects.filter((p) => p.has_production).length;
  const sum = $('dp-summary');
  if (sum) sum.textContent = `${total} projects · ${delCount} deletable · ${inUse} in use · ${prod} production`;

  if (!rows.length) {
    setBody('<div class="dp-empty">No projects match.</div>');
  } else {
    setBody('<div class="dp-list">' + rows.map(_row).join('') + '</div>');
    const body = $('dp-body');
    body.querySelectorAll('input[type=checkbox][data-pid]').forEach((cb) => {
      cb.addEventListener('change', () => {
        if (cb.checked) _selected.add(cb.getAttribute('data-pid'));
        else _selected.delete(cb.getAttribute('data-pid'));
        _syncDeleteBtn();
      });
    });
  }
  _syncDeleteBtn();
}

function _row(p) {
  const checked = _selected.has(p.id) ? ' checked' : '';
  const cb = p.deletable
    ? `<input type="checkbox" data-pid="${escapeHtml(p.id)}"${checked}>`
    : `<span class="dp-lock" title="${escapeHtml(p.reason || 'protected')}">🔒</span>`;
  const badges = [];
  if (p.in_use) badges.push('<span class="dp-badge dp-badge--inuse">In use</span>');
  if (p.has_production) badges.push('<span class="dp-badge dp-badge--prod">Production</span>');
  if (!p.has_production && p.sandbox_creds > 0) badges.push('<span class="dp-badge dp-badge--sbx">Sandbox</span>');
  if (p.region) badges.push('<span class="dp-tag">' + escapeHtml(p.region) + '</span>');
  const svc = (p.services || []).join(', ');
  return `<label class="dp-row${p.deletable ? '' : ' dp-row--locked'}">
    <span class="dp-row-cb">${cb}</span>
    <span class="dp-row-main">
      <span class="dp-row-name">${escapeHtml(p.name || '(unnamed)')} ${badges.join(' ')}</span>
      <span class="dp-row-meta">${escapeHtml(p.type || '')}${svc ? ' · ' + escapeHtml(svc.slice(0, 90)) : ''}</span>
      <span class="dp-row-id">${escapeHtml(p.id)}${p.cred ? ' · <code>' + escapeHtml(p.cred) + '</code>' : ''}</span>
    </span>
  </label>`;
}

function onSelectAll(e) {
  const on = e.target.checked;
  _filtered().forEach((p) => {
    if (p.deletable) { if (on) _selected.add(p.id); else _selected.delete(p.id); }
  });
  render();
}

function _syncDeleteBtn() {
  const btn = $('dp-delete-btn');
  if (!btn) return;
  const n = _selected.size;
  btn.disabled = n === 0 || _deleting;
  btn.textContent = n > 0 ? `Delete selected (${n})` : 'Delete selected';
}

function onDelete() {
  if (_deleting) return;
  const ids = Array.from(_selected);
  if (!ids.length) return;
  if (!window.confirm(`Delete ${ids.length} project(s)?\n\nThis permanently removes them from Mastercard Developers and revokes their sandbox keys. This cannot be undone.`)) return;
  _deleting = true;
  _syncDeleteBtn();
  const prog = $('dp-progress'); if (prog) prog.hidden = false;
  _setProgress(0, ids.length, 'Starting…');
  _nativeFetch('/developer-projects/delete', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ ids }),
  })
    .then((r) => r.json())
    .then((d) => {
      if (d.error || !d.job_id) {
        _deleting = false; _syncDeleteBtn();
        window.alert('Delete could not start: ' + (d.error || 'unknown'));
        return;
      }
      _pollJob(d.job_id, d.total || ids.length);
    })
    .catch(() => { _deleting = false; _syncDeleteBtn(); window.alert('Delete failed to start.'); });
}

function _pollJob(jobId, total) {
  _nativeFetch('/developer-projects/delete/' + encodeURIComponent(jobId), { cache: 'no-store' })
    .then((r) => r.json())
    .then((j) => {
      const tot = j.total || total;
      const done = j.done || 0;
      const failed = (j.results || []).filter((x) => !x.ok).length;
      const okN = done - failed;
      const cur = j.current ? ` · deleting “${j.current}”` : '';
      _setProgress(done, tot, `Deleted ${okN}/${tot}${failed ? ` · ${failed} failed` : ''}${(j.status !== 'done' && j.current) ? cur : ''}`);

      // Finalize when the server says done, OR defensively if every project has
      // been processed (so a lagging status flag never leaves us "stuck").
      if (j.status === 'done' || done >= tot) {
        _deleting = false;
        _selected.clear();
        _finishJob(j, tot, okN, failed);
        return;
      }
      _jobPoll = setTimeout(() => _pollJob(jobId, total), 900);
    })
    .catch(() => { _jobPoll = setTimeout(() => _pollJob(jobId, total), 1500); });
}

function _finishJob(j, tot, okN, failed) {
  _setProgress(tot, tot, `Done — deleted ${okN}${failed ? `, ${failed} failed` : ''}.`);
  const fails = (j.results || []).filter((x) => !x.ok);
  const body = $('dp-body');
  if (fails.length && body) {
    // Surface WHY each failed so the user can act on it.
    const items = fails.map((x) =>
      `<div>• <strong>${escapeHtml(x.name || x.id)}</strong> — ${escapeHtml(x.error || 'failed')}</div>`
    ).join('');
    const banner = document.createElement('div');
    banner.className = 'dp-fail-summary';
    banner.innerHTML = `<div>${fails.length} project(s) could not be deleted:</div>${items}`;
    body.prepend(banner);
  }
  // Reload the list; on success (no failures) also tidy the progress bar away.
  setTimeout(() => {
    if (!failed) { const p = $('dp-progress'); if (p) p.hidden = true; }
    load();
  }, failed ? 400 : 1200);
}

function _setProgress(done, total, text) {
  const fill = $('dp-progress-fill');
  const txt = $('dp-progress-text');
  const pct = total ? Math.round((done / total) * 100) : 0;
  if (fill) fill.style.width = pct + '%';
  if (txt) txt.textContent = text;
}
