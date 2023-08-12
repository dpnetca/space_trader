from space_traders.space_traders import Client
from typing import List
from space_traders.models import (
    ApiError,
    System,
    Waypoint,
    Market,
    Jumpgate,
    Shipyard,
)
from space_traders.utils import paginator


class SystemApi:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.base_endpoint = "/systems"

    # SYSTEM LEVEL #
    def get_system(self, system_symbol: str) -> System | ApiError:
        endpoint = self.base_endpoint + f"/{system_symbol}"
        response = self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return System(**response["data"])

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
        response = paginator(self.client, "get", self.base_endpoint)
        if isinstance(response, ApiError):
            return response
        return [System(**s) for s in response]

    # WAYPOINT LEVEL #
    def get_waypoint(
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
        response = self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Waypoint(**response["data"])

    def list_waypoints(
        self, system_symbol: str, limit=20, page=1
    ) -> List[Waypoint] | ApiError:
        params = {"limit": limit, "page": page}
        endpoint = self.base_endpoint + f"/{system_symbol}/waypoints"
        response = self.client.send("get", endpoint, params=params)
        if "error" in response.keys():
            return ApiError(**response)
        return [Waypoint(**w) for w in response["data"]]

    def list_all_waypoints(
        self, system_symbol: str
    ) -> List[Waypoint] | ApiError:
        endpoint = self.base_endpoint + f"/{system_symbol}/waypoints"
        response = paginator(self.client, "get", endpoint)
        if isinstance(response, ApiError):
            return response
        return [Waypoint(**s) for s in response]

    def get_market(
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
        response = self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Market(**response["data"])

    def get_jumpgate(
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
        response = self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Jumpgate(**response["data"])

    def get_shipyard(
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
        response = self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Shipyard(**response["data"])

    @staticmethod
    def _get_system_from_waypoint(waypoint: str) -> str:
        system = waypoint.split("-")[:2]
        return "-".join(system)
