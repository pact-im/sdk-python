from abc import ABC
from typing import Any
from pact_im import exceptions
import requests


class PactClientBase(ABC):

    def __init__(self, api_token: str):
        if not api_token or api_token == '':
            raise exceptions.InvalidArgumentException('API token can\'t be empty string')
        self.api_token = api_token

    def request(self, method: str, uri: str, headers: dict = None, params: dict = None, body: Any = None):
        """
        Request
        :param method: HTTP method name
        :param uri:
        :param headers:
        :param params:
        :param body:
        :return:
        """
        headers = headers or dict()
        headers.update({'X-Private-Api-Token': self.api_token})

        response = requests.request(method, uri, headers=headers, params=params, json=body)
        if 200 <= response.status_code < 300:
            return response
        raise exceptions.ApiCallException('Api returned HTTP non-OK status: %s' % response.status_code)
