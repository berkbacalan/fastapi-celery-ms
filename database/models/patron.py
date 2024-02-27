from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Patron(Base):
    __tablename__ = "patrons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    checkouts = relationship("Checkout", back_populates="patron")
