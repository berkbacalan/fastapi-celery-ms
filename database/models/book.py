from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)

    checkouts = relationship("Checkout", back_populates="book")
