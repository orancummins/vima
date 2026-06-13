// -------------------------------------------------------------------
// core/catalog.js
// Shared data layer for the bundles + use-cases catalog. Both the
// Bundles tab (features/bundles.js) and the API detail panel
// (renderApiPairs in main.js) read this cache, so it lives in one
// place. Caches are warmed once at startup.
// -------------------------------------------------------------------
let _bundlesCache = null;
let _useCasesCache = null;

export function loadBundles() {
  if (_bundlesCache) return Promise.resolve(_bundlesCache);
  return fetch('/catalog/bundles', { cache: 'no-store' })
    .then((r) => r.json())
    .then((d) => { _bundlesCache = d.bundles || []; return _bundlesCache; })
    .catch(() => []);
}

export function loadUseCases() {
  if (_useCasesCache) return Promise.resolve(_useCasesCache);
  return fetch('/usecases', { cache: 'no-store' })
    .then((r) => r.json())
    .then((d) => { _useCasesCache = d.use_cases || []; return _useCasesCache; })
    .catch(() => []);
}

// Synchronous cache accessors (null until the matching loader resolves).
export function getBundlesCache() { return _bundlesCache; }
export function getUseCasesCache() { return _useCasesCache; }

// Warm both caches at startup, matching the original eager load.
loadBundles();
loadUseCases();
