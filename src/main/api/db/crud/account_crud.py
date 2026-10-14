from requests import Session
from sqlalchemy.orm import Session
from src.main.api.db.models.account_table import Account

class AccountCrudDb:
    @staticmethod
    def get_account_by_id(db: Session, account_id: int) -> Account | None:
        return db.query(Account).filter(Account.id == account_id).first()

    @staticmethod
    def delete_account(db: Session, account_id: int) -> None:
        account = db.query(Account).filter(id = account_id).first()
        if account:
            db.delete(account)
            db.commit()
