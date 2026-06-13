// -------------------------------------------------------------------
// features/bundles.js
// API Bundles tab - sidebar entries open a rich detail panel in the
// content area. Mirrors the APIs / Use Cases tab layout. Each bundle's
// detail includes "What you can do", a numbered "How the APIs fit
// together" journey, end-to-end walkthroughs and the API roster.
// The shared bundle/use-case data layer lives in core/catalog.js.
// -------------------------------------------------------------------
import { USE_CASES } from '../core/env.js';
import { escapeHtml } from '../core/html.js';
import { _isNonUsBlockedApiId, _isNonUsBlockedUseCaseById } from '../core/region.js';
import { loadBundles, loadUseCases } from '../core/catalog.js';
import { _initSdkDemo, _initLiveDemo } from './openFinanceSdk.js';
  function _bundleApiTileHtml(bundle, a) {
    const isAnchor = a.id === bundle.anchor;
    const cls = 'bundle-api-tile' + (a.configured ? ' configured' : '') + (isAnchor ? ' anchor' : '');
    return `<button class="${cls}" data-bundle-api="${escapeHtml(a.id)}"
              title="${isAnchor ? 'Anchor \u00b7 ' : ''}${escapeHtml(a.group || '')} \u00b7 ${a.configured ? 'Configured' : 'Not configured'}">
        <span class="bundle-api-dot ${a.configured ? 'ok' : 'off'}"></span>
        <span class="bundle-api-meta">
          <span class="bundle-api-name">${escapeHtml(a.name)}</span>
          <span class="bundle-api-group">${escapeHtml(a.group || '')}</span>
        </span>
        ${isAnchor ? '<span class="bundle-anchor-pill">anchor</span>' : ''}
      </button>`;
  }

  // Per-bundle hero visualization — each bundle gets a unique thematic SVG
  // that summarises what it does at a glance. The bundle's accent colour is
  // inherited via CSS so the artwork tints itself.
  function _bundleHeroVisual(bundleId) {
    const visuals = {
      pfm_stack: `
        <svg viewBox="0 0 320 160" class="bhv-svg bhv-pfm" preserveAspectRatio="xMidYMid meet">
          <!-- Phone frame -->
          <rect x="18" y="14" width="110" height="132" rx="14" fill="#0f0f12" stroke="currentColor" stroke-width="1.2" opacity="0.85"/>
          <rect x="40" y="18" width="40" height="3" rx="1.5" fill="#1a1a1f"/>
          <!-- Donut of categories -->
          <g transform="translate(73 80)">
            <circle r="34" fill="none" stroke="#1f1f24" stroke-width="10"/>
            <circle r="34" fill="none" stroke="currentColor" stroke-width="10"
                    stroke-dasharray="60 153" transform="rotate(-90)"/>
            <circle r="34" fill="none" stroke="#f37338" stroke-width="10"
                    stroke-dasharray="42 171" stroke-dashoffset="-60" transform="rotate(-90)"/>
            <circle r="34" fill="none" stroke="#ffcb05" stroke-width="10"
                    stroke-dasharray="30 183" stroke-dashoffset="-102" transform="rotate(-90)"/>
            <text y="4" text-anchor="middle" fill="rgba(255,230,180,0.95)" font-size="11" font-weight="700" font-family="JetBrains Mono, monospace">£2.4k</text>
          </g>
          <text x="73" y="135" text-anchor="middle" fill="rgba(255,180,100,0.6)" font-size="7" font-weight="700" letter-spacing="1">THIS MONTH</text>
          <!-- Insights card -->
          <g transform="translate(146 22)">
            <rect width="160" height="120" rx="10" fill="#15151a" stroke="currentColor" stroke-width="1" opacity="0.9"/>
            <text x="14" y="20" fill="rgba(255,200,140,0.6)" font-size="7" font-weight="700" letter-spacing="1">CATEGORIES</text>
            <g font-size="8.5" font-family="JetBrains Mono, monospace">
              <g transform="translate(14 38)"><circle cx="4" cy="-3" r="3" fill="currentColor"/><text x="14" y="0" fill="rgba(255,230,180,0.9)">Groceries</text><text x="140" y="0" text-anchor="end" fill="currentColor" font-weight="700">£612</text></g>
              <g transform="translate(14 56)"><circle cx="4" cy="-3" r="3" fill="#f37338"/><text x="14" y="0" fill="rgba(255,230,180,0.9)">Transport</text><text x="140" y="0" text-anchor="end" fill="#f37338" font-weight="700">£428</text></g>
              <g transform="translate(14 74)"><circle cx="4" cy="-3" r="3" fill="#ffcb05"/><text x="14" y="0" fill="rgba(255,230,180,0.9)">Dining</text><text x="140" y="0" text-anchor="end" fill="#ffcb05" font-weight="700">£305</text></g>
            </g>
            <rect x="14" y="90" width="132" height="18" rx="5" fill="rgba(255,203,5,0.12)" stroke="rgba(255,203,5,0.35)"/>
            <text x="80" y="102" text-anchor="middle" fill="#ffcb05" font-size="8" font-weight="700">Budget on track ✓</text>
          </g>
        </svg>`,

      subscriptions: `
        <svg viewBox="0 0 320 160" class="bhv-svg bhv-subs" preserveAspectRatio="xMidYMid meet">
          <!-- Calendar -->
          <g transform="translate(18 18)">
            <rect width="124" height="124" rx="10" fill="#15151a" stroke="currentColor" stroke-width="1" opacity="0.9"/>
            <rect width="124" height="22" rx="10" fill="currentColor" opacity="0.25"/>
            <text x="62" y="15" text-anchor="middle" fill="currentColor" font-size="9" font-weight="700" letter-spacing="1">JUNE 2026</text>
            <g font-size="7" font-family="JetBrains Mono, monospace" fill="rgba(255,210,160,0.6)">
              ${[0,1,2,3,4,5,6].map((d,i)=>`<text x="${10+i*15}" y="36" text-anchor="middle">${'SMTWTFS'[i]}</text>`).join('')}
            </g>
            <g font-size="8" font-family="JetBrains Mono, monospace" fill="rgba(255,230,180,0.85)">
              ${Array.from({length:28}, (_,i)=>{
                const col = i%7, row = Math.floor(i/7);
                const d = i+1;
                const isHit = [5,12,19,26].includes(d);
                return `<g transform="translate(${10+col*15} ${52+row*18})">
                  ${isHit?`<circle cx="0" cy="-3" r="8" fill="currentColor" opacity="0.85"/>`:''}
                  <text text-anchor="middle" fill="${isHit?'#0a0a0a':'rgba(255,230,180,0.7)'}" font-weight="${isHit?'700':'400'}">${d}</text>
                </g>`;
              }).join('')}
            </g>
          </g>
          <!-- Subscription cards stack -->
          <g transform="translate(150 28)">
            <rect width="158" height="34" rx="7" fill="#1a1a1f" stroke="currentColor" stroke-width="1" opacity="0.6" transform="translate(8 8)"/>
            <rect width="158" height="34" rx="7" fill="#1a1a1f" stroke="currentColor" stroke-width="1" opacity="0.8" transform="translate(4 4)"/>
            <rect width="158" height="34" rx="7" fill="#15151a" stroke="currentColor" stroke-width="1.2"/>
            <circle cx="20" cy="17" r="9" fill="currentColor" opacity="0.25"/>
            <text x="20" y="20" text-anchor="middle" fill="currentColor" font-size="11" font-weight="700">N</text>
            <text x="36" y="15" fill="rgba(255,230,180,0.92)" font-size="8.5" font-weight="600">Netflix</text>
            <text x="36" y="26" fill="rgba(255,180,100,0.55)" font-size="6.5" letter-spacing="0.3">Next 26 Jun · monthly</text>
            <text x="148" y="20" text-anchor="end" fill="currentColor" font-size="10" font-weight="700" font-family="JetBrains Mono, monospace">£10.99</text>
          </g>
          <g transform="translate(150 90)">
            <rect width="158" height="44" rx="7" fill="rgba(255,203,5,0.08)" stroke="currentColor" stroke-width="1"/>
            <text x="10" y="14" fill="rgba(255,200,140,0.55)" font-size="6.5" font-weight="700" letter-spacing="1">PRICE CHANGE</text>
            <text x="10" y="28" fill="rgba(255,230,180,0.9)" font-size="8">Spotify £9.99 → £11.99</text>
            <text x="148" y="38" text-anchor="end" fill="currentColor" font-size="8" font-weight="700">+£2.00 / mo</text>
          </g>
        </svg>`,

      loyalty_stack: `
        <svg viewBox="0 0 320 160" class="bhv-svg bhv-loyalty" preserveAspectRatio="xMidYMid meet">
          <!-- Coupons/offers fan -->
          <g transform="translate(50 80)">
            <g transform="rotate(-18) translate(-55 -38)">
              <rect width="110" height="76" rx="10" fill="#15151a" stroke="currentColor" stroke-width="1" opacity="0.6"/>
              <circle cx="0" cy="38" r="6" fill="#0a0a0a"/><circle cx="110" cy="38" r="6" fill="#0a0a0a"/>
            </g>
            <g transform="rotate(-6) translate(-55 -38)">
              <rect width="110" height="76" rx="10" fill="#15151a" stroke="currentColor" stroke-width="1" opacity="0.85"/>
              <circle cx="0" cy="38" r="6" fill="#0a0a0a"/><circle cx="110" cy="38" r="6" fill="#0a0a0a"/>
            </g>
            <g transform="rotate(8) translate(-55 -38)">
              <rect width="110" height="76" rx="10" fill="#15151a" stroke="currentColor" stroke-width="1.4"/>
              <circle cx="0" cy="38" r="6" fill="#0a0a0a"/><circle cx="110" cy="38" r="6" fill="#0a0a0a"/>
              <line x1="55" y1="6" x2="55" y2="70" stroke="currentColor" stroke-width="1" stroke-dasharray="2 3" opacity="0.4"/>
              <text x="30" y="22" text-anchor="middle" fill="rgba(255,200,140,0.55)" font-size="6" font-weight="700" letter-spacing="1">OFFER</text>
              <text x="30" y="42" text-anchor="middle" fill="currentColor" font-size="18" font-weight="800" font-family="JetBrains Mono, monospace">15%</text>
              <text x="30" y="56" text-anchor="middle" fill="rgba(255,230,180,0.7)" font-size="7">cashback</text>
              <text x="83" y="34" text-anchor="middle" fill="rgba(255,230,180,0.85)" font-size="8" font-weight="600">Coffee</text>
              <text x="83" y="46" text-anchor="middle" fill="rgba(255,180,100,0.5)" font-size="6.5">Shops</text>
            </g>
          </g>
          <!-- Wallet -->
          <g transform="translate(158 24)">
            <rect width="150" height="112" rx="10" fill="#15151a" stroke="currentColor" stroke-width="1" opacity="0.9"/>
            <text x="12" y="20" fill="rgba(255,200,140,0.6)" font-size="7" font-weight="700" letter-spacing="1">PUBLISHED TO USER</text>
            <g transform="translate(12 30)">
              <rect width="126" height="22" rx="6" fill="rgba(255,203,5,0.10)" stroke="currentColor" stroke-width="0.8"/>
              <circle cx="13" cy="11" r="6" fill="currentColor" opacity="0.3"/>
              <text x="13" y="14" text-anchor="middle" fill="currentColor" font-size="8" font-weight="700">★</text>
              <text x="24" y="14" fill="rgba(255,230,180,0.9)" font-size="7.5">Pret · 10% off</text>
              <text x="120" y="14" text-anchor="end" fill="currentColor" font-size="6.5" font-weight="700">NEW</text>
            </g>
            <g transform="translate(12 58)">
              <rect width="126" height="22" rx="6" fill="rgba(255,203,5,0.06)" stroke="currentColor" stroke-width="0.8" opacity="0.7"/>
              <circle cx="13" cy="11" r="6" fill="currentColor" opacity="0.2"/>
              <text x="13" y="14" text-anchor="middle" fill="currentColor" font-size="8" font-weight="700">★</text>
              <text x="24" y="14" fill="rgba(255,230,180,0.75)" font-size="7.5">BP · 5p/litre</text>
            </g>
            <g transform="translate(12 92)" font-size="7" font-family="JetBrains Mono, monospace">
              <text fill="rgba(255,180,100,0.55)">Eligible offers</text>
              <text x="126" text-anchor="end" fill="currentColor" font-weight="700">12</text>
            </g>
          </g>
        </svg>`,

      merchant_resolution: `
        <svg viewBox="0 0 320 160" class="bhv-svg bhv-merch" preserveAspectRatio="xMidYMid meet">
          <!-- Raw transaction -->
          <g transform="translate(14 20)">
            <rect width="124" height="120" rx="8" fill="#15151a" stroke="rgba(255,90,90,0.4)" stroke-width="1"/>
            <text x="12" y="18" fill="rgba(255,140,140,0.65)" font-size="7" font-weight="700" letter-spacing="1">RAW DESCRIPTOR</text>
            <text x="12" y="38" fill="rgba(255,230,180,0.85)" font-size="8.5" font-family="JetBrains Mono, monospace">SQ *ACME COFFEE</text>
            <text x="12" y="50" fill="rgba(255,230,180,0.65)" font-size="8.5" font-family="JetBrains Mono, monospace">LON GB 0078432</text>
            <line x1="12" y1="62" x2="112" y2="62" stroke="rgba(255,90,90,0.2)" stroke-dasharray="2 3"/>
            <text x="12" y="76" fill="rgba(255,140,140,0.55)" font-size="7" font-family="JetBrains Mono, monospace">? unknown brand</text>
            <text x="12" y="88" fill="rgba(255,140,140,0.55)" font-size="7" font-family="JetBrains Mono, monospace">? no category</text>
            <text x="12" y="100" fill="rgba(255,140,140,0.55)" font-size="7" font-family="JetBrains Mono, monospace">? no logo</text>
            <text x="12" y="112" fill="rgba(255,140,140,0.55)" font-size="7" font-family="JetBrains Mono, monospace">? no location</text>
          </g>
          <!-- Arrow -->
          <g transform="translate(148 80)" fill="currentColor">
            <path d="M 0 -6 L 14 -6 L 14 -12 L 26 0 L 14 12 L 14 6 L 0 6 Z" opacity="0.85"/>
            <text x="13" y="-18" text-anchor="middle" fill="currentColor" font-size="7" font-weight="700" letter-spacing="1">ENRICH</text>
          </g>
          <!-- Clean transaction -->
          <g transform="translate(184 20)">
            <rect width="122" height="120" rx="8" fill="#15151a" stroke="currentColor" stroke-width="1.4"/>
            <g transform="translate(10 14)">
              <rect width="22" height="22" rx="6" fill="currentColor"/>
              <text x="11" y="16" text-anchor="middle" fill="#0a0a0a" font-size="13" font-weight="800">☕</text>
            </g>
            <text x="38" y="22" fill="rgba(255,230,180,0.95)" font-size="9.5" font-weight="700">Acme Coffee</text>
            <text x="38" y="33" fill="rgba(255,200,140,0.55)" font-size="6.5" letter-spacing="0.2">COFFEE SHOPS</text>
            <line x1="10" y1="46" x2="112" y2="46" stroke="currentColor" stroke-dasharray="2 3" opacity="0.3"/>
            <g font-size="7" font-family="JetBrains Mono, monospace">
              <g transform="translate(10 60)"><text fill="rgba(255,180,100,0.55)">MCC</text><text x="104" text-anchor="end" fill="rgba(255,230,180,0.85)">5814</text></g>
              <g transform="translate(10 74)"><text fill="rgba(255,180,100,0.55)">Brand</text><text x="104" text-anchor="end" fill="rgba(255,230,180,0.85)">Acme</text></g>
              <g transform="translate(10 88)"><text fill="rgba(255,180,100,0.55)">Postcode</text><text x="104" text-anchor="end" fill="rgba(255,230,180,0.85)">EC2A 4DP</text></g>
              <g transform="translate(10 102)"><text fill="rgba(255,180,100,0.55)">Logo</text><text x="104" text-anchor="end" fill="currentColor" font-weight="700">✓</text></g>
            </g>
          </g>
        </svg>`,

      issuer_toolkit: `
        <svg viewBox="0 0 320 160" class="bhv-svg bhv-issuer" preserveAspectRatio="xMidYMid meet">
          <!-- Credit card -->
          <g transform="translate(30 30)">
            <rect width="170" height="106" rx="12" fill="url(#issuer-card-grad)" stroke="currentColor" stroke-width="1.2"/>
            <defs>
              <linearGradient id="issuer-card-grad" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0%" stop-color="#1c1c24"/>
                <stop offset="100%" stop-color="#0a0a0e"/>
              </linearGradient>
            </defs>
            <!-- Chip -->
            <rect x="16" y="22" width="22" height="18" rx="3" fill="currentColor" opacity="0.85"/>
            <line x1="16" y1="28" x2="38" y2="28" stroke="#0a0a0e" stroke-width="0.6"/>
            <line x1="16" y1="34" x2="38" y2="34" stroke="#0a0a0e" stroke-width="0.6"/>
            <line x1="27" y1="22" x2="27" y2="40" stroke="#0a0a0e" stroke-width="0.6"/>
            <!-- Number -->
            <text x="16" y="64" fill="rgba(255,230,180,0.9)" font-size="11" font-weight="700" font-family="JetBrains Mono, monospace" letter-spacing="2">5412 ••••</text>
            <text x="16" y="80" fill="rgba(255,180,100,0.55)" font-size="6.5" letter-spacing="1.5">CARDHOLDER</text>
            <text x="16" y="90" fill="rgba(255,230,180,0.85)" font-size="8" font-weight="600">ALEX MORGAN</text>
            <!-- Mastercard circles -->
            <circle cx="142" cy="82" r="11" fill="#eb001b" opacity="0.95"/>
            <circle cx="156" cy="82" r="11" fill="#ffcb05" opacity="0.85"/>
            <!-- BIN tag -->
            <g transform="translate(118 16)">
              <rect width="44" height="18" rx="5" fill="rgba(255,203,5,0.18)" stroke="currentColor" stroke-width="0.8"/>
              <text x="22" y="12" text-anchor="middle" fill="currentColor" font-size="8" font-weight="700" font-family="JetBrains Mono, monospace">BIN 541</text>
            </g>
          </g>
          <!-- Benefit badges stack -->
          <g transform="translate(204 22)">
            <rect width="106" height="22" rx="6" fill="rgba(255,203,5,0.10)" stroke="currentColor" stroke-width="0.8"/>
            <circle cx="13" cy="11" r="6" fill="currentColor" opacity="0.25"/>
            <text x="13" y="14" text-anchor="middle" fill="currentColor" font-size="8" font-weight="700">✓</text>
            <text x="24" y="14" fill="rgba(255,230,180,0.9)" font-size="7.5">Travel insurance</text>
          </g>
          <g transform="translate(204 50)">
            <rect width="106" height="22" rx="6" fill="rgba(255,203,5,0.10)" stroke="currentColor" stroke-width="0.8"/>
            <circle cx="13" cy="11" r="6" fill="currentColor" opacity="0.25"/>
            <text x="13" y="14" text-anchor="middle" fill="currentColor" font-size="8" font-weight="700">✓</text>
            <text x="24" y="14" fill="rgba(255,230,180,0.9)" font-size="7.5">Purchase cover</text>
          </g>
          <g transform="translate(204 78)">
            <rect width="106" height="22" rx="6" fill="rgba(255,203,5,0.10)" stroke="currentColor" stroke-width="0.8"/>
            <circle cx="13" cy="11" r="6" fill="currentColor" opacity="0.25"/>
            <text x="13" y="14" text-anchor="middle" fill="currentColor" font-size="8" font-weight="700">✓</text>
            <text x="24" y="14" fill="rgba(255,230,180,0.9)" font-size="7.5">Lounge access</text>
          </g>
          <g transform="translate(204 110)">
            <rect width="106" height="22" rx="6" fill="rgba(120,200,140,0.10)" stroke="rgba(120,200,140,0.55)" stroke-width="0.8"/>
            <text x="53" y="14" text-anchor="middle" fill="rgba(120,200,140,0.95)" font-size="7.5" font-weight="700" letter-spacing="0.5">CONSENT GRANTED</text>
          </g>
        </svg>`,

      acquirer_risk: `
        <svg viewBox="0 0 320 160" class="bhv-svg bhv-risk" preserveAspectRatio="xMidYMid meet">
          <!-- Shield -->
          <g transform="translate(30 24)">
            <path d="M 50 0 L 100 18 L 100 60 C 100 88 78 108 50 116 C 22 108 0 88 0 60 L 0 18 Z"
                  fill="rgba(160,16,16,0.15)" stroke="currentColor" stroke-width="1.4"/>
            <path d="M 30 58 L 44 72 L 72 42" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
            <text x="50" y="100" text-anchor="middle" fill="rgba(255,180,180,0.7)" font-size="7" font-weight="700" letter-spacing="1">PROTECTED</text>
          </g>
          <!-- Transaction stream + alert -->
          <g transform="translate(150 18)">
            <text x="0" y="10" fill="rgba(255,180,180,0.6)" font-size="7" font-weight="700" letter-spacing="1">LIVE TRANSACTION RISK</text>
            <!-- Heartbeat line -->
            <g transform="translate(0 24)">
              <rect width="160" height="38" rx="6" fill="#15151a" stroke="currentColor" stroke-width="0.8" opacity="0.85"/>
              <polyline points="6,22 22,22 26,10 32,32 38,16 48,22 64,22 68,8 74,34 80,22 100,22 106,14 112,28 118,22 154,22"
                        fill="none" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round" stroke-linecap="round"/>
              <circle cx="68" cy="8" r="2.5" fill="currentColor"/>
              <circle cx="74" cy="34" r="2.5" fill="currentColor"/>
            </g>
            <!-- Risk rows -->
            <g transform="translate(0 70)" font-family="JetBrains Mono, monospace" font-size="7.5">
              <rect width="160" height="20" rx="5" fill="rgba(120,200,140,0.08)" stroke="rgba(120,200,140,0.4)" stroke-width="0.6"/>
              <circle cx="10" cy="10" r="3" fill="rgba(120,200,140,0.95)"/>
              <text x="20" y="13" fill="rgba(255,230,180,0.85)">£42.10 Fuel</text>
              <text x="152" y="13" text-anchor="end" fill="rgba(120,200,140,0.95)" font-weight="700">OK</text>
            </g>
            <g transform="translate(0 94)" font-family="JetBrains Mono, monospace" font-size="7.5">
              <rect width="160" height="20" rx="5" fill="rgba(255,90,90,0.10)" stroke="currentColor" stroke-width="0.6"/>
              <circle cx="10" cy="10" r="3" fill="currentColor"/>
              <text x="20" y="13" fill="rgba(255,230,180,0.85)">£2,990 Crypto</text>
              <text x="152" y="13" text-anchor="end" fill="currentColor" font-weight="700">BLOCKED</text>
            </g>
            <g transform="translate(0 118)" font-family="JetBrains Mono, monospace" font-size="7.5">
              <rect width="160" height="20" rx="5" fill="rgba(255,203,5,0.08)" stroke="rgba(255,203,5,0.45)" stroke-width="0.6"/>
              <circle cx="10" cy="10" r="3" fill="#ffcb05"/>
              <text x="20" y="13" fill="rgba(255,230,180,0.85)">£780 Online</text>
              <text x="152" y="13" text-anchor="end" fill="#ffcb05" font-weight="700">REVIEW</text>
            </g>
          </g>
        </svg>`,

      sustainability: `
        <svg viewBox="0 0 320 160" class="bhv-svg bhv-sust" preserveAspectRatio="xMidYMid meet">
          <!-- Leaf -->
          <g transform="translate(28 24)">
            <path d="M 0 110 C 0 50 50 0 110 0 C 110 60 60 110 0 110 Z"
                  fill="rgba(120,200,140,0.18)" stroke="currentColor" stroke-width="1.4"/>
            <path d="M 8 100 C 40 70 70 50 100 22" fill="none" stroke="currentColor" stroke-width="1" opacity="0.6"/>
            <path d="M 18 96 C 30 90 38 88 46 88 M 32 84 C 44 78 52 76 62 76 M 50 70 C 60 64 70 62 80 62" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.5"/>
            <circle cx="55" cy="60" r="14" fill="#0a0a0a" stroke="currentColor" stroke-width="1"/>
            <text x="55" y="58" text-anchor="middle" fill="currentColor" font-size="11" font-weight="800" font-family="JetBrains Mono, monospace">CO₂</text>
            <text x="55" y="68" text-anchor="middle" fill="rgba(255,230,180,0.7)" font-size="6" font-weight="600">tracked</text>
          </g>
          <!-- Footprint card -->
          <g transform="translate(166 22)">
            <rect width="138" height="116" rx="10" fill="#15151a" stroke="currentColor" stroke-width="1" opacity="0.9"/>
            <text x="12" y="18" fill="rgba(180,230,200,0.6)" font-size="7" font-weight="700" letter-spacing="1">YOUR FOOTPRINT</text>
            <text x="12" y="38" fill="currentColor" font-size="20" font-weight="800" font-family="JetBrains Mono, monospace">82.4</text>
            <text x="58" y="38" fill="rgba(255,230,180,0.7)" font-size="9">kg CO₂e</text>
            <text x="12" y="50" fill="rgba(180,230,200,0.5)" font-size="7">vs 91.2 last month · ↓ 10%</text>
            <!-- Trending bars -->
            <g transform="translate(12 62)">
              ${[55,62,48,70,58,46,38].map((h,i)=>`<rect x="${i*18}" y="${44-h*0.6}" width="12" height="${h*0.6}" rx="2" fill="currentColor" opacity="${0.4 + i*0.08}"/>`).join('')}
            </g>
            <!-- Offset CTA -->
            <g transform="translate(12 104)">
              <rect width="114" height="0" />
            </g>
          </g>
        </svg>`,
    };
    return visuals[bundleId] || '';
  }

  function _bundleJourneyStepHtml(step, idx, byId) {
    const api = byId[step.api_id];
    const apiName = api ? api.name : step.api_id;
    return `<li class="bundle-journey-step">
      <span class="bundle-journey-num">${idx + 1}</span>
      <div class="bundle-journey-body">
        <div class="bundle-journey-head">
          <span class="bundle-journey-title">${escapeHtml(step.title)}</span>
          <button class="bundle-journey-api" data-bundle-api="${escapeHtml(step.api_id)}" title="Open ${escapeHtml(apiName)}">${escapeHtml(apiName)}</button>
        </div>
        <p class="bundle-journey-detail">${escapeHtml(step.detail)}</p>
      </div>
    </li>`;
  }

  function renderBundleDetail(bundle) {
    const aboutPanel = document.getElementById('bundle-about-panel');
    const detail = document.getElementById('bundle-detail');
    if (aboutPanel) aboutPanel.classList.add('hidden');
    if (!detail) return;
    detail.classList.remove('hidden');
    detail.style.setProperty('--bundle-accent', bundle.accent || '#ffcb05');

    const pct = bundle.total ? Math.round((bundle.configured / bundle.total) * 100) : 0;
    const byId = {};
    (bundle.apis || []).forEach((a) => { byId[a.id] = a; });

    const valueProps = (bundle.value_props || []).map((v) =>
      `<li class="bundle-value-prop"><span class="bundle-value-tick">✓</span>${escapeHtml(v)}</li>`
    ).join('');

    const journey = (bundle.journey || [])
      .map((step, idx) => _bundleJourneyStepHtml(step, idx, byId))
      .join('');

    const walkthroughs = (bundle.walkthroughs || []).map((w) =>
      `<article class="bundle-walkthrough">
        <h4 class="bundle-walkthrough-title">${escapeHtml(w.title)}</h4>
        <p class="bundle-walkthrough-body">${escapeHtml(w.body)}</p>
      </article>`
    ).join('');

    const apiTiles = (bundle.apis || []).map((a) => _bundleApiTileHtml(bundle, a)).join('');

    const examplesChips = (bundle.examples || []).map((ex) =>
      `<span class="bundle-example-chip">${escapeHtml(ex)}</span>`
    ).join('');

    const bundleApiSet = new Set((bundle.apis || []).map((a) => a.id));
    const relevantUseCases = (USE_CASES || []).filter((uc) => {
      const ucApis = Array.isArray(uc.apis) ? uc.apis.filter((a) => typeof a === 'string' && a) : [];
      if (!ucApis.length) return false;
      return ucApis.every((a) => bundleApiSet.has(a));
    });
    const useCaseChips = relevantUseCases.map((uc) => {
      const blocked = _isNonUsBlockedUseCaseById(uc.id);
      const cls = 'bundle-use-case-chip' + (blocked ? ' blocked' : '');
      const title = blocked
        ? `${uc.name} — not available in your region`
        : `Open ${uc.name}`;
      return `<button class="${cls}" data-bundle-use-case="${escapeHtml(uc.id)}" title="${escapeHtml(title)}"${blocked ? ' disabled' : ''}>
        <span class="bundle-use-case-chip-arrow" aria-hidden="true">→</span>${escapeHtml(uc.name)}
      </button>`;
    }).join('');

    const heroVisual = _bundleHeroVisual(bundle.id);

    detail.innerHTML = `
      <header class="bundle-detail-header">
        <div class="bundle-detail-header-main">
          <span class="bundle-detail-icon" aria-hidden="true">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
              <path d="${escapeHtml(bundle.icon_path || '')}"></path>
            </svg>
          </span>
          <div>
            <div class="bundle-detail-eyebrow">Solution bundle</div>
            <h1 class="bundle-detail-title">${escapeHtml(bundle.name)}</h1>
            <p class="bundle-detail-tagline">${escapeHtml(bundle.tagline || '')}</p>
          </div>
        </div>
        <div class="bundle-detail-progress" title="${bundle.configured} of ${bundle.total} APIs configured">
          <span class="bundle-progress-text">${bundle.configured}<span class="bundle-progress-sep">/</span>${bundle.total}</span>
          <span class="bundle-progress-label">configured</span>
          <div class="bundle-progress-bar"><div class="bundle-progress-fill" style="width:${pct}%;"></div></div>
        </div>
      </header>

      ${heroVisual ? `<div class="bundle-hero-visual">${heroVisual}</div>` : ''}

      <p class="bundle-detail-desc">${escapeHtml(bundle.description || '')}</p>

      ${valueProps ? `<section class="bundle-section">
        <h3 class="bundle-section-title">What you can do with this bundle</h3>
        <ul class="bundle-value-props">${valueProps}</ul>
      </section>` : ''}

      ${journey ? `<section class="bundle-section">
        <h3 class="bundle-section-title">How the APIs fit together</h3>
        <ol class="bundle-journey">${journey}</ol>
      </section>` : ''}

      ${walkthroughs ? `<section class="bundle-section">
        <h3 class="bundle-section-title">Walkthroughs</h3>
        <div class="bundle-walkthroughs">${walkthroughs}</div>
      </section>` : ''}

      <section class="bundle-section">
        <h3 class="bundle-section-title">APIs in this bundle</h3>
        <div class="bundle-api-grid">${apiTiles}</div>
      </section>

      ${useCaseChips ? `<section class="bundle-section">
        <h3 class="bundle-section-title">Try it in these use cases</h3>
        <div class="bundle-use-cases-row">${useCaseChips}</div>
      </section>` : ''}

      ${examplesChips ? `<section class="bundle-section bundle-section--examples">
        <h3 class="bundle-section-title">Other example experiences</h3>
        <div class="bundle-examples-row">${examplesChips}</div>
      </section>` : ''}
    `;

    detail.querySelectorAll('[data-bundle-api]').forEach((btn) => {
      btn.addEventListener('click', () => {
        const apiId = btn.dataset.bundleApi;
        const apisTabBtn = document.querySelector('.top-tab[data-top-tab="apis"]');
        if (apisTabBtn) apisTabBtn.click();
        setTimeout(() => {
          const apiBtn = document.querySelector(`[data-api-id="${apiId}"]`);
          if (apiBtn) apiBtn.click();
        }, 0);
      });
    });

    detail.querySelectorAll('[data-bundle-use-case]').forEach((btn) => {
      btn.addEventListener('click', () => {
        const ucId = btn.dataset.bundleUseCase;
        if (_isNonUsBlockedUseCaseById(ucId)) return;
        const ucTabBtn = document.querySelector('.top-tab[data-top-tab="usecases"]');
        if (ucTabBtn) ucTabBtn.click();
        setTimeout(() => {
          const ucBtn = document.querySelector(`[data-uc-id="${ucId}"]`);
          if (ucBtn) ucBtn.click();
        }, 0);
      });
    });

    detail.scrollTop = 0;
  }

  function _hideSdkPanel() {
    const sdk = document.getElementById('sdk-panel');
    if (sdk) sdk.classList.add('hidden');
    if (window.__sdkDemo) window.__sdkDemo.stop();
    document.querySelectorAll('[data-sdk-id]').forEach((b) => b.classList.remove('active'));
  }

  function showBundleAbout() {
    const aboutPanel = document.getElementById('bundle-about-panel');
    const detail = document.getElementById('bundle-detail');
    if (aboutPanel) aboutPanel.classList.remove('hidden');
    if (detail) detail.classList.add('hidden');
    _hideSdkPanel();
    document.querySelectorAll('[data-bundle-id]').forEach((b) => b.classList.remove('active'));
    const aboutBtn = document.getElementById('bundle-about-btn');
    if (aboutBtn) aboutBtn.classList.add('active');
  }

  function selectBundle(id) {
    _hideSdkPanel();
    document.querySelectorAll('[data-bundle-id]').forEach((b) =>
      b.classList.toggle('active', b.dataset.bundleId === id)
    );
    const aboutBtn = document.getElementById('bundle-about-btn');
    if (aboutBtn) aboutBtn.classList.remove('active');
    loadBundles().then((bundles) => {
      const b = bundles.find((x) => x.id === id);
      if (b) renderBundleDetail(b);
    });
  }

  function selectSdk(id) {
    const aboutPanel = document.getElementById('bundle-about-panel');
    const detail = document.getElementById('bundle-detail');
    const sdk = document.getElementById('sdk-panel');
    if (aboutPanel) aboutPanel.classList.add('hidden');
    if (detail) detail.classList.add('hidden');
    document.querySelectorAll('[data-bundle-id]').forEach((b) => b.classList.remove('active'));
    const aboutBtn = document.getElementById('bundle-about-btn');
    if (aboutBtn) aboutBtn.classList.remove('active');
    document.querySelectorAll('[data-sdk-id]').forEach((b) =>
      b.classList.toggle('active', b.dataset.sdkId === id)
    );
    if (sdk) {
      sdk.classList.remove('hidden');
      sdk.scrollTop = 0;
    }
    _initSdkDemo();
    _initLiveDemo();
  }

  document.querySelectorAll('[data-bundle-id]').forEach((btn) => {
    btn.addEventListener('click', () => selectBundle(btn.dataset.bundleId));
  });
  document.querySelectorAll('[data-bundle-link]').forEach((btn) => {
    btn.addEventListener('click', () => selectBundle(btn.dataset.bundleLink));
  });
  document.querySelectorAll('[data-sdk-id]').forEach((btn) => {
    btn.addEventListener('click', () => selectSdk(btn.dataset.sdkId));
  });
  const _bundleAboutBtn = document.getElementById('bundle-about-btn');
  if (_bundleAboutBtn) _bundleAboutBtn.addEventListener('click', showBundleAbout);
