import pytest
from src.main.api.models.account_up_requests import AccountUpRequests
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.models.create_user_requests import CreateUserRequests, CreateCreditUserRequests
from src.main.api.models.get_credit_requests import GetCreditRequests


@pytest.fixture
def create_user_requests(api_manager: ApiManager):
    user_request = RandomModelGenerator.generate(CreateUserRequests)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_credit_user_requests(api_manager: ApiManager):
    user_request = RandomModelGenerator.generate(CreateCreditUserRequests)
    api_manager.admin_steps.create_credit_user(user_request)
    return user_request

@pytest.fixture
def create_account_requests(api_manager:ApiManager, create_user_requests: CreateUserRequests) -> int:
    response = api_manager.user_steps.create_account(create_user_requests)
    assert response.balance == 0, "Аккаунт не создан"
    return response.id

@pytest.fixture
def create_credit_account_requests(api_manager: ApiManager, create_credit_user_requests: CreateUserRequests)-> int:
    response = api_manager.user_steps.create_account(create_credit_user_requests)
    assert response.balance == 0, "Аккаунт не создан, баланс равен нулю"
    return response.id

@pytest.fixture
def get_account_requests(api_manager: ApiManager, create_user_requests: CreateUserRequests, create_account_requests):
    response = api_manager.user_steps.get_account(create_user_requests, create_account_requests)
    assert hasattr(response, "transactions"), "Данные счета не получены, история транзакций не доступна"
    return response

@pytest.fixture
def get_accounts_requests_valid(api_manager:ApiManager, create_user_requests: CreateUserRequests):
    response1 = api_manager.user_steps.create_account(create_user_requests)
    assert response1.balance == 0, "Аккаунт не создан"

    request = api_manager.user_steps.get_account(create_user_requests, response1.id)
    assert hasattr(request, "transactions"), "Данные счета не получены, история транзакций не доступна"

    amount1 = RandomModelGenerator.generate_deposit_amount()
    amount2 = 10000 - amount1
    account_up_requests = AccountUpRequests(accountId=response1.id, amount=amount1)
    request1 = api_manager.user_steps.account_up_valid(create_user_requests, account_up_requests)
    assert request1.balance == request.balance + amount1, "Баланс счета не увеличился на сумму пополнения"
    account_up_requests = AccountUpRequests(accountId=response1.id, amount=amount2)
    request_1 = api_manager.user_steps.account_up_valid(create_user_requests, account_up_requests)
    assert request_1.balance == request1.balance + amount2, "Баланс счета не увеличился на сумму пополнения"


    response2 = api_manager.user_steps.create_account(create_user_requests)
    assert response2.balance == 0, "Аккаунт не создан"
    request2 = api_manager.user_steps.get_account(create_user_requests, response2.id)
    assert hasattr(request2, "transactions"), "Данные счета не получены, история транзакций не доступна"

    return {
        "request1": request1,
        "request2": request2
    }

@pytest.fixture
def get_accounts_requests_invalid(api_manager: ApiManager, create_user_requests: CreateUserRequests):
    response1 = api_manager.user_steps.create_account(create_user_requests)
    assert response1.balance == 0, "Аккаунт не создан"

    request = api_manager.user_steps.get_account(create_user_requests, response1.id)
    assert hasattr(request, "transactions"), "Данные счета не получены"

    amount1 = 9000
    amount2 = 2000
    account_up_requests1 = AccountUpRequests(accountId=response1.id, amount=amount1)
    request1 = api_manager.user_steps.account_up_valid(create_user_requests, account_up_requests1)
    account_up_requests2 = AccountUpRequests(accountId=response1.id, amount=amount2)
    requests2 = api_manager.user_steps.account_up_valid(create_user_requests, account_up_requests2)

    response2 = api_manager.user_steps.create_account(create_user_requests)
    assert response2.balance == 0, "Аккаунт не создан"
    request2 = api_manager.user_steps.get_account(create_user_requests, response2.id)
    assert hasattr(request2, "transactions"), "Данные счета не получены, история транзакций не доступна"

    return {
        "request1": request1,
        "request2": request2
    }

@pytest.fixture
def get_credit_valid(api_manager: ApiManager, create_credit_user_requests: CreateCreditUserRequests, create_credit_account_requests: int):
    get_credit_requests = GetCreditRequests(accountId=create_credit_account_requests, amount=RandomModelGenerator.generate_credit_amount(), termMonths=12)
    response = api_manager.user_steps.get_credit_valid(create_credit_user_requests, get_credit_requests)
    assert response.creditId is not None, "Кредит не получен"
    return response
