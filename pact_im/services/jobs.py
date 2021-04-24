from pact_im.services.base import Service


class JobsService(Service):
    ENDPOINT = 'companies/%s/channels/%s/jobs/%s'

    def get_job(self, company_id: int, channel_id: int, job_id: int):
        # TODO https://pact-im.github.io/api-doc/?shell#message-delivery-jobs
        pass