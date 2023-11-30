# This file was auto-generated by Fern from our API Definition.

import typing

import httpx


class BaseClientWrapper:
    def __init__(self, *, token: typing.Union[str, typing.Callable[[], str]], base_url: str):
        self._token = token
        self._base_url = base_url

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "X-Fern-Language": "Python",
            "X-Fern-SDK-Name": "vocode-api",
            "X-Fern-SDK-Version": "0.0.28",
        }
        headers["Authorization"] = f"Bearer {self._get_token()}"
        return headers

    def _get_token(self) -> str:
        if isinstance(self._token, str):
            return self._token
        else:
            return self._token()

    def get_base_url(self) -> str:
        return self._base_url


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self, *, token: typing.Union[str, typing.Callable[[], str]], base_url: str, httpx_client: httpx.Client
    ):
        super().__init__(token=token, base_url=base_url)
        self.httpx_client = httpx_client


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self, *, token: typing.Union[str, typing.Callable[[], str]], base_url: str, httpx_client: httpx.AsyncClient
    ):
        super().__init__(token=token, base_url=base_url)
        self.httpx_client = httpx_client
