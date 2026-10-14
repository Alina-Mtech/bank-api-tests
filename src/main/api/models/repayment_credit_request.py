from src.main.api.models.base_model import BaseModel

class RepaymentCreditRequests(BaseModel):
    creditId: int
    accountId: int
    amount: int