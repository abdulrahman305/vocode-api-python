# This file was auto-generated by Fern from our API Definition.

import typing

from .dtmf_action_params import DtmfActionParams
from .end_conversation_action_params import EndConversationActionParams
from .transfer_call_action_update_params import TransferCallActionUpdateParams

CreateActionRequest = typing.Union[TransferCallActionUpdateParams, EndConversationActionParams, DtmfActionParams]
