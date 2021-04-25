from pact_im.services import MessagesService
from tests.mock import ServiceTestCase, mocked_messages_service


class TestMessageService(ServiceTestCase):
    service = MessagesService
    mock_func = mocked_messages_service

    def test_get_messages(self):
        result = self.srv.get_messages(
            company_id=54,
            conversation_id=1
        )
        self.assertEqual(result.messages[0].external_id, 47098)

    def test_send_message(self):
        result = self.srv.send_message(
            company_id=54,
            conversation_id=1,
            message='Hello',
            attachments=[123]
        )

        self.assertEqual(result.company_id, 154)
