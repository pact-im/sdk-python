from typing import Optional, Union

from .base import Service
from pact_im.schema.companies import CompanyListRequest, CompanyUpdate, CompaniesList, CreateCompany
from pact_im.schema import Method
from ..schema.base import PactResponse, SortDirection


class CompaniesService(Service):
    ENDPOINT = 'companies'

    def get_companies(self, from_: int = None, per: int = 50,
                      sort: Union[str, SortDirection] = SortDirection.ASC) -> CompaniesList:
        """This method return list of all user companies

        :param from_: Next page token geted from last request. Not valid or empty token return first page
        :param per: Number of elements per page. Default: 50
        :param sort: Change sorting direction. Available values: asc, desc. Default: asc
        :return CompaniesList:
        :rtype CompaniesList:
        :raise exceptions.ApiCallException: Api call error
        """
        query = CompanyListRequest.parse_obj({'from': from_, 'per': per, 'sort_direction': sort})

        response = self.request(
            method=Method.GET,
            endpoint=self._endpoint(),
            params=query
        )

        return response.to_class(CompaniesList)

    def update_company(self, external_id: int, name: Optional[str] = None, phone: Optional[str] = None,
                       description: Optional[str] = None,
                       webhook_url: Optional[str] = None, hidden: Optional[bool] = None) -> Optional[int]:
        """This method updates specific company attributes

        If you want to receive webhooks make sure that webhook_url is present.
            Webhook url must be valid and response code on POST json-request
            {'source':'pact.im', 'operation':'test'} must be 200
        :param external_id: Id of the company for update
        :param name: Company name
        :param phone: Official company phone number of contact person
        :param description: Company description
        :param webhook_url: Endpoint for webhooks
        :param hidden: Hide/Show a company in the Pact web ivnterface
        :return int:
        :raise exceptions.ApiCallException: Api call error
        """
        query = CompanyUpdate(name=name, phone=phone, description=description, webhook_url=webhook_url, hidden=hidden)

        response = self.request(
            method=Method.PUT,
            endpoint=self._endpoint('%s', str(external_id)),
            body=query
        )

        return response.data.get('external_id')

    def create_company(self, name: str, phone: Optional[str] = None, description: Optional[str] = None,
                       webhook_url: Optional[str] = None) -> Optional[int]:
        """
        This method creates a new company for user
         :param name: Company name
        :param phone: Official company phone number of contact person
        :param description: Company description
        :param webhook_url: Endpoint for webhooks
        :return int:
        :raise exceptions.ApiCallException: Api call error
        """
        query = CreateCompany(name=name, phone=phone, description=description, webhook_url=webhook_url)

        response = self.request(
            method=Method.POST,
            endpoint=self._endpoint(),
            body=query
        )

        return response.data.get('external_id')
