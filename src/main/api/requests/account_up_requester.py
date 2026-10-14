from http import HTTPStatus
from src.main.api.models.account_up_requests import AccountUpRequests
from src.main.api.models.account_up_response import AccountUpResponse
from src.main.api.requests.requester import Requester
import requests

class AccountUpRequester(Requester):
    def post(self, account_up_requests: AccountUpRequests):
        url = f"{self.base_url}/account/deposit"
        response = requests.post(
            url,
            json=account_up_requests.model_dump(),
            headers=self.headers,
        )
        self.response_spec(response)
        if response.status_code == HTTPStatus.OK:
            return AccountUpResponse(**response.json())
        return response
