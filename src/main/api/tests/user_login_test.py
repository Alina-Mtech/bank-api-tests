import pytest
from src.main.api.models.login_user_requests import LoginUserRequests

@pytest.mark.api
class TestUserLogin:
    def test_login_admin(self, api_manager):
        login_user_request = LoginUserRequests(username="admin", password="123456")
        response = api_manager.admin_steps.login_user(login_user_request)
        assert login_user_request.username == response.user.username
        assert response.user.role == "ROLE_ADMIN"

    def test_login_user(self, api_manager, create_user_requests):
        response = api_manager.admin_steps.login_user(create_user_requests)
        assert create_user_requests.username == response.user.username
        assert response.user.role == "ROLE_USER"







