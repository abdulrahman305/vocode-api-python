# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .pinecone_vector_database_update_params_index import PineconeVectorDatabaseUpdateParamsIndex
from .pinecone_vector_database_update_params_api_key import PineconeVectorDatabaseUpdateParamsApiKey
from .pinecone_vector_database_update_params_api_environment import PineconeVectorDatabaseUpdateParamsApiEnvironment
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PineconeVectorDatabaseUpdateParams(UniversalBaseModel):
    type: typing.Literal["vector_database_pinecone"] = "vector_database_pinecone"
    index: typing.Optional[PineconeVectorDatabaseUpdateParamsIndex] = None
    api_key: typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey] = None
    api_environment: typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
