from src.main.api.models.base_model import BaseModel

class GetCreditRequests(BaseModel):
    accountId: int
    amount: int
    termMonths: int