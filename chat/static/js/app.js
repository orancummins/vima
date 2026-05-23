/* ─── State ─────────────────────────────────────────────────────────── */
let sessionId = crypto.randomUUID();
let isStreaming = false;
let currentFile = null;

/* ─── DOM refs ──────────────────────────────────────────────────────── */
const messagesEl  = document.getElementById('messages');
const chatInputEl = document.getElementById('chat-input');
const sendBtn     = document.getElementById('send-btn');
const clearBtn    = document.getElementById('clear-btn');
const statusBar   = document.getElementById('chat-status-bar');

/* ─── Status bar ────────────────────────────────────────────────────── */
let _statusTimer = null;
function setStatus(state, text) {
  clearTimeout(_statusTimer);
  statusBar.className = 'chat-status-bar' + (state ? ' ' + state : '');
  if (state === 'working') {
    statusBar.innerHTML = `<div class="status-dot"></div><span class="status-text">${escHtml(text || 'Agent is working\u2026')}</span>`;
  } else if (state === 'done') {
    statusBar.innerHTML = '<div class="status-dot"></div><span class="status-text">Done</span>';
    _statusTimer = setTimeout(() => setStatus(''), 2000);
  } else {
    statusBar.innerHTML = '';
  }
}

/* ─── Tab switching ─────────────────────────────────────────────────── */
document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    const name = tab.dataset.tab;
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById(`tab-${name}`).classList.add('active');
    if (name === 'files')    loadFileTree();
    if (name === 'settings') loadSettings();
  });
});

/* ─── Utilities ─────────────────────────────────────────────────────── */
function escHtml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

