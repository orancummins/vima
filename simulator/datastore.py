"""Simulator data store — one SQLite DB per API, committed to source control."""
from __future__ import annotations

import json
import sqlite3
import threading
from pathlib import Path

_FIXTURES_DIR = Path(__file__).parent / "fixtures"
_DB_DIR = Path(__file__).parent / "db"
_DB_DIR.mkdir(exist_ok=True)

_SCHEMA = (
    "CREATE TABLE IF NOT EXISTS records "
    "(resource TEXT, id TEXT, data TEXT, "
    "captured INTEGER DEFAULT 0, "
    "PRIMARY KEY(resource, id))"
)


def _id_for(rec: dict, i: int) -> str:
    for key in ("id", "binNum", "locationId", "uuid", "offerId",
                "merchantCategoryCode", "industry", "transUid",
                "cardReference", "orderId", "reportId"):
        if rec.get(key) is not None:
            return str(rec[key])
    return str(i)


class SimDataStore:
    def __init__(self):
        self._loaded: set[str] = set()
        self._conns: dict[str, sqlite3.Connection] = {}
        self._lock = threading.Lock()

    def _conn(self, api: str) -> sqlite3.Connection:
        with self._lock:
            if api not in self._conns:
                path = _DB_DIR / f"{api}.db"
                conn = sqlite3.connect(str(path), check_same_thread=False)
                conn.execute(_SCHEMA)
                conn.commit()
                self._conns[api] = conn
            return self._conns[api]

    def lazy_load(self, api: str):
        """Seed from fixture JSON only if the DB has no records at all."""
        if api in self._loaded:
            return
        conn = self._conn(api)
        count = conn.execute("SELECT COUNT(*) FROM records").fetchone()[0]
        if count == 0:
            path = _FIXTURES_DIR / f"{api}.json"
            if path.exists():
                self._load_fixtures(api, path)
        self._loaded.add(api)

    def _load_fixtures(self, api: str, path: Path):
        conn = self._conn(api)
        with open(path) as f:
            data = json.load(f)
        for resource, records in data.items():
            for i, rec in enumerate(records):
                rid = _id_for(rec, i)
                conn.execute(
                    "INSERT OR REPLACE INTO records VALUES (?,?,?,0)",
                    (resource, rid, json.dumps(rec))
                )
        conn.commit()

    def put(self, api: str, resource: str, id: str, data: dict, captured: bool = False):
        conn = self._conn(api)
        conn.execute(
            "INSERT OR REPLACE INTO records VALUES (?,?,?,?)",
            (resource, str(id), json.dumps(data), 1 if captured else 0)
        )
        conn.commit()

    def get(self, api: str, resource: str, id: str) -> dict | None:
        row = self._conn(api).execute(
            "SELECT data FROM records WHERE resource=? AND id=?",
            (resource, str(id))
        ).fetchone()
        return json.loads(row[0]) if row else None

    def list(self, api: str, resource: str) -> list[dict]:
        rows = self._conn(api).execute(
            "SELECT data FROM records WHERE resource=? ORDER BY rowid",
            (resource,)
        ).fetchall()
        return [json.loads(r[0]) for r in rows]

    def delete(self, api: str, resource: str, id: str):
        conn = self._conn(api)
        conn.execute(
            "DELETE FROM records WHERE resource=? AND id=?",
            (resource, str(id))
        )
        conn.commit()

    def reset(self, api: str):
        conn = self._conn(api)
        conn.execute("DELETE FROM records")
        conn.commit()
        self._loaded.discard(api)

    def search(self, api: str, resource: str, filters: list[dict]) -> list[dict]:
        records = self.list(api, resource)
        for f in filters:
            k, v = f.get("key"), str(f.get("value", ""))
            records = [r for r in records if str(r.get(k, "")).lower().startswith(v.lower())]
        return records

    def search_field(self, api: str, resource: str, field: str, value: str) -> list[dict]:
        records = self.list(api, resource)
        v = str(value).lower()
        return [r for r in records if str(r.get(field, "")).lower() == v]

    def upsert_many(self, api: str, resource: str, records: list[dict], id_field: str):
        """Upsert a batch of records from a live API capture."""
        if not records:
            return
        conn = self._conn(api)
        for i, rec in enumerate(records):
            rid = str(rec.get(id_field) or _id_for(rec, i))
            conn.execute(
                "INSERT OR REPLACE INTO records VALUES (?,?,?,1)",
                (resource, rid, json.dumps(rec))
            )
        conn.commit()

    def stats(self, api: str) -> dict:
        conn = self._conn(api)
        rows = conn.execute(
            "SELECT resource, COUNT(*), SUM(captured) FROM records GROUP BY resource"
        ).fetchall()
        return {r[0]: {"total": r[1], "captured": r[2] or 0} for r in rows}


store = SimDataStore()
