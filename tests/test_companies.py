import unittest
from unittest import mock

from pact_im import PactClient
from pact_im.exceptions import PactBadRequest
from pact_im.services import CompaniesService
from tests.mock import mocked_companies, ServiceTestCase


class CompaniesServiceTest(ServiceTestCase):
    service = CompaniesService
    mock_func = mocked_companies

    def test_get_companies(self):
        companies = self.srv.get_companies()

        self.assertEqual(len(companies.companies), 1)
        self.assertEqual(companies.companies[0].name, 'COMPANY_NAME')

    def test_company_update(self):
        external_id = self.srv.update_company(1, name='MockCompany')

        self.assertEqual(external_id, 1)

    def test_create_company(self):
        external_id = self.srv.create_company(name='MockCompany')

        self.assertEqual(external_id, 5)

    def test_create_company_error(self):
        try:
            _ = self.srv.create_company(name='MockCompanyError')
        except Exception as e:
            self.assertIsInstance(e, PactBadRequest)
