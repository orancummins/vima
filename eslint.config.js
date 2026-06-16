// eslint.config.js — ESLint 10 flat config
// No npm dependencies required — all rules and globals are defined inline.
// CJS format because there is no package.json with "type":"module" in this project.
"use strict";

module.exports = [
  // ── Global ignores ────────────────────────────────────────────────────────
  {
    ignores: [
      "usecases/**",
      "chat/**",
      "simulator/**",
      "tools/**",
      "tests/**",
      "static/globe.js",
      "**/*.min.js",
    ],
  },

  // ── Main config (all other JS) ────────────────────────────────────────────
  {
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "script",
      globals: {
        // Browser built-ins
        window: "readonly",
        document: "readonly",
        navigator: "readonly",
        location: "readonly",
        history: "readonly",
        screen: "readonly",
        self: "readonly",
        globalThis: "readonly",
        // I/O & timers
        console: "readonly",
        setTimeout: "readonly",
        clearTimeout: "readonly",
        setInterval: "readonly",
        clearInterval: "readonly",
        requestAnimationFrame: "readonly",
        cancelAnimationFrame: "readonly",
        // Networking
        fetch: "readonly",
        Request: "readonly",
        Response: "readonly",
        Headers: "readonly",
        FormData: "readonly",
        XMLHttpRequest: "readonly",
        EventSource: "readonly",
        AbortController: "readonly",
        AbortSignal: "readonly",
        // URL / encoding
        URL: "readonly",
        URLSearchParams: "readonly",
        encodeURIComponent: "readonly",
        decodeURIComponent: "readonly",
        encodeURI: "readonly",
        decodeURI: "readonly",
        atob: "readonly",
        btoa: "readonly",
        // Storage
        localStorage: "readonly",
        sessionStorage: "readonly",
        // UI / DOM
        alert: "readonly",
        confirm: "readonly",
        prompt: "readonly",
        Event: "readonly",
        CustomEvent: "readonly",
        MouseEvent: "readonly",
        KeyboardEvent: "readonly",
        MutationObserver: "readonly",
        IntersectionObserver: "readonly",
        ResizeObserver: "readonly",
        HTMLElement: "readonly",
        Element: "readonly",
        Node: "readonly",
        NodeList: "readonly",
        SVGElement: "readonly",
        performance: "readonly",
        // Primitives & stdlib
        Promise: "readonly",
        JSON: "readonly",
        Math: "readonly",
        Date: "readonly",
        Array: "readonly",
        Object: "readonly",
        String: "readonly",
        Number: "readonly",
        Boolean: "readonly",
        RegExp: "readonly",
        Error: "readonly",
        Map: "readonly",
        Set: "readonly",
        WeakMap: "readonly",
        WeakSet: "readonly",
        Symbol: "readonly",
        Proxy: "readonly",
        Reflect: "readonly",
        Uint8Array: "readonly",
        ArrayBuffer: "readonly",
        DataView: "readonly",
        Blob: "readonly",
        File: "readonly",
        FileReader: "readonly",
        TextDecoder: "readonly",
        TextEncoder: "readonly",
        crypto: "readonly",
        // Web Components
        customElements: "readonly",
        HTMLTemplateElement: "readonly",
        ShadowRoot: "readonly",
        // CSS API
        CSS: "readonly",
        CSSStyleSheet: "readonly",
        // Type helpers
        isNaN: "readonly",
        isFinite: "readonly",
        parseInt: "readonly",
        parseFloat: "readonly",
        undefined: "readonly",
        NaN: "readonly",
        Infinity: "readonly",
        // Node globals sometimes referenced in build/test scripts
        process: "readonly",
        __dirname: "readonly",
        __filename: "readonly",
        module: "readonly",
        require: "readonly",
        exports: "readonly",
      },
    },
    rules: {
      // ── eslint:recommended subset ─────────────────────────────────────────
      "no-undef": "error",
      "no-dupe-keys": "error",
      "no-dupe-args": "error",
      "no-dupe-else-if": "error",
      "no-duplicate-case": "error",
      "no-empty": ["warn", { allowEmptyCatch: true }],
      "no-extra-boolean-cast": "warn",
      "no-extra-semi": "warn",
      "no-fallthrough": "error",
      "no-redeclare": "error",
      "no-unreachable": "error",
      "no-unsafe-finally": "error",
      "no-constant-condition": ["error", { checkLoops: false }],
      "no-debugger": "warn",
      "use-isnan": "error",
      "valid-typeof": ["error", { requireStringLiterals: true }],
      // ── Custom rules ──────────────────────────────────────────────────────
      // Underscore-prefixed names are private/future-use by convention.
      // args/caughtErrors are excluded because callback signatures must match.
      "no-unused-vars": ["warn", { args: "none", caughtErrors: "none", varsIgnorePattern: "^_" }],
      "no-console": "off",
    },
  },

  // ── ES module override (must come last to win over the sourceType above) ──
  // static/js/app/** uses import/export; parse as ES modules.
  {
    files: ["static/js/app/**/*.js"],
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "module",
    },
  },
];
