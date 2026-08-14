// Network helpers.
// `_appPath` rewrites absolute same-origin paths to respect a reverse-proxy
// SCRIPT_ROOT prefix; `_nativeFetch` is a thin fetch wrapper that applies it.

import { SCRIPT_ROOT } from './env.js';

export function _appPath(path) {
  if (typeof path !== 'string') return path;
  if (!SCRIPT_ROOT) return path;
  if (!path.startsWith('/') && !/^https?:\/\//i.test(path)) return path;
  try {
    const url = new URL(path, window.location.href);
    if (url.origin !== window.location.origin) return path;
    if (url.pathname === SCRIPT_ROOT || url.pathname.startsWith(`${SCRIPT_ROOT}/`)) {
      return path;
    }
    url.pathname = `${SCRIPT_ROOT}${url.pathname.startsWith('/') ? '' : '/'}${url.pathname}`;
    return /^https?:\/\//i.test(path) ? url.href : `${url.pathname}${url.search}${url.hash}`;
  } catch (_) {
    return path;
  }
}

export const _nativeFetch = (resource, init) => {
  if (typeof resource === 'string') {
    return window.fetch(_appPath(resource), init);
  }
  if (resource instanceof Request) {
    const rewrittenUrl = _appPath(resource.url);
    if (rewrittenUrl === resource.url) return window.fetch(resource, init);
    return window.fetch(new Request(rewrittenUrl, resource), init);
  }
  return window.fetch(resource, init);
};
