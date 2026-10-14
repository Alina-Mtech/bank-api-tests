from dataclasses import dataclass
from enum import Enum
from src.main.api.models.account_up_response import AccountUpResponse
from src.main.api.models.account_up_requests import AccountUpRequests
from src.main.api.models.base_model import BaseModel
from typing import Optional, Type
from src.main.api.models.get_account_response import GetAccountResponse
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.login_user_response import LoginUserResponse
from src.main.api.models.login_user_requests import LoginUserRequests
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.models.create_user_requests import CreateUserRequests
from src.main.api.models.transfer_requests import TransferRequests
from src.main.api.models.transfer_response import TransferResponse
from src.main.api.models.get_credit_response import GetCreditResponse
from src.main.api.models.get_credit_requests import GetCreditRequests
from src.main.api.models.repayment_credit_request import RepaymentCreditRequests
from src.main.api.models.repayment_credit_response import RepaymentCreditResponse

@dataclass
class EndpointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]

class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfiguration(
        request_model = CreateUserRequests,
        url = "/admin/create",
        response_model = CreateUserResponse
    )
    ADMIN_CREATE_CREDIT_USER = EndpointConfiguration(
        request_model=CreateUserRequests,
        url="/admin/create",
        response_model=CreateUserResponse
    )
    ADMIN_DELETE_USER = EndpointConfiguration(
        request_model = None,
        url = "/admin/users",
        response_model = None
    )
    LOGIN_USER = EndpointConfiguration(
        request_model = LoginUserRequests,
        url = "/auth/token/login",
        response_model = LoginUserResponse
    )
    CREATE_ACCOUNT = EndpointConfiguration(
        request_model=None,
        url="/account/create",
        response_model=CreateAccountResponse
    )
    GET_ACCOUNT = EndpointConfiguration(
        request_model=CreateAccountResponse,
        url="/account/transactions",
        response_model=GetAccountResponse
    )
    ACCOUNT_UP = EndpointConfiguration(
        request_model=AccountUpRequests,
        url="/account/deposit",
        response_model=AccountUpResponse
    )
    TRANSFER = EndpointConfiguration(
        request_model=TransferRequests,
        url="/account/transfer",
        response_model=TransferResponse
    )
    GET_CREDIT = EndpointConfiguration(
        request_model=GetCreditRequests,
        url="/credit/request",
        response_model=GetCreditResponse
    )
    REPAYMENT_CREDIT = EndpointConfiguration(
        request_model=RepaymentCreditRequests,
        url="/credit/repay",
        response_model=RepaymentCreditResponse
    )
