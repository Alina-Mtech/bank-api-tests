from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_requests import CreateCreditUserRequests
from src.main.api.models.get_credit_requests import GetCreditRequests
from src.main.api.models.get_credit_response import GetCreditResponse
from src.main.api.models.repayment_credit_request import RepaymentCreditRequests
from sqlalchemy.orm import Session
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from src.main.api.generators.model_generator import RandomModelGenerator

class TestRepaymentCredit:
    def test_get_credit_valid(self, api_manager: ApiManager, create_credit_user_requests: CreateCreditUserRequests, create_credit_account_requests: int, get_credit_valid: GetCreditResponse, db_session: Session):
        amount = get_credit_valid.amount
        repayment_credit_requests = RepaymentCreditRequests(creditId = get_credit_valid.creditId, accountId = create_credit_account_requests, amount=amount)
        response3 = api_manager.user_steps.repayment_credit_valid(create_credit_user_requests, repayment_credit_requests)
        db_session.expire_all()
        repayment_credit_db = Credit.get_credit_by_credit_id(db_session, get_credit_valid.creditId)

        assert repayment_credit_db is not None, "Кредит не найден в БД"
        assert repayment_credit_db.balance == 0, "Остаток долга не обнулился"


    def test_get_credit_invalid(self, api_manager: ApiManager, create_credit_user_requests: CreateCreditUserRequests, create_credit_account_requests: int, get_credit_valid: GetCreditResponse, db_session: Session):
        amount = RandomModelGenerator.generate_amount(1, get_credit_valid.amount - 1)
        repayment_credit_requests = RepaymentCreditRequests(creditId=get_credit_valid.creditId, accountId=create_credit_account_requests, amount=amount)
        response3 = api_manager.user_steps.repayment_credit_invalid(create_credit_user_requests, repayment_credit_requests)
        db_session.expire_all()
        repayment_credit_db = Credit.get_credit_by_credit_id(db_session, get_credit_valid.creditId)
        assert repayment_credit_db.amount == get_credit_valid.balance, "Кредит погашен, ошибка"
