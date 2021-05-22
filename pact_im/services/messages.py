from typing import Optional, Union, List

from pact_im.schema import Method
from pact_im.schema.base import SortDirection
from pact_im.schema.messages import MessageListRequest, MessageList, MessageCreate, MessageResponse
from pact_im.services.base import Service


class MessagesService(Service):
    ENDPOINT = 'companies/%s/conversations/%s/messages'

    def get_messages(self, company_id: int, conversation_id: int, from_: Optional[int] = None,
                     per: Optional[int] = None,
                     sort: Optional[Union[str, SortDirection]] = None) -> MessageList:
        """
        Get conversation messages
        https://pact-im.github.io/api-doc/#get-conversation-messages

        :param company_id:
        :param conversation_id:
        :param from_:
        :param per:
        :param sort:
        :return:
        """
        query = MessageListRequest.parse_obj({'from_': from_, 'per': per, 'sort': sort})

        response = self.request(
            method=Method.GET,
            endpoint=self._endpoint(None, company_id, conversation_id),
            params=query
        )

        return response.to_class(MessageList)

    def send_message(self, company_id: int, conversation_id: int, message: Optional[str] = None,
                     attachments: Optional[Union[List[int], int]] = None) -> MessageResponse:
        """
        Send message and/or attachments
        https://pact-im.github.io/api-doc/#send-message

        :param company_id:
        :param conversation_id:
        :param message:
        :param attachments: attachments ids
        :return:
        """
        if isinstance(attachments, int):
            attachments = [attachments]
        query = MessageCreate(message=message, attachments_ids=attachments)

        response = self.request(
            method=Method.POST,
            endpoint=self._endpoint(None, company_id, conversation_id),
            body=query
        )
        return response.to_class(MessageResponse)
