import json
from typing import List

from space_traders.client import Client
from space_traders.models import (
    AgentCargoTransaction,
    AgentFuelTransaction,
    AgentShipTransaction,
    ApiError,
    CooldownExtractionCargo,
    CooldownSurveys,
    Ship,
    ShipCargo,
    ShipCooldown,
    ShipNav,
    Survey,
)
from space_traders.utils import paginator


class ShipApi:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.base_endpoint = "/my/ships"

    async def get_ship_cargo(self, symbol: str) -> ShipCargo | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/cargo"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipCargo(**response["data"])

    async def get_ship_cooldown(
        self, symbol: str
    ) -> ShipCooldown | ApiError | dict:
        endpoint = self.base_endpoint + f"/{symbol}/cooldown"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        if "data" in response.keys():
            return ShipCooldown(**response["data"])
        return response

    async def dock_ship(self, symbol: str) -> ShipNav | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/dock"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipNav(**response["data"]["nav"])

    async def extract_resources(
        self, symbol: str, survey: Survey | None = None
    ) -> CooldownExtractionCargo | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/extract"
        data = None
        if survey:
            # this is ugly..is there  a better way?
            data = {"survey": json.loads(survey.model_dump_json())}
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return CooldownExtractionCargo(**response["data"])

    async def get_ship(self, symbol: str) -> Ship | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Ship(**response["data"])

    async def list_ships(
        self, limit: int = 20, page: int = 1
    ) -> List[Ship] | ApiError:
        params = {"limit": limit, "page": page}
        endpoint = self.base_endpoint
        response = await self.client.send("get", endpoint, params=params)
        if "error" in response.keys():
            return ApiError(**response)
        return [Ship(**s) for s in response["data"]]

    async def list_all_ships(self) -> List[Ship] | ApiError:
        response = await paginator(self.client, "get", self.base_endpoint)
        if isinstance(response, ApiError):
            return response
        return [Ship(**s) for s in response]

    async def navigate_ship(
        self, symbol: str, waypoint_symbol: str
    ) -> ShipNav | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/navigate"
        data = {"waypointSymbol": waypoint_symbol}
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipNav(**response["data"]["nav"])

    async def orbit_ship(self, symbol: str) -> ShipNav | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/orbit"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipNav(**response["data"]["nav"])

    async def purchase_ship(
        self, ship_type: str, waypoint_symbol: str
    ) -> AgentShipTransaction | ApiError:
        endpoint = self.base_endpoint
        data = {
            "shipType": ship_type,
            "waypointSymbol": waypoint_symbol,
        }
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentShipTransaction(**response["data"])

    async def refuel_ship(
        self, symbol: str
    ) -> AgentFuelTransaction | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/refuel"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentFuelTransaction(**response["data"])

    async def sell_cargo(
        self, symbol: str, item_symbol: str, units: int
    ) -> AgentCargoTransaction | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/sell"
        data = {"symbol": item_symbol, "units": units}
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentCargoTransaction(**response["data"])

    async def create_survey(self, symbol: str) -> CooldownSurveys | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/survey"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return CooldownSurveys(**response["data"])

    # following still need implementation
    async def ship_refine(self):
        raise NotImplemented

    async def create_chart(self):
        raise NotImplemented

    async def jettison_cargo(self):
        raise NotImplemented

    async def jump_ship(self):
        raise NotImplemented

    async def patch_ship_nav(self):
        raise NotImplemented

    async def warp_ship(self):
        raise NotImplemented

    async def scan_systems(self):
        raise NotImplemented

    async def scan_waypoints(self):
        raise NotImplemented

    async def scan_ships(self):
        raise NotImplemented

    async def purchase_cargo(self):
        raise NotImplemented

    async def transfer_cargo(self):
        raise NotImplemented

    async def negotiate_contract(self):
        raise NotImplemented

    async def get_mounts(self):
        raise NotImplemented

    async def install_mount(self):
        raise NotImplemented

    async def remove_mount(self):
        raise NotImplemented
