import logging

import httpx
from aiolimiter import AsyncLimiter


class Client:
    def __init__(self, token: str | None = None) -> None:
        self.token = token
        self.base_url = "https://api.spacetraders.io/v2"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.rate_limit = AsyncLimiter(1, 0.35)
        self.client = httpx.AsyncClient()

    async def send(
        self,
        method: str,
        endpoint: str,
        auth: bool = True,
        headers: dict | None = None,
        data: dict | None = None,
        **kwargs,
    ) -> dict:
        url = self.base_url + endpoint
        head = self.headers
        if auth:
            head["Authorization"] = f"Bearer {self.token}"
        if isinstance(headers, dict):
            head.update(headers)

        match method.lower():
            case "get":
                response = await self._get(url, headers=head, **kwargs)
            case "post":
                response = await self._post(
                    url, headers=head, data=data, **kwargs
                )

        if response.status_code == 204:
            response_data = {}
        else:
            response_data = response.json()

        if response.status_code == 429:
            # TODO handle rate limiting
            pass

        if "error" in response_data.keys():
            print(
                f"ERROR {response_data['error']['code']}: "
                f"{response_data['error']['message']}"
            )
        return response_data

    async def _get(
        self, url: str, headers: dict | None = None, **kwargs
    ) -> httpx.Response:
        r = await self.client.get(url, headers=headers, **kwargs)
        logging.info(r.content)
        return r

    async def _post(
        self,
        url: str,
        headers: dict | None = None,
        data: dict | None = None,
        **kwargs,
    ) -> httpx.Response:
        r = await self.client.post(url, headers=headers, json=data, **kwargs)
        logging.info(r.content)
        return r
