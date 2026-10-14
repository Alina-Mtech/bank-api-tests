from src.main.api.models.base_model import BaseModel

class Transactions(BaseModel):
    transactionId: int
    type: str
    amount: int
    fromAccountId: int
    toAccountId: int
    createdAt: str
class GetAccountResponse(BaseModel):
    id: int
    number: int
    balance: float
    transactions: list[Transactions]
