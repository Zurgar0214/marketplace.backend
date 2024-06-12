from fastapi import File, UploadFile
from pydantic import BaseModel
from sqlalchemy import Double
from dddpy.application.Models.entityModel import EntityModel


class PostModel(BaseModel, EntityModel):
    createdUser: str
    name:str
    category:int
    price:float
    description:str
    stock:int
    status:int

class CreatePostModel(BaseModel):
    createdUser: str
    name:str
    category:int
    price: float
    description:str
    stock:int
    status:int