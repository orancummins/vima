(() => {
  const THEME_STORAGE_KEY = 'vima:theme';
  const ROOT_EL = document.documentElement;

  function normalizeTheme(mode) {
    return mode === 'light' ? 'light' : 'dark';
  }

  function applyTheme(mode) {
    const theme = normalizeTheme(mode);
    const isLight = theme === 'light';
    ROOT_EL.classList.toggle('theme-light', isLight);
    ROOT_EL.setAttribute('data-theme', theme);
    document.body?.setAttribute('data-theme', theme);
  }

  function readStoredTheme() {
    try {
      return normalizeTheme(localStorage.getItem(THEME_STORAGE_KEY));
    } catch (e) {
      return 'dark';
    }
  }

  applyTheme(readStoredTheme());
  document.addEventListener('DOMContentLoaded', () => applyTheme(readStoredTheme()), { once: true });

  window.addEventListener('message', (event) => {
    if (event.origin !== window.location.origin) return;
    const data = event.data || {};
    if (data.type !== 'vima:theme') return;
    const theme = normalizeTheme(data.theme);
    applyTheme(theme);
    try {
      localStorage.setItem(THEME_STORAGE_KEY, theme);
    } catch (e) {}
  });
})();