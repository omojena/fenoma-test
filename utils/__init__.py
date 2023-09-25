from typing import List, Dict

from models.order import Order


def valid_orders_crud(orders: list[Order]) -> bool:
    for order_data in orders:
        price = order_data.price
        quantity = order_data.quantity

        if price < 0 or quantity < 0:
            return False
    return True


def valid_orders(orders: List[Dict[str, any]]) -> bool:
    for order_data in orders:
        price = order_data.get("price", 0)
        quantity = order_data.get("quantity", 0)

        if price < 0 or quantity < 0:
            return False

    return True
