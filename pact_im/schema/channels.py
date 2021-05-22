import datetime
from typing import Optional, List, Union

from pydantic import BaseModel, AnyHttpUrl, Field, root_validator, Extra

from pact_im.schema import Provider, ChallengeType
from pact_im.schema.base import NextPage, ListRequest, PhoneNumber, PactResponse, PactResultResponse


class Channel(BaseModel):
    external_id: int
    provider: Provider


class ChannelList(NextPage):
    channels: List[Channel]


class ChannelListRequest(ListRequest):
    pass


class BaseChannelCreate(BaseModel):
    provider: Union[str, Provider]

    class Config:
        extra = Extra.allow
        json_encoders = {
            datetime.datetime: lambda v: int(v.timestamp())
        }


class ChannelCreate(BaseChannelCreate):
    token: str


class ChannelUpdate(BaseModel):
    token: str


class WhatsAppChannelCreate(BaseChannelCreate):
    sync_messages_from: Optional[datetime.datetime]
    do_not_mark_as_read: Optional[bool]


class AvitoChannelCreate(BaseChannelCreate):
    login: str
    password: str


class ChannelInstagramUpdate(BaseModel):
    login: str
    password: str


class InstagramChannelCreate(BaseChannelCreate, ChannelInstagramUpdate):
    sync_messages_from: Optional[datetime.datetime]
    sync_comments: Optional[bool]


class Template(BaseModel):
    id: str
    language_code: str
    parameters: dict


class TemplateMessage(BaseModel):
    phone: PhoneNumber
    template: Template


class CodeRequest(BaseModel):
    provider: Union[str, Provider]
    challenge_variant: Optional[int]
    challenge_type: Optional[Union[str, ChallengeType]]


class CodeConfirm(BaseModel):
    provider: Union[str, Provider]
    confirmation_code: str


class CodeConfirmTwoFactor(CodeConfirm):
    confirmation_type: ChallengeType
    confirmation_variant: int = Field(gt=0)


class TelegramPersonalCodeResponse(BaseModel):
    code_length: int
    code_type: str
    expires_in: int
    next_type: str
    session_id: int
    status: str


class TelegramPersonalConfirmationResponse(PactResultResponse):
    state: str
