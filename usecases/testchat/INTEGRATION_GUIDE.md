# Test Chat - Tab Implementation Guide

This guide describes how to add the "Test 2" tab to the Test Chat use case.

## Changes Required

### 1. Update `static/js/app.js`

Find the `renderTestChat()` function (around line 7300) and replace it with:

```javascript
// ===================== Test Chat Use Case =====================
// Clean chat interface with a revolving Mastercard globe.
// Globe rendering is ported from globe_preview.html as pure vanilla canvas.

let _testChatAnimRef = null;
let TEST_CHAT_TAB = "globe"; // "globe" | "test2"

function renderTestChat() {
  if (_testChatAnimRef) {
    cancelAnimationFrame(_testChatAnimRef);
    _testChatAnimRef = null;
  }
  const body = $('uc-body');
  if (!body) return;

  body.innerHTML = `
    <div class="tc-shell">
      <nav class="tc-tabs" role="tablist">
        <button class="tc-tab${TEST_CHAT_TAB === "globe" ? " tc-tab--active" : ""}" id="tc-tab-globe" role="tab">
          <svg width="13" height="13" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8">
            <circle cx="10" cy="10" r="7"/>
            <path d="M2 10h16M10 2a8 8 0 0 0 0 16 8 8 0 0 0 0-16" stroke-linecap="round"/>
          </svg>
          Globe View
        </button>
        <button class="tc-tab${TEST_CHAT_TAB === "test2" ? " tc-tab--active" : ""}" id="tc-tab-test2" role="tab">
          <svg width="13" height="13" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8">
            <rect x="3" y="3" width="14" height="14" rx="2"/>
            <path d="M7 7h6M7 10h6M7 13h4" stroke-linecap="round"/>
          </svg>
          Test 2
        </button>
      </nav>
      
      <div class="tc-tab-content">
        ${TEST_CHAT_TAB === "globe" ? _tcGlobeTabHtml() : _tcTest2TabHtml()}
      </div>
    </div>

    <!-- Edit modal -->
    <div class="tc-modal-backdrop" id="tc-modal" style="display:none" role="dialog" aria-modal="true" aria-label="Edit">
      <div class="tc-modal">
        <div class="tc-modal-header">
          <span class="tc-modal-title">Edit</span>
          <button class="tc-modal-close" id="tc-modal-close" title="Close">
            <svg width="14" height="14" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4l12 12M16 4L4 16" stroke-linecap="round"/></svg>
          </button>
        </div>
        <iframe class="tc-modal-iframe" id="tc-modal-iframe" src="" title="Edit"></iframe>
      </div>
    </div>`;

  // Tab switching
  document.getElementById('tc-tab-globe')?.addEventListener('click', () => {
    if (TEST_CHAT_TAB === "globe") return;
    TEST_CHAT_TAB = "globe";
    renderTestChat();
  });
  document.getElementById('tc-tab-test2')?.addEventListener('click', () => {
    if (TEST_CHAT_TAB === "test2") return;
    TEST_CHAT_TAB = "test2";
    renderTestChat();
  });

  // Wire up Globe tab buttons if active
  if (TEST_CHAT_TAB === "globe") {
    document.getElementById('tc-refresh-btn')?.addEventListener('click', () => {
      const iframe = document.getElementById('tc-view');
      if (iframe) iframe.src = iframe.src;
    });
    document.getElementById('tc-edit-btn')?.addEventListener('click', () => _tcOpenEditModal());
  }

  // Modal handlers
  document.getElementById('tc-modal-close')?.addEventListener('click', () => _tcCloseEditModal());
  document.getElementById('tc-modal')?.addEventListener('click', e => {
    if (e.target === document.getElementById('tc-modal')) _tcCloseEditModal();
  });
}

function _tcGlobeTabHtml() {
  return `
    <div class="tc-btn-group">
      <button class="tc-edit-btn" id="tc-refresh-btn" title="Refresh">
        <svg width="13" height="13" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" style="flex-shrink:0">
          <path d="M4 10a6 6 0 1 1 12 0" stroke-linecap="round"/>
          <path d="M4 10l-2-2 2-2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        Refresh
      </button>
      <button class="tc-edit-btn" id="tc-edit-btn" title="Edit">
        <svg width="13" height="13" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" style="flex-shrink:0">
          <path d="M14.5 2.5a2.121 2.121 0 0 1 3 3L6 17l-4 1 1-4L14.5 2.5z" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        Edit
      </button>
    </div>
    <iframe class="tc-view" id="tc-view" src="/testchat/globe.html" title="Test Chat"></iframe>`;
}

function _tcTest2TabHtml() {
  return `
    <div class="tc-test2-container">
      <div class="tc-test2-card">
        <div class="tc-test2-header">
          <svg width="24" height="24" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5">
            <rect x="3" y="3" width="14" height="14" rx="2"/>
            <path d="M7 7h6M7 10h6M7 13h4" stroke-linecap="round"/>
          </svg>
          <h3>Test 2 Panel</h3>
        </div>
        <div class="tc-test2-body">
          <p class="tc-test2-description">
            This is the Test 2 tab panel. This area can be customized to display 
            additional content, features, or experimental interfaces.
          </p>
          <div class="tc-test2-grid">
            <div class="tc-test2-item">
              <div class="tc-test2-item-icon" style="background: linear-gradient(135deg, #eb6200 0%, #ff7a1a 100%);">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="white" stroke-width="1.8">
                  <path d="M10 2v16M2 10h16" stroke-linecap="round"/>
                </svg>
              </div>
              <div class="tc-test2-item-content">
                <h4>Feature One</h4>
                <p>Placeholder for first feature</p>
              </div>
            </div>
            <div class="tc-test2-item">
              <div class="tc-test2-item-icon" style="background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="white" stroke-width="1.8">
                  <circle cx="10" cy="10" r="7"/>
                </svg>
              </div>
              <div class="tc-test2-item-content">
                <h4>Feature Two</h4>
                <p>Placeholder for second feature</p>
              </div>
            </div>
            <div class="tc-test2-item">
              <div class="tc-test2-item-icon" style="background: linear-gradient(135deg, #15803d 0%, #22c55e 100%);">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="white" stroke-width="1.8">
                  <path d="M3 10l4 4 10-10" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <div class="tc-test2-item-content">
                <h4>Feature Three</h4>
                <p>Placeholder for third feature</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>`;
}

function _tcOpenEditModal() {
  const modal = document.getElementById('tc-modal');
  const iframe = document.getElementById('tc-modal-iframe');
  if (!modal || !iframe) return;
  iframe.src = 'http://localhost:3333/simple';
  modal.style.display = 'flex';
  requestAnimationFrame(() => modal.classList.add('tc-modal-backdrop--open'));
}

function _tcCloseEditModal() {
  const modal = document.getElementById('tc-modal');
  if (!modal) return;
  modal.classList.remove('tc-modal-backdrop--open');
  modal.addEventListener('transitionend', () => {
    modal.style.display = 'none';
    const iframe = document.getElementById('tc-modal-iframe');
    if (iframe) iframe.src = '';
    renderTestChat();
  }, { once: true });
}
```

