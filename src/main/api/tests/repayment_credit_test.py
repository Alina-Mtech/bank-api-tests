from src.main.api.models.get_credit_requests import GetCreditRequests
from src.main.api.models.repayment_credit_request import RepaymentCreditRequests
from sqlalchemy.orm import Session
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit

class TestRepaymentCredit:
    def test_get_credit_valid(self, api_manager, create_credit_user_requests, db_session: Session):
        amount = 6000
        response1 = api_manager.user_steps.create_account(create_credit_user_requests)
        assert response1.balance == 0
        get_credit_requests = GetCreditRequests(accountId=response1.id, amount=amount, termMonths=12)
        response2 = api_manager.user_steps.get_credit_valid(create_credit_user_requests, get_credit_requests)
        assert response2.creditId is not None

        credit_before = Credit.get_credit_by_credit_id(db_session, response2.creditId)
        balance_before = credit_before.balance

        repayment_credit_requests = RepaymentCreditRequests(creditId = response2.creditId, accountId = response1.id, amount=amount)
        response3 = api_manager.user_steps.repayment_credit_valid(create_credit_user_requests, repayment_credit_requests)
        db_session.expire_all()
        repayment_credit_db = Credit.get_credit_by_credit_id(db_session, response2.creditId)

        assert repayment_credit_db is not None, "Кредит не найден в БД"
        assert repayment_credit_db.balance == 0, "Остаток долга не обнулился"


    def test_get_credit_invalid(self, api_manager, create_credit_user_requests, db_session: Session):
        amount = 6000
        response1 = api_manager.user_steps.create_account(create_credit_user_requests)
        assert response1.balance == 0
        get_credit_requests = GetCreditRequests(accountId=response1.id, amount=amount, termMonths=12)
        response2 = api_manager.user_steps.get_credit_valid(create_credit_user_requests, get_credit_requests)
        assert response2.creditId is not None

        repayment_credit_requests = RepaymentCreditRequests(creditId=response2.creditId, accountId=response1.id, amount=5000)
        response3 = api_manager.user_steps.repayment_credit_invalid(create_credit_user_requests, repayment_credit_requests)
        db_session.expire_all()
        repayment_credit_db = Credit.get_credit_by_credit_id(db_session, response2.creditId)
        assert repayment_credit_db.amount == response2.balance, "Кредит погашен, ошибка"