/** Very light Markdown → HTML (code blocks, inline code, bold, headings, bullets) */
function renderMd(raw) {
  let s = escHtml(raw);

  // fenced code blocks
  s = s.replace(/```[\w]*\n?([\s\S]*?)```/g, (_, code) =>
    `<pre><code>${code.trim()}</code></pre>`);

  // inline code
  s = s.replace(/`([^`\n]+)`/g, (_, c) => `<code>${c}</code>`);

  // bold
  s = s.replace(/\*\*([^*\n]+)\*\*/g, '<strong>$1</strong>');

  // italic
  s = s.replace(/\*([^*\n]+)\*/g, '<em>$1</em>');

  // headings (## and ###)
  s = s.replace(/^### (.+)$/gm, '<h4>$1</h4>');
  s = s.replace(/^## (.+)$/gm,  '<h3>$1</h3>');
  s = s.replace(/^# (.+)$/gm,   '<h2>$1</h2>');

  // bullet lists
  s = s.replace(/^[*-] (.+)$/gm, '<li>$1</li>');
  s = s.replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>');

  // paragraph line breaks (two newlines = new para, one = <br>)
  s = s.replace(/\n{2,}/g, '</p><p>');
  s = s.replace(/\n/g, '<br>');
  s = `<p>${s}</p>`;

  // clean up empty paragraphs
  s = s.replace(/<p><\/p>/g, '');
  return s;
}

function scrollBottom() {
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function refreshPreview() {
  const f = document.getElementById('preview-frame');
  if (f) f.src = f.src;
}

/* ─── Chat: adding elements ─────────────────────────────────────────── */
function addUserBubble(text) {
  const el = document.createElement('div');
  el.className = 'message user';
  el.innerHTML = `<div class="message-label">You</div>
    <div class="message-bubble">${escHtml(text)}</div>`;
  messagesEl.appendChild(el);
  scrollBottom();
}

function createAssistantBubble() {
  const el = document.createElement('div');
  el.className = 'message assistant';
  el.innerHTML = `<div class="message-label">Claude</div>
    <div class="message-bubble"></div>`;
  messagesEl.appendChild(el);
  scrollBottom();
  return el.querySelector('.message-bubble');
}

function addStreamingDots() {
  setStatus('working', 'Claude is thinking\u2026');
}

function removeStreamingDots() {
  // status bar now handles working state; called for compatibility
}

function addToolEvent(kind, name, payload) {
  const el = document.createElement('div');
  el.className = `tool-event ${kind}`;

  let icon, label;
  if (kind === 'executing') { icon = '⚙️'; label = `Calling: ${name}`; }
  else if (kind === 'result') { icon = '✓'; label = `${name} returned`; }
  else { icon = '✗'; label = `Error in ${name}`; }

  let preview = '';
  if (payload && Object.keys(payload).length) {
    const raw = JSON.stringify(payload, null, 2);
    preview = `<pre>${escHtml(raw.length > 400 ? raw.slice(0, 400) + '\n…' : raw)}</pre>`;
  }

  el.innerHTML = `<div class="tool-event-header">${icon} ${escHtml(label)}</div>${preview}`;
  messagesEl.appendChild(el);
  scrollBottom();
}

/* ─── Chat: send ────────────────────────────────────────────────────── */
async function sendMessage() {
  const text = chatInputEl.value.trim();
  if (!text || isStreaming) return;

  // remove welcome card on first message
  messagesEl.querySelector('.welcome-card')?.remove();

  chatInputEl.value = '';
  isStreaming = true;
  sendBtn.disabled = true;

  addStreamingDots();

  let assistantBubble = null;
  let assistantText   = '';

  try {
    const resp = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ session_id: sessionId, message: text }),
    });

    if (!resp.ok) {
      const err = await resp.json().catch(() => ({ error: resp.statusText }));
      throw new Error(err.error || `HTTP ${resp.status}`);
    }

    const reader  = resp.body.getReader();
    const decoder = new TextDecoder();
    let   buffer  = '';

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const parts = buffer.split('\n\n');
      buffer = parts.pop();                     // keep incomplete chunk

      for (const chunk of parts) {
        for (const line of chunk.split('\n')) {
          if (!line.startsWith('data: ')) continue;
          let data;
          try { data = JSON.parse(line.slice(6)); } catch { continue; }

          switch (data.type) {

            case 'text':
              removeStreamingDots();
              if (!assistantBubble) assistantBubble = createAssistantBubble();
              assistantText += data.content;
              assistantBubble.innerHTML = renderMd(assistantText);
              scrollBottom();
              break;

            case 'tool_executing':
              setStatus('working', `Using tool: ${data.name}`);
              addToolEvent('executing', data.name, data.input);
              break;

            case 'tool_result':
              addToolEvent('result', data.name, data.result);
              setStatus('working', 'Claude is thinking\u2026');
              break;

            case 'error':
              setStatus('');
              addToolEvent('error', 'Error', { message: data.message });
              break;

            case 'done':
              setStatus('done');
              refreshPreview();
              // Reload file editor if a file is open (Claude may have changed it)
              if (currentFile) loadFile(currentFile, null, true);
              break;
          }
        }
      }
    }

  } catch (err) {
    setStatus('');
    addToolEvent('error', 'Network / API error', { message: err.message });
  } finally {
    isStreaming = false;
    sendBtn.disabled = false;
    scrollBottom();
  }
}

chatInputEl.addEventListener('keydown', e => {
  if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
});
sendBtn.addEventListener('click', sendMessage);

clearBtn.addEventListener('click', async () => {
  await fetch('/api/chat/clear', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ session_id: sessionId }),
  });
  sessionId = crypto.randomUUID();
  messagesEl.innerHTML = `<div class="welcome-card">
    <h2>Chat cleared</h2><p>Starting a fresh conversation.</p></div>`;
});

/* ─── Files tab ─────────────────────────────────────────────────────── */
function fileIcon(name) {
  const ext = name.split('.').pop().toLowerCase();
  return { html:'🌐', css:'🎨', js:'⚡', ts:'🔷', py:'🐍',
           json:'📋', md:'📝', txt:'📄', sh:'🖥',
           jpg:'🖼', jpeg:'🖼', png:'🖼', gif:'🖼', svg:'🖼' }[ext] || '📄';
}

async function loadFileTree() {
  const tree = document.getElementById('file-tree');
  tree.innerHTML = '<div style="padding:12px;color:var(--text2)">Loading…</div>';
  try {
    const data = await fetch('/api/files').then(r => r.json());
    if (data.error) { tree.innerHTML = `<div style="padding:12px;color:var(--red)">${escHtml(data.error)}</div>`; return; }

    tree.innerHTML = '';
    for (const item of data.items) {
      const el = document.createElement('div');
      if (item.type === 'directory') {
        el.className = 'file-item dir-item';
        el.innerHTML = `<span class="file-icon">📁</span><span>${escHtml(item.name)}</span>`;
      } else {
        el.className = 'file-item';
        el.dataset.path = item.path || item.name;
        el.innerHTML = `<span class="file-icon">${fileIcon(item.name)}</span><span>${escHtml(item.name)}</span>`;
        el.addEventListener('click', () => loadFile(el.dataset.path, el));
      }
      tree.appendChild(el);
    }
  } catch (e) {
    tree.innerHTML = `<div style="padding:12px;color:var(--red)">Error: ${escHtml(e.message)}</div>`;
  }
}

async function loadFile(path, itemEl, silent = false) {
  if (!silent) {
    document.querySelectorAll('.file-item').forEach(el => el.classList.remove('active'));
    itemEl?.classList.add('active');
    currentFile = path;
  }

  const editorEl   = document.getElementById('code-editor');
  const filenameEl = document.getElementById('editor-filename');
  const saveBtnEl  = document.getElementById('save-file-btn');

  filenameEl.textContent = path;

  try {
    const data = await fetch(`/api/files/read?path=${encodeURIComponent(path)}`).then(r => r.json());
    if (data.error) { if (!silent) { editorEl.value = `Error: ${data.error}`; editorEl.disabled = true; } return; }
    editorEl.value    = data.content;
    editorEl.disabled = false;
    saveBtnEl.style.display = 'block';
  } catch (e) {
    if (!silent) editorEl.value = `Error: ${e.message}`;
  }
}

document.getElementById('save-file-btn').addEventListener('click', async () => {
  if (!currentFile) return;
  const content = document.getElementById('code-editor').value;
  const btn = document.getElementById('save-file-btn');
  try {
    const data = await fetch('/api/files/write', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ path: currentFile, content }),
    }).then(r => r.json());

    if (data.success) {
      const orig = btn.textContent;
      btn.textContent = '✓ Saved';
      btn.style.cssText = 'background:var(--green);color:var(--bg)';
      refreshPreview();
      setTimeout(() => { btn.textContent = orig; btn.style.cssText = ''; }, 1600);
    } else {
      alert(`Save failed: ${data.error}`);
    }
  } catch (e) { alert(`Save failed: ${e.message}`); }
});

document.getElementById('refresh-files').addEventListener('click', loadFileTree);

/* ─── Preview tab ───────────────────────────────────────────────────── */
document.getElementById('refresh-preview').addEventListener('click', refreshPreview);

/* ─── Settings tab ──────────────────────────────────────────────────── */
async function loadSettings() {
  try {
    const cfg = await fetch('/api/config').then(r => r.json());
    document.getElementById('allowed-commands').value = cfg.allowed_commands.join('\n');
  } catch (e) { console.error('Failed to load settings', e); }
}

document.getElementById('save-commands-btn').addEventListener('click', async () => {
  const raw = document.getElementById('allowed-commands').value;
  const commands = raw.split('\n').map(s => s.trim()).filter(Boolean);
  const statusEl = document.getElementById('commands-status');

  try {
    const data = await fetch('/api/config/commands', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ commands }),
    }).then(r => r.json());

    if (data.success) {
      statusEl.textContent = '✓ Saved';
      statusEl.className = 'status-msg success';
    } else {
      statusEl.textContent = `Error: ${data.error}`;
      statusEl.className = 'status-msg error';
    }
  } catch (e) {
    statusEl.textContent = `Error: ${e.message}`;
    statusEl.className = 'status-msg error';
  }
  setTimeout(() => { statusEl.textContent = ''; statusEl.className = 'status-msg'; }, 3000);
});
