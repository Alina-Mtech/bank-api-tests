import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_requests import CreateUserRequests, CreateCreditUserRequests
from src.main.api.models.get_credit_requests import GetCreditRequests
from sqlalchemy.orm import Session
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from src.main.api.generators.model_generator import RandomModelGenerator

class TestGetCredit:
    def test_get_credit_valid(self, api_manager: ApiManager, create_credit_user_requests: CreateUserRequests, create_credit_account_requests: CreateCreditUserRequests, db_session: Session):
        get_credit_requests = GetCreditRequests(accountId=create_credit_account_requests, amount=RandomModelGenerator.generate_credit_amount(), termMonths=12)
        response2 = api_manager.user_steps.get_credit_valid(create_credit_user_requests, get_credit_requests)
        assert response2.creditId is not None, "Кредит не одобрен"

        credit_from_db = Credit.get_credit_by_id(db_session, response2.accountId)
        assert credit_from_db.account_id == response2.accountId, "Кредит не одобрен"
        assert response2.creditId is not None, "Кредит не одобрен"


    @pytest.mark.parametrize(
        "amount_check",
        [
            (4999),
            (15001),
        ]
    )
    def test_get_credit_invalid(self, api_manager:ApiManager, create_credit_user_requests: CreateUserRequests, create_credit_account_requests: CreateCreditUserRequests, amount_check: int, db_session: Session):
        get_credit_requests = GetCreditRequests(accountId=create_credit_account_requests, amount=amount_check, termMonths=12)
        response2 = api_manager.user_steps.get_credit_invalid(create_credit_user_requests, get_credit_requests)

        credit_from_db = Credit.get_credit_by_id(db_session, create_credit_account_requests)
        assert credit_from_db is None, "Кредит одобрен, ошибка"


