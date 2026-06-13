// ===========================================================================
// US-IP Status Poller
// Polls /diagnostics/us-ip-status and reflects state on [data-us-ip-warning]
// cards. US Open Finance APIs require a US VPN connection.
// ===========================================================================
import { _nativeFetch } from '../core/net.js';

let _ipStatusTimer = null;
let _lastUsIpStatus = null;

function _applyUsIpStatus(payload) {
  const statusOk = !!(payload && payload.success);
  const isUs = !!(payload && payload.is_us);
  const country = (payload && payload.country_code) ? String(payload.country_code).toUpperCase() : '';
  const ip = (payload && payload.ip) ? String(payload.ip) : '';
  const source = (payload && payload.source) ? String(payload.source) : 'server';

  const statusText = statusOk && isUs
    ? `US IP detected${ip ? ` (${ip})` : ''} via ${source}`
    : `Non-US or unverified${country ? ` (${country})` : ''}${ip ? ` - ${ip}` : ''} via ${source}`;
  const lightClass = statusOk && isUs ? 'of-ip-light--green' : 'of-ip-light--red';
  const pillClass = statusOk && isUs ? 'of-ip-pill--green' : 'of-ip-pill--red';
  const shortLabel = statusOk && isUs ? 'US IP' : 'Non-US IP used';
  const tooltip = `${statusText}\nUS Open Finance APIs require a US VPN connection.`;

  document.querySelectorAll('[data-us-ip-warning]').forEach((card) => {
    const light = card.querySelector('[data-us-ip-light]');
    const label = card.querySelector('[data-us-ip-text]');
    if (light) {
      light.classList.remove('of-ip-light--green', 'of-ip-light--red', 'of-ip-light--unknown');
      light.classList.add(lightClass);
    }
    if (label) label.textContent = shortLabel;
    card.classList.remove('of-ip-pill--green', 'of-ip-pill--red', 'of-ip-pill--unknown');
    card.classList.add(pillClass);
    card.setAttribute('title', tooltip);
    card.setAttribute('data-tooltip', tooltip);
  });

  _lastUsIpStatus = { success: statusOk, is_us: isUs, country_code: country, ip, source };
}

export function refreshUsIpStatus() {
  const applyFailure = (source) => {
    if (_lastUsIpStatus && _lastUsIpStatus.success) {
      _applyUsIpStatus(Object.assign({}, _lastUsIpStatus, { source: _lastUsIpStatus.source || source || 'cached' }));
      return;
    }
    _applyUsIpStatus({
      success: false,
      is_us: false,
      country_code: '',
      ip: '',
      source: source || 'unverified',
    });
  };

  _nativeFetch('/diagnostics/us-ip-status', { cache: 'no-store' })
    .then((r) => r.json())
    .then((data) => {
      const payload = data || {};
      if (payload.success) {
        _applyUsIpStatus(payload);
      } else {
        applyFailure('diagnostics-unavailable');
      }
    })
    .catch(() => applyFailure('diagnostics-unavailable'));
}

export function startUsIpStatusPolling() {
  if (_ipStatusTimer) return;
  refreshUsIpStatus();
  _ipStatusTimer = setInterval(refreshUsIpStatus, 15000);
}
