/* ====================== Info / How-to-run Modal ====================== */
(function () {
  var modal = document.getElementById('info-modal');
  if (!modal) return;

  var REPO = 'https://github.com/orancummins/vima';
  var SCRIPTS = {
    win: {
      title: 'PowerShell ÔÇö Windows',
      prompt: 'PS C:\\>',
      copy: 'git clone ' + REPO + '\ncd vima\n.\\run.bat',
      steps: [
        { cmd: 'git clone ' + REPO, out: ["Cloning into 'vima'... done."] },
        { cmd: 'cd vima', out: [] },
        { cmd: '.\\run.bat', out: ['Creating virtual environment...', 'Installing dependencies...', 'Serving on http://localhost:9021'] }
      ]
    },
    nix: {
      title: 'bash ÔÇö macOS / Linux',
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
    var done = function () { flashCopied(btn, 'Ô£ô Copied'); };
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

  trigger && trigger.addEventListener('click', open);
  closeBtn && closeBtn.addEventListener('click', close);
  overlay && overlay.addEventListener('click', close);
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
