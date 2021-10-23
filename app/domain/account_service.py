from sqlalchemy.orm.session import Session
from app.main import account
from domain.account_model import Account
from domain.account_repository import AccountRepository
from domain.account_schema import AccountSchema, AccountSchemaCreate

def create(db: Session, body: AccountSchemaCreate) -> AccountSchema:
    account = Account(**body.dict())
    return AccountRepository().create(db, account)

def get_accounts(db: Session) -> AccountSchema:
    return AccountRepository().all(db, Account)