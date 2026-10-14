from http import HTTPStatus
from src.main.api.requests.requester import Requester
from src.main.api.models.repayment_credit_request import RepaymentCreditRequests
from src.main.api.models.repayment_credit_response import RepaymentCreditResponse
import requests


class RepaymentCreditRequester(Requester):
    def post(self, repayment_credit_request: RepaymentCreditRequests):
        url = f"{self.base_url}/credit/repay"
        response = requests.post(
            url,
            json=repayment_credit_request.model_dump(),
            headers=self.headers,
        )
        self.response_spec(response)

        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return RepaymentCreditResponse(**response.json())
        return response