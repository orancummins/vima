// -------------------------------------------------------------------
// workbench/launchBanner.js
// Sticky launch banner for the API workbench. When an operation returns
// a browser-handoff (Open Finance EU / AU / US managed-flow open_link, or
// a 3DS browser_action), the Launch button + sandbox test-credentials
// table are rendered into a sticky banner at the top of the op-panel
// scroll so the user doesn't have to scroll past the params list.
//
// Pure DOM helpers — no workbench state. Callers (restoreIo / send /
// renderApi) live in main.js and import these.
// -------------------------------------------------------------------
import { $ } from '../core/dom.js';

export function _resetLaunchBanner() {
  const el = $("op-launch-banner");
  if (!el) return;
  el.innerHTML = "";
  el.hidden = true;
  el.removeAttribute("data-url");
}
// Show a placeholder banner before the call is made — prompts the user
// to click Send first, then the real URL is injected once the card
// reference is returned.
export function _showLaunchBannerPending() {
  const el = $("op-launch-banner");
  if (!el) return;
  el.innerHTML = "";
  el.className = "op-launch-banner op-launch-banner--pending";
  const text = document.createElement("div");
  text.className = "op-launch-banner-text";
  const title = document.createElement("strong");
  title.className = "op-launch-banner-title";
  title.textContent = "Browser action required";
  const desc = document.createElement("span");
  desc.textContent = "Click Send to enroll the card \u2014 a Launch 3DS Method button will appear here once the card reference is ready.";
  text.appendChild(title);
  text.appendChild(desc);
  el.appendChild(text);
  el.hidden = false;
  el.removeAttribute("data-url");
}
export function _showLaunchBanner({ url, label, note, testCredentials }) {
  const el = $("op-launch-banner");
  if (!el) return;
  el.innerHTML = "";
  const text = document.createElement("div");
  text.className = "op-launch-banner-text";
  const title = document.createElement("strong");
  title.className = "op-launch-banner-title";
  title.textContent = "Browser action required";
  const desc = document.createElement("span");
  desc.textContent = note;
  text.appendChild(title);
  text.appendChild(desc);
  const btn = document.createElement("a");
  btn.className = "op-launch-banner-btn";
  btn.href = url;
  btn.target = "_blank";
  btn.rel = "noopener";
  btn.textContent = label;
  el.appendChild(text);
  el.appendChild(btn);
  if (testCredentials && Array.isArray(testCredentials.rows) && testCredentials.rows.length) {
    el.appendChild(_buildTestCredentialsBlock(testCredentials));
  }
  el.hidden = false;
  el.dataset.url = url;
}

// Render a compact sandbox-test-users credentials table inside the launch
// banner. Highlights the recommended starter user and links to the official
// docs page so reviewers can cross-check.
export function _buildTestCredentialsBlock(creds) {
  const wrap = document.createElement("div");
  wrap.className = "op-launch-banner-creds";
  const header = document.createElement("div");
  header.className = "op-launch-banner-creds-header";
  const h = document.createElement("strong");
  h.textContent = creds.title || "Sandbox test users";
  header.appendChild(h);
  if (creds.docs_url) {
    const a = document.createElement("a");
    a.href = creds.docs_url;
    a.target = "_blank";
    a.rel = "noopener";
    a.textContent = creds.docs_label || "View in docs ↗";
    a.className = "op-launch-banner-creds-docs";
    header.appendChild(a);
  }
  wrap.appendChild(header);
  if (creds.providers_note) {
    const p = document.createElement("div");
    p.className = "op-launch-banner-creds-note";
    p.textContent = creds.providers_note;
    wrap.appendChild(p);
  }
  const table = document.createElement("table");
  table.className = "op-launch-banner-creds-table";
  if (Array.isArray(creds.columns)) {
    const thead = document.createElement("thead");
    const tr = document.createElement("tr");
    creds.columns.forEach((c) => {
      const th = document.createElement("th");
      th.textContent = c;
      tr.appendChild(th);
    });
    thead.appendChild(tr);
    table.appendChild(thead);
  }
  const tbody = document.createElement("tbody");
  const rec = creds.recommended || "";
  creds.rows.forEach((row) => {
    const tr = document.createElement("tr");
    if (row[0] === rec) tr.className = "is-recommended";
    row.forEach((cell, idx) => {
      const td = document.createElement("td");
      // First three columns are short identifiers — render as <code>.
      if (idx < 3) {
        const code = document.createElement("code");
        code.textContent = cell;
        td.appendChild(code);
      } else {
        td.textContent = cell;
      }
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });
  table.appendChild(tbody);
  wrap.appendChild(table);
  return wrap;
}
