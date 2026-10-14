from src.main.api.models.account_up_requests import AccountUpRequests
import pytest
from src.main.api.models.transfer_requests import TransferRequests
from sqlalchemy.orm import Session
from src.main.api.db.crud.transaction_crud import TransactionCrudDb as Transaction

class TestTransfer:
    def test_transfer_valid(self, api_manager, create_user_requests, db_session: Session):
        response1 = api_manager.user_steps.create_account(create_user_requests)
        assert response1.balance == 0

        request1 = api_manager.user_steps.get_account(create_user_requests, response1.id)
        assert hasattr(request1, "transactions")

        amount = 1000
        account_up_requests = AccountUpRequests(accountId=response1.id, amount=amount)
        requests = api_manager.user_steps.account_up_valid(create_user_requests, account_up_requests)
        assert requests.balance == request1.balance + amount

        response2 = api_manager.user_steps.create_account(create_user_requests)
        assert response2.balance == 0
        request2 = api_manager.user_steps.get_account(create_user_requests, response2.id)
        assert hasattr(request2, "transactions")

        transfer_requests = TransferRequests(fromAccountId=response1.id, toAccountId=response2.id, amount=amount)
        request = api_manager.user_steps.transfer_account_valid(create_user_requests, transfer_requests)
        request3 = api_manager.user_steps.get_account(create_user_requests, request.toAccountId)
        assert request3.balance == response2.balance + amount

        transaction_from_db = Transaction.get_transaction_balance_by_id(db_session, request.toAccountId)
        assert transaction_from_db.to_account_id == request.toAccountId, "Транзакции не было, id транзакции нет в БД"
        assert transaction_from_db.amount == amount, "Поле баланса транзакции отсутствует в БД"

    @pytest.mark.parametrize(
        "amount_check",
        [
            (499),
            (10001),
        ]
    )
    def test_transfer_invalid(self, api_manager, create_user_requests, amount_check, db_session: Session):
        response1 = api_manager.user_steps.create_account(create_user_requests)
        assert response1.balance == 0
        amount1 = 9000
        amount2 = 2000
        account_up_requests1 = AccountUpRequests(accountId=response1.id, amount=amount1)
        requests1 = api_manager.user_steps.account_up_valid(create_user_requests, account_up_requests1)
        account_up_requests2 = AccountUpRequests(accountId=response1.id, amount=amount2)
        requests2 = api_manager.user_steps.account_up_valid(create_user_requests, account_up_requests2)

        response2 = api_manager.user_steps.create_account(create_user_requests)

        transfer_requests = TransferRequests(fromAccountId=response1.id, toAccountId=response2.id, amount=amount_check)
        request = api_manager.user_steps.transfer_account_invalid(create_user_requests, transfer_requests)

        transaction_from_db = Transaction.get_transaction_balance_by_id(db_session, response2.id)
        assert transaction_from_db is None, "Транзакция ошибочно появилась в БД"





