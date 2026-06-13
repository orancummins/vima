// -------------------------------------------------------------------
// features/apiSnippets.js
// APIs tab "View Code" Python snippets drawer. Extracted from main.js.
// Reads the current workbench selection via injected accessors so it
// stays decoupled from main.js's mutable currentApiId / currentOpId.
// -------------------------------------------------------------------
import { $ } from '../core/dom.js';
import { _nativeFetch } from '../core/net.js';
import { escapeHtml } from '../core/html.js';
import { APIS, SERVER_MODE } from '../core/env.js';

let _getCurrentApiId = () => null;
let _getCurrentOpId = () => null;

// Wire accessors from main.js so the drawer can follow the selected
// API / operation without owning that mutable state.
export function initApisSnippets(opts) {
  opts = opts || {};
  if (opts.getCurrentApiId) _getCurrentApiId = opts.getCurrentApiId;
  if (opts.getCurrentOpId) _getCurrentOpId = opts.getCurrentOpId;
}
  // -------------------------------------------------------------------
  // APIs tab — Python snippets drawer
  // Renders a copy-able Python snippet for the currently-selected API,
  // calling /explorer/<api_id>/snippet for the authoritative server-
  // rendered code. Selecting a different API in the sidebar updates
  // the snippet shown here.
  // -------------------------------------------------------------------
  let APIS_SNIPPETS_VISIBLE = false;
  let APIS_SNIPPETS_ACTIVE = null; // api_id of currently shown snippet

  function _snippetHighlight(code) {
    // Very small Python-ish syntax highlighter — order matters: strings
    // first (to swallow keyword-like content), then comments, then
    // keywords/numbers. We tokenise into a flat list so we never wrap a
    // span that already contains another span.
    const KEYWORDS = ['import', 'from', 'as', 'def', 'return', 'if', 'else', 'for', 'in', 'True', 'False', 'None', 'print', 'with'];
    const tokens = [];
    let i = 0;
    while (i < code.length) {
      const ch = code[i];
      if (ch === '#') {
        const end = code.indexOf('\n', i);
        const stop = end === -1 ? code.length : end;
        tokens.push({ t: 'com', v: code.slice(i, stop) });
        i = stop;
        continue;
      }
      if (ch === '"' || ch === "'") {
        // Triple-quoted strings
        if (code.slice(i, i + 3) === ch + ch + ch) {
          const end = code.indexOf(ch + ch + ch, i + 3);
          const stop = end === -1 ? code.length : end + 3;
          tokens.push({ t: 'str', v: code.slice(i, stop) });
          i = stop;
          continue;
        }
        // Single-line string
        let j = i + 1;
        while (j < code.length && code[j] !== ch) {
          if (code[j] === '\\' && j + 1 < code.length) j += 2;
          else j += 1;
        }
        tokens.push({ t: 'str', v: code.slice(i, j + 1) });
        i = j + 1;
        continue;
      }
      // Word
      if (/[A-Za-z_]/.test(ch)) {
        let j = i;
        while (j < code.length && /[A-Za-z0-9_]/.test(code[j])) j += 1;
        const word = code.slice(i, j);
        if (KEYWORDS.indexOf(word) !== -1) tokens.push({ t: 'kw', v: word });
        else if (code[j] === '(') tokens.push({ t: 'fn', v: word });
        else tokens.push({ t: 'raw', v: word });
        i = j;
        continue;
      }
      // Number
      if (/[0-9]/.test(ch)) {
        let j = i;
        while (j < code.length && /[0-9.]/.test(code[j])) j += 1;
        tokens.push({ t: 'num', v: code.slice(i, j) });
        i = j;
        continue;
      }
      tokens.push({ t: 'raw', v: ch });
      i += 1;
    }
    return tokens.map((tok) => {
      const v = escapeHtml(tok.v);
      if (tok.t === 'raw') return v;
      return `<span class="apis-snippets-tok-${tok.t}">${v}</span>`;
    }).join('');
  }

  function _snippetRenderTabs() { /* removed — only one snippet shown at a time */ }

  function _snippetRenderBody(api) {
    const body = $('apis-snippets-body');
    if (!body) return;
    if (!api) {
      body.innerHTML = `<p class="api-calls-empty">No API in this group.</p>`;
      return;
    }
    // Show a loading state immediately, then fetch the authoritative
    // server-rendered snippet (which knows the upstream URL, the env
    // vars from the catalog, and the OAuth1 signing pattern). This
    // replaces the previous client-only "call the proxy" stub.
    body.innerHTML = `
      <div class="apis-snippets-section">
        <div class="apis-snippets-section-meta">
          <span class="apis-snippets-section-label">Loading\u2026</span>
        </div>
        <pre class="apis-snippets-code"><code>${escapeHtml('# Building authentic snippet\u2026')}</code></pre>
      </div>`;
    const op = (api.operations || []).find((o) => o.id === _getCurrentOpId())
             || (api.operations || [])[0];
    const opId = op ? op.id : '';
    const url = `/explorer/${encodeURIComponent(api.id)}/snippet`
              + (opId ? `?op=${encodeURIComponent(opId)}` : '');
    // Guard against rapid tab switches — only render if this fetch is
    // still the latest one for the active API.
    const requestForApi = api.id;
    fetch(url)
      .then((r) => r.ok ? r.json() : Promise.reject(new Error('HTTP ' + r.status)))
      .then((data) => {
        if (APIS_SNIPPETS_ACTIVE !== requestForApi) return;
        const code = data.snippet || '';
        const summary = data.summary || (op ? `${op.method || 'POST'} \u00b7 ${op.name}` : 'No operations');
        const runBtn = SERVER_MODE
          ? ''
          : `<button class="apis-snippets-copy apis-snippets-run" type="button" data-snippet-run title="Open a terminal on this machine and run the snippet">\u25b6 Run in terminal</button>`;
        body.innerHTML = `
          <div class="apis-snippets-section">
            <div class="apis-snippets-section-meta">
              <span class="apis-snippets-section-label">${escapeHtml(summary)}</span>
              <div class="apis-snippets-section-actions">
                <button class="apis-snippets-codeonly" type="button" data-snippet-copy title="Copy the Python source">Copy code</button>
                ${runBtn}
              </div>
            </div>
            <pre class="apis-snippets-code"><code contenteditable="plaintext-only" spellcheck="false" autocorrect="off" autocapitalize="off" data-snippet-code>${_snippetHighlight(code)}</code></pre>
          </div>`;
        const codeEl = body.querySelector('[data-snippet-code]');
        const getCurrentCode = () => (codeEl ? codeEl.innerText : code);
        // First edit strips syntax highlighting so the user sees plain
        // editable text instead of fighting nested <span> elements.
        let flattened = false;
        if (codeEl) {
          const flatten = () => {
            if (flattened) return;
            flattened = true;
            const txt = codeEl.innerText;
            codeEl.textContent = txt;
          };
          codeEl.addEventListener('focus', flatten, { once: true });
          codeEl.addEventListener('beforeinput', flatten, { once: true });
          // Tab inserts 4 spaces instead of moving focus out of the
          // editor. Shift+Tab still escapes so keyboard users aren't
          // trapped. Works with multi-line selections by indenting
          // every selected line.
          codeEl.addEventListener('keydown', (ev) => {
            if (ev.key !== 'Tab' || ev.shiftKey) return;
            ev.preventDefault();
            flatten();
            const sel = window.getSelection();
            if (!sel || sel.rangeCount === 0) return;
            const range = sel.getRangeAt(0);
            const INDENT = '    ';
            if (range.collapsed) {
              range.insertNode(document.createTextNode(INDENT));
              range.collapse(false);
            } else {
              const text = range.toString();
              const replaced = text.includes('\n')
                ? text.split('\n').map((ln) => INDENT + ln).join('\n')
                : INDENT + text;
              range.deleteContents();
              const node = document.createTextNode(replaced);
              range.insertNode(node);
              range.setStartAfter(node);
              range.collapse(true);
            }
            sel.removeAllRanges();
            sel.addRange(range);
          });
        }
        const flashCopied = (btn, label) => {
          const original = btn.textContent;
          btn.textContent = label || 'Copied';
          btn.classList.add('apis-snippets-copy--copied');
          setTimeout(() => {
            btn.textContent = original;
            btn.classList.remove('apis-snippets-copy--copied');
          }, 1600);
        };
        const copyBtn = body.querySelector('[data-snippet-copy]');
        if (copyBtn) copyBtn.addEventListener('click', () => {
          navigator.clipboard.writeText(getCurrentCode()).then(() => flashCopied(copyBtn, 'Copied \u2713'));
        });
        const runBtnEl = body.querySelector('[data-snippet-run]');
        if (runBtnEl) runBtnEl.addEventListener('click', () => {
          const original = runBtnEl.textContent;
          runBtnEl.disabled = true;
          runBtnEl.textContent = 'Launching\u2026';
          _nativeFetch(`/explorer/${encodeURIComponent(api.id)}/run`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ operation: opId, code: getCurrentCode() }),
          })
            .then((r) => r.json().then((d) => ({ ok: r.ok, d })))
            .then(({ ok, d }) => {
              runBtnEl.disabled = false;
              if (!ok || d.error) {
                runBtnEl.textContent = 'Failed';
                runBtnEl.classList.add('apis-snippets-run--err');
                alert('Could not launch terminal: ' + (d.error || 'unknown error'));
                setTimeout(() => {
                  runBtnEl.textContent = original;
                  runBtnEl.classList.remove('apis-snippets-run--err');
                }, 2400);
              } else {
                runBtnEl.textContent = 'Launched \u2713';
                runBtnEl.classList.add('apis-snippets-copy--copied');
                setTimeout(() => {
                  runBtnEl.textContent = original;
                  runBtnEl.classList.remove('apis-snippets-copy--copied');
                }, 2400);
              }
            })
            .catch((err) => {
              runBtnEl.disabled = false;
              runBtnEl.textContent = original;
              alert('Could not launch terminal: ' + (err && err.message || err));
            });
        });
      })
      .catch((err) => {
        if (APIS_SNIPPETS_ACTIVE !== requestForApi) return;
        body.innerHTML = `
          <div class="apis-snippets-section">
            <div class="apis-snippets-section-meta">
              <span class="apis-snippets-section-label">Snippet unavailable</span>
            </div>
            <pre class="apis-snippets-code"><code>${escapeHtml('# Unable to build snippet: ' + (err && err.message || err))}</code></pre>
          </div>`;
      });
  }

  // ---- "Commands" sub-modal --------------------------------------
  // Builds a one-shot install + env-var script for the user's OS using
  // values pulled from the local Solution Studio config. Disabled in
  // server mode (the button isn't rendered, and the endpoint 403s).
  function _detectOs() {
    const p = (navigator.userAgentData && navigator.userAgentData.platform)
      || navigator.platform || navigator.userAgent || '';
    const s = String(p).toLowerCase();
    if (s.indexOf('win') !== -1) return 'windows';
    if (s.indexOf('mac') !== -1) return 'macos';
    return 'linux';
  }

  function _shellQuote(val, os) {
    if (val === null || val === undefined) val = '';
    const s = String(val);
    if (os === 'windows') {
      // PowerShell single-quoted: double any embedded single quotes.
      return "'" + s.replace(/'/g, "''") + "'";
    }
    // POSIX single-quoted: close, escape, reopen.
    return "'" + s.replace(/'/g, "'\\''") + "'";
  }

  function _buildSetupScript(data, os) {
    const pkgs = (data.packages || []).join(' ');
    const lines = [];
    if (os === 'windows') {
      lines.push('# Windows PowerShell \u2014 uses `py -m pip` so it works even if pip.exe is blocked.');
      if (pkgs) lines.push(`py -m pip install --user ${pkgs}`);
      lines.push('');
      (data.env || []).forEach((e) => {
        const v = e.set ? e.value : `<your ${e.name}>`;
        lines.push(`$env:${e.name} = ${_shellQuote(v, os)}`);
      });
    } else {
      lines.push(os === 'macos' ? '# macOS (bash/zsh)' : '# Linux (bash/zsh)');
      if (pkgs) lines.push(`python3 -m pip install --user ${pkgs}`);
      lines.push('');
      (data.env || []).forEach((e) => {
        const v = e.set ? e.value : `<your ${e.name}>`;
        lines.push(`export ${e.name}=${_shellQuote(v, os)}`);
      });
    }
    return lines.join('\n') + '\n';
  }

  // Build a single, paste-and-run command for the user's OS:
  //   * exports the credentials (real values where set locally, placeholders otherwise)
  //   * pip-installs the dependencies (via `<launcher> -m pip` so it
  //     works even if pip.exe is blocked by AV/EDR, which is common on
  //     locked-down corporate Windows machines)
  //   * pipes the snippet into the Python launcher via stdin so no .py
  //     file is needed
  // Uses `py` on Windows (the launcher is installed by every Python
  // distribution, while `python.exe` is often the WindowsApps store
  // stub) and `python3` on POSIX. `--user` avoids permission errors
  // when site-packages isn't writable.
  function _buildRunCommand(setup, code, os) {
    const pkgs = (setup.packages || []).join(' ');
    const lines = [];
    if (os === 'windows') {
      const launcher = 'py';
      lines.push('# Paste into PowerShell. Sets env vars, installs deps, runs the snippet.');
      lines.push('# Uses the `py` launcher + `py -m pip` so it works even if pip.exe / python.exe');
      lines.push('# are blocked by corporate AV or shadowed by the Windows Store stub.');
      (setup.env || []).forEach((e) => {
        const v = e.set ? e.value : `<your ${e.name}>`;
        lines.push(`$env:${e.name} = ${_shellQuote(v, os)}`);
      });
      if (pkgs) lines.push(`${launcher} -m pip install --user ${pkgs}`);
      // Single-quoted PowerShell here-string: opaque literal, no
      // variable expansion, no escaping needed for $ or quotes inside.
      lines.push("@'");
      lines.push(code.replace(/\r?\n$/, ''));
      lines.push(`'@ | ${launcher} -`);
    } else {
      const launcher = 'python3';
      lines.push(os === 'macos'
        ? '# Paste into a macOS terminal (bash/zsh). Sets env vars, installs deps, runs the snippet.'
        : '# Paste into a Linux terminal (bash/zsh). Sets env vars, installs deps, runs the snippet.');
      (setup.env || []).forEach((e) => {
        const v = e.set ? e.value : `<your ${e.name}>`;
        lines.push(`export ${e.name}=${_shellQuote(v, os)}`);
      });
      if (pkgs) lines.push(`${launcher} -m pip install --user ${pkgs}`);
      // Quoted heredoc terminator disables shell expansion inside the
      // body, so the snippet's $vars / backticks survive untouched.
      lines.push(`${launcher} - <<'VIMA_SNIPPET_EOF'`);
      lines.push(code.replace(/\r?\n$/, ''));
      lines.push('VIMA_SNIPPET_EOF');
    }
    return lines.join('\n') + '\n';
  }

  function _snippetShowSetup(apiId) {
    _nativeFetch(`/explorer/${encodeURIComponent(apiId)}/setup`)
      .then((r) => r.ok ? r.json() : Promise.reject(new Error('HTTP ' + r.status)))
      .then((data) => {
        const osList = ['windows', 'macos', 'linux'];
        const initialOs = _detectOs();
        const missing = (data.env || []).filter((e) => !e.set).map((e) => e.name);
        const warning = missing.length
          ? `<div class="apis-setup-warning">${escapeHtml('Not set locally: ' + missing.join(', ') + ' \u2014 placeholders inserted.')}</div>`
          : '';
        const tabs = osList.map((o) => {
          const label = o === 'windows' ? 'Windows (PowerShell)' : (o === 'macos' ? 'macOS' : 'Linux');
          return `<button class="apis-setup-tab${o === initialOs ? ' apis-setup-tab--active' : ''}" data-setup-os="${o}" type="button">${label}</button>`;
        }).join('');
        const html = `
          <div class="tc-modal-backdrop apis-setup-backdrop" id="apis-setup-backdrop">
            <div class="tc-modal apis-setup-modal" role="dialog" aria-modal="true" aria-label="Setup commands">
              <div class="tc-modal-header">
                <div class="tc-modal-title">Setup commands <span class="apis-snippets-modal-chip">${escapeHtml(apiId)}</span></div>
                <button class="tc-modal-close" data-setup-close aria-label="Close">&times;</button>
              </div>
              <div class="apis-setup-body">
                <div class="apis-setup-tabs">${tabs}</div>
                ${warning}
                <pre class="apis-snippets-code apis-setup-code"><code></code></pre>
                <div class="apis-setup-actions">
                  <button class="apis-snippets-copy" type="button" data-setup-copy>Copy</button>
                </div>
              </div>
            </div>
          </div>`;
        const wrap = document.createElement('div');
        wrap.innerHTML = html.trim();
        const backdrop = wrap.firstChild;
        document.body.appendChild(backdrop);
        const codeEl = backdrop.querySelector('.apis-setup-code code');
        const render = (os) => {
          const script = _buildSetupScript(data, os);
          codeEl.textContent = script;
          codeEl.dataset.script = script;
        };
        render(initialOs);
        requestAnimationFrame(() => backdrop.classList.add('tc-modal-backdrop--open'));
        const close = () => {
          backdrop.classList.remove('tc-modal-backdrop--open');
          setTimeout(() => backdrop.remove(), 200);
        };
        backdrop.querySelector('[data-setup-close]').addEventListener('click', close);
        backdrop.addEventListener('click', (e) => { if (e.target === backdrop) close(); });
        backdrop.querySelectorAll('[data-setup-os]').forEach((btn) => {
          btn.addEventListener('click', () => {
            backdrop.querySelectorAll('[data-setup-os]').forEach((b) => b.classList.remove('apis-setup-tab--active'));
            btn.classList.add('apis-setup-tab--active');
            render(btn.dataset.setupOs);
          });
        });
        const copyBtn = backdrop.querySelector('[data-setup-copy]');
        copyBtn.addEventListener('click', () => {
          navigator.clipboard.writeText(codeEl.dataset.script || '').then(() => {
            copyBtn.textContent = 'Copied';
            copyBtn.classList.add('apis-snippets-copy--copied');
            setTimeout(() => {
              copyBtn.textContent = 'Copy';
              copyBtn.classList.remove('apis-snippets-copy--copied');
            }, 1400);
          });
        });
      })
      .catch((err) => {
        alert('Unable to build setup commands: ' + (err && err.message || err));
      });
  }

  function apisSnippetsShow(apiId) {
    const active = APIS.find((a) => a.id === apiId)
                || APIS.find((a) => a.id === _getCurrentApiId())
                || APIS[0];
    APIS_SNIPPETS_ACTIVE = active ? active.id : null;
    const groupChip = $('apis-snippets-group');
    if (groupChip) groupChip.textContent = active ? active.name : '';
    _snippetRenderBody(active);
  }

  function apisSnippetsOpen() {
    APIS_SNIPPETS_VISIBLE = true;
    const backdrop = $('apis-snippets-backdrop');
    if (backdrop) {
      backdrop.classList.remove('hidden');
      // Force a reflow so the opacity/transform transition runs.
      // eslint-disable-next-line no-unused-expressions
      backdrop.offsetHeight;
      requestAnimationFrame(() => backdrop.classList.add('tc-modal-backdrop--open'));
    }
    const fab = $('apis-snippets-fab');
    if (fab) {
      fab.classList.add('api-calls-fab--active');
      const lbl = fab.querySelector('.api-calls-fab-label');
      if (lbl) lbl.textContent = 'Hide snippet';
    }
    apisSnippetsShow(_getCurrentApiId());
  }

  function apisSnippetsClose() {
    APIS_SNIPPETS_VISIBLE = false;
    const backdrop = $('apis-snippets-backdrop');
    if (backdrop) {
      backdrop.classList.remove('tc-modal-backdrop--open');
      // Match the 0.2s transition before hiding so we keep the fade-out.
      setTimeout(() => { backdrop.classList.add('hidden'); }, 200);
    }
    const fab = $('apis-snippets-fab');
    if (fab) {
      fab.classList.remove('api-calls-fab--active');
      const lbl = fab.querySelector('.api-calls-fab-label');
      if (lbl) lbl.textContent = 'View Code';
    }
  }

  // --- Public seam helpers (encapsulate visibility checks for callers) ---
  function apisSnippetsToggle() {
    if (APIS_SNIPPETS_VISIBLE) apisSnippetsClose();
    else apisSnippetsOpen();
  }
  function apisSnippetsIsVisible() {
    return APIS_SNIPPETS_VISIBLE;
  }
  // Called when the selected API changes; follow it if the drawer is open.
  function apisSnippetsFollowApi(apiId) {
    if (APIS_SNIPPETS_VISIBLE) apisSnippetsShow(apiId);
  }
  // Called when the selected operation changes; refresh the body only if
  // the drawer is currently showing this API's snippet.
  function apisSnippetsRefreshOp(apiId) {
    if (APIS_SNIPPETS_VISIBLE && APIS_SNIPPETS_ACTIVE === apiId) {
      const active = APIS.find((a) => a.id === apiId);
      if (active) _snippetRenderBody(active);
    }
  }

export {
  apisSnippetsShow,
  apisSnippetsOpen,
  apisSnippetsClose,
  apisSnippetsToggle,
  apisSnippetsIsVisible,
  apisSnippetsFollowApi,
  apisSnippetsRefreshOp,
};
