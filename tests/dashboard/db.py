"""tests/dashboard/db.py — SQLite persistence for Vima test run results.

The database is stored at tests/results.db (gitignored).
Schema is created automatically on first use.
"""
from __future__ import annotations

import os
import sqlite3
from contextlib import contextmanager
from typing import Any, Dict, List, Optional

# DB lives next to this file's parent (tests/)
_TESTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DB_PATH = os.path.join(_TESTS_DIR, "results.db")

_PAGE_SIZE = 15

# ── Connection helper ──────────────────────────────────────────────────────────

@contextmanager
def _conn():
    con = sqlite3.connect(_DB_PATH)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA journal_mode=WAL")
    try:
        yield con
        con.commit()
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()


# ── Schema ─────────────────────────────────────────────────────────────────────

_SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    run_at          TEXT    NOT NULL,
    duration_seconds REAL   DEFAULT 0,
    install_type    TEXT    DEFAULT 'existing',
    os_name         TEXT,
    os_detail       TEXT,
    total_tests     INTEGER DEFAULT 0,
    passed_tests    INTEGER DEFAULT 0,
    failed_tests    INTEGER DEFAULT 0,
    scope           TEXT    DEFAULT 'smoke',
    base_url        TEXT,
    email_sent      INTEGER DEFAULT 0,
    email_sent_at   TEXT,
    email_error     TEXT,
    notes           TEXT
);

