"""Simulator data store — SQLite-backed, lazy-loads from fixture JSON files."""
from __future__ import annotations
import json
import sqlite3
from pathlib import Path

_FIXTURES_DIR = Path(__file__).parent / "fixtures"
_DB_PATH = Path(__file__).parent / "sim_data.db"


class SimDataStore:
    def __init__(self):
        self._loaded: set[str] = set()
        self._db = sqlite3.connect(str(_DB_PATH), check_same_thread=False)
        self._db.execute(
            "CREATE TABLE IF NOT EXISTS records "
            "(api TEXT, resource TEXT, id TEXT, data TEXT, "
            "PRIMARY KEY(api, resource, id))"
        )
        self._db.commit()

    def lazy_load(self, api: str):
        if api in self._loaded:
            return
        path = _FIXTURES_DIR / f"{api}.json"
        if path.exists():
            self.load_fixtures(api, path)
        self._loaded.add(api)

    def load_fixtures(self, api: str, path):
        with open(path) as f:
            data = json.load(f)
        for resource, records in data.items():
            for i, rec in enumerate(records):
                rid = str(
                    rec.get("id",
                    rec.get("binNum",
                    rec.get("locationId",
                    rec.get("uuid",
                    rec.get("offerId", i)))))
                )
                self.put(api, resource, rid, rec)

    def put(self, api: str, resource: str, id: str, data: dict):
        self._db.execute(
            "INSERT OR REPLACE INTO records VALUES (?,?,?,?)",
            (api, resource, str(id), json.dumps(data))
        )
        self._db.commit()

    def get(self, api: str, resource: str, id: str) -> dict | None:
        row = self._db.execute(
            "SELECT data FROM records WHERE api=? AND resource=? AND id=?",
            (api, resource, str(id))
        ).fetchone()
        return json.loads(row[0]) if row else None

    def list(self, api: str, resource: str) -> list[dict]:
        rows = self._db.execute(
            "SELECT data FROM records WHERE api=? AND resource=?",
            (api, resource)
        ).fetchall()
        return [json.loads(r[0]) for r in rows]

    def delete(self, api: str, resource: str, id: str):
        self._db.execute(
            "DELETE FROM records WHERE api=? AND resource=? AND id=?",
            (api, resource, str(id))
        )
        self._db.commit()

    def reset(self, api: str):
        self._db.execute("DELETE FROM records WHERE api=?", (api,))
        self._db.commit()
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


store = SimDataStore()
