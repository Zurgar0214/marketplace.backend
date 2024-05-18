# dto/post_dto.py
from sqlalchemy import Column, Integer, String, Float
from dddpy.insfrastructure.sqlite.database import Base


class PostDTO(Base):
    __tablename__ = "Posts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(Integer)
    price = Column(Float)
    description = Column(String)
    stock = Column(Integer)
    status = Column(Integer)
