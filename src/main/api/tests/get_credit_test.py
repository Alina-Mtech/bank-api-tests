import pytest
from src.main.api.models.get_credit_requests import GetCreditRequests
from sqlalchemy.orm import Session
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit

class TestGetCredit:
    def test_get_credit_valid(self, api_manager, create_credit_user_requests, db_session: Session):
        response1 = api_manager.user_steps.create_account(create_credit_user_requests)
        assert response1.balance == 0
        get_credit_requests = GetCreditRequests(accountId=response1.id, amount=6000, termMonths=12)
        response2 = api_manager.user_steps.get_credit_valid(create_credit_user_requests, get_credit_requests)
        assert response2.creditId is not None

        credit_from_db = Credit.get_credit_by_id(db_session, response2.accountId)
        assert credit_from_db.account_id == response2.accountId, "Кредит не одобрен"
        assert response2.creditId is not None


    @pytest.mark.parametrize(
        "amount_check",
        [
            (4999),
            (15001),
        ]
    )
    def test_get_credit_invalid(self, api_manager, create_credit_user_requests, amount_check, db_session: Session):
        response1 = api_manager.user_steps.create_account(create_credit_user_requests)
        assert response1.balance == 0
        get_credit_requests = GetCreditRequests(accountId=response1.id, amount=amount_check, termMonths=12)
        response2 = api_manager.user_steps.get_credit_invalid(create_credit_user_requests, get_credit_requests)

        credit_from_db = Credit.get_credit_by_id(db_session, response1.id)
        assert credit_from_db is None, "Кредит одобрен, ошибка"


