# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import VocodeEnvironment
from .resources.actions.client import ActionsClient, AsyncActionsClient
from .resources.agents.client import AgentsClient, AsyncAgentsClient
from .resources.calls.client import AsyncCallsClient, CallsClient
from .resources.numbers.client import AsyncNumbersClient, NumbersClient
from .resources.prompts.client import AsyncPromptsClient, PromptsClient
from .resources.usage.client import AsyncUsageClient, UsageClient
from .resources.voices.client import AsyncVoicesClient, VoicesClient
from .resources.webhooks.client import AsyncWebhooksClient, WebhooksClient


class Vocode:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: VocodeEnvironment = VocodeEnvironment.PRODUCTION,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx.Client(timeout=timeout),
        )
        self.numbers = NumbersClient(client_wrapper=self._client_wrapper)
        self.calls = CallsClient(client_wrapper=self._client_wrapper)
        self.usage = UsageClient(client_wrapper=self._client_wrapper)
        self.actions = ActionsClient(client_wrapper=self._client_wrapper)
        self.agents = AgentsClient(client_wrapper=self._client_wrapper)
        self.voices = VoicesClient(client_wrapper=self._client_wrapper)
        self.webhooks = WebhooksClient(client_wrapper=self._client_wrapper)
        self.prompts = PromptsClient(client_wrapper=self._client_wrapper)


class AsyncVocode:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: VocodeEnvironment = VocodeEnvironment.PRODUCTION,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx.AsyncClient(timeout=timeout),
        )
        self.numbers = AsyncNumbersClient(client_wrapper=self._client_wrapper)
        self.calls = AsyncCallsClient(client_wrapper=self._client_wrapper)
        self.usage = AsyncUsageClient(client_wrapper=self._client_wrapper)
        self.actions = AsyncActionsClient(client_wrapper=self._client_wrapper)
        self.agents = AsyncAgentsClient(client_wrapper=self._client_wrapper)
        self.voices = AsyncVoicesClient(client_wrapper=self._client_wrapper)
        self.webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)
        self.prompts = AsyncPromptsClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: VocodeEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
