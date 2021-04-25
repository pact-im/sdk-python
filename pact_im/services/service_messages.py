from pact_im.schema import Method
from pact_im.schema.base import PhoneNumber, PactResponse
from pact_im.schema.service_messages import ServiceMessageCreate
from pact_im.services.base import Service


class ServiceMessagesService(Service):
    ENDPOINT = 'companies/%s/service_messages'

    def send_message(self, company_id: int, phone: str, short_message: str, long_message: str) -> PactResponse:
        response = self.request(
            method=Method.POST,
            endpoint=self._endpoint(None, company_id),
            body=ServiceMessageCreate(phone=PhoneNumber(phone), short_text=short_message, long_text=long_message)
        )

        return response
