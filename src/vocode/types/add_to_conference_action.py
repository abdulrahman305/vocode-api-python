# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .add_to_conference_config import AddToConferenceConfig
from .add_to_conference_action_action_trigger import AddToConferenceActionActionTrigger
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class AddToConferenceAction(UniversalBaseModel):
    id: str
    user_id: str
    type: typing.Literal["action_add_to_conference"] = "action_add_to_conference"
    config: AddToConferenceConfig
    action_trigger: typing.Optional[AddToConferenceActionActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
