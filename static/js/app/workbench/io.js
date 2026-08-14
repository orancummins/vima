// -------------------------------------------------------------------
// workbench/io.js
// Request/response panel rendering for the API workbench: HTTP status
// pill, JSON formatting (with optional header hiding), the header
// show/hide toggle, and two small JSON-walk helpers used by the send
// handler. Pure helpers + two in-place-mutated state objects
// (headersVisible, lastIoData) — no dependency on the workbench's
// API/op selection.
// -------------------------------------------------------------------
import { $ } from '../core/dom.js';

export const HTTP_REASONS = {
  100:"Continue",101:"Switching Protocols",200:"OK",201:"Created",202:"Accepted",
  204:"No Content",206:"Partial Content",301:"Moved Permanently",302:"Found",
  304:"Not Modified",400:"Bad Request",401:"Unauthorized",403:"Forbidden",
  404:"Not Found",405:"Method Not Allowed",406:"Not Acceptable",
  409:"Conflict",410:"Gone",422:"Unprocessable Entity",429:"Too Many Requests",
  500:"Internal Server Error",501:"Not Implemented",502:"Bad Gateway",
  503:"Service Unavailable",504:"Gateway Timeout",
};

export function setStatus(code) {
  const el = $("resp-status");
  if (code == null) { el.textContent = ""; el.className = "status-pill"; el.title = ""; return; }
  const s = String(code);
  el.textContent = s;
  el.className = "status-pill s" + s[0];
  el.title = HTTP_REASONS[Number(code)] || "";
}

// Recursively find the first https:// URL string in a JSON object/array.
export function _findFirstUrl(obj) {
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
export function _findKey(obj, key) {
  if (obj == null) return null;
  if (Array.isArray(obj)) {
    for (const v of obj) { const r = _findKey(v, key); if (r) return r; }
  } else if (typeof obj === "object") {
    if (obj[key] != null && typeof obj[key] === "string" && obj[key]) return obj[key];
    for (const v of Object.values(obj)) { const r = _findKey(v, key); if (r) return r; }
  }
  return null;
}

export function fmt(obj) {
  if (obj == null) return "—";
  try { return JSON.stringify(obj, null, 2); }
  catch { return String(obj); }
}

// -----------------------------------------------------------------------
// Headers toggle
// -----------------------------------------------------------------------
// Track whether headers are shown for each panel
export const headersVisible = { request: false, response: false };
// Store the last raw request/response objects so we can re-render on toggle
export const lastIoData = { request: null, response: null };

export function fmtWithoutHeaders(obj) {
  if (obj == null) return "—";
  try {
    const copy = { ...obj };
    delete copy.headers;
    return JSON.stringify(copy, null, 2);
  } catch { return String(obj); }
}

export function renderIoPanel(panel, obj) {
  // panel = 'request' | 'response'
  const elId = panel === 'request' ? 'req-body' : 'resp-body';
  const el = $(elId);
  if (!obj) { el.textContent = "—"; return; }
  el.textContent = headersVisible[panel] ? fmt(obj) : fmtWithoutHeaders(obj);
}

export function updateHeaderToggleBtn(panel) {
  const btnId = panel === 'request' ? 'req-headers-toggle' : 'resp-headers-toggle';
  const btn = $(btnId);
  if (!btn) return;
  btn.textContent = headersVisible[panel] ? 'Hide Headers' : 'Show Headers';
  btn.classList.toggle('active', headersVisible[panel]);
}

// Wire the request/response "Show/Hide Headers" toggle buttons.
export function initHeaderToggles() {
  document.querySelectorAll('.btn-toggle-headers').forEach(btn => {
    btn.addEventListener('click', () => {
      const panel = btn.dataset.panel;
      headersVisible[panel] = !headersVisible[panel];
      updateHeaderToggleBtn(panel);
      renderIoPanel(panel, lastIoData[panel]);
    });
  });
}
