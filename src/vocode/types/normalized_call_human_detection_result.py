# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NormalizedCallHumanDetectionResult(str, enum.Enum):
    HUMAN = "human"
    NO_HUMAN = "no_human"

    def visit(self, human: typing.Callable[[], T_Result], no_human: typing.Callable[[], T_Result]) -> T_Result:
        if self is NormalizedCallHumanDetectionResult.HUMAN:
            return human()
        if self is NormalizedCallHumanDetectionResult.NO_HUMAN:
            return no_human()
