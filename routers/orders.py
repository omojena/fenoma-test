from fastapi import APIRouter
from services.orders import get_orders, get_order, create_order, update_order, delete_order
from models.order import CreateOrderRequest, UpdateOrderRequest, Order

router = APIRouter(prefix='/orders', tags=['Orders'])


@router.get("/")
async def fetch_orders():
    return get_orders()


@router.get("/{order_id}")
async def fetch_order(order_id: int):
    return get_order(order_id)


@router.post("/")
async def add_order(order: CreateOrderRequest) -> dict:
    return create_order(order)


@router.patch("/{order_id}")
async def edit_order(order_id: int, order: UpdateOrderRequest) -> dict:
    return update_order(order_id, order)


@router.patch("/{order_id}")
async def remove_order(order_id: int) -> dict:
    return delete_order(order_id)
