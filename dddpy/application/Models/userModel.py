from pydantic import BaseModel, EmailStr, Field

from dddpy.application.Models.entityModel import EntityModel


class UserModel(BaseModel):
    name: str = Field(pattern= "^[a-zA-Z]{3,50}$", description="El campo nombres debe contener mínimo 3 y máximo 50 caracteres válidos")
    lastName: str = Field(pattern="^[a-zA-Z]{3,50}$", description="El campo apellidos debe contener mínimo 3 y máximo 50 caracteres válidos")
    email: EmailStr = Field(default="no@gmail.com")
    phone: str = Field(pattern='^\d{10}$', description="El campo nombre debe contener solo caracteres numéricos hasta un máximo de 10")
    password: str = Field(pattern="", min_length=8, description="Password must be at least 8 characters long, contain one uppercase letter, and one number")