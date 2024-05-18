from pydantic import BaseModel
from dddpy.application.Models.entityModel import EntityModel


class Post(BaseModel, EntityModel):
    name:str
    category:int
    price:float
    description:str
    stock:int
    status:int