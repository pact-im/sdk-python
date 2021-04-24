from typing import Optional, List

from pydantic import BaseModel, AnyHttpUrl, Field, root_validator
from .base import PactResponse, SortDirection


def is_not_none(v) -> bool:
    if v is None:
        return False
    return True


class Company(BaseModel):
    external_id: int
    name: str
    phone: Optional[str]
    description: Optional[str]
    webhook_url: Optional[AnyHttpUrl]


class CompaniesList(BaseModel):
    companies: List[Company]
    next_page: Optional[str]


class CompanyListRequest(BaseModel):
    from_: Optional[str] = Field(alias='from', max_length=255)
    per: Optional[int] = Field(50, ge=1, le=100)
    sort_direction: Optional[SortDirection] = Field(SortDirection.ASC)


class CompanyUpdate(BaseModel):
    name: Optional[str] = Field(max_length=255)
    phone: Optional[str]
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
    phone: Optional[str]
    description: Optional[str]
    webhook_url: Optional[AnyHttpUrl]
