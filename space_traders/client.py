import asyncio
import logging
from typing import Callable
import httpx
import datetime

from aiolimiter import AsyncLimiter

log = logging.getLogger("SpaceTrader")


class Client:
    def __init__(
        self,
        token: str | None = None,
        log_func: Callable | None = None,
    ) -> None:
        self.token = token
        self.log_func = log_func

        self.base_url = "https://api.spacetraders.io/v2"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.limiter_requests = 1
        self.limiter_period = 0.34
        self.rate_limit = AsyncLimiter(
            self.limiter_requests, self.limiter_period
        )
        self.client = httpx.AsyncClient()
        self.timeout = 10
        self.timeout_exception_delay = 30

    async def close(self) -> None:
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
        head["x-request-timestamp"] = datetime.datetime.now(
            tz=datetime.UTC
        ).isoformat()
        timeout = kwargs.pop("timeout", self.timeout)
        match method.lower():
            case "get":
                response = await self._get(
                    url, headers=head, timeout=timeout, **kwargs
                )
            case "post":
                response = await self._post(
                    url, headers=head, data=data, timeout=timeout, **kwargs
                )

        if self.log_func:
            await self.log_func(response)

        try:
            response_data = response.json()
        except ValueError:
            response_data = {}

        if response.status_code >= 500:
            log.error(f"5xx SERVER Error caught: {response.content}")
            f"{self.timeout_exception_delay} seconds and retrying"
            await asyncio.sleep(self.timeout_exception_delay)
            return await self.send(
                method, endpoint, auth, headers, data, handle_429, **kwargs
            )

        if response.status_code == 429 and handle_429:
            delay = (
                response_data.get("error", {})
                .get("data", {})
                .get("retryAfter", 5)
            )
            log.warning(
                f"Rate Limit hit, automatic retry after {delay} seconds"
            )
            await asyncio.sleep(delay)
            return await self.send(
                method, endpoint, auth, headers, data, handle_429, **kwargs
            )

        if "error" in response_data.keys():
            log.warning(
                f"ERROR {response_data['error'].get('code')}: "
                f"{response_data['error'].get('message')}"
            )
        return response_data

    async def _get(
        self, url: str, headers: dict | None = None, **kwargs
    ) -> httpx.Response:
        await self.rate_limit.acquire()
        try:
            r = await self.client.get(url, headers=headers, **kwargs)
        except httpx.TimeoutException as e:
            log.error(
                f"TIMEOUT EXCEPTION caught on GET: {url}, sleeping"
                f"{self.timeout_exception_delay} seconds and retrying"
            )
            await asyncio.sleep(self.timeout_exception_delay)
            r = await self._get(url, headers=headers, **kwargs)

        log.debug(r.content)
        return r

    async def _post(
        self,
        url: str,
        headers: dict | None = None,
        data: dict | None = None,
        **kwargs,
    ) -> httpx.Response:
        await self.rate_limit.acquire()
        try:
            r = await self.client.post(
                url, headers=headers, json=data, **kwargs
            )
        except httpx.TimeoutException as e:
            log.error(
                f"TIMEOUT EXCEPTION caught on POST: {url}, sleeping"
                f"{self.timeout_exception_delay} seconds and retrying"
            )
            await asyncio.sleep(self.timeout_exception_delay)
            r = await self._post(url, headers, data, **kwargs)

        log.debug(r.content)
        return r
