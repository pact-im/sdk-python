from abc import ABC

from pydantic import BaseModel

from pact_im import DEFAULT_API_BASE
from pact_im import exceptions
from pact_im.base import PactClientBase


class Service(ABC):
    ENDPOINT = None

    def __init__(self, client: PactClientBase):
        self.__client = client

    def get_endpoint(self) -> str:
        if not self.ENDPOINT:
            raise exceptions.InvalidArgumentException('Endpoint cannot not be empty')
        return self.ENDPOINT.strip('/')

    def request(self, method: str, method_endpoint: str, params: dict = None, body=None, headers: dict = None):
        if isinstance(body, BaseModel):
            body = body.json(exclude_none=True)
        response = self.__client.request(
            method,
            f'{DEFAULT_API_BASE.rstrip("/")}/{self.get_endpoint()}/{method_endpoint}',
            headers=headers,
            params=params,
            body=body
        )
        return response.raw
