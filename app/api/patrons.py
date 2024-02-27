from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.core.schemas.patron import Patron, PatronCreate, PatronUpdate
from database.database import get_db
from app.core.services import patron_service

router = APIRouter()

@router.post("/", response_model=Patron)
def create_patron(patron: PatronCreate, db: Session = Depends(get_db)):
    return patron_service.create_patron(db, patron.name, patron.email, patron.password)

@router.get("/", response_model=List[Patron])
def get_all_patrons(db: Session = Depends(get_db)):
    patrons = patron_service.get_patrons(db)
    return patrons

@router.get("/{patron_id}", response_model=Patron)
def get_patron_by_id(patron_id: int, db: Session = Depends(get_db)):
    db_patron = patron_service.get_patron_by_id(db, patron_id)
    if db_patron is None:
        raise HTTPException(status_code=404, detail="Patron not found")
    return db_patron

@router.put("/{patron_id}", response_model=Patron)
def update_patron(patron_id: int, patron: PatronUpdate, db: Session = Depends(get_db)):
    db_patron = patron_service.get_patron_by_id(db, patron_id)
    if db_patron is None:
        raise HTTPException(status_code=404, detail="Patron not found")
    return patron_service.update_patron(db, patron_id, patron.name, patron.email, patron.password)

@router.delete("/{patron_id}", response_model=Patron)
def delete_patron(patron_id: int, db: Session = Depends(get_db)):
    db_patron = patron_service.get_patron_by_id(db, patron_id)
    if db_patron is None:
        raise HTTPException(status_code=404, detail="Patron not found")
    return patron_service.delete_patron(db, patron_id)
