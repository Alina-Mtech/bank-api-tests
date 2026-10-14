from src.main.api.requests.requester import Requester
import requests
from src.main.api.models.create_account_response import CreateAccountResponse

class CreateAccountRequester(Requester):
    def post(self, model = None) -> CreateAccountResponse:
        url = f"{self.base_url}/account/create"
        response = requests.post(
            url,
            headers=self.headers,
        )
        self.response_spec(response)
        return CreateAccountResponse(**response.json())

