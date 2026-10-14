from typing import Protocol

from requests import Response

from src.main.api.models.base_model import BaseModel
from typing import Optional, Type

class CrudEndpoint(Protocol):
    def post(self, model: Optional[BaseModel]) -> BaseModel | Response: ...
    def get(self, id: int) -> BaseModel | Response: ...
    def delete(self, user_id: int) -> BaseModel | Response: ...

