from os import terminal_size
from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, Field
from sqlalchemy import orm
from sqlalchemy.sql.expression import update

from app.config.database import Base

class AccountSchema(BaseModel):
    id: int
    name: str=Field(..., example="João")
    born_date: date
    document: str
    phone_number: Optional[str]
    created_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True

class AccountSchemaCreate(BaseModel):
    name: str
    born_date: date
    document: str
    email: str
    phone_number: str

    class Config:
        orm_mode = True