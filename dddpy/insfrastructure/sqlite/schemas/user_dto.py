from datetime import datetime
from sqlalchemy import Column, DateTime, String
from dddpy.insfrastructure.sqlite.database import Base
import uuid
from dddpy.insfrastructure.services import EncryptService

class UserDTO(Base):
    __tablename__ = "Users"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    lastName = Column(String)
    name = Column(String)
    lastName = Column(String)
    email = Column(String)
    password = Column(String)
    phone = Column(String)
    password = Column(String)
    creation_date = Column(DateTime)
    last_modified_date = Column(DateTime)

    def __init__(self, name, lastName, email, phone, password):
        self.id = str(uuid.uuid4())
        self.name = name
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.password = EncryptService.encrypt_password(password)
        self.creation_date = datetime.now()
        self.last_modified_date = self.creation_date

    #     return UserDTO( name = name, lastName = lastName, email = email, phone = phone, password = password
    #                    creation_date = DateTime)