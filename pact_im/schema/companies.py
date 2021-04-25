from typing import Optional, List, Union

from pydantic import BaseModel, AnyHttpUrl, Field, root_validator

from pact_im.schema import SortDirection
from pact_im.schema.base import NextPage, ListRequest, PhoneNumber


def is_not_none(v) -> bool:
    if v is None:
        return False
    return True


class Company(BaseModel):
    external_id: int
    name: str
    phone: Optional[PhoneNumber]
    description: Optional[str]
    webhook_url: Optional[AnyHttpUrl]


class CompaniesList(NextPage):
    companies: List[Company]


class CompanyListRequest(ListRequest):
    pass


class CompanyUpdate(BaseModel):
    name: Optional[str] = Field(max_length=255)
    phone: Optional[PhoneNumber]
    description: Optional[str]
    webhook_url: Optional[AnyHttpUrl]
    hidden: Optional[bool]

    @root_validator
    def non_none_update(cls, values):
        if not any([is_not_none(v) for v in values.values()]):
            raise ValueError('at least one parameter must be passed')
        return values


class CreateCompany(BaseModel):
    name: str = Field(..., max_length=255)
    phone: Optional[PhoneNumber]
    description: Optional[str]
    webhook_url: Optional[AnyHttpUrl]
