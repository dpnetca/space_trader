import asyncio
import logging

import httpx
from aiolimiter import AsyncLimiter

logger  = logging.getLogger("SpaceTrader")

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

    async def close(self):
        await self.client.aclose()

    async def send(
        self,
        method: str,
        endpoint: str,
        auth: bool = True,
        headers: dict | None = None,
        data: dict | None = None,
        handle_429=True,
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

        if response.status_code == 429 and handle_429:
            delay = response_data["error"]["data"]["retryAfter"]
            logger.warning(
                f"Rate Limit hit, automatic retry after {delay} seconds"
            )
            await asyncio.sleep(delay)
            return await self.send(
                method, endpoint, auth, headers, data, handle_429, **kwargs
            )

        if "error" in response_data.keys():
            logger.warning(
                f"ERROR {response_data['error']['code']}: "
                f"{response_data['error']['message']}"
            )
        return response_data

    async def _get(
        self, url: str, headers: dict | None = None, **kwargs
    ) -> httpx.Response:
        await self.rate_limit.acquire()
        r = await self.client.get(url, headers=headers, **kwargs)
        logger.debug(r.content)
        return r

    async def _post(
        self,
        url: str,
        headers: dict | None = None,
        data: dict | None = None,
        **kwargs,
    ) -> httpx.Response:
        await self.rate_limit.acquire()
        r = await self.client.post(url, headers=headers, json=data, **kwargs)
        logger.debug(r.content)
        return r
