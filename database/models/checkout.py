from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base

class Checkout(Base):
    __tablename__ = "checkouts"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    patron_id = Column(Integer, ForeignKey("patrons.id"))
    checkout_date = Column(DateTime)
    due_date = Column(DateTime)

    book = relationship("Book", back_populates="checkouts")
    patron = relationship("Patron", back_populates="checkouts")
