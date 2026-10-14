import pytest
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.models.create_user_requests import CreateUserRequests, CreateCreditUserRequests


@pytest.fixture
def create_user_requests(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequests)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_credit_user_requests(api_manager):
    user_request = RandomModelGenerator.generate(CreateCreditUserRequests)
    api_manager.admin_steps.create_credit_user(user_request)
    return user_request