from enum import Enum


class BaseEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


class ResponseStatus(BaseEnum):
    OK = 'ok'
    UPDATED = 'updated'
    CREATED = 'created'
    DELETED = 'deleted'


class SortDirection(BaseEnum):
    ASC = 'asc'
    DESC = 'desc'


class Method(BaseEnum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'


class Provider(BaseEnum):
    Avito = 'avito'
    WhatsApp = 'whatsapp'
    WhatsAppBusiness = 'whatsapp_business'
    Instagram = 'instagram'
    Telegram = 'telegram'
    TelegramPersonal = 'telegram_personal'
    Viber = 'viber'
    VK = 'vk'
    Facebook = 'facebook'


class ChallengeType(BaseEnum):
    TWO_FACTOR = 'two_factor'


class ConfirmationType(BaseEnum):
    CODE = 'code'
    PASSWORD = 'password'
