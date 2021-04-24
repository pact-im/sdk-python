import unittest
from unittest import mock

from pact_im import PactClient
from pact_im.exceptions import PactBadRequest
from tests.mock import mocked_companies


class CompaniesServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = PactClient('some_token')
        self.srv = self.client.companies

    @mock.patch('requests.request', side_effect=mocked_companies)
    def test_get_companies(self, mock_request):
        companies = self.srv.get_companies()

        self.assertEqual(len(companies.companies), 1)
        self.assertEqual(companies.companies[0].name, 'COMPANY_NAME')

    @mock.patch('requests.request', side_effect=mocked_companies)
    def test_company_update(self, mock_request):
        external_id = self.srv.update_company(1, name='MockCompany')

        self.assertEqual(external_id, 1)

    @mock.patch('requests.request', side_effect=mocked_companies)
    def test_create_company(self, mock_request):
        external_id = self.srv.create_company(name='MockCompany')

        self.assertEqual(external_id, 5)

    @mock.patch('requests.request', side_effect=mocked_companies)
    def test_create_company_error(self, mock_request):
        try:
            _ = self.srv.create_company(name='MockCompanyError')
        except Exception as e:
            self.assertIsInstance(e, PactBadRequest)
