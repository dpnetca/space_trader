from typing import List

from space_traders.client import Client
from space_traders.models import Agent, ApiError
from space_traders.utils import paginator


class AgentApi:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.base_endpoint = "/agents"

    async def get_my_agent(self) -> Agent | ApiError:
        response = await self.client.send("get", "/my/agent")
        if "error" in response.keys():
            return ApiError(**response)
        return Agent(**response)

    async def get_agent(self, symbol: str) -> Agent | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Agent(**response["agent"])

    async def list_agents(
        self, limit: int = 20, page: int = 1
    ) -> List[Agent] | ApiError:
        params = {"limit": limit, "page": page}
        response = await self.client.send(
            "get", self.base_endpoint, params=params
        )
        if "error" in response.keys():
            return ApiError(**response)
        return [Agent(**a) for a in response["data"]]

    async def list_all_agents(self) -> List[Agent] | ApiError:
        response = await paginator(self.client, "get", self.base_endpoint)
        if isinstance(response, ApiError):
            return response
        return [Agent(**a) for a in response]
