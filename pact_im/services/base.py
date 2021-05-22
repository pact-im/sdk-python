from abc import ABC
from typing import Union, Optional

from pydantic import BaseModel

from pact_im import exceptions
from pact_im.base import PactClientBase
from pact_im.schema.base import PactResponse
from pact_im.utils import camel_to_snake


class Service(ABC):
    ENDPOINT = None

    @classmethod
    def class_name(cls):
        name = cls.__name__[:-7]
        if not len(name):
            return cls.__name__.lower()
        return camel_to_snake(name)

    def __init__(self, client: PactClientBase):
        self.__client = client

    def get_endpoint(self) -> str:
        if not self.ENDPOINT:
            raise exceptions.InvalidArgumentException('Endpoint cannot not be empty')
        return self.ENDPOINT.strip('/')

    def _endpoint(self, method_endpoint=None, *args) -> str:
        base_args = [
            self.__client.base_url.rstrip("/"),
            self.get_endpoint(),
            str(method_endpoint or '').lstrip("/")
        ]
        endpoint = '/'.join(base_args)
        if not len(args):
            return endpoint
        return endpoint % args

    def request(self, method: str, endpoint: str, params: Optional[Union[dict, BaseModel]] = None,
                body: Optional[Union[dict, BaseModel]] = None, headers: dict = None, file: dict = None, *,
                json: bool = False) -> Union[dict, list, PactResponse]:
        """

        :param file:
        :param method:
        :param endpoint:
        :param params:
        :param body:
        :param headers:
        :return:
        :raise exceptions.ApiCallException: Api call error
        """
        if isinstance(body, BaseModel):
            body = body.json(exclude_none=True, exclude_defaults=True)
        if isinstance(params, BaseModel):
            params = params.dict(exclude_none=True, exclude_defaults=True)

        response = self.__client.request(
            method,
            endpoint,
            headers=headers,
            params=params,
            body=body,
            file=file
        )
        if json:
            return response.json()
        return PactResponse.parse_raw(response.content)
