from sqlalchemy.orm import Session

from dddpy.application.Models.orderModel import CreateOrderModel
from dddpy.domain.Enums.orderStatus import orderStatus
from dddpy.domain.schemas.order_dto import OrderDTO
from dddpy.domain.schemas.post_dto import PostDTO
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository

def create_order_service(order:CreateOrderModel, db: Session) -> str:
    post_repository = GenericRepository(db, PostDTO)
    order_repository = GenericRepository(db, OrderDTO)

    post_entity = post_repository.get(order.postId)
    new_order = OrderDTO(user_id=order.userId, post_id=post_entity.id, quantity=order.quantity, total_amount=post_entity.price * order.quantity, status=orderStatus.CREATED)
    response = order_repository.add(new_order)
    return response.id