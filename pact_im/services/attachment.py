import os.path
from io import BytesIO
from typing import Union, Optional, IO

from pact_im.schema import Method
from pact_im.schema.attachments import FileUpload
from pact_im.services.base import Service


class AttachmentService(Service):
    ENDPOINT = 'companies/%s/conversations/%s/messages/attachments'

    def attach_local_file(self, company_id: int, conversation_id: int, file: Union[str, IO]) -> Optional[int]:
        if isinstance(file, str):
            if os.path.isfile(file):
                file_io = open(file, 'rb')
            else:
                raise FileNotFoundError(file)
        else:
            file_io = file

        response = self.request(
            method=Method.POST,
            endpoint=self._endpoint(None, company_id, conversation_id),
            file={'file': file_io}
        )

        return response.external_id

    def attach_remote_file(self, company_id: int, conversation_id: int, url: str) -> Optional[int]:
        response = self.request(
            method=Method.POST,
            endpoint=self._endpoint(None, company_id, conversation_id),
            body=FileUpload.parse_obj(dict(file_url=url))
        )
        return response.external_id

    def upload_file(self, company_id: int, conversation_id: int, *, url: str = None, file: Union[str, IO] = None):
        """
        Сreates an attachment which can be sent in message
        https://pact-im.github.io/api-doc/#upload-attachments

        :param company_id:
        :param conversation_id:
        :param url:
        :param file:
        :return:
        """
        assert url or file, 'must be set url or file'

        if url:
            return self.attach_remote_file(company_id, conversation_id, url)
        return self.attach_local_file(company_id, conversation_id, file)
