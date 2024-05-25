from pydantic import BaseModel

from dddpy.application.Models.entityModel import EntityModel


class UserModel(EntityModel, BaseModel):
    name: str
    lastName: str
    email: str
    phone: str
    password: str