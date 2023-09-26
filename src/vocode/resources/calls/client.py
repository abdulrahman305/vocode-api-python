# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.call import Call
from ...types.call_page import CallPage
from ...types.create_call_request_agent import CreateCallRequestAgent
from ...types.create_call_request_on_machine_answer import CreateCallRequestOnMachineAnswer
from ...types.http_validation_error import HttpValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CallsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_calls(self, *, page: typing.Optional[int] = None, size: typing.Optional[int] = None) -> CallPage:
        """
        Parameters:
            - page: typing.Optional[int].

            - size: typing.Optional[int].
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/calls/list"),
            params=remove_none_from_dict({"page": page, "size": size}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CallPage, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_call(self, *, id: str) -> Call:
        """
        Parameters:
            - id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/calls"),
            params=remove_none_from_dict({"id": id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Call, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def end_call(self, *, id: str) -> Call:
        """
        Parameters:
            - id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/calls/end"),
            params=remove_none_from_dict({"id": id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Call, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_call(
        self,
        *,
        from_number: str,
        to_number: str,
        agent: CreateCallRequestAgent,
        on_machine_answer: typing.Optional[CreateCallRequestOnMachineAnswer] = OMIT,
        hipaa_compliant: typing.Optional[bool] = OMIT,
        context: typing.Optional[typing.Dict[str, str]] = OMIT,
    ) -> Call:
        """
        Parameters:
            - from_number: str.

            - to_number: str.

            - agent: CreateCallRequestAgent.

            - on_machine_answer: typing.Optional[CreateCallRequestOnMachineAnswer].

            - hipaa_compliant: typing.Optional[bool].

            - context: typing.Optional[typing.Dict[str, str]].
        """
        _request: typing.Dict[str, typing.Any] = {"from_number": from_number, "to_number": to_number, "agent": agent}
        if on_machine_answer is not OMIT:
            _request["on_machine_answer"] = on_machine_answer
        if hipaa_compliant is not OMIT:
            _request["hipaa_compliant"] = hipaa_compliant
        if context is not OMIT:
            _request["context"] = context
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/calls/create"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Call, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_recording(self, *, id: str) -> typing.Any:
        """
        Parameters:
            - id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/calls/recording"),
            params=remove_none_from_dict({"id": id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncCallsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_calls(self, *, page: typing.Optional[int] = None, size: typing.Optional[int] = None) -> CallPage:
        """
        Parameters:
            - page: typing.Optional[int].

            - size: typing.Optional[int].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/calls/list"),
            params=remove_none_from_dict({"page": page, "size": size}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CallPage, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_call(self, *, id: str) -> Call:
        """
        Parameters:
            - id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/calls"),
            params=remove_none_from_dict({"id": id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Call, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def end_call(self, *, id: str) -> Call:
        """
        Parameters:
            - id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/calls/end"),
            params=remove_none_from_dict({"id": id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Call, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_call(
        self,
        *,
        from_number: str,
        to_number: str,
        agent: CreateCallRequestAgent,
        on_machine_answer: typing.Optional[CreateCallRequestOnMachineAnswer] = OMIT,
        hipaa_compliant: typing.Optional[bool] = OMIT,
        context: typing.Optional[typing.Dict[str, str]] = OMIT,
    ) -> Call:
        """
        Parameters:
            - from_number: str.

            - to_number: str.

            - agent: CreateCallRequestAgent.

            - on_machine_answer: typing.Optional[CreateCallRequestOnMachineAnswer].

            - hipaa_compliant: typing.Optional[bool].

            - context: typing.Optional[typing.Dict[str, str]].
        """
        _request: typing.Dict[str, typing.Any] = {"from_number": from_number, "to_number": to_number, "agent": agent}
        if on_machine_answer is not OMIT:
            _request["on_machine_answer"] = on_machine_answer
        if hipaa_compliant is not OMIT:
            _request["hipaa_compliant"] = hipaa_compliant
        if context is not OMIT:
            _request["context"] = context
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/calls/create"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Call, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_recording(self, *, id: str) -> typing.Any:
        """
        Parameters:
            - id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/calls/recording"),
            params=remove_none_from_dict({"id": id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
