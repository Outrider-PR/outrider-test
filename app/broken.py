def compute_total(items):
    total = 0
    for item in items:
        total += item.price
    return total


def apply_discount(order, rate:
    return order.total * (1 - rate)
