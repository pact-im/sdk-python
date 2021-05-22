from pact_im.schema import Method
from pact_im.schema.messages import MessageResponse
from pact_im.services.base import Service


class JobsService(Service):
    ENDPOINT = 'companies/%s/channels/%s/jobs/%s'

    def get_job(self, company_id: int, channel_id: int, job_id: int) -> MessageResponse:
        """
        This method return info about message delivery job
        https://pact-im.github.io/api-doc/?shell#message-delivery-jobs

        :param company_id: ID of the company
        :param channel_id: iD of the channel
        :param job_id: Job ID
        :return:
        """
        response = self.request(
            method=Method.GET,
            endpoint=self._endpoint(None, company_id, channel_id, job_id)
        )

        return response.to_class(MessageResponse)

