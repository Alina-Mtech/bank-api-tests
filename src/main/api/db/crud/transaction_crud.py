from requests import Session
from sqlalchemy.orm import Session
from src.main.api.db.models.transaction_table import Transaction

class TransactionCrudDb:
    @staticmethod
    def get_transaction_balance_by_id(db: Session, account_id: int) -> Transaction | None:
        return db.query(Transaction).filter(Transaction.to_account_id == account_id).first()