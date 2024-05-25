from pydantic import BaseModel
from dddpy.domain.Enums import postCategory, postStatus
from typing import List
from dddpy.domain.Entities.entity import Entity

class Post(Entity, BaseModel):
    def __init__(self,id: str, name : str, category: postCategory, price: float, description: str, stock: int, images :List[str], status: postStatus):
        super().__init__(id)
        self.Name : str = name
        self.Descrption : str = description
        self.Stock : int = stock
        self.Images : List[str] = images
        self.Category: postCategory = category
        self.Price: float = price
        self.Status : postStatus = status
