// -------------------------------------------------------------------
// core/history.js
// Browser Back/Forward + deep-link (?tab/?bundle/?api/?uc) integration.
// Extracted verbatim from main.js. Self-contained: drives navigation by
// synthesizing clicks on nav elements, so it depends only on the DOM.
// Must run AFTER nav + sidebar click handlers are wired (call inline at
// the original source position).
// -------------------------------------------------------------------

export function initHistory() {
    // ---------------------------------------------------------------------
    // Browser history integration (Back / Forward buttons)
    // ---------------------------------------------------------------------
    // Every in-app navigation already happens via clicks on a known set of
    // elements (top tabs, sidebar items, bundle/API/use-case rows). We listen
    // for those clicks on the document AFTER the original handlers have run
    // and push the resulting state to the URL via the History API. A popstate
    // listener replays the click-driven handlers when the user goes Back /
    // Forward, guarded by ``_applyingHistory`` so the synthetic clicks don't
    // loop back through this same recorder.
    // ---------------------------------------------------------------------
    let _applyingHistory = false;
    let _navState = { tab: 'home' };

    function _stateToUrl(state) {
      const params = new URLSearchParams();
      if (state.tab && state.tab !== 'home') params.set('tab', state.tab);
      if (state.bundle) params.set('bundle', state.bundle);
      if (state.api) params.set('api', state.api);
      if (state.uc) params.set('uc', state.uc);
      const qs = params.toString();
      return location.pathname + (qs ? '?' + qs : '');
    }

    function _pushNavState(patch, { replace = false } = {}) {
      if (_applyingHistory) return;
      // Merge; clearing tab also clears tab-scoped selections.
      const next = Object.assign({}, _navState, patch);
      // Stringified comparison — avoids duplicate entries when the user
      // clicks the same row twice.
      if (!replace && _stateToUrl(next) === _stateToUrl(_navState)) return;
      _navState = next;
      const url = _stateToUrl(next);
      try {
        history[replace ? 'replaceState' : 'pushState'](next, '', url);
      } catch (_) { /* ignore — some sandboxed contexts disallow pushState */ }
    }

    function _applyNavState(state) {
      _applyingHistory = true;
      try {
        const tab = state.tab || 'home';
        const tabBtn = document.querySelector(`.top-tab[data-top-tab="${tab}"]`);
        if (tabBtn) tabBtn.click();
        if (state.bundle) {
          const bBtn = document.querySelector(`[data-bundle-id="${state.bundle}"]`);
          if (bBtn) bBtn.click();
        }
        if (state.api) {
          const aBtn = document.querySelector(`[data-api-id="${state.api}"]`);
          if (aBtn) aBtn.click();
        }
        if (state.uc) {
          const uBtn = document.querySelector(`[data-uc-id="${state.uc}"]`);
          if (uBtn) uBtn.click();
        }
      } finally {
        _applyingHistory = false;
        _navState = Object.assign({ tab: 'home' }, state);
      }
    }

    // Bubble-phase document recorder — fires after element handlers complete.
    document.addEventListener('click', (e) => {
      if (_applyingHistory) return;
      const t = e.target.closest('.top-tab, [data-bundle-id], [data-api-id], [data-uc-id]');
      if (!t) return;
      // Every nav click — whether from a real user gesture or a synthetic
      // ``.click()`` issued by another handler (e.g. a home-page CTA that
      // switches tabs, or a chip that opens an API) — gets its own history
      // entry. Earlier we collapsed synthetic clicks via ``replace`` to
      // avoid "intermediate hops", but that ate the home entry whenever a
      // CTA jumped from home to a tab, leaving Back to exit the app.
      if (t.matches('.top-tab')) {
        const tab = t.dataset.topTab;
        // Switching tabs clears the in-tab selection so Back goes to the bare tab.
        _pushNavState({ tab, bundle: null, api: null, uc: null });
      } else if (t.matches('[data-bundle-id]')) {
        // Each per-tab selection also clears the *other* tabs' selections,
        // otherwise stale ?api=… / ?uc=… ride along in the URL and get
        // re-applied when the user pops back to a different tab.
        _pushNavState({ tab: 'bundles', bundle: t.dataset.bundleId, api: null, uc: null });
      } else if (t.matches('[data-api-id]')) {
        _pushNavState({ tab: 'apis', api: t.dataset.apiId, bundle: null, uc: null });
      } else if (t.matches('[data-uc-id]')) {
        _pushNavState({ tab: 'usecases', uc: t.dataset.ucId, bundle: null, api: null });
      }
    });

    window.addEventListener('popstate', (e) => {
      const state = e.state || (function () {
        const p = new URLSearchParams(location.search);
        return {
          tab: p.get('tab') || 'home',
          bundle: p.get('bundle'),
          api: p.get('api'),
          uc: p.get('uc'),
        };
      })();
      _applyNavState(state);
    });

    // Honour ?tab=apis / ?tab=usecases / ?bundle=… / ?api=… / ?uc=… from
    // shared links or home-page CTAs. Replace (not push) so the first Back
    // press lands on the previous site, not on an empty home view.
    (function _bootstrapNavFromUrl() {
      const p = new URLSearchParams(location.search);
      const initial = {
        tab: p.get('tab'),
        bundle: p.get('bundle'),
        api: p.get('api'),
        uc: p.get('uc'),
      };
      // Infer tab from a deep-link selection if no explicit ?tab=.
      if (!initial.tab) {
        if (initial.bundle) initial.tab = 'bundles';
        else if (initial.api) initial.tab = 'apis';
        else if (initial.uc) initial.tab = 'usecases';
        else initial.tab = 'home';
      }
      if (initial.tab !== 'home' || initial.bundle || initial.api || initial.uc) {
        _applyNavState(initial);
      } else {
        document.body.style.overflow = 'hidden'; // home is the default tab
        const hdr = document.querySelector('.header');
        if (hdr) hdr.classList.add('header--home');
      }
      _pushNavState(initial, { replace: true });
    })();
}
