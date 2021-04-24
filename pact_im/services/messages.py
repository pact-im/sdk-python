from typing import Optional, Union, List

from pact_im.schema.base import SortDirection
from pact_im.services.base import Service


class MessageService(Service):
    ENDPOINT = 'companies/%s/conversations/%s/messages'

    def get_messages(self, company_id: int, conversation_id: int, from_: Optional[int] = None, per: Optional[int] = None,
                    sort: Optional[Union[str, SortDirection]] = None):
        # TODO https://pact-im.github.io/api-doc/#get-conversation-messages
        pass

    def send_message(self, company_id: int, conversation_id: int, message: Optional[str] = None, attachments: Optional[List[int]] = None):
        # TODO https://pact-im.github.io/api-doc/#send-message
        pass