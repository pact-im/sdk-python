from pact_im.base import PactClientBase
from pact_im.services.companies import CompaniesService


class PactClient(PactClientBase):

    @property
    def companies(self) -> CompaniesService:
        return CompaniesService(self)
