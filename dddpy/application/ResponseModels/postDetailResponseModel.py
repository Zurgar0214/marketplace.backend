from typing import List
from pydantic import BaseModel

from dddpy.application.Models.entityModel import EntityModel
from dddpy.application.Models.qualificationModel import QualificationModel
from dddpy.domain.schemas.post_dto import PostDTO


class PostDetailResponseModel(EntityModel):
    name:str
    category:int
    price:float
    description:str
    stock:int
    status:int
    qualifications: List[QualificationModel]
    images: List[str]

    def __init__(self, post :PostDTO, qualifications: List[QualificationModel]):
        self.id = post.id
        self.name = post.name
        self.category = post.category
        self.price = post.price
        self.description = post.description
        self.stock = post.stock
        self.status = post.status
        self.creationDate = post.creation_date
        self.qualifications = qualifications
        



    