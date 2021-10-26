from fastapi import Depends
from typing import List
from fastapi.routing import APIRouter
from config.database import get_db
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from domain.transaction import transaction_service
from domain.transaction.transaction_schema import TransactionSchema, TransactionSchemaCreate

router = APIRouter()

@router.get("/",
            summary="Operação responsavél por retornar todas transações por filtro.",
            response_model=List[TransactionSchema])
def get_transactions(db: Session = Depends(get_db)):
    return transaction_service.get_transaction(db)

@router.post("/",
            summary="Operação responsavél por criar uma nova transação",
            response_model=TransactionSchema)
def create_transaction(body: TransactionSchemaCreate, db: Session = Depends(get_db)):
    return transaction_service.create(db, body)
    




