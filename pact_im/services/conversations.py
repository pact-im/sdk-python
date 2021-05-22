from typing import Union, Optional

from pact_im.schema import SortDirection, Provider, Method
from pact_im.schema.base import PhoneNumber
from pact_im.schema.conversations import ConversationListRequest, ConversationList, ConversationCreate, \
    ConversationResponse
from pact_im.services.base import Service


class ConversationsService(Service):
    ENDPOINT = 'companies/%s/conversations'

    def get_conversations(self, company_id: int, from_: int = None, per: int = 50,
                          sort: Union[str, SortDirection] = SortDirection.ASC) -> ConversationList:
        """
        Gets all conversations
        https://pact-im.github.io/api-doc/#get-all-conversations

        :param company_id: ID of the company
        :param from_: Next page token geted from last request. Not valid or empty token return first page
        :param per: Number of elements per page. Default: 50
        :param sort: We sort results by id. Change sorting direction. Avilable values: asc, desc
        :return:
        """
        query = ConversationListRequest.parse_obj({'from': from_, 'per': per, 'sort_direction': sort})

        response = self.request(
            method=Method.GET,
            endpoint=self._endpoint(None, company_id),
            params=query
        )

        return response.to_class(ConversationList)

    def create_conversation(self, company_id: int, phone: str,
                            provider: Union[str, Provider] = Provider.WhatsApp) -> ConversationResponse:
        """
        Creates new conversation
        This endpoint creates conversation in the company
        https://pact-im.github.io/api-doc/#create-new-conversation

        :param company_id: ID of the company
        :param phone: Phone
        :param provider: Provider
        :return:
        """
        response = self.request(
            method=Method.POST,
            endpoint=self._endpoint(None, company_id),
            body=ConversationCreate(provider=provider, phone=PhoneNumber(phone))
        )

        return response.to_class(ConversationResponse)

    def get_detail(self, company_id: int, conversation_id: int) -> ConversationResponse:
        """
        Retrieves conversation details from server
        https://pact-im.github.io/api-doc/#get-conversation-details

        :param company_id: ID of the company
        :param conversation_id: ID of the conversation
        :return: Conversation Detail
        """
        response = self.request(
            method=Method.GET,
            endpoint=self._endpoint('%s', company_id, conversation_id)
        )
        return response.to_class(ConversationResponse)

    def update_assignee(self, company_id: int, conversation_id: int, assignee_id: int) -> Optional[int]:
        """
        Update assignee for conversation
        This endpoint update assignee of conversation in the company using whatsapp channel
        https://pact-im.github.io/api-doc/#update-assignee-for-conversation

        :param company_id: ID of the company
        :param conversation_id: ID of the conversation
        :param assignee_id: User id
        :return: Conversation External ID
        """
        assert assignee_id > 0, 'assignee_id must be greater then 0'

        response = self.request(
            method=Method.PUT,
            endpoint=self._endpoint('%s/assign', company_id, conversation_id),
            body=dict(assignee_id=assignee_id)
        )
        return response.external_id
