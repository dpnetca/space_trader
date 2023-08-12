from space_traders.space_traders import Client
from typing import List
from space_traders.models import ApiError, System
from space_traders.utils import paginator


class SystemApi:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.base_endpoint = "/systems"

    def list_systems(
        self, limit: int = 20, page: int = 1
    ) -> List[System] | ApiError:
        params = {"limit": limit, "page": page}
        endpoint = self.base_endpoint
        response = self.client.send("get", endpoint, params=params)
        if "error" in response.keys():
            return ApiError(**response)
        return [System(**s) for s in response["data"]]

    def list_all_systems(self) -> List[System] | ApiError:
        ships = paginator(self.client, "get", self.base_endpoint)
        if isinstance(ships, ApiError):
            return ApiError
        return [System(**s) for s in ships]

    def get_system(self, system_symbol: str) -> System | ApiError:
        endpoint = self.base_endpoint + f"/{system_symbol}"
        response = self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return System(**response["data"])
