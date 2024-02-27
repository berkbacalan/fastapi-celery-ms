from sqlalchemy.orm import Session
from app.core.repositories import checkout_repository

def create_checkout(db: Session, book_id: int, patron_id: int):
    from app.tasks.celery_worker import send_reminder_email
    checkout = checkout_repository.create_checkout(db, book_id, patron_id)
    if checkout:
        send_reminder_email.apply_async((checkout.id,), eta=checkout.due_date)
    return checkout

def get_checkout_by_id(db: Session, checkout_id: int):
    return checkout_repository.get_checkout_by_id(db, checkout_id)

def get_checked_out_books(db: Session):
    return checkout_repository.get_checked_out_books(db)

def get_overdue_books(db: Session):
    return checkout_repository.get_overdue_books(db)

def remove_checkout_by_id(db: Session, checkout_id: int):
    return checkout_repository.remove_check_out_by_id(db, checkout_id)
