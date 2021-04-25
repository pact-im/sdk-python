from io import BytesIO
from typing import Union

from pact_im.services.base import Service


class AttachmentService(Service):
    ENDPOINT = 'companies/%s/conversations/%s/messages/attachments'

    def attach_local_file(self, company_id: int, conversation_id: int, file: BytesIO):
        # TODO attach_local_file
        pass

    def attach_remote_file(self, company_id: int, conversation_id: int, url: str):
        # TODO attach_remote_file
        pass

    def upload_file(self, company_id: int, conversation_id: int, file: Union[str, BytesIO]):
        # TODO uploadFile
        pass