from enum import Enum

from pydantic import BaseModel


class ResponseStatus(str, Enum):
    OK = 'ok'
    UPDATED = 'updated'
    CREATED = 'created'


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

    def __str__(self) -> str:
        return self.value


class Provider(str, Enum):
    WhatsApp = 'whatsapp'
    WhatsAppBusiness = 'whatsapp_business'
    Instagram = 'instagram'
    Telegram = 'telegram'
    Viber = 'viber'
    VK = 'vk'
    Facebook = 'facebook'

    def __str__(self) -> str:
        return self.value
