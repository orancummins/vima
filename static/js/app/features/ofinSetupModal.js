// -------------------------------------------------------------------
// features/ofinSetupModal.js
// Open Finance setup guide modal. Shown when the user opens the
// open_finance API (or when refresh_accounts returns nothing). The
// "Go create a test customer" button jumps to the workbench, so the
// workbench's selectOp is injected via initOfinSetupModal().
// -------------------------------------------------------------------
import { $ } from '../core/dom.js';

const OFIN_SUPPRESS_KEY = 'vima:ofin-setup-suppress';

// Injected from main.js once the workbench is wired up.
let _selectOp = () => {};

export function initOfinSetupModal(opts) {
  opts = opts || {};
  if (opts.selectOp) _selectOp = opts.selectOp;
}

(function () {
  const modal = $("ofin-setup-modal");
  const closeBtn = $("ofin-setup-close");
  const dismissBtn = $("ofin-setup-dismiss");
  const goCreateBtn = $("ofin-setup-go-create");
  const suppressCb = $("ofin-setup-suppress");
  if (!modal) return;

  // Reflect stored suppression state onto the checkbox
  try {
    if (localStorage.getItem(OFIN_SUPPRESS_KEY) === '1') suppressCb.checked = true;
  } catch (e) {}

  function saveSuppression() {
    try {
      if (suppressCb && suppressCb.checked) {
        localStorage.setItem(OFIN_SUPPRESS_KEY, '1');
      } else {
        localStorage.removeItem(OFIN_SUPPRESS_KEY);
      }
    } catch (e) {}
  }

  function hide() {
    saveSuppression();
    modal.classList.add("hidden");
  }

  closeBtn && closeBtn.addEventListener("click", hide);
  dismissBtn && dismissBtn.addEventListener("click", hide);
  modal.addEventListener("click", (e) => { if (e.target === modal) hide(); });

  goCreateBtn && goCreateBtn.addEventListener("click", () => {
    hide();
    // Navigate to open_finance API and select create_test_customer op
    const apiBtn = document.querySelector('[data-api-id="open_finance"]');
    if (apiBtn) {
      apiBtn.click();
      // Wait for renderApi to complete, then select the op
      setTimeout(() => _selectOp("create_test_customer"), 100);
    }
  });
})();

export function showOfinSetupModal() {
  try {
    if (localStorage.getItem(OFIN_SUPPRESS_KEY) === '1') return;
  } catch (e) {}
  const modal = $("ofin-setup-modal");
  if (modal) modal.classList.remove("hidden");
}

// Preserve the legacy public global (templates / other scripts may call it).
window.showOfinSetupModal = showOfinSetupModal;
