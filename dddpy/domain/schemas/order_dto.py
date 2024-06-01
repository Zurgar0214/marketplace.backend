from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime

from dddpy.insfrastructure.sqlite.database import Base

class OrderDTO(Base):
    __tablename__ = "Orders"
    id = Column(String, primary_key= True, index=True)
    user_id = Column(String, ForeignKey('Users.id'))
    total_amount = Column(Float)
    creation_date = Column(DateTime)
    last_modified_date = Column(DateTime)
    post_id = Column(String, ForeignKey('Posts.id'))
    post = relationship("PostDTO", back_populates="orders")
    qualifications = relationship("QualificationDTO", back_populates="order")
