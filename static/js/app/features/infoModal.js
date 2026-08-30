/* ====================== Info / How-to-run Modal ====================== */
(function () {
  var modal = document.getElementById('info-modal');
  if (!modal) return;

  var REPO = 'https://github.com/orancummins/vima';
  var SCRIPTS = {
    win: {
      title: 'PowerShell — Windows',
      prompt: 'PS C:\\>',
      copy: 'git clone ' + REPO + '\ncd vima\n.\\run.bat',
      steps: [
        { cmd: 'git clone ' + REPO, out: ["Cloning into 'vima'... done."] },
        { cmd: 'cd vima', out: [] },
        { cmd: '.\\run.bat', out: ['Creating virtual environment...', 'Installing dependencies...', 'Serving on http://localhost:9021'] }
      ]
    },
    nix: {
      title: 'bash — macOS / Linux',
      prompt: '$',
      copy: 'git clone ' + REPO + '\ncd vima\n./run.sh',
      steps: [
        { cmd: 'git clone ' + REPO, out: ["Cloning into 'vima'... done."] },
        { cmd: 'cd vima', out: [] },
        { cmd: './run.sh', out: ['Creating virtual environment...', 'Installing dependencies...', 'Serving on http://localhost:9021'] }
      ]
    }
  };

  var overlay = document.getElementById('info-overlay');
  var closeBtn = document.getElementById('info-close');
  var trigger = document.getElementById('info-trigger-btn');
  var pdfBtn = document.getElementById('info-pdf-btn');
  var termBody = document.getElementById('info-term-body');
  var termTitle = document.getElementById('info-term-title');
  var copyWin = document.getElementById('info-copy-win');
  var copyNix = document.getElementById('info-copy-nix');

  var platform = 'win';
  var timers = [];
  var running = false;

  function clearTimers() { timers.forEach(function (t) { clearTimeout(t); }); timers = []; }
  function wait(ms) { return new Promise(function (res) { timers.push(setTimeout(res, ms)); }); }

  function addLine(cls, text) {
    var div = document.createElement('div');
    div.className = 'info-term-line' + (cls ? ' ' + cls : '');
    div.textContent = text;
    termBody.appendChild(div);
    termBody.scrollTop = termBody.scrollHeight;
    return div;
  }

  function typeCmd(prompt, text) {
    var line = document.createElement('div');
    line.className = 'info-term-line';
    var p = document.createElement('span');
    p.className = 'info-term-prompt';
    p.textContent = prompt + ' ';
    var cmd = document.createElement('span');
    cmd.className = 'info-term-cmd';
    var caret = document.createElement('span');
    caret.className = 'info-term-caret';
    line.appendChild(p); line.appendChild(cmd); line.appendChild(caret);
    termBody.appendChild(line);
    termBody.scrollTop = termBody.scrollHeight;
    var i = 0;
    return (function step() {
      if (!running) { caret.remove(); return Promise.resolve(); }
      if (i >= text.length) { caret.remove(); return Promise.resolve(); }
      cmd.textContent += text[i++];
      termBody.scrollTop = termBody.scrollHeight;
      return wait(26 + Math.random() * 38).then(step);
    })();
  }

  async function run() {
    if (!termBody) return;
    running = true;
    clearTimers();
    termBody.innerHTML = '';
    var script = SCRIPTS[platform];
    if (termTitle) termTitle.textContent = script.title;
    await wait(260);
    for (var s = 0; s < script.steps.length; s++) {
      if (!running) return;
      var st = script.steps[s];
      await typeCmd(script.prompt, st.cmd);
      await wait(300);
      for (var o = 0; o < st.out.length; o++) {
        if (!running) return;
        addLine('info-term-out', st.out[o]);
        await wait(260);
      }
      await wait(420);
    }
    if (!running) return;
    var line = document.createElement('div');
    line.className = 'info-term-line';
    var p = document.createElement('span');
    p.className = 'info-term-prompt';
    p.textContent = script.prompt + ' ';
    var caret = document.createElement('span');
    caret.className = 'info-term-caret';
    line.appendChild(p); line.appendChild(caret);
    termBody.appendChild(line);
    termBody.scrollTop = termBody.scrollHeight;
    running = false;
  }

  function setPlatform(p) {
    if (!SCRIPTS[p]) return;
    platform = p;
    if (copyWin) copyWin.classList.toggle('is-active', p === 'win');
    if (copyNix) copyNix.classList.toggle('is-active', p === 'nix');
    running = false;
    clearTimers();
    requestAnimationFrame(run);
  }

  function flashCopied(btn, label) {
    var orig = btn.dataset.origLabel || btn.textContent;
    btn.dataset.origLabel = orig;
    btn.textContent = label;
    btn.classList.add('is-copied');
    setTimeout(function () {
      btn.classList.remove('is-copied');
      btn.textContent = btn.dataset.origLabel;
    }, 1500);
  }

  function copyFor(p, btn) {
    var text = SCRIPTS[p].copy;
    var done = function () { flashCopied(btn, '✓ Copied'); };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done).catch(done);
    } else {
      done();
    }
  }

  function open() {
    modal.classList.remove('info-hidden');
    document.body.style.overflow = 'hidden';
    setPlatform(platform);
  }
  function close() {
    modal.classList.add('info-hidden');
    document.body.style.overflow = '';
    running = false;
    clearTimers();
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function cmdBlock(script) {
    var rows = script.copy.split('\n').map(function (l) {
      return '<div class="cmd">' + esc(script.prompt) + ' ' + esc(l) + '</div>';
    }).join('');
    return '<div class="term"><div class="term-title">' + esc(script.title) + '</div>' + rows + '</div>';
  }

  function exportPdf() {
    var win = window.open('', '_blank');
    if (!win) return;
    var steps = [
      { n: 1, title: 'Sign up to Mastercard Developers',
        desc: "Create a free account at developer.mastercard.com/account/sign-up — you'll use it to generate the API keys that power every use case." },
      { n: 2, title: 'Install Git & Python',
        desc: "You'll need both on your machine. Get Git from git-scm.com/downloads and Python 3.9+ from python.org/downloads. Verify with <code>git --version</code> and <code>python --version</code>." },
      { n: 3, title: 'Clone the repo & run',
        desc: 'Pull the project and launch it — the run script sets up the virtual env and installs dependencies for you. The app opens at localhost:9021 once it boots.',
        extra: cmdBlock(SCRIPTS.win) + cmdBlock(SCRIPTS.nix) },
      { n: 4, title: 'Provision your API keys',
        desc: 'On first launch a welcome window appears. Choose <strong>Auto-provision Keys</strong> — a browser opens, you log in to Mastercard Developers, and Solution Studio creates the projects and downloads every key for you.' }
    ];
    var stepsHtml = steps.map(function (s) {
      return '<section class="step">' +
        '<div class="step-head"><span class="num">' + s.n + '</span><h2>' + esc(s.title) + '</h2></div>' +
        '<p>' + s.desc + '</p>' +
        (s.extra || '') +
        '</section>';
    }).join('');
    var html = '<!doctype html><html><head><meta charset="utf-8">' +
      '<title>Install & Run Solution Studio</title><style>' +
      '*{box-sizing:border-box}' +
      'body{font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#1a1a1a;margin:40px;line-height:1.55}' +
      'h1{font-size:24px;margin:0 0 4px}' +
      '.sub{color:#666;font-size:13px;margin:0 0 28px}' +
      '.step{margin:0 0 22px;padding-bottom:22px;border-bottom:1px solid #eee}' +
      '.step:last-child{border-bottom:none}' +
      '.step-head{display:flex;align-items:center;gap:10px;margin-bottom:6px}' +
      '.num{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;background:linear-gradient(180deg,#ffcb05,#f79e1b);color:#1a1300;font-weight:800;font-size:13px;flex:0 0 auto}' +
      '.step h2{font-size:16px;margin:0}' +
      '.step p{margin:0 0 10px;font-size:13.5px;color:#333}' +
      'code{font-family:Consolas,Menlo,monospace;background:#f2f2f2;padding:1px 5px;border-radius:4px;font-size:12.5px}' +
      '.term{background:#0f1116;border-radius:8px;padding:12px 14px;margin:8px 0}' +
      '.term-title{color:#9aa0aa;font-size:11px;margin-bottom:6px;font-family:Consolas,Menlo,monospace}' +
      '.term .cmd{color:#e6e6e6;font-family:Consolas,Menlo,monospace;font-size:12.5px;white-space:pre-wrap}' +
      '@media print{body{margin:24px}.step{page-break-inside:avoid}}' +
      '</style></head><body>' +
      '<h1>Install &amp; Run Solution Studio</h1>' +
      '<p class="sub">Four steps from zero to a fully-provisioned local instance.</p>' +
      stepsHtml +
      '</body></html>';
    win.document.open();
    win.document.write(html);
    win.document.close();
    win.focus();
    setTimeout(function () { win.print(); }, 300);
  }

  trigger && trigger.addEventListener('click', open);
  closeBtn && closeBtn.addEventListener('click', close);
  overlay && overlay.addEventListener('click', close);
  pdfBtn && pdfBtn.addEventListener('click', exportPdf);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !modal.classList.contains('info-hidden')) close();
  });

  copyWin && copyWin.addEventListener('click', function () {
    if (platform !== 'win') setPlatform('win');
    copyFor('win', copyWin);
  });
  copyNix && copyNix.addEventListener('click', function () {
    if (platform !== 'nix') setPlatform('nix');
    copyFor('nix', copyNix);
  });
})();
