from typing import List

from space_traders.client import Client
from space_traders.models import ApiError, Faction
from space_traders.utils import paginator


class FactionApi:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.base_endpoint = "/factions"

    async def get_faction(self, symbol: str) -> Faction | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Faction(**response["data"])

    async def list_factions(
        self, limit: int = 20, page: int = 1
    ) -> List[Faction] | ApiError:
        params = {"limit": limit, "page": page}
        response = await self.client.send(
            "get", self.base_endpoint, params=params
        )
        if "error" in response.keys():
            return ApiError(**response)
        return [Faction(**f) for f in response["data"]]

    async def list_all_factions(self) -> List[Faction] | ApiError:
        response = await paginator(self.client, "get", self.base_endpoint)
        if isinstance(response, ApiError):
            return response
        return [Faction(**f) for f in response]
