from http import HTTPStatus
import requests
from src.main.api.requests.requester import Requester
from src.main.api.models.get_credit_requests import GetCreditRequests
from src.main.api.models.get_credit_response import GetCreditResponse

class GetCreditRequester(Requester):
    def post(self, get_credit_requests: GetCreditRequests):
        url = f"{self.base_url}/credit/request"
        response = requests.post(
            url,
            json=get_credit_requests.model_dump(),
            headers=self.headers,
        )
        print(response.json())
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return GetCreditResponse(**response.json())
        return response




