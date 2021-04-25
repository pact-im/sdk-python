from pact_im.services import MessageService
from tests.mock import ServiceTestCase, mocked_messages_service


class TestMessageService(ServiceTestCase):
    service = MessageService
    mock_func = mocked_messages_service

    def test_get_messages(self):
        self.fail()

    def test_send_message(self):
        self.fail()
