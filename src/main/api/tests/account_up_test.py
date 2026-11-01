from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.account_up_requests import AccountUpRequests
import pytest
from sqlalchemy.orm import Session
from src.main.api.db.crud.account_crud import AccountCrudDb as Account
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_requests import CreateUserRequests
from src.main.api.models.get_account_response import GetAccountResponse


class TestAccountUp:
    def test_account_up_valid(self, api_manager: ApiManager, create_user_requests: CreateUserRequests, get_account_requests: GetAccountResponse, db_session: Session):
        amount = RandomModelGenerator.generate_deposit_amount()
        account_up_requests = AccountUpRequests(accountId=get_account_requests.id,amount=amount)
        requests = api_manager.user_steps.account_up_valid(create_user_requests, account_up_requests)
        assert  requests.balance == get_account_requests.balance + amount, "Баланс счета не увеличился на сумму пополнения"

        account_from_db = Account.get_account_by_id(db_session, requests.id)
        assert account_from_db.balance == get_account_requests.balance + amount, "Счет не пополнился"


    @pytest.mark.parametrize(
        "amount_check",
        [
            (999),
            (9001)
        ]
    )
    def test_account_up_invalid(self, api_manager: ApiManager, create_user_requests: CreateUserRequests, get_account_requests: GetAccountResponse, amount_check: int, db_session: Session):
        account_up_requests = AccountUpRequests(accountId=get_account_requests.id, amount=amount_check)
        requests = api_manager.user_steps.account_up_invalid(create_user_requests, account_up_requests)

        account_from_db = Account.get_account_by_id(db_session, get_account_requests.id)
        assert account_from_db.balance == get_account_requests.balance, "Cчет пополнился, ошибка"







