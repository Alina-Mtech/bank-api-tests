from src.main.api.models.account_up_requests import AccountUpRequests
import pytest
from sqlalchemy.orm import Session
from src.main.api.db.crud.account_crud import AccountCrudDb as Account

class TestAccountUp:
    def test_account_up_valid(self, api_manager, create_user_requests, db_session: Session):
        response = api_manager.user_steps.create_account(create_user_requests)
        assert response.balance == 0
        request = api_manager.user_steps.get_account(create_user_requests, response.id)
        assert hasattr(request, "transactions")
        amount = 1000
        account_up_requests = AccountUpRequests(accountId=response.id,amount=amount)
        requests = api_manager.user_steps.account_up_valid(create_user_requests, account_up_requests)
        assert  requests.balance == request.balance + amount

        account_from_db = Account.get_account_by_id(db_session, requests.id)
        assert account_from_db.balance == request.balance + amount, "Счет не пополнился"


    @pytest.mark.parametrize(
        "amount_check",
        [
            (999),
            (9001)
        ]
    )
    def test_account_up_invalid(self, api_manager, create_user_requests, amount_check, db_session: Session):
        response = api_manager.user_steps.create_account(create_user_requests)
        assert response.balance == 0
        account_up_requests = AccountUpRequests(accountId=response.id, amount=amount_check)
        requests = api_manager.user_steps.account_up_invalid(create_user_requests, account_up_requests)

        account_from_db = Account.get_account_by_id(db_session, response.id)
        assert account_from_db.balance == response.balance, "Cчет пополнился, ошибка"







