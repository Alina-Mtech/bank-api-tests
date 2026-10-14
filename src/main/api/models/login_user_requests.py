from src.main.api.models.base_model import BaseModel

class LoginUserRequests(BaseModel):
    username: str
    password: str

