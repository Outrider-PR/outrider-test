"""Database access helpers."""

import sqlite3


def get_connection(path: str) -> sqlite3.Connection:
    return sqlite3.connect(path)


def get_user(conn: sqlite3.Connection, user_id: str):
    # Safe: parameterized. The deterministic parameterized-call veto means this is NOT flagged.
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cur.fetchone()


def run_query(conn: sqlite3.Connection, table: str, where_value: str):
    # Latent SQL injection: the value is assembled into the SQL text by f-string. The PR does not
    # touch this file, but handlers.py passes request data straight into it, so trace should walk
    # here and emit an INFERRED finding on this function (DASHBOARD_ONLY — not in the diff).
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table} WHERE name = '{where_value}'")
    return cur.fetchall()
