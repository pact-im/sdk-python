from pact_im.base import PactClientBase
from pact_im import services


class PactClient(PactClientBase):

    @property
    def companies(self) -> services.CompaniesService:
        return services.CompaniesService(self)

    @property
    def channels(self) -> services.ChannelsService:
        return services.ChannelsService(self)

    @property
    def conversations(self) -> services.ConversationsService:
        return services.ConversationsService(self)

    @property
    def messages(self) -> services.MessagesService:
        return services.MessagesService(self)

    @property
    def jobs(self) -> services.JobsService:
        return services.JobsService(self)

    @property
    def service_messages(self) -> services.ServiceMessagesService:
        return services.ServiceMessagesService(self)

    @property
    def attachment(self) -> services.AttachmentService:
        return services.AttachmentService(self)