CREATE TABLE IF NOT EXISTS suite_results (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id        INTEGER NOT NULL REFERENCES runs(id) ON DELETE CASCADE,
    suite         TEXT    NOT NULL,
    test_name     TEXT    NOT NULL,
    status        TEXT    NOT NULL,
    error_message TEXT
);
"""

_initialized = False


def init_db() -> None:
    global _initialized
    if _initialized:
        return
    with _conn() as con:
        con.executescript(_SCHEMA)
    _initialized = True


# ── Write helpers ──────────────────────────────────────────────────────────────

def save_run(
    *,
    run_at: str,
    duration_seconds: float,
    install_type: str,
    os_name: str,
    os_detail: str,
    total_tests: int,
    passed_tests: int,
    failed_tests: int,
    scope: str,
    base_url: str,
    results: List[Dict[str, Any]],
) -> int:
    """Persist a completed test run. Returns the new run id."""
    with _conn() as con:
        cur = con.execute(
            """
            INSERT INTO runs
                (run_at, duration_seconds, install_type, os_name, os_detail,
                 total_tests, passed_tests, failed_tests, scope, base_url)
            VALUES (?,?,?,?,?,?,?,?,?,?)
            """,
            (
                run_at, duration_seconds, install_type, os_name, os_detail,
                total_tests, passed_tests, failed_tests, scope, base_url,
            ),
        )
        run_id = cur.lastrowid
        con.executemany(
            """
            INSERT INTO suite_results (run_id, suite, test_name, status, error_message)
            VALUES (?,?,?,?,?)
            """,
            [
                (
                    run_id,
                    r["suite"],
                    r["name"],
                    "pass" if r["passed"] else "fail",
                    r.get("message") or None,
                )
                for r in results
            ],
        )
    return run_id


def update_email_status(run_id: int, sent: bool, error: Optional[str]) -> None:
    import time as _time
    with _conn() as con:
        con.execute(
            """
            UPDATE runs SET email_sent=?, email_sent_at=?, email_error=? WHERE id=?
            """,
            (
                1 if sent else 0,
                _time.strftime("%Y-%m-%dT%H:%M:%S") if sent else None,
                error,
                run_id,
            ),
        )


# ── Read helpers ───────────────────────────────────────────────────────────────

def count_runs() -> int:
    init_db()
    with _conn() as con:
        row = con.execute("SELECT COUNT(*) FROM runs").fetchone()
        return row[0] if row else 0


def list_runs(page: int = 1, page_size: int = _PAGE_SIZE) -> List[sqlite3.Row]:
    init_db()
    offset = (page - 1) * page_size
    with _conn() as con:
        return con.execute(
            """
            SELECT * FROM runs ORDER BY id DESC LIMIT ? OFFSET ?
            """,
            (page_size, offset),
        ).fetchall()


def get_run(run_id: int) -> Optional[sqlite3.Row]:
    init_db()
    with _conn() as con:
        return con.execute("SELECT * FROM runs WHERE id=?", (run_id,)).fetchone()


def get_run_results(run_id: int) -> List[sqlite3.Row]:
    init_db()
    with _conn() as con:
        return con.execute(
            "SELECT * FROM suite_results WHERE run_id=? ORDER BY id",
            (run_id,),
        ).fetchall()


def get_stats() -> dict:
    """Return aggregated statistics for the stats dashboard."""
    init_db()
    with _conn() as con:
        summary_row = con.execute("""
            SELECT
                COUNT(*) as total_runs,
                COALESCE(SUM(total_tests), 0) as total_tests_run,
                ROUND(COALESCE(AVG(CAST(passed_tests AS FLOAT) / NULLIF(total_tests, 0) * 100), 0), 1) as avg_pass_rate,
                ROUND(COALESCE(AVG(CASE WHEN duration_seconds > 0 THEN duration_seconds END), 0), 1) as avg_duration,
                ROUND(COALESCE(MIN(CASE WHEN duration_seconds > 0 THEN duration_seconds END), 0), 1) as min_duration,
                SUM(CASE WHEN failed_tests = 0 AND total_tests > 0 THEN 1 ELSE 0 END) as perfect_runs
            FROM runs
        """).fetchone()

        trend_rows = con.execute("""
            SELECT id, run_at, total_tests, passed_tests, failed_tests,
                   duration_seconds, scope, os_name, install_type
            FROM runs ORDER BY id DESC LIMIT 50
        """).fetchall()

        reliability_rows = con.execute("""
            SELECT test_name, suite,
                   COUNT(*) as total_runs,
                   SUM(CASE WHEN status='pass' THEN 1 ELSE 0 END) as passes,
                   ROUND(CAST(SUM(CASE WHEN status='pass' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) * 100, 1) as pass_rate
            FROM suite_results
            GROUP BY test_name, suite
            ORDER BY pass_rate ASC, total_runs DESC
        """).fetchall()

        os_rows = con.execute(
            "SELECT COALESCE(os_name,'Unknown') as label, COUNT(*) as cnt FROM runs GROUP BY os_name ORDER BY cnt DESC"
        ).fetchall()
        scope_rows = con.execute(
            "SELECT COALESCE(scope,'smoke') as label, COUNT(*) as cnt FROM runs GROUP BY scope ORDER BY cnt DESC"
        ).fetchall()
        install_rows = con.execute(
            "SELECT COALESCE(install_type,'existing') as label, COUNT(*) as cnt FROM runs GROUP BY install_type ORDER BY cnt DESC"
        ).fetchall()

    trend = list(reversed([dict(r) for r in trend_rows]))
    all_rel = [dict(r) for r in reliability_rows]
    most_reliable = sorted(
        [r for r in all_rel if r["pass_rate"] == 100.0],
        key=lambda r: -r["total_runs"],
    )[:10]
    least_reliable = [r for r in all_rel if r["pass_rate"] < 100.0][:10]

    return {
        "summary": dict(summary_row) if summary_row else {
            "total_runs": 0, "total_tests_run": 0, "avg_pass_rate": 0.0,
            "avg_duration": 0.0, "min_duration": 0.0, "perfect_runs": 0,
        },
        "trend": trend,
        "most_reliable": most_reliable,
        "least_reliable": least_reliable,
        "os_breakdown": [dict(r) for r in os_rows],
        "scope_breakdown": [dict(r) for r in scope_rows],
        "install_breakdown": [dict(r) for r in install_rows],
    }
