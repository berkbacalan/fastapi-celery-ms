from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.core.schemas.checkout import Checkout, CheckoutCreate
from database.database import get_db
from app.core.services import checkout_service

router = APIRouter()

@router.post("/", response_model=Checkout)
def create_checkout(checkout: CheckoutCreate, db: Session = Depends(get_db)):
    return checkout_service.create_checkout(db, checkout.book_id, checkout.patron_id)

@router.get("/", response_model=List[Checkout])
def get_all_checkouts(db: Session = Depends(get_db)):
    checkouts = checkout_service.get_checked_out_books(db)
    return checkouts

@router.get("/{checkout_id}", response_model=Checkout)
def get_checkout_by_id(checkout_id: int, db: Session = Depends(get_db)):
    db_checkout = checkout_service.get_checkout_by_id(db, checkout_id)
    if db_checkout is None:
        raise HTTPException(status_code=404, detail="Checkout not found")
    return db_checkout

@router.delete("/{checkout_id}", response_model=Checkout)
def delete_checkout(checkout_id: int, db: Session = Depends(get_db)):
    db_checkout = checkout_service.get_checkout_by_id(db, checkout_id)
    if db_checkout is None:
        raise HTTPException(status_code=404, detail="Checkout not found")
    return checkout_service.remove_checkout_by_id(db, checkout_id)
