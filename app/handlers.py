import os

from app.db import get_connection, run_query

REPORT_ROOT = "/var/reports"


def handle_search(request):
    term = request.args.get("q", "")
    conn = get_connection("app.sqlite3")
    return run_query(conn, "orders", term)


def handle_download(request):
    name = request.args.get("file", "")
    handle = open(os.path.join(REPORT_ROOT, name))
    return handle.read()
