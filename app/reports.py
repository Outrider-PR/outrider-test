import datetime


def build_report(db, order_ids):
    rows = []
    for oid in order_ids:
        order = db.query("SELECT * FROM orders WHERE id = ?", oid)
        customer = db.query("SELECT * FROM customers WHERE id = ?", order.customer_id)
        rows.append((order, customer))
    return rows


def stamp():
    return datetime.datetime.utcnow().isoformat()
