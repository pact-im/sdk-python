import datetime
from typing import Union, Optional

from pact_im.schema.base import SortDirection, Provider
from pact_im.services.base import Service


class ChannelsService(Service):
    ENDPOINT = 'companies/%s/channels'

    def get_all_channels(self, company_id:int, from_: int = None, per: int = None, sort: Union[str, SortDirection] = None):
        # TODO Get All channels https://pact-im.github.io/api-doc/?php#get-all-channels
        pass

    def create_new_channel(self, company_id: int, provider: str, **options):
        # TODO create_new_channel https://pact-im.github.io/api-doc/?php#create-new-channel
        pass

    def update_channel(self, company_id: int, channel_id: int, **options):
        # TODO update_channel https://pact-im.github.io/api-doc/?php#update-channel
        pass

    def delete_channel(self, company_id: int, channel_id: int):
        # TODO delete_channel https://pact-im.github.io/api-doc/?php#delete-channel
        pass

    def send_first_whatsapp_message(self, phone: str, text: str):
        pass

    def request_code(self, company_id: int, channel_id: int, provider: str, challenge_type: Optional[str] = None,
                     challenge_variant: Optional[int] = None):
        assert challenge_variant or challenge_type, 'required challenge_type or challenge_variant'
        # TODO   request_code https://pact-im.github.io/api-doc/?shell#request-code-instagram-only
        return 1

    def confirm_code(self, company_id: int, channel_id: int, provider: str, confirmation_code: str, **options):
        confirmation_type = options.get('confirmation_type')
        confirmation_variant = options.get('confirmation_variant')
        # TODO confirm_code https://pact-im.github.io/api-doc/?shell#confirm-code-instagram-only
        return 1

    def request_challenge_code(self, company_id: int, channel_id: int, challenge_variant: int = 0):
        # TODO What is challenge_variant? Why == 0
        return self.request_code(company_id, channel_id, Provider.Instagram, challenge_variant=challenge_variant)

    def request_two_factor_code(self, company_id: int, channel_id: int, challenge_type: str = 'two_factor'):
        return self.request_code(company_id, channel_id, Provider.Instagram, challenge_type=challenge_type)

    def confirm_challenge_code(self, company_id: int, channel_id: int, confirmation_code: str):
        return self.confirm_code(company_id, channel_id, Provider.Instagram, confirmation_code=confirmation_code)

    def confirm_two_factor_code(self, company_id: int, channel_id: int, confirmation_code: str,
                                confirmation_variant: int, confirmation_type: str = 'two_factor'):
        return self.confirm_code(company_id, channel_id, Provider.Instagram, confirmation_code=confirmation_code,
                                 confirmation_type=confirmation_type, confirmation_variant=confirmation_variant)
