from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from dddpy.insfrastructure.sqlite.database import Base

class QualificationDTO(Base):
    __tablename__ = "Qualifications"
    id = Column(String, primary_key=True, index=True)
    order_id = Column(String, ForeignKey('Orders.id'))
    score = Column(Integer)
    comment = Column(String)
    creation_date = Column(DateTime)
    last_modified_date = Column(DateTime)
    order = relationship("OrderDTO", back_populates="qualifications")
