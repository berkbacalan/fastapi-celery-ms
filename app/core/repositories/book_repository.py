from sqlalchemy.orm import Session
from database.models.book import Book

def get_books(db: Session):
    return db.query(Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, title: str, author: str):
    db_book = Book(title=title, author=author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, title: str, author: str):
    db_book = get_book_by_id(db, book_id)
    if db_book:
        db_book.title = title
        db_book.author = author
        db.commit()
        db.refresh(db_book)
        return db_book
    return None

def delete_book(db: Session, book_id: int):
    db_book = get_book_by_id(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    return False
