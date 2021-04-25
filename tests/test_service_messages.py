from unittest import TestCase

from pact_im.services import ServiceMessagesService
from tests.mock import ServiceTestCase, mocked_service_messages_service


class TestServiceMessagesService(ServiceTestCase):
    service = ServiceMessagesService
    mock_func = mocked_service_messages_service

    def test_send_message(self):
        result = self.srv.send_message(
            company_id=54,
            phone='79250000001',
            short_message='hi',
            long_message='hello'
        )

        self.assertEqual(result.data, {
            "id": 42,
            "company_id": 154
        })
