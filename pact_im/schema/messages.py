import datetime
from typing import Optional, Any, Union, List

from pydantic import BaseModel

from pact_im.schema import Provider
from pact_im.schema.base import NextPage, ListRequest


class ChannelMessage(BaseModel):
    id: int
    type: Union[str, Provider]


class MessageResponse(BaseModel):
    id: int
    company_id: int
    channel: ChannelMessage
    conversation_id: int
    state: str
    message_id: Optional[int]
    details: Optional[Any]
    created_at: datetime.datetime

    @property
    def is_delivered(self) -> bool:
        return self.state == 'delivered'


class MessageRequest(BaseModel):
    phone: str
    message: str


class Message(BaseModel):
    external_id: int
    channel_id: int
    channel_type: Union[str, Provider]
    message: str
    income: bool
    created_at: datetime.datetime
    created_at_timestamp: int
    attachments: List[Any]


class MessageList(NextPage):
    messages: List[Message]


class MessageListRequest(ListRequest):
    pass


class MessageCreate(BaseModel):
    message: Optional[str]
    attachments_ids: Optional[List[Any]]
