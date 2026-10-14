from src.main.api.models.base_model import BaseModel
from pydantic import Field

class GetCreditResponse(BaseModel):
    accountId: int = Field(alias="id")
    amount: int
    termMonths: int
    balance: int
    creditId: int