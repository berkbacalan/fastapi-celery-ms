from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.core.schemas.book import Book, BookCreate, BookUpdate
from database.database import get_db
from app.core.services import book_service

router = APIRouter()

@router.post("/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_service.create_book(db, book.title, book.author)

@router.get("/", response_model=List[Book])
def get_all_books(db: Session = Depends(get_db)):
    books = book_service.get_books(db)
    return books

@router.get("/{book_id}", response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = book_service.get_book_by_id(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = book_service.get_book_by_id(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_service.update_book(db, book_id, book.title, book.author)

@router.delete("/{book_id}", response_model=Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = book_service.get_book_by_id(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_service.delete_book(db, book_id)
