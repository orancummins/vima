// -------------------------------------------------------------------
// core/region.js
// Region-gating helpers for NON-US mode. Shared by the menu, the API
// list, the Bundles tab and the use-case launchers. Pure functions —
// depend only on env config.
// -------------------------------------------------------------------
import { NON_US_MODE, OPEN_FINANCE_US_API_ID, USE_CASES } from './env.js';

export function _isNonUsBlockedApiId(apiId) {
  return NON_US_MODE && apiId === OPEN_FINANCE_US_API_ID;
}

export function _isNonUsBlockedUseCaseById(ucId) {
  if (!NON_US_MODE) return false;
  const uc = USE_CASES.find((u) => u.id === ucId);
  if (!uc) return false;
  return (uc.apis || []).includes(OPEN_FINANCE_US_API_ID);
}
