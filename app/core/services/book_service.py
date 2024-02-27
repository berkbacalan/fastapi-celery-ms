from sqlalchemy.orm import Session
from app.core.repositories import book_repository
from app.core.repositories import checkout_repository

def get_books(db: Session):
    return book_repository.get_books(db)

def get_book_by_id(db: Session, book_id: int):
    return book_repository.get_book_by_id(db, book_id)

def create_book(db: Session, title: str, author: str):
    return book_repository.create_book(db, title, author)

def update_book(db: Session, book_id: int, title: str, author: str):
    is_checkout = checkout_repository.get_check_out_book_by_book_id(db, book_id)
    if not is_checkout:
        return False
    return book_repository.update_book(db, book_id, title, author)

def delete_book(db: Session, book_id: int):
    is_checkout = checkout_repository.get_check_out_book_by_book_id(db, book_id)
    if not is_checkout:
        return False
    return book_repository.delete_book(db, book_id)
