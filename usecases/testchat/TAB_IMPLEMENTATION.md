# Test Chat - Tab Implementation Guide

## Overview
This guide adds a "Test X" tab to the Test Chat use case, creating a clean tabbed interface consistent with other Vima use cases.

## Changes Required

### 1. JavaScript Changes (static/js/app.js)

#### Add state management for tabs
Find the `renderTestChat` function and add this state object before it:

```javascript
const TESTCHAT = {
  tab: 'globe'  // 'globe' | 'testx'
};
```

#### Update `renderTestChat` function
Replace the existing `renderTestChat` function with:

```javascript
function renderTestChat() {
  if (_testChatAnimRef) {
    cancelAnimationFrame(_testChatAnimRef);
    _testChatAnimRef = null;
  }
  const body = $('uc-body');
  if (!body) return;

  body.innerHTML = `
    <div class="tc-shell">
      <div class="tc-header">
        <div class="tc-tabs">
          <button class="tc-tab ${TESTCHAT.tab === 'globe' ? 'tc-tab-active' : ''}" data-tab="globe">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="2" y1="12" x2="22" y2="12"></line>
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
            </svg>
            Globe
          </button>
          <button class="tc-tab ${TESTCHAT.tab === 'testx' ? 'tc-tab-active' : ''}" data-tab="testx">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
            Test X
          </button>
        </div>
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
      </div>
      
      <div class="tc-content">
        ${TESTCHAT.tab === 'globe' ? _tcGlobeView() : _tcTestXView()}
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

  // Wire tabs
  document.querySelectorAll('.tc-tab').forEach(btn => {
    btn.addEventListener('click', () => {
      TESTCHAT.tab = btn.dataset.tab;
      renderTestChat();
    });
  });

  document.getElementById('tc-refresh-btn')?.addEventListener('click', () => {
    if (TESTCHAT.tab === 'globe') {
      const iframe = document.getElementById('tc-view');
      if (iframe) iframe.src = iframe.src;
    } else {
      renderTestChat();
    }
  });
  document.getElementById('tc-edit-btn')?.addEventListener('click', () => _tcOpenEditModal());
  document.getElementById('tc-modal-close')?.addEventListener('click', () => _tcCloseEditModal());
  document.getElementById('tc-modal')?.addEventListener('click', e => {
    if (e.target === document.getElementById('tc-modal')) _tcCloseEditModal();
  });
}

function _tcGlobeView() {
  return `<iframe class="tc-view" id="tc-view" src="/testchat/globe.html" title="Test Chat Globe"></iframe>`;
}

function _tcTestXView() {
  return `
    <div class="tc-testx">
      <div class="tc-testx-content">
        <div class="tc-testx-icon">
          <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </div>
        <h2 class="tc-testx-title">Test X</h2>
        <p class="tc-testx-desc">
          This is a placeholder for experimental features and testing scenarios.
          Connect APIs, build interactions, or prototype new use cases here.
        </p>
        <div class="tc-testx-stats">
          <div class="tc-testx-stat">
            <div class="tc-testx-stat-val">0</div>
            <div class="tc-testx-stat-lbl">Active Tests</div>
          </div>
          <div class="tc-testx-stat">
            <div class="tc-testx-stat-val">0</div>
            <div class="tc-testx-stat-lbl">API Calls</div>
          </div>
          <div class="tc-testx-stat">
            <div class="tc-testx-stat-val">Ready</div>
            <div class="tc-testx-stat-lbl">Status</div>
          </div>
        </div>
        <button class="tc-testx-btn" onclick="alert('Test X feature coming soon!')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
          Start Test
        </button>
      </div>
    </div>`;
}
```

### 2. CSS Changes (static/css/styles.css)

Add these styles after the existing `.tc-modal-iframe` rule:

```css
/* Test Chat Header & Tabs */
.tc-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  background: rgba(0, 0, 0, 0.3);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.tc-tabs {
  display: flex;
  gap: 6px;
}

.tc-tab {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  font-size: 13px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.5);
  background: transparent;
  border: 1px solid transparent;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  letter-spacing: 0.01em;
}

.tc-tab svg {
  opacity: 0.6;
  transition: opacity 0.2s ease;
}

.tc-tab:hover {
  color: rgba(255, 255, 255, 0.8);
  background: rgba(255, 255, 255, 0.04);
}

.tc-tab:hover svg {
  opacity: 0.9;
}

.tc-tab-active {
  color: #fff;
  background: rgba(235, 98, 0, 0.12);
  border-color: rgba(235, 98, 0, 0.3);
}

.tc-tab-active svg {
  opacity: 1;
}

.tc-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 0;
  overflow: hidden;
}

/* Update tc-btn-group to work in header */
.tc-header .tc-btn-group {
  position: static;
  margin: 0;
}

/* Test X View */
.tc-testx {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
  overflow-y: auto;
}

.tc-testx-content {
  max-width: 540px;
  text-align: center;
}

.tc-testx-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 96px;
  height: 96px;
  margin: 0 auto 24px;
  background: linear-gradient(135deg, rgba(235, 98, 0, 0.15), rgba(235, 98, 0, 0.05));
  border: 1px solid rgba(235, 98, 0, 0.2);
  border-radius: 20px;
}

.tc-testx-icon svg {
  color: rgba(235, 98, 0, 0.9);
}

.tc-testx-title {
  margin: 0 0 12px;
  font-size: 28px;
  font-weight: 600;
  color: #fff;
  letter-spacing: -0.02em;
}

.tc-testx-desc {
  margin: 0 0 32px;
  font-size: 14px;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.6);
}

.tc-testx-stats {
  display: flex;
  gap: 24px;
  justify-content: center;
  margin-bottom: 32px;
  padding: 24px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 12px;
}

.tc-testx-stat {
  text-align: center;
}

.tc-testx-stat-val {
  font-size: 24px;
  font-weight: 600;
  color: #fff;
  margin-bottom: 4px;
}

.tc-testx-stat-lbl {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.tc-testx-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  font-size: 14px;
  font-weight: 600;
  color: #fff;
  background: linear-gradient(135deg, rgba(235, 98, 0, 0.9), rgba(235, 98, 0, 0.7));
  border: 1px solid rgba(235, 98, 0, 0.4);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  letter-spacing: 0.01em;
}

.tc-testx-btn:hover {
  background: linear-gradient(135deg, rgba(235, 98, 0, 1), rgba(235, 98, 0, 0.85));
  border-color: rgba(235, 98, 0, 0.6);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(235, 98, 0, 0.3);
}

.tc-testx-btn:active {
  transform: translateY(0);
}
```

### 3. Update tc-view for the new layout

Find and update the `.tc-view` rule:

```css
.tc-view {
  flex: 1;
  width: 100%;
  border: none;
  display: block;
}
```

### 4. Update tc-btn-group positioning

Find and update the `.tc-btn-group` rule to remove absolute positioning since it's now in the header:

```css
.tc-btn-group {
  display: flex;
  gap: 8px;
}
```

## Summary

This implementation adds:
- ✅ Clean tab navigation (Globe | Test X)
- ✅ Consistent styling with other Vima use cases
- ✅ Placeholder Test X view with stats and CTA
- ✅ Tab state management
- ✅ Maintains all existing functionality (Refresh, Edit buttons)
- ✅ Responsive and accessible design

The Test X tab provides a foundation for future experimental features while keeping the interface clean and professional.
