from pydantic import BaseModel

from pact_im.schema.base import PhoneNumber


class ServiceMessageCreate(BaseModel):
    phone: PhoneNumber
    short_text: str
    long_text: str
