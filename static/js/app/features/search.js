// features/search.js
// Global command-palette search. Triggered by ⌘K / Ctrl+K or the search button.
// Searches APIs, operations, use cases, and bundles entirely client-side.

import { APIS, USE_CASES } from '../core/env.js';
import { getBundlesCache } from '../core/catalog.js';
import { escapeHtml } from '../core/html.js';
import { selectOp } from '../workbench/core.js';

// ---------------------------------------------------------------------------
// Index building
// ---------------------------------------------------------------------------

function _stripHtml(str) {
  return (str || '').replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim();
}

function _buildIndex() {
  const entries = [];

  for (const api of (APIS || [])) {
    const howToText = _stripHtml(api.how_to);
    const apiText = [
      api.name,
      api.description || '',
      api.group || '',
      (api.categories || []).join(' '),
      howToText,
    ].join(' ').toLowerCase();

    entries.push({
      type: 'api',
      label: api.name,
      sub: api.group || '',
      id: api.id,
      configured: !!api.configured,
      searchText: apiText,
      action() { _navigateToApi(api.id); },
    });

    for (const op of (api.operations || [])) {
      const opText = [op.name, op.description || '', op.category || '', api.name].join(' ').toLowerCase();
      entries.push({
        type: 'operation',
        label: op.name,
        sub: api.name,
        id: api.id,
        opId: op.id,
        configured: !!api.configured,
        searchText: opText,
        action() { _navigateToApi(api.id, op.id); },
      });
    }
  }

  for (const uc of (USE_CASES || [])) {
    const ucText = [uc.name, uc.description || '', (uc.apis || []).join(' ')].join(' ').toLowerCase();
    entries.push({
      type: 'usecase',
      label: uc.name,
      sub: uc.description || '',
      id: uc.id,
      searchText: ucText,
      action() { _navigateToUseCase(uc.id); },
    });
  }

  // Static SDK entries
  entries.push({
    type: 'sdk',
    label: 'Global Open Finance',
    sub: 'One SDK across the US, Australia and Europe',
    id: 'global_open_finance',
    searchText: 'global open finance sdk ofin finicity australia europe us united states cli command line',
    action() { _navigateToSdk('global_open_finance'); },
  });

  for (const bundle of (window.__BUNDLES__ || getBundlesCache() || [])) {
    const apiNames = (bundle.apis || []).map(a => (typeof a === 'string' ? a : a.name) || '').join(' ');
    const bText = [bundle.name, bundle.tagline || '', bundle.description || '', apiNames].join(' ').toLowerCase();
    entries.push({
      type: 'bundle',
      label: bundle.name,
      sub: bundle.tagline || bundle.description || '',
      id: bundle.id,
      searchText: bText,
      action() { _navigateToBundle(bundle.id); },
    });
  }

  return entries;
}

// ---------------------------------------------------------------------------
// Navigation
// ---------------------------------------------------------------------------

function _navigateToApi(apiId, opId) {
  const tabBtn = document.querySelector('.top-tab[data-top-tab="apis"]');
  if (tabBtn) tabBtn.click();
  setTimeout(() => {
    const apiBtn = document.querySelector(`[data-api-id="${CSS.escape(apiId)}"]`);
    if (apiBtn) {
      apiBtn.click();
      if (opId) setTimeout(() => selectOp(opId), 40);
    }
  }, 0);
}

function _navigateToUseCase(ucId) {
  const tabBtn = document.querySelector('.top-tab[data-top-tab="usecases"]');
  if (tabBtn) tabBtn.click();
  setTimeout(() => {
    const ucBtn = document.querySelector(`[data-uc-id="${CSS.escape(ucId)}"]`);
    if (ucBtn) ucBtn.click();
  }, 0);
}

function _navigateToBundle(bundleId) {
  const tabBtn = document.querySelector('.top-tab[data-top-tab="bundles"]');
  if (tabBtn) tabBtn.click();
  setTimeout(() => {
    const bundleBtn = document.querySelector(`[data-bundle-id="${CSS.escape(bundleId)}"]`);
    if (bundleBtn) bundleBtn.click();
  }, 0);
}

function _navigateToSdk(sdkId) {
  const tabBtn = document.querySelector('.top-tab[data-top-tab="bundles"]');
  if (tabBtn) tabBtn.click();
  setTimeout(() => {
    const sdkBtn = document.querySelector(`[data-sdk-id="${CSS.escape(sdkId)}"]`);
    if (sdkBtn) sdkBtn.click();
  }, 0);
}

// ---------------------------------------------------------------------------
// Search scoring
// ---------------------------------------------------------------------------

function _score(entry, tokens) {
  let total = 0;
  const nameLower = entry.label.toLowerCase();
  for (const token of tokens) {
    let s = 0;
    if (nameLower === token)              s = 5;
    else if (nameLower.startsWith(token)) s = 4;
    else if (nameLower.includes(token))   s = 2;
    else if (entry.searchText.includes(token)) s = 1;
    if (s === 0) return -1; // all tokens must match
    total += s;
  }
  return total;
}

const _TYPE_PRIORITY = { api: 0, usecase: 1, bundle: 2, sdk: 2, operation: 3 };

