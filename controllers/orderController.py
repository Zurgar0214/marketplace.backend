from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dddpy.application.Models.orderModel import CreateOrderModel
from dddpy.application.Services.orderService import create_order_service, get_all_orders_service, get_order_by_id_service
from dddpy.insfrastructure.sqlite.database import get_db

order_router = APIRouter(prefix="/order",tags=["order"])
@order_router.post(
        "/createOrder"
        )
async def create_order(order: CreateOrderModel, db: Session = Depends(get_db)) -> str:
    return create_order_service(order, db)

@order_router.get(
        "/getAllOrders"
        )
async def get_all_orders(db: Session = Depends(get_db)):
    return get_all_orders_service(db)

@order_router.get(
    "/getOrderById"
)
async def get_order_by_id(id: str, db: Session = Depends(get_db)):
    return get_order_by_id_service(id, db)
    