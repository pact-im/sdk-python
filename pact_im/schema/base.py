import re

from typing import Optional, Union, Any

from pydantic import BaseModel, Field

from pact_im.schema import ResponseStatus, SortDirection


class PactResponse(BaseModel):
    status: ResponseStatus
    data: Optional[dict] = {}

    @property
    def external_id(self) -> Optional[int]:
        external_id = self.data.get('external_id')
        try:
            if not external_id and len(self.data):
                external_id = list(self.data.values())[0].get('external_id')
        except IndexError:
            pass
        return external_id

    def is_ok(self) -> bool:
        return self.status == ResponseStatus.OK

    def is_updated(self) -> bool:
        return self.status == ResponseStatus.UPDATED

    def is_created(self) -> bool:
        return self.status == ResponseStatus.CREATED

    def is_deleted(self) -> bool:
        return self.status == ResponseStatus.DELETED

    def is_success(self) -> bool:
        return any([
            self.is_ok(),
            self.is_deleted(),
            self.is_created(),
            self.is_updated()
        ])

    def to_class(self, class_: Any) -> Any:
        if not issubclass(class_, BaseModel):
            raise TypeError('class_ must be subclass of BaseModel')
        return class_.parse_obj(self.data)


class PactResultResponse(BaseModel):
    result: str


class NextPage(BaseModel):
    next_page: Optional[str]


class ListRequest(BaseModel):
    from_: Optional[str] = Field(alias='from', max_length=255)
    per: Optional[int] = Field(50, ge=1, le=100)
    sort_direction: Optional[Union[str, SortDirection]] = Field(SortDirection.ASC)


phone_number_regex = re.compile(r'^7\d{10}$')


class PhoneNumber(str):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError('string required')
        m = phone_number_regex.fullmatch(v.strip())
        if not m:
            raise ValueError('Phone number must be in format 79250000001')

        return cls(v.strip())

    def __repr__(self):
        return f'PhoneNumber({super().__repr__()})'
