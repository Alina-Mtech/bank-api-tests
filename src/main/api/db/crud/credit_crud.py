from requests import Session
from sqlalchemy.orm import Session
from src.main.api.db.models.credit_table import Credit

class CreditCrudDb:
    @staticmethod
    def get_credit_by_id(db: Session, account_id: int) -> Credit | None:
        return db.query(Credit).filter(Credit.account_id == account_id).first()
    def get_credit_by_credit_id(db: Session, credit_id: int) -> Credit | None:
        return db.query(Credit).filter(Credit.id == credit_id).first()
