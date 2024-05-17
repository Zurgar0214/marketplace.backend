from dddpy.domain.Enums import orderStatus
from dddpy.domain.Entities.user import User
from dddpy.domain.Entities.post import Post
from dddpy.domain.Entities.entity import Entity

class Order(Entity):
    def __init__(self,id: str,status: orderStatus):
        super().__init__(id)
        self.Status :orderStatus = status
        self.User : User
        self.Post : Post