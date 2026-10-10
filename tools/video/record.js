// -------------------------------------------------------------------
// tools/video/record.js
// Films Mastercard Solution Studio for the walkthrough video.
//
// Drives a running Solution Studio (and Find A Card, which it embeds) with
// Playwright in real time, 1600×900 CSS pixels at 1.2× so the picture is a
// sharp 1920×1080. Every action is scheduled from out/timeline.json
// (written by tts.py), so the picture follows the narration.
//
// Frames come from Chrome's own screencast (CDP Page.startScreencast), each
// stamped with the wall-clock time it was drawn, and are saved to
// out/frames/ with an index in out/frames.json. build.py lays them on the
// narration's clock exactly. (Playwright's recordVideo drifts unevenly by
// a second or two over a few minutes, which is too much for narration.)
//
// Usage:
//   NODE_PATH=$(npm root -g) node tools/video/record.js [--base http://localhost:9021] [--headed]
//
// Needs Solution Studio on --base and Find A Card on port 5432 (the Find A
// Card use case must show the app, not "Service not running"). Nothing here
// provisions keys: the provisioning dialog is opened and closed, never run.
// -------------------------------------------------------------------
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const args = process.argv.slice(2);
const opt = (name, dflt) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : dflt; };
const BASE = opt('--base', 'http://localhost:9021').replace(/\/$/, '');
const OUT = path.resolve(opt('--out', path.join(__dirname, 'out')));
const HEADED = args.includes('--headed');

const TL = JSON.parse(fs.readFileSync(path.join(OUT, 'timeline.json'), 'utf8'));
const LINES = {};
TL.sections.forEach((s) => Object.assign(LINES, s.lines));
const S = (id) => { if (!LINES[id]) throw new Error('no line ' + id); return LINES[id].start; };
const E = (id) => LINES[id].end;
const SEC = (id) => TL.sections.find((s) => s.id === id);

const OVERLAY = `(() => {
  if (window.top !== window || document.getElementById('__cursor')) return;
  const css = document.createElement('style');
  css.textContent = \`
    #__cursor{position:fixed;left:0;top:0;width:26px;height:26px;z-index:2147483647;pointer-events:none;
      transform:translate(-100px,-100px);transition-property:transform,opacity;transition-timing-function:cubic-bezier(.45,.05,.25,1);opacity:0}
    #__cursor svg{display:block;filter:drop-shadow(0 2px 3px rgba(0,0,0,.45))}
    .__ripple{position:fixed;width:34px;height:34px;margin:-17px 0 0 -17px;border-radius:50%;pointer-events:none;
      z-index:2147483646;border:2px solid #ff7a1a;box-shadow:0 0 14px rgba(255,95,0,.7);animation:__rip .6s ease-out forwards}
    @keyframes __rip{from{transform:scale(.3);opacity:1}to{transform:scale(1.5);opacity:0}}\`;
  document.documentElement.appendChild(css);
  const c = document.createElement('div');
  c.id = '__cursor';
  c.innerHTML = '<svg width="26" height="26" viewBox="0 0 26 26"><path d="M4 2.5v19.2l5.1-4.7 3.3 7.4 3.3-1.5-3.3-7.3 7-.3z" fill="#fff" stroke="#111" stroke-width="1.4" stroke-linejoin="round"/></svg>';
  document.documentElement.appendChild(c);
})();`;

