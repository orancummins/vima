// -------------------------------------------------------------------
// workbench/simToggle.js
// The per-API "Sim / Live" simulator toggle in the workbench header.
// Talks to /api-sim/admin/{toggle,status}. fetchSimStatus() is called
// by renderApi() whenever an API is opened; initSimToggle() wires the
// checkbox once at startup.
// -------------------------------------------------------------------
import { $ } from '../core/dom.js';
import { currentApi } from '../core/state.js';

export function setSimUI(simulated) {
  const cb = $("sim-toggle-cb");
  const label = $("sim-toggle-label");
  const track = document.querySelector(".sim-toggle-track");
  if (!cb || !label) return;
  cb.checked = simulated;
  label.textContent = simulated ? "Sim" : "Live";
  label.classList.toggle("sim-on", simulated);
  if (track) track.style.background = simulated ? "#7c3aed" : "";
  const thumb = track && track.querySelector(".sim-toggle-thumb");
  if (thumb) thumb.style.left = simulated ? "19px" : "3px";
}

export function fetchSimStatus(apiId) {
  fetch("/api-sim/admin/status")
    .then((r) => r.json())
    .then((data) => {
      const entry = data[apiId];
      setSimUI(entry ? entry.simulated : false);
    })
    .catch(() => setSimUI(false));
}

export function initSimToggle() {
  const cb = $("sim-toggle-cb");
  const label = $("sim-toggle-label");
  if (!cb) return;
  cb.addEventListener("change", () => {
    const api = currentApi();
    if (!api) return;
    const simulated = cb.checked;
    fetch("/api-sim/admin/toggle", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ api: api.id, simulated }),
    })
      .then((r) => r.json())
      .then(() => setSimUI(simulated))
      .catch(() => {});
  });
}
