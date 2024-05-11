from dddpy.domain.Enums import orderStatus
from dddpy.domain.Entities.user import User
from dddpy.domain.Entities.post import Post

class Order:
    def __init__(self,status: orderStatus):
        self.Status :orderStatus = status
        self.User : User
        self.Post : Post