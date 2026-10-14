from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_requests import CreateUserRequests, CreateCreditUserRequests
from src.main.api.models.login_user_requests import LoginUserRequests
from src.main.api.specs.requests_specs import RequestsSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.foundation.requesters.crud_requester import CrudRequester

class AdminSteps(BaseSteps):
    def create_user(self, create_user_request: CreateUserRequests):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.ADMIN_CREATE_USER,
            ResponseSpecs.requests_ok()
        ).post(create_user_request)

        self.created_obj.append(response)
        return response

    def create_credit_user(self, create_user_request: CreateCreditUserRequests):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.ADMIN_CREATE_CREDIT_USER,
            ResponseSpecs.requests_ok()
        ).post(create_user_request)

        self.created_obj.append(response)
        return response

    def delete_user(self, user_id: int):
        CrudRequester(
            RequestsSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.ADMIN_DELETE_USER,
            ResponseSpecs.requests_ok()
        ).delete(user_id)

    def create_invalid_user(self, create_user_request: CreateUserRequests):
        CrudRequester(
            RequestsSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.ADMIN_CREATE_USER,
            ResponseSpecs.requests_bad()
        ).post(create_user_request)

    def login_user(self, login_user_request: LoginUserRequests):
        response = ValidateCrudRequester(
            RequestsSpecs.unauth_headers(),
            Endpoint.LOGIN_USER,
            ResponseSpecs.requests_ok()
        ).post(login_user_request)
        return response


