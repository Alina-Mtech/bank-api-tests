from src.main.api.models.base_model import BaseModel

class TransferRequests(BaseModel):
    fromAccountId: int
    toAccountId: int
    amount: float