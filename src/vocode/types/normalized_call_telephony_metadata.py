# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .twilio_telephony_metadata import TwilioTelephonyMetadata
from .vonage_telephony_metadata import VonageTelephonyMetadata


class NormalizedCallTelephonyMetadata_TelephonyMetadataVonage(VonageTelephonyMetadata):
    type: typing_extensions.Literal["telephony_metadata_vonage"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class NormalizedCallTelephonyMetadata_TelephonyMetadataTwilio(TwilioTelephonyMetadata):
    type: typing_extensions.Literal["telephony_metadata_twilio"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


NormalizedCallTelephonyMetadata = typing.Union[
    NormalizedCallTelephonyMetadata_TelephonyMetadataVonage, NormalizedCallTelephonyMetadata_TelephonyMetadataTwilio
]
