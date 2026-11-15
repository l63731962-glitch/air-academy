"""One-off: copy an existing SQLite database into your Supabase Postgres database.

    python migrate_sqlite_to_supabase.py            # reads ./academy.db
    python migrate_sqlite_to_supabase.py path/to/academy.db

Needs DATABASE_URL set (in .env or the shell). Safe to run more than once: rows that are already there are skipped.
Skipped on purpose: courses (rebuilt from courses_seed.py on every start), sign-in codes and half-finished sign-ups
(they expire within minutes anyway).
"""
import os
import sqlite3
import sys

import psycopg

import app   # importing it connects to DATABASE_URL and creates any missing tables

SOURCE = sys.argv[1] if len(sys.argv) > 1 else os.getenv("DATABASE_PATH", "academy.db")
# Parents before children, so foreign keys are satisfied.
TABLES = ("users", "enrollments", "payments", "progress", "scores", "certificates",
          "class_groups", "class_group_courses", "class_group_members", "purchase_requests")
COUNTERS = ("scores", "purchase_requests")   # tables whose id counts up on its own

if not os.path.exists(SOURCE):
    sys.exit(f"Cannot find the SQLite file: {SOURCE}")

src = sqlite3.connect(SOURCE)
src.row_factory = sqlite3.Row
have = {r[0] for r in src.execute("SELECT name FROM sqlite_master WHERE type='table'")}

with psycopg.connect(app._dsn(), prepare_threshold=None) as dst:
    for t in TABLES:
        if t not in have:
            print(f"{t:<22} not in the SQLite file, skipped")
            continue
        theirs = {r[0] for r in dst.execute(
            "SELECT column_name FROM information_schema.columns WHERE table_schema='public' AND table_name=%s", (t,))}
        rows = src.execute(f"SELECT * FROM {t}").fetchall()
        cols = [c for c in (rows[0].keys() if rows else []) if c in theirs]
        added = 0
        if rows:
            sql = f"INSERT INTO {t}({','.join(cols)}) VALUES({','.join(['%s'] * len(cols))}) ON CONFLICT DO NOTHING"
            for r in rows:
                added += dst.execute(sql, [r[c] for c in cols]).rowcount
        print(f"{t:<22} {len(rows):>5} found, {added:>5} copied, {len(rows) - added:>5} already there")
    for t in COUNTERS:   # keep new ids counting up from the highest copied one
        dst.execute(f"SELECT setval(pg_get_serial_sequence('{t}','id'), m) FROM (SELECT MAX(id) m FROM {t}) x WHERE m IS NOT NULL")
    print("Done. Committed.")