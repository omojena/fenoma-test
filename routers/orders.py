from typing import Dict, Any, List

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from services.orders import get_orders, get_order, create_order, update_order, delete_order, solution_orders, \
    solution_orders_crud
from models.order import OrderResponse

router = APIRouter(prefix='/orders', tags=['Orders'])


@router.get("/")
async def fetch_orders():
    return get_orders()


@router.get("/{order_id}")
async def fetch_order(order_id: int):
    return get_order(order_id)


@router.post("/", response_model=OrderResponse)
async def add_order(order: OrderResponse) -> OrderResponse:
    return create_order(order)


@router.patch("/{order_id}")
async def edit_order(order_id: int, order: OrderResponse) -> dict:
    return update_order(order_id, order)


@router.patch("/{order_id}")
async def remove_order(order_id: int) -> dict:
    return delete_order(order_id)


@router.post("/solution", response_model=None)
async def solution_order(payload: Dict[str, Any]):
    orders = payload["orders"]
    criterion = payload["criterion"]
    result = solution_orders(orders, criterion)
    return JSONResponse(result)


@router.post("/solution/crud", response_model=None)
async def solution_order(orders: List[int]):
    result = solution_orders_crud(orders)
    return JSONResponse(result)
