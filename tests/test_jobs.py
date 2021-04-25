from unittest import TestCase

from pact_im.services import JobsService
from tests.mock import ServiceTestCase, mocked_jobs


class TestJobsService(ServiceTestCase):
    service = JobsService
    mock_func = mocked_jobs

    def test_get_job(self):
        result = self.srv.get_job(
            company_id=54,
            channel_id=1,
            job_id=1
        )
        self.assertEqual(result.state, 'delivered')
        self.assertEqual(result.message_id, 1)
        self.assertEqual(result.details, {'result': 'DELIVERED'})
