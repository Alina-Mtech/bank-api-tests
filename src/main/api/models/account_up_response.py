from src.main.api.models.base_model import BaseModel

class AccountUpResponse(BaseModel):
    id: int
    balance: float