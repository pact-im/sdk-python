import datetime
from unittest.mock import patch

from pact_im.schema import Provider
from pact_im.schema.channels import ChannelInstagramUpdate
from pact_im.services import ChannelsService
from tests.mock import ServiceTestCase, mocked_channels


class ChannelsServiceTest(ServiceTestCase):
    service = ChannelsService
    mock_func = mocked_channels

    def test_get_channels(self):
        channels = self.srv.get_channels(
            company_id=5
        )
        self.assertEqual(channels.channels[0].external_id, 399)

    def test_create_channel_unified(self):
        result = self.srv.create_channel_unified(
            company_id=54,
            provider=Provider.WhatsApp,
            sync_messages_from=datetime.datetime(2021, 1, 1)
        )
        self.assertEqual(result, 1)

    def test_create_channel_whatsapp(self):
        result = self.srv.create_channel_whatsapp(
            company_id=54,
            sync_messages_from=datetime.datetime(2021, 1, 1)
        )
        self.assertEqual(result, 1)

    def test_create_channel_by_token(self):
        result = self.srv.create_channel_by_token(
            company_id=54,
            provider=Provider.Telegram,
            token='SomeSecretToken'
        )
        self.assertEqual(result, 1)

    def test_create_channel_instagram(self):
        result = self.srv.create_channel_instagram(
            company_id=54,
            login='user',
            password='password_user'
        )
        self.assertEqual(result, 1)

    def test_update_channel(self):
        result = self.srv.update_channel(
            company_id=54,
            channel_id=1,
            query=ChannelInstagramUpdate(login='user', password='pass')
        )
        self.assertEqual(result, 1)

    def test_update_channel_instagram(self):
        result = self.srv.update_channel_instagram(
            company_id=54,
            channel_id=1,
            login='user',
            password='pass'
        )
        self.assertEqual(result, 1)

    def test_update_channel_token(self):
        result = self.srv.update_channel_token(
            company_id=54,
            channel_id=1,
            token='SuperSecretNewToken'
        )
        self.assertEqual(result, 1)