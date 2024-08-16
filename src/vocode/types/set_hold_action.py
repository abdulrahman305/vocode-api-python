# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .empty_action_config import EmptyActionConfig
from .set_hold_action_action_trigger import SetHoldActionActionTrigger
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class SetHoldAction(UniversalBaseModel):
    id: str
    user_id: str
    type: typing.Literal["action_set_hold"] = "action_set_hold"
    config: typing.Optional[EmptyActionConfig] = None
    action_trigger: typing.Optional[SetHoldActionActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
