from typing import List

from space_traders.client import Client
from space_traders.models import Agent, ApiError, Meta, ListAgents
from space_traders.utils import paginator


class AgentApi:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.base_endpoint = "/agents"

    async def get_my_agent(self) -> Agent | ApiError:
        """Get agent assigned to API Token

        Returns:
            Agent | ApiError: Agent details
        """
        response = await self.client.send("get", "/my/agent")
        if "error" in response.keys():
            return ApiError(**response)
        return Agent(**response["data"])

    async def get_agent(self, symbol: str) -> Agent | ApiError:
        """Get public agent details for passed in agent symbol

        Args:
            symbol (str): agent symbol

        Returns:
            Agent | ApiError: Public agent details
        """
        endpoint = self.base_endpoint + f"/{symbol}"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Agent(**response["data"])

    async def list_all_agents(self) -> List[Agent] | ApiError:
        """get a list of all agents public agent details

        Returns:
            List[Agent] | ApiError: list of public agent details
        """
        response = await paginator(self.client, "get", self.base_endpoint)
        if isinstance(response, ApiError):
            return response
        return [Agent(**a) for a in response]
