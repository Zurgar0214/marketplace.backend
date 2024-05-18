from pydantic import BaseModel
from dddpy.application.Models.entityModel import EntityModel
from dddpy.domain.Enums.orderStatus import orderStatus


class Order(EntityModel, BaseModel):
    status: orderStatus
    userId: str
    postId: str