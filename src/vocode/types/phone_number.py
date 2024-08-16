# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .agent import Agent
from .phone_number_telephony_provider import PhoneNumberTelephonyProvider
from .twilio_account_connection import TwilioAccountConnection
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PhoneNumber(UniversalBaseModel):
    id: str
    user_id: str
    active: typing.Optional[bool] = None
    label: typing.Optional[str] = None
    inbound_agent: typing.Optional[Agent] = None
    outbound_only: typing.Optional[bool] = None
    example_context: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    number: str
    telephony_provider: typing.Optional[PhoneNumberTelephonyProvider] = None
    telephony_account_connection: typing.Optional[TwilioAccountConnection] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
