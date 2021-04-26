import unittest

from pact_im import PactClient
from pact_im.base import PactClientBase
from pact_im.exceptions import InvalidArgumentException
from pact_im import services as s

BASE_API_ENDPOINT = 'https://api.pact.im/p1/'


class PactClientTest(unittest.TestCase):

    def setUp(self):
        self.client = PactClient('some_token')

    def test_wrong_token(self):
        try:
            PactClient('')
        except Exception as e:
            self.assertIsInstance(e, InvalidArgumentException)

    def test_client(self):
        self.assertEqual(self.client.base_url, BASE_API_ENDPOINT)
        self.assertIsInstance(self.client, PactClientBase)

    def test_service_companies(self):
        service = self.client.companies
        self.assertIsInstance(service, s.CompaniesService)
        self.assertEqual(service.get_endpoint(), 'companies')

    def test_service_channels(self):
        service = self.client.channels
        self.assertIsInstance(service, s.ChannelsService)
        self.assertEqual(service.get_endpoint(), 'companies/%s/channels')

    def test_service_conversations(self):
        service = self.client.conversations
        self.assertIsInstance(service, s.ConversationsService)
        self.assertEqual(service.get_endpoint(), 'companies/%s/conversations')

    def test_service_messages(self):
        service = self.client.messages
        self.assertIsInstance(service, s.MessagesService)
        self.assertEqual(service.get_endpoint(), 'companies/%s/conversations/%s/messages')

    def test_service_jobs(self):
        service = self.client.jobs
        self.assertIsInstance(service, s.JobsService)
        self.assertEqual(service.get_endpoint(), 'companies/%s/channels/%s/jobs/%s')

    def test_service_service_messages(self):
        service = self.client.service_messages
        self.assertIsInstance(service, s.ServiceMessagesService)
        self.assertEqual(service.get_endpoint(), 'companies/%s/service_messages')
