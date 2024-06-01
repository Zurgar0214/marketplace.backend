from typing import List
from pydantic import BaseModel

from dddpy.application.Models.entityModel import EntityModel
from dddpy.application.Models.qualificationModel import QualificationModel
from dddpy.domain.schemas.post_dto import PostDTO


class PostDetailResponseModel(BaseModel, EntityModel):
    name:str
    category:int
    price:float
    description:str
    stock:int
    status:int
    qualifications: List[QualificationModel]

    def __init__(self, post :PostDTO, qualifications: List[QualificationModel]):
        self.name = post.name
        self.category = post.category
        self.qualifications = qualifications
        



    