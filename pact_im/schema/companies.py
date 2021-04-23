from typing import Optional, List

from pydantic import BaseModel, AnyHttpUrl, Field
from .base import PactResponse, SortDirection


class Company(BaseModel):
    external_id: int
    name: str
    phone: Optional[str]
    description: Optional[str]
    webhook_url: Optional[AnyHttpUrl]


class CompaniesList(BaseModel):
    companies: List[Company]
    next_page: Optional[str]


class CompaniesListResponse(PactResponse):
    data: CompaniesList


class CompanyListRequest(BaseModel):
    from_: Optional[str] = Field(alias='from', max_length=255)
    per: Optional[int] = Field(50, ge=1, le=100)
    sort_direction: Optional[SortDirection] = Field(SortDirection.ASC)