function _search(query, index) {
  if (!query) return [];
  const tokens = query.toLowerCase().split(/\s+/).filter(Boolean);
  if (!tokens.length) return [];

  const scored = [];
  for (const entry of index) {
    const s = _score(entry, tokens);
    if (s >= 0) scored.push({ entry, score: s });
  }

  scored.sort((a, b) => {
    if (b.score !== a.score) return b.score - a.score;
    return (_TYPE_PRIORITY[a.entry.type] ?? 4) - (_TYPE_PRIORITY[b.entry.type] ?? 4);
  });

  // Cap results: up to 20 total, max 6 operations
  const result = [];
  let opCount = 0;
  for (const { entry } of scored) {
    if (entry.type === 'operation') {
      if (++opCount > 6) continue;
    }
    result.push(entry);
    if (result.length >= 20) break;
  }
  return result;
}

// ---------------------------------------------------------------------------
// Rendering
// ---------------------------------------------------------------------------

const _TYPE_LABEL      = { api: 'API', operation: 'Operation', usecase: 'Use Case', bundle: 'Bundle', sdk: 'SDK' };
const _TYPE_GROUP      = { api: 'APIs', operation: 'Operations', usecase: 'Use Cases', bundle: 'Bundles', sdk: 'SDKs' };
const _TYPE_ORDER      = ['api', 'usecase', 'bundle', 'sdk', 'operation'];

function _renderResults(results, matches, onSelect) {
  const entries = [];

  if (!matches.length) {
    results.innerHTML = '<div class="search-empty">No results</div>';
    return entries;
  }

  // Group while preserving relative score order within each group
  const grouped = {};
  for (const entry of matches) {
    if (!grouped[entry.type]) grouped[entry.type] = [];
    grouped[entry.type].push(entry);
  }

  let html = '';
  for (const type of _TYPE_ORDER) {
    if (!grouped[type]) continue;
    html += `<div class="search-group-header">${_TYPE_GROUP[type]}</div>`;
    for (const entry of grouped[type]) {
      entries.push(entry);
      const dot = (entry.type === 'api' || entry.type === 'operation')
        ? `<span class="search-result-dot ${entry.configured ? 'ok' : 'off'}"></span>`
        : '';
      html += `<button class="search-result-item" type="button">
        <div class="search-result-main">
          ${dot}<span class="search-result-label">${escapeHtml(entry.label)}</span>
          ${entry.sub ? `<span class="search-result-sub">${escapeHtml(entry.sub)}</span>` : ''}
        </div>
        <span class="search-result-type search-result-type--${entry.type}">${_TYPE_LABEL[entry.type]}</span>
      </button>`;
    }
  }

  results.innerHTML = html;

  const items = results.querySelectorAll('.search-result-item');
  items.forEach((el, i) => {
    el.addEventListener('mouseenter', () => onSelect(i, false));
    el.addEventListener('click', () => {
      const action = entries[i] && entries[i].action;
      if (action) action();
    });
  });

  return entries;
}

// ---------------------------------------------------------------------------
// Public init
// ---------------------------------------------------------------------------

export function initSearch() {
  const backdrop = document.getElementById('search-backdrop');
  const input    = document.getElementById('search-input');
  const results  = document.getElementById('search-results');
  if (!backdrop || !input || !results) return;

  let _index     = null;
  let _activeIdx = -1;
  let _entries   = [];    // flat list matching rendered item order

  function _getIndex() {
    if (!_index) _index = _buildIndex();
    return _index;
  }

  function _getItems() {
    return results.querySelectorAll('.search-result-item');
  }

  function _setActive(idx, scroll) {
    _activeIdx = idx;
    const items = _getItems();
    items.forEach((el, i) => el.classList.toggle('search-result-item--active', i === _activeIdx));
    if (scroll && _activeIdx >= 0 && items[_activeIdx]) {
      items[_activeIdx].scrollIntoView({ block: 'nearest' });
    }
  }

  function _open() {
    backdrop.classList.add('search-backdrop--open');
    input.value = '';
    results.innerHTML = '';
    _activeIdx = -1;
    _entries = [];
    input.focus();
  }

  function _close() {
    backdrop.classList.remove('search-backdrop--open');
  }

  function _runSearch() {
    _activeIdx = -1;
    _entries = _renderResults(results, _search(input.value.trim(), _getIndex()), (i, scroll) => _setActive(i, scroll));
    // Patch close into every rendered click handler so the palette dismisses
    results.querySelectorAll('.search-result-item').forEach((el, i) => {
      el.addEventListener('click', _close);
    });
  }

  // ── Trigger: header button ──
  const triggerBtn = document.getElementById('search-trigger-btn');
  if (triggerBtn) triggerBtn.addEventListener('click', _open);

  // ── Trigger: ⌘K / Ctrl+K ──
  document.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      if (!backdrop.classList.contains('search-backdrop--open')) _open(); else _close();
      return;
    }
    if (!backdrop.classList.contains('search-backdrop--open')) return;
    switch (e.key) {
      case 'Escape':
        _close();
        break;
      case 'ArrowDown': {
        e.preventDefault();
        const items = _getItems();
        _setActive(Math.min(_activeIdx + 1, items.length - 1), true);
        break;
      }
      case 'ArrowUp': {
        e.preventDefault();
        _setActive(Math.max(_activeIdx - 1, -1), true);
        break;
      }
      case 'Enter': {
        const items = _getItems();
        if (_activeIdx >= 0 && items[_activeIdx]) {
          _close();
          if (_entries[_activeIdx]) _entries[_activeIdx].action();
        }
        break;
      }
    }
  });

  // ── Close on backdrop click ──
  backdrop.addEventListener('click', (e) => {
    if (e.target === backdrop) _close();
  });
  input.addEventListener('input', _runSearch);
}
