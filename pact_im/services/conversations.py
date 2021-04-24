from typing import Union

from pact_im.schema.base import SortDirection, Provider
from pact_im.services.base import Service


class ConversationsService(Service):
    ENDPOINT = 'companies/%s/conversations'

    def get_conversations(self, company_id: int, from_: int = None, per: int = None,
                          sort: Union[str, SortDirection] = None):
        # TODO get_all_conversations https://pact-im.github.io/api-doc/?shell#get-all-conversations
        pass

    def create_conversation(self, company_id: int, provider: Union[str, Provider], phone: str):
        # TODO https://pact-im.github.io/api-doc/#create-new-conversation
        pass

    def get_detail(self, company_id: int, conversation_id: int):
        # TODO https://pact-im.github.io/api-doc/#get-conversation-details
        pass

    def update_assignee(self, company_id: int, conversation_id: int, assignee_id: int):
        # TODO https://pact-im.github.io/api-doc/#update-assignee-for-conversation
        pass
        