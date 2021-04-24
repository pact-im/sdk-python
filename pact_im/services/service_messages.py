from pact_im.services.base import Service


class ServiceMessagesService(Service):
    ENDPOINT = 'companies/%s/service_messages'

    def send_message(self, company_id: int, phone: str, short_message: str, long_message: str):
        # TODO https://pact-im.github.io/api-doc/?shell#service-messages
        pass