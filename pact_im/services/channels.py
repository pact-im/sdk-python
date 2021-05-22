import datetime
from typing import Union, Optional

from pydantic import BaseModel

from pact_im.schema import Method, SortDirection, Provider, ChallengeType, ConfirmationType
from pact_im.schema.base import PhoneNumber, PactResponse, PactResultResponse

from pact_im.schema.channels import ChannelListRequest, ChannelList, BaseChannelCreate, ChannelCreate, \
    WhatsAppChannelCreate, InstagramChannelCreate, ChannelInstagramUpdate, ChannelUpdate, Template, TemplateMessage, \
    CodeRequest, CodeConfirm, CodeConfirmTwoFactor, TelegramPersonalCodeResponse, TelegramPersonalConfirmationResponse
from pact_im.schema.messages import MessageResponse, MessageRequest
from pact_im.services.base import Service


class ChannelsService(Service):
    ENDPOINT = 'companies/%s/channels'

    def get_channels(self, company_id: int, from_: int = None, per: int = 50,
                     sort: Union[str, SortDirection] = SortDirection.ASC) -> ChannelList:
        """
        This method returns all the company channels
        https://pact-im.github.io/api-doc/#get-all-channels

        :param company_id: Id of the company
        :param from_: Next page token geted from last request. Not valid or empty token return first page
        :param per: Number of elements per page. Default: 50
        :param sort: Change sorting direction (sorting by id). Avilable values: asc, desc. Default: asc.
        :return:
        """
        query = ChannelListRequest(**{'from': from_, 'per': per, 'sort': sort})
        response = self.request(
            method=Method.GET,
            endpoint=self._endpoint(None, company_id),
            params=query
        )
        return response.to_class(ChannelList)

    def _create_channel(self, company_id: int, query: BaseChannelCreate) -> Optional[int]:
        """
        Create channel
        https://pact-im.github.io/api-doc/#create-new-channel

        :param company_id:
        :param query:
        :return:
        """
        response = self.request(
            Method.POST,
            self._endpoint(None, company_id),
            body=query
        )

        return response.external_id

    def create_channel_unified(self, company_id: int, provider: Union[str, Provider], **options) -> Optional[int]:
        """Unified method that can create channel in company.

        https://pact-im.github.io/api-doc/#create-new-channel

        Note:
            You can connect only one channel per one company for each provider.
            Contact with support if you want to use more than one channel

        :param company_id: Id of the company
        :param provider: Provider
        :param options:
        :keyword sync_messages_from: Only messages created after sync_messages_from will be synchronized
        :keyword do_not_mark_as_read: Do not mark chats as read after synchronization
        :keyword sync_comments:
        :keyword login:
        :keyword password:
        :keyword token:
        :return:
        """
        options.update(provider=provider)
        query = BaseChannelCreate.parse_obj(options)
        return self._create_channel(company_id, query)

    def create_channel_by_token(self, company_id: int, provider: Union[str, Provider], token: str) -> Optional[int]:
        """This method create a new channel in the company using token.

        https://pact-im.github.io/api-doc/#create-new-channel

        List of supported channels that can be created by token you can see in link above

        :param company_id: Id of the company
        :param provider: (facebook, viber, vk, ...)
        :param token:
        :return:
        """
        query = ChannelCreate(provider=provider, token=token)
        return self._create_channel(company_id, query)

    def create_channel_whatsapp(self, company_id: int, sync_messages_from: Optional[datetime.datetime] = None,
                                do_not_mark_as_read: Optional[bool] = None) -> Optional[int]:
        """This method create a new channel for WhatsApp

        https://pact-im.github.io/api-doc/#create-new-channel

        :param company_id: Id of the company
        :param sync_messages_from: Only messages created after will be synchronized
        :param do_not_mark_as_read: Do not mark chats as read after synchronization
        :return:
        """
        query = WhatsAppChannelCreate(provider=Provider.WhatsApp, sync_messages_from=sync_messages_from,
                                      do_not_mark_as_read=do_not_mark_as_read)
        return self._create_channel(company_id, query)

    def create_channel_instagram(self, company_id: int, login: str, password: str,
                                 sync_messages_from: Optional[datetime.datetime] = None,
                                 sync_comments: Optional[bool] = None) -> Optional[int]:
        """ This method create a new channel for Instagram

        :param company_id: Id of the company
        :param login: Instagram login
        :param password: Instagram password
        :param sync_messages_from: Only messages created after will be synchronized
        :param sync_comments:
        :return:
        """
        query = InstagramChannelCreate(provider=Provider.WhatsApp, login=login, password=password,
                                       sync_messages_from=sync_messages_from, sync_comments=sync_comments)
        return self._create_channel(company_id, query)

    def update_channel(self, company_id: int, channel_id: int, query: Optional[BaseModel] = None, **options) -> \
            Optional[int]:
        """This method updates existing channel in the company

        https://pact-im.github.io/api-doc/#update-channel

        :param query:
        :param company_id: Id of the company
        :param channel_id: Id of the channel
        :param options:
        :return:
        """
        assert company_id > 0, 'company_id must be greater then 0'
        assert channel_id > 0, 'channel_id must be greater then 0'

        response = self.request(
            method=Method.PUT,
            endpoint=self._endpoint('%s', company_id, channel_id),
            body=query or options
        )
        return response.external_id

    def update_channel_instagram(self, company_id: int, channel_id: int, login: str, password: str) -> Optional[int]:
        """This method updates instagramm channel

        https://pact-im.github.io/api-doc/#update-channel

        :param company_id: Id of the company
        :param channel_id: Id of the channel
        :param login: Instagram login
        :param password: Instagram password
        :return:
        """
        query = ChannelInstagramUpdate(login=login, password=password)
        return self.update_channel(company_id, channel_id, query=query)

    def update_channel_token(self, company_id: int, channel_id: int, token: str) -> Optional[int]:
        """This method updates channels that using tokens to auth

        https://pact-im.github.io/api-doc/#update-channel

        :param company_id: Id of the company
        :param channel_id: Id of the channel
        :param token:
        :return:
        """
        query = ChannelUpdate(token=token)
        return self.update_channel(company_id, channel_id, query=query)

    def send_whatsapp_template_message(self, company_id: int, channel_id: int, phone: str, template_id: str,
                                       template_language: str, template_parameters: dict) -> MessageResponse:
        """Send first message to whatsapp (business)

        https://pact-im.github.io/api-doc/#how-to-write-first-message-to-whatsapp-business

        :param company_id: Id of the company
        :param channel_id: Id of the channel
        :param phone: Phone
        :param template_id:
        :param template_language:
        :param template_parameters:
        :return:
        """
        template = Template(
            id=template_id,
            language_code=template_language,
            parameters=template_parameters
        )

        query = TemplateMessage(phone=PhoneNumber(phone), template=template)

        response = self.request(
            method=Method.POST,
            endpoint=self._endpoint('%s/conversations', company_id, channel_id),
            body=query
        )
        return response.to_class(MessageResponse)

    def send_first_whatsapp_message(self, company_id: int, channel_id: int, phone: str,
                                    message: str) -> MessageResponse:
        """Send first message to whatsapp

        https://pact-im.github.io/api-doc/#how-to-write-first-message-to-whatsapp

        :param company_id: Id of the company
        :param channel_id: Id of the channel
        :param phone: Phone
        :param message: Message
        :return:
        """
        query = MessageRequest(phone=phone, message=message)

        response = self.request(
            method=Method.POST,
            endpoint=self._endpoint('%s', company_id, channel_id),
            body=query
        )

        return response.to_class(MessageResponse)

    def delete_channel(self, company_id: int, channel_id: int) -> PactResponse:
        """
        Method deletes (disables) the channel
        https://pact-im.github.io/api-doc/#delete-channel

        :param company_id: Id of the company
        :param channel_id: Id of the channel
        :return:
        """
        response = self.request(
            method=Method.DELETE,
            endpoint=self._endpoint('%s', company_id, channel_id)
        )
        return response

    def request_channel_code(self, company_id: int, channel_id: int, provider: Union[str, Provider],
                             **parameters) -> dict:
        """
        https://pact-im.github.io/api-doc/#request-code-instagram-only

        :param company_id:
        :param channel_id:
        :param provider:
        :param parameters:
        :return:
        """
        query = CodeRequest(
            provider=provider,
            challenge_variant=parameters.get('challenge_variant'),
            challenge_type=parameters.get('challenge_type'),
        )
        response = self.request(
            method=Method.POST,
            endpoint=self._endpoint('%s/request_code', company_id, channel_id),
            body=query,
            json=True
        )
        return response

    def request_instagram_code(self, company_id: int, channel_id: int, challenge_variant: int) -> dict:
        """
        https://pact-im.github.io/api-doc/#request-code-instagram-only

        :param company_id: ID of the company
        :param channel_id: ID of the channel
        :param challenge_variant:
        :return:
        """
        return self.request_channel_code(company_id, channel_id, provider=Provider.Instagram,
                                         challenge_variant=challenge_variant)

    def request_instagram_two_factor_code(self, company_id: int, channel_id: int, challenge_type: Union[
        str, ChallengeType] = ChallengeType.TWO_FACTOR) -> dict:
        """
        https://pact-im.github.io/api-doc/#request-code-instagram-only

        :param company_id:
        :param channel_id:
        :return:
        """
        return self.request_channel_code(company_id, channel_id, provider=Provider.Instagram,
                                         challenge_type=challenge_type)

    def confirm_channel_code(self, company_id: int, channel_id: int, provider: Union[str, Provider],
                             **parameters) -> dict:
        """
        https://pact-im.github.io/api-doc/#confirm-code-instagram-only

        :param company_id: ID of the company
        :param channel_id: ID of the channel
        :param provider: Provider
        :param parameters:
        :return:
        """
        query = parameters.pop('query')
        if not query:
            query = parameters
            query.update(provider=provider)

        response = self.request(
            method=Method.POST,
            endpoint=self._endpoint('%s/confirm', company_id, channel_id),
            body=query,
            json=True
        )

        return response

    def confirm_instagram_code(self, company_id: int, channel_id: int, confirmation_code: str) -> dict:
        """
        https://pact-im.github.io/api-doc/#confirm-code-instagram-only

        :param company_id:
        :param channel_id:
        :param confirmation_code:
        :return:
        """
        query = CodeConfirm(provider=Provider.Instagram, confirmation_code=confirmation_code)
        return self.confirm_channel_code(company_id, channel_id, provider=query.provider, query=query)

    def confirm_instagram_two_factor_code(self, company_id: int, channel_id: int, confirmation_code: str,
                                          confirmation_variant: int) -> dict:
        """
        https://pact-im.github.io/api-doc/#confirm-code-instagram-only

        :param company_id:
        :param channel_id:
        :param confirmation_code:
        :param confirmation_variant:
        :return:
        """
        query = CodeConfirmTwoFactor(provider=Provider.Instagram, confirmation_code=confirmation_code,
                                     confirmation_type=ChallengeType.TWO_FACTOR,
                                     confirmation_variant=confirmation_variant)
        return self.confirm_channel_code(company_id, channel_id, provider=query.provider, query=query)

    def request_telegram_personal_code(self, company_id: int, channel_id: int) -> dict:
        """This endpoint request code for telegram personal

        https://pact-im.github.io/api-doc/#request-code-telegram-personal

        :param company_id: ID of the company
        :param channel_id: ID of the channel
        :rtype TelegramPersonalCodeResponse:
        :return: TelegramPersonalCodeResponse
        """
        response = self.request_channel_code(company_id, channel_id, provider=Provider.TelegramPersonal)
        return response.to_class(TelegramPersonalCodeResponse)

    def confirm_telegram_personal_code(self, company_id: int, channel_id: int,
                                       code: Union[str, int],
                                       confirmation_type: Union[
                                           str, ConfirmationType]) -> dict:
        """This endpoint confirm telegram personal channel with two types: code, password

        :param confirmation_type:
        :param company_id: ID of the company
        :param channel_id: ID of the channel
        :param code: Confirmation code
        :return:
        """
        return self.confirm_channel_code(company_id, channel_id, provider=Provider.TelegramPersonal,
                                         confirmation_type=confirmation_type, code=code)