### 2. Update `static/css/styles.css`

Find the Test Chat Use Case section (around line 6524) and update/add these styles:

```css
/* ── Test Chat Use Case ────────────────────────────────────────────────── */
.tc-shell {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 100%;
  min-height: 520px;
  height: 100%;
  background: linear-gradient(135deg, #0a0a0a 0%, #0f0a00 60%, #1a0f00 100%);
  border-radius: 12px;
  overflow: hidden;
}

/* Subtle top accent bar */
.tc-shell::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(235,98,0,0.7), transparent);
  pointer-events: none;
}

/* Tabs */
.tc-tabs {
  display: flex;
  gap: 0;
  border-bottom: 2px solid rgba(255,255,255,0.08);
  padding: 0 20px;
  background: rgba(0,0,0,0.2);
}

.tc-tab {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 12px 20px;
  border: none;
  background: transparent;
  font-size: 13px;
  font-weight: 600;
  color: rgba(255,255,255,0.5);
  cursor: pointer;
  border-bottom: 2px solid transparent;
  margin-bottom: -2px;
  transition: color 0.15s, border-color 0.15s;
  font-family: inherit;
}

.tc-tab:hover {
  color: rgba(255,255,255,0.8);
}

.tc-tab--active {
  color: #eb6200;
  border-bottom-color: #eb6200;
}

.tc-tab svg {
  flex-shrink: 0;
}

.tc-tab-content {
  flex: 1;
  width: 100%;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.tc-view {
  flex: 1;
  width: 100%;
  min-height: 520px;
  border: none;
  display: block;
}

.tc-btn-group {
  display: flex;
  gap: 10px;
  padding: 16px 20px;
  background: rgba(0,0,0,0.15);
  border-bottom: 1px solid rgba(255,255,255,0.05);
}

.tc-edit-btn {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 8px 14px;
  border: 1px solid rgba(255,255,255,0.12);
  background: rgba(255,255,255,0.04);
  color: rgba(255,255,255,0.85);
  font-size: 12px;
  font-weight: 600;
  font-family: inherit;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.15s;
}

.tc-edit-btn:hover {
  background: rgba(255,255,255,0.08);
  border-color: rgba(255,255,255,0.2);
  color: #fff;
}

.tc-edit-btn:active {
  transform: scale(0.98);
}

/* Test 2 Tab Styles */
.tc-test2-container {
  flex: 1;
  padding: 32px 20px;
  overflow-y: auto;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.tc-test2-card {
  width: 100%;
  max-width: 800px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px;
  overflow: hidden;
}

.tc-test2-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 20px 24px;
  background: rgba(0,0,0,0.2);
  border-bottom: 1px solid rgba(255,255,255,0.08);
}

.tc-test2-header svg {
  color: #eb6200;
  flex-shrink: 0;
}

.tc-test2-header h3 {
  margin: 0;
  font-size: 16px;
  font-weight: 700;
  color: rgba(255,255,255,0.95);
}

.tc-test2-body {
  padding: 24px;
}

.tc-test2-description {
  margin: 0 0 24px 0;
  font-size: 14px;
  line-height: 1.6;
  color: rgba(255,255,255,0.7);
}

.tc-test2-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

.tc-test2-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 16px;
  background: rgba(0,0,0,0.2);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 8px;
  transition: all 0.2s;
}

.tc-test2-item:hover {
  background: rgba(0,0,0,0.3);
  border-color: rgba(255,255,255,0.12);
  transform: translateY(-1px);
}

.tc-test2-item-icon {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.tc-test2-item-content {
  flex: 1;
}

.tc-test2-item-content h4 {
  margin: 0 0 4px 0;
  font-size: 14px;
  font-weight: 600;
  color: rgba(255,255,255,0.95);
}

.tc-test2-item-content p {
  margin: 0;
  font-size: 13px;
  color: rgba(255,255,255,0.6);
}

/* Modal styles */
.tc-modal-backdrop {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.8);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10000;
  opacity: 0;
  transition: opacity 0.2s;
}

.tc-modal-backdrop--open { opacity: 1; }

.tc-modal {
  width: 90vw;
  height: 85vh;
  max-width: 1400px;
  background: #1a1a1a;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  transform: scale(0.95);
  transition: transform 0.2s;
}

.tc-modal-backdrop--open .tc-modal {
  transform: scale(1);
}

.tc-modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

.tc-modal-title {
  font-size: 14px;
  font-weight: 600;
  color: rgba(255,255,255,0.95);
}

.tc-modal-close {
  width: 28px;
  height: 28px;
  border: none;
  background: rgba(255,255,255,0.04);
  color: rgba(255,255,255,0.6);
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s;
}

.tc-modal-close:hover { background: rgba(255,255,255,0.08); color: #fff; }

.tc-modal-iframe {
  flex: 1;
  width: 100%;
  border: none;
  border-radius: 0 0 12px 12px;
}

@media (max-width: 768px) {
  .tc-tabs {
    padding: 0 12px;
  }
  
  .tc-tab {
    padding: 10px 12px;
    font-size: 12px;
  }
  
  .tc-btn-group {
    padding: 12px 16px;
  }
  
  .tc-test2-container {
    padding: 20px 16px;
  }
  
  .tc-test2-body {
    padding: 20px;
  }
}
```

## Summary

The changes add a clean tab interface to Test Chat with two tabs:
1. **Globe View** - The existing revolving globe interface
2. **Test 2** - A new placeholder panel with a card-based layout

The implementation follows the same patterns used in other use cases (BIN Lookup, Specials) for consistency.
