# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agent import Agent
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.agent_page import AgentPage
from ..types.agent_params_prompt import AgentParamsPrompt
from ..types.agent_params_voice import AgentParamsVoice
from ..types.language import Language
from ..types.agent_params_actions_item import AgentParamsActionsItem
from ..types.agent_params_webhook import AgentParamsWebhook
from ..types.agent_params_vector_database import AgentParamsVectorDatabase
from ..types.interrupt_sensitivity import InterruptSensitivity
from ..types.agent_params_endpointing_sensitivity import AgentParamsEndpointingSensitivity
from ..types.agent_params_ivr_navigation_mode import AgentParamsIvrNavigationMode
from ..types.agent_params_openai_account_connection import AgentParamsOpenaiAccountConnection
from ..types.internal_llm_fallback import InternalLlmFallback
from ..types.agent_params_deepgram_keywords_value import AgentParamsDeepgramKeywordsValue
from ..types.agent_update_params_name import AgentUpdateParamsName
from ..types.agent_update_params_prompt import AgentUpdateParamsPrompt
from ..types.agent_update_params_language import AgentUpdateParamsLanguage
from ..types.agent_update_params_actions import AgentUpdateParamsActions
from ..types.agent_update_params_voice import AgentUpdateParamsVoice
from ..types.agent_update_params_initial_message import AgentUpdateParamsInitialMessage
from ..types.agent_update_params_webhook import AgentUpdateParamsWebhook
from ..types.agent_update_params_vector_database import AgentUpdateParamsVectorDatabase
from ..types.agent_update_params_interrupt_sensitivity import AgentUpdateParamsInterruptSensitivity
from ..types.agent_update_params_context_endpoint import AgentUpdateParamsContextEndpoint
from ..types.agent_update_params_noise_suppression import AgentUpdateParamsNoiseSuppression
from ..types.agent_update_params_endpointing_sensitivity import AgentUpdateParamsEndpointingSensitivity
from ..types.agent_update_params_ivr_navigation_mode import AgentUpdateParamsIvrNavigationMode
from ..types.agent_update_params_conversation_speed import AgentUpdateParamsConversationSpeed
from ..types.agent_update_params_initial_message_delay import AgentUpdateParamsInitialMessageDelay
from ..types.agent_update_params_openai_model_name_override import AgentUpdateParamsOpenaiModelNameOverride
from ..types.agent_update_params_ask_if_human_present_on_idle import AgentUpdateParamsAskIfHumanPresentOnIdle
from ..types.agent_update_params_openai_account_connection import AgentUpdateParamsOpenaiAccountConnection
from ..types.agent_update_params_run_do_not_call_detection import AgentUpdateParamsRunDoNotCallDetection
from ..types.agent_update_params_llm_fallback import AgentUpdateParamsLlmFallback
from ..types.agent_update_params_deepgram_keywords import AgentUpdateParamsDeepgramKeywords
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AgentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_agent(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> Agent:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            Successful Response

        Examples
        --------
        from vocode import Vocode

        client = Vocode(
            token="YOUR_TOKEN",
        )
        client.agents.get_agent(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/agents",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Agent,
                    parse_obj_as(
                        type_=Agent,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_agents(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentPage
            Successful Response

        Examples
        --------
        from vocode import Vocode

        client = Vocode(
            token="YOUR_TOKEN",
        )
        client.agents.list_agents()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/agents/list",
            method="GET",
            params={
                "page": page,
                "size": size,
                "sort_column": sort_column,
                "sort_desc": sort_desc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AgentPage,
                    parse_obj_as(
                        type_=AgentPage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_agent(
        self,
        *,
        prompt: AgentParamsPrompt,
        voice: AgentParamsVoice,
        name: typing.Optional[str] = OMIT,
        language: typing.Optional[Language] = OMIT,
        actions: typing.Optional[typing.Sequence[AgentParamsActionsItem]] = OMIT,
        initial_message: typing.Optional[str] = OMIT,
        webhook: typing.Optional[AgentParamsWebhook] = OMIT,
        vector_database: typing.Optional[AgentParamsVectorDatabase] = OMIT,
        interrupt_sensitivity: typing.Optional[InterruptSensitivity] = OMIT,
        context_endpoint: typing.Optional[str] = OMIT,
        noise_suppression: typing.Optional[bool] = OMIT,
        endpointing_sensitivity: typing.Optional[AgentParamsEndpointingSensitivity] = OMIT,
        ivr_navigation_mode: typing.Optional[AgentParamsIvrNavigationMode] = OMIT,
        conversation_speed: typing.Optional[float] = OMIT,
        initial_message_delay: typing.Optional[float] = OMIT,
        openai_model_name_override: typing.Optional[str] = OMIT,
        ask_if_human_present_on_idle: typing.Optional[bool] = OMIT,
        openai_account_connection: typing.Optional[AgentParamsOpenaiAccountConnection] = OMIT,
        run_do_not_call_detection: typing.Optional[bool] = OMIT,
        llm_fallback: typing.Optional[InternalLlmFallback] = OMIT,
        deepgram_keywords: typing.Optional[typing.Dict[str, typing.Optional[AgentParamsDeepgramKeywordsValue]]] = OMIT,
        llm_temperature: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Agent:
        """
        Parameters
        ----------
        prompt : AgentParamsPrompt

        voice : AgentParamsVoice

        name : typing.Optional[str]

        language : typing.Optional[Language]

        actions : typing.Optional[typing.Sequence[AgentParamsActionsItem]]

        initial_message : typing.Optional[str]

        webhook : typing.Optional[AgentParamsWebhook]

        vector_database : typing.Optional[AgentParamsVectorDatabase]

        interrupt_sensitivity : typing.Optional[InterruptSensitivity]

        context_endpoint : typing.Optional[str]

        noise_suppression : typing.Optional[bool]

        endpointing_sensitivity : typing.Optional[AgentParamsEndpointingSensitivity]

        ivr_navigation_mode : typing.Optional[AgentParamsIvrNavigationMode]

        conversation_speed : typing.Optional[float]

        initial_message_delay : typing.Optional[float]

        openai_model_name_override : typing.Optional[str]

        ask_if_human_present_on_idle : typing.Optional[bool]

        openai_account_connection : typing.Optional[AgentParamsOpenaiAccountConnection]

        run_do_not_call_detection : typing.Optional[bool]

        llm_fallback : typing.Optional[InternalLlmFallback]

        deepgram_keywords : typing.Optional[typing.Dict[str, typing.Optional[AgentParamsDeepgramKeywordsValue]]]

        llm_temperature : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            Successful Response

        Examples
        --------
        from vocode import Vocode

        client = Vocode(
            token="YOUR_TOKEN",
        )
        client.agents.create_agent(
            prompt="prompt",
            voice="voice",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/agents/create",
            method="POST",
            json={
                "name": name,
                "prompt": prompt,
                "language": language,
                "actions": actions,
                "voice": voice,
                "initial_message": initial_message,
                "webhook": webhook,
                "vector_database": vector_database,
                "interrupt_sensitivity": interrupt_sensitivity,
                "context_endpoint": context_endpoint,
                "noise_suppression": noise_suppression,
                "endpointing_sensitivity": endpointing_sensitivity,
                "ivr_navigation_mode": ivr_navigation_mode,
                "conversation_speed": conversation_speed,
                "initial_message_delay": initial_message_delay,
                "openai_model_name_override": openai_model_name_override,
                "ask_if_human_present_on_idle": ask_if_human_present_on_idle,
                "openai_account_connection": openai_account_connection,
                "run_do_not_call_detection": run_do_not_call_detection,
                "llm_fallback": llm_fallback,
                "deepgram_keywords": deepgram_keywords,
                "llm_temperature": llm_temperature,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Agent,
                    parse_obj_as(
                        type_=Agent,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_agent(
        self,
        *,
        id: str,
        name: typing.Optional[AgentUpdateParamsName] = OMIT,
        prompt: typing.Optional[AgentUpdateParamsPrompt] = OMIT,
        language: typing.Optional[AgentUpdateParamsLanguage] = OMIT,
        actions: typing.Optional[AgentUpdateParamsActions] = OMIT,
        voice: typing.Optional[AgentUpdateParamsVoice] = OMIT,
        initial_message: typing.Optional[AgentUpdateParamsInitialMessage] = OMIT,
        webhook: typing.Optional[AgentUpdateParamsWebhook] = OMIT,
        vector_database: typing.Optional[AgentUpdateParamsVectorDatabase] = OMIT,
        interrupt_sensitivity: typing.Optional[AgentUpdateParamsInterruptSensitivity] = OMIT,
        context_endpoint: typing.Optional[AgentUpdateParamsContextEndpoint] = OMIT,
        noise_suppression: typing.Optional[AgentUpdateParamsNoiseSuppression] = OMIT,
        endpointing_sensitivity: typing.Optional[AgentUpdateParamsEndpointingSensitivity] = OMIT,
        ivr_navigation_mode: typing.Optional[AgentUpdateParamsIvrNavigationMode] = OMIT,
        conversation_speed: typing.Optional[AgentUpdateParamsConversationSpeed] = OMIT,
        initial_message_delay: typing.Optional[AgentUpdateParamsInitialMessageDelay] = OMIT,
        openai_model_name_override: typing.Optional[AgentUpdateParamsOpenaiModelNameOverride] = OMIT,
        ask_if_human_present_on_idle: typing.Optional[AgentUpdateParamsAskIfHumanPresentOnIdle] = OMIT,
        openai_account_connection: typing.Optional[AgentUpdateParamsOpenaiAccountConnection] = OMIT,
        run_do_not_call_detection: typing.Optional[AgentUpdateParamsRunDoNotCallDetection] = OMIT,
        llm_fallback: typing.Optional[AgentUpdateParamsLlmFallback] = OMIT,
        deepgram_keywords: typing.Optional[AgentUpdateParamsDeepgramKeywords] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Agent:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[AgentUpdateParamsName]

        prompt : typing.Optional[AgentUpdateParamsPrompt]

        language : typing.Optional[AgentUpdateParamsLanguage]

        actions : typing.Optional[AgentUpdateParamsActions]

        voice : typing.Optional[AgentUpdateParamsVoice]

        initial_message : typing.Optional[AgentUpdateParamsInitialMessage]

        webhook : typing.Optional[AgentUpdateParamsWebhook]

        vector_database : typing.Optional[AgentUpdateParamsVectorDatabase]

        interrupt_sensitivity : typing.Optional[AgentUpdateParamsInterruptSensitivity]

        context_endpoint : typing.Optional[AgentUpdateParamsContextEndpoint]

        noise_suppression : typing.Optional[AgentUpdateParamsNoiseSuppression]

        endpointing_sensitivity : typing.Optional[AgentUpdateParamsEndpointingSensitivity]

        ivr_navigation_mode : typing.Optional[AgentUpdateParamsIvrNavigationMode]

        conversation_speed : typing.Optional[AgentUpdateParamsConversationSpeed]

        initial_message_delay : typing.Optional[AgentUpdateParamsInitialMessageDelay]

        openai_model_name_override : typing.Optional[AgentUpdateParamsOpenaiModelNameOverride]

        ask_if_human_present_on_idle : typing.Optional[AgentUpdateParamsAskIfHumanPresentOnIdle]

        openai_account_connection : typing.Optional[AgentUpdateParamsOpenaiAccountConnection]

        run_do_not_call_detection : typing.Optional[AgentUpdateParamsRunDoNotCallDetection]

        llm_fallback : typing.Optional[AgentUpdateParamsLlmFallback]

        deepgram_keywords : typing.Optional[AgentUpdateParamsDeepgramKeywords]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            Successful Response

        Examples
        --------
        from vocode import Vocode

        client = Vocode(
            token="YOUR_TOKEN",
        )
        client.agents.update_agent(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/agents/update",
            method="POST",
            params={
                "id": id,
            },
            json={
                "name": name,
                "prompt": prompt,
                "language": language,
                "actions": actions,
                "voice": voice,
                "initial_message": initial_message,
                "webhook": webhook,
                "vector_database": vector_database,
                "interrupt_sensitivity": interrupt_sensitivity,
                "context_endpoint": context_endpoint,
                "noise_suppression": noise_suppression,
                "endpointing_sensitivity": endpointing_sensitivity,
                "ivr_navigation_mode": ivr_navigation_mode,
                "conversation_speed": conversation_speed,
                "initial_message_delay": initial_message_delay,
                "openai_model_name_override": openai_model_name_override,
                "ask_if_human_present_on_idle": ask_if_human_present_on_idle,
                "openai_account_connection": openai_account_connection,
                "run_do_not_call_detection": run_do_not_call_detection,
                "llm_fallback": llm_fallback,
                "deepgram_keywords": deepgram_keywords,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Agent,
                    parse_obj_as(
                        type_=Agent,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAgentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_agent(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> Agent:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            Successful Response

        Examples
        --------
        import asyncio

        from vocode import AsyncVocode

        client = AsyncVocode(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.get_agent(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/agents",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Agent,
                    parse_obj_as(
                        type_=Agent,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_agents(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentPage
            Successful Response

        Examples
        --------
        import asyncio

        from vocode import AsyncVocode

        client = AsyncVocode(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.list_agents()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/agents/list",
            method="GET",
            params={
                "page": page,
                "size": size,
                "sort_column": sort_column,
                "sort_desc": sort_desc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AgentPage,
                    parse_obj_as(
                        type_=AgentPage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_agent(
        self,
        *,
        prompt: AgentParamsPrompt,
        voice: AgentParamsVoice,
        name: typing.Optional[str] = OMIT,
        language: typing.Optional[Language] = OMIT,
        actions: typing.Optional[typing.Sequence[AgentParamsActionsItem]] = OMIT,
        initial_message: typing.Optional[str] = OMIT,
        webhook: typing.Optional[AgentParamsWebhook] = OMIT,
        vector_database: typing.Optional[AgentParamsVectorDatabase] = OMIT,
        interrupt_sensitivity: typing.Optional[InterruptSensitivity] = OMIT,
        context_endpoint: typing.Optional[str] = OMIT,
        noise_suppression: typing.Optional[bool] = OMIT,
        endpointing_sensitivity: typing.Optional[AgentParamsEndpointingSensitivity] = OMIT,
        ivr_navigation_mode: typing.Optional[AgentParamsIvrNavigationMode] = OMIT,
        conversation_speed: typing.Optional[float] = OMIT,
        initial_message_delay: typing.Optional[float] = OMIT,
        openai_model_name_override: typing.Optional[str] = OMIT,
        ask_if_human_present_on_idle: typing.Optional[bool] = OMIT,
        openai_account_connection: typing.Optional[AgentParamsOpenaiAccountConnection] = OMIT,
        run_do_not_call_detection: typing.Optional[bool] = OMIT,
        llm_fallback: typing.Optional[InternalLlmFallback] = OMIT,
        deepgram_keywords: typing.Optional[typing.Dict[str, typing.Optional[AgentParamsDeepgramKeywordsValue]]] = OMIT,
        llm_temperature: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Agent:
        """
        Parameters
        ----------
        prompt : AgentParamsPrompt

        voice : AgentParamsVoice

        name : typing.Optional[str]

        language : typing.Optional[Language]

        actions : typing.Optional[typing.Sequence[AgentParamsActionsItem]]

        initial_message : typing.Optional[str]

        webhook : typing.Optional[AgentParamsWebhook]

        vector_database : typing.Optional[AgentParamsVectorDatabase]

        interrupt_sensitivity : typing.Optional[InterruptSensitivity]

        context_endpoint : typing.Optional[str]

        noise_suppression : typing.Optional[bool]

        endpointing_sensitivity : typing.Optional[AgentParamsEndpointingSensitivity]

        ivr_navigation_mode : typing.Optional[AgentParamsIvrNavigationMode]

        conversation_speed : typing.Optional[float]

        initial_message_delay : typing.Optional[float]

        openai_model_name_override : typing.Optional[str]

        ask_if_human_present_on_idle : typing.Optional[bool]

        openai_account_connection : typing.Optional[AgentParamsOpenaiAccountConnection]

        run_do_not_call_detection : typing.Optional[bool]

        llm_fallback : typing.Optional[InternalLlmFallback]

        deepgram_keywords : typing.Optional[typing.Dict[str, typing.Optional[AgentParamsDeepgramKeywordsValue]]]

        llm_temperature : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            Successful Response

        Examples
        --------
        import asyncio

        from vocode import AsyncVocode

        client = AsyncVocode(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.create_agent(
                prompt="prompt",
                voice="voice",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/agents/create",
            method="POST",
            json={
                "name": name,
                "prompt": prompt,
                "language": language,
                "actions": actions,
                "voice": voice,
                "initial_message": initial_message,
                "webhook": webhook,
                "vector_database": vector_database,
                "interrupt_sensitivity": interrupt_sensitivity,
                "context_endpoint": context_endpoint,
                "noise_suppression": noise_suppression,
                "endpointing_sensitivity": endpointing_sensitivity,
                "ivr_navigation_mode": ivr_navigation_mode,
                "conversation_speed": conversation_speed,
                "initial_message_delay": initial_message_delay,
                "openai_model_name_override": openai_model_name_override,
                "ask_if_human_present_on_idle": ask_if_human_present_on_idle,
                "openai_account_connection": openai_account_connection,
                "run_do_not_call_detection": run_do_not_call_detection,
                "llm_fallback": llm_fallback,
                "deepgram_keywords": deepgram_keywords,
                "llm_temperature": llm_temperature,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Agent,
                    parse_obj_as(
                        type_=Agent,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_agent(
        self,
        *,
        id: str,
        name: typing.Optional[AgentUpdateParamsName] = OMIT,
        prompt: typing.Optional[AgentUpdateParamsPrompt] = OMIT,
        language: typing.Optional[AgentUpdateParamsLanguage] = OMIT,
        actions: typing.Optional[AgentUpdateParamsActions] = OMIT,
        voice: typing.Optional[AgentUpdateParamsVoice] = OMIT,
        initial_message: typing.Optional[AgentUpdateParamsInitialMessage] = OMIT,
        webhook: typing.Optional[AgentUpdateParamsWebhook] = OMIT,
        vector_database: typing.Optional[AgentUpdateParamsVectorDatabase] = OMIT,
        interrupt_sensitivity: typing.Optional[AgentUpdateParamsInterruptSensitivity] = OMIT,
        context_endpoint: typing.Optional[AgentUpdateParamsContextEndpoint] = OMIT,
        noise_suppression: typing.Optional[AgentUpdateParamsNoiseSuppression] = OMIT,
        endpointing_sensitivity: typing.Optional[AgentUpdateParamsEndpointingSensitivity] = OMIT,
        ivr_navigation_mode: typing.Optional[AgentUpdateParamsIvrNavigationMode] = OMIT,
        conversation_speed: typing.Optional[AgentUpdateParamsConversationSpeed] = OMIT,
        initial_message_delay: typing.Optional[AgentUpdateParamsInitialMessageDelay] = OMIT,
        openai_model_name_override: typing.Optional[AgentUpdateParamsOpenaiModelNameOverride] = OMIT,
        ask_if_human_present_on_idle: typing.Optional[AgentUpdateParamsAskIfHumanPresentOnIdle] = OMIT,
        openai_account_connection: typing.Optional[AgentUpdateParamsOpenaiAccountConnection] = OMIT,
        run_do_not_call_detection: typing.Optional[AgentUpdateParamsRunDoNotCallDetection] = OMIT,
        llm_fallback: typing.Optional[AgentUpdateParamsLlmFallback] = OMIT,
        deepgram_keywords: typing.Optional[AgentUpdateParamsDeepgramKeywords] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Agent:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[AgentUpdateParamsName]

        prompt : typing.Optional[AgentUpdateParamsPrompt]

        language : typing.Optional[AgentUpdateParamsLanguage]

        actions : typing.Optional[AgentUpdateParamsActions]

        voice : typing.Optional[AgentUpdateParamsVoice]

        initial_message : typing.Optional[AgentUpdateParamsInitialMessage]

        webhook : typing.Optional[AgentUpdateParamsWebhook]

        vector_database : typing.Optional[AgentUpdateParamsVectorDatabase]

        interrupt_sensitivity : typing.Optional[AgentUpdateParamsInterruptSensitivity]

        context_endpoint : typing.Optional[AgentUpdateParamsContextEndpoint]

        noise_suppression : typing.Optional[AgentUpdateParamsNoiseSuppression]

        endpointing_sensitivity : typing.Optional[AgentUpdateParamsEndpointingSensitivity]

        ivr_navigation_mode : typing.Optional[AgentUpdateParamsIvrNavigationMode]

        conversation_speed : typing.Optional[AgentUpdateParamsConversationSpeed]

        initial_message_delay : typing.Optional[AgentUpdateParamsInitialMessageDelay]

        openai_model_name_override : typing.Optional[AgentUpdateParamsOpenaiModelNameOverride]

        ask_if_human_present_on_idle : typing.Optional[AgentUpdateParamsAskIfHumanPresentOnIdle]

        openai_account_connection : typing.Optional[AgentUpdateParamsOpenaiAccountConnection]

        run_do_not_call_detection : typing.Optional[AgentUpdateParamsRunDoNotCallDetection]

        llm_fallback : typing.Optional[AgentUpdateParamsLlmFallback]

        deepgram_keywords : typing.Optional[AgentUpdateParamsDeepgramKeywords]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            Successful Response

        Examples
        --------
        import asyncio

        from vocode import AsyncVocode

        client = AsyncVocode(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.update_agent(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/agents/update",
            method="POST",
            params={
                "id": id,
            },
            json={
                "name": name,
                "prompt": prompt,
                "language": language,
                "actions": actions,
                "voice": voice,
                "initial_message": initial_message,
                "webhook": webhook,
                "vector_database": vector_database,
                "interrupt_sensitivity": interrupt_sensitivity,
                "context_endpoint": context_endpoint,
                "noise_suppression": noise_suppression,
                "endpointing_sensitivity": endpointing_sensitivity,
                "ivr_navigation_mode": ivr_navigation_mode,
                "conversation_speed": conversation_speed,
                "initial_message_delay": initial_message_delay,
                "openai_model_name_override": openai_model_name_override,
                "ask_if_human_present_on_idle": ask_if_human_present_on_idle,
                "openai_account_connection": openai_account_connection,
                "run_do_not_call_detection": run_do_not_call_detection,
                "llm_fallback": llm_fallback,
                "deepgram_keywords": deepgram_keywords,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Agent,
                    parse_obj_as(
                        type_=Agent,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
