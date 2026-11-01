from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.account_up_response import AccountUpResponse
import pytest
from src.main.api.models.get_account_response import GetAccountResponse
from src.main.api.models.create_user_requests import CreateUserRequests
from src.main.api.models.transfer_requests import TransferRequests
from sqlalchemy.orm import Session
from src.main.api.db.crud.transaction_crud import TransactionCrudDb as Transaction
from src.main.api.generators.model_generator import RandomModelGenerator

class TestTransfer:
    def test_transfer_valid(self, api_manager: ApiManager, create_user_requests: CreateUserRequests, get_accounts_requests_valid: dict[str, AccountUpResponse | GetAccountResponse], db_session: Session):
        amount = RandomModelGenerator.generate_transfer_amount()
        transfer_requests = TransferRequests(fromAccountId=get_accounts_requests_valid["request1"].id, toAccountId=get_accounts_requests_valid["request2"].id, amount=amount)
        response1 = api_manager.user_steps.transfer_account_valid(create_user_requests, transfer_requests)
        response2 = api_manager.user_steps.get_account(create_user_requests, response1.toAccountId)
        assert response2.balance == get_accounts_requests_valid["request2"].balance + amount, "Перевод не осуществился"

        transaction_from_db = Transaction.get_transaction_balance_by_id(db_session, response1.toAccountId)
        assert transaction_from_db.to_account_id == response1.toAccountId, "Транзакции не было, id транзакции нет в БД"
        assert transaction_from_db.amount == amount, "Поле баланса транзакции отсутствует в БД"

    @pytest.mark.parametrize(
        "amount_check",
        [
            (499),
            (10001),
        ]
    )
    def test_transfer_invalid(self, api_manager: ApiManager, create_user_requests: CreateUserRequests, get_accounts_requests_invalid: dict[str, AccountUpResponse | GetAccountResponse], amount_check: int, db_session: Session):
        transfer_requests = TransferRequests(fromAccountId=get_accounts_requests_invalid["request1"].id, toAccountId=get_accounts_requests_invalid["request2"].id, amount=amount_check)
        response1 = api_manager.user_steps.transfer_account_invalid(create_user_requests, transfer_requests)
        transaction_from_db = Transaction.get_transaction_balance_by_id(db_session, get_accounts_requests_invalid["request2"].id)
        assert transaction_from_db is None, "Транзакция ошибочно появилась в БД"







