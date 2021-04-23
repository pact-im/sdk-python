from enum import Enum

from pydantic import BaseModel


class ResponseStatus(str, Enum):
    OK = 'ok'
    UPDATED = 'updated'


class PactResponse(BaseModel):
    status: ResponseStatus
    data: dict

    def is_ok(self) -> bool:
        return self.status == ResponseStatus.OK

    def is_updated(self) -> bool:
        return self.status == ResponseStatus.UPDATED


class SortDirection(str, Enum):
    ASC = 'asc'
    DESC = 'desc'


class Method(str, Enum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'
