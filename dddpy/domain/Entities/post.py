from dddpy.domain.Enums import postCategory, postStatus
from typing import List


class Post:
    def __init__(self, name : str, category: postCategory, price: float, description: str, stock: int, images :List[str], status: postStatus):
        self.Name : str = name
        self.Descrption : str = description
        self.Stock : int = stock
        self.Images : List[str] = images
        self.Category: postCategory = category
        self.Price: float = price
        self.Status : postStatus = status