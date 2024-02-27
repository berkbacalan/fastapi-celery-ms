from sqlalchemy.orm import Session
from app.core.repositories import patron_repository

def get_patrons(db: Session):
    return patron_repository.get_patrons(db)

def get_patron_by_id(db: Session, patron_id: int):
    return patron_repository.get_patron_by_id(db, patron_id)

def create_patron(db: Session, name: str, email: str, password: str):
    return patron_repository.create_patron(db, name, email, password)

def update_patron(db: Session, patron_id: int, name: str, email: str, password: str):
    return patron_repository.update_patron(db, patron_id, name, email, password)

def delete_patron(db: Session, patron_id: int):
    return patron_repository.delete_patron(db, patron_id)
