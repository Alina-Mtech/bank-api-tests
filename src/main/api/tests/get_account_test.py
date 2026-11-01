from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_requests import CreateUserRequests
from src.main.api.models.login_user_requests import LoginUserRequests
from src.main.api.requests.get_account_requester import GetAccountRequester
from src.main.api.specs.requests_specs import RequestsSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.requests.login_user_requester import LoginUserRequester
from src.main.api.requests.create_account_requester import CreateAccountRequester
from src.main.api.requests.create_user_requester import CreateUserRequester


class TestGetAccount:
    def test_get_account(self, api_manager: ApiManager, create_user_requests: CreateUserRequests, create_account_requests: CreateUserRequests):
        request = api_manager.user_steps.get_account(create_user_requests, create_account_requests)
        assert hasattr(request, "transactions"), "Данные счета не получены, история транзакций не доступна"
