from typing import List, Dict, Union

from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import and_
from database.database import Session
from models.order import Order, OrderResponse
from utils import valid_orders, valid_orders_crud


class OrderRequest(BaseModel):
    status: str
    price: float
    quantity: int


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


def create_order(order: OrderResponse) -> OrderResponse:
    session = Session()
    new_order = Order(
        id=order.id,
        item=order.item,
        quantity=order.quantity,
        price=order.price,
        status=order.status
    )
    if not valid_orders_crud([new_order]):
        raise HTTPException(status_code=400, detail="price and quantity invalid")
    session.add(new_order)
    session.commit()
    session.close()
    return order


def update_order(order_id: int, updated_order: OrderResponse) -> dict:
    if updated_order.price < 0 or updated_order.quantity < 0:
        raise HTTPException(status_code=400, detail="price and quantity invalid")
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


def solution_orders_crud(orders: List[int]) -> dict[str, int]:
    session = Session()
    orders_list = session.query(Order).filter(Order.id.in_(orders))

    if not valid_orders_crud(orders_list):
        raise HTTPException(status_code=400, detail="price and quantity invalid")
    filtered_orders = [order for order in orders_list]
    revenue = sum(order.price * order.quantity for order in filtered_orders)
    return {"total_revenue": revenue}


def solution_orders(orders: List[Dict[str, any]], criterion: str) -> dict[str, int]:
    if not valid_orders(orders):
        raise HTTPException(status_code=400, detail="price and quantity invalid")
    filtered_orders = [order for order in orders if order.get('status') == criterion]
    revenue = sum(order.get('price', 0) * order.get('quantity', 0) for order in filtered_orders)
    return {"total_revenue": revenue}


