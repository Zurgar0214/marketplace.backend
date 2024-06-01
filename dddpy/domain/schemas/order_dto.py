from datetime import datetime

from sqlalchemy import Column, String, ForeignKey, Float, DateTime, Enum
from sqlalchemy.orm import relationship

from dddpy.domain.Enums.orderStatus import orderStatus
from dddpy.insfrastructure.sqlite.database import Base

class OrderDTO(Base):
    __tablename__ = "Orders"
    id = Column(String, primary_key= True, index=True)
    user_id = Column(String, ForeignKey('Users.id'))
    user = relationship("UserDTO", back_populates="users")
    total_amount = Column(Float)
    creation_date = Column(DateTime)
    last_modified_date = Column(DateTime)
    post_id = Column(String, ForeignKey('Posts.id'), back_populates="posts")
    post = relationship("PostDTO")
    status = Column(Enum(orderStatus))
