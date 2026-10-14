from src.main.api.models.base_model import BaseModel

class AccountUpRequests(BaseModel):
    accountId: int
    amount: float