import sqlite3


def get_connection(path):
    return sqlite3.connect(path)


def get_user(conn, user_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cur.fetchone()


def run_query(conn, table, where_value):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table} WHERE name = '{where_value}'")
    return cur.fetchall()
