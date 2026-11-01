import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_requests import CreateUserRequests
from src.main.api.models.login_user_requests import LoginUserRequests

@pytest.mark.api
class TestUserLogin:
    def test_login_admin(self, api_manager: ApiManager):
        login_user_request = LoginUserRequests(username="admin", password="123456")
        response = api_manager.admin_steps.login_user(login_user_request)
        assert login_user_request.username == response.user.username, "Username администратора не совпадает"
        assert response.user.role == "ROLE_ADMIN", "Role администратора не совпадает"

    def test_login_user(self, api_manager: ApiManager, create_user_requests: CreateUserRequests):
        response = api_manager.admin_steps.login_user(create_user_requests)
        assert create_user_requests.username == response.user.username, "Username пользователя не совпадает"
        assert response.user.role == "ROLE_USER", "Role пользователя не совпадает"







