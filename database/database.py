from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from typing import Generator

from config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from database.models import book
from database.models import patron
from database.models import checkout

Base.metadata.create_all(bind=engine, checkfirst=True)
book.Base.metadata.create_all(bind=engine, checkfirst=True)
patron.Base.metadata.create_all(bind=engine, checkfirst=True)
checkout.Base.metadata.create_all(bind=engine, checkfirst=True)
