from database.database import Session
from models.order import Order, CreateOrderRequest, UpdateOrderRequest


def get_orders() -> list:
    session = Session()
    orders = session.query(Order).all()
    session.close()
    return orders


def get_order(order_id: int) -> Order:
    session = Session()
    order = session.query(Order).filter(Order.id == order_id).first()
    session.close()
    return order


def create_order(order: CreateOrderRequest) -> dict:
    session = Session()
    session.add(order)
    session.commit()
    session.close()
    return {"message": "Order created successfully", "order_id": order.id}


def update_order(order_id: int, updated_order: UpdateOrderRequest) -> dict:
    session = Session()
    order = session.query(Order).filter(Order.id == order_id).first()
    if order:
        order.item = updated_order.item
        order.quantity = updated_order.quantity
        order.price = updated_order.price
        order.status = updated_order.status
        session.commit()
        session.close()
        return {"message": "Order updated successfully"}
    session.close()
    return {"message": "Order not found"}


def delete_order(order_id: int) -> dict:
    session = Session()
    order = session.query(Order).filter(Order.id == order_id).first()
    if order:
        session.delete(order)
        session.commit()
        session.close()
        return {"message": "Order deleted successfully"}
    session.close()
    return {"message": "Order not found"}