(async () => {
  const FRAMES = path.join(OUT, 'frames');
  fs.rmSync(FRAMES, { recursive: true, force: true });
  fs.mkdirSync(FRAMES, { recursive: true });
  const browser = await chromium.launch({ headless: !HEADED });
  const ctx = await browser.newContext({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 1.2 });
  await ctx.addInitScript(() => { try { localStorage.setItem('vima:theme', 'dark'); } catch (e) {} });
  const page = await ctx.newPage();
  const log = (...a) => console.log(((Date.now() - (t0 || Date.now())) / 1000).toFixed(2).padStart(7), ...a);
  let t0 = 0;
  const cur = { x: 800, y: 600, shown: false };

  // ---------- helpers ----------
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  async function at(t) {
    const wait = t0 + t * 1000 - Date.now();
    if (wait > 0) await sleep(wait);
    else if (wait < -400) log(`  ↳ running ${(-wait / 1000).toFixed(1)} s behind the narration`);
  }
  function mark(id) { log('section', id); }
  async function cursor(x, y, dur = 0.7, show = true) {
    cur.x = x; cur.y = y;
    await page.evaluate(({ x, y, dur, show }) => {
      const c = document.getElementById('__cursor');
      c.style.transitionDuration = dur + 's,.3s';
      c.style.opacity = show ? '1' : '0';
      c.style.transform = `translate(${x - 4}px,${y - 2}px)`;
    }, { x, y, dur, show });
    await page.mouse.move(x, y, { steps: Math.max(2, Math.round(dur * 20)) });
  }
  async function hideCursor() {
    await page.evaluate(() => { const c = document.getElementById('__cursor'); c.style.opacity = '0'; });
  }
  async function centre(loc, dx = 0.5, dy = 0.5) {
    await loc.first().waitFor({ state: 'visible', timeout: 8000 });
    await loc.first().scrollIntoViewIfNeeded({ timeout: 3000 }).catch(() => {});
    const b = await loc.first().boundingBox();
    return { x: b.x + b.width * dx, y: b.y + b.height * dy };
  }
  // A step that fails is logged and skipped, so one bad selector doesn't lose the take.
  const failures = [];
  const safe = (name, fn) => async (...a) => {
    try { return await fn(...a); } catch (e) {
      failures.push(name + ': ' + String(e.message || e).split('\n')[0]);
      log('  ✗', failures[failures.length - 1]);
    }
  };
  // Glide the cursor to an element and click it: in the top page or inside any iframe.
  const click = safe('click', async (loc, { dur = 0.7, dx = 0.5, dy = 0.5 } = {}) => {
    const p = await centre(loc, dx, dy);
    await cursor(p.x, p.y, dur);
    await sleep(dur * 1000 + 60);
    await page.evaluate(({ x, y }) => {
      const r = document.createElement('div');
      r.className = '__ripple'; r.style.left = x + 'px'; r.style.top = y + 'px';
      document.documentElement.appendChild(r); setTimeout(() => r.remove(), 700);
    }, p);
    await page.mouse.click(p.x, p.y);
  });
  const hover = safe('hover', async (loc, dur = 0.7) => { const p = await centre(loc); await cursor(p.x, p.y, dur); });
  async function smoothScroll(frameOrPage, selector, to) {
    await frameOrPage.evaluate(({ selector, to }) => {
      const el = selector ? document.querySelector(selector) : document.scrollingElement;
      if (!el) return;
      const top = typeof to === 'number' ? to : (() => {
        const t = [...el.querySelectorAll(to.sel)].find((x) => new RegExp(to.text).test(x.textContent));
        return t ? el.scrollTop + t.getBoundingClientRect().top - el.getBoundingClientRect().top - (to.offset || 24) : el.scrollTop;
      })();
      el.scrollTo({ top, behavior: 'smooth' });
    }, { selector, to });
  }
  const tab = (id) => page.locator(`.top-tab[data-top-tab="${id}"]`);
  const os = page.frameLocator('#os-frame');
  const fac = page.frameLocator('#findacard-webview-frame').frameLocator('iframe.fac-frame');
  const facFrame = () => page.frames().find((f) => f.url().startsWith('http://localhost:5432') || f.url().includes(':5432/'));
  const osFrame = () => page.frames().find((f) => f.url().includes('/mcos/'));

  // ---------- warm-up (cut from the final video) ----------
  console.log('warm-up: loading', BASE);
  await page.goto(BASE + '/app', { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
  await page.evaluate(OVERLAY);   // cursor and click ripple, on the top page only
  const skip = page.locator('#prov-modal:not(.prov-hidden) #prov-btn-skip');
  if (await skip.count()) await skip.click();
  // Load Find A Card once, so its frame is cached and ready.
  await tab('usecases').click();
  await page.locator('[data-uc-id="findacard"]').click();
  await fac.locator('#panel1').waitFor({ state: 'visible', timeout: 20000 }).catch(() => {
    throw new Error('Find A Card is not showing: start it on port 5432 first.');
  });
  // Load the Operating System picture and hold it on the spinning globe.
  await tab('os').click();
  await os.locator('#svg').waitFor({ timeout: 20000 });
  await sleep(500);
  await osFrame().evaluate(() => {
    if (!window.__held) {
      const orig = window.runIntro;
      window.__hold = true;
      window.runIntro = function (to, done) { if (window.__hold && to === 1) return undefined; return orig(to, done); };
      window.__held = true;
    }
    cancelAnimationFrame(iraf); iraf = 0; st.p = 0; applyIntro();
  });
  await tab('home').click();
  await page.evaluate(() => document.querySelectorAll('.top-tab').forEach((b) => b.blur()));
  await page.mouse.move(1598, 898);   // out of the way, so nothing shows a hover tooltip

  // ---------- screencast ----------
  const cdp = await ctx.newCDPSession(page);
  const frames = [];
  const writes = [];
  cdp.on('Page.screencastFrame', (f) => {
    const file = String(frames.length).padStart(6, '0') + '.jpg';
    frames.push({ file, ts: f.metadata.timestamp });
    writes.push(fs.promises.writeFile(path.join(FRAMES, file), Buffer.from(f.data, 'base64')));
    cdp.send('Page.screencastFrameAck', { sessionId: f.sessionId }).catch(() => {});
  });
  await cdp.send('Page.startScreencast', { format: 'jpeg', quality: 92, maxWidth: 1920, maxHeight: 1080, everyNthFrame: 1 });
  await sleep(2500);

  // ---------- the take ----------
  t0 = Date.now();
  mark('start');

  // 1 · Mastercard's mission — the Home screen.
  await at(SEC('s1_mission').start); mark('s1_mission');

  // 2 · More than a card network — the Operating System globe, then the stack.
  await at(SEC('s2_studio').start); mark('s2_studio');
  await cursor(1180, 520, 0.01, false);
  await at(S('o1') + 0.5); await click(tab('os'), { dur: 0.9 });
  await at(S('o2') + 0.4); await cursor(560, 520, 1.2);
  await at(S('o6') + 0.1);
  await osFrame().evaluate(() => { window.__hold = false; runIntro(1); });
  await hideCursor();

  // 3 · The operating system — open the stack, the kernel, BIN Lookup.
  await at(SEC('s3_os').start); mark('s3_os');
  await at(S('a1') + 0.4); await click(os.locator('.layer[data-l="L3"]'), { dur: 0.8 });
  await at(S('a2') + 0.3); await click(os.locator('#side .row[data-go="L1"]'));
  await at(S('a2') + 3.2); await hover(os.locator('.blk.studio[data-t="1.3"]'), 0.8);
  await at(S('a3') + 0.5); await click(os.locator('#side .tile[data-t="1.3"]'));
  await at(S('a3') + 2.4); await click(os.locator('.prod[data-p="binlookup"] > button'));
  await at(S('a4') + 0.5); await click(os.locator('.prod[data-p="binlookup"] .mcos-link--api'));

  // 4 · A live API — BIN Lookup in the workbench.
  await at(SEC('s4_api').start); mark('s4_api');
  await at(S('p1') + 1.2); await hover(page.locator('#api-title'), 0.8);
  await at(S('p2') + 0.1); await click(page.locator('#op-categories .op-btn').first(), { dur: 0.6 });
  await at(S('p2') + 1.3); await click(page.locator('#op-send'), { dur: 0.6 });
  await at(S('p3') + 1.0); await hover(page.locator('#resp-body'), 0.9);
  await at(S('p4') + 0.6); await click(page.locator('#apis-snippets-fab'), { dur: 0.8 });

  // 5 · API bundles — Merchant resolution.
  await at(SEC('s5_bundles').start); mark('s5_bundles');
  await at(S('b1') + 0.1); await click(page.locator('#apis-snippets-close'), { dur: 0.5 });
  await at(S('b1') + 1.0); await click(tab('bundles'));
  await at(S('b1') + 2.8); await click(page.locator('.bundle-sidebar-item[data-bundle-id="merchant_resolution"]'));
  await at(S('b2') + 1.0); await hover(page.locator('.bundle-detail-title'), 1.0);
  await at(S('b4') + 0.2);
  await smoothScroll(page, '.bundles-content', { sel: '.bundle-section-title', text: 'fit together', offset: 30 });
  await at(S('b4') + 1.8); await cursor(900, 520, 0.9);

  // 6 · Find A Card — the agent, Open Finance and the spend profile.
  await at(SEC('s6_findacard').start); mark('s6_findacard');
  await at(S('f1') + 0.4); await click(tab('usecases'));
  await at(S('f1') + 2.4); await click(page.locator('[data-uc-id="findacard"]'));
  // Find A Card's bank connection takes about ten seconds, so the request is
  // typed as the agent is introduced and the connection starts early: the
  // spend profile then lands as the narration describes it.
  await at(S('f2') + 2.2); await click(fac.locator('#userDescribe'), { dur: 0.6 });
  await fac.locator('#userDescribe').pressSequentially('Travel rewards, no foreign fees, and I want it now.', { delay: 16 });
  await at(S('f3') + 0.3); await click(fac.locator('#panel1 .btn-primary'), { dur: 0.45 });
  await at(S('f3') + 1.4);
  await click(fac.locator('#panel2 button', { hasText: 'Connect To Bank' }), { dur: 0.5 });
  await at(S('f6') + 1.6); await click(fac.locator('#panel3 .btn-primary'), { dur: 0.6 });
  await at(S('f6') + 2.9); await click(fac.locator('#btnSearch'), { dur: 0.5 });
  await at(S('f7') + 0.4);
  const ff = facFrame();
  if (ff) await smoothScroll(ff, null, 160);
  await at(S('f7') + 1.2); await hover(fac.locator('#resultsGrid > *').first(), 0.9);

  // 7 · Open to everyone, easy to set up — the info guide, then auto-provisioning.
  await at(SEC('s7_open').start); mark('s7_open');
  await at(S('e1') + 0.4); await click(page.locator('#info-trigger-btn'));
  await at(S('e2') + 0.6); await smoothScroll(page, '.info-panel-body', 380);
  await at(S('e2') + 3.2); await smoothScroll(page, '.info-panel-body', 760);
  await at(S('e3') - 0.3); await click(page.locator('#info-close'), { dur: 0.5 });
  await at(S('e3') + 0.6);
  await page.evaluate(() => {
    // The welcome dialog Solution Studio shows on first run.
    const m = document.getElementById('prov-modal');
    ['prov-screen-welcome', 'prov-screen-select', 'prov-screen-progress'].forEach((id) => {
      const s = document.getElementById(id); if (s) s.classList.toggle('prov-hidden', id !== 'prov-screen-welcome');
    });
    m.classList.remove('prov-hidden');
  });
  await at(S('e4') + 0.6); await click(page.locator('#prov-btn-auto'), { dur: 0.8 });
  await at(S('e4') + 3.2); await hover(page.locator('#prov-api-grid .prov-api-item').nth(4), 0.9);
  await at(S('e5') + 0.4); await hover(page.locator('#prov-btn-start'), 0.8);   // hovered, never clicked
  await at(S('e5') + 2.0);
  await page.evaluate(() => { document.getElementById('prov-modal').classList.add('prov-hidden'); document.body.style.overflow = ''; });
  await at(S('e5') + 2.2); await click(tab('home'), { dur: 0.6 });

  // 8 · Close — Home.
  await at(SEC('s8_close').start); mark('s8_close');
  await at(S('c1') + 0.8); await hideCursor();

  await at(TL.total); mark('end');
  await sleep(500);

  await cdp.send('Page.stopScreencast').catch(() => {});
  await Promise.all(writes);
  fs.writeFileSync(path.join(OUT, 'frames.json'), JSON.stringify({ t0: t0 / 1000, total: TL.total, frames }));
  console.log(`recorded ${frames.length} frames to ${FRAMES}`);
  await ctx.close();
  if (failures.length) console.log(`${failures.length} step(s) failed:\n  ` + failures.join('\n  '));
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
