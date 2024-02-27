from pydantic import BaseModel

class PatronBase(BaseModel):
    name: str
    email: str

class PatronCreate(PatronBase):
    password: str

class PatronUpdate(PatronBase):
    password: str

class Patron(PatronBase):
    id: int

    class Config:
        orm_mode = True
