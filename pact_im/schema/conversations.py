import datetime
from typing import List, Union

from pydantic import BaseModel

from pact_im.schema import Provider
from pact_im.schema.base import NextPage, ListRequest, PhoneNumber


class Conversation(BaseModel):
    external_id: int
    name: str
    channel_id: int
    channel_type: Union[str, Provider]
    created_at: datetime.datetime
    created_at_timestamp: int
    avatar: str
    sender_external_id: str
    meta: dict


class ConversationList(NextPage):
    conversations: List[Conversation]


class ConversationListRequest(ListRequest):
    pass


class ConversationCreate(BaseModel):
    provider: Union[str, Provider]
    phone: PhoneNumber


class ConversationResponse(BaseModel):
    conversation: Conversation
