from sqlalchemy import Column, DateTime, String
from dddpy.insfrastructure.sqlite.database import Base

class UserDTO(Base):
    __tablename__ = "Users"
    id = Column(String, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    creation_date = Column(DateTime)
    last_modified_date = Column(DateTime)
