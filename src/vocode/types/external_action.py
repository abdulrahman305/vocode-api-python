# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .external_action_config import ExternalActionConfig
from .function_call_action_trigger import FunctionCallActionTrigger
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ExternalAction(UniversalBaseModel):
    id: str
    user_id: str
    type: typing.Literal["action_external"] = "action_external"
    config: ExternalActionConfig
    action_trigger: typing.Optional[FunctionCallActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
