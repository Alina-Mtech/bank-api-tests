from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_requests import CreateUserRequests
from src.main.api.models.get_credit_requests import GetCreditRequests
from src.main.api.models.transfer_requests import TransferRequests
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.specs.requests_specs import RequestsSpecs
from src.main.api.models.account_up_requests import AccountUpRequests
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.models.repayment_credit_request import RepaymentCreditRequests

class UserSteps(BaseSteps):
    def create_account(self, create_user_requests: CreateUserRequests):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_requests.username, password = create_user_requests.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.requests_created()
        ).post()
        return response

    def get_account(self, create_user_requests: CreateUserRequests, id: int):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_requests.username, password=create_user_requests.password),
            Endpoint.GET_ACCOUNT,
            ResponseSpecs.requests_ok()
        ).get(id)
        return response

    def account_up_valid(self, create_user_requests: CreateUserRequests, account_up_requests: AccountUpRequests):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_requests.username, password=create_user_requests.password),
            Endpoint.ACCOUNT_UP,
            ResponseSpecs.requests_ok()
        ).post(account_up_requests)
        return response

    def account_up_invalid(self, create_user_requests: CreateUserRequests, account_up_requests: AccountUpRequests):
        response = CrudRequester(
            RequestsSpecs.auth_headers(username=create_user_requests.username, password=create_user_requests.password),
            Endpoint.ACCOUNT_UP,
            ResponseSpecs.requests_bad()
        ).post(account_up_requests)
        return response

    def transfer_account_valid(self, create_user_requests: CreateUserRequests, transfer_requests: TransferRequests):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_requests.username, password=create_user_requests.password),
            Endpoint.TRANSFER,
            ResponseSpecs.requests_ok()
        ).post(transfer_requests)
        return response

    def transfer_account_invalid(self, create_user_requests: CreateUserRequests, transfer_requests: TransferRequests):
        response = CrudRequester(
            RequestsSpecs.auth_headers(username=create_user_requests.username, password=create_user_requests.password),
            Endpoint.TRANSFER,
            ResponseSpecs.requests_bad()
        ).post(transfer_requests)
        return response

    def get_credit_valid(self, create_user_requests: CreateUserRequests, get_credit_requests: GetCreditRequests):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_requests.username, password=create_user_requests.password),
            Endpoint.GET_CREDIT,
            ResponseSpecs.requests_created()
        ).post(get_credit_requests)
        return response

    def get_credit_invalid(self, create_user_requests: CreateUserRequests, get_credit_requests: GetCreditRequests):
        response = CrudRequester(
            RequestsSpecs.auth_headers(username=create_user_requests.username, password=create_user_requests.password),
            Endpoint.GET_CREDIT,
            ResponseSpecs.requests_bad()
        ).post(get_credit_requests)
        return response

    def repayment_credit_valid(self, create_user_requests: CreateUserRequests, repayment_credit_requests: RepaymentCreditRequests):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_requests.username, password=create_user_requests.password),
            Endpoint.REPAYMENT_CREDIT,
            ResponseSpecs.requests_ok()
        ).post(repayment_credit_requests)
        return response

    def repayment_credit_invalid(self, create_user_requests: CreateUserRequests, repayment_credit_requests: RepaymentCreditRequests):
        response = CrudRequester(
            RequestsSpecs.auth_headers(username=create_user_requests.username, password=create_user_requests.password),
            Endpoint.REPAYMENT_CREDIT,
            ResponseSpecs.requests_bad_repayment()
        ).post(repayment_credit_requests)
        return response




