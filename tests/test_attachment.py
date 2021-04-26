import io

from pact_im.services import AttachmentService
from tests.mock import ServiceTestCase, mocked_attachment_service


class TestAttachmentService(ServiceTestCase):
    service = AttachmentService
    mock_func = mocked_attachment_service

    def test_upload_file(self):
        result = self.srv.upload_file(
            company_id=54,
            conversation_id=1,
            url='https://google.com/image.png'
        )
        self.assertEqual(result, 1)

        result_file = self.srv.upload_file(
            company_id=54,
            conversation_id=1,
            file=io.BytesIO(b'Awesome file Attachment')
        )
        self.assertEqual(result_file, 1)
