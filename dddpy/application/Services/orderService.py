from sqlalchemy.orm import Session

from dddpy.application.Models.orderModel import CreateOrderModel
from dddpy.domain.Enums.orderStatus import orderStatus
from dddpy.domain.schemas.order_dto import OrderDTO
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository

def create_order_service(order:CreateOrderModel, db: Session) -> str:
    new_order = OrderDTO(order.userId, order.productId, order.quantity, order.total, orderStatus.CREATED)
    repository = GenericRepository(db, OrderDTO)
    response = repository.add(new_order)
    return response