import sqlite3

c = sqlite3.connect(r"tests/results.db")
tables = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")]
print("tables:", tables)

# Columns of suite_results
cols = [r[1] for r in c.execute("PRAGMA table_info(suite_results)")]
print("suite_results cols:", cols)

rid = c.execute("SELECT MAX(run_id) FROM suite_results").fetchone()[0]
print("latest run_id:", rid)

# Status breakdown for latest run
for status, n in c.execute(
    "SELECT status, COUNT(*) FROM suite_results WHERE run_id=? GROUP BY status", (rid,)
):
    print(f"  {status}: {n}")

print("\n--- non-pass tests (latest run) ---")
rows = c.execute(
    "SELECT suite, test_name, status, error_message FROM suite_results "
    "WHERE run_id=? AND status<>'pass'",
    (rid,),
).fetchall()
print("count:", len(rows))
for suite, name, status, err in rows[:60]:
    print(f"[{status}] {suite} :: {name}")
    if err:
        print("   ", (err or "").replace("\n", " ")[:240])
c.close()
