from pact_im.services import ConversationsService
from tests.mock import ServiceTestCase, mocked_conversations


class TestConversationsService(ServiceTestCase):
    service = ConversationsService
    mock_func = mocked_conversations

    def test_get_conversations(self):
        result = self.srv.get_conversations(
            company_id=54
        )
        self.assertEqual(len(result.conversations), 1)
        first = result.conversations[0]
        self.assertEqual(first.name, 'Friend')
        self.assertEqual(first.sender_external_id, '79260000001')

    def test_create_conversation(self):
        result = self.srv.create_conversation(
            company_id=54,
            phone='79250000001'
        )
        self.assertEqual(result.conversation.name, '79250000001')

    def test_get_detail(self):
        result = self.srv.get_detail(
            company_id=54,
            conversation_id=1
        )
        self.assertEqual(result.conversation.name, '79250000001')

    def test_update_assignee(self):
        result = self.srv.update_assignee(
            company_id=54,
            conversation_id=1,
            assignee_id=1
        )
        self.assertEqual(result, 1)
