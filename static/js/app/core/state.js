// -------------------------------------------------------------------
// core/state.js
// Single source of truth for the API workbench's mutable selection
// state. Extracted from main.js so the workbench render/send modules,
// the API Guide, the snippets drawer and the setup modal can all read
// the same selection without closure coupling.
//
// The scalar selection (api id / op id / server state) is private and
// reached through accessors because ES module `let` bindings are
// read-only to importers. The two caches are plain objects mutated in
// place, so they are exported directly.
// -------------------------------------------------------------------
import { APIS } from './env.js';

let _currentApiId = null; // null = About panel shown; set when user selects an API
let _currentOpId = null;
let _currentState = {};

// ioCache[apiId][opId] = { request, response, statusCode, hint, ... }
export const ioCache = {};
// lastOpByApi[apiId] = opId
export const lastOpByApi = {};

export function getCurrentApiId() { return _currentApiId; }
export function setCurrentApiId(v) { _currentApiId = v; }

export function getCurrentOpId() { return _currentOpId; }
export function setCurrentOpId(v) { _currentOpId = v; }

export function getCurrentState() { return _currentState; }
export function setCurrentState(v) { _currentState = v; }

export function currentApi() {
  return APIS.find((a) => a.id === _currentApiId);
}

export function currentOp() {
  const a = currentApi();
  if (!a) return null;
  return a.operations.find((o) => o.id === _currentOpId);
}
