from typing import Optional
from datetime import date, datetime
from fastapi import background
from pydantic import BaseModel, Field
from sqlalchemy.sql.expression import update

class TransactionSchema(BaseModel):
    id: int
    transactionType: str=Field(..., example="CREDIT")
    amount: float
    destinationAccount: int
    created_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True

class TransactionSchemaCreate(BaseModel):
    transactionType: str
    amount: float

    class Config:
        orm_mode = True
