from typing import List

from space_traders.models import (
    ApiError,
    Jumpgate,
    Market,
    Shipyard,
    System,
    Waypoint,
)
from space_traders.space_traders import Client
from space_traders.utils import paginator


class SystemApi:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.base_endpoint = "/systems"

    # SYSTEM LEVEL #
    async def get_system(self, system_symbol: str) -> System | ApiError:
        endpoint = self.base_endpoint + f"/{system_symbol}"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return System(**response["data"])

    async def list_all_systems(self) -> List[System] | ApiError:
        response = await paginator(self.client, "get", self.base_endpoint)
        if isinstance(response, ApiError):
            return response
        return [System(**s) for s in response]

    # WAYPOINT LEVEL #
    async def get_waypoint(
        self,
        waypoint_symbol: str,
        system_symbol: str | None = None,
    ) -> Waypoint | ApiError:
        if system_symbol is None:
            system_symbol = self._get_system_from_waypoint(waypoint_symbol)
        endpoint = (
            self.base_endpoint
            + f"/{system_symbol}/waypoints/{waypoint_symbol}"
        )
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Waypoint(**response["data"])

    async def list_all_waypoints(
        self, system_symbol: str
    ) -> List[Waypoint] | ApiError:
        endpoint = self.base_endpoint + f"/{system_symbol}/waypoints"
        response = await paginator(self.client, "get", endpoint)
        if isinstance(response, ApiError):
            return response
        return [Waypoint(**s) for s in response]

    async def get_market(
        self,
        waypoint_symbol: str,
        system_symbol: str | None = None,
    ) -> Market | ApiError:
        if system_symbol is None:
            system_symbol = self._get_system_from_waypoint(waypoint_symbol)
        endpoint = (
            self.base_endpoint
            + f"/{system_symbol}/waypoints/{waypoint_symbol}/market"
        )
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Market(**response["data"])

    async def get_jumpgate(
        self,
        waypoint_symbol: str,
        system_symbol: str | None = None,
    ) -> Jumpgate | ApiError:
        if system_symbol is None:
            system_symbol = self._get_system_from_waypoint(waypoint_symbol)
        endpoint = (
            self.base_endpoint
            + f"/{system_symbol}/waypoints/{waypoint_symbol}/jump-gate"
        )
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Jumpgate(**response["data"])

    async def get_shipyard(
        self,
        waypoint_symbol: str,
        system_symbol: str | None = None,
    ) -> Shipyard | ApiError:
        if system_symbol is None:
            system_symbol = self._get_system_from_waypoint(waypoint_symbol)
        endpoint = (
            self.base_endpoint
            + f"/{system_symbol}/waypoints/{waypoint_symbol}/shipyard"
        )
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Shipyard(**response["data"])

    @staticmethod
    def _get_system_from_waypoint(waypoint: str) -> str:
        system = waypoint.split("-")[:2]
        return "-".join(system)
