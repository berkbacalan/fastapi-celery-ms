from sqlalchemy.orm import Session

from database.models.checkout import Checkout
from datetime import datetime, timedelta

def get_checkout_by_id(db: Session, checkout_id: int):
    return db.query(Checkout).filter(Checkout.id == checkout_id).first()

def create_checkout(db: Session, book_id: int, patron_id: int):
    checkout_date = datetime.now()
    due_date = checkout_date + timedelta(weeks=1)

    checkout = Checkout(book_id=book_id, patron_id=patron_id, checkout_date=checkout_date, due_date=due_date)
    db.add(checkout)
    db.commit()
    db.refresh(checkout)
    
    return checkout

def get_check_out_book_by_book_id(db: Session, book_id: int):
    return db.query(Checkout).filter(Checkout.book_id == book_id).first()

def get_checked_out_books(db: Session):
    return db.query(Checkout).all()

def get_overdue_books(db: Session):
    return db.query(Checkout).filter(Checkout.due_date < datetime.now()).all()

def remove_check_out_by_id(db: Session, id: int):
    db_checkout = get_checkout_by_id(db, id)
    if db_checkout:
        db.delete(db_checkout)
        db.commit()
        return True
    return False