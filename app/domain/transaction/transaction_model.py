from sqlalchemy.sql.sqltypes import Float
from config.database import Base
from sqlalchemy.types import Date
from sqlalchemy import Column, Integer, String, Float


class Transaction(Base):
    __tablename__ = "transaction"

    transactionId = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    destinationAccountId = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"{self.type}, {self.amount}"