from sqlalchemy import Column, DateTime, String
from dddpy.insfrastructure.sqlite.database import Base

class UserDTO(Base):
    __tablename__ = "Users"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    lastName = Column(String)
    email = Column(String)
    phone = Column(String)
    password = Column(String)
    creation_date = Column(DateTime)
    last_modified_date = Column(DateTime)

    def createUser(name : str,lastName : str, email: str, phone: str, password: str ):
        return UserDTO( name = name, lastName = lastName, email = email, phone = phone, password = password
                       creation_date = DateTime)