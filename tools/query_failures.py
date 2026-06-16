import sqlite3
db = 'C:/Users/e031093/dev/vima/tests/results.db'
c = sqlite3.connect(db)
rows = c.execute(
    "SELECT run_id,suite,test_name,status,error_message FROM suite_results "
    "WHERE run_id IN (33,34) AND status <> 'pass'"
).fetchall()
for r in rows:
    print(f"Run {r[0]} | {r[1]} | {r[2]} | {r[3]}")
    if r[4]:
        print(f"  ERROR: {r[4][:300]}")
c.close()
