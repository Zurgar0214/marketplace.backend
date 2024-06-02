from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dddpy.application.Models.orderModel import CreateOrderModel
from dddpy.application.Services.orderService import create_order_service
from dddpy.insfrastructure.sqlite.database import get_db

order_router = APIRouter(prefix="/order",tags=["order"])
@order_router.post(
        "/createOrder"
        )
async def create_order(order: CreateOrderModel, db: Session = Depends(get_db)) -> str:
    return create_order_service(order, db)
    