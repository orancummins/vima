// -------------------------------------------------------------------
// core/nav.js
// Top-tab switching + home-page CTA buttons. Extracted from main.js.
// Pure DOM; communicates with history.js only via clicks/data-attrs.
// -------------------------------------------------------------------
import { $ } from './dom.js';
import { SERVER_MODE } from './env.js';
import { apiCallsClose, _startPolling, _stopPolling } from '../features/apiCallLog.js';
import { apisSnippetsClose } from '../features/apiSnippets.js';

export function initNav() {
    // ---------------------------------------------------------------------
    // Top tabs
    // ---------------------------------------------------------------------
    document.querySelectorAll(".top-tab").forEach((btn) => {
      btn.addEventListener("click", () => {
        document.querySelectorAll(".top-tab").forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        const tab = btn.dataset.topTab;
        document.body.style.overflow = tab === 'home' ? 'hidden' : '';
        const hdr = document.querySelector('.header');
        if (hdr) hdr.classList.toggle('header--home', tab === 'home');
        $("panel-home").classList.toggle("hidden", tab !== "home");
        $("panel-apis").classList.toggle("hidden", tab !== "apis");
        const bp = $("panel-bundles");
        if (bp) bp.classList.toggle("hidden", tab !== "bundles");
        $("panel-usecases").classList.toggle("hidden", tab !== "usecases");
        const fab = $('api-calls-fab');
        if (fab) fab.classList.toggle('hidden', tab !== 'usecases');
        const snipFab = $('apis-snippets-fab');
        if (snipFab) snipFab.classList.toggle('hidden', tab !== 'apis');
        // ViMA chat edit is only available on Use Cases
        const editBtnTop = $('global-edit-btn');
        if (editBtnTop) editBtnTop.classList.toggle('hidden', tab !== 'usecases' || SERVER_MODE);
        if (tab !== 'usecases') { apiCallsClose(); _stopPolling(); }
        else _startPolling();
        if (tab !== 'apis') apisSnippetsClose();
      });
    });

    // Home panel CTA buttons — switch to APIs or Use Cases tab
    document.querySelectorAll('.home-cta[data-switch-tab]').forEach(function(btn) {
      btn.addEventListener('click', function() {
        const tabBtn = document.querySelector('.top-tab[data-top-tab="' + btn.dataset.switchTab + '"]');
        if (tabBtn) tabBtn.click();
      });
    });
}
