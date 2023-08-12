from space_traders.client import Client
from space_traders.models import Agent, ApiError
from typing import List


from space_traders.utils import paginator


class AgentApi:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.base_endpoint = "/agents"

    def get_me(self) -> Agent | ApiError:
        response = self.client.send("get", "/my/agent")
        if "error" in response.keys():
            return ApiError(**response)
        return Agent(**response)

    def get(self, symbol: str) -> Agent | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}"
        response = self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Agent(**response)

    def list(self, limit: int = 20, page: int = 1) -> List[Agent] | ApiError:
        params = {"limit": limit, "page": page}
        response = self.client.send("get", self.base_endpoint, params=params)
        if "error" in response.keys():
            return ApiError(**response)
        return [Agent(**a) for a in response["data"]]

    def list_all(self) -> List[Agent] | ApiError:
        agents = paginator(self.client, "get", self.base_endpoint)
        if isinstance(agents, ApiError):
            return ApiError
        return [Agent(**a) for a in agents]
