from space_traders.client import Client
from space_traders.models import Agent, ApiError
from typing import List


from space_traders.utils import paginator


class AgentApi:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.base_endpoint = "/agents"

    def get_my_agent(self) -> Agent | ApiError:
        r = self.client.send("get", "/my/agent")
        if "error" in r.keys():
            return ApiError(**r)
        return Agent(**r)

    def get_agent(self, symbol: str) -> Agent | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}"
        r = self.client.send("get", endpoint)
        if "error" in r.keys():
            return ApiError(**r)
        return Agent(**r)

    def list_agents(self, limit=20, page=1) -> List[Agent] | ApiError:
        params = {"limit": limit, "page": page}
        r = self.client.send("get", self.base_endpoint, params=params)
        if "error" in r.keys():
            return ApiError(**r)
        return [Agent(**a) for a in r["data"]]

    def list_all_agents(self) -> List[Agent] | ApiError:
        agents = paginator(self.client, "get", self.base_endpoint)
        return agents
