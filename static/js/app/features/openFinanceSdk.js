// -------------------------------------------------------------------
// features/openFinanceSdk.js
// Global Open Finance SDK panel + Live Demo (Bundles tab). Extracted
// from main.js. Self-contained: talks to the app only through the DOM
// and the window.__sdkDemo / __sdkRunViz / __sdkGlobe globals it shares
// with the inline globe script. main.js calls _initSdkDemo / _initLiveDemo
// from selectSdk().
// -------------------------------------------------------------------
import { APIS } from '../core/env.js';
import { _nativeFetch } from '../core/net.js';
import { escapeHtml } from '../core/html.js';
  /* ============ Global Open Finance SDK panel ============ */
  const SDK_BANKS = {
    us: { name: 'First Platypus Bank', host: 'connect2.finicity.com', initial: 'P', accent: '#eb001b' },
    au: { name: 'Regional Australia Bank', host: 'connect.openbanking.mastercard.com.au', initial: 'R', accent: '#00843d' },
    eu: { name: 'Nordea', host: 'connect.openbanking.mastercard.eu', initial: 'N', accent: '#2d6cdf' },
  };
  const SDK_SCRIPTS = {
    us: [
      { cmd: 'ofin us auth token', out: [
        ['ok', '● 200  HTTP status'],
        ['dim', '{'],
        ['key', '  "token": "g3gT34fZtZ...",'],
        ['dim', '  "message": "Token created successfully"'],
        ['dim', '}'],
      ] },
      { cmd: 'ofin us customers add-testing --username demo1', out: [
        ['ok', '● 201  HTTP status'],
        ['dim', 'saved: customer_id=9021936662'],
      ] },
      { cmd: 'ofin us connect generate --open', out: [
        ['ok', '● 200  HTTP status'],
        ['key', '  link → https://connect2.finicity.com/?ticket=a1b2c3'],
        ['dim', '↗ opening secure bank login…'],
      ], bank: true },
      { cmd: 'ofin us transactions list --from-date 1748649600 --to-date 1749513600', out: [
        ['ok', '● 200  HTTP status'],
        ['dim', '{ "transactions": ['],
        ['dim', '  {'],
        ['key', '    "id": 8645213782,'],
        ['dim', '    "amount": -42.18,'],
        ['dim', '    "accountId": 7045123456,'],
        ['dim', '    "description": "BLUE BOTTLE COFFEE",'],
        ['dim', '    "status": "active",'],
        ['dim', '    "postedDate": 1749081600,'],
        ['dim', '    "transactionDate": 1748995200,'],
        ['dim', '    "categorization": { "category": "Restaurants" }'],
        ['dim', '  },'],
        ['key', '    "id": 8645213655,'],
        ['dim', '    "amount": 2350.00,  "description": "PAYROLL DEPOSIT" …'],
        ['dim', '] }  (32 transactions)'],
      ] },
    ],
    au: [
      { cmd: 'ofin au auth token', out: [
        ['ok', '● 200  HTTP status'],
        ['dim', '{'],
        ['key', '  "token": "q5HmLWuu7u...",'],
        ['dim', '  "message": "Token created successfully"'],
        ['dim', '}'],
      ] },
      { cmd: 'ofin au connect generate --open', out: [
        ['ok', '● 200  HTTP status'],
        ['key', '  link → https://connect.openbanking.mastercard.com.au/?id=9f2a'],
        ['dim', '↗ opening secure bank login…'],
      ], bank: true },
      { cmd: 'ofin au transactions list', out: [
        ['ok', '● 200  HTTP status'],
        ['dim', '{ "data": { "transactions": ['],
        ['dim', '  {'],
        ['key', '    "transactionId": "4f9c1a7e-22b0-4f6a-9d1e-7c8b",'],
        ['dim', '    "accountId": "0a3f8d21-5e44-4b9c-aa12",'],
        ['dim', '    "type": "PAYMENT",  "status": "POSTED",'],
        ['dim', '    "description": "WOOLWORTHS 1234 SYDNEY",'],
        ['dim', '    "postingDateTime": "2026-06-10T08:14:22Z",'],
        ['dim', '    "amount": "-58.40",  "currency": "AUD"'],
        ['dim', '  },'],
        ['key', '    "amount": "-12.90",  "description": "OPAL TRANSPORT" …'],
        ['dim', '] } }  (18 transactions)'],
      ] },
    ],
    eu: [
      { cmd: 'ofin eu auth token', out: [
        ['ok', '● 200  HTTP status'],
        ['dim', '{'],
        ['key', '  "access_token": "eyJhbGciOiJS...",'],
        ['dim', '  "token_type": "bearer",'],
        ['dim', '  "message": "Token created successfully"'],
        ['dim', '}'],
      ] },
      { cmd: 'ofin eu flow create --open', out: [
        ['ok', '● 200  HTTP status'],
        ['key', '  flowUrl → https://connect.openbanking.mastercard.eu/?flow=7c1d'],
        ['dim', '↗ opening secure bank login…'],
      ], bank: true },
      { cmd: 'ofin eu transactions list', out: [
        ['ok', '● 200  HTTP status'],
        ['dim', '{ "transactions": ['],
        ['dim', '  {'],
        ['key', '    "id": "f1e2d3c4-9a8b-4c7d-8e6f",'],
        ['dim', '    "date": "2026-06-10",'],
        ['dim', '    "text": "Netto Supermarked",'],
        ['dim', '    "amount": -124.50,  "currency": "DKK",'],
        ['dim', '    "type": "Debit",  "state": "Booked"'],
        ['dim', '  },'],
        ['key', '    "amount": 18500.00,  "text": "LØN — SALARY" …'],
        ['dim', '] }  (24 transactions)'],
      ] },
    ],
  };
  // "All commands" lists the full operation catalog spanning all three
  // continents — exactly what `ofin ops` prints (US + AU + EU).
  SDK_SCRIPTS.all = [
    { cmd: 'ofin ops', out: [
      ['dim', 'Open Finance — all operations across 3 continents'],
      ['dim', ''],
      ['ok', '🇺🇸  UNITED STATES  (Finicity)'],
      ['key', '  ofin us auth token'],
      ['key', '  ofin us customers add-testing --username demo1'],
      ['key', '  ofin us customers list [--search foo] [--limit 25]'],
      ['key', '  ofin us customers get [--customer-id ID]'],
      ['key', '  ofin us customers use <CUSTOMER_ID>'],
      ['key', '  ofin us connect generate [--customer-id ID] [--experience EXP] [--open]'],
      ['key', '  ofin us accounts list [--customer-id ID]'],
      ['key', '  ofin us accounts refresh [--customer-id ID]'],
      ['key', '  ofin us balance [--customer-id ID] [--account-id ID]'],
      ['key', '  ofin us transactions list --from-date <epoch> --to-date <epoch> [--limit N]'],
      ['key', '  ofin us reports voa [--account-ids a,b]'],
      ['key', '  ofin us reports voi [--account-ids a,b]'],
      ['dim', ''],
      ['ok', '🇦🇺  AUSTRALIA  (CDR)'],
      ['key', '  ofin au auth token'],
      ['key', '  ofin au customers add-testing --username demo1'],
      ['key', '  ofin au customers list'],
      ['key', '  ofin au institutions list [--search foo]'],
      ['key', '  ofin au connect generate [--customer-id ID] [--webhook-url URL] [--open]'],
      ['key', '  ofin au consents list [--customer-id ID] [--status ACTIVE]'],
      ['key', '  ofin au accounts list [--customer-id ID] [--consent-receipt-id ID]'],
      ['dim', ''],
      ['ok', '🇪🇺  EUROPE  (Aiia)'],
      ['key', '  ofin eu auth token'],
      ['key', '  ofin eu providers list [--country DK] [--limit 25]'],
      ['key', '  ofin eu consent create --email you@example.com [--use-case-id ID] [--end-user-id ID]'],
      ['key', '  ofin eu consent get [--consent-id ID]'],
      ['key', '  ofin eu consent revoke [--consent-id ID] --yes'],
      ['key', '  ofin eu flow create [--consent-id ID] [--end-user-id ID] [--provider-id ID] [--open]'],
      ['key', '  ofin eu accounts list [--consent-id ID]'],
      ['key', '  ofin eu account get [--account-id ID] [--consent-id ID]'],
      ['key', '  ofin eu transactions list [--account-id ID] [--consent-id ID] [--from-date D] [--to-date D]'],
      ['key', '  ofin eu balance [--account-id ID] [--consent-id ID] [--max-age PT0S]'],
      ['key', '  ofin eu verify-ownership --customer-name "Jane Doe" [--account-ids a,b]'],
      ['dim', ''],
      ['dim', '30 operations · 3 regions · one consistent tool'],
    ] },
  ];

  function _sdkMakeBank() {
    const screen = document.getElementById('sdk-bank-screen');
    const urlEl = document.getElementById('sdk-bank-url');
    const wrap = document.getElementById('sdk-bank');
    let timers = [];
    function clear() { timers.forEach((t) => clearTimeout(t)); timers = []; }
    function wait(ms) { return new Promise((res) => { timers.push(setTimeout(res, ms)); }); }

    function reset(region) {
      clear();
      const b = SDK_BANKS[region] || SDK_BANKS.us;
      if (urlEl) urlEl.textContent = b.host;
      if (wrap) wrap.classList.remove('sdk-bank--live');
      if (screen) {
        screen.innerHTML =
          '<div class="sdk-bank-idle">' +
            '<div class="sdk-bank-idle-icon">🏦</div>' +
            '<p>Generate a Connect URL to launch the secure bank login</p>' +
          '</div>';
      }
    }

    async function launch(region) {
      const b = SDK_BANKS[region] || SDK_BANKS.us;
      if (!screen) return;
      clear();
      if (wrap) wrap.classList.add('sdk-bank--live');
      if (urlEl) urlEl.textContent = b.host + '/?session=' + Math.random().toString(16).slice(2, 8);

      // 1) loading spinner
      screen.innerHTML = '<div class="sdk-bank-loading"><span class="sdk-bank-spinner"></span><p>Connecting to ' + b.name + '…</p></div>';
      await wait(900);

      // 2) login form
      screen.innerHTML =
        '<div class="sdk-bank-login" style="--bank-accent:' + b.accent + ';">' +
          '<div class="sdk-bank-brand"><span class="sdk-bank-logo">' + b.initial + '</span><span class="sdk-bank-name">' + b.name + '</span></div>' +
          '<div class="sdk-bank-secure">🔒 Secured by Mastercard Open Banking</div>' +
          '<label class="sdk-bank-field"><span>Username</span><div class="sdk-bank-input" id="sdk-bank-user"></div></label>' +
          '<label class="sdk-bank-field"><span>Password</span><div class="sdk-bank-input" id="sdk-bank-pass"></div></label>' +
          '<button class="sdk-bank-btn" id="sdk-bank-btn">Log in</button>' +
        '</div>';
      await wait(420);

      const userEl = document.getElementById('sdk-bank-user');
      const passEl = document.getElementById('sdk-bank-pass');
      async function typeInto(el, text, mask) {
        if (!el) return;
        el.classList.add('typing');
        for (let i = 0; i < text.length; i++) {
          el.textContent = mask ? '•'.repeat(i + 1) : text.slice(0, i + 1);
          await wait(70 + Math.random() * 60);
        }
        el.classList.remove('typing');
      }
      await typeInto(userEl, 'demo.user', false);
      await wait(180);
      await typeInto(passEl, 'open-finance', true);
      await wait(360);

      // 3) submit → authorising
      const btn = document.getElementById('sdk-bank-btn');
      if (btn) btn.classList.add('pressed');
      await wait(500);
      screen.innerHTML = '<div class="sdk-bank-loading"><span class="sdk-bank-spinner"></span><p>Authorising access…</p></div>';
      await wait(1000);

      // 4) consent granted — success is always green (never the region accent)
      screen.innerHTML =
        '<div class="sdk-bank-done">' +
          '<div class="sdk-bank-check">✓</div>' +
          '<h4>Consent granted</h4>' +
          '<p>' + b.name + ' securely shared the selected accounts.</p>' +
          '<div class="sdk-bank-redirect">↩ returning to your app…</div>' +
        '</div>';
      await wait(900);
    }

    return { reset, launch, stop: clear };
  }

  function _sdkMakeDemo() {
    const body = document.getElementById('sdk-terminal-body');
    const bank = _sdkMakeBank();
    let region = 'us';
    let timers = [];
    let running = false;

    function clearTimers() { timers.forEach((t) => clearTimeout(t)); timers = []; }
    function wait(ms) { return new Promise((res) => { timers.push(setTimeout(res, ms)); }); }

    function addLine(cls, text) {
      const div = document.createElement('div');
      div.className = 'sdk-line ' + (cls ? 'sdk-line-' + cls : '');
      div.textContent = text;
      body.appendChild(div);
      body.scrollTop = body.scrollHeight;
      return div;
    }

    async function typeCmd(text) {
      const line = document.createElement('div');
      line.className = 'sdk-line';
      const prompt = document.createElement('span');
      prompt.className = 'sdk-line-prompt';
      prompt.innerHTML = '<span class="sdk-region-mark">' + region + '</span>:~$ ';
      const cmd = document.createElement('span');
      cmd.className = 'sdk-line-cmd';
      const caret = document.createElement('span');
      caret.className = 'sdk-caret';
      line.appendChild(prompt); line.appendChild(cmd); line.appendChild(caret);
      body.appendChild(line);
      body.scrollTop = body.scrollHeight;
      for (let i = 0; i < text.length; i++) {
        if (!running) return;
        cmd.textContent += text[i];
        await wait(28 + Math.random() * 40);
      }
      caret.remove();
    }

    async function run() {
      running = true;
      clearTimers();
      bank.stop();
      bank.reset(region);
      body.innerHTML = '';
      const script = SDK_SCRIPTS[region] || [];
      await wait(250);
      for (const step of script) {
        if (!running) return;
        await typeCmd(step.cmd);
        await wait(360);
        for (const ln of step.out) {
          if (!running) return;
          if (Array.isArray(ln)) addLine(ln[0], ln[1]);
          await wait(120);
        }
        if (step.bank && running) {
          await bank.launch(region);
        }
        if (!running) return;
        await wait(720);
      }
      // Final idle prompt with blinking caret.
      const line = document.createElement('div');
      line.className = 'sdk-line';
      line.innerHTML = '<span class="sdk-line-prompt"><span class="sdk-region-mark">' +
        region + '</span>:~$ </span><span class="sdk-caret"></span>';
      body.appendChild(line);
      body.scrollTop = body.scrollHeight;
      running = false;
    }

    return {
      setRegion(r) { if (SDK_SCRIPTS[r]) { region = r; this.replay(); } },
      replay() { running = false; clearTimers(); bank.stop(); requestAnimationFrame(() => run()); },
      stop() { running = false; clearTimers(); bank.stop(); },
    };
  }

  // Looping "watch it run" visualization for the SDK code section.
  function _sdkMakeRunViz() {
    const statusEl = document.getElementById('sdk-result-status');
    const bodyEl = document.getElementById('sdk-result-body');
    if (!statusEl || !bodyEl) return { start() {}, stop() {} };
    let timers = [];
    let running = false;
    function clear() { timers.forEach((t) => clearTimeout(t)); timers = []; }
    function wait(ms) { return new Promise((res) => { timers.push(setTimeout(res, ms)); }); }

    async function loop() {
      running = true;
      while (running) {
        statusEl.className = 'sdk-result-status';
        statusEl.textContent = 'idle';
        bodyEl.innerHTML = '<div class="sdk-result-row" style="color:var(--sdk-muted)">client.us.get_token() · au.get_token() · eu.get_token()</div>';
        await wait(950); if (!running) return;

        statusEl.className = 'sdk-result-status running';
        statusEl.textContent = 'running';
        bodyEl.innerHTML = '<div class="sdk-result-row"><span class="sdk-result-spinner"></span>authenticating across 3 continents…</div>';
        await wait(1150); if (!running) return;

        statusEl.className = 'sdk-result-status ok';
        statusEl.textContent = '200 ok';
        const rows = [
          '<span class="sdk-r-str">🇺🇸 us</span>  <span class="sdk-r-key">ok</span>=<span class="sdk-r-true">True</span>  <span class="sdk-r-key">status</span>=<span class="sdk-r-num">200</span>  <span class="sdk-r-str">"g3gT34fZtZ…"</span>',
          '<span class="sdk-r-str">🇦🇺 au</span>  <span class="sdk-r-key">ok</span>=<span class="sdk-r-true">True</span>  <span class="sdk-r-key">status</span>=<span class="sdk-r-num">200</span>  <span class="sdk-r-str">"q5HmLWuu7u…"</span>',
          '<span class="sdk-r-str">🇪🇺 eu</span>  <span class="sdk-r-key">ok</span>=<span class="sdk-r-true">True</span>  <span class="sdk-r-key">status</span>=<span class="sdk-r-num">200</span>  <span class="sdk-r-str">"eyJhbGciOiJS…"</span>',
          '',
          '<span class="sdk-r-key">→ one client, three continents, zero glue code</span>',
        ];
        bodyEl.innerHTML = '';
        rows.forEach((html, i) => {
          const d = document.createElement('div');
          d.className = 'sdk-result-row';
          d.style.animationDelay = (i * 60) + 'ms';
          d.innerHTML = html;
          bodyEl.appendChild(d);
        });
        await wait(3400); if (!running) return;
      }
    }
    return {
      start() { if (running) return; clear(); loop(); },
      stop() { running = false; clear(); },
    };
  }

  let _sdkInited = false;
  function _initSdkDemo() {
    // Reflect Open Finance config status on region chips + pins.
    const statusByRegion = {
      us: (APIS.find((a) => a.id === 'open_finance') || {}).configured,
      au: (APIS.find((a) => a.id === 'open_finance_au') || {}).configured,
      eu: (APIS.find((a) => a.id === 'open_finance_eu') || {}).configured,
    };
    Object.keys(statusByRegion).forEach((r) => {
      const chip = document.querySelector('[data-sdk-status="' + r + '"]');
      if (chip) {
        chip.classList.toggle('ok', !!statusByRegion[r]);
        chip.classList.toggle('off', !statusByRegion[r]);
        chip.title = statusByRegion[r] ? 'Configured' : 'Not configured';
      }
    });

    if (!window.__sdkDemo) window.__sdkDemo = _sdkMakeDemo();
    if (!_sdkInited) {
      _sdkInited = true;
      function setActiveRegion(r) {
        document.querySelectorAll('.sdk-cli-tab').forEach((t) =>
          t.classList.toggle('active', t.dataset.sdkRegion === r));
        if (window.__sdkGlobe) window.__sdkGlobe.setRegion(r);
        window.__sdkDemo.setRegion(r);
      }
      document.querySelectorAll('.sdk-cli-tab').forEach((el) => {
        el.addEventListener('click', () => setActiveRegion(el.dataset.sdkRegion));
      });
      // Region card API links → open that API in the APIs tab.
      document.querySelectorAll('[data-sdk-api]').forEach((el) => {
        el.addEventListener('click', (e) => {
          e.stopPropagation();
          const apisTab = document.querySelector('.top-tab[data-top-tab="apis"]');
          if (apisTab) apisTab.click();
          setTimeout(() => {
            const btn = document.querySelector(`[data-api-id="${el.dataset.sdkApi}"]`);
            if (btn) btn.click();
          }, 0);
        });
      });
      // Region card CLI links → scroll to the CLI section and focus that region.
      document.querySelectorAll('[data-sdk-cli]').forEach((el) => {
        el.addEventListener('click', (e) => {
          e.stopPropagation();
          setActiveRegion(el.dataset.sdkCli);
          const target = document.getElementById('sdk-cli');
          if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
      });
      const replay = document.getElementById('sdk-terminal-replay');
      if (replay) replay.addEventListener('click', () => window.__sdkDemo.replay());
      const codeRun = document.getElementById('sdk-code-run');
      if (codeRun) codeRun.addEventListener('click', () => {
        const original = '▶ Run Code';
        codeRun.disabled = true;
        codeRun.textContent = 'Launching…';
        codeRun.classList.remove('sdk-code-run--ok', 'sdk-code-run--err');
        _nativeFetch('/sdk/run', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({}),
        })
          .then((r) => r.json().then((d) => ({ ok: r.ok, d })))
          .then(({ ok, d }) => {
            codeRun.disabled = false;
            if (!ok || d.error) {
              codeRun.textContent = 'Failed';
              codeRun.classList.add('sdk-code-run--err');
              alert('Could not launch terminal: ' + (d.error || 'unknown error'));
            } else {
              codeRun.textContent = 'Launched ✓';
              codeRun.classList.add('sdk-code-run--ok');
            }
            setTimeout(() => {
              codeRun.textContent = original;
              codeRun.classList.remove('sdk-code-run--ok', 'sdk-code-run--err');
            }, 2400);
          })
          .catch((err) => {
            codeRun.disabled = false;
            codeRun.textContent = original;
            alert('Could not launch terminal: ' + (err && err.message || err));
          });
      });
      document.querySelectorAll('[data-sdk-scroll]').forEach((btn) => {
        btn.addEventListener('click', () => {
          const target = document.getElementById(btn.dataset.sdkScroll);
          if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
      });
    }
    const _initialTab = document.querySelector('.sdk-cli-tab.active');
    const _initialRegion = _initialTab ? _initialTab.dataset.sdkRegion : 'us';
    if (window.__sdkGlobe) window.__sdkGlobe.setRegion(_initialRegion);
    window.__sdkDemo.setRegion(_initialRegion);
    if (!window.__sdkRunViz) window.__sdkRunViz = _sdkMakeRunViz();
    window.__sdkRunViz.start();
  }

  // ---------------------------------------------------------------------
  // Live Demo — real Open Finance bank linking (admin + customer app)
  // ---------------------------------------------------------------------
  let _liveDemoInited = false;
  // Inline SVG flags — regional-indicator emoji don't render as flags on
  // Windows (they show as "US"/"AU"/"EU" letters), so we draw them ourselves.
  const LD_FLAG_SVG = {
    us: '<svg class="ld-flag-svg" viewBox="0 0 30 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
        '<rect width="30" height="20" fill="#fff"/>' +
        '<g fill="#b22234">' +
        '<rect width="30" height="1.54" y="0"/><rect width="30" height="1.54" y="3.08"/>' +
        '<rect width="30" height="1.54" y="6.15"/><rect width="30" height="1.54" y="9.23"/>' +
        '<rect width="30" height="1.54" y="12.31"/><rect width="30" height="1.54" y="15.38"/>' +
        '<rect width="30" height="1.54" y="18.46"/></g>' +
        '<rect width="13" height="10.77" fill="#3c3b6e"/>' +
        '<g fill="#fff">' +
        '<circle cx="2.2" cy="2" r="0.7"/><circle cx="5.2" cy="2" r="0.7"/><circle cx="8.2" cy="2" r="0.7"/><circle cx="11.2" cy="2" r="0.7"/>' +
        '<circle cx="3.7" cy="4" r="0.7"/><circle cx="6.7" cy="4" r="0.7"/><circle cx="9.7" cy="4" r="0.7"/>' +
        '<circle cx="2.2" cy="6" r="0.7"/><circle cx="5.2" cy="6" r="0.7"/><circle cx="8.2" cy="6" r="0.7"/><circle cx="11.2" cy="6" r="0.7"/>' +
        '<circle cx="3.7" cy="8" r="0.7"/><circle cx="6.7" cy="8" r="0.7"/><circle cx="9.7" cy="8" r="0.7"/></g>' +
        '</svg>',
    au: '<svg class="ld-flag-svg" viewBox="0 0 30 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
        '<rect width="30" height="20" fill="#00247d"/>' +
        '<g><path d="M0 0L12 8M12 0L0 8" stroke="#fff" stroke-width="1.8"/>' +
        '<path d="M0 0L12 8M12 0L0 8" stroke="#cf142b" stroke-width="0.8"/>' +
        '<rect x="5.1" width="1.8" height="8" fill="#fff"/><rect y="3.1" width="12" height="1.8" fill="#fff"/>' +
        '<rect x="5.5" width="1" height="8" fill="#cf142b"/><rect y="3.5" width="12" height="1" fill="#cf142b"/></g>' +
        '<g fill="#fff">' +
        '<circle cx="6" cy="14.5" r="1.6"/>' +
        '<circle cx="22" cy="4" r="0.9"/><circle cx="26" cy="8" r="0.9"/><circle cx="22" cy="12" r="0.9"/>' +
        '<circle cx="18.5" cy="8.5" r="0.7"/><circle cx="24" cy="16" r="0.8"/></g>' +
        '</svg>',
    eu: '<svg class="ld-flag-svg" viewBox="0 0 30 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
        '<rect width="30" height="20" fill="#003399"/>' +
        '<g fill="#ffcc00">' +
        '<circle cx="15" cy="4" r="1"/><circle cx="18" cy="4.8" r="1"/><circle cx="20.2" cy="7" r="1"/>' +
        '<circle cx="21" cy="10" r="1"/><circle cx="20.2" cy="13" r="1"/><circle cx="18" cy="15.2" r="1"/>' +
        '<circle cx="15" cy="16" r="1"/><circle cx="12" cy="15.2" r="1"/><circle cx="9.8" cy="13" r="1"/>' +
        '<circle cx="9" cy="10" r="1"/><circle cx="9.8" cy="7" r="1"/><circle cx="12" cy="4.8" r="1"/></g>' +
        '</svg>',
  };
  const LD_REGION_META = {
    us: { flag: LD_FLAG_SVG.us, name: 'United States', accent: '#eb001b' },
    au: { flag: LD_FLAG_SVG.au, name: 'Australia', accent: '#00843d' },
    eu: { flag: LD_FLAG_SVG.eu, name: 'Europe', accent: '#2d6cdf' },
  };
  const _ldPolls = {}; // region -> interval id
  const _ldExpanded = {}; // region -> Set of expanded account ids

  function _ldFmtMoney(amount, currency) {
    if (amount === null || amount === undefined || isNaN(amount)) return '—';
    const cur = (currency || '').toUpperCase();
    try {
      return new Intl.NumberFormat(undefined, {
        style: cur ? 'currency' : 'decimal', currency: cur || undefined,
        minimumFractionDigits: 2, maximumFractionDigits: 2,
      }).format(amount);
    } catch (e) {
      return (cur ? cur + ' ' : '') + Number(amount).toFixed(2);
    }
  }

  function _ldRenderConnection(region, conn, opts) {
    opts = opts || {};
    const meta = LD_REGION_META[region];
    const accounts = (conn && conn.accounts) || [];
    const txns = (conn && conn.transactions) || [];
    const connected = conn && conn.connected;
    const pending = opts.pending;
    let statusCls = 'ld-conn-status';
    let statusText;
    if (opts.error) { statusCls += ' ld-err'; statusText = opts.error; }
    else if (pending) { statusCls += ' ld-pending'; statusText = 'Waiting for bank login…'; }
    else if (connected) { statusCls += ' ld-ok'; statusText = 'Connected · ' + (conn.connected_at || ''); }
    else { statusText = 'Not connected'; }

    let actions = '';
    if (pending) {
      actions = `<button class="ld-btn" disabled><span class="ld-spinner"></span>Linking…</button>`;
    } else if (connected) {
      actions = `<div class="ld-conn-actions">
        <button class="ld-btn ld-btn--ghost" data-ld-refresh="${region}">Refresh data</button>
        <button class="ld-btn" data-ld-connect="${region}">Reconnect</button>
      </div>`;
    } else {
      actions = `<button class="ld-btn" data-ld-connect="${region}">Connect a bank</button>`;
    }

    let body = '';
    if (pending) {
      body = `<p class="ld-conn-hint"><span class="ld-spinner"></span>Complete the sandbox bank login in the new tab. We'll pull your accounts automatically.</p>`;
    } else if (connected && accounts.length) {
      const expanded = _ldExpanded[region] || (_ldExpanded[region] = new Set());
      const txnRow = (t) => {
        const amt = (t.amount === null || t.amount === undefined) ? null : Number(t.amount);
        const cls = amt === null ? '' : (amt < 0 ? 'ld-neg' : 'ld-pos');
        return `<div class="ld-txn">
          <span class="ld-txn-date">${escapeHtml(t.date || '')}</span>
          <span class="ld-txn-desc">${escapeHtml(t.description || '')}</span>
          <span class="ld-txn-amt ${cls}">${escapeHtml(_ldFmtMoney(t.amount, t.currency))}</span>
        </div>`;
      };
      // Bucket transactions by their owning account; anything we can't match
      // falls into an "Other" group so no data is ever dropped.
      const byAcct = {};
      const matchedIds = new Set(accounts.map((a) => String(a.id)));
      (txns || []).forEach((t) => {
        const k = (t.account_id !== undefined && t.account_id !== null && matchedIds.has(String(t.account_id)))
          ? String(t.account_id) : '__other__';
        (byAcct[k] = byAcct[k] || []).push(t);
      });
      const groupHtml = (key, headHtml, list) => {
        const isOpen = expanded.has(key);
        const inner = (list && list.length)
          ? `<div class="ld-txns">${list.slice(0, 25).map(txnRow).join('')}</div>`
          : `<p class="ld-empty-note">No transactions for this account.</p>`;
        const count = (list && list.length) ? list.length : 0;
        return `<div class="ld-acct-group${isOpen ? ' is-open' : ''}">
          <button type="button" class="ld-acct" data-ld-acct="${escapeHtml(key)}" aria-expanded="${isOpen ? 'true' : 'false'}">
            ${headHtml}
            <span class="ld-acct-toggle">
              <span class="ld-acct-count">${count}</span>
              <svg class="ld-acct-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
            </span>
          </button>
          <div class="ld-acct-txns">${inner}</div>
        </div>`;
      };
      const acctBlocks = accounts.map((a) => {
        const head = `<span class="ld-acct-info">
            <span class="ld-acct-name">${escapeHtml(a.name || 'Account')}</span>
            <span class="ld-acct-sub">${escapeHtml([a.type, a.mask].filter(Boolean).join(' · '))}</span>
          </span>
          <span class="ld-acct-bal">${escapeHtml(_ldFmtMoney(a.balance, a.currency))}<small>${escapeHtml((a.currency || '').toUpperCase())}</small></span>`;
        return groupHtml(String(a.id), head, byAcct[String(a.id)] || []);
      }).join('');
      let otherBlock = '';
      if ((byAcct.__other__ || []).length) {
        const head = `<span class="ld-acct-info">
            <span class="ld-acct-name">Other transactions</span>
            <span class="ld-acct-sub">Not linked to a listed account</span>
          </span>`;
        otherBlock = groupHtml('__other__', head, byAcct.__other__);
      }
      body = `<div class="ld-accts">${acctBlocks}${otherBlock}</div>`;
    } else if (opts.error) {
      body = `<p class="ld-conn-hint">${escapeHtml(opts.error)}</p>`;
    } else {
      body = `<p class="ld-conn-hint">Launch a secure sandbox bank login and we'll pull real account &amp; transaction data.</p>`;
    }

    return `<article class="ld-conn-card" data-ld-card="${region}" style="--ld-accent:${meta.accent};">
      <div class="ld-conn-head">
        <span class="ld-conn-flag">${meta.flag}</span>
        <div class="ld-conn-meta">
          <span class="ld-conn-name">${escapeHtml(meta.name)}</span>
          <span class="${statusCls}">${escapeHtml(statusText)}</span>
        </div>
        ${actions}
      </div>
      <div class="ld-conn-body">${body}</div>
    </article>`;
  }

  function _ldRenderApp(state) {
    const empty = document.getElementById('ld-app-empty');
    const cards = document.getElementById('ld-app-cards');
    if (!cards) return;
    const enabled = (state.regions || []).filter((r) => r.enabled);
    if (!enabled.length) {
      if (empty) empty.style.display = '';
      cards.innerHTML = '';
      return;
    }
    if (empty) empty.style.display = 'none';
    cards.innerHTML = enabled.map((r) =>
      _ldRenderConnection(r.region, r.connection, { pending: !!_ldPolls[r.region] })
    ).join('');
    _ldWireCards();
  }

  function _ldRenderAdmin(state) {
    const rows = document.getElementById('ld-admin-rows');
    if (!rows) return;
    rows.innerHTML = (state.regions || []).map((r) => {
      const meta = LD_REGION_META[r.region];
      const sub = r.configured
        ? (r.connection && r.connection.connected ? 'Bank connected' : 'Ready')
        : 'Credentials not configured';
      const subCls = r.configured ? 'ld-row-sub' : 'ld-row-sub ld-unconfigured';
      return `<div class="ld-admin-row" data-disabled="${r.configured ? 0 : 1}">
        <span class="ld-row-flag">${meta.flag}</span>
        <div class="ld-row-meta">
          <span class="ld-row-name">${escapeHtml(meta.name)}</span>
          <span class="${subCls}">${escapeHtml(sub)}</span>
        </div>
        <label class="ld-switch">
          <input type="checkbox" data-ld-toggle="${r.region}" ${r.enabled ? 'checked' : ''} ${r.configured ? '' : 'disabled'} />
          <span class="ld-switch-track"></span>
        </label>
      </div>`;
    }).join('');
    rows.querySelectorAll('[data-ld-toggle]').forEach((cb) => {
      cb.addEventListener('change', () => {
        const region = cb.dataset.ldToggle;
        cb.disabled = true;
        _nativeFetch('/live-demo/enable', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ region, enabled: cb.checked }),
        }).then((r) => r.json()).then((data) => {
          if (data && data.state) { _ldRenderAdmin(data.state); _ldRenderApp(data.state); }
        }).catch(() => { cb.checked = !cb.checked; })
          .finally(() => { cb.disabled = false; });
      });
    });
  }

  function _ldRefreshState() {
    return _nativeFetch('/live-demo/state').then((r) => r.json()).then((state) => {
      _ldRenderAdmin(state);
      _ldRenderApp(state);
      return state;
    });
  }

  function _ldStartPolling(region) {
    if (_ldPolls[region]) return;
    let tries = 0;
    const tick = () => {
      tries += 1;
      _nativeFetch('/live-demo/poll', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ region }),
      }).then((r) => r.json()).then((data) => {
        if (data && data.connected && data.connection) {
          _ldStopPolling(region);
          _ldRefreshState();
        } else if (tries >= 40) { // ~3 min at 4.5s
          _ldStopPolling(region);
          const card = document.querySelector(`[data-ld-card="${region}"]`);
          if (card) card.outerHTML = _ldRenderConnection(region, null,
            { error: 'Timed out waiting for bank login. Click Connect to retry.' });
          _ldWireCards();
        }
      }).catch(() => {});
    };
    _ldPolls[region] = setInterval(tick, 4500);
    tick();
  }

  function _ldStopPolling(region) {
    if (_ldPolls[region]) { clearInterval(_ldPolls[region]); delete _ldPolls[region]; }
  }

  function _ldConnect(region) {
    // Open the bank-login tab synchronously inside the click handler. The
    // flow URL only arrives after the async fetch below, but calling
    // window.open() from within a .then() callback is treated as a
    // non-user-initiated popup and gets blocked by the browser. Opening a
    // blank tab now (on the user gesture) and navigating it once the URL
    // returns avoids the popup blocker.
    let popup = window.open('', '_blank');
    if (popup) { try { popup.opener = null; } catch (e) {} }
    const card = document.querySelector(`[data-ld-card="${region}"]`);
    if (card) {
      card.outerHTML = _ldRenderConnection(region, null, { pending: true });
      _ldWireCards();
    }
    _nativeFetch('/live-demo/connect', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ region }),
    }).then((r) => r.json()).then((data) => {
      if (data && data.success && data.flow_url) {
        if (popup && !popup.closed) { popup.location.href = data.flow_url; }
        else { window.open(data.flow_url, '_blank', 'noopener'); }
        _ldStartPolling(region);
      } else {
        if (popup && !popup.closed) popup.close();
        const c = document.querySelector(`[data-ld-card="${region}"]`);
        if (c) c.outerHTML = _ldRenderConnection(region, null,
          { error: (data && data.error) || 'Could not start the bank connection.' });
        _ldWireCards();
      }
    }).catch(() => {
      if (popup && !popup.closed) popup.close();
      const c = document.querySelector(`[data-ld-card="${region}"]`);
      if (c) c.outerHTML = _ldRenderConnection(region, null, { error: 'Network error starting connection.' });
      _ldWireCards();
    });
  }

  function _ldRefreshData(region) {
    const btn = document.querySelector(`[data-ld-refresh="${region}"]`);
    if (btn) { btn.disabled = true; btn.textContent = 'Refreshing…'; }
    _nativeFetch('/live-demo/refresh', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ region }),
    }).then((r) => r.json()).then(() => _ldRefreshState())
      .catch(() => _ldRefreshState());
  }

  function _ldWireCards() {
    document.querySelectorAll('[data-ld-connect]').forEach((b) => {
      b.onclick = () => _ldConnect(b.dataset.ldConnect);
    });
    document.querySelectorAll('[data-ld-refresh]').forEach((b) => {
      b.onclick = () => _ldRefreshData(b.dataset.ldRefresh);
    });
    document.querySelectorAll('[data-ld-card]').forEach((card) => {
      const region = card.dataset.ldCard;
      const set = _ldExpanded[region] || (_ldExpanded[region] = new Set());
      card.querySelectorAll('[data-ld-acct]').forEach((btn) => {
        btn.onclick = () => {
          const key = btn.dataset.ldAcct;
          const group = btn.closest('.ld-acct-group');
          const open = !(group && group.classList.contains('is-open'));
          if (group) group.classList.toggle('is-open', open);
          btn.setAttribute('aria-expanded', open ? 'true' : 'false');
          if (open) set.add(key); else set.delete(key);
        };
      });
    });
  }

  function _initLiveDemo() {
    if (!document.getElementById('live-demo')) return;
    _ldRefreshState();
    if (_liveDemoInited) return;
    _liveDemoInited = true;
  }

export { _initSdkDemo, _initLiveDemo };
