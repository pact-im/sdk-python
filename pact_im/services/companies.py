from .base import Service
from pact_im.schema.companies import CompanyListRequest, CompaniesListResponse
from pact_im.schema import Method


class CompaniesService(Service):
    ENDPOINT = 'companies'

    def get_companies(self, from_: int = None, per: int = None, sort: str = None):
        query = CompanyListRequest.parse_obj({'from': from_, 'per': per, 'sort_direction': sort})

        response = self.request(
            method=Method.GET,
            method_endpoint='',
            params=query.dict(exclude_defaults=True, exclude_none=True)
        )
        return CompaniesListResponse.parse_raw(response)

    def update_company(self):
        pass

    def create_company(self):
        pass
