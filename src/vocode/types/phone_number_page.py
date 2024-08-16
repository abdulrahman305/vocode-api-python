# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .normalized_phone_number import NormalizedPhoneNumber
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PhoneNumberPage(UniversalBaseModel):
    items: typing.List[NormalizedPhoneNumber]
    page: int
    size: int
    has_more: bool
    total: int
    total_is_estimated: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
