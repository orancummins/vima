// Theme management.
// Light/dark toggle with localStorage persistence, plus propagation of the
// active theme into embedded use-case iframes via postMessage.

import { $ } from './dom.js';
import { ROOT_EL, THEME_STORAGE_KEY } from './env.js';

export function _currentThemeMode() {
  return ROOT_EL.classList.contains('theme-light') ? 'light' : 'dark';
}

export function _postThemeToEmbeddedFrame(frame, mode) {
  if (!frame || !frame.contentWindow) return;
  const theme = mode === 'light' ? 'light' : 'dark';
  try {
    frame.contentWindow.postMessage({ type: 'vima:theme', theme }, window.location.origin);
  } catch (e) {}
}

export function _syncEmbeddedUseCaseTheme(mode) {
  const theme = mode === 'light' ? 'light' : 'dark';
  document.querySelectorAll('.sonic-webview-frame').forEach((frame) => {
    _postThemeToEmbeddedFrame(frame, theme);
  });
  _postThemeToEmbeddedFrame($('global-edit-modal-iframe'), theme);
}

export function _applyThemeMode(mode) {
  const theme = mode === 'light' ? 'light' : 'dark';
  const isLight = theme === 'light';
  ROOT_EL.classList.toggle('theme-light', isLight);
  document.body?.setAttribute('data-theme', theme);
  _syncEmbeddedUseCaseTheme(theme);
  const nextTheme = isLight ? 'dark' : 'light';
  const label = `Switch to ${nextTheme} theme`;
  document.querySelectorAll('.theme-toggle').forEach((toggle) => {
    toggle.setAttribute('aria-pressed', String(isLight));
    toggle.setAttribute('aria-label', label);
    toggle.title = label;
  });
}

export function _toggleThemeMode() {
  const nextTheme = _currentThemeMode() === 'light' ? 'dark' : 'light';
  _applyThemeMode(nextTheme);
  try {
    localStorage.setItem(THEME_STORAGE_KEY, nextTheme);
  } catch (e) {}
}

// Apply the persisted/initial theme and wire the top-bar toggle.
export function initTheme() {
  _applyThemeMode(_currentThemeMode());
  $('theme-toggle')?.addEventListener('click', _toggleThemeMode);
}
