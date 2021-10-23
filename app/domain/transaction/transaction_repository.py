from sqlalchemy.orm.session import Session
from commons.base_repository import BaseRepository

class TransactionRepository(BaseRepository):
    def read_transaction(id: int, db: Session, cls):
        #return db.query(cls).filter(==id)
        pass