from typing import Optional

from .base import Service
from pact_im.schema.companies import CompanyListRequest, CompanyUpdate, CompaniesList
from pact_im.schema import Method
from ..schema.base import PactResponse


class CompaniesService(Service):
    ENDPOINT = 'companies'

    def get_companies(self, from_: int = None, per: int = None, sort: str = None) -> CompaniesList:
        query = CompanyListRequest.parse_obj({'from': from_, 'per': per, 'sort_direction': sort})

        response = self.request(
            method=Method.GET,
            method_endpoint='',
            params=query.dict(exclude_defaults=True, exclude_none=True)
        )
        response_model = PactResponse.parse_raw(response)

        return CompaniesList.parse_obj(response_model.data)

    def update_company(self, external_id: int, name: Optional[str], phone: Optional[str], description: Optional[str],
                       webhook_url: Optional[str], hidden: Optional[bool]) -> Optional[int]:
        query = CompanyUpdate(name=name, phone=phone, description=description, webhook_url=webhook_url, hidden=hidden)

        response = self.request(
            method=Method.PUT,
            method_endpoint=str(external_id),
            params=query.dict(exclude_defaults=True, exclude_none=True)
        )
        response_model = PactResponse.parse_raw(response)

        return response_model.data.get('external_id')

    def create_company(self):
        pass
