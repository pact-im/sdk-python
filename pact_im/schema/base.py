from enum import Enum

from pydantic import BaseModel


class PactResponse(BaseModel):
    status: str

    def is_ok(self) -> bool:
        return self.status == 'ok'


class SortDirection(str, Enum):
    ASC = 'asc'
    DESC = 'desc'


class Method(str, Enum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'
