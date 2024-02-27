from pydantic import BaseModel
from datetime import datetime

class CheckoutBase(BaseModel):
    book_id: int
    patron_id: int

class CheckoutCreate(CheckoutBase):
    pass

class CheckoutUpdate(CheckoutBase):
    pass

class Checkout(CheckoutBase):
    id: int
    checkout_date: datetime
    due_date: datetime

    class Config:
        orm_mode = True
