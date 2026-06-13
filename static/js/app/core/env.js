// Core environment / runtime configuration.
// Read-only values injected by the server into the page (window.__*__) plus a
// few shared DOM/runtime constants. Imported wherever the app needs to know
// the catalog, runtime mode flags, or platform paths.

export const APIS = window.__APIS__ || [];
export const USE_CASES = window.__USE_CASES__ || [];
export const RUNTIME_MODE = window.__RUNTIME_MODE__ || {};
export const SERVER_MODE = !!RUNTIME_MODE.server_mode;
export const NON_US_MODE = !!RUNTIME_MODE.non_us_mode;
export const OPEN_FINANCE_US_API_ID = 'open_finance';
export const SERVER_MODE_TOOLTIP = 'server mode';
export const NON_US_TOOLTIP =
  'Disabled in non-us mode. If running on US IP, this would be enabled.';
export const THEME_STORAGE_KEY = 'vima:theme';
export const SCRIPT_ROOT = (document.body?.dataset?.scriptRoot || '').replace(/\/$/, '');
export const ROOT_EL = document.documentElement;
