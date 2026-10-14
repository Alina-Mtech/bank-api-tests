from src.main.api.requests.requester import Requester
from src.main.api.models.get_account_response import GetAccountResponse
import requests

class GetAccountRequester(Requester):
    def get(self, id: int):
        url = f"{self.base_url}/account/transactions/{id}"
        response = requests.get(
            url,
            headers=self.headers,
        )
        self.response_spec(response)

        return GetAccountResponse(**response.json())
