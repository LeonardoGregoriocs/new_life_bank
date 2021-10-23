from typing import Any 
#Typing é um built-in do python, traz um conjunto de TIPOS para serem utilizado em definições mais complexas
#Any recebe uma que sequência e verifica se a condição é verdadeira, quando for retorna TRUE.

from sqlalchemy.orm.session import Session


class BaseRepository():
    def create(self, db: Session, model: Any) -> Any:
        db.add(model)
        db.commit()
        db.refresh(model) #recarrega o arquivo
        return model

    def all(self, db: Session, cls) -> Any:
        return db.query(cls).all()



