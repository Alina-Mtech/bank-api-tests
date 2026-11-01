import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_requests import CreateUserRequests
from src.main.api.db.crud.user_crud import UserCrudDb as User
from sqlalchemy.orm import Session

@pytest.mark.api
class TestCreateUser:
    @pytest.mark.parametrize(
        "create_user_requests",
            [RandomModelGenerator.generate(CreateUserRequests)],
    )
    def test_create_user_valid(self, api_manager: ApiManager, create_user_requests: CreateUserRequests, db_session: Session):
        response = api_manager.admin_steps.create_user(create_user_requests)
        assert create_user_requests.username == response.username, "Username созданного пользователя не совпадает с ожидаемым"
        assert create_user_requests.role == response.role, "Role созданного пользователя не совпадает с ожидаемой"

        user_from_db = User.get_user_by_username(db_session, create_user_requests.username)
        assert user_from_db.username == create_user_requests.username, "Созданного пользователя нет в БД"

    @pytest.mark.parametrize(
        "username, password",
        [
            ("абв", "Pas!sw0rd"),
            ("ab", "Pas!sw0rd"),
            ("abv!", "Pas!sw0rd"),
            ("Maxx1", "Pas!sw0rд"),
            ("Maxx2", "Pas!sw0"),
            ("Maxx3", "pas!sw0rd"),
            ("Maxx4", "PAS!SWORD"),
            ("Maxx5", "Passw0rd"),
            ("Maxx6", "Pas!sword")

        ]
    )
    def test_create_user_invalid(self, db_session:Session, username: str, password: str, api_manager: ApiManager):
        create_user_request = CreateUserRequests(username = username, password = password, role = "ROLE_USER")
        api_manager.admin_steps.create_invalid_user(create_user_request)

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db is None, "Пользователь создан, ошибка"




