from sqlalchemy.orm import Session
from database.models.patron import Patron

def get_patrons(db: Session):
    return db.query(Patron).all()

def get_patron_by_id(db: Session, patron_id: int):
    return db.query(Patron).filter(Patron.id == patron_id).first()

def create_patron(db: Session, name: str, email: str, password: str):
    db_patron = Patron(name=name, email=email, password=password)
    db.add(db_patron)
    db.commit()
    db.refresh(db_patron)
    return db_patron

def update_patron(db: Session, patron_id: int, name: str, email: str, password: str):
    db_patron = get_patron_by_id(db, patron_id)
    if db_patron:
        db_patron.name = name
        db_patron.email = email
        db_patron.password = password
        db.commit()
        db.refresh(db_patron)
        return db_patron
    return None

def delete_patron(db: Session, patron_id: int):
    db_patron = get_patron_by_id(db, patron_id)
    if db_patron:
        db.delete(db_patron)
        db.commit()
        return True
    return False